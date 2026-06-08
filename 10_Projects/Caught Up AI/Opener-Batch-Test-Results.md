---
created: 2026-06-07
updated: 2026-06-08
tags: [project, caught-up-ai, testing, openers, handoff]
project: "[[Caught Up AI]]"
---

# Opener Batch Test, results and fixes (handoff)

Dry run of [[Opener-Batch-Test-Plan]]. 28 openers generated, verified, and rendered on 2026-06-07. Samuel reviewed the teacher PDFs and found three rendering/content issues plus one unstated "article type" concern. This note is the handoff so a fresh session can finish the fixes without re-running the expensive generation.

## What exists on disk (do NOT regenerate)

All in `10_Projects/Caught Up AI/Sample-Briefs/`:
- `openers.json` — the 28 final opener dicts (render schema + `_meta` id/register/basis). This is the source of truth; edit THIS, then re-render.
- `openers_matrix.json` — the locked 28-row variety matrix (register, basis, topic, template, open/close, sources).
- `render_batch.py` — renders openers.json to 56 PDFs (teacher+student), `randomize_answers` once per piece. Run: `python render_batch.py openers.json`.
- `extract_openers.py` — harvested the dicts from the interrupted workflow journal (already run; kept for reference).
- `render_report.json` — id/register/basis/headline/FRQ/answers/pages table.
- 56 PDFs named `Caught Up AI Opener - 2026-06-07 - <Headline> (<Register>) - {Teacher|Student} copy.pdf`.
- `wf_generate_run.js` / `wf_generate.js` — the generation workflow (embedded matrix). Only needed if regenerating prose.

Generation history: the generate+verify workflow (run `wf_8b080f31-5ee`) was interrupted overnight, then a cross-session resume re-ran most agents (this burned ~8.8M tokens and a 5-hour limit, Samuel was rightly unhappy). LESSON: cross-session `resumeFromRunId` did NOT cache-hit; do not rely on it. For long runs, keep the app open or use a scheduled/remote routine. The dicts were ultimately harvested from the on-disk journal with zero model cost.

## The three issues Samuel flagged (fix 1 and 2 now; 3 is deferred)

> **STATUS 2026-06-08: Issue 1 FIXED + permanent fix COMPLETE. Issue 2 data-fixed but being RE-DONE (scope widened, see below).** See [[2026-06-08 - Opener batch fixes (Issue 1 and 2)]]. `openers.json` corrected in place (backup: `openers.backup-pre-fix-2026-06-08.json`); all 56 PDFs rebuilt; verified opens=closers=device count on every piece, no raw `[[ ]]` leaks. #17 was re-tagged by hand (NOT a missing-closer; 6 devices, tags laid as 3 pairs, numbers not mapping to devices).
> **Issue 1 permanent fix (defense in depth, all in place):** (1) draft prompt in `wf_generate.js` now shows the exact `[[1]]...[[/1]]` slashed shape + a self-check; (2) the mechanical AND devices verifiers now explicitly check slash-closers and opens=closes=devices counts; (3) a DETERMINISTIC tag gate (`normalizeClosers`+`tagLint`) runs in the workflow's verify stage — auto-repairs duplicate-closers, forces a redraft on anything it can't fix (unit-tested on all three bug shapes); (4) `normalize_closers()` in `render_batch.py` is the final render-time net. A model verifier reads `[[1]]..[[1]]` as "span 1" and is blind to the defect; the deterministic gate is the real fix.
> **Issue 2 DONE 2026-06-08 (widened scope).** #12 and #24 rewritten as prose to remove ALL in-text scholarly citations — not just `(Author, year)` parentheticals but inline forms too ("Carstensen's work", "Portfolio studies do find", "one of the most replicated results..."). Facts kept true, device spans untouched. Permanent fix baked in: explicit citation ban added to [[Anti-Tell-List]] (fixed the ambiguous "names a source" rule + new banned item + step 7) and [[Accuracy-Guardrail]] (traceability lives in the fact list, not the prose); draft-prompt ban + mechanical-verifier check (8) + a deterministic `citationLint` gate in `wf_generate.js` (tested: flags the raw pre-fix citations, passes the fix). See [[feedback_openers_no_citations]].
> **CROSSCHECK FINDING 2026-06-08 (the audit the original run never did).** A render-truth crosscheck across all 28 (run the actual renderer + count/parse tags) caught TWO defects the quick audit MISLABELLED as correct: **#5** (device-4 span left unclosed, leaked a raw `[[4]]`) and **#10** (crossed/overlapping Concession+Logos spans `[[1]]..[[2]][[/1]][[/2]]`, only 4/5 parsed). Both FIXED (hand re-tag; #10 split into two adjacent spans per the device purposes). Net: ALL 26 active pieces now clean; the old "14 correct pieces" list below was WRONG (it included #5 and #10). Render driver also hardened with retry/backoff against intermittent OneDrive file-lock (errno 22) that was leaving the 56-PDF batch half-rendered.
> **Issue 3 DONE 2026-06-08.** #2 and #4 hand-tagged (11 spans from the device purposes); all 28 openers now fully tagged, citation-free, render-clean (full render-truth crosscheck passes). REMAINING: device-label cleanup (the #17 "Syntax"/double-"Logos" and the #4 "Polysyndeton"/"Allusion" mislabels, a device-vocabulary pass); #24 residual study-description; the unspecified "article type" issue (needs Samuel); cross-piece sameness critic over the 28; accuracy spot-checks (#23 Boeing, political Open Letters).

