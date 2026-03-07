# Task 8: RAG Knowledge Base (Qdrant + LangChain)

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 3 output (working FastAPI), `docs/CHAT_WIDGET_ARCHITECTURE.md`  
**Output:** Qdrant running in Docker, LangChain ingestion pipeline, retrieval chain callable from FastAPI  
**Estimated Time:** 2 sessions (~2–3 hours)

---

## Subtasks

- **8.1** — Qdrant service added to Docker Compose (dev and prod)
- **8.2** — LangChain integration in FastAPI (document loader, text splitter, embedding model)
- **8.3** — Ingestion pipeline: load product docs, technical specs, FAQ content into Qdrant collection `lejibe_knowledge`
- **8.4** — Admin endpoint `POST /api/admin/rag/ingest` — triggers full re-ingestion (clears collection + re-ingests)
- **8.5** — Retrieval function: query Qdrant → top 5–8 chunks → return with metadata (used by Task 9 chat endpoint)

---

## Cline Prompt

```
Can we please plan task 8 — RAG Knowledge Base?

Reference:
- README.md (tech stack: Qdrant, LangChain, FastAPI)
- ROADMAP.md (subtasks 8.1–8.5)
- .clinerules
- docs/CHAT_WIDGET_ARCHITECTURE.md (RAG pipeline section — the authoritative spec)

We need:
1. Qdrant added to docker-compose.yml:
   - Service: qdrant (image: qdrant/qdrant)
   - Port: 6333 (REST API), 6334 (gRPC)
   - Volume: persist collection data between restarts
   - Internal only — not exposed externally in production

2. LangChain setup in backend:
   - Install: langchain, langchain-community, langchain-anthropic, qdrant-client, sentence-transformers
   - Embedding model: multilingual-e5-large (sentence-transformers) — strong French support
   - Document loaders for plain text and markdown files from a /docs/knowledge-base/ directory

3. Ingestion pipeline (backend/app/rag/ingest.py):
   - Load all .md and .txt files from /docs/knowledge-base/
   - Split with RecursiveCharacterTextSplitter (chunk_size=500, chunk_overlap=50)
   - Add metadata per chunk: { source, doc_type, language, last_updated }
   - doc_type values: spec, faq, blog, comparison, pricing
   - Embed with multilingual-e5-large
   - Store in Qdrant collection 'lejibe_knowledge'
   - Ingest is destructive: clear collection then re-ingest (clean slate)

4. Admin endpoint POST /api/admin/rag/ingest:
   - Admin-only (same Bearer token auth as other admin endpoints)
   - Calls the ingest pipeline asynchronously
   - Returns 202 Accepted immediately, runs ingestion in background
   - Log ingestion progress (count of chunks ingested)

5. Retrieval function (backend/app/rag/retrieve.py):
   - Accepts a query string
   - Embeds query with same model
   - Queries Qdrant collection, returns top 5-8 chunks with metadata
   - Optional: filter by doc_type if intent is clear
   - Returns list of {content, source, doc_type} dicts
   - This function will be called by the chat endpoint in Task 9

Initial knowledge base content:
- Create /docs/knowledge-base/ directory with placeholder files:
  - product-overview.md (what Le Jibé is, who it's for)
  - features-spec.md (base, seat, joystick, front wheel — technical details)
  - faq.md (common questions and answers)
  - pricing.md (€9,800, financing, no reimbursement dependency)
  - comparison.md (how Le Jibé compares to alternatives — no competitor names)
- Content should follow .clinerules: no speed figures, no road use, no medical language
```

---

## Confidence Criteria

- [ ] Qdrant service starts with `docker compose up` and persists data
- [ ] Qdrant dashboard accessible at `http://localhost:6333/dashboard`
- [ ] Ingestion pipeline successfully processes markdown files from `/docs/knowledge-base/`
- [ ] Collection `lejibe_knowledge` exists in Qdrant after ingestion
- [ ] Chunk metadata includes `source`, `doc_type`, `language`, `last_updated`
- [ ] Retrieval function returns 5–8 relevant chunks for a test query
- [ ] Admin ingest endpoint triggers re-ingestion (verify collection count changes)
- [ ] Re-ingestion clears old data before writing new data
- [ ] Placeholder knowledge base files cover product, features, FAQ, pricing, comparison
- [ ] All knowledge base content complies with `.clinerules` (no speed figures, no road context)

---

## Decisions to Watch For

- **Embedding model:** Start with `multilingual-e5-large` — strong French performance. Can upgrade to an API-based model later without changing the pipeline interface
- **Async ingestion:** The ingest endpoint should return immediately (202) and run ingestion in a background task — it could take 30–60 seconds for larger document sets
- **Collection management:** Recreate on ingest (delete + create) rather than upsert — simpler, avoids stale chunk accumulation
- **Knowledge base location:** `/docs/knowledge-base/` in the repo — version-controlled, easy to update. Ingested into Qdrant on first deploy and when admin triggers re-ingest
- **Metadata doc_type:** Enables metadata filtering in retrieval — e.g. if a user asks a pricing question, filter to `doc_type: pricing` for more precise context

---

## Notes

This task builds the foundation for the chat widget (Task 9) — the retrieval function is the key output. Task 9 will call `retrieve()` to get context before building the Claude prompt. The knowledge base content is placeholder for now — JB will provide real technical documentation, which gets ingested via the admin endpoint. See `docs/CHAT_WIDGET_ARCHITECTURE.md` for the full RAG pipeline design.

**Depends on:** Task 3  
**Blocks:** Task 9
