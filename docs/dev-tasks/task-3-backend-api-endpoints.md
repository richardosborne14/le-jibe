# Task 3: Backend API Endpoints

**Status:** Not started | **Target Confidence:** 9/10

**Input:** Task 2 output (FastAPI scaffold, models, schemas), ROADMAP.md  
**Output:** All 6 API endpoints working and testable via Swagger  
**Estimated Time:** 1–2 sessions (~90 min)

---

## Subtasks

- **3.1** — `POST /api/signups` — create signup, validate email, deduplicate
- **3.2** — `GET /api/posts` — list published posts (title, slug, published_at, excerpt)
- **3.3** — `GET /api/posts/{slug}` — single post (full body)
- **3.4** — `GET /api/admin/signups` — list all signups (admin-only, token auth)
- **3.5** — `POST /api/admin/posts` — create post (admin-only)
- **3.6** — `PATCH /api/admin/posts/{id}` — update/publish post (admin-only)

---

## Cline Prompt

```
Can we please plan task 3 — Backend API Endpoints?

Reference:
- README.md (all logic in FastAPI, tech stack)
- ROADMAP.md (subtasks 3.1–3.6)
- CLAUDE_RULES.md
- Existing backend/ code from Task 2 (models, schemas, DB session)

We need 6 endpoints across 2 routers:

Public router (app/routers/public.py):
1. POST /api/signups — accepts {first_name, email, profile_type}, validates email format, returns 409 if email exists, 201 on success
2. GET /api/posts — returns list of published posts only, sorted by published_at desc, each with title, slug, published_at, excerpt (first 200 chars of body_md)
3. GET /api/posts/{slug} — returns full post by slug, 404 if not found or not published

Admin router (app/routers/admin.py):
4. GET /api/admin/signups — returns all signups, sorted by created_at desc
5. POST /api/admin/posts — creates a new post (auto-generate slug from title)
6. PATCH /api/admin/posts/{id} — update any field, if published is set to true and published_at is null, set published_at to now()

Admin auth: simple Bearer token from env var ADMIN_TOKEN. Use a FastAPI dependency.

All endpoints should have proper error handling and return consistent JSON shapes.
```

---

## Confidence Criteria

- [ ] All 6 endpoints return correct status codes
- [ ] Email deduplication works (409 on duplicate signup)
- [ ] Email validation rejects malformed addresses
- [ ] Admin endpoints reject requests without valid token (401)
- [ ] Admin endpoints reject requests with wrong token (401)
- [ ] Published posts list excludes unpublished posts
- [ ] Slug auto-generation works and handles duplicates (append `-2`, `-3`, etc.)
- [ ] PATCH correctly sets `published_at` on first publish
- [ ] All testable via Swagger UI at `/docs`

---

## Decisions to Watch For

- **Email validation:** Use Pydantic's `EmailStr` — don't roll your own regex
- **Excerpt generation:** Strip markdown before truncating, or just truncate raw? Raw is fine for MVP
- **Slug collisions:** What if two posts have the same title? Append a number suffix
- **Admin token:** Single static token from env is fine for MVP. No user accounts needed yet
- **Pagination:** Not needed for MVP (we won't have hundreds of posts or signups). Add later if needed

---

## Notes

This is the most critical backend task. After this, the API is complete for MVP. Every endpoint should be demonstrable in Swagger. Consider writing a quick test script or using the Swagger UI to verify all 6 endpoints work end-to-end.

**Depends on:** Task 2  
**Blocks:** Task 5, Task 6, Task 7
