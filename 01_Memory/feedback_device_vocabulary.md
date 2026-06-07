---
name: feedback-device-vocabulary
description: "Caught Up AI lesson openers may label/highlight rhetorical devices ONLY from a fixed AP list, and only where genuinely present"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 776a4dc9-83ea-452d-8043-9832204b5684
---

For Caught Up AI lesson openers (and any rhetorical-device labeling for the product), use ONLY the fixed AP device vocabulary, and tag a device only where it is genuinely present. Do not invent device names ("the level close", "comparison that sets scale") and do not force a label to hit a count.

The controlled list with definitions lives at `10_Projects/Caught Up AI/Rhetorical-Device-Vocabulary.md`. Two changes Samuel made 2026-06-06: (1) REMOVED "Understatement / litotes" from the list (too flimsy to teach reliably); do not tag it. (2) Allusion must be to something the average reader would recognize; a fact only specialists know (e.g., a motto carved on one specific building) does not work as an allusion because the borrowed meaning never lands.

**Why:** Samuel flagged on 2026-06-05 that early sample briefs invented loose device names and mislabeled devices (called mid-clause parallelism "anaphora"). The customer is an AP Lang teacher; a wrong device label is a credibility failure.

**How to apply:** When highlighting or explaining devices in a piece, pick the single correct term from the list. Watch the look-alikes: anaphora is repetition at the START of clauses (mid-clause repetition is parallelism); keep metaphor vs simile, antithesis vs juxtaposition, asyndeton vs polysyndeton distinct. Relates to [[feedback_ai_writing_formulaic]] and the [[project_caught_up_ai]] prose engine.

**2026-06-06 Opener-format rules (three additions Samuel set on the rough draft):**
1. Highlight every device in ONE color, not a different color per device. The v2 renderer `10_Projects/Caught Up AI/Sample-Briefs/render_opener_v2.py` uses a single light-yellow highlight (#FFF3A0, chosen to stay legible on a black-and-white printer) + single dark-blue inline label (#1F4E79). (The v1 `render_briefs.py` six-color scheme is superseded.)
2. Name the SPECIFIC device, never the umbrella category. A short clipped sentence is a "telegraphic sentence," not "syntax." "Telegraphic sentence" was added to the controlled list for exactly this. Prefer the precise named device wherever one exists over "syntax"/"diction"/"tone".
3. In the TEACHER copy, do not just point out and describe each device, also give its PURPOSE: why the author chose it and what it accomplishes. Keep each to a line or two, readable at a glance (a "Devices, and why they are here" section). Student copy stays clean.

First piece built in this format: the Long Think opener "What the Waiting Did" (2026-06-06), teacher + student PDFs in Sample-Briefs/.
