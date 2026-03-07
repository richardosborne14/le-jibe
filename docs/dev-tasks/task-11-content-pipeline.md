# Task 11: Content Pipeline

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 4 (landing page with video/media slots), Task 8 (RAG knowledge base), Task 9 (chat widget), `docs/LANDING_PAGE_CONTENT_BRIEF.md`, `docs/COMMUNITY_MARKETING_STRATEGY.md`  
**Output:** YouTube/Instagram embeds live, RAG knowledge base populated with real product content, first blog post published  
**Estimated Time:** 2 sessions — depends on JB providing assets

---

## Subtasks

- **11.1** — Integrate YouTube video embed into landing page hero (replace placeholder once JB provides URL)
- **11.2** — Integrate Instagram post embeds where applicable (replace placeholders)
- **11.3** — Write initial RAG knowledge base content (product specs, FAQ, pricing, comparison) — awaiting technical docs from JB
- **11.4** — Trigger RAG re-ingestion via admin endpoint once knowledge base content is ready
- **11.5** — Write and publish first blog post via admin panel

---

## Cline Prompt

```
Can we please plan task 11 — Content Pipeline?

Reference:
- ROADMAP.md (subtasks 11.1–11.5)
- docs/LANDING_PAGE_CONTENT_BRIEF.md (assets needed from JB, video/photo slots)
- docs/COMMUNITY_MARKETING_STRATEGY.md (content calendar, first blog post ideas)
- Existing frontend code from Task 4 (landing page with video/embed placeholders)
- RAG knowledge base from Task 8 (/docs/knowledge-base/ directory)
- Admin panel from Task 7 (for publishing blog posts)

This task is partially gated on JB providing assets. Structure it in two parts:

PART A — Dev work (can do now, before assets arrive):

1. YouTube embed component (src/lib/components/VideoEmbed.svelte):
   - Accepts a youtubeId prop
   - When youtubeId is provided: renders a privacy-respecting YouTube embed (use youtube-nocookie.com domain)
   - When youtubeId is null/empty: shows the existing placeholder div with play button
   - Add a TODO comment: "Replace YOUTUBE_VIDEO_ID with JB's video URL once provided"
   - 16:9 aspect ratio, responsive

2. Instagram embed slot:
   - For MVP, Instagram embeds load via Instagram's oEmbed API or their embed script
   - Create a placeholder component that shows the embed when a URL is provided
   - Add TODO comment for JB's Instagram post URLs

3. RAG knowledge base structure:
   - Ensure /docs/knowledge-base/ directory has the right file structure
   - Files: product-overview.md, features-spec.md, faq.md, pricing.md, comparison.md
   - Fill with best-effort content based on README.md and existing docs
   - Add clear TODO comments for sections awaiting JB's technical documentation
   - Mark each doc_type in frontmatter: --- doc_type: spec/faq/pricing/comparison ---

PART B — Content (blocked on JB providing assets):

4. Once JB provides YouTube URLs:
   - Replace YOUTUBE_VIDEO_ID placeholder in the VideoEmbed component
   - Test embed loads correctly and respects privacy (nocookie domain)

5. Once JB provides technical documentation:
   - Update /docs/knowledge-base/ files with real specs (weight, battery, range, charging time)
   - Do NOT add speed figures — these are excluded from all public content
   - Trigger re-ingestion via POST /api/admin/rag/ingest
   - Test chat widget with real knowledge base: ask about pricing, features, suitability

6. First blog post (JB writes, Richard edits, publish via admin panel):
   Suggested topic: "Pourquoi j'ai construit Le Jibé" — JB's story in his own words
   Tone: direct, personal, engineering perspective
   Length: 600–800 words
   No speed figures, no road context, no medical framing
   Publish via /admin/posts/new once admin panel (Task 7) is live
```

---

## Confidence Criteria

- [ ] VideoEmbed component renders placeholder when no youtubeId provided
- [ ] VideoEmbed component renders privacy-respecting embed when youtubeId provided
- [ ] Instagram embed slot exists with clear TODO placeholder
- [ ] `/docs/knowledge-base/` contains all 5 content files with correct structure
- [ ] Knowledge base files comply with `.clinerules` (no speed figures, no road context, no medical language)
- [ ] doc_type frontmatter present in all knowledge base files
- [ ] TODO comments clearly mark sections awaiting JB's content
- [ ] Once JB provides video URL: embed appears on landing page
- [ ] Once knowledge base updated: RAG re-ingestion triggers successfully
- [ ] Once re-ingested: chat widget answers questions accurately from new content
- [ ] First blog post published and visible on `/blog`

---

## Decisions to Watch For

- **YouTube privacy:** Use `youtube-nocookie.com` instead of `youtube.com` for embeds — GDPR-friendlier, no tracking cookies without consent
- **Lazy loading embeds:** Don't load YouTube iframe on page load — use a click-to-load approach (show thumbnail + play button, load iframe on click). Better performance
- **Knowledge base content:** Write from what's known in the README and product docs. Mark anything uncertain with `<!-- TODO: verify with JB -->`. Better to have something to edit than a blank file
- **First blog post authorship:** JB writes the first post — not us. Richard can help edit for clarity and flow, but the voice must be JB's. Don't ghost-write unless explicitly asked
- **RAG after update:** After any knowledge base content update, the admin must trigger re-ingestion. Remind JB this step is required. Consider adding a note to the admin panel

---

## Notes

This task has two modes: dev work (now) and content work (when JB provides assets). Don't block on JB — do the dev scaffolding first, then slot in real content as it arrives. The RAG knowledge base placeholder content is critical to get right from day one — it's what the chat widget will use until JB provides real specs. Every piece of content, including RAG docs, must comply with `.clinerules`. See `docs/LANDING_PAGE_CONTENT_BRIEF.md` for the full list of assets needed from JB.

**Assets still needed from JB:**
- [ ] YouTube video URLs (everyday use footage)
- [ ] Instagram post URLs
- [ ] Photo of JB in the device (for story section)
- [ ] Technical documentation (weight, range, charging time, dimensions)
- [ ] First blog post text (JB writes)

**Depends on:** Task 4 (landing page), Task 8 (RAG knowledge base), Task 9 (chat widget), Task 7 (admin panel for blog)  
**Blocks:** Task 12 (deploy — want real content live before go-live)
