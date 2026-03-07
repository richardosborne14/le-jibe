# Le Jibé

A complete electric mobility device designed from the inside — by a paraplegic engineer in the Dordogne, France. Segway base, front stabilising wheel, 3D-printed carbon fibre custom seat, joystick control.

This repo is the full platform: landing page, interest capture, AI chat assistant, blog, and eventually preorder management.

---

## Vision

A direct-to-customer platform for Le Jibé that handles the full journey:
- Discovery and brand storytelling
- Interest capture and community building
- AI chat assistant with product knowledge (RAG-powered)
- Blog for design/build updates (transparency builds trust)
- Preorder management and payment (Phase 2)
- BNPL financing integration (Phase 2)
- Order fulfilment and tracking (Phase 3)

No reimbursement pathway. No medical device certification. Le Jibé is sold direct to customers as a performance mobility device for private use.

---

## The Product

Le Jibé is a **complete standalone mobility device**, not an attachment or add-on.

**What the customer receives:**
- Modified Segway base (large all-terrain wheels, gyroscopic stabilisation)
- Steel frame connecting base to seat
- Front stabilising wheel (anti-fall, curb-mounting capability)
- 3D-printed carbon fibre seat — custom-fitted to the individual user's body dimensions
- Rigid-mount joystick (one side of frame, gentle push to move, no body movement required)

**Key differentiators:**
- Front wheel provides stability that no competitor offers with electric propulsion
- Joystick + gyroscopic base means body movement does NOT cause unintended displacement — user can lean, reach, carry objects safely
- Custom seat accommodates individual needs: flat open sides for users who slide-transfer, supported sides for users with trunk stability
- User keeps their existing wheelchair as a backup (no reimbursement conflict)
- User transfers their own custom cushion between their wheelchair and Le Jibé

**Price:** €9,800 delivered. BNPL financing available (10 or 12 instalments).

**What we do NOT say publicly:**
- No specific speed figures (legal implications — see `.clinerules`)
- Never describe as road-legal, street-legal, or homologué
- Describe capabilities (terrain, manoeuvrability, range) without specifying context of use
- Standard disclaimer at checkout: "Destiné à un usage privé, non homologué pour la voie publique"

---

## Current Phase: Phase 1 — Landing Page + Community + Chat Assistant

**We are building:**
- Landing page with updated product story, video embeds, feature overview
- Interest signup form (name, email, profile type)
- AI chat assistant widget (LangChain + Qdrant RAG, fed with product/technical docs)
- Optional disability profile capture (behind RGPD health-data consent)
- Blog engine (admin writes posts, public reads them)
- Simple admin view (see signups, write/publish posts)
- Community channels (WhatsApp and/or Telegram group)

**We are NOT building yet:**
- Preorder flow → Phase 2 (September 2026)
- BNPL integration (Alma / Pledg / Cofidis) → Phase 2
- Customer accounts → Phase 2
- Order tracking and fulfilment → Phase 3

---

## Timeline

| Milestone | Target | Notes |
|-----------|--------|-------|
| Landing page live | ASAP | Updated content, video embeds, signup form |
| AI chat widget live | Before Sept 2026 | RAG on product docs, optional profile capture |
| Community channels active | Alongside landing page | WhatsApp/Telegram for updates and live Q&A |
| First working prototype | September 2026 | JB testing with himself and friends |
| Preorders open | September 2026 | Announce to email list and community |
| First deliveries | December 2026 | Christmas target |

---

## Tech Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Frontend | SvelteKit | SSR + static where appropriate |
| Backend | FastAPI (Python) | All business logic and API routes |
| Database | PostgreSQL | Via Alembic for migrations |
| RAG | Qdrant + LangChain | Product knowledge base for chat widget |
| LLM | Claude API (Anthropic) | Powers the chat assistant |
| Infra | Hetzner VPS | Single box, EU-hosted |
| Containers | Docker Compose | All services containerised |
| Reverse proxy | nginx | SSL termination via Let's Encrypt |
| Deployment | Git pull + rebuild | Via Cline over SSH |

**Rule:** All API logic lives in FastAPI. SvelteKit only calls `/api/*` endpoints — no server-side logic in SvelteKit routes.

---

## Design Language

Brand: warm industrial editorial. Dark background, amber accent. French performance brand, not medical equipment.

- Display font: **Outfit** (clean geometric, legible at all sizes) — replaces Syne
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

Production runs on a single Hetzner VPS. Deploy via git pull and Docker Compose rebuild, executed by Cline over SSH.
