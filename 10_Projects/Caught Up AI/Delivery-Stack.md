---
created: 2026-06-12
updated: 2026-06-12
tags: [project, caught-up-ai, delivery, email, infrastructure]
project: "[[Caught Up AI]]"
---

# Caught Up AI Delivery Stack

How a generated edition gets from "PDFs produced" to "a teacher opens it." This is the
wrapper around the [[Generation-Pipeline]] that turns the engine into a real service.
Started 2026-06-12. Sending identity is DONE; the rest is scoped, not yet built.

## The end-to-end flow (the seam)

Generation already ends by producing two PDFs. Delivery picks up from there:

1. Generation finishes -> teacher copy + student copy PDFs + metadata (date, headline, register).
2. Upload the PDFs to storage -> two stable URLs.
3. Record the edition (date, the two URLs, subject line, one-line preview).
4. Query who is due today (weekday + June-July throttle + active subscription + not unsubscribed).
5. Send each due teacher one short email: two buttons (Teacher copy / Student copy) + manage/unsubscribe footer.

Steps 2-5 are designed to live inside Base44, where the Teacher data already is.
Generation (Claude Code) hands off the edition; Base44 does the mailing. Keeps the
un-debuggable code surface small ([[feedback_no_code_path]]).

## Decisions made (2026-06-12)

- **Email provider = Resend.** Simplest to wire from Base44, strong deliverability, free
  under a few thousand sends/mo then ~$20/mo, clean HTTP API. (Postmark was the runner-up.)
- **Deliver PDFs as LINKS to hosted files, not attachments.** District mail filters
  distrust attachments; links also allow open-tracking and fixing a bad edition post-send.
- **Sending identity = a dedicated subdomain `send.caughtupai.com`** (isolates mail
  reputation from the root/website domain).
- **Deliverability must-haves:** SPF + DKIM + DMARC on the sending domain (done), plus a
  one-click unsubscribe wired to the existing /manage unsubscribe (Gmail/Yahoo bulk-sender
  rule, and the biggest reputation lever is a low spam-complaint rate). School domains
  (Google Workspace / M365 for Education) are the hardest audience; this is why auth + links
  + clean list discipline matter.

## DONE: sending identity (Resend + Porkbun DNS)

- Resend account live (workspace "northwestern", login samuellevy2030@u.northwestern.edu).
- Sending domain `send.caughtupai.com` added in Resend (region us-east-1 / N. Virginia).
- Four DNS records added in Porkbun and SUBMITTED (Porkbun confirmed "record created" x4),
  existing website records left intact (used the "Do not delete existing records" path):

  | Type | Host (Porkbun) | Value | Priority |
  |---|---|---|---|
  | TXT | resend._domainkey.send | DKIM public key (p=...) | |
  | MX | send.send | feedback-smtp.us-east-1.amazonses.com | 10 |
  | TXT | send.send | v=spf1 include:amazonses.com ~all | |
  | TXT | _dmarc | v=DMARC1; p=none; | |

- Resend **verified** the domain (2026-06-12). Sending identity is fully live.

### Two gotchas found on caughtupai.com (keep for future DNS work)

- **Wildcard CNAME exists:** `*.caughtupai.com` -> base44.onrender.com (Base44 set this so
  any subdomain serves the app). It means new subdomains resolve to the app until an
  explicit record is added; an explicit record always beats the wildcard, so the four
  records resolve correctly now. Verified live before/after via DNS lookups.
- **Porkbun's DNS panel does not display this domain's existing records** (a UI glitch on
  the account; records confirmed present via live DNS). The Add form still works; it stages
  records into a batch table, then "Submit Records" commits. Verify additions via live DNS
  rather than trusting the panel list. Nameservers are Porkbun's defaults
  (fortaleza/salvador/maceio/curitiba.ns.porkbun.com), so Porkbun is authoritative.

## NEXT (next session starts here)

1. **Host the PDFs.** Confirm whether Base44 can store files with public URLs; if not, use
   Cloudflare R2 / S3. Verify Base44 can also (a) run a scheduled function and (b) make
   outbound calls to Resend (the latter near-certain, since service-role functions already
   call the entity API).
2. **Build the send function** in Base44 (`sendTodaysEdition`, service-role): take the
   edition, run the "who is due today" query, loop due teachers, call Resend per teacher.
3. **Edition record + recipient query** (weekday + throttle + active + not-unsubscribed).
4. **Email template** (logo, one-line preview, two buttons, manage + one-click unsubscribe).
5. Later segments: scheduling (the launch path is a scheduled Claude Code routine on the
   subscription, NOT the Batches API -- see [[Batch-API-Readiness]]), and payments (Stripe).

### Open wrinkle to carry forward

The `audience` flag (AP Lang vs General English) changes the TEACHER copy's labels, so a
mixed list needs up to TWO teacher-copy renders per edition, routed per teacher. Student
copy is identical. Not a launch blocker (AP Lang is the wedge), but build the edition record
to hold both teacher-copy URLs from day one.

Related: [[Generation-Pipeline]], [[Batch-API-Readiness]], [[Website-Setup]],
[[2026-06-12 - Delivery stack and Resend DNS setup]], [[Caught Up AI]].
