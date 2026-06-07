---
name: reference-mcq-spec
description: Caught Up AI Opener multiple-choice questions follow MCQ-Construction-Spec.md (AP-grounded)
metadata: 
  node_type: memory
  type: reference
  originSessionId: fc148499-c96f-41fd-bb61-341391f8e1fc
---

Caught Up AI Opener MCQs are governed by `10_Projects/Caught Up AI/MCQ-Construction-Spec.md`, grounded in the official AP English Language and Composition CED (2024). Key facts: Section I = 45 multiple choice (23-25 reading + 20-22 writing); the four reading skills are CED Skill Categories 1/3/5/7 (Rhetorical Situation, Claims and Evidence, Reasoning and Organization, Style), which equal Big Ideas 1-4. Watch the off-by-one: "Skill Category 3" is Claims and Evidence, not "Big Idea 3."

Each opener carries exactly 2 reading MCQs that must target DIFFERENT skills. Every distractor must be plausible and partly true and fail by a named trap (right device/wrong effect, right effect/wrong location, true-but-not-the-function-asked, too literal, over-broad/extreme, inverted relationship, out-of-passage import); no free-elimination option a student discards on sight; exactly one defensibly-best answer. Run the spec self-check before shipping.

ANSWER-KEY RANDOMIZATION (Samuel, 2026-06-06): early samples keyed every single question to A. Fix is NOT an even split (that is its own predictable pattern) but true random assignment, like the real AP exam. `render_opener_v2.randomize_answers(piece)` shuffles each MCQ's options at render time and recomputes the answer letter; call it ONCE per piece before building both the teacher and student copies so their option order matches. The author marks the single correct option by content; the renderer places it randomly. Two questions landing on the same letter by chance is fine, not a flaw. Rationales must reference distractors by content, never by letter, or the shuffle breaks them.

WRITING PROMPT (FRQ) SELECTION (Samuel, 2026-06-06): each opener also has one writing prompt tied to an AP free-response type. AP Lang has 3: Q1 synthesis (needs 6-7 provided sources, does NOT fit a single-passage opener), Q2 rhetorical analysis (fits any opener), Q3 argument (fits only passages that advance a contestable claim). Choose the type that FITS the passage; do not default everything to Q2 and do not force a rotation. Argument-driven registers (Reckoning, Long Think, Ledger, Open Letter) support Q2 and Q3 (rotate them); observational/consecratory ones (Long Look, Tribute) usually only Q2. Same principle as the answer-key fix: vary by fit, never by pattern. The first sample batch defaulted all three new openers to Q2, which is the FRQ version of the all-A bug.

The production prompt [[caughtupai-sampleprompt-V1]] now loads this spec. Built 2026-06-06 via a 20-agent workflow that verified the exam facts against the primary CED PDF (and caught a "52 questions" hallucination; the real figure is 45). Relates to [[feedback_device_vocabulary]] and [[project_caught_up_ai]].
