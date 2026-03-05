# Roadmap

## Phase 1: MVP — Interest Capture
**Goal:** Live site that captures interest signups and publishes blog posts.  
**Target:** 2–3 weeks of focused sessions.

---

### Task 1: Infrastructure & Repo Setup ✅
- [x] 1.1 — Initialise monorepo structure (frontend/, backend/, nginx/, docker-compose.yml, .env.example)
- [x] 1.2 — Write base docker-compose.yml (postgres, backend, frontend, nginx services)
- [x] 1.3 — Configure nginx for local dev reverse proxy (frontend on /*, backend on /api/*)
- [x] 1.4 — Hetzner VPS provisioning (Ubuntu 24, Docker, Docker Compose, SSH key)
- [x] 1.5 — Production nginx config + Let's Encrypt SSL for le-jibe.com

### Task 2: Database & Backend Foundation
- [ ] 2.1 — FastAPI project scaffold (app structure, config, DB session, health endpoint)
- [ ] 2.2 — PostgreSQL schema: `signups` table (id, email, first_name, profile_type, created_at)
- [ ] 2.3 — PostgreSQL schema: `posts` table (id, slug, title, body_md, published, published_at, created_at)
- [ ] 2.4 — Alembic migrations for both tables
- [ ] 2.5 — Pydantic schemas for signups and posts

### Task 3: Backend API Endpoints
- [ ] 3.1 — `POST /api/signups` — create signup, validate email, deduplicate
- [ ] 3.2 — `GET /api/posts` — list published posts (title, slug, published_at, excerpt)
- [ ] 3.3 — `GET /api/posts/{slug}` — single post (full body)
- [ ] 3.4 — `GET /api/admin/signups` — list all signups (admin-only, token auth)
- [ ] 3.5 — `POST /api/admin/posts` — create post (admin-only)
- [ ] 3.6 — `PATCH /api/admin/posts/{id}` — update / publish post (admin-only)

### Task 4: SvelteKit Frontend — Landing Page
- [ ] 4.1 — SvelteKit project scaffold (routing, fonts, CSS variables matching brand)
- [ ] 4.2 — Nav component (fixed, logo, links, CTA button)
- [ ] 4.3 — Hero section (headline, stats, YouTube embed placeholder)
- [ ] 4.4 — Story section (JB narrative, photo slot)
- [ ] 4.5 — Features grid (3 cards: base, seat, joystick)
- [ ] 4.6 — Ticker / marquee strip
- [ ] 4.7 — Footer

### Task 5: Signup Form (wired to API)
- [ ] 5.1 — Signup form component (first name, email, profile type select)
- [ ] 5.2 — Wire to `POST /api/signups` with loading/success/error states
- [ ] 5.3 — Success confirmation UI (no page reload)

### Task 6: Blog (public)
- [ ] 6.1 — `/blog` listing page (cards: title, date, excerpt)
- [ ] 6.2 — `/blog/[slug]` post page (rendered markdown, back link)
- [ ] 6.3 — Markdown rendering (marked.js or similar, styled to brand)

### Task 7: Admin
- [ ] 7.1 — `/admin` login page (static token, no user accounts yet)
- [ ] 7.2 — `/admin/signups` — table view of all signups, CSV export button
- [ ] 7.3 — `/admin/posts` — list posts with published status
- [ ] 7.4 — `/admin/posts/new` — write + preview + publish form
- [ ] 7.5 — `/admin/posts/[id]/edit` — edit existing post

### Task 8: Deployment & Go-Live
- [ ] 8.1 — Production .env (secrets, DB credentials, admin token)
- [ ] 8.2 — Full docker compose up on Hetzner, smoke test all endpoints
- [ ] 8.3 — DNS: point lejibe.fr to Hetzner, SSL cert via certbot
- [ ] 8.4 — Verify signup form end-to-end on production
- [ ] 8.5 — Write first blog post from admin panel

---

## Phase 2: Product & Ordering
*(Start after MVP validates interest and LPPR/pricing strategy is clearer)*

- Product page with configuration (seat type, options)
- Alma BNPL integration (2x/3x/4x first; 10x/12x once approved)
- Order form and confirmation email
- Customer order status page
- Stripe fallback for direct payment

---

## Phase 3: Operations & Compliance
*(Start after first orders)*

- Production tracking (per-order build status)
- LPPR reimbursement workflow support
- Prescription upload / ergothérapeute referral tracking
- MDPH/Agefiph funding documentation tooling
- Multi-language (FR + EN)

---

## Deferred (no timeline)

| Feature | Reason deferred |
|---|---|
| Customer accounts / login | Not needed for interest capture |
| Inventory management | Too early — small batch production |
| Live chat | Manual email is fine at this scale |
| Analytics dashboard | Basic server logs sufficient for MVP |
