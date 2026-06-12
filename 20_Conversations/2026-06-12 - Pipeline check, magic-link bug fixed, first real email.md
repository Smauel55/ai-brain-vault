---
created: 2026-06-12
updated: 2026-06-12
tags: [conversation, caught-up-ai, delivery, email, base44]
project: "[[Caught Up AI]]"
---

# 2026-06-12 - Pipeline check, magic-link bug fixed, first real email

Ran the delivery "pipeline check" (prove the PDF URL + the magic link both work), found and
fixed a real bug, and delivered the first email with real content + working links to Samuel.

## What was proven
- **Public PDF hosting: PROVEN.** Uploaded the real "The Voice That Carried" (Tribute) teacher +
  student PDFs via `Core.UploadFile`; both URLs return HTTP 200 / `application/pdf`, served from
  `media.base44.com/files/public/...`, with NO auth token sent. Clears the long-open runtime risk;
  no R2/S3 fallback needed.
- **Magic link: PROVEN.** `/manage?t=<token>` loads the real prefilled settings page. The page
  reads query param `t`, not `token`.

## The bug (real, production)
- `sendTodaysEdition` built the manage + unsubscribe links as `…/manage?token=MANAGE_TOKEN`, but
  the live `/manage` page only reads `?t=` (confirmed in the deployed JS bundle:
  `new URLSearchParams(window.location.search).get("t")`). So every teacher's manage AND
  unsubscribe link was dead, including in the earlier test email. With a wrong param the page
  shows "This link is invalid or expired" and never even calls `getTeacherByToken`.

## Fix (in PREVIEW, not published)
Edited `functions/sendTodaysEdition.ts` (via the Base44 chat agent), three changes:
1. manage/unsubscribe links now use `?t=` (with `&action=unsubscribe` on the latter).
2. In `test` mode, look up the Teacher by `email == test_email` (asServiceRole) and use that
   teacher's `manage_token` + first name; fallback to "there"/empty token if none.
3. Added optional `edition_id` input (load that exact Edition); else load by `edition_date`,
   and if multiple editions share a date pick the most recently created one.

## How the send was run + verified
- Ran `sendTodaysEdition` via the editor's Test Function:
  `{mode:"test", test_email:<samuel>, edition_id:"6a2c843b…"}` -> `{ok:true, mode:"test",
  recipient_count:3, sent:1, failed:0}`. (3 due Friday teachers = Samuel + 2 fakes; test sends 1.)
- Resend: **Delivered**. Verified the email HTML: both buttons point at the real
  `…/files/mp/public/…teacher-ap.pdf` / `…student.pdf`; footer links are
  `…/manage?t=8d184dda…` and `…&action=unsubscribe`. Re-curled both button URLs: 200 /
  application/pdf / full bytes. Sign-off "Have a great class, Samuel" (personalization worked).

## Platform facts learned (reusable)
- The app **`api_key`** (createClient `headers:{api_key}`) authenticates as the app OWNER. It can
  call `Core.UploadFile` and `entities.Edition.create/list/filter` directly (owner bypasses the
  locked `create:false`), so the local pipeline can upload PDFs + create editions over REST and
  SKIP the admin-gated `createEdition` entirely.
- BUT `entities.Edition.delete` / `.update` via the api_key return **404** (rls `delete/update:false`
  is NOT bypassed by the owner REST client; only asServiceRole inside a function bypasses writes).
- `createEdition` and `sendTodaysEdition` are admin-guarded (`auth.me` role check). The api_key is
  NOT a user identity, so calling them over REST 500s ("Authentication required to view users").
  Sends therefore run via the editor Test Function (admin) or need a pipeline-secret guard added.
- Base44 editor is very freeze-prone (Data grid, function runs): 30s+ renderer hangs are normal;
  reload the route to recover. Do NOT click Edition's "Permissions / Fix" banner (false positive
  that would re-lock Edition read and re-break asServiceRole reads).

## Created this session
- Real Edition `6a2c843ba74c5fb9116d864a` ("The Voice That Carried", live public PDF URLs).
- Real Teacher record `6a2c864bf04328512186612e` (Samuel Levy, trial, Mon-Fri, AP Lang, Eastern,
  with a manage_token) -> Samuel is now a real subscriber, magic link is genuinely his.

## Still open
- **Publish** the `?t=` fix for production (also pushes the staged audience/Course `/manage` work).
  Test sends to Samuel's inbox already work off the preview/draft.
- **Delete the dummy "Measles" Edition** (`6a2c6feb…`). Couldn't, via the frozen Data grid or REST
  (rls delete:false -> 404). Neutralized by the latest-wins selection; still worth one-click delete.
- **Delete the fake test Teachers** before any real broadcast (2 are "due" on Fridays).

Related: [[Delivery-Stack]], [[2026-06-12 - Delivery build Edition entity and createEdition]],
[[project_caught_up_ai]], [[Caught Up AI]].