Diagnostic already run (per-opener tag/citation audit). Precise affected lists:

### Issue 1: literal `[[ ]]` brackets instead of highlights (FORMATTING) — FIXED 2026-06-08
- Affected ids: **1, 3, 6, 9, 16, 17, 20, 25, 27, 28** (10 pieces).
- Root cause: the renderer (`render_opener_v2.py`, regex `MARK = \[\[(\d+)\]\](.*?)\[\[/\1\]\]`) requires a SLASHED closing tag `[[/n]]`. These drafts closed the span with a second `[[n]]` (no slash), so nothing matched and the raw tags printed with no highlight and no device-name label. #17 dropped the closer entirely (6 opens, 0 closers of any kind).
- CORRECTED 2026-06-08: the quick audit's "14 correct pieces" list was WRONG. It named 5,7,8,10,11,13,14,15,18,19,21,22,23,26 as clean, but the render-truth crosscheck found **#5** (unclosed device-4 span) and **#10** (crossed spans, 4/5 parsed) were ALSO broken. Genuinely-clean-from-the-start pieces: 7,8,11,13,14,15,18,19,21,22,23,26. Lesson: do NOT trust opens-vs-closers counts alone (#10 had balanced counts but mismatched numbering); run the actual renderer + MARK parse as the source of truth. (Also: id 17 was mis-labelled "ok" by the same audit; it was broken, now fixed.)
- FIX (mostly deterministic, no model):
  - For the 9 duplicate-closer pieces (1,3,6,9,16,20,25,27,28): regex-repair each body string so the SECOND `[[n]]` of each pair becomes `[[/n]]`. Per paragraph, for each n that appears exactly twice as `[[n]]`, replace the 2nd occurrence with `[[/n]]`. Then re-render and eyeball.
  - For #17 (closers missing entirely): the span END is unknown, so a pure regex cannot place `[[/n]]`. Options: (a) cheap targeted re-tag of just #17's body (one small model call that returns the body with correct `[[n]]...[[/n]]` spans, devices array unchanged), or (b) hand-place closers using the device `purpose` text as a guide. Prefer (a), one agent.
  - PERMANENT FIX to prevent recurrence: either harden the renderer to also accept a second `[[n]]` as the closer, OR add a normalization pass in render_batch.py that repairs closers before building. Recommend the normalization pass (keeps the renderer strict). Also tighten the draft prompt: show the exact `[[1]]span[[/1]]` shape with the slash and add a self-check "every open tag has a matching slashed close."

