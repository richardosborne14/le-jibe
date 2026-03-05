# Le Jibé — Deployment Guide

## Server Details

| | |
|---|---|
| **Provider** | Hetzner Cloud |
| **Server name** | le-jibe-prod |
| **Server ID** | 122903131 |
| **IP** | 178.104.38.111 |
| **Type** | cx23 (2 vCPU, 4GB RAM, 40GB SSD) |
| **Location** | Nuremberg, Germany (nbg1) |
| **OS** | Ubuntu 24.04 |
| **Monthly cost** | ~€2.99 |

## SSH Access

The deploy key was generated during Task 1 and stored in the project root (gitignored).

```bash
# Add to your SSH agent (run once per session or add to ~/.bash_profile)
ssh-add /path/to/le-jibe-deploy

# Or connect directly with the key
ssh -i /path/to/le-jibe-deploy root@178.104.38.111
```

**Recommended:** copy key to `~/.ssh/` and add an alias in `~/.ssh/config`:

```
Host le-jibe
    HostName 178.104.38.111
    User root
    IdentityFile ~/.ssh/le-jibe-deploy
```

Then: `ssh le-jibe`

---

## One-time Server Setup

Run these once after first SSH in. The server is a fresh Ubuntu 24.04 install.

```bash
ssh -i le-jibe-deploy root@178.104.38.111

# 1. Update system
apt update && apt upgrade -y

# 2. Install Docker
curl -fsSL https://get.docker.com | sh

# 3. Install Docker Compose plugin (v2)
apt install -y docker-compose-plugin

# 4. Verify
docker --version
docker compose version

# 5. Create deploy user (safer than running as root)
useradd -m -s /bin/bash deploy
usermod -aG docker deploy
mkdir -p /home/deploy/.ssh
cp ~/.ssh/authorized_keys /home/deploy/.ssh/
chown -R deploy:deploy /home/deploy/.ssh

# 6. Create app directory
mkdir -p /opt/lejibe
chown deploy:deploy /opt/lejibe

# 7. Switch to deploy user
su - deploy

# 8. Clone the repo
cd /opt/lejibe
git clone https://github.com/richardosborne14/le-jibe.git .

# 9. Create production .env
cp .env.example .env
nano .env  # Fill in real values — see "Production .env" section below
```

---

## Production .env

Required values on the server. Do not commit this file.

```bash
# Database
POSTGRES_DB=lejibe
POSTGRES_USER=lejibe
POSTGRES_PASSWORD=<generate: openssl rand -hex 24>

# Backend
DATABASE_URL=postgresql://lejibe:<password>@postgres:5432/lejibe
ADMIN_TOKEN=<generate: openssl rand -hex 32>
ALLOWED_ORIGINS=https://le-jibe.com,https://www.le-jibe.com

# Frontend (empty = use /api via nginx same-origin)
PUBLIC_API_URL=

# Domain
DOMAIN=le-jibe.com
```

---

## Deploy (subsequent deploys)

```bash
ssh le-jibe  # or: ssh -i le-jibe-deploy root@178.104.38.111

cd /opt/lejibe
git pull

# Build and restart all services
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

# Run any pending migrations
docker compose exec backend alembic upgrade head

# Check everything is running
docker compose ps
docker compose logs -f backend
```

---

## SSL — Let's Encrypt via Certbot

Run once after DNS is pointing at `178.104.38.111`:

```bash
# On the server
apt install -y certbot

# First: start nginx on HTTP only (SSL stanza commented out) so certbot can verify
# Then issue the cert:
certbot certonly --webroot \
  -w /var/www/certbot \
  -d le-jibe.com \
  -d www.le-jibe.com \
  --email admin@le-jibe.com \
  --agree-tos \
  --no-eff-email

# Certs are written to: /etc/letsencrypt/live/le-jibe.com/

# Now enable the full SSL nginx config and restart
docker compose restart nginx

# Auto-renewal (add to root crontab)
# crontab -e
0 3 * * * certbot renew --quiet && docker compose -f /opt/lejibe/docker-compose.yml -f /opt/lejibe/docker-compose.prod.yml restart nginx
```

---

## DNS Records

Point these at `178.104.38.111` once the domain is registered:

| Type | Name | Value | TTL |
|---|---|---|---|
| A | `@` | `178.104.38.111` | 300 |
| A | `www` | `178.104.38.111` | 300 |

---

## Useful Commands

```bash
# View logs
docker compose logs -f backend
docker compose logs -f frontend
docker compose logs -f nginx

# Restart a single service
docker compose restart backend

# Run Alembic migration
docker compose exec backend alembic upgrade head

# Connect to database
docker compose exec postgres psql -U lejibe -d lejibe

# Check server resources
htop
df -h
```

---

## Hetzner Console

Manage the server at: https://console.hetzner.cloud/
Project: le-jibe | Server: le-jibe-prod
