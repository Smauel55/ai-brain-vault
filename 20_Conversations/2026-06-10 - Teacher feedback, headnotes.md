---
created: 2026-06-10
updated: 2026-06-10
tags: [conversation, caught-up-ai, product, teacher-feedback, headnote]
project: "[[Caught Up AI]]"
---

# 2026-06-10 — Teacher feedback, refining the product (headnotes)

## Context

First teacher meeting happened (2026-06-08, Samuel's own AP Lang teacher). Meeting went well; teacher was very interested. Samuel is working through his feedback one issue at a time. This session = issue #1. (More issues to come; this log will grow.)

## Teacher feedback, issue #1: the prose reads impersonal

- Writing quality was strong; the one problem was that the pieces felt impersonal.
- His reasoning: a large part of AP Lang is reading for the author's point of view, audience, and purpose, which reveal the underlying tone.
- Example he loved: a Dwight Eisenhower letter to the Allied forces, because it opened a window onto how Eisenhower saw and addressed his troops.
- His fix: a short context blurb before each piece, telling the reader who is speaking, to whom, and why.

## Decision: adopt a register-aware AP-exam-style headnote

Honest read (not blind agreement): the idea is right, but with caveats.
- Why right (stronger than he framed it): the real AP Lang exam opens every passage with a one-sentence italic headnote giving speaker/audience/occasion. Adopting it makes our stimulus look like the actual test. It also primes rhetorical reading (SOAPSTone).
- Caveat 1: a headnote does not fix impersonal prose (that is a generation problem, the [[Proxy-Pilot-Run-2]] diagnosis). It only earns its place if written FIRST and the piece is drafted to earn it. Otherwise it is a caption masking the symptom.
- Caveat 2: the Eisenhower payoff (a real person revealed) is the one thing we cannot replicate for invented personas. So: no elaborate fake bios.
- Caveat 3: speaker/audience/purpose does not map onto neutral registers (Ledger, Long Look); those get an occasion/context line, not a fake speaker.

Two judgment calls Samuel approved by saying "build what you recommended":
1. Frame invented personas by ROLE and scenario ("an open letter from a small-town pharmacist to..."), never a fabricated named person. Real subjects (a real person in a Tribute, real events in a Ledger) are named truthfully. Same as the AP exam framing a fiction excerpt.
2. The headnote does NOT disclose AI authorship. That is a teacher/product-level matter; inside the stimulus the student analyzes the situation as presented, like a constructed AP synthesis scenario.

Samuel's added instruction: headnote on BOTH copies; use real AP Lang exam headnotes as the style guide.

## What was built

- New spec: [[Headnote-Spec]] (D10) — form rules, the two honesty rules, neutrality inheritance, a register-by-register content table, the write-it-first forcing function, and an AP-exam style guide with banned moves.
- Renderer `Sample-Briefs/render_opener_v2.py`: added a `headnote` field, rendered as an italic AP-exam-style line (Times-Italic, `hnote` style) directly above the article on BOTH teacher and student copies. Optional/backward-compatible (older pieces without the field still render). Verified by rendering the built-in Long Think sample and extracting text from both PDFs: headnote present on both.
- Generation wiring: [[Generation-Briefs]] now has a write-the-headnote-first step, a headnote slot in all 7 briefs' "Fill before drafting," and a Gate 2 pre-flight check (the finished prose must actually deliver the speaker/audience/purpose the headnote promises). Sample prompt [[caughtupai-sampleprompt-V1]] updated: Headnote-Spec added to its read-list and a HEADNOTE block added to its output.

## Open threads

- Issue #2+ from the teacher meeting still to come.
- Backfill decision pending: existing demo PDFs (the 2026-06-08 meeting edition; the 28-piece batch in `openers.json`) have no headnotes yet. Offered to backfill the key demo pieces or regenerate fresh; awaiting Samuel's call.
- Google Docs export paths (`render_opener_html.py`, `render_opener_docx.py`) still need the same `headnote` field if Openers are ever delivered as Google Docs; the PDF path is done.
