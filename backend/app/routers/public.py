"""Public API endpoints — no authentication required."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.post import Post
from app.models.signup import Signup
from app.routers.deps import get_db
from app.schemas.post import PostListItem, PostRead
from app.schemas.signup import SignupCreate, SignupRead

router = APIRouter(tags=["public"])


# ---------------------------------------------------------------------------
# Signups
# ---------------------------------------------------------------------------


@router.post(
    "/signups",
    response_model=SignupRead,
    status_code=status.HTTP_201_CREATED,
    summary="Register interest",
)
def create_signup(payload: SignupCreate, db: Session = Depends(get_db)) -> SignupRead:
    """Create a new signup record.

    Returns 409 if the email address is already registered.
    Email format is validated by Pydantic (EmailStr).
    """
    existing = db.query(Signup).filter(Signup.email == payload.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email address is already registered.",
        )

    signup = Signup(
        email=payload.email,
        first_name=payload.first_name,
        profile_type=payload.profile_type.value,
    )
    db.add(signup)
    db.commit()
    db.refresh(signup)
    return signup  # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Posts
# ---------------------------------------------------------------------------


@router.get(
    "/posts",
    response_model=list[PostListItem],
    summary="List published posts",
)
def list_posts(db: Session = Depends(get_db)) -> list[PostListItem]:
    """Return all published posts sorted by published_at descending.

    Each item includes a plain-text excerpt (first 200 chars of body_md).
    """
    posts = (
        db.query(Post)
        .filter(Post.published.is_(True))
        .order_by(Post.published_at.desc())
        .all()
    )

    result: list[PostListItem] = []
    for post in posts:
        excerpt: str | None = None
        if post.body_md:
            # Raw truncation — no markdown stripping for MVP
            excerpt = post.body_md[:200]
        result.append(
            PostListItem(
                id=post.id,
                slug=post.slug,
                title=post.title,
                published_at=post.published_at,
                excerpt=excerpt,
            )
        )
    return result


@router.get(
    "/posts/{slug}",
    response_model=PostRead,
    summary="Get a published post by slug",
)
def get_post(slug: str, db: Session = Depends(get_db)) -> PostRead:
    """Return a single published post by slug.

    Returns 404 if the post does not exist or is not published.
    """
    post = (
        db.query(Post)
        .filter(Post.slug == slug, Post.published.is_(True))
        .first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found.",
        )
    return post  # type: ignore[return-value]
