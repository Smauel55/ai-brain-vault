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

## MILESTONE 2026-06-12: send path verified, FIRST EMAIL DELIVERED

The whole email path works end to end. Built + DONE this session:
- Resend API key (`caughtupai-base44`, Sending access, scoped to send.caughtupai.com) ->
  Base44 Secrets `RESEND_API_KEY`. Email template v1. App published.
- `sendTodaysEdition` (admin-only; modes dry_run[default]/test/live; recipient filter;
  audience routing; Resend + List-Unsubscribe + one-click). Code-verified safe.
- **RLS fix:** Edition `rls.read` set to true (asServiceRole reads were blocked by
  read:false -- same platform quirk as Teacher). Write still locked
  (`{create:false, read:true, update:false, delete:false}`).
- **Test send DELIVERED** to samuellevy2030@u.northwestern.edu (Resend "Delivered" to a
  Google Workspace EDU inbox = SPF/DKIM/DMARC + reputation all good). Used a dummy
  2026-06-12 edition with placeholder PDF links.

## NEXT (next session starts here)

1. **Wire the pipeline -> createEdition** (`.claude/workflows/caughtup-opener.mjs`): after
   render, POST metadata + the rendered PDFs (base64) to `createEdition`. App `api_key`
   from a LOCAL env var, never committed. This is the LAST core piece AND the only way to
   prove the open runtime risk below.
2. **Delete the dummy 2026-06-12 test Edition** before any real scheduling.
3. Later: scheduling (scheduled Claude Code routine on the subscription, NOT the Batches
   API -- see [[Batch-API-Readiness]]); payments (Stripe; native Base44 connector available).

## RESOLVED 2026-06-12 (eve): pipeline check passed + magic-link bug fixed

Ran the pipeline check end to end and delivered the first REAL-content email to Samuel with
working links. See [[2026-06-12 - Pipeline check, magic-link bug fixed, first real email]].

- **Public file URL -- PROVEN.** Uploaded the real Tribute PDFs via `Core.UploadFile`; both URLs
  return 200 / `application/pdf` from `media.base44.com/files/public/...` with no auth. No R2/S3
  needed.
- **api_key path (skips createEdition).** The app `api_key` authenticates as the app OWNER and can
  call `Core.UploadFile` + `entities.Edition.create/list/filter` directly (owner bypasses the
  locked `create:false`). So the local pipeline can upload PDFs + create the Edition over REST and
  skip the admin-gated `createEdition`. CAVEAT: `Edition.delete`/`.update` via api_key return 404
  (rls delete/update:false is NOT bypassed by the owner REST client; only asServiceRole inside a
  function bypasses writes).
- **Admin gate is real.** `createEdition` AND `sendTodaysEdition` 500 over REST
  ("Authentication required to view users") because the api_key is not a user identity. Sends run
  via the editor Test Function (admin), or need a pipeline-secret guard added to the function.
- **BUG FOUND + FIXED (preview).** `sendTodaysEdition` built manage/unsubscribe links with
  `?token=`, but the live `/manage` page only reads `?t=` -> every teacher's manage + unsubscribe
  link was dead. Fixed in PREVIEW (not published): `?t=`, test-mode personalization by test_email,
  optional `edition_id` + latest-wins on date collision. Test send Delivered; all 4 links verified.
- Created: Edition `6a2c843b` (real public URLs) + Samuel's Teacher record `6a2c864b`.

### Remaining before production
1. **Publish** the `?t=` fix (also pushes the staged audience/Course `/manage` changes). Test sends
   to Samuel already work off draft.
2. **Delete the dummy "Measles" Edition** `6a2c6feb` (couldn't via the frozen Data grid or REST;
   neutralized by latest-wins selection).
3. **Delete the fake test Teachers** before any real broadcast (2 are "due" on Fridays).

**Safety gate:** the FIRST real broadcast to the teacher list still requires explicit go.
Test/live sends to Samuel's own inbox are fine.

