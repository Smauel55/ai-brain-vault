---
created: 2026-06-10
updated: 2026-06-10
tags: [conversation, caught-up-ai, product, customization, delivery, pricing]
project: "[[Caught Up AI]]"
---

# 2026-06-10 — Delivery frequency customization

## Context

Second topic of the session (after [[2026-06-10 - Teacher feedback, headnotes|headnotes]]). Some teachers will want openers only 1 to 3 days a week, not daily. Samuel wants teachers to choose how often and which days they receive. The question he raised: does this level of customization need a portal or website login system?

## Decision (three forks, all locked to the lean option)

1. **Mechanism = magic-link preferences page. No portal/login.**
   - Schedule is set on the existing 4-minute signup form (default all five weekdays; deselect to taste).
   - A signed "change my schedule" link in every email footer opens a no-password preferences page (days, political dial, unsubscribe). Cheap on Base44, no auth system to maintain.
   - A full login portal is deferred until several account-reasons co-exist at once (multi-seat / department management, billing self-service, a content archive teachers browse). Frequency alone never justifies the support surface (password resets, login tickets).
2. **Content model = broadcast + edition-rolled rotation.**
   - One edition is published per day; frequency is a receive-filter on which days a teacher gets it. Content load, print-and-go, and QA all unchanged.
   - Register rotation advances by **edition date, not weekday**, so a part-week teacher still cycles the whole palette over time (a Mondays-only teacher cycles the registers over several weeks).
   - Rejected per-teacher streams (per-teacher queue state, multiplies QA, wrong for a manual / semi-auto MVP).
   - Note: the rotation grid in [[Generation-Briefs]] already specifies rolling advance when publishing fewer than seven days, so this is a config choice, not new work.
3. **Pricing = one price; frequency is free.**
   - Not a tier. No cost basis (one edition serves all) and it avoids "$20 for 8 openers a month" math.
   - Frequency reframed as a churn / retention lever: an overwhelmed teacher dials down to one day instead of canceling.

## Design details

- Teachers pick specific **days** (M-F), not just a count: AP Lang meets on fixed schedules (MWF, etc.).
- Consistent with the political-dial precedent ([[2026-06-07 - Opener customization strategy]]): low-cardinality, set at signup, changeable later, no parallel pipelines.

## Defaults (confirmed 2026-06-10)

- Weekdays only; no weekend editions. CONFIRMED.
- 1 to 5 days a week allowed; default = all 5. CONFIRMED.
- **Summer (June to July) auto-throttles to ONE opener a week for everyone.** Reason: cuts generation cost roughly 80% over those weeks (broadcast, so it is one edition produced instead of five) while keeping the habit alive in the inbox. Billing is untouched, so this is consistent with the prior no-billing-pause / summer-as-a-feature decision; it REPLACES a pause toggle (no separate pause offered). Normal cadence resumes in August for back-to-school (also the launch window).
- Open / deferred: treat the summer window as an operator-controlled setting, not a hard date, for late-return districts; a summer-school override for a teacher who wants more; both deferred.

## Built (same session, 2026-06-10): the /manage page on Base44

Claude drove Samuel's browser (Chrome extension) into the Base44 editor and built the page in the production app (the one holding the verified caughtupai.com domain; "Caught Up AI (Copy)" is a backup). All changes are in PREVIEW, NOT PUBLISHED.

- Access decision first: the page is gated subscriber-vs-stranger, not paid-vs-unpaid. Unlisted route /manage + signed token in the email footer (?t=manage_token). Trial users CAN customize (it drives conversion); strangers see only an invalid-link message. No nav/footer/sitemap link anywhere.
- Created Teacher entity: full_name, email, school, delivery_days (Mon-Fri list, default all), political_content (neutral/civic, default neutral), time_zone (IANA, default America/New_York), manage_token (auto-generated unique), status (trial/active/canceled, default trial). Built to be the same record the future signup form writes.
- Page behavior (all verified by hand in preview): token lookup; invalid/no token shows only the error line; valid token shows prefilled form (delivery-day toggles, political radio, US timezone dropdown, Save) plus a separated, muted unsubscribe block and the 6am/summer footer note.
- 3 sample Teacher records created for testing (Sarah Chen all-days/Eastern/neutral/trial; Marcus Webb MWF/Central/civic/active; Priya Nair TuTh/Pacific/neutral/trial), each with a /manage?t=... test URL (in the Base44 chat log).
- BUG FOUND AND FIXED during testing: unsubscribe originally fired off one stray click (native confirm + layout shift + buttons missing type="button" submitting the form). Fix: in-page two-step confirm (Are you sure? / Yes, unsubscribe me / Keep my Openers), a "Changed your mind? Restore my subscription" link on the unsubscribed state, more spacing between Save and Unsubscribe. Second bug: the panel buttons were unwired (handler after an early return + state updates blocked behind a throwing async write); fixed by Base44 after a specific defect report.
- Final verified pass: no-token case; prefill per record; save persists across reload (Tue added to Marcus stuck); last-day guard blocks with "At least one delivery day must remain selected"; Keep dismisses; unsubscribe shows message + restore; restore returns and persists.

## Open / next

- PUBLISH is Samuel's call (pushes to caughtupai.com; /manage is unlisted so nothing visible changes for visitors; landing page untouched).
- Before real teachers use it: verify on the PUBLISHED app that an anonymous (token-only, no-login) visitor can save/unsubscribe (the builder noted an "unauthenticated write" error in preview; entity permissions may need explicit anonymous read/update scoping, and over-open permissions would let anyone enumerate Teacher records, so it needs scoping BOTH ways).
- Wire the token into the real flow when it exists: signup form creates the Teacher record; every email footer carries caughtupai.com/manage?t=TOKEN.
- Resend send-time segmentation by delivery_days + time_zone (the receive-filter half of the broadcast model).
- Spec files not yet updated with the delivery-frequency model; this note + memory carry it.
