---
created: 2026-06-11
updated: 2026-06-11
tags: [project, caught-up-ai, teacher-feedback, tracker]
project: "[[Caught Up AI]]"
---

# Teacher Feedback Tracker

Running log of what the teacher has raised and how each item was resolved. First meeting: 2026-06-08 (went well; teacher very interested). Refinements worked one item at a time since.

## Resolved

### 1. Prose read impersonal / voiceless
- **He said:** the Openers were strong but felt impersonal, no clear point of view.
- **Resolved (2026-06-10):** added a register-aware, AP-exam-style **headnote** (one or two italic sentences naming speaker/audience/occasion), written FIRST as a forcing function so the prose commits to a point of view instead of defaulting to the generic explainer voice. On both teacher and student copies. Personas framed by role (no fabricated names, no real people), no AI disclosure in the headnote.
- **Status:** DONE. Wired into the renderer, the generation briefs, and the sample prompt.

### 2. Civic teachers want pointed pieces
- **He said:** civic-subscription teachers actually want pointed pieces (pointed but not aggressive). AP Lang teaches persuasion, and position-taking rhetoric is the richest thing to analyze.
- **Resolved (2026-06-11):** the neutrality firewall now has **two modes**. Neutral-explainer (every tier, always safe) and **pointed advocacy (civic tier only)**, where a piece may argue a position with full force in a clear rhetorical situation, aimed at the issue or institution. Three hard bans kept on every tier: no attack on a named/identifiable person, no attack on a group, no side on the national third rails (abortion, guns, partisan elections/candidates, birthright-citizenship-style value questions stay neutral). Pointed pieces must **vary in form** (op-ed, unsigned editorial, first-person essay, letter to a body, witness account), not all be one testimony template.
- **Status:** DONE in spec and propagated to all generation files. NOT yet pressure-tested with a live batch (the open verification step).

### 3. Works for regular (non-AP) English teachers too
- **He said:** the system would be great for regular English teachers as well; nothing needs to change except the AP-Lang labels on the Openers, the rest is great English practice regardless.
- **Decided (2026-06-11):** keep **AP Lang as the launch wedge** (sharp, ownable message); build general-English support as a **post-launch fast-follow**. Mechanism: an "audience: AP Lang / General English" toggle, one more customization dimension like the political dial and delivery frequency. Student Opener stays identical; the toggle swaps only the teacher-copy skill tags (AP reading skills / AP-alignment section -> general reading-analysis or Common Core) and the marketing framing. No second content pipeline.
- **Status:** DIRECTION DECIDED, not built.

## Open actions (mine / Samuel's)
- Pressure-test pointed civic pieces with a real batch: do the forms come out distinct, and do they hold the issue-vs-person line under pressure? (Item 2.)
- Verify reading-level fit with a general-English teacher before scaling the expansion; the prose is AP-caliber in sentence craft, the one claim in "just the labels" not to take on faith. (Item 3.)

## Talking points for next meeting
- Show a pointed civic Opener (the new capability he asked for) and confirm it matches what he meant by "pointed but not aggressive."
- Ask which general-English grade levels his colleagues teach, to gauge the reading-level question.
