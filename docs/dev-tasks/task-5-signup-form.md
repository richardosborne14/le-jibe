# Task 5: Signup Form (Wired to API)

**Status:** Not started | **Target Confidence:** 9/10

**Input:** Task 3 output (working `/api/signups` endpoint), Task 4 output (landing page with signup placeholder)  
**Output:** Working signup form on the landing page that creates signups in the database  
**Estimated Time:** 1 session (~45–60 min)

---

## Subtasks

- **5.1** — Signup form component (first name, email, profile type select)
- **5.2** — Wire to `POST /api/signups` with loading/success/error states
- **5.3** — Success confirmation UI (no page reload)

---

## Cline Prompt

```
Can we please plan task 5 — Signup Form wired to API?

Reference:
- README.md (design language)
- ROADMAP.md (subtasks 5.1–5.3)
- CLAUDE_RULES.md
- Existing frontend code from Task 4 (the signup placeholder section)
- Backend endpoint: POST /api/signups accepts {first_name, email, profile_type}

We need:
1. A Svelte component for the signup form with:
   - First name input (text)
   - Email input (email type)
   - Profile type dropdown: "Utilisateur de fauteuil roulant", "Aidant ou proche d'un utilisateur", "Professionnel de santé / ergothérapeute", "Autre"
   - Submit button: "Manifester son intérêt →"
   - Privacy note: "Aucun engagement. Désinscription possible à tout moment. Données stockées en UE."

2. Three states:
   - Default: form visible, button enabled
   - Loading: button shows spinner/disabled, inputs disabled
   - Success: form replaced with confirmation message (no page reload, smooth transition)
   - Error: inline error message (email already registered → specific message, other errors → generic)

3. Wire to POST /api/signups via fetch to /api/signups (nginx proxies this)

4. Basic client-side validation before submit (email format, required fields)

All text in French. Matches brand aesthetic from Task 4.
```

---

## Confidence Criteria

- [ ] Form renders in the signup section of the landing page
- [ ] All 3 fields work and validate client-side
- [ ] Submit creates a signup in the database (verify via admin endpoint or psql)
- [ ] Loading state shows during API call
- [ ] Success state replaces form with confirmation
- [ ] Duplicate email shows specific error message
- [ ] Invalid email shows validation error
- [ ] Empty required fields prevented from submitting
- [ ] No page reload on submit
- [ ] Works on mobile

---

## Decisions to Watch For

- **Profile type values:** Send English enum values to API (`user`, `caregiver`, `professional`, `other`) but display French labels
- **Error messages:** In French. "Cet email est déjà inscrit" for duplicates
- **Success message:** Something warm — "Merci ! Nous vous tiendrons informé(e) dès que Le Jibé sera disponible."
- **Form reset:** After success, don't show the form again (they've signed up). Maybe show a small "Inscrit ✓" badge

---

## Notes

This is a short, focused task but it's the single most important user interaction on the site. Test the full flow: fill form → submit → see success → check database. Also test error cases: duplicate email, missing fields, network error.

**Depends on:** Task 3, Task 4  
**Blocks:** Task 8
