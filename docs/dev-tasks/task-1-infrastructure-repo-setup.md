# Task 1: Infrastructure & Repo Setup

**Status:** Not started | **Target Confidence:** 8/10

**Input:** README.md (tech stack, project structure), ROADMAP.md  
**Output:** Working monorepo with Docker Compose, nginx reverse proxy, all services bootable locally  
**Estimated Time:** 1–2 sessions (~90 min)

---

## Subtasks

- **1.1** — Initialise monorepo structure (`frontend/`, `backend/`, `nginx/`, `docker-compose.yml`, `.env.example`)
- **1.2** — Write base `docker-compose.yml` (postgres, backend, frontend, nginx services)
- **1.3** — Configure nginx for local dev reverse proxy (frontend on `/*`, backend on `/api/*`)
- **1.4** — Hetzner VPS provisioning (Ubuntu 24, Docker, Docker Compose, SSH key)
- **1.5** — Production nginx config + Let's Encrypt SSL for `lejibe.fr`

---

## Cline Prompt

```
Can we please plan task 1 — Infrastructure & Repo Setup?

Reference:
- README.md (tech stack: SvelteKit, FastAPI, PostgreSQL, Docker Compose, nginx, Hetzner)
- ROADMAP.md (subtasks 1.1–1.5)

We need:
1. Monorepo with frontend/, backend/, nginx/ directories
2. docker-compose.yml that boots all services (postgres, backend, frontend, nginx)
3. nginx config: frontend on /*, backend on /api/*
4. .env.example with all required variables
5. Production nginx config with SSL (separate from dev)

Rule from README: All API logic lives in FastAPI. SvelteKit only calls /api/* endpoints.

Subtask 1.4 (Hetzner provisioning) is manual — just document the steps, don't try to SSH.
Subtask 1.5 (production nginx + SSL) — write the config files, deployment is a later task.
```

---

## Confidence Criteria

- [ ] `docker compose up` boots all 4 services without errors
- [ ] `http://localhost:5173` serves SvelteKit frontend
- [ ] `http://localhost:8000/docs` serves FastAPI Swagger
- [ ] nginx correctly proxies `/api/*` → backend, `/*` → frontend
- [ ] `.env.example` documents every required variable
- [ ] Production nginx config exists with SSL placeholder
- [ ] Hetzner provisioning steps documented in a `DEPLOY.md` or similar

---

## Decisions to Watch For

- **Port mapping:** Keep it simple — 5173 (frontend), 8000 (backend), 5432 (postgres), 80/443 (nginx)
- **Postgres volume:** Must persist data between restarts
- **Hot reload:** Both SvelteKit and FastAPI should hot-reload in dev mode inside Docker
- **Production vs dev:** Separate docker-compose.prod.yml or override file

---

## Notes

This is pure infrastructure — no application code yet. The goal is: clone the repo, run one command, everything works. Subtask 1.4 (Hetzner) is a manual step you'll do yourself; the task doc should just list the commands.

**Depends on:** Nothing (first task)  
**Blocks:** Task 2, Task 4
