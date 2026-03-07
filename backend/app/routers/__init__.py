"""Routers package — exports public and admin APIRouter instances."""

from app.routers.admin import router as admin_router
from app.routers.public import router as public_router

__all__ = ["public_router", "admin_router"]
