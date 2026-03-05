# Learnings

Running log of decisions, solutions, and gotchas discovered during development.  
Add entries as you go — this is read at the start of sessions to avoid re-solving known problems.

Format: newest entries at the top.

---

## Deferred Ideas

Things that came up during implementation but deliberately not built yet:

| Idea | Context | Revisit in |
|---|---|---|
| Email confirmation on signup | Would be nice UX but needs SMTP setup | Phase 2 |
| CSV export in admin | Currently manual from DB | Phase 2 |

---

## Architecture Decisions

### 2025: Single-server deployment on Hetzner
One VPS hosts all services via Docker Compose. Deliberate choice: simpler, cheaper, under JB's control, EU-hosted. Not using Vercel/Netlify for frontend despite trade-offs (no CDN, no preview deployments). Revisit if traffic becomes a problem — at that point, split services is trivial with this architecture.

### 2025: Static admin token (no user auth)
Admin panel uses a single token from the environment variable `ADMIN_TOKEN`. No user accounts, no sessions. Simple and sufficient for a single-person operation. Will need proper auth before any second person needs admin access.

### 2025: Markdown for blog posts (stored as raw MD in DB)
Blog posts are stored as raw Markdown in the database and rendered client-side. Simple to write, easy to edit. No CMS required at this scale. If the blog becomes more active, consider a lightweight editor in the admin panel.

---

## Gotchas & Solutions

*(Add entries here as you discover them)*

### Example format:
**Problem:** Docker Compose was rebuilding postgres on every `up --build`, wiping data.  
**Solution:** Postgres doesn't need a `build:` key — use `image: postgres:16` directly. Data persists in the named volume.  
**Date:** YYYY-MM-DD
