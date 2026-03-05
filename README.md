# Le Jibé

A high-performance electric wheelchair designed from the inside — by a paraplegic engineer in the Dordogne, France. Segway-type base, carbon fibre custom seat, joystick control, 30km/h.

This repo is the full platform: landing page, interest capture, blog, and eventually e-commerce and order management.

---

## Vision

A direct-to-customer platform for Le Jibé that handles the full journey:
- Discovery and brand storytelling
- Interest capture and waitlist
- Blog for design/build updates (transparency builds trust)
- Product configuration and ordering (Phase 2)
- Payment via Alma BNPL (Phase 2)
- Order state tracking per customer (Phase 3)
- LPPR reimbursement workflow tooling (Phase 3)

The long-term goal is LPPR registration (French medical device reimbursement). Until then, the platform serves self-paying customers directly.

---

## Current Phase: MVP — Interest Capture

**We are building:**
- Landing page with brand story, hero video embed, and feature overview
- Interest signup form (name, email, profile type)
- Blog engine (admin writes posts, public reads them)
- Simple admin view (see signups, write/publish posts)

**We are NOT building yet:**
- Product ordering or configuration → Phase 2
- Alma payment integration → Phase 2
- Customer accounts → Phase 2
- Order tracking → Phase 3
- LPPR/reimbursement workflow → Phase 3

---

## Tech Stack

| Layer       | Technology          | Notes                              |
|-------------|--------------------|------------------------------------|
| Frontend    | SvelteKit          | SSR + static where appropriate     |
| Backend     | FastAPI (Python)   | All business logic and API routes  |
| Database    | PostgreSQL         | Via Alembic for migrations         |
| Infra       | Hetzner VPS        | Single box, EU-hosted, ~€15/month  |
| Containers  | Docker Compose     | All services containerised         |
| Reverse proxy | nginx            | SSL termination via Let's Encrypt  |
| Deployment  | Git pull + rebuild | Via Cline over SSH                 |

**Rule:** All API logic lives in FastAPI. SvelteKit only calls `/api/*` endpoints — no server-side logic in SvelteKit routes.

---

## Design Language

Brand: warm industrial editorial. Dark background, amber accent. French performance brand, not medical equipment.

- Display font: Syne (geometric, architectural)
- Body font: Instrument Sans
- Accent serif: Instrument Serif (italic moments)
- Primary colour: `#D4860A` (amber)
- Background: `#0D0D0B` (near-black)

See `lejibe-landing.html` for the approved mockup. All UI should follow this aesthetic.

---

## Local Development

```bash
# Prerequisites: Docker, Docker Compose

cp .env.example .env
docker compose up -d

# Frontend: http://localhost:5173
# Backend:  http://localhost:8000
# API docs: http://localhost:8000/docs
```

---

## Deployment

Production runs on a single Hetzner VPS. Deployments are manual via SSH:

```bash
ssh deploy@<server-ip>
cd /opt/lejibe
git pull
docker compose up -d --build
```

See `CLAUDE_RULES.md` for full deployment conventions.

---

## Project Structure

```
lejibe/
├── frontend/          # SvelteKit app
│   ├── src/
│   │   ├── routes/    # Pages only — no server logic
│   │   └── lib/       # Shared components and utils
│   └── Dockerfile
├── backend/           # FastAPI app
│   ├── app/
│   │   ├── api/       # Route handlers
│   │   ├── models/    # SQLAlchemy models
│   │   ├── schemas/   # Pydantic schemas
│   │   └── core/      # Config, DB session, etc.
│   ├── alembic/       # DB migrations
│   └── Dockerfile
├── nginx/             # nginx config + SSL
├── docker-compose.yml
├── .env.example
├── README.md          ← you are here
├── ROADMAP.md
├── CLAUDE_RULES.md
├── TASK_TEMPLATE.md
└── LEARNINGS.md
```
