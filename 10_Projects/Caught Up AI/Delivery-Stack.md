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

## PROGRESS: Base44 build (2026-06-12, session 2)

Architecture confirmed against the live app, foundation entity built.

- **App ID** = `6a1f286b511ece79b6ef3942` (Caught Up AI in Samuel's Base44 workspace).
- **Backend = Deno + `@base44/sdk`.** Service-role data access via
  `base44.asServiceRole.entities.X.filter/create/update`; outbound `fetch` to Resend is
  native to Deno (confirms the send function can call Resend directly).
- **Pipeline -> Base44 seam = REST API.** App exposes `POST /entities/{Entity}` and
  `POST /functions/{fn}`, authenticated by an app `api_key`. So the local generation
  pipeline can push an edition in by calling a backend function (no manual upload).
- **File hosting = Base44 `Core.UploadFile`** -> returns a `file_url`. INTENDED to be a
  public URL that opens without login (teachers click straight from email), and Base44
  reports it uploads to "public storage" -- but this is NOT yet proven at runtime. Treat
  as a RISK until a real uploaded URL is confirmed to open with no auth; R2/S3 is the
  fallback if it requires login.
- **`Edition` entity built + verified (11 fields).** `edition_date*` (req), `headline`,
  `register`, `preview`, `subject`, `student_pdf_url`, `teacher_pdf_url_ap`,
  `teacher_pdf_url_general` (string); `status` (draft|sent); `sent_at` (date-time);
  `recipient_count` (number). Permissions locked to **service-role + admin only**.
- **`createEdition` function = BUILT + code-reviewed (correct); runtime test PENDING.**
  Admin-only (auth.me, `role==='admin'`). POST JSON: `edition_date` (req, YYYY-MM-DD),
  `headline`, `register`, `preview`, `subject`, `student_pdf_base64` (req),
  `teacher_pdf_ap_base64` (req), `teacher_pdf_general_base64` (optional). Decodes each
  base64 -> PDF file, uploads via `Core.UploadFile`, names them
  `edition-<date>-student.pdf` / `-teacher-ap.pdf` / `-teacher-general.pdf`, creates one
  Edition record with the resulting URLs + `status='draft'`, returns `{ok, edition}`.
  Reviewed the full source in the Base44 code editor; logic is complete and correct.

## TWO RUNTIME RISKS to clear with one live `createEdition` call (not by reading)

1. **Public file URL** -- `Core.UploadFile`'s `file_url` must open with NO login. If it
   needs auth, switch PDF hosting to R2/S3. This is the core "host the PDFs" bet.
2. **Admin-auth via api_key** -- the pipeline's `api_key` call must pass the
   `role==='admin'` guard, else 403. Both answered the moment the pipeline fires a real call.

## NEXT (next session starts here)

1. **Wire the pipeline** (`.claude/workflows/caughtup-opener.mjs`): after render, POST
   metadata + the rendered PDFs (base64) to `createEdition`. App `api_key` from a LOCAL env
   var, never committed. Then one live call to clear the two risks above.
2. **Build `sendTodaysEdition`** (service-role): take an edition, run "who is due today"
   (weekday in `delivery_days` AND `status` in trial/active), send each via Resend with the
   teacher-copy link matching their `audience`. Dry-run first.
3. **Email template** (logo, one-line preview, two buttons, manage + one-click unsubscribe).
   Samuel approves copy (his voice) before any send.
4. **Samuel actions for the send path:** create a Resend API key + add to Base44 Secrets as
   `RESEND_API_KEY` himself (Claude never enters keys); **Publish** the app so the new
   entity + function go live at the REST endpoint.
5. Later: scheduling (scheduled Claude Code routine on the subscription, NOT the Batches API
   -- see [[Batch-API-Readiness]]); payments (Stripe; native Base44 connector available).

**Safety gate:** the send path is built + dry-run only; the FIRST real email goes to
Samuel's inbox alone, on explicit go. Never the teacher list during testing.

Base44 chat gotcha: input sends on Enter and treats newlines as separate messages. Send
multi-field specs as ONE single-line message (semicolons), or it fragments into a queue.

### Open wrinkle to carry forward

The `audience` flag (AP Lang vs General English) changes the TEACHER copy's labels, so a
mixed list needs up to TWO teacher-copy renders per edition, routed per teacher. Student
copy is identical. Not a launch blocker (AP Lang is the wedge), but build the edition record
to hold both teacher-copy URLs from day one.

Related: [[Generation-Pipeline]], [[Batch-API-Readiness]], [[Website-Setup]],
[[2026-06-12 - Delivery stack and Resend DNS setup]], [[Caught Up AI]].
