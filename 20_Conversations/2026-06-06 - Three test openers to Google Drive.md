---
created: 2026-06-06
updated: 2026-06-06
tags: [conversation, caught-up-ai, opener, test-batch, google-drive]
---

# 2026-06-06 - Three test openers to Google Drive

First full end-to-end test run of the [[Caught Up AI]] opener engine: three fresh openers built from the specs, delivered to Google Drive.

## What was built
Three openers, registers chosen for variety (per the Cross-Piece-Sameness-Rubric):
- **Totality** - The Long Look (lyric awe; renders an eclipse, withholds judgment).
- **The Books We Don't Read** - The Long Think (reasons to an earned turn; the "antilibrary").
- **The Recycling We Were Sold** - The Reckoning (moral charge; ~9% plastic recycled, OECD).

Each doc = student copy + teacher copy in one file: marked article (yellow highlight, whole-device spans, controlled vocab, concession tagged alone), devices-and-why, 2 reading MCQs + key (two different AP skills, named distractor traps), discussion + sample responses, Q2/Q3 writing prompt, misconceptions, AP alignment, and a test-run sourcing note.

## Decisions
- Test ran on EVERGREEN/stable subjects on purpose: isolates the prose engine from the live-sourcing gate, so no breaking-news facts were fabricated. Every factual claim carries a flagged sourcing note per the Accuracy-Guardrail.
- Engineered variety in first: 3 distinct opener types, closes, rhythms, paragraph counts. Mechanical anti-tell pass clean (0 em-dashes, 0 banned vocab).

## Delivery + the tooling constraint
- Could NOT put native .docx in Drive: the Google Drive connector only auto-converts text/plain to a native Doc, and pushing a binary .docx requires emitting ~55k chars of base64 verbatim (unreliable, corrupts the file). Native Docs created via the connector cannot carry background-color highlight.
- Solution: uploaded each as an HTML file (text I author directly), which opens in Google Docs with the yellow highlight intact. Upload fidelity verified (Drive fileSize == local source byte counts).
- Drive folder: "Caught Up AI - Test Openers (2026-06-06)". Real .docx copies (true highlight) also saved locally in 10_Projects/Caught Up AI/Sample-Briefs/.
- See [[reference_drive_mcp_formatting]].

## Artifacts
- Renderers: Sample-Briefs/render_opener_docx.py (data + .docx) and render_opener_html.py (HTML for Drive). Single source of truth = the data dicts in render_opener_docx.py.

## Open / next
- Confirm the HTML opens cleanly in Google Docs with highlight (open one and check).
- These three are candidates for the human AP-Lang panel blind test.
