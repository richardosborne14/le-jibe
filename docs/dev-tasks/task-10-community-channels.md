# Task 10: Community Channels

**Status:** Not started | **Target Confidence:** 9/10

**Input:** Task 5 output (signup form with post-signup confirmation), `docs/COMMUNITY_MARKETING_STRATEGY.md`  
**Output:** WhatsApp and Telegram groups live, join links integrated into the landing page and post-signup flow  
**Estimated Time:** 1 session (~45 min) — mostly manual setup, minimal dev work

---

## Subtasks

- **10.1** — Create WhatsApp group (JB creates, adds Richard as co-admin)
- **10.2** — Create Telegram channel (secondary — mirrors WhatsApp content)
- **10.3** — Write welcome message template for new members
- **10.4** — Add join links to landing page (in footer and post-signup confirmation section)
- **10.5** — Add join links to post-signup confirmation message in the signup form component

---

## Cline Prompt

```
Can we please plan task 10 — Community Channels?

Reference:
- ROADMAP.md (subtasks 10.1–10.5)
- docs/COMMUNITY_MARKETING_STRATEGY.md (community channels section)
- Existing frontend code from Tasks 4 and 5 (landing page, signup confirmation)

Subtasks 10.1–10.3 are manual (JB creates the groups) — document what needs to be set up and provide the welcome message template. Do not attempt to automate.

For the dev work (10.4–10.5):

1. Landing page — add community join section:
   After the signup section, or integrated into the footer area:
   - WhatsApp join button/link (opens wa.me/... invite link)
   - Telegram join button/link (opens t.me/... invite link)
   - Brief copy: "Rejoignez la communauté Le Jibé — questions, mises à jour, sessions live avec Jean-Baptiste."
   - Styling: matches brand (amber CTA buttons or text links depending on visual context)

2. Signup form (Task 5 component) — update post-signup success state:
   After successful signup confirmation message, add:
   - "Rejoignez aussi notre groupe WhatsApp pour suivre le développement en direct."
   - WhatsApp join button
   - Telegram join button (secondary)
   - Keep it optional — not pushy

3. Placeholder links:
   Use placeholder URLs for now (e.g. https://chat.whatsapp.com/PLACEHOLDER)
   JB will provide the real invite links once groups are created.
   Add a TODO comment in the code marking where to replace the URLs.

Welcome message template (for manual use when new members join WhatsApp):
   Write a short, warm welcome message in French that:
   - Introduces Le Jibé in 2 sentences
   - Explains what the group is for (updates, questions, live sessions)
   - Sets expectations (JB posts regularly, members can ask anything)
   - Ends with an invitation to introduce themselves
```

---

## Confidence Criteria

- [ ] WhatsApp group created (manual — JB confirms)
- [ ] Telegram channel created (manual — JB confirms)
- [ ] Welcome message template written in French and approved by JB
- [ ] Community join links appear on landing page
- [ ] Community join links appear in post-signup confirmation
- [ ] Links use placeholder URLs with TODO comments for easy replacement
- [ ] Copy matches brand tone (warm, direct, not pushy)
- [ ] Join buttons work on mobile (WhatsApp deep links open the app)

---

## Decisions to Watch For

- **WhatsApp vs Telegram priority:** WhatsApp is primary (lower barrier for French disability community). Telegram is secondary/broadcast. Both links provided wherever community is mentioned
- **Invite link management:** WhatsApp invite links can be reset (do this if the link is shared too widely and attracts spam). Telegram channels have permanent usernames
- **Moderation:** JB + Richard moderate both. Keep it simple — no bots, no auto-responses for now
- **Landing page placement:** Community section should feel like a natural next step after signing up — not a distraction from the signup form itself

---

## Notes

This is mostly a manual task for JB to set up the groups. The dev work is minor: adding 2–3 links to the landing page and signup confirmation. The welcome message template is the most important output — it sets the tone for the community from day one. See `docs/COMMUNITY_MARKETING_STRATEGY.md` for the full community strategy and what these channels are meant to do in the broader funnel.

**Depends on:** Task 5 (signup form, for post-signup integration)  
**Blocks:** Nothing directly — but should be live alongside the landing page launch
