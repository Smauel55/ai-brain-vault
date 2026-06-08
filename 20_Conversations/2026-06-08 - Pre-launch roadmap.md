---
created: 2026-06-08
updated: 2026-06-08
tags: [conversation, caught-up-ai, launch, strategy]
project: "[[Caught Up AI]]"
---

# 2026-06-08 — Pre-launch roadmap

## Context

Samuel feels the product is a few weeks of testing from launch and asked for the big-picture list of everything needed before going live, including business-level setup (pricing, entity, payments).

## Key points

- **Timing reframe (the main strategic note):** launch date should be set by the school calendar, not by when testing finishes. AP Lang runs Aug–May; teachers choose tools over summer / first weeks of school. High-leverage window is **late July to early September** for fall adoption, which aligns with The Garage (Sept 2026). A great product launched in July sells far worse than the same product in late August. Use any slack time (e.g. July) for business setup, launch into the new school year.
- **Two most underrated items:** (1) daily operational reliability — the real product is "a correct, accurate, neutral Opener goes out every morning, hands-off," not just good prose; (2) launch timing vs the school calendar.

## Pre-launch workstreams (parallel once product gate clears)

1. **Product readiness (the gate):** pass the human AP Lang teacher panel blind test; prove the daily generate→QA→render→deliver pipeline runs without hand-fixing; lock the QA gate (accuracy, neutrality, tag/citation lint).
2. **Pricing/packaging:** per-teacher seat to start (department/site license as a manual quote); annual billing aligned to school year + monthly option; free trial or free weekly tier; research teacher/department willingness-to-pay; founding-cohort price.
3. **Money plumbing:** Stripe recurring subscriptions wired into the site; signup/access/cancel flow (check Base44 vs Stripe coverage).
4. **Legal/formation:** LLC + EIN + business bank account; lean on Northwestern/The Garage legal clinic before paying a lawyer; ToS + Privacy Policy; AI-disclosure + content disclaimer; sales-tax awareness (Stripe Tax).
5. **Delivery/front-end:** reliable automated daily delivery (email w/ PDFs or portal); finish the landing page (value prop, public sample Opener, pricing, signup) — site is live but paused at content stage.
6. **Go-to-market:** beachhead = Samuel's own AP Lang teacher + meeting contacts as founding subscribers; channels = AP Lang FB groups, AP Community, Reddit, NCTE, TPT; discounted founding-cohort offer for feedback/testimonials.
7. **Support/ops:** support email, refund/cancellation policy, churn handling; daily content op as a standing routine; track signups, trial→paid conversion, churn from day one.

## Suggested critical path

1. Pass teacher panel + lock daily QA gate. 2. In parallel: pricing, entity, Stripe, ToS/Privacy. 3. Delivery pipeline + landing page. 4. Founding-cohort soft launch. 5. Public signups timed to back-to-school.

## Open / next

- Offered to build a tracked `Launch-Checklist.md` in 10_Projects/Caught Up AI/ (owners + status per item) to drive the run-up. Awaiting Samuel's go-ahead.

## Related

[[Caught Up AI]], [[Website-Setup]], [[Content-Sourcing]], [[Blind-Test-Protocol]]
