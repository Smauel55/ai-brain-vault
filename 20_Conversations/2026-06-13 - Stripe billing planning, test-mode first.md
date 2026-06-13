---
created: 2026-06-13
updated: 2026-06-13
tags: [conversation]
project: "[[Caught Up AI]]"
---

# 2026-06-13 — Stripe billing planning, test-mode first

## Context

Samuel wants to start implementing Stripe so the site is functional and he can test the
flow before going live. A SECOND Claude session was concurrently editing the Base44 app
(email buttons + /manage customization). He asked whether work could proceed safely without
interference.

## Key points

- Real collision surface is **Base44, not the vault.** Both the button/customization work
  and Stripe live in the same Base44 app, and Base44 **Publish ships ALL pending drafts at
  once**, so two sessions editing Base44 risks shipping half-finished work live.
- Vault is safe (sync never deletes, newest-wins), so writing the plan here is conflict-free.
- Key unlock: a **Stripe Payment Link in test mode** gives a real, clickable checkout with
  **zero code and zero Base44**, so the "test how it works" goal is fully isolated.

## Decisions

- **Proceed, scoped to "Stripe + plan only, no Base44"** (Samuel's pick). No Base44 edits,
  no Publish, until the other session is clear.
- **Two-phase plan:** Phase 1 (now, isolated) = test-mode account + product + price + free
  trial + Payment Link + test-card walkthrough. Phase 2 (later, collides) = Base44 wiring
  (webhook/connector -> `Teacher.subscription_status`).
- Pricing left as PLACEHOLDER ($89/yr + 7-day trial); real number is still OPEN.
- Filed the plan-of-record: `10_Projects/Caught Up AI/Billing-Stripe.md`.

## Action items

- [ ] Samuel — create/log in to Stripe (use the u.northwestern.edu email), confirm Test
      mode ON; report account status (fresh vs existing) + whether he wants Claude to drive
      the dashboard via the Chrome extension or be walked through it.
- [ ] Then — Segment 2: product + annual price + free trial, generate a test Payment Link.
- [ ] Before any LIVE billing — fix the Teacher read-leak; set up business entity + real
      address (already on the August-launch reminder).

## New knowledge to file

Nothing reusable beyond the project; the design lives in [[Billing-Stripe]].

## Open threads

- Phase 2 integration fork: Base44 native Stripe connector vs custom function + webhook
  (decide when the Base44 session is clear).
- Final pricing number/trial length.

Related: [[Billing-Stripe]], [[Delivery-Stack]], [[2026-06-12 - Product pipeline, resources, pricing]].
