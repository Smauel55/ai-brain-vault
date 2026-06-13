---
created: 2026-06-13
updated: 2026-06-13
tags: [conversation, caught-up-ai, delivery, bugfix, security]
project: "[[Caught Up AI]]"
---

# 2026-06-13 — Manage save fix, email link colors, RLS leak found

## Context

Test run of the email product: the /manage magic-link page loaded fine but the Save button spun forever and never persisted. Also wanted the email's "Manage dates" and "Unsubscribe" links to have visible color. Diagnosed live in Chrome, fixed in Base44, published, verified by behavior.

## Key points

- Root cause of the Save hang: a day-format mismatch. The whole system stores/returns full capitalized weekday names (`Monday`..`Friday`), but `updateTeacherByToken` validated against three-letter codes `['Mon','Tue','Wed','Thu','Fri']`, so every save returned `400 {"error":"Invalid days: ..."}`. The page has no error handler, so the button spun forever.
- The same mismatch existed in two more places, both found and fixed in the same pass:
  - `pages/Manage` day chips carried short-code VALUES while prefill/stored data were full names, so prefilled days never highlighted and toggling a day injected a short code the backend rejected. Fixed: chips now use `{label:'Mon', value:'Monday'}` objects; selected-state, toggle, and Save payload all use the full-name value.
  - `sendTodaysEdition` recipient filter computed the weekday as a short code (`WEEKDAY_NAMES = ['Sun','Mon',...]`) and matched it against full-name `delivery_days`, so a real `live` broadcast would have matched ZERO teachers. Invisible until now because every test used `test` mode (skips the filter). Fixed: `WEEKDAY_NAMES` now full names.
- Email footer links recolored in `sendTodaysEdition`: "Change your delivery days" -> `#5b21b6` underlined; "Unsubscribe" -> `#6b7280` underlined (both were `#9ca3af` gray).
- Published the app (twice) and verified live by behavior: prefill now highlights all selected days; toggled Friday off -> Save returned `200 {"success":true}` with `["Monday".."Thursday"]`; reload confirmed persistence; restored Friday so the test record ended back at all five days.
- Fixes were driven through the Base44 agent chat with tightly-scoped single-line instructions (Enter sends; newlines fragment), reviewing each before/after diff before publishing.

## Decisions

- Canonical delivery-day format across the entire stack = full capitalized weekday names (`Monday`..`Sunday`). The /manage display labels stay short (`Mon`..`Fri`) but the stored value is the full name. Anything touching `delivery_days` must use full names.

## Action items

- [ ] CRITICAL SECURITY — re-lock the Teacher entity REST read without breaking `asServiceRole` reads. See Open threads. Blocks real launch.
- [ ] Optional: send a `test`-mode email to Samuel's inbox to eyeball the new link colors live.
- [ ] Delete the fake test Teacher records before any real broadcast (they are exposed by the leak and would also receive sends).
- [ ] Keep `10_Projects/Caught Up AI/email-template-v1.html` footer colors in sync with the live function if it's still used as the reference.

## New knowledge to file

None new beyond the project notes; the day-format canonical decision is captured in [[Delivery-Stack]] and the project memory.

## Open threads

- LIVE PII + CREDENTIAL LEAK (regression). An anonymous `GET /api/apps/6a1f286b511ece79b6ef3942/entities/Teacher` (credentials omitted) returns `200` with every teacher's `email` and `manage_token` (the magic-link secret). It regressed because the Teacher entity `read` was set back to `true` during 2026-06-12 debugging to unblock `asServiceRole` reads (Base44 quirk: `read:false` blocks even service-role reads). Only fake/test data exposed right now. The naive fix (`read:false`) re-breaks `getTeacherByToken` and the now-working Save. Needs a real fix: route all Teacher reads through service-role functions with the entity genuinely locked, or remove the entity from the public REST surface, or a proper RLS `user_condition`. Do NOT click the Base44 Permissions "Fix" banner (known false positive).
