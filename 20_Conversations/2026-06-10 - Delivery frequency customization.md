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

## Open / next

- Confirm the minor defaults above.
- Build phase (not started): day-set field on signup + the magic-link page on Base44; segment the daily send by each teacher's day-set in the ESP (Resend). Easy in both Phase 0 (send to today's segment) and Phase 1 (semi-auto scheduled send).
- Not yet written into the spec files; this note plus the memory update capture the decision.
