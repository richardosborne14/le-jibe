"""Database engine, session factory, and declarative base.

Usage:
    - Import `Base` in models so they register with the metadata.
    - Use `get_db` as a FastAPI dependency to obtain a session per request.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Detect stale connections before use
    pool_size=5,
    max_overflow=10,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Shared declarative base for all SQLAlchemy models."""
    pass


def get_db():
    """FastAPI dependency that yields a DB session and closes it when done."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
