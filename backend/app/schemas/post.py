"""Pydantic schemas for blog post request/response bodies."""

import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    """Payload for creating a new post (POST /api/admin/posts).

    `slug` is optional — if omitted it will be auto-generated from `title`
    using python-slugify in the route handler.
    """

    title: str = Field(..., min_length=1, max_length=255, description="Post title")
    slug: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
        description="URL-safe slug (auto-generated from title if omitted)",
    )
    body_md: str | None = Field(default=None, description="Post body in Markdown")
    published: bool = Field(default=False, description="Whether the post is publicly visible")


class PostUpdate(BaseModel):
    """Payload for partial update of a post (PATCH /api/admin/posts/{id}).

    All fields are optional — only provided fields are updated.
    """

    title: str | None = Field(default=None, min_length=1, max_length=255)
    slug: str | None = Field(default=None, min_length=1, max_length=255)
    body_md: str | None = None
    published: bool | None = None
    published_at: datetime | None = None


class PostRead(BaseModel):
    """Full post record returned from the API."""

    id: uuid.UUID
    slug: str
    title: str
    body_md: str | None
    published: bool
    published_at: datetime | None
    created_at: datetime

    model_config = {"from_attributes": True}


class PostListItem(BaseModel):
    """Lightweight post summary used in listing endpoints.

    `excerpt` is the first 200 characters of `body_md`, stripped of Markdown
    syntax by the route handler before serialisation.
    """

    id: uuid.UUID
    slug: str
    title: str
    published_at: datetime | None
    excerpt: str | None = Field(default=None, description="Plain-text excerpt (~200 chars)")

    model_config = {"from_attributes": True}
