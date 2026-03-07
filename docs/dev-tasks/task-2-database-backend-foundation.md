# Task 2: Database & Backend Foundation

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 1 output (working Docker environment), ROADMAP.md  
**Output:** FastAPI scaffold with health endpoint, PostgreSQL schemas for `signups`, `posts`, and `user_profiles`, Alembic migrations, Pydantic models  
**Estimated Time:** 1 session (~60–90 min)

---

## Subtasks

- **2.1** — FastAPI project scaffold (app structure, config, DB session, health endpoint)
- **2.2** — PostgreSQL schema: `signups` table (`id`, `email`, `first_name`, `profile_type`, `created_at`, `updated_at`)
- **2.3** — PostgreSQL schema: `posts` table (`id`, `slug`, `title`, `body_md`, `published`, `published_at`, `created_at`, `updated_at`)
- **2.4** — PostgreSQL schema: `user_profiles` table (`id`, `signup_id` FK, `disability_type`, `trunk_stability`, `transfer_method`, `hand_function`, `current_chair`, `car_loading`, `consent_given_at`, `created_at`, `updated_at`)
- **2.5** — Alembic migrations for all three tables
- **2.6** — Pydantic schemas for signups, posts, and user profiles

---

## Cline Prompt

```
Can we please plan task 2 — Database & Backend Foundation?

Reference:
- README.md (tech stack, the rule about all logic in FastAPI)
- ROADMAP.md (subtasks 2.1–2.6)
- .clinerules

We need:
1. FastAPI project inside backend/ with clean structure:
   - app/main.py (FastAPI app, CORS, lifespan)
   - app/config.py (settings from env vars)
   - app/db.py (SQLAlchemy engine, session, Base)
   - app/models/ (SQLAlchemy models)
   - app/schemas/ (Pydantic models)
   - app/routers/ (will be populated in Task 3)
2. Health endpoint: GET /api/health returns {"status": "ok"}
3. Three tables:
   - signups: id (UUID), email (unique), first_name, profile_type (enum: user/caregiver/professional/other), created_at, updated_at
   - posts: id (UUID), slug (unique), title, body_md (text), published (bool default false), published_at (nullable), created_at, updated_at
   - user_profiles: id (UUID), signup_id (FK → signups.id, nullable — profile can be created before email signup confirmed), disability_type (varchar, free text), trunk_stability (enum: oui/partiellement/non), transfer_method (enum: glissé_autonome/planche_transfert/aide_tierce), hand_function (enum: complète_deux_mains/limitée/une_main), current_chair (enum: manuel_actif/manuel_standard/électrique/autre), car_loading (enum: seul/avec_aide/non_concerné), consent_given_at (timestamp, required — no profile row without this), created_at, updated_at
4. Alembic setup with initial migration creating all three tables
5. Pydantic schemas:
   - SignupCreate, SignupRead
   - PostCreate, PostUpdate, PostRead, PostListItem
   - UserProfileCreate, UserProfileRead (consent field validated as required)

Rules:
- UUID primary keys on all tables
- created_at and updated_at on all tables (server_default + onupdate)
- Foreign keys enforced
- user_profiles.consent_given_at must be non-null — enforce at both Pydantic and DB level

After completion: docker compose up should boot, and GET /api/health should return 200.
```

---

## Confidence Criteria

- [ ] FastAPI app starts cleanly inside Docker
- [ ] `GET /api/health` returns `{"status": "ok"}`
- [ ] Alembic migration runs and creates all three tables
- [ ] `user_profiles.consent_given_at` is non-nullable at the DB level
- [ ] FK from `user_profiles.signup_id` → `signups.id` enforced
- [ ] Pydantic schemas validate correctly (test with example data)
- [ ] SQLAlchemy models match the schema design
- [ ] DB session properly opens and closes (no connection leaks)
- [ ] Config reads all values from environment variables
- [ ] All tables have `created_at` and `updated_at` timestamps

---

## Decisions to Watch For

- **UUIDs vs auto-increment:** UUIDs are better for a public API — no enumeration
- **Slug generation:** Auto-generate from title, or require manual? Auto-generate with override option is cleanest
- **profile_type:** Use a Python Enum mapped to a Postgres enum, or just a varchar with validation? Enum is safer
- **Timestamps:** Use `server_default=func.now()` so Postgres handles it, not Python
- **user_profiles signup_id:** Nullable FK — a user can start building a profile in chat before they've submitted the signup form. The profile can be linked retrospectively when they provide their email
- **Health data enums:** Keep as Python Enum types for strict validation — refuse unknown values

---

## Notes

No API endpoints beyond health in this task — that's Task 3. The `user_profiles` table holds RGPD-sensitive health data (Article 9 GDPR) — the `consent_given_at` column is the critical control. No row should ever exist without it. Enforce this at the schema level, not just in application code.

**Depends on:** Task 1  
**Blocks:** Task 3
