# Task 6: Blog (Public)

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 3 output (working `/api/posts` and `/api/posts/{slug}` endpoints), Task 4 output (SvelteKit routing and global styles)  
**Output:** Public blog listing page and individual post pages with markdown rendering  
**Estimated Time:** 1 session (~60–90 min)

---

## Subtasks

- **6.1** — `/blog` listing page (cards: title, date, excerpt)
- **6.2** — `/blog/[slug]` post page (rendered markdown, back link)
- **6.3** — Markdown rendering (marked.js or similar, styled to brand)

---

## Cline Prompt

```
Can we please plan task 6 — Public Blog?

Reference:
- README.md (design language)
- ROADMAP.md (subtasks 6.1–6.3)
- CLAUDE_RULES.md
- Existing frontend code from Task 4 (global styles, layout, fonts)
- Backend endpoints: GET /api/posts (list), GET /api/posts/{slug} (single)

We need:
1. /blog listing page:
   - Fetches published posts from GET /api/posts
   - Displays as cards: title, published_at (formatted in French locale), excerpt
   - Cards link to /blog/{slug}
   - Empty state if no posts yet: "Aucun article pour le moment. Revenez bientôt !"
   - Matches brand aesthetic (dark bg, amber accents, editorial feel)

2. /blog/[slug] post page:
   - Fetches post from GET /api/posts/{slug}
   - Renders body_md as HTML (use marked.js or mdsvex)
   - Styled markdown: headings, paragraphs, lists, code blocks, images, links — all matching brand
   - Published date displayed (French locale)
   - Back link to /blog
   - 404 page if slug not found

3. Markdown rendering library:
   - Install marked (or similar) in frontend
   - Create a markdown style sheet that matches brand typography
   - Sanitize HTML output (DOMPurify or similar)

All text and dates in French.
```

---

## Confidence Criteria

- [ ] `/blog` lists published posts with title, date, excerpt
- [ ] Dates formatted in French (e.g., "15 janvier 2025")
- [ ] Cards link to correct `/blog/{slug}` pages
- [ ] Post page renders markdown correctly (headings, bold, lists, links, images)
- [ ] Markdown styling matches brand (not default unstyled markdown)
- [ ] Back link returns to `/blog`
- [ ] Empty state displays when no posts exist
- [ ] 404 displays for invalid slugs
- [ ] HTML output is sanitized (no XSS from markdown)
- [ ] Responsive on mobile

---

## Decisions to Watch For

- **Markdown library:** `marked` is simple and lightweight. `mdsvex` is overkill for rendering API content (it's for .svx files). Go with `marked` + `DOMPurify`
- **Date formatting:** Use `Intl.DateTimeFormat('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' })`
- **Code blocks:** Style them but don't over-invest — blog posts will mostly be narrative, not code
- **Image handling in markdown:** Images in markdown body will need to be absolute URLs (no local file upload yet)

---

## Notes

The blog serves two purposes: SEO and trust-building. Posts will cover the design/build process, the story behind Le Jibé, and accessibility topics. The design should feel editorial and premium — like reading a well-designed magazine blog, not a default markdown dump.

**Depends on:** Task 3, Task 4  
**Blocks:** Task 8
