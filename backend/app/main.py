"""FastAPI application entry point.

Registers middleware, lifespan events, and routers.
Route handlers live in app/routers/ — see Task 3.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.db import engine  # noqa: F401 — imported to ensure engine is initialised
from app.routers import admin_router, public_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan: startup and shutdown hooks."""
    # Nothing to do on startup for now — Alembic handles migrations separately.
    # Add any startup logic here (e.g. warm up caches) in future tasks.
    yield
    # Shutdown: dispose connection pool cleanly
    engine.dispose()


app = FastAPI(
    title="Le Jibé API",
    description="Backend API for le-jibe.com — interest capture, blog, admin.",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(public_router, prefix="/api")
app.include_router(admin_router, prefix="/api/admin")


@app.get("/api/health", tags=["meta"])
def health() -> dict:
    """Liveness check — returns 200 when the service is up."""
    return {"status": "ok"}