### Issue 2: in-text academic citations in the prose (CONTENT) — FIXED 2026-06-08
- SCOPE BROADENED 2026-06-08 (Samuel): ban is NOT just parentheticals — it covers ALL in-text scholarly citation, including inline forms ("Carstensen's work," "Portfolio studies do find"). No in-text citations of any kind in an Opener. See [[feedback_openers_no_citations]].
- PERMANENT FIX BAKED IN 2026-06-08: deterministic tag-lint+auto-normalize gate + hardened draft prompt + tightened verifier tag check + explicit in-text-citation ban all wired into `wf_generate.js` (modified, uncommitted); helpers unit-tested. Suggested-order item 4 below is DONE.
- Affected ids: **12, 24** (both evergreen; e.g. "(Kahneman and Tversky, 1979)", "(Ameriks and Zeldes, NBER 2004)").
- Root cause: the SOURCE stage gave these evergreen pieces scholarly references and the DRAFT folded them in as parenthetical citations. The product must NEVER show in-text citations or reference lists; facts are stated plainly (the citation is the AI/academic tell and is off-brand).
- FIX: strip parenthetical citation patterns `\([A-Z][^)]*\b(18|19|20)\d\d[a-z]?\)` from those two bodies, then re-read each sentence so it still flows (the strip can leave a dangling space or stranded clause). This is light but needs a human/quick model read, not blind regex. PERMANENT FIX: add to the draft prompt and the mechanical/anti-tell verifier an explicit ban on in-text citations and reference lists in the prose. (The accuracy guardrail already says attribute facts, but that means name a body inline like "the GAO reported," NOT academic parentheticals; clarify this distinction in [[Accuracy-Guardrail]] and [[Anti-Tell-List]].)

### Issue 3: no annotations at all — FIXED 2026-06-08
- Affected ids: **2, 4** (Reckoning "The First State to Name the Man"; Open Letter "The Purse You Promised to Guard"). Body had zero `[[n]]` tags though the devices array and explanations existed, so the marked-article section showed nothing.
- FIXED: hand-placed all 11 spans (6 in #2, 5 in #4) from each device's `para`+`purpose`, in device order, non-overlapping, via `fix_openers_issue3.py` (assert-on-match, render-truth crosscheck passes). Every span maps to the right device note; re-rendered. All 28 openers now fully tagged + render-clean.
- DEVICE-LABEL FLAGS found while tagging #4 (NOT fixed; same class as the #17 label issue, queued for the device-vocabulary pass): device 5 is labelled **Polysyndeton** but "spent on nothing, helping no child, vindicating no principle" has NO conjunctions (that is asyndeton; #2 device 4 correctly calls an identical list "Asyndeton"); device 3 labels a direct constitutional quote an **Allusion**. See [[feedback_device_vocabulary]].

## The fourth, still-unspecified issue
Samuel said there is "one issue with the type of article in general" but did not detail it before ending the session. ASK him to specify before acting. (Possible candidates to raise: the batch leans politically heavy on the real-news pieces; or a register/topic-type concern. Do not guess and rework.)

## Other deferred items from the run (not yet done)
- The batch-level CROSS-PIECE SAMENESS critic was skipped to save tokens; run it cheaply over the 28 first sentences/spines when convenient ([[Cross-Piece-Sameness-Rubric]]).
- Accuracy spot-checks before any classroom use: **#23 "The Record Behind the Bolt" (Boeing)** scouted source was a weak outlet, confirm the specific June 4 2026 incident; and glance at the three political Open Letters (#4 Vought, #11 Roberts, #18 Trump) for classroom-neutrality fit.

## Suggested order for the next session (token-frugal)
1. Write a `fix_openers.py` that: (a) normalizes duplicate-`[[n]]` closers to `[[/n]]` for ids 1,3,6,9,16,20,25,27,28; (b) strips in-text citations for 12,24. Deterministic, zero model cost.
2. One small agent to re-tag #17 (and, if doing Issue 3, #2 and #4).
3. Re-run `python render_batch.py openers.json`, reopen the affected teacher PDFs, confirm.
4. Bake the permanent fixes into `wf_generate.js` draft prompt + the renderer/normalizer so a future batch does not repeat this.
5. Ask Samuel about the unspecified "article type" issue and run the cross-piece critic.

## Render report (28 openers, as generated 2026-06-07)
See `render_report.json`. FRQ split is correct by register (argument registers Q3; observational/consecratory Q2). 6 pieces were verifier-redrafts (6,8,9,12,16); the rest passed adversarial verify first pass.

## Related
[[Opener-Batch-Test-Plan]], [[Register-Specs]], [[Anti-Tell-List]], [[Rhetorical-Device-Vocabulary]], [[MCQ-Construction-Spec]], [[Accuracy-Guardrail]], [[Cross-Piece-Sameness-Rubric]], [[Caught Up AI]].
