# Task 2: Database & Backend Foundation

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 1 output (working Docker environment), ROADMAP.md  
**Output:** FastAPI scaffold with health endpoint, PostgreSQL schemas for `signups` and `posts`, Alembic migrations, Pydantic models  
**Estimated Time:** 1 session (~60–90 min)

---

## Subtasks

- **2.1** — FastAPI project scaffold (app structure, config, DB session, health endpoint)
- **2.2** — PostgreSQL schema: `signups` table (`id`, `email`, `first_name`, `profile_type`, `created_at`)
- **2.3** — PostgreSQL schema: `posts` table (`id`, `slug`, `title`, `body_md`, `published`, `published_at`, `created_at`)
- **2.4** — Alembic migrations for both tables
- **2.5** — Pydantic schemas for signups and posts

---

## Cline Prompt

```
Can we please plan task 2 — Database & Backend Foundation?

Reference:
- README.md (tech stack, the rule about all logic in FastAPI)
- ROADMAP.md (subtasks 2.1–2.5)
- CLAUDE_RULES.md

We need:
1. FastAPI project inside backend/ with clean structure:
   - app/main.py (FastAPI app, CORS, lifespan)
   - app/config.py (settings from env vars)
   - app/db.py (SQLAlchemy engine, session, Base)
   - app/models/ (SQLAlchemy models)
   - app/schemas/ (Pydantic models)
   - app/routers/ (will be populated in Task 3)
2. Health endpoint: GET /api/health returns {"status": "ok"}
3. Two tables:
   - signups: id (UUID), email (unique), first_name, profile_type (enum: user/caregiver/professional/other), created_at
   - posts: id (UUID), slug (unique), title, body_md (text), published (bool default false), published_at (nullable), created_at
4. Alembic setup with initial migration creating both tables
5. Pydantic schemas: SignupCreate, SignupRead, PostCreate, PostUpdate, PostRead, PostListItem

After completion: docker compose up should boot, and GET /api/health should return 200.
```

---

## Confidence Criteria

- [ ] FastAPI app starts cleanly inside Docker
- [ ] `GET /api/health` returns `{"status": "ok"}`
- [ ] Alembic migration runs and creates both tables
- [ ] Pydantic schemas validate correctly (test with example data)
- [ ] SQLAlchemy models match the schema design
- [ ] DB session properly opens and closes (no connection leaks)
- [ ] Config reads all values from environment variables

---

## Decisions to Watch For

- **UUIDs vs auto-increment:** UUIDs are better for a public API — no enumeration
- **Slug generation:** Auto-generate from title, or require manual? Auto-generate with override option is cleanest
- **profile_type:** Use a Python Enum mapped to a Postgres enum, or just a varchar with validation? Enum is safer
- **Timestamps:** Use `server_default=func.now()` so Postgres handles it, not Python

---

## Notes

No API endpoints beyond health in this task — that's Task 3. Keep the focus tight: scaffold, models, schemas, migrations. Everything should be testable by just booting the containers and hitting `/api/health`.

**Depends on:** Task 1  
**Blocks:** Task 3
