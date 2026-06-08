---
created: 2026-06-08
updated: 2026-06-08
tags: [conversation, caught-up-ai, openers, testing]
project: "[[Caught Up AI]]"
---

# 2026-06-08 — Opener batch fixes (Issue 1 and 2)

## Context

Continued the 28-opener dry run from a handoff note ([[Opener-Batch-Test-Results]]). Applied the Issue 1 and Issue 2 fixes, then dug into root cause: why the bugs happened and why the verify pass missed them.

## Key points

- Verified the handoff's diagnosis against the file: all 12 affected pieces matched exactly.
- **Issue 1 (highlights) fixed** for all 10 pieces. The 9 duplicate-closer pieces (1,3,6,9,16,20,25,27,28) repaired deterministically (2nd `[[n]]` → `[[/n]]`). #17 was NOT a simple missing-closer: 6 devices but tags laid as 3 open/close pairs, numbers not mapping to devices. Re-tagged by hand from each device's `purpose` text. No model agent, zero token cost.
- **Issue 2 (citations) fixed** for #12 and #24. Stripped every `(Author, year)` parenthetical, re-read all modified sentences for flow. Clean.
- All 56 PDFs re-rendered. Verified opens = closers = device count on every fixed piece; teacher render emits correct highlight count; no raw `[[ ]]` leaks.
- Tooling added: `fix_openers.py` (one-shot, idempotent, backs nothing up itself), `normalize_closers()` in `render_batch.py` (render-time self-heal for the duplicate-closer class). Backup at `openers.backup-pre-fix-2026-06-08.json`.

## Decisions

- **Root cause is NOT "didn't verify all openers" or "no crosscheck."** Samuel floated that; I disagreed with evidence. Pieces 6, 9, 16, 12 were verifier *redrafts* yet still shipped these exact defects, and the broken tag pattern is 100% identical across all 9 pieces. Coverage would not have caught them.
- Real causes: (1) **Issue 1** is a format-contract mismatch (drafter wrote `[[n]]` close, renderer's regex demands `[[/n]]`) that is invisible to a content/semantic verifier — verify and render were decoupled, nothing ever ran the renderer or counted tags. (2) **Issue 2**: the accuracy guardrail *rewards* attribution, so an academic parenthetical read to the verifier as GOOD sourcing, not an off-brand tell; the "inline attribution OK, parenthetical citation banned" distinction was never encoded. Hit only #12/#24 because they're the evergreen/research pieces whose source stage pulled scholarly refs.
- The cross-piece **sameness critic checks for templated sameness**, not tag syntax or citations, so it was genuinely irrelevant to these two issues.
- **Permanent fix = a deterministic lint gate** (run renderer + assert opens=closers=devices + scan citation regex), zero tokens. That same diagnostic found and confirmed the fixes. Should become a required batch stage.

## Action items

- [ ] Make the mechanical lint gate (tag balance + citation scan) a required stage in `wf_generate.js`; harden draft prompt to show the slashed `[[1]]…[[/1]]` shape + self-check; add explicit in-text-citation ban to the anti-tell verifier brief. (Only bites on regenerate.)
- [ ] Issue 3 (deferred): re-tag #2 and #4 (zero `[[n]]` spans though devices exist).
- [ ] Ask Samuel to specify the unstated "article type" concern.
- [ ] Run the cross-piece sameness critic over the 28 first sentences/spines.
- [ ] Accuracy spot-check #23 (Boeing) source; classroom-neutrality glance at #4/#11/#18.

## Open threads

- Residuals noticed, not fixed (out of Issue 1/2 scope): #17 device labels include umbrella terms (`Syntax`, two `Logos`); #24 still reads academic after the citation strip (`Carstensen's work` survives inline, "Portfolio studies do find," etc.).

## Related

[[Opener-Batch-Test-Results]], [[Caught Up AI]], [[Anti-Tell-List]], [[Accuracy-Guardrail]], [[Rhetorical-Device-Vocabulary]], [[Cross-Piece-Sameness-Rubric]]
