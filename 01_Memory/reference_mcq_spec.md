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

The production prompt [[caughtupai-sampleprompt-V1]] now loads this spec. Built 2026-06-06 via a 20-agent workflow that verified the exam facts against the primary CED PDF (and caught a "52 questions" hallucination; the real figure is 45). Relates to [[feedback_device_vocabulary]] and [[project_caught_up_ai]].