Base44 notes: chat input sends on Enter and treats newlines as separate messages -- send
multi-field specs as ONE single-line message. The editor freezes ~30s under load (publish,
function runs, long typed inputs); verify sends via the Resend tab when it hangs. To change
entity permissions, edit `entities/<Name>.json` `rls` and insist on exact values (the diff
panel's "No restrictions" can mean unchanged current state, not a new opening).

## RESOLVED 2026-06-13: magic-link Save fixed end to end + email link colors

The /manage Save button hung forever because of a **day-format mismatch**. Diagnosed live
in Chrome (Save POSTed `updateTeacherByToken` -> `400 {"error":"Invalid days: ..."}`, page
had no error handler so it span). The canonical format across storage, `getTeacherByToken`,
and the page payload is **full capitalized weekday names** (`Monday`..`Friday`); three places
disagreed and were all aligned to full names:

1. **`updateTeacherByToken`** validated against `['Mon','Tue','Wed','Thu','Fri']`. Fixed:
   accepts the seven full names, case-insensitive, normalizes to capitalized full names
   before saving.
2. **`pages/Manage` day chips** carried short-code VALUES (prefill never highlighted;
   toggling sent a short code the backend rejected). Fixed: chips are now
   `{label:'Mon', value:'Monday'}`; selected-state, toggle, and Save payload use the
   full-name value (plus a legacy short-code normalizer).
3. **`sendTodaysEdition` recipient filter** computed the weekday as a short code
   (`WEEKDAY_NAMES = ['Sun','Mon',...]`) and matched it against full-name `delivery_days`,
   so a real `live` broadcast would have reached **ZERO** teachers (hidden because every test
   used `test` mode, which skips the filter). Fixed: `WEEKDAY_NAMES` now full names.

**Email footer links recolored** in `sendTodaysEdition`: "Change your delivery days" ->
`color:#5b21b6;text-decoration:underline`; "Unsubscribe" -> `color:#6b7280;text-decoration:underline`
(both were `#9ca3af` gray and hard to see).

Published and **verified live by behavior**: prefill highlights selected days; toggled Friday
off -> Save `200 {"success":true}` with `["Monday".."Thursday"]`; reload confirmed
persistence; restored to all five. Samuel's founder-test record left intact at all 5 days.

### >>> CRITICAL SECURITY REGRESSION (found 2026-06-13) <<<

The Teacher entity is **leaking again**. An anonymous (no-auth) `GET
/api/apps/6a1f286b511ece79b6ef3942/entities/Teacher` returns `200` with every record's
`email` and `manage_token` (the magic-link secret = full account control). It regressed
because Teacher `read` was set back to `true` during 2026-06-12 debugging (Base44 quirk:
`read:false` blocks even `asServiceRole` reads, which broke `getTeacherByToken`). Only
fake/test data is exposed now. **This is a hard launch blocker.** Naive re-lock (`read:false`)
re-breaks the working Save. Real fix options: lock the entity and serve ALL Teacher reads
only through service-role functions returning safe fields; or remove Teacher from the public
REST surface; or a proper RLS `user_condition`. Do NOT click the Permissions "Fix" banner
(known false positive). Needs its own focused session.

## Email + sender details (2026-06-12)

- **Template v1 built** at `10_Projects/Caught Up AI/email-template-v1.html` (table-based,
  inline styles, links not attachments, one-click unsubscribe, no em-dashes). Personalized
  sign-off: "Have a great class, {{teacher_first_name}}" (derive first name from full_name).
  Subject line: "Today's Opener: {{headline}}". Buttons: Open teacher copy / Open student
  copy. Helper line explains teacher vs student copy.
- **From address** (to wire in send fn): something like `Caught Up AI
  <opener@send.caughtupai.com>` on the verified sending subdomain.
- **Footer postal address (CAN-SPAM):** interim = Samuel's HOME address (provided
  2026-06-12, Greenville SC 29615). Set the literal value directly in the Base44 send
  function, NOT in committed vault files. Samuel accepted that the home address is visible
  to all recipients in the meantime.

### >>> AUGUST LAUNCH REMINDER <<<

When real-business launch work begins (targeted **August 2026**), set up a **virtual
mailbox** (real street address, mail managed online, ~$10-20/mo) and swap it into the email
footer in place of Samuel's home address. Samuel explicitly asked to be reminded of this at
launch. Also revisit: business entity, the Stripe/payments segment, and any "real business
address" needs (invoicing schools).

### Open wrinkle to carry forward

The `audience` flag (AP Lang vs General English) changes the TEACHER copy's labels, so a
mixed list needs up to TWO teacher-copy renders per edition, routed per teacher. Student
copy is identical. Not a launch blocker (AP Lang is the wedge), but build the edition record
to hold both teacher-copy URLs from day one.

Related: [[Generation-Pipeline]], [[Batch-API-Readiness]], [[Website-Setup]],
[[2026-06-12 - Delivery stack and Resend DNS setup]], [[Caught Up AI]].
