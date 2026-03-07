# Chat Widget & RAG Architecture

**Status:** Design phase
**Phase:** 1 (build alongside landing page)

---

## Overview

An AI chat assistant embedded in the landing page that:
1. Answers any question about Le Jibé (product, pricing, suitability, logistics)
2. Conversationally assesses whether Le Jibé is a good fit for the user's disability profile
3. Captures email addresses and (with consent) disability profile data for personalised outreach
4. Works in anonymous mode for users who don't want to share personal data

---

## System Architecture

```
┌─────────────────┐
│  SvelteKit       │
│  Chat Widget     │ ──── POST /api/chat ────┐
│  (floating panel)│                          │
└─────────────────┘                          ▼
                                    ┌─────────────────┐
                                    │  FastAPI         │
                                    │  /api/chat       │
                                    │                  │
                                    │  1. Parse message │
                                    │  2. Query Qdrant  │
                                    │  3. Build prompt  │
                                    │  4. Call Claude   │
                                    │  5. Stream back   │
                                    └────────┬─────────┘
                                             │
                              ┌──────────────┼──────────────┐
                              ▼              ▼              ▼
                        ┌──────────┐  ┌──────────┐  ┌──────────┐
                        │  Qdrant  │  │  Claude   │  │ Postgres │
                        │  (RAG)   │  │  API      │  │ (profiles│
                        │          │  │          │  │  signups) │
                        └──────────┘  └──────────┘  └──────────┘
```

---

## Data Flow

### Chat Request
1. User types message in widget
2. SvelteKit sends `POST /api/chat` with: `{ message, session_id, conversation_history[] }`
3. FastAPI receives, queries Qdrant for relevant context chunks
4. FastAPI builds full prompt: system prompt + retrieved context + conversation history + user message
5. FastAPI calls Claude API with streaming enabled
6. Response streams back to widget via SSE (Server-Sent Events)

### Profile Capture (with consent)
1. During conversation, assistant naturally asks about the user's situation
2. If user provides disability-related information, assistant asks for RGPD consent:
   "Ces informations nous aident à personnaliser nos communications. Souhaitez-vous qu'on les conserve ? Vous pouvez aussi continuer sans rien enregistrer."
3. If consented: FastAPI stores profile data in `user_profiles` table, linked to signup
4. If declined: conversation continues normally, no data persisted

### Email Capture
1. Assistant naturally suggests signing up during conversation
2. If user provides email in chat: `POST /api/signups` is called server-side
3. No duplicate — if email already exists, silently continue

---

## RAG Pipeline

### Ingestion
- **Source documents:** Product specs, FAQ, pricing info, comparison docs, blog posts, JB's technical notes
- **Processing:** LangChain document loaders → text splitter (chunk size ~500 tokens, overlap ~50)
- **Embedding:** Open-source model (start with `all-MiniLM-L6-v2` or `multilingual-e5-large` for French)
- **Storage:** Qdrant collection `lejibe_knowledge`
- **Metadata per chunk:** `{ source, doc_type, language, last_updated }`

### Retrieval
- Query embedding → Qdrant similarity search (top 5-8 chunks)
- Filter by `doc_type` if query intent is clear (e.g. pricing question → filter to pricing docs)
- Return chunks with metadata for attribution

### Re-ingestion
- Admin endpoint: `POST /api/admin/rag/ingest` — clears collection and re-ingests all source docs
- Triggered manually when JB provides new documentation or specs change

---

## Chat System Prompt

The system prompt is critical. It must include:

```
Tu es l'assistant du Jibé, un dispositif de mobilité électrique complet conçu par 
Jean-Baptiste, ingénieur et paraplégique, en Dordogne.

RÈGLES ABSOLUES:
- Ne jamais mentionner de vitesse (ni km/h, ni "rapide"). Dire "fluide", "réactif".
- Ne jamais dire que Le Jibé est homologué route ou utilisable sur la voie publique.
- Ne jamais utiliser de langage médical ("aide médicale", "dispositif médical"). 
  Le Jibé est un "outil de liberté", un "dispositif de mobilité performante".
- Ne jamais nommer de concurrents sauf si l'utilisateur le fait en premier.

TON:
- Direct, factuel, chaleureux mais pas sentimental.
- Tu es un expert produit, pas un vendeur.
- Tu peux dire "je ne sais pas" si l'information n'est pas dans ton contexte.

PROFIL UTILISATEUR:
- Si la conversation s'y prête naturellement, tu peux poser des questions sur la 
  situation de l'utilisateur (type de handicap, stabilité du tronc, méthode de 
  transfert, usage actuel).
- Avant de stocker quoi que ce soit, demande le consentement RGPD explicitement.
- Si l'utilisateur refuse, continue normalement sans insister.

EMAIL:
- Si l'utilisateur semble intéressé et n'a pas donné son email, propose l'inscription 
  naturellement. Une seule fois. Ne pas insister.

CONTEXTE PRODUIT:
{retrieved_context}
```

