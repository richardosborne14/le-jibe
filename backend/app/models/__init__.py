"""Models package — import all models here so Alembic can discover them via Base.metadata."""

from app.models.post import Post  # noqa: F401
from app.models.signup import Signup  # noqa: F401

__all__ = ["Signup", "Post"]
