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

> **STATUS 2026-06-08: Issues 1 and 2 are FIXED and re-rendered.** See [[2026-06-08 - Opener batch fixes (Issue 1 and 2)]]. `openers.json` corrected in place (backup: `openers.backup-pre-fix-2026-06-08.json`); all 56 PDFs rebuilt; verified opens=closers=device count on every piece, no raw `[[ ]]` leaks, no citations in 12/24. Tooling: `fix_openers.py` (one-shot) + `normalize_closers()` added to `render_batch.py` (render-time self-heal). #17 was re-tagged by hand (it was NOT a missing-closer; 6 devices, tags laid as 3 pairs, numbers not mapping to devices). Issue 3 and the unspecified "article type" issue still open.

Diagnostic already run (per-opener tag/citation audit). Precise affected lists:

### Issue 1: literal `[[ ]]` brackets instead of highlights (FORMATTING) — FIXED 2026-06-08
- Affected ids: **1, 3, 6, 9, 16, 17, 20, 25, 27, 28** (10 pieces).
- Root cause: the renderer (`render_opener_v2.py`, regex `MARK = \[\[(\d+)\]\](.*?)\[\[/\1\]\]`) requires a SLASHED closing tag `[[/n]]`. These drafts closed the span with a second `[[n]]` (no slash), so nothing matched and the raw tags printed with no highlight and no device-name label. #17 dropped the closer entirely (6 opens, 0 closers of any kind).
- The 14 correct pieces (5,7,8,10,11,13,14,15,18,19,21,22,23,26) used `[[/n]]` properly. NOTE id 17 was mis-labelled "ok" by a status-logic bug in the quick audit; it IS broken (closers=0). Trust the closers-vs-opens count, not the status string.
- FIX (mostly deterministic, no model):
  - For the 9 duplicate-closer pieces (1,3,6,9,16,20,25,27,28): regex-repair each body string so the SECOND `[[n]]` of each pair becomes `[[/n]]`. Per paragraph, for each n that appears exactly twice as `[[n]]`, replace the 2nd occurrence with `[[/n]]`. Then re-render and eyeball.
  - For #17 (closers missing entirely): the span END is unknown, so a pure regex cannot place `[[/n]]`. Options: (a) cheap targeted re-tag of just #17's body (one small model call that returns the body with correct `[[n]]...[[/n]]` spans, devices array unchanged), or (b) hand-place closers using the device `purpose` text as a guide. Prefer (a), one agent.
  - PERMANENT FIX to prevent recurrence: either harden the renderer to also accept a second `[[n]]` as the closer, OR add a normalization pass in render_batch.py that repairs closers before building. Recommend the normalization pass (keeps the renderer strict). Also tighten the draft prompt: show the exact `[[1]]span[[/1]]` shape with the slash and add a self-check "every open tag has a matching slashed close."

### Issue 2: in-text academic citations in the prose (CONTENT) — FIXED 2026-06-08
- Affected ids: **12, 24** (both evergreen; e.g. "(Kahneman and Tversky, 1979)", "(Ameriks and Zeldes, NBER 2004)").
- Root cause: the SOURCE stage gave these evergreen pieces scholarly references and the DRAFT folded them in as parenthetical citations. The product must NEVER show in-text citations or reference lists; facts are stated plainly (the citation is the AI/academic tell and is off-brand).
- FIX: strip parenthetical citation patterns `\([A-Z][^)]*\b(18|19|20)\d\d[a-z]?\)` from those two bodies, then re-read each sentence so it still flows (the strip can leave a dangling space or stranded clause). This is light but needs a human/quick model read, not blind regex. PERMANENT FIX: add to the draft prompt and the mechanical/anti-tell verifier an explicit ban on in-text citations and reference lists in the prose. (The accuracy guardrail already says attribute facts, but that means name a body inline like "the GAO reported," NOT academic parentheticals; clarify this distinction in [[Accuracy-Guardrail]] and [[Anti-Tell-List]].)

### Issue 3 (DEFERRED per Samuel): no annotations at all
- Affected ids: **2, 4** (Reckoning "The First State to Name the Man"; Open Letter "The Purse You Promised to Guard"). Body has zero `[[n]]` tags though the devices array and explanations exist, so the marked-article section shows nothing pointing to the device notes.
- FIX (later): targeted re-tag of just these two bodies (one small agent each) to insert `[[n]]...[[/n]]` spans matching the existing devices arrays, or regenerate devices+tags together.

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
