---
created: 2026-06-06
updated: 2026-06-06
tags: [conversation, caught-up-ai, opener, pdf, formatting]
project: "[[Caught Up AI]]"
---

# 2026-06-06 — Caught Up AI Opener samples and format

## Context

Samuel wanted real, inbox-identical sample outputs from the v2 prose engine, then iterated on the PDF format. Session ended mid-formatting; to be continued in a fresh session.

## Key points

- Built a reusable prompt to generate finished Openers end to end (route, verify facts, run the 4 gates): [[caughtupai-sampleprompt-V1]] at 10_Projects/Caught Up AI/caughtupai-sampleprompt-V1.md.
- Generated 3 real-news sample Openers across 3 registers and beats: Ledger (House Ukraine aid vote), Long Look (East Antarctic Fan-shaped Basin Province), Tribute (Marjane Satrapi). Facts web-verified; guardrail caught and fixed two bad facts ("$1.3B" -> >$1B + up to $8B loans; held Satrapi "died of grief" until Wikipedia-confirmed and attributed to family).
- Product is delivered as **PDFs** (teacher copy + student copy per edition), not chat text.
- PDF generator: 10_Projects/Caught Up AI/Sample-Briefs/render_briefs.py. Real logo: Sample-Briefs/caughtup-logo.png (copied from Downloads).
- Final format mirrors Samuel's reference "Teacher Meeting Brief v0.2.pdf" (lives at C:\Users\srlev\OneDrive\Documents\Claude\Projects\Caught Up AI\): plain layout, numbered paragraphs, bold colon headings. Student copy = article + Discussion questions + AP-style MCQ + Writing prompt. Teacher copy = the article marked for devices (highlight + inline [paragraph N: device] label) + Quick reference + MCQ + answer key + sample discussion responses + writing prompt + common misconceptions + AP exam alignment.

## Decisions

- **Product name = "Opener."** The daily PDF a teacher receives is an "Opener" (count noun). Two versions: teacher copy / student copy. Each day = an edition. Do NOT call it a "brief." Saved to memory reference_product_naming.md. File pattern: `Caught Up AI Opener - YYYY-MM-DD - Topic (Register) - Teacher copy.pdf`.
- **Device labels: fixed AP vocabulary only**, only where genuinely present. Full list at 10_Projects/Caught Up AI/Rhetorical-Device-Vocabulary.md; saved to memory feedback_device_vocabulary.md. Fixed a real mislabel: the Satrapi "rendered as... rendered as..." run is parallelism, not anaphora (repeated element is mid-clause).
- Topic mode for samples: real current events (web-verified), not placeholders.
- Writing prompt currently set to Q3 argument for all three (matching the reference); Q2 value noted in AP exam alignment.
- Kept a small logo in the header even though the reference is fully bare (Samuel asked for the logo earlier).

## Action items

- [ ] Next session — continue tweaking Opener formatting (see Open threads for the list).

## New knowledge to file

- Filed in-project: [[Rhetorical-Device-Vocabulary]] (controlled device list). Memory: reference_product_naming.md, feedback_device_vocabulary.md.

## Open threads (resume here next session)

How to resume: open render_briefs.py, edit, rerun `python render_briefs.py` from the Sample-Briefs folder. NOTE: the Read tool cannot rasterize PDFs (poppler/pdftoppm not installed); preview by rendering pages to PNG with PyMuPDF (installed: `import fitz`), then Read the PNG. Delete preview PNGs after.

Pending format decisions Samuel may want to tweak:
- Logo: keep the small header logo, or strip it for an exact match to the bare reference.
- Writing prompt: keep Q3 argument, or switch to Q2 rhetorical analysis per piece.
- Highlight shades, spacing, and how much inline labeling is too much.
- Number of devices highlighted per piece (currently 5 to 7).
- MCQ count and difficulty; consider adding a vocabulary-in-context item.
- Student copy: add a "devices to find" word bank, or keep it blank for independent annotation.
- Per-edition PDFs vs one combined multi-edition PDF.
- The header right-side "Sample edition X of 3" is sample-only; the real product would show just the date.

## Related

- [[caughtupai-sampleprompt-V1]], [[Rhetorical-Device-Vocabulary]], [[Generation-Briefs]], [[Style-Palette]], [[Anti-Tell-List]], [[Accuracy-Guardrail]], [[2026-06-05 - Prose engine v2 build]], [[Caught Up AI]].
