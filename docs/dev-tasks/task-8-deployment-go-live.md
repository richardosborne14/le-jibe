# Task 8: Deployment & Go-Live

**Status:** Not started | **Target Confidence:** 10/10

**Input:** All previous tasks complete and working locally, Hetzner VPS provisioned (from Task 1.4)  
**Output:** Live site at `lejibe.fr` with SSL, all features working in production  
**Estimated Time:** 1–2 sessions (~90 min)

---

## Subtasks

- **8.1** — Production `.env` (secrets, DB credentials, admin token)
- **8.2** — Full `docker compose up` on Hetzner, smoke test all endpoints
- **8.3** — DNS: point `lejibe.fr` to Hetzner, SSL cert via certbot
- **8.4** — Verify signup form end-to-end on production
- **8.5** — Write first blog post from admin panel

---

## Cline Prompt

```
Can we please plan task 8 — Deployment & Go-Live?

Reference:
- README.md (deployment section, Hetzner VPS)
- ROADMAP.md (subtasks 8.1–8.5)
- CLAUDE_RULES.md
- Production nginx config from Task 1.5
- DEPLOY.md or provisioning notes from Task 1.4

We need:
1. Production .env file (template — actual secrets filled in manually):
   - POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
   - DATABASE_URL
   - ADMIN_TOKEN
   - DOMAIN=lejibe.fr
   - Any other env vars the app needs

2. Deployment script or documented steps:
   - SSH into Hetzner
   - Clone repo (or git pull if already cloned)
   - Copy production .env
   - docker compose -f docker-compose.prod.yml up -d --build
   - Run Alembic migrations
   - Smoke test: hit /api/health, load homepage, test signup

3. SSL setup:
   - certbot with nginx plugin, or standalone + nginx reload
   - Auto-renewal cron job
   - Redirect HTTP → HTTPS

4. DNS checklist:
   - A record: lejibe.fr → Hetzner IP
   - AAAA record if IPv6
   - www redirect (optional)

5. Go-live verification checklist:
   - [ ] Homepage loads with correct fonts/images
   - [ ] Signup form submits successfully
   - [ ] Admin login works
   - [ ] Can create and publish a blog post
   - [ ] Published post appears on /blog
   - [ ] SSL certificate valid (no mixed content warnings)
   - [ ] Mobile responsive

Subtask 8.5 (first blog post) is manual — just note it in the checklist.
```

---

## Confidence Criteria

- [ ] Site loads at `https://lejibe.fr` with valid SSL
- [ ] HTTP redirects to HTTPS
- [ ] Homepage renders correctly (fonts, images, layout)
- [ ] Signup form creates a record in production database
- [ ] Admin panel accessible and functional
- [ ] Blog post can be created, published, and read
- [ ] No console errors in browser
- [ ] No mixed content warnings
- [ ] SSL auto-renewal configured
- [ ] Database persists across container restarts

---

## Decisions to Watch For

- **docker-compose.prod.yml:** Separate from dev — no hot reload, no exposed ports except 80/443, restart policies set to `unless-stopped`
- **Database backups:** At minimum, set up a daily pg_dump cron job to a local file. Can add offsite backup later
- **Secrets management:** Never commit the production `.env`. Add it to `.gitignore`
- **SSL approach:** certbot with `--nginx` plugin is simplest if nginx is on the host. If nginx is in Docker, use `--standalone` or a Docker certbot sidecar
- **Rollback plan:** If deployment fails, `docker compose down` and re-deploy previous version

---

## Notes

This is the finish line for Phase 1. Everything before this was local — now it's real. Take it slow, test each step, and don't rush DNS propagation. The first blog post (subtask 8.5) is a nice milestone moment — write something genuine about why Le Jibé exists.

**Depends on:** All previous tasks (1–7)  
**Blocks:** Nothing — this is the end of Phase 1
