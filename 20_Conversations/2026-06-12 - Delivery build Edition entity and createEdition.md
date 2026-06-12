---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, delivery, base44]
project: "[[Caught Up AI]]"
---

# 2026-06-12 - Delivery build: Edition entity and createEdition

Continuation of the delivery build (after [[2026-06-12 - Delivery stack and Resend DNS setup]]).
Goal this session: host the PDFs and start the Base44 send path.

## Decisions
- **PDF upload seam = pipeline auto-uploads** (Samuel chose). The local generation
  workflow will call a Base44 function with metadata + the PDFs (base64); Base44 stores
  them and creates the edition. Cleanest path to scheduling; rejected manual-upload page
  and external R2 (keeps the surface small).
- **Two-function split**: `createEdition` (safe, no email) + `sendTodaysEdition` (gated,
  sends). All Base44 logic server-side; pipeline just makes HTTP calls.

## Recon confirmed (live Base44 app, appId 6a1f286b511ece79b6ef3942)
- Backend functions = Deno + `@base44/sdk`, `base44.asServiceRole.entities.X.filter/create`,
  native `fetch` (so Resend calls work). Existing fns: getTeacherByToken,
  updateTeacherByToken, setSubscriptionByToken (all return only safe fields).
- REST API exists: `POST /entities/{Entity}`, `POST /functions/{fn}`, authed by an app
  `api_key` (shown on the API page). SDK: `createClient({appId, headers:{api_key}})`.
- Teacher schema: full_name, email, school, delivery_days[], political_content
  (neutral|civic), audience (ap_lang|general_english), time_zone (IANA), manage_token,
  status (trial|active|canceled). Everything the recipient query needs.
- Stripe + Gmail connectors available natively (Stripe for the payments segment later).

## Built and verified
- **Edition entity** created. 11 fields: edition_date (required), headline, register,
  preview, subject, student_pdf_url, teacher_pdf_url_ap, teacher_pdf_url_general,
  status (draft|sent), sent_at (date-time), recipient_count (number). Permissions locked
  to service-role + admin. Schema verified on the API page.
- **createEdition function** built (admin-guarded via auth.me role==='admin'; validates
  edition_date + the two required PDFs; base64->File; uploads 3 PDFs via
  Core.UploadFile -> file_url; creates draft Edition; returns {ok, edition}). Code
  reviewed line by line, correct.

## Open / next session
- TWO runtime assumptions still unproven (need a live test, not a read):
  1. Core.UploadFile `file_url` must open WITHOUT login (teachers click from email). If
     not, fall back to R2.
  2. The pipeline's api_key call must satisfy the admin guard (else 403).
  Both answered by wiring the pipeline + one real createEdition call.
- Samuel actions for the send path: create a Resend API key and add it to Base44 Secrets
  as `RESEND_API_KEY` himself (Claude does not enter keys); Publish the app so the new
  entity + function go live; approve the email template copy.
- Safety gate: first real send goes to Samuel's inbox only, on explicit go. Never the
  teacher list during testing.
- Remaining tasks: wire pipeline -> createEdition (task 3), sendTodaysEdition + recipient
  query (task 4), email template (task 5), then scheduling + Stripe.

## Process note
- Base44's chat input SENDS on Enter and treats newlines as separate messages. Paste
  multi-field instructions as ONE single-line message (semicolons, no newlines) or it
  fragments into a queue. The browser `type` tool times out on ack for this textarea but
  the text still lands; verify by screenshot, then click send.

Related: [[Delivery-Stack]], [[Generation-Pipeline]], [[Caught Up AI]].
