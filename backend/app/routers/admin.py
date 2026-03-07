"""Admin API endpoints — Bearer token authentication required."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from slugify import slugify
from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.signup import Signup
from app.routers.deps import get_db, verify_admin_token
from app.schemas.post import PostCreate, PostRead, PostUpdate
from app.schemas.signup import SignupRead

router = APIRouter(
    tags=["admin"],
    dependencies=[Depends(verify_admin_token)],
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _generate_unique_slug(db: Session, base_title: str, exclude_id: uuid.UUID | None = None) -> str:
    """Generate a URL-safe slug from a title, appending a numeric suffix on collision.

    Args:
        db: Active database session.
        base_title: The post title to slugify.
        exclude_id: Post UUID to exclude when checking for collisions (used on update).

    Returns:
        A unique slug string.
    """
    base = slugify(base_title)
    candidate = base
    counter = 2

    while True:
        query = db.query(Post).filter(Post.slug == candidate)
        if exclude_id:
            query = query.filter(Post.id != exclude_id)
        if not query.first():
            return candidate
        candidate = f"{base}-{counter}"
        counter += 1


# ---------------------------------------------------------------------------
# Signups
# ---------------------------------------------------------------------------


@router.get(
    "/signups",
    response_model=list[SignupRead],
    summary="List all signups",
)
def list_signups(db: Session = Depends(get_db)) -> list[SignupRead]:
    """Return all signup records sorted by created_at descending."""
    return db.query(Signup).order_by(Signup.created_at.desc()).all()  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Posts
# ---------------------------------------------------------------------------


@router.get(
    "/posts",
    response_model=list[PostRead],
    summary="List all posts (including unpublished)",
)
def list_all_posts(db: Session = Depends(get_db)) -> list[PostRead]:
    """Return all posts (published and draft) sorted by created_at descending.

    Used by the admin interface to show the full post list regardless of
    published status. Public endpoint only returns published posts.
    """
    return db.query(Post).order_by(Post.created_at.desc()).all()  # type: ignore[return-value]


@router.get(
    "/posts/{post_id}",
    response_model=PostRead,
    summary="Get a single post by ID (including unpublished)",
)
def get_post_by_id(post_id: uuid.UUID, db: Session = Depends(get_db)) -> PostRead:
    """Return any post by ID regardless of published status.

    Used by the admin edit page. Returns 404 if not found.
    """
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found.",
        )
    return post  # type: ignore[return-value]


@router.post(
    "/posts",
    response_model=PostRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new post",
)
def create_post(payload: PostCreate, db: Session = Depends(get_db)) -> PostRead:
    """Create a new blog post.

    If no slug is provided it is auto-generated from the title.
    Slug collisions are resolved by appending a numeric suffix (-2, -3, …).
    If published is True on creation, published_at is set to now.
    """
    if payload.slug:
        # Caller supplied a slug — still check for collisions
        slug = payload.slug
        if db.query(Post).filter(Post.slug == slug).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A post with slug '{slug}' already exists.",
            )
    else:
        slug = _generate_unique_slug(db, payload.title)

    published_at: datetime | None = None
    if payload.published:
        published_at = datetime.now(timezone.utc)

    post = Post(
        slug=slug,
        title=payload.title,
        body_md=payload.body_md,
        published=payload.published,
        published_at=published_at,
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post  # type: ignore[return-value]


@router.patch(
    "/posts/{post_id}",
    response_model=PostRead,
    summary="Update a post",
)
def update_post(
    post_id: uuid.UUID,
    payload: PostUpdate,
    db: Session = Depends(get_db),
) -> PostRead:
    """Partially update a blog post.

    Only fields explicitly provided in the request body are changed.
    If published is being set to True for the first time (published_at is
    currently None), published_at is automatically set to now().
    """
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found.",
        )

    update_data = payload.model_dump(exclude_unset=True)

    # Handle slug uniqueness if slug is being changed
    if "slug" in update_data and update_data["slug"] != post.slug:
        if db.query(Post).filter(Post.slug == update_data["slug"], Post.id != post_id).first():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A post with slug '{update_data['slug']}' already exists.",
            )

    # Auto-set published_at on first publish
    if update_data.get("published") is True and post.published_at is None:
        update_data.setdefault("published_at", datetime.now(timezone.utc))

    for field, value in update_data.items():
        setattr(post, field, value)

    db.commit()
    db.refresh(post)
    return post  # type: ignore[return-value]
