---
created: 2026-05-16
updated: 2026-05-16
tags: [conversation, caught-up-ai, build-readiness]
project: "[[Caught Up AI]]"
---

# 2026-05-16 — Caught Up AI build-readiness session

## Context

Samuel asked, in plan mode, how confident Claude really is that it can build exactly what the [[Caught Up AI]] product brief designs. This turned into a brutally-honest 7-issue working session with everything recorded so the conversation never has to repeat.

## Key points

- Claude's first-pass confidence numbers were too high. Stress-tested down: infrastructure ~75-80%, prompt orchestration ~50-60%, hallucination prevention without human QA ~20-25%. Missed categories entirely on first pass (deliverability, support, ops).
- The parts Claude is most confident in (auth, billing) matter least to whether the venture wins. Daily brief quality over months is what matters, and Claude cannot self-verify against the AP Lang teacher bar.
- "Training Claude on AP Lang videos" is a misconception. Claude is a fixed model. A curated reference corpus (RAG) raises the floor but does not replace teacher-in-the-loop verification.
- A calendar collision was found in the brief's timeline: the manual MVP cannot run July-early August because U.S. schools are out. September goal reframed.
- Core throughline: the build risk is a 2027 scale-phase problem. September 2026 is a sales-and-evidence problem solvable with zero code.

## Decisions

See [[Decisions Log]] D-002 for the canonical list. Seven decisions locked: Samuel as quality bar (with trigger), sample-based hallucination audit, open/CC-only sourcing, hybrid drift management, 3-tier editorial framework, Claude support agent + optimized infra, timeline reframe. Discovery script revised into Product Brief v1.1.

## Action items

- [ ] Samuel — verify the Wildfire pre-accelerator fall-2026 application deadline (highest-leverage open fact)
- [ ] Samuel — during the Claude mastery plan window, start building the AP Lang reference corpus as a side activity (AP Daily transcripts, College Board scoring guides, released FRQs)
- [ ] Samuel — hand-write 1-2 sample briefs before customer discovery starts (needed for the new sample-brief reaction question)
- [ ] Carry the revised Section 8 script (Product Brief v1.1) into customer discovery

## New knowledge to file

The plan-of-record file `C:\Users\srlev\.claude\plans\we-have-been-working-silly-cloud.md` is the canonical artifact, including the full QA scaffolding spec for the eventual build. Not duplicated into `30_Knowledge/`; referenced from the project memory file instead.

## Open threads

- Freshness window, personalization model, and topics-to-avoid handling all deferred to customer discovery answers.
- Editorial neutrality policy needs final lock before manual MVP.
- Strategic question logged but not resolved: AP-Lang-only TAM (~$240k ARR at 10% saturation) is a healthy solo business but not venture-scale alone; the venture case rests on the expansion path. Separate conversation needed.
