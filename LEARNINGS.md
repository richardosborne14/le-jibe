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

### SvelteKit vite.config.ts fails with "ESM only" error in Docker
**Problem:** Frontend container crashed with `Failed to resolve "@sveltejs/kit/vite". This package is ESM only but it was tried to load by require.`  
**Solution:** Add `"type": "module"` to `frontend/package.json`. SvelteKit requires the project to be treated as ES modules.  
**Date:** 2026-03-05

### Host port conflicts in dev (multiple projects running)
**Problem:** `vh-command-centre` project was already using port 8000 on the host, causing `docker compose up` to fail with "port already allocated".  
**Solution:** Changed backend host port mapping in `docker-compose.yml` to `8002:8000`. Internal Docker networking is unaffected (nginx → backend:8000 still works). In production on Hetzner, the full 8000 port is available.  
**Note:** The README shows `localhost:8000` as the canonical backend address — on a clean machine this is correct. On this dev machine use `localhost:8002`.  
**Date:** 2026-03-05

### Hetzner cx22 deprecated
**Problem:** `cx22` server type was deprecated and rejected by the Hetzner API with `"server type 104 is deprecated"`.  
**Solution:** Use `cx23` — identical spec (2 vCPU, 4GB RAM, 40GB SSD), slightly cheaper at €2.99/mo.  
**Date:** 2026-03-05
