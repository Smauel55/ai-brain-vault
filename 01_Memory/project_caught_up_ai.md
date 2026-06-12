---
name: caught-up-ai-project-state
description: "Current state of Samuel's daily AP Lang lesson-opener startup; durable decisions + pointers to vault detail"
metadata: 
  node_type: memory
  type: project
  originSessionId: cff28425-c81b-4fde-97cb-38350e1bf10c
---

**What it is:** The "Opener" — a daily 10-15 minute lesson opener for AP English Language teachers. Each edition = a fully AI-GENERATED original nonfiction piece (written from verified facts, never reproduced source text) + apparatus: italic AP-style headnote, rhetorical devices marked (teacher copy only), 2 MCQs + randomized key, discussion questions, writing prompt, misconceptions, alignment notes. Two copies per edition (teacher / student). Broadcast model: one edition per weekday; per-teacher frequency is a receive-filter, rotation advances by edition date. Delivered by email as PDF links (not attachments).

**Why:** The Garage (Northwestern) evidence stack by Sept 2026. ~10,000 US AP Lang teachers, 8-15 hrs/wk article-prep pain, already pay out of pocket.

**Stack:**
- Generation: enforced model-routed workflow `.claude/workflows/caughtup-opener.mjs` (Verify = Fable 5 web-confirms facts -> Compose = Fable 5 drafts + gates -> Render = Haiku via render_opener_v2.py unmodified). Trigger: "build today's Opener" (optional topic/register). Recency via editions-log.tsv. Proven end to end 2026-06-11. See [[reference_opener_renderer]].
- Site + data: Base44 (caughtupai.com). Teacher entity locked `{create/read/update/delete:false}`, all access via service-role backend functions (getTeacherByToken / updateTeacherByToken / setSubscriptionByToken). /manage magic-link preferences page live (days, political dial, audience, unsubscribe), no portal/login. GOTCHA: never click the Base44 editor's Permissions "Fix" banner — false positive that would break the working lock. (A read-leak vuln was found, fixed, live-verified closed 2026-06-11.)
- Email: Resend, sending domain send.caughtupai.com VERIFIED (DKIM/SPF/DMARC in Porkbun, 2026-06-12). DNS gotchas: a `*.caughtupai.com` wildcard CNAME -> base44 exists (explicit records override it); Porkbun's panel doesn't display this domain's existing records — verify via live DNS lookups.
- Billing: Stripe, not built.

**Where it stands (2026-06-12):** Delivery stack in progress; sending identity live. NEXT: host the PDFs (confirm Base44 file hosting, else R2/S3), Base44 sendTodaysEdition function (who-is-due query: weekday + summer throttle + active + not-unsubscribed), edition record holding BOTH teacher-copy URLs (audience flag = up to 2 teacher renders), email template (logo + preview line + two buttons + manage/unsubscribe footer), then scheduling (cloud routine, NOT Batches API) + Stripe. Pricing OPEN: ~$79-99/yr annual frame, monthly ~$9-12, free trial, ONE price (frequency free), card-pay wedge. Full design: 10_Projects/Caught Up AI/Delivery-Stack.md.

**Durable decisions:**
- Content = full AI generation (2026-06-05 pivot). The reproduction model died on licensing: only PD/CC0/CC-BY are reproducible+annotatable (D-006), the free pool is too thin for daily (D-007), commissioning ruled out by Samuel, and D-009 (untouched article + separate apparatus) verified sound-with-conditions but moot post-pivot. Detail: Licensing-Verification.md, Content-Sourcing.md.
- Prose engine v2.1: 7-register palette (Ledger / Open Letter / Reckoning / Tribute / Long Think / Witness Stand / Long Look), 10 spec files in 10_Projects/Caught Up AI/ (Style-Palette, Register-Specs, Generation-Briefs, Anti-Tell-List, etc.). The AI-judge proxy went 100% detection in both runs -> saturated, do NOT optimize against it; fix was the friction/anti-symmetry layer in Anti-Tell-List v2.1. The decisive test is a HUMAN AP-Lang panel (Blind-Test-Protocol.md), not yet run. Known weak spot: Ledger (the daily default) reads wordy — readability pass still owed in Register-Specs.
- Editorial Gate 0 (Editorial-Standards.md, runs before every register): neutrality firewall ([[feedback_opener_neutrality]], rev. 2026-06-11: civic tier allows issue-pointed persona advocacy; never person/group attacks or national third rails) + plain-knowledge rule ([[feedback_opener_reading_level]]).
- Headnote (D10, Headnote-Spec.md): register-aware italic headnote on both copies, written FIRST; personas framed by role, no fabricated names, no AI disclosure in it.
- Audience toggle (D11, General-English-Mode-Spec.md): ap_lang | general_english swaps labels/alignment only, learning content identical; AP Lang stays the LAUNCH WEDGE, general-English is marketing-gated on a reading-level check with a real general-English teacher.
- Delivery frequency: magic-link prefs page, NO portal (deferred until multi-seat + billing + archive co-exist); broadcast + edition-rolled rotation (no per-teacher streams); frequency free, never a tier.
- Scope/cadence: AP Lang only in 2026; weekdays only, default 5/wk; June-July auto-throttle to 1/wk (replaces a pause toggle; billing untouched = summer-as-feature); annual billing default; no Pro tier year 1; the AP canon stays OUT of the default cadence (D-004/D-008).
- Quality bar: Samuel is the editor; eyeball every edition's facts until accuracy holds across a real batch; one teacher-feedback issue at a time ([[feedback_one_issue_at_a_time]]).

**Timeline:** customer discovery May-June 2026; fall manual MVP Sept (live classrooms); convert pilots to paying Oct. FIRST TEACHER MEETING 2026-06-08 (Samuel's own AP Lang teacher) went well — produced the headnote feature (#1), general-English direction (#3); issues #2+ still unprocessed.

**Open items:** delivery-stack NEXT steps above; teacher-feedback issues #2+; regenerate/pull the pre-guardrail partisan + jargon samples in Sample-Briefs before any teacher demo; run the human AP-Lang blind panel; reading-level check before marketing general-English; delete the fake test Teacher records in Base44 (low pri).

**Detail map:** specs live in vault `10_Projects/Caught Up AI/`; session-by-session history in `20_Conversations/` (dated, one per session); product brief v1.1 + decisions log + meeting briefs in `C:\Users\srlev\OneDrive\Documents\Claude\Projects\Caught Up AI\`; build-readiness plan-of-record at `C:\Users\srlev\.claude\plans\we-have-been-working-silly-cloud.md`. For any Caught Up AI session, this file + the relevant spec file is enough to orient.
