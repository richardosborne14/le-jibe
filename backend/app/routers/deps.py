"""Shared FastAPI dependencies used across routers."""

from typing import Generator

from fastapi import Header, HTTPException, status
from sqlalchemy.orm import Session

from app.config import settings
from app.db import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """Yield a database session and ensure it is closed after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_admin_token(authorization: str | None = Header(default=None)) -> None:
    """Validate the Bearer token for admin-only endpoints.

    Raises 401 if the header is missing or the token does not match
    the configured ADMIN_TOKEN environment variable.
    """
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or token != settings.admin_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or incorrect token",
            headers={"WWW-Authenticate": "Bearer"},
        )
