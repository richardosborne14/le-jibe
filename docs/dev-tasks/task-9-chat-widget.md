# Task 9: AI Chat Widget

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 8 output (Qdrant + retrieval function), Task 4 output (landing page with chat placeholder), `docs/CHAT_WIDGET_ARCHITECTURE.md`  
**Output:** Working AI chat widget on the landing page, streaming responses, RGPD-compliant profile capture  
**Estimated Time:** 3–4 sessions (~3–4 hours)

---

## Subtasks

- **9.1** — `POST /api/chat` — FastAPI endpoint: receives message + history, queries Qdrant, calls Claude, streams response via SSE
- **9.2** — Chat system prompt: product expert persona, strict positioning rules, conversational profile extraction, email capture nudge
- **9.3** — `POST /api/chat/profile` — accepts profile data from chat (requires RGPD consent)
- **9.4** — SvelteKit chat widget component (floating button, slide-out panel, message thread, input)
- **9.5** — Wire widget to `/api/chat` with SSE streaming response display
- **9.6** — RGPD consent flow within chat (inline accept/decline buttons, before storing any data)
- **9.7** — Anonymous mode: user can chat without providing any personal data

---

## Cline Prompt

```
Can we please plan task 9 — AI Chat Widget?

Reference:
- README.md (tech stack: SvelteKit, FastAPI, Claude API, Qdrant)
- ROADMAP.md (subtasks 9.1–9.7)
- .clinerules (CRITICAL — all 6 positioning rules must be in the system prompt)
- docs/CHAT_WIDGET_ARCHITECTURE.md (the authoritative spec for this entire task)
- Existing backend/ code from Tasks 2–3 (models, schemas, DB session, admin auth)
- Retrieval function from Task 8 (backend/app/rag/retrieve.py)

We need:

BACKEND:

1. POST /api/chat (SSE streaming):
   Input: { message: string, session_id: string (uuid), history: [{role, content}] }
   Flow:
   - Call retrieve(message) from Task 8 to get 5-8 relevant Qdrant chunks
   - Build full prompt: system prompt + retrieved context + conversation history + user message
   - Call Claude API (claude-3-5-sonnet) with stream=True
   - Stream tokens back to client via Server-Sent Events (FastAPI StreamingResponse)
   - Response format: SSE text/event-stream, each chunk is "data: <token>\n\n", end with "data: [DONE]\n\n"

2. System prompt (see docs/CHAT_WIDGET_ARCHITECTURE.md for full French text):
   - Must embed all 6 positioning rules from .clinerules
   - Must include: "Tu es l'assistant du Jibé..."
   - No speed figures. No road use. No medical language.
   - Tone: direct, factual, warm. Expert, not salesperson.
   - Profile capture: ask conversationally if context allows. One field at a time.
   - RGPD: ask for explicit consent before storing anything.
   - Email capture: suggest signup naturally once. Don't insist.
   - Includes {retrieved_context} placeholder filled at runtime

3. POST /api/chat/profile:
   Input: { email: string, consent: true, profile: {...disability profile fields} }
   - Requires consent: true (422 if missing)
   - Calls POST /api/profiles logic (reuse from Task 3)
   - Returns 200 or 422

FRONTEND:

4. Chat widget Svelte component (src/lib/components/ChatWidget.svelte):
   Layout:
   - Floating button: bottom-right, amber background, chat icon, label "Une question ?"
   - Click opens slide-out panel (~400px wide desktop, full-width mobile)
   - Panel: header (logo + close button), message thread, input row (text + send button)
   - Panel closes on Escape key or close button

   Messages:
   - User messages: right-aligned, amber background
   - Assistant messages: left-aligned, dark background
   - Typing indicator (3 animated dots) while waiting for first token
   - Streaming: append tokens to assistant message in real time

   Session management:
   - session_id: generate once per browser session (UUID, stored in sessionStorage)
   - Conversation history: kept in component state, sent with each request
   - History is NOT persisted across page reloads (privacy by default)

   Special chat UI:
   - If assistant message contains a consent request → show inline amber "Oui, j'accepte" / "Non merci" buttons
   - If assistant suggests signup → show inline mini signup form (just email + prénom, submits to POST /api/signups)
   - "Continuer sans créer de compte" link always visible below input

   Accessibility:
   - Full keyboard navigation (Tab, Enter, Escape)
   - ARIA labels on all interactive elements
   - Focus trap when panel is open
   - Screen reader compatible

5. SSE connection:
   - Use fetch() with ReadableStream to consume SSE from /api/chat
   - Parse "data: " prefix, accumulate tokens, render progressively
   - Handle "data: [DONE]" to close stream
   - Handle network errors gracefully (show "Une erreur est survenue. Réessayez.")
```

---

## Confidence Criteria

- [ ] `POST /api/chat` returns a streaming SSE response
- [ ] System prompt includes all 6 positioning rules from `.clinerules`
- [ ] System prompt is in French
- [ ] No speed figures, road use, or medical language in any assistant response
- [ ] Qdrant context is retrieved and included in every prompt
- [ ] Chat widget renders correctly on landing page (floating button, slide-out panel)
- [ ] User messages appear right-aligned, assistant messages left-aligned
- [ ] Streaming works: tokens appear progressively, not all at once
- [ ] Typing indicator shows while waiting for first token
- [ ] RGPD consent buttons appear inline when assistant asks for consent
- [ ] Accepting consent → profile stored in DB; declining → conversation continues cleanly
- [ ] "Continuer sans créer de compte" always available
- [ ] session_id generated per session, history kept in component state only
- [ ] Widget fully keyboard navigable, focus trapped when open
- [ ] Works on mobile (full-width panel)
- [ ] Network errors displayed in French

---

## Decisions to Watch For

- **Streaming implementation:** SSE via FastAPI `StreamingResponse` with `media_type="text/event-stream"`. Use `async for` over the Claude stream
- **Claude model:** `claude-3-5-sonnet-20241022` — best balance of quality, speed, cost for French language
- **History truncation:** Include last 10 turns maximum (to stay within token budget). Older history dropped silently
- **Rate limiting:** Add a simple per-session rate limit (e.g. 20 messages/session) to prevent abuse. Return 429 with a friendly French message
- **CORS:** `/api/chat` must be accessible from the SvelteKit frontend — confirm CORS headers allow it
- **Consent UI trigger:** The assistant signals consent request by including a specific phrase (e.g. `[RGPD_CONSENT]`) that the widget detects and replaces with the inline button UI
- **Profile storage from chat:** Widget calls `POST /api/chat/profile` — never calls DB directly

---

## Notes

This is the most complex task in Phase 1. Take it methodically: build and test the backend endpoint first (use curl or Swagger to verify streaming), then build the widget component against it. The system prompt is critical — review it against all 6 `.clinerules` positioning rules before shipping. Full architecture spec is in `docs/CHAT_WIDGET_ARCHITECTURE.md`.

**Depends on:** Task 8 (RAG retrieval), Task 4 (landing page with chat placeholder)  
**Blocks:** Task 12 (deploy)
