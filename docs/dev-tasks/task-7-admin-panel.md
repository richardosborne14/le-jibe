# Task 7: Admin Panel

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 3 output (admin API endpoints), Task 4 output (SvelteKit routing and global styles)  
**Output:** Working admin interface for viewing signups and managing blog posts  
**Estimated Time:** 1–2 sessions (~90 min)

---

## Subtasks

- **7.1** — `/admin` login page (static token, no user accounts yet)
- **7.2** — `/admin/signups` — table view of all signups, CSV export button
- **7.3** — `/admin/posts` — list posts with published status
- **7.4** — `/admin/posts/new` — write + preview + publish form
- **7.5** — `/admin/posts/[id]/edit` — edit existing post

---

## Cline Prompt

```
Can we please plan task 7 — Admin Panel?

Reference:
- README.md (design language, though admin can be simpler/more functional)
- ROADMAP.md (subtasks 7.1–7.5)
- CLAUDE_RULES.md
- Backend admin endpoints:
  - GET /api/admin/signups (Bearer token auth)
  - POST /api/admin/posts (Bearer token auth)
  - PATCH /api/admin/posts/{id} (Bearer token auth)
- Existing frontend code from Task 4

We need:
1. /admin login page:
   - Simple token input field
   - Store token in sessionStorage (or Svelte store)
   - Redirect to /admin/signups on success
   - No user accounts — just a shared admin token

2. /admin/signups:
   - Table: first_name, email, profile_type, created_at
   - Sorted by created_at desc (newest first)
   - CSV export button (client-side generation from table data)
   - Count badge showing total signups

3. /admin/posts:
   - Table: title, published status (badge), published_at, created_at
   - Link to edit each post
   - "New post" button → /admin/posts/new

4. /admin/posts/new:
   - Title input
   - Markdown editor (textarea is fine for MVP — no fancy editor)
   - Live preview pane (rendered markdown, same styles as public blog)
   - "Save as draft" and "Publish" buttons
   - After save, redirect to /admin/posts

5. /admin/posts/[id]/edit:
   - Same form as new, pre-filled with existing data
   - Additional "Unpublish" option if currently published

6. All admin pages protected: redirect to /admin login if no token in store

Admin design can be simpler than the public site — functional over pretty.
But still use the same fonts and colour palette for consistency.
```

---

## Confidence Criteria

- [ ] Login page accepts correct token, rejects wrong token
- [ ] All admin pages redirect to login if not authenticated
- [ ] Signups table displays all signups with correct data
- [ ] CSV export downloads a valid CSV file with all signups
- [ ] Posts list shows all posts (published and unpublished) with status badges
- [ ] New post form creates a post via API
- [ ] Markdown preview renders correctly in real-time
- [ ] Publish button sets post as published
- [ ] Edit form loads existing post data
- [ ] Edit form saves changes correctly
- [ ] Unpublish toggles published status

---

## Decisions to Watch For

- **Token storage:** `sessionStorage` means token clears on tab close — that's fine for admin
- **Markdown editor:** Plain `<textarea>` with a side-by-side preview is perfectly adequate for MVP. No need for CodeMirror or ProseMirror
- **CSV export:** Generate client-side with `Blob` + `URL.createObjectURL`. Don't build a server-side CSV endpoint for MVP
- **Auth guard:** Use a Svelte layout load function that checks for the token and redirects if missing
- **Form validation:** Require title and body for posts. Slug is auto-generated server-side

---

## Notes

The admin panel is a tool for one person (JB). It doesn't need to be beautiful — it needs to work reliably. Focus on functionality over polish. The most important flow to test: login → write post → preview → publish → verify it appears on public `/blog`.

**Depends on:** Task 3, Task 4  
**Blocks:** Task 8
