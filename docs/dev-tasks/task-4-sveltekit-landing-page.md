# Task 4: SvelteKit Frontend — Landing Page

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 1 output (SvelteKit scaffold), README.md (design language), landing page examples in `docs/landing-page-examples/`  
**Output:** Complete landing page with all sections, matching brand aesthetic  
**Estimated Time:** 2–3 sessions (~2–3 hours)

**⚠️ DESIGN NOTE:** The exact landing page style hasn't been chosen yet. This task doc covers the structural requirements and sections needed regardless of which visual direction is picked. When starting this task, update the Cline prompt below with the chosen design reference.

---

## Subtasks

- **4.1** — SvelteKit project scaffold (routing, fonts, CSS variables matching brand)
- **4.2** — Nav component (fixed, logo, links, CTA button)
- **4.3** — Hero section (headline, stats, YouTube embed placeholder)
- **4.4** — Story section (JB narrative, photo slot)
- **4.5** — Features grid (3 cards: base, seat, joystick)
- **4.6** — Ticker/marquee strip
- **4.7** — Footer

---

## Cline Prompt

```
Can we please plan task 4 — SvelteKit Frontend: Landing Page?

Reference:
- README.md (design language: dark bg, amber accent, Syne/Instrument Sans/Instrument Serif fonts)
- ROADMAP.md (subtasks 4.1–4.7)
- CLAUDE_RULES.md
- [INSERT CHOSEN DESIGN REFERENCE HERE — e.g. docs/landing-page-examples/lejibe-landing.html]

We need:
1. SvelteKit project scaffold in frontend/ with:
   - Global CSS: variables matching brand (colours, fonts, spacing)
   - Google Fonts loaded: Syne, Instrument Sans, Instrument Serif
   - Base layout component with <slot/>
   - Routing: /, /blog, /blog/[slug], /admin/*

2. Landing page sections (all on /):
   - Nav: fixed top, logo "Le Jibé", links (L'histoire, Le fauteuil, Blog), CTA button "Manifester son intérêt"
   - Hero: headline, subtitle, stats row (speed, range, weight — placeholder values ok), YouTube embed placeholder
   - Story: JB narrative section with photo placeholder, editorial tone
   - Features: 3-card grid (base/Segway, seat/carbon fibre, joystick/control)
   - Ticker/marquee: horizontal scrolling text strip
   - Footer: logo, copyright, links (Blog, Contact, Mentions légales)

3. The signup section is Task 5 — leave an anchor/placeholder for it

Design rule: warm industrial editorial. This is a French performance brand, NOT medical equipment.
The page should feel premium, confident, and personal.

All content in French.
```

---

## Confidence Criteria

- [ ] Page loads at `http://localhost:5173` with correct fonts and colours
- [ ] Nav is fixed and all links scroll/route correctly
- [ ] Hero section has headline, stats, video placeholder
- [ ] Story section conveys the personal narrative
- [ ] Features grid displays 3 cards with icons/visuals
- [ ] Ticker/marquee animates smoothly
- [ ] Footer contains all required links
- [ ] Responsive: works on mobile (375px), tablet (768px), desktop (1280px+)
- [ ] Signup section has a visible placeholder/anchor
- [ ] Brand aesthetic matches the chosen design reference
- [ ] All text is in French

---

## Decisions to Watch For

- **CSS approach:** Scoped Svelte styles vs global CSS vs a utility framework? Scoped Svelte styles + global CSS variables is probably cleanest
- **Fonts:** Load from Google Fonts CDN, not self-hosted (simpler for MVP)
- **Images:** Use placeholder images/SVGs for now — real photos come later
- **YouTube embed:** Use a placeholder div with a play button, not an actual iframe (faster page load)
- **Responsive strategy:** Mobile-first CSS with breakpoints at 768px and 1280px
- **Animation:** Keep it subtle — scroll reveals are fine, nothing heavy

---

## Notes

This is the most visually important task. The landing page IS the product for MVP — it's what convinces people to sign up. Once the design direction is chosen, paste the specific reference file into the Cline prompt where indicated. The structure and sections above are stable regardless of style choice.

**Depends on:** Task 1  
**Blocks:** Task 5, Task 6, Task 7
