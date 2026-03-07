# Learnings

Running log of solutions, decisions, and gotchas. Check this at the start of each task.

---

## 2026-03: Product pivot — complete device, not detachable base

**Context:** Le Jibé was originally conceived as a detachable motorised base that attaches to existing wheelchair frames (e.g. TraceS). After JB's analysis of the market and user feedback, the product is now a **complete standalone mobility device**.

**Why:** The TraceS frame has deal-breaker limitations for a large portion of the target market:
- Sloped seat sides prevent slide-transfer for many paraplegic users
- Combined weight (TraceS + Jibé base) too heavy for solo car loading
- Committing to TraceS means 5 years locked in (reimbursement cycle) if unsatisfied
- TraceS itself costs €7,000+ before adding the Jibé

**New model:** JB buys the Segway base, builds the steel frame, 3D-prints a carbon fibre seat custom-fitted to each user's body dimensions. User transfers their own cushion. €9,800 delivered.

**Apply to:** All product descriptions, landing page copy, feature explanations, chat widget knowledge base.

---

## 2026-03: No regulatory track — private use only

**Context:** The 30+ km/h speed and lack of medical device certification mean Le Jibé cannot be legally used on public roads in France. The standard industry approach for similar devices is to sell with a private-use disclaimer.

**Decision:** No CERAH outreach. No LPPR registration. No reimbursement pathway. Direct-to-customer only.

**Apply to:** All public-facing copy must avoid speed figures, road-use implications, and medical device language. Checkout disclaimer: "Destiné à un usage privé, non homologué pour la voie publique."

---

## 2026-03: Landing page font — Syne replaced by Outfit

**Context:** JB approved the first dark template (lejibe-landing.html) but found Syne (display font) too unusual. Directions A and B (Éditoriale and Atelier) were rejected — the original dark template is the one to implement.

**Decision:** Swap Syne → Outfit (geometric, clean, legible, Google Fonts). Keep Instrument Sans (body) and Instrument Serif (accent italic).

**Apply to:** All frontend work, design tokens, CSS variables.

---

## 2026-03: Reimbursement landscape post-Dec 2025 reform

**Context:** The December 2025 Sécurité Sociale reform has caused widespread reimbursement refusals across JB's network. Appeals with corrected line-by-line nomenclature pricing are the recommended approach.

**Relevance to Jibé:** This validates the direct-to-customer model. Users can't rely on the state for anything beyond basic classic wheelchairs. Le Jibé's pitch is: "use your reimbursement for your classic chair, buy Le Jibé separately."

**Apply to:** Pricing section copy, chat widget responses about cost/reimbursement, marketing messaging.

---

## 2026-03: RGPD health data — separate storage, explicit consent

**Context:** Disability profile data is "données sensibles" under Article 9 GDPR. Requires explicit, informed, specific consent — not just a checkbox.

**Decision:** Separate `user_profiles` table, linked by FK to signups. Consent timestamp required before any write. Anonymous chat mode available. Right to erasure implemented.

**Apply to:** All backend work involving profile data, chat widget consent flow, admin data views.

---

## Quick Reference

| Issue | Solution | Entry |
|-------|----------|-------|
| Product framing | Complete device, not add-on | 2026-03 pivot |
| Speed mentions | Never — use "fluide", "réactif" | 2026-03 regulatory |
| Display font | Outfit (replaced Syne) | 2026-03 font |
| Health data storage | Separate table, explicit consent | 2026-03 RGPD |
| Reimbursement messaging | "Keep your classic chair, buy Jibé separately" | 2026-03 reimbursement |
