"""SQLAlchemy model for the signups table."""

import uuid

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base

# PostgreSQL-native enum — enforced at DB level
ProfileTypeEnum = Enum(
    "user",
    "caregiver",
    "professional",
    "other",
    name="profile_type_enum",
)


class Signup(Base):
    """Stores interest-capture signups from the landing page form."""

    __tablename__ = "signups"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    profile_type: Mapped[str] = mapped_column(ProfileTypeEnum, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
