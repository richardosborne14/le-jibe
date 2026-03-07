# Task 3: Backend API Endpoints

**Status:** Not started | **Target Confidence:** 9/10

**Input:** Task 2 output (FastAPI scaffold, models, schemas), ROADMAP.md  
**Output:** All API endpoints working and testable via Swagger  
**Estimated Time:** 1–2 sessions (~90 min)

---

## Subtasks

- **3.1** — `POST /api/signups` — create signup, validate email, deduplicate
- **3.2** — `POST /api/profiles` — create/update disability profile (requires RGPD consent flag)
- **3.3** — `GET /api/posts` — list published posts (title, slug, published_at, excerpt)
- **3.4** — `GET /api/posts/{slug}` — single post (full body)
- **3.5** — `GET /api/admin/signups` — list all signups with profile data (admin-only, token auth)
- **3.6** — `POST /api/admin/posts` — create post (admin-only)
- **3.7** — `PATCH /api/admin/posts/{id}` — update / publish post (admin-only)
- **3.8** — `GET /api/admin/signups/export` — CSV export of signups + profiles (admin-only)

---

## Cline Prompt

```
Can we please plan task 3 — Backend API Endpoints?

Reference:
- README.md (all logic in FastAPI, tech stack)
- ROADMAP.md (subtasks 3.1–3.8)
- .clinerules
- Existing backend/ code from Task 2 (models, schemas, DB session)

We need 8 endpoints across 2 routers:

Public router (app/routers/public.py):
1. POST /api/signups
   - Accepts {first_name, email, profile_type}
   - Validates email format (Pydantic EmailStr)
   - Returns 409 if email already exists
   - Returns 201 on success with the created signup

2. POST /api/profiles
   - Accepts {email, consent: true, profile: {disability_type, trunk_stability, transfer_method, hand_function, current_chair, car_loading}}
   - Requires consent: true — return 422 if missing or false
   - Links to signup via email if signup exists, otherwise creates orphaned profile
   - Upserts: if a profile already exists for this email, update it
   - Sets consent_given_at to current timestamp

3. GET /api/posts
   - Returns list of published posts only, sorted by published_at desc
   - Each item: title, slug, published_at, excerpt (first 200 chars of body_md)

4. GET /api/posts/{slug}
   - Returns full post by slug
   - 404 if not found or not published

Admin router (app/routers/admin.py):
5. GET /api/admin/signups
   - Returns all signups sorted by created_at desc
   - Include joined profile data if it exists (nullable profile fields)

6. POST /api/admin/posts
   - Creates a new post (auto-generate slug from title)
   - Handles slug collisions by appending -2, -3, etc.

7. PATCH /api/admin/posts/{id}
   - Update any field
   - If published is set to true and published_at is null, set published_at to now()

8. GET /api/admin/signups/export
   - Returns CSV of all signups with their profile data (if any)
   - Columns: id, email, first_name, profile_type, created_at, disability_type, trunk_stability, transfer_method, hand_function, current_chair, car_loading, consent_given_at
   - Content-Type: text/csv
   - Content-Disposition: attachment; filename="signups.csv"

Admin auth: simple Bearer token from env var ADMIN_TOKEN. Use a FastAPI dependency.

All endpoints should have proper error handling and return consistent JSON shapes.
```

---

## Confidence Criteria

- [ ] All 8 endpoints return correct status codes
- [ ] Email deduplication works (409 on duplicate signup)
- [ ] Email validation rejects malformed addresses
- [ ] `POST /api/profiles` returns 422 if `consent` is missing or false
- [ ] `POST /api/profiles` correctly upserts (creates or updates)
- [ ] Admin endpoints reject requests without valid token (401)
- [ ] Admin endpoints reject requests with wrong token (401)
- [ ] Published posts list excludes unpublished posts
- [ ] Slug auto-generation works and handles duplicates (append `-2`, `-3`, etc.)
- [ ] `PATCH` correctly sets `published_at` on first publish
- [ ] CSV export returns valid CSV with correct columns
- [ ] Profile data included in signups list response (nullable join)
- [ ] All testable via Swagger UI at `/docs`

---

## Decisions to Watch For

- **Email validation:** Use Pydantic's `EmailStr` — don't roll your own regex
- **Excerpt generation:** Strip markdown before truncating, or just truncate raw? Raw is fine for MVP
- **Slug collisions:** What if two posts have the same title? Append a number suffix
- **Admin token:** Single static token from env is fine for MVP. No user accounts needed yet
- **Pagination:** Not needed for MVP (we won't have hundreds of posts or signups). Add later if needed
- **CSV encoding:** UTF-8 with BOM (`utf-8-sig`) for French characters — Excel handles this correctly
- **Profile consent:** Never store profile data without `consent_given_at` — enforce this in the router, not just the model

---

## Notes

This is the most critical backend task. After this, the API is complete for MVP. Every endpoint should be demonstrable in Swagger. Pay particular attention to `POST /api/profiles` — it handles RGPD-sensitive health data and the consent gate must be airtight. The CSV export should include profile data columns even if null (so the spreadsheet headers are consistent).

**Depends on:** Task 2  
**Blocks:** Task 5, Task 6, Task 7
