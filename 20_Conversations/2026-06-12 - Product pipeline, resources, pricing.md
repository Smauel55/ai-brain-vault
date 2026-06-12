---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, pipeline, pricing, go-to-market]
project: "[[Caught Up AI]]"
---

# 2026-06-12 - Product pipeline, resources, pricing

Strategy talk on what the final product looks like end to end: the production pipeline, the outside resources needed, and price modeling. Framing and recommendations, not yet hard decisions by Samuel.

## Key reframe

- The creative/editorial engine is DONE (Verify -> Compose -> Fact-check -> Render). The remaining work is the service shell around it.
- It is a BROADCAST product (one edition/day, all teachers get the same content, frequency is a receive-filter). This single fact drives both pipeline shape and pricing math.

## The full pipeline (8 stages) and what is missing

- DONE: Generate (2), human fact-gate (3, manual), Manage page (7).
- MISSING / launch-critical, four boxes: **Trigger** (1, nightly schedule ~4am CT), **Store PDFs** in a cloud location with shareable URLs (4), **Deliver** to due teachers (6), **Bill** (8, payments).
- PARTIAL: Pick recipients (5) - Teacher entity + /manage exist; still need the "who is due today" query (weekday + June-July 1/wk throttle).

## Outside resources needed

- Email sending service (NEED): Resend or Postmark recommended, for deliverability.
- Sending-domain DNS auth SPF/DKIM/DMARC on Porkbun (NEED): non-negotiable vs aggressive school-district spam filters.
- Cloud storage for PDFs (NEED): Cloudflare R2 / S3, or lean on Base44 storage to start.
- Scheduler/host (NEED): use the Claude Code scheduled CLOUD ROUTINE on the subscription (no server, no un-debuggable code).
- Payments (NEED): Stripe, ideally via a Base44 integration.
- HAVE: domain (caughtupai.com/Porkbun), Base44 app, Teacher entity, /manage.

## Decisions / recommendations reached

- **Deliver as LINKS to hosted PDFs, not attachments.** District filters flag/strip attachments; links also give open-tracking and a post-send fix path. Cost is one extra click.
- **Do NOT use the Batches API at launch.** A single daily broadcast Opener is one item: batch gives only the flat 50% discount, no throughput gain, plus a "within 24h" turnaround risk for a same-day-news product, plus un-debuggable SDK/orchestration code. "Run on Anthropic cloud" should mean the scheduled subscription routine, not batch. Batch stays parked until Fable leaves subscription inclusion, the spec freezes, OR the product goes per-teacher personalized (many items/day). Consistent with [[Batch-API-Readiness]].

## Pricing

- COGS is essentially solved and structurally favorable: broadcast = content cost is FIXED per day regardless of subscriber count, so cost/subscriber falls toward zero. ~$0 marginal on subscription routine; ~$160/mo API daily; ~$80/mo batch. Small fixed costs: email, storage (pennies), Stripe 2.9%+30c, domain. Margin excellent at any real subscriber count.
- Old "16-46 subs fund one writer/wk" math is DEAD (that was the licensing path; AI generation removed the per-piece variable cost).
- Price-to-teacher (still OPEN): recommended starting position = one per-teacher plan, billed ANNUALLY on the school year (parks summer churn, complements the June-July throttle), anchor ~$79-99/yr (or ~$9-12/mo priced to nudge annual), free trial over a unit/few weeks. One price, frequency free (churn lever not a tier).
- Channel: individual teacher card-pay is the LAUNCH WEDGE; department/school PO sales are a later expansion, not a launch requirement.

## Next (priority order)

1. Email service + deliverability (critical-path blocker): provider, links-not-attachments, DNS auth.
2. Confirm scheduling host = subscription routine (not batch SDK).
3. Set the actual price point - from a teacher conversation, not a spreadsheet.
4. Payments: Stripe via Base44 or standalone.

Suggested first deep-dive: the delivery stack (pick provider, map send flow, list DNS records).

Related: [[Caught Up AI]], [[Generation-Pipeline]], [[Batch-API-Readiness]], [[Website-Setup]], [[feedback_no_code_path]], [[feedback_production_token_budget]].