---

## Disability Profile Fields

Collected conversationally, not as a form. Each field maps to a column in `user_profiles`.

| Field | Chat Question (example) | Column | Values |
|-------|------------------------|--------|--------|
| Type de handicap | "Quel est votre type de handicap, si vous souhaitez le partager ?" | `disability_type` | paraplégie, tétraplégie, autre (free text) |
| Stabilité du tronc | "Pouvez-vous rester assis sans appui dorsal ?" | `trunk_stability` | oui, partiellement, non |
| Méthode de transfert | "Comment passez-vous de votre fauteuil à un autre siège ?" | `transfer_method` | glissé autonome, planche de transfert, aide tierce personne |
| Fonction mains/bras | "Avez-vous l'usage complet de vos deux mains ?" | `hand_function` | complète deux mains, limitée, une main |
| Fauteuil actuel | "Quel type de fauteuil utilisez-vous actuellement ?" | `current_chair` | manuel actif, manuel standard, électrique, autre |
| Chargement voiture | "Chargez-vous votre fauteuil dans une voiture seul(e) ?" | `car_loading` | seul, avec aide, non concerné |

---

## RGPD Compliance

### Health data = données sensibles (Article 9 GDPR)

- **Explicit consent required** — not just a checkbox, but informed and specific
- **Consent text:** "Vos informations de santé sont des données sensibles au sens du RGPD. Elles nous permettent de personnaliser nos communications et de vous proposer la configuration la plus adaptée. En acceptant, vous consentez à leur stockage sécurisé. Vous pouvez demander leur suppression à tout moment."
- **Consent stored:** `consent_given_at` timestamp in `user_profiles`
- **Right to erasure:** Admin endpoint `DELETE /api/profiles/{id}` — or user can request via email/chat
- **Data minimisation:** Only collect what's needed for product fit assessment
- **Storage:** PostgreSQL with encryption at rest. No profile data in Qdrant. No profile data in logs.
- **Retention:** Profile data deleted if user requests it or if no signup activity for 24 months

### Anonymous mode
- User can chat without providing any personal data
- No session data persisted beyond the browser tab
- RAG still works — user gets full product information
- Widget shows clear toggle: "Continuer sans créer de compte"

---

## Frontend Widget Spec

### Layout
- Floating button: bottom-right corner, amber background, chat icon
- Click opens slide-out panel (right side, ~400px wide on desktop, full-width on mobile)
- Panel contains: header (Le Jibé logo + "close" button), message thread, input field + send button

### Behaviour
- Messages display as chat bubbles (user right, assistant left)
- Streaming: assistant response appears token by token
- Typing indicator while waiting for first token
- Conversation persists within the browser session (not across sessions)
- If assistant suggests signup, show inline signup mini-form within chat
- If assistant asks for RGPD consent, show inline accept/decline buttons

### Accessibility
- Full keyboard navigation
- Screen reader compatible (ARIA labels on all interactive elements)
- Sufficient contrast ratios (already handled by dark theme)
- Focus trap when panel is open

---

## API Endpoints

### `POST /api/chat`
```json
{
  "message": "string",
  "session_id": "string (uuid, client-generated)",
  "history": [
    { "role": "user", "content": "..." },
    { "role": "assistant", "content": "..." }
  ]
}
```
Response: SSE stream of text chunks.

### `POST /api/chat/profile`
```json
{
  "email": "string",
  "consent": true,
  "profile": {
    "disability_type": "paraplégie",
    "trunk_stability": "partiellement",
    "transfer_method": "glissé autonome",
    "hand_function": "complète deux mains",
    "current_chair": "manuel actif",
    "car_loading": "seul"
  }
}
```
Requires `consent: true`. Returns 200 or 422 if consent missing.

### `POST /api/admin/rag/ingest`
Admin-only. Triggers full re-ingestion of knowledge base documents.

---

## Tech Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| LLM | Claude API (Anthropic) | Best French language quality, system prompt adherence |
| Orchestration | LangChain | Mature RAG pipeline tooling, good Qdrant integration |
| Vector DB | Qdrant | Open source, self-hosted, lightweight, Docker-friendly |
| Embedding model | `multilingual-e5-large` (start) | Strong French performance, can upgrade later |
| Streaming | SSE via FastAPI StreamingResponse | Simple, well-supported, no WebSocket complexity |
| Session management | Client-side (session_id + history in memory) | No server-side session state needed in Phase 1 |

---

## Open Questions

- [ ] Embedding model: start with `multilingual-e5-large` or go straight to an API-based option?
- [ ] Chat history length: how many turns to include before truncating? (Token budget consideration)
- [ ] Rate limiting: how many chat messages per session/hour to prevent abuse?
- [ ] Should the chat widget be available on blog pages too, or landing page only?
