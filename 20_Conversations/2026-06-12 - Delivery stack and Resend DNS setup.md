---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, delivery, email]
project: "[[Caught Up AI]]"
---

# 2026-06-12 - Delivery stack and Resend DNS setup

## What we did
- Mapped the full product pipeline + outside resources + price modeling at a high level,
  then went deep on **delivery** (see [[Delivery-Stack]] for the durable design).
- Chose **Resend** as the email provider; decided links-not-attachments; chose a dedicated
  sending subdomain `send.caughtupai.com`.
- Set up the sending identity end to end via the browser (Claude drove it):
  - Created the Resend sending domain.
  - Added 4 DNS records in Porkbun (DKIM TXT, SPF MX+TXT on send.send, DMARC TXT on _dmarc),
    DKIM key copy-pasted from Resend so it was character-perfect.
  - Submitted via Porkbun's batch flow with "Do not delete existing records" checked.
  - **Resend verified the domain.** Sending identity is live.

## Key findings (carried into [[Delivery-Stack]])
- `*.caughtupai.com` wildcard CNAME -> base44.onrender.com (explicit records override it).
- Porkbun's panel won't display this domain's existing records (UI glitch); verified via
  live DNS instead. Nameservers are Porkbun defaults (authoritative).

## Cost frame (from earlier in session)
- Broadcast model = content cost is FIXED per day regardless of subscriber count, so
  cost-per-subscriber falls toward zero. COGS ~$0 on subscription routine, ~$160/mo at API
  daily, ~$80/mo on batch. Price-to-teacher still open; starting position ~$79-99/yr annual
  (school-year cycle), monthly ~$9-12, free trial, one price (frequency free). Individual
  card-pay is the launch wedge; school/PO sales later.

## Next session
- Build the delivery mechanics in Base44: host PDFs, send function, edition record +
  recipient query, email template. Then scheduling (subscription routine, not Batches) and
  Stripe. Start point documented at the bottom of [[Delivery-Stack]].
