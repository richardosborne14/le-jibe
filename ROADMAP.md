# Roadmap

## Phase 1: Landing Page + Community + Chat Assistant
**Goal:** Live site that captures interest, builds community, and lets visitors chat with an AI assistant that knows everything about Le Jibé.
**Target:** Live well before September 2026. Start now, iterate continuously.

---

### Task 1: Infrastructure & Repo Setup
- [ ] 1.1 — Initialise monorepo structure (frontend/, backend/, nginx/, docker-compose.yml, .env.example)
- [ ] 1.2 — Write base docker-compose.yml (postgres, backend, frontend, nginx, qdrant services)
- [ ] 1.3 — Configure nginx for local dev reverse proxy (frontend on /*, backend on /api/*)
- [ ] 1.4 — Hetzner VPS provisioning (Ubuntu 24, Docker, Docker Compose, SSH key)
- [ ] 1.5 — Production nginx config + Let's Encrypt SSL for lejibe.fr

### Task 2: Database & Backend Foundation
- [ ] 2.1 — FastAPI project scaffold (app structure, config, DB session, health endpoint)
- [ ] 2.2 — PostgreSQL schema: `signups` table (id, email, first_name, profile_type, created_at)
- [ ] 2.3 — PostgreSQL schema: `posts` table (id, slug, title, body_md, published, published_at, created_at)
- [ ] 2.4 — PostgreSQL schema: `user_profiles` table (id, signup_id FK, disability_type, trunk_stability, transfer_method, hand_function, current_chair, car_loading, consent_given_at, created_at)
- [ ] 2.5 — Alembic migrations for all tables
- [ ] 2.6 — Pydantic schemas for signups, posts, and user profiles

### Task 3: Backend API Endpoints
- [ ] 3.1 — `POST /api/signups` — create signup, validate email, deduplicate
- [ ] 3.2 — `POST /api/profiles` — create/update disability profile (requires RGPD consent flag)
- [ ] 3.3 — `GET /api/posts` — list published posts (title, slug, published_at, excerpt)
- [ ] 3.4 — `GET /api/posts/{slug}` — single post (full body)
- [ ] 3.5 — `GET /api/admin/signups` — list all signups with profile data (admin-only, token auth)
- [ ] 3.6 — `POST /api/admin/posts` — create post (admin-only)
- [ ] 3.7 — `PATCH /api/admin/posts/{id}` — update / publish post (admin-only)
- [ ] 3.8 — `GET /api/admin/signups/export` — CSV export of signups + profiles

### Task 4: Landing Page Update
- [ ] 4.0 — Swap Syne → Outfit in approved landing page template
- [ ] 4.1 — SvelteKit project scaffold (routing, fonts, CSS variables matching brand)
- [ ] 4.2 — Nav component (fixed, logo, links, CTA button)
- [ ] 4.3 — Hero section (headline, YouTube/Instagram embed slots)
- [ ] 4.4 — Story section (JB narrative — updated to reflect complete device, not add-on)
- [ ] 4.5 — Problem/solution section (why existing options fall short — stability, weight, seat fit)
- [ ] 4.6 — Features section (base, seat, joystick, front wheel — updated to complete device)
- [ ] 4.7 — Pricing section (€9,800 delivered, financing mention, no reimbursement dependency framing)
- [ ] 4.8 — Ticker / marquee strip
- [ ] 4.9 — Footer

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
- [ ] 7.2 — `/admin/signups` — table view of all signups + profiles, CSV export button
- [ ] 7.3 — `/admin/posts` — list posts with published status
- [ ] 7.4 — `/admin/posts/new` — write + preview + publish form
- [ ] 7.5 — `/admin/posts/[id]/edit` — edit existing post

### Task 8: RAG Knowledge Base (Qdrant + LangChain)
- [ ] 8.1 — Qdrant service added to Docker Compose
- [ ] 8.2 — LangChain integration in FastAPI (document loader, text splitter, embedding model)
- [ ] 8.3 — Ingestion pipeline: load product docs, technical specs, FAQ content into Qdrant
- [ ] 8.4 — Admin endpoint to trigger re-ingestion when docs are updated
- [ ] 8.5 — Retrieval chain: query Qdrant → build context → call Claude API with system prompt + retrieved chunks

### Task 9: AI Chat Widget
- [ ] 9.1 — `POST /api/chat` — accepts user message, returns assistant response (streaming preferred)
- [ ] 9.2 — `POST /api/chat/profile` — accepts profile data from conversational extraction (RGPD consent required)
- [ ] 9.3 — Chat system prompt: product expert persona, conversational disability profile extraction, email capture prompts
- [ ] 9.4 — SvelteKit chat widget component (floating button, slide-out panel, message history)
- [ ] 9.5 — Wire widget to `/api/chat` with streaming response display
- [ ] 9.6 — RGPD consent flow within chat (before storing any profile data)
- [ ] 9.7 — Anonymous mode: user can chat and get answers without providing any personal data

### Task 10: Community Channels
- [ ] 10.1 — Create WhatsApp and/or Telegram group
- [ ] 10.2 — Add join links to landing page and post-signup confirmation
- [ ] 10.3 — Welcome message template for new members

### Task 11: Content Pipeline
- [ ] 11.1 — Integrate YouTube video embeds into landing page (slots ready, JB provides URLs)
- [ ] 11.2 — Integrate Instagram post embeds (same approach)
- [ ] 11.3 — Write initial RAG knowledge base content (product specs, FAQ, comparison with competitors, pricing logic)
- [ ] 11.4 — First blog post: JB's story and what Le Jibé is

### Task 12: Deploy Phase 1
- [ ] 12.1 — Production Docker Compose with all services (postgres, backend, frontend, nginx, qdrant)
- [ ] 12.2 — Environment variables and secrets management
- [ ] 12.3 — SSL + domain configuration
- [ ] 12.4 — Smoke test full flow: landing page → signup → chat → blog
- [ ] 12.5 — Monitoring and basic alerting

---

## Phase 2: Preorders + Financing (September 2026)
**Goal:** Convert email list and community into paying preorders.

- [ ] Preorder flow (product page → checkout → confirmation)
- [ ] BNPL integration (Alma / Pledg / Cofidis — evaluate and pick one)
- [ ] Customer accounts (email + password, view order status)
- [ ] Preorder management admin (list orders, update status, contact customer)
- [ ] Personalised preorder announcement emails (using disability profile data where consented)
- [ ] Checkout disclaimer: "Destiné à un usage privé, non homologué pour la voie publique"
- [ ] Seat configuration questionnaire (body measurements for custom 3D print)

---

## Phase 3: Fulfilment + Post-Sale (December 2026+)
**Goal:** Ship devices and support customers.

- [ ] Order tracking (production status, shipping, delivery)
- [ ] Post-sale support channel
- [ ] Customer feedback collection
- [ ] Referral programme (word of mouth is everything in this community)
- [ ] Newsletter automation (updates, tips, community highlights)

---

## Deferred / Out of Scope

| Item | Reason |
|------|--------|
| Medical device certification (CERAH/LPPR) | Not pursuing — direct-to-customer model, no reimbursement pathway |
| Speed claims in marketing | Legal risk — describe capabilities without specific speed figures |
| Multi-language support | French market only for now |
| Mobile app | Web-first, responsive design sufficient |
