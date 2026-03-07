"""Pydantic schemas for signup request/response bodies."""

import uuid
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, Field


class ProfileType(str, Enum):
    """Allowed values for the profile_type field."""

    user = "user"
    caregiver = "caregiver"
    professional = "professional"
    other = "other"


class SignupCreate(BaseModel):
    """Payload for creating a new signup (POST /api/signups)."""

    email: EmailStr = Field(..., description="Contact email address")
    first_name: str = Field(..., min_length=1, max_length=100, description="First name")
    profile_type: ProfileType = Field(..., description="How the person relates to the product")


class SignupRead(BaseModel):
    """Full signup record returned from the API."""

    id: uuid.UUID
    email: str
    first_name: str
    profile_type: ProfileType
    created_at: datetime

    model_config = {"from_attributes": True}
