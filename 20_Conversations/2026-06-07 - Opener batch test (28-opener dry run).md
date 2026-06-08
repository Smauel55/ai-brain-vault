---
created: 2026-06-07
updated: 2026-06-08
tags: [conversation, caught-up-ai, openers, testing, workflow]
project: "[[Caught Up AI]]"
---

# 2026-06-07 - Opener batch test (28-opener dry run)

## What happened
- Ran the [[Opener-Batch-Test-Plan]] as a multi-agent workflow: 28 openers, 4 per register, register-by-fact-basis matrix (18 real-news live-sourced, 10 evergreen/persona).
- Phase A (scout + lock): 4 web-research scouts -> 48 candidates -> locked a 28-row variety matrix. Corrected the matrix templates/openers for cross-batch spread (no adjacency, capped per 7-window). Saved `Sample-Briefs/openers_matrix.json`.
- Phase B (generate + verify): pipeline per opener = SOURCE -> DRAFT (register + friction layer + device tags + full AP apparatus) -> 4 adversarial verifiers (accuracy/devices/MCQ/mechanical) -> redraft once on fail -> cross-piece critic.
- Workflow was interrupted overnight (app closed). Cross-session resume did NOT cache-hit and re-ran ~364 agents, burning ~8.8M tokens and a 5-hour limit. Recovered by harvesting the 28 finished dicts from the on-disk journal at zero model cost (`extract_openers.py` -> `openers.json`).
- Rendered all 28 to teacher+student PDFs (56 files) and opened the 28 teacher copies.

## Issues Samuel found in review (see [[Opener-Batch-Test-Results]] for the fix plan)
1. Literal `[[ ]]` brackets, not highlighted: ids 1,3,6,9,16,17,20,25,27,28. Cause: closers written as `[[n]]` not `[[/n]]` (or dropped). Mostly a deterministic regex repair.
2. In-text academic citations in the prose: ids 12,24. Must never appear; strip them and ban in the prompt + verifier.
3. (Deferred) No annotations at all: ids 2,4.
4. (Unspecified) "one issue with the type of article in general" — Samuel to detail next session; do not guess.

## Decisions / lessons
- Do NOT rely on cross-session workflow resume; it re-ran everything. Keep the app open for long runs or use a scheduled/remote routine. Harvest from the journal if interrupted.
- The dicts in `openers.json` are the source of truth; edit them and re-render, do not regenerate prose.

## Next
- Continue in a new session: apply Issue 1 + 2 fixes (mostly deterministic), re-render, then address Issue 3, the unspecified type issue, the cross-piece sameness critic, and accuracy spot-checks (#23 Boeing, political Open Letters #4/#11/#18). Full plan in [[Opener-Batch-Test-Results]].
