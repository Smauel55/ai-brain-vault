---
created: 2026-06-11
updated: 2026-06-11
tags: [conversation, caught-up-ai, generation, pipeline]
---

# 2026-06-11 - Opener Generation Pipeline

## What happened
- Started by designing an on-demand "build an Opener on a whim" paste-prompt ([[caughtupai-quickprompt-V1]]) and baking model-routing guidance into it.
- Samuel reframed: it is not a whim tool, it is the beta for the real product. Asked to build the production generation pipeline now.
- Built the pipeline as an enforced, model-routed workflow and proved it end to end.

## Decisions (AskUserQuestion)
- Build scope: generation pipeline only this pass (delivery + scheduling deferred).
- No mid-run human approval; pipeline runs end to end.
- Beta delivery will be email with PDF attachments, but that is out of this build.

## Built
- `.claude/workflows/caughtup-opener.mjs` - 3 phases: Verify (Haiku) -> Compose (Fable 5) -> Render (Haiku). Model routing enforced per phase.
- Data contract locked by JSON schema mirroring `render_opener_v2.py`'s piece dict; renderer left unmodified.
- New `Sample-Briefs/editions-log.tsv` for persistent recency, so runs do not repeat the last register/template/opener/close.
- Doc: [[Generation-Pipeline]].

## Verified by behavior
- First run produced both PDFs (~850KB each) unattended in ~8.5 min / ~193k tokens.
- Story chosen and verified by the pipeline: 2026 US measles totals (The Ledger register).
- Facts independently re-confirmed against CDC / CIDRAP / CNN (2,030 cases as of June 4; Spartanburg 997, over Apr 26; 945/990 unvaccinated). Haiku verify pass was accurate.
- Structure clean: [[n]] device marks mapped correctly, 2 MCQs on different AP skills, devices only from the controlled list, no em-dashes/emojis/citations.

## Open / next
- Eyeball facts before any Opener reaches a real teacher until it holds across a batch.
- Deferred: email-PDF delivery, daily scheduling.
- Prior session's general-English Base44 build still has Publish + live re-verify open (separate thread).
