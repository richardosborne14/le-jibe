# Task 4: SvelteKit Frontend — Landing Page

**Status:** Not started | **Target Confidence:** 8/10

**Input:** Task 1 output (SvelteKit scaffold), README.md (design language), `docs/landing-page-examples/lejibe-landing.html` (approved design), `docs/LANDING_PAGE_CONTENT_BRIEF.md`  
**Output:** Complete landing page with all sections, matching brand aesthetic, content aligned with brief  
**Estimated Time:** 2–3 sessions (~2–3 hours)

**Design reference:** `docs/landing-page-examples/lejibe-landing.html` — confirmed by JB. All UI follows this aesthetic.

---

## Subtasks

- **4.0** — Font swap: replace any Syne references with Outfit throughout codebase
- **4.1** — SvelteKit project scaffold (routing, fonts, CSS variables matching brand)
- **4.2** — Nav component (fixed, logo, links, CTA button)
- **4.3** — Hero section (headline, video embed slot, NO speed or spec stats)
- **4.4** — Story section (JB narrative — complete device framing, not add-on)
- **4.5** — Problem/solution section (why existing options fail, Le Jibé's answer)
- **4.6** — Features section (base + front wheel, custom seat, joystick — complete device framing)
- **4.7** — Pricing section (€9,800 delivered, financing mention, no reimbursement complexity)
- **4.8** — Ticker/marquee strip
- **4.9** — Footer

---

## Cline Prompt

```
Can we please plan task 4 — SvelteKit Frontend: Landing Page?

Reference:
- README.md (design language: dark bg #0D0D0B, amber accent #D4860A, Outfit/Instrument Sans/Instrument Serif fonts)
- ROADMAP.md (subtasks 4.0–4.9)
- .clinerules (CRITICAL: no speed figures, no road use, no medical language)
- docs/landing-page-examples/lejibe-landing.html (approved design)
- docs/LANDING_PAGE_CONTENT_BRIEF.md (full section-by-section content spec)

We need:
1. SvelteKit project scaffold in frontend/ with:
   - Global CSS: variables matching brand (colours, fonts, spacing)
   - Google Fonts loaded: Outfit (display), Instrument Sans (body), Instrument Serif (accent italic)
   - ⚠️ NO Syne — confirmed replaced by Outfit
   - Base layout component with <slot/>
   - Routing: /, /blog, /blog/[slug], /admin/*

2. Landing page sections (all on /), content in French, following the narrative arc in the content brief:

   Nav: fixed top, logo "Le Jibé" (Outfit, clean), links (Le fauteuil · L'histoire · Nous contacter), CTA "S'inscrire" (amber)

   Hero: strong headline (options: "Mobilité sans compromis." / "Conçu de l'intérieur." / "Le fauteuil qui n'existait pas."), one-sentence sub-headline describing the complete device, YouTube embed slot (placeholder div — JB provides URL later).
   ⚠️ NO stat strip with speed/range/weight. Replace with 4 capability badges: "Tout-terrain", "Siège sur mesure", "Roue stabilisatrice", "Contrôle par joystick"

   Problem section (NEW): editorial prose explaining why every existing option is a compromise — no front wheel → fall risk, sloped seats users can't transfer into, car-loading impossible, 5-year reimbursement lock-in. Ends with Le Jibé's answer: keep your wheelchair, use your reimbursement for that, Le Jibé is your second device. Tone: factual, no dramatic flair.

   Story: JB is paraplegic, engineer. Built the thing that didn't exist. Photo placeholder. Signature block: "Jean-Baptiste — Fondateur, ingénieur & premier utilisateur". Direct and factual — the story sells itself.

   Features (3 cards, complete device framing):
   - Card 1: Base Segway + roue avant stabilisatrice — all-terrain wheels, gyroscopic stabilisation, front wheel reduces fall risk, mounts curbs, works on grass/gravel/tile/uneven surfaces. NO speed mention.
   - Card 2: Siège carbone sur mesure — 3D-printed carbon fibre, fitted to user's body dimensions, flat open sides OR supported sides for different transfer methods, user keeps their own cushion.
   - Card 3: Joystick & contrôle intuitif — rigid-mount joystick, gentle push tips the frame → Segway moves, body movement does NOT cause displacement, 360° rotation, natural control in minutes.

   Pricing section (NEW): €9,800 livré. Financing mention (details Phase 2). Key framing: "Votre fauteuil classique reste votre solution principale. Le Jibé est votre outil de liberté quotidienne."

   Signup placeholder: anchor #signup — the actual form component is Task 5. Leave a clearly labelled placeholder div.

   Chat widget placeholder: floating button placeholder, bottom-right — the actual widget is Task 9.

   Ticker/marquee: horizontal scrolling text strip with brand phrases.

   Footer: "Le Jibé — Dordogne, France", contact email, mentions légales link. Small text: "Destiné à un usage privé."

3. Design principles (from content brief):
   - French. Always.
   - Direct, factual, warm but not sentimental
   - Engineering pride, not medical pity
   - Short sentences. No superlatives.
   - No speed figures. No road context. No medical language.
```

---

## Confidence Criteria

- [ ] Page loads at `http://localhost:5173` with Outfit, Instrument Sans, Instrument Serif
- [ ] No reference to Syne anywhere in the frontend
- [ ] Nav is fixed and all links scroll/route correctly
- [ ] Hero has headline, sub-headline, video placeholder, and capability badges (NOT speed stats)
- [ ] Problem/solution section exists with correct narrative (no medical language, no road context)
- [ ] Story section has JB narrative, photo placeholder, signature block
- [ ] Features grid uses "complete device" framing (NOT "detachable base" or "add-on")
- [ ] Pricing section shows €9,800 and "outil de liberté" framing
- [ ] Ticker/marquee animates
- [ ] Footer contains all required elements including "Destiné à un usage privé" small text
- [ ] `#signup` anchor exists for Task 5
- [ ] Chat widget placeholder exists bottom-right for Task 9
- [ ] Responsive: works on mobile (375px), tablet (768px), desktop (1280px+)
- [ ] All text is in French
- [ ] Zero speed figures, road references, or medical language anywhere

---

## Decisions to Watch For

- **CSS approach:** Scoped Svelte styles + global CSS variables — cleanest for this project
- **Fonts:** Load from Google Fonts CDN. Order: Outfit (display, 400/600/700), Instrument Sans (body, 400/500), Instrument Serif (italic accent, 400 italic)
- **Images:** Use placeholder images/SVGs for now — real photos from JB come later
- **YouTube embed:** Placeholder `<div>` with aspect ratio and play button SVG — NOT an actual `<iframe>` yet (faster page load, cleaner)
- **Problem section:** This is new — content brief has the key points. Write as editorial paragraphs, not a bullet list
- **Pricing section:** This is new — no BNPL details yet (Phase 2), just the €9,800 figure and the framing copy
- **Responsive strategy:** Mobile-first CSS with breakpoints at 768px and 1280px
- **Animation:** Scroll reveals are fine, nothing heavy — the content is the focus

---

## Notes

This is the most visually important task. The design reference is confirmed: `docs/landing-page-examples/lejibe-landing.html`. The font change from Syne to Outfit is also confirmed — check for any Syne reference in the HTML examples and replace when implementing. The Problem and Pricing sections are entirely new (not in the original HTML template) and need to be inserted into the narrative arc at the right points. Full content spec is in `docs/LANDING_PAGE_CONTENT_BRIEF.md`.

**Depends on:** Task 1  
**Blocks:** Task 5, Task 6, Task 7
