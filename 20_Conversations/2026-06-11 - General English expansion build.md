---
created: 2026-06-11
updated: 2026-06-11
tags: [conversation, caught-up-ai, product, general-english, customization, base44]
project: "[[Caught Up AI]]"
---

# 2026-06-11 — General English expansion build

## Context

Teacher-feedback item #3 (the system works for non-AP English teachers too) was a
direction-decided fast-follow. Samuel asked to build it now and add it to the Base44
customization (/manage) page. Brought forward and built same day.

## Built (content side, in the vault)

- New spec [[General-English-Mode-Spec]] (D11): the `audience` dimension (`ap_lang` default
  | `general_english`), the label map, the AP reading-skill -> general/Common Core mapping,
  the dual-write requirement, and what does NOT change (all student pedagogical content).
- `Sample-Briefs/render_opener_v2.py` parameterized with an `audience` field. It swaps four
  things on the teacher copy + masthead only: masthead tagline ("The daily AP English
  Language Opener" -> "The daily English Language Opener"), MCQ header ("AP-style multiple
  choice:" -> "Close-reading multiple choice:"), writing-type label (Q1/Q2/Q3 -> plain
  names via `gen_type`/`ap_to_gen`), and the alignment section ("AP exam alignment:" ->
  "Reading and analysis skills:", body from `gen_alignment`). Default `ap_lang`, so old
  pieces render unchanged.
- Dual-write wired into [[caughtupai-sampleprompt-V1]] (read-list + a SKILL ALIGNMENT
  output block asking for both `ap_alignment`/`gen_alignment` and `type`/`gen_type`) and
  [[MCQ-Construction-Spec]] (a General-English framing table mapping the 4 AP reading
  skills + 3 FRQ types to Common Core).
- VERIFIED: rendered the same Long Think piece both ways and extracted text. AP copy shows
  "AP English / AP-style / AP exam alignment / Q3 argument"; general copy shows "English
  Language / Close-reading / Reading and analysis skills / argument essay". Pedagogical
  content (passage, devices, MCQs, discussion, prompt text) byte-identical.

## Design note (student copy)

"Student Opener identical" = identical LEARNING content. The masthead tagline, MCQ header,
and writing-type label DO swap on the student copy too, so a general-English handout never
says "AP-style" or "Q3." Flagged to Samuel; reversible if he wants byte-identical student
copies.

## Built (page side, Base44, PREVIEW only)

Drove the Base44 editor (Chrome) and instructed the in-app builder to add `audience` the
same secure way as delivery_days/political_content. Result, all code-verified in preview:

- Teacher entity: `audience` field (string, ap_lang|general_english, default ap_lang). Lock
  UNCHANGED and confirmed in the Permissions panel: `{create:false, read:false,
  update:false, delete:false}`. (The "Permissions issues detected" banner is the same known
  false-positive from the security work; the true anonymous probe returns [].)
- `getTeacherByToken`: returns `audience` (prefill defaults missing -> ap_lang).
- `updateTeacherByToken`: validates audience in {ap_lang, general_english} (400 otherwise),
  persists via `base44.asServiceRole` through the locked entity.
- /manage page: a prefilled "Course" radio group ("AP English Language" / "General English
  (non-AP)") styled like the political dial, included in the Save payload, with helper text
  "This sets how your teacher notes are labeled. Your students' handout is the same either
  way."

## Open / next

- HARD GATE: Samuel clicks **Publish** in the Base44 editor (publishing to the live domain
  is correctly his call, not Claude's). Then live re-verify: (a) anonymous probe to the
  Teacher entities endpoint still returns 0/`[]` (lock held through the schema change);
  (b) /manage prefills the Course selector and saving the audience persists across reload.
- Wire `audience` into the render pipeline per teacher when the real send flow exists (the
  broadcast edition rendered with each teacher's audience flag).
- Reading-level fit with a general-English teacher still to confirm before marketing the
  expansion (Teacher-Feedback-Tracker open action). AP Lang stays the launch wedge.
- Marketing/signup copy (audience choice at signup) not built here; tracked separately.
