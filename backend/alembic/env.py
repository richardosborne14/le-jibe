"""Alembic environment configuration.

Reads the database URL from app settings so there's one source of truth.
All models are imported via app.models so autogenerate can detect them.
"""

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool

from alembic import context

# ---------------------------------------------------------------------------
# Alembic config object — provides access to alembic.ini values
# ---------------------------------------------------------------------------
config = context.config

# Interpret the config file for Python logging, if present.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ---------------------------------------------------------------------------
# Import app metadata — models MUST be imported before target_metadata is set
# so SQLAlchemy's mapper registry knows about them.
# ---------------------------------------------------------------------------
from app.config import settings  # noqa: E402
from app.db import Base  # noqa: E402
import app.models  # noqa: E402, F401 — registers Signup + Post on Base.metadata

target_metadata = Base.metadata

# Override the sqlalchemy.url with the value from our settings rather than
# hard-coding it in alembic.ini (which would duplicate/diverge from .env).
config.set_main_option("sqlalchemy.url", settings.database_url)


# ---------------------------------------------------------------------------
# Migration helpers
# ---------------------------------------------------------------------------

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    Emits migration SQL to stdout rather than executing it against a live DB.
    Useful for generating SQL scripts for review before applying.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode against a live database connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
