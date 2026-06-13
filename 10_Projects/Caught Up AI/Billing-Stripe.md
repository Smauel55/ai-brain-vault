---
created: 2026-06-13
updated: 2026-06-13
tags: [project, caught-up-ai, billing, stripe, infrastructure]
project: "[[Caught Up AI]]"
---

# Caught Up AI Billing (Stripe)

How a teacher goes from "wants it" to "paying subscriber." The billing box of the
[[Delivery-Stack]]. Started 2026-06-13. Approach: build and TEST in Stripe test mode
first, fully isolated from Base44, then wire it into the app in a later focused session.

## Why two phases

A second session was editing the Base44 app (email buttons + /manage customization) when
this started. Base44's Publish ships ALL pending draft changes at once, so editing Base44
from two sessions risks shipping half-finished work. Stripe's own setup (account, product,
price, hosted Payment Link, test cards) lives entirely in the Stripe dashboard and touches
no Base44 code, so Phase 1 is safe to do in parallel. Phase 2 (the Base44 wiring) is the
only part that collides, and it waits until the app is clear.

## Phase 1: test-mode checkout, no code (ISOLATED — do now)

Goal: a real, clickable checkout Samuel can run a fake purchase through, to see exactly how
the flow feels, before any code.

1. Stripe account, confirm **Test mode** toggle is ON (test data only, no real charges).
2. Create the **product**: "Caught Up AI — AP Lang Opener (annual subscription)".
3. Create the **price**: recurring, yearly. PLACEHOLDER **$89/yr** (pricing is OPEN, see
   below) with a **free trial** (placeholder 7 days; the model is the free-week wedge).
4. Generate a **Payment Link** for that price (Stripe-hosted checkout page, no code).
5. Click through with Stripe **test cards** (success `4242 4242 4242 4242`; decline
   `4000 0000 0000 0002`), confirm the trial + the receipt + the subscription appears in the
   test dashboard.

Output of Phase 1: confirmed the purchase experience end to end, a test Payment Link URL,
and a settled view on price/trial wording before we touch the app.

## Phase 2: wire into Base44 (LATER — collides with the app, do when clear)

Turns a successful payment into an active subscription on the teacher's record.

- **Integration fork (decide then):**
  - **A. Base44 native Stripe connector** — least code, fewest moving parts, fits
    [[feedback_no_code_path]]. PREFERRED unless it can't drive subscription status onto the
    Teacher entity. Verify what it can actually do before committing.
  - **B. Custom backend function + Stripe webhook** — a Base44 function receives Stripe's
    `checkout.session.completed` / subscription events and sets `subscription_status` (+
    period end) on the matching Teacher via service-role. More control, more surface.
- **Teacher entity needs a billing field** (e.g. `subscription_status`:
  trialing|active|past_due|canceled, plus `current_period_end`). Add in the same Base44
  session, behind the existing locked permissions.
- **Link identity:** the Stripe customer email must map to the Teacher record (email is the
  join key; the magic-link `manage_token` stays the access secret).
- **Checkout entry point:** a "Subscribe" button on caughtupai.com (or the Payment Link)
  that, on success, returns the teacher to a confirmation + their /manage link.

## Pricing (OPEN — placeholder only)

Not decided. Working assumptions from [[2026-06-12 - Product pipeline, resources, pricing]]:
~$79-99/yr annual (placeholder $89), optional monthly ~$9-12, **ONE price** (frequency is
free, never a tier), free trial, card-pay as the launch wedge (school POs later). Set the
real number before Phase 2 / go-live.

## Hard dependencies before ANY real (live-mode) billing

- **Teacher entity read-leak must be fixed** (the live security blocker in [[Delivery-Stack]]
  "CRITICAL SECURITY REGRESSION"). Do not take real payments while PII + manage_tokens leak.
- **Business entity + real address** — billing/invoices need a real business identity, and
  the CAN-SPAM/footer address swap is already on the August-launch reminder
  ([[project_august_launch_reminders]]). Live-mode Stripe also wants real business + bank
  details; test mode does not.
- Delete the fake test Teacher records before any list-wide flow.

## Status

- Phase 1: NOT STARTED (account setup is Samuel's hands; account creation needs his login +
  email verification).
- Phase 2: blocked on the concurrent Base44 session being clear + the read-leak fix.

Related: [[Delivery-Stack]], [[2026-06-12 - Product pipeline, resources, pricing]],
[[project_august_launch_reminders]], [[Caught Up AI]].
