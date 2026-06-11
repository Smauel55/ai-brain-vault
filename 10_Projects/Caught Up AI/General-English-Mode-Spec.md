---
created: 2026-06-11
updated: 2026-06-11
tags: [project, caught-up-ai, product, customization, general-english, spec]
project: "[[Caught Up AI]]"
---

# General-English Mode Spec (D11)

How the **audience** customization dimension works: one daily Opener, framed for either
an **AP English Language** teacher or a **general (non-AP) English** teacher. Built from
teacher feedback item #3 (see [[Teacher-Feedback-Tracker]]): the system works for regular
English teachers too; only the AP-Lang labels need to change.

Origin decision (2026-06-11): keep **AP Lang as the launch wedge**; general English is a
fast-follow, shipped as one more low-cardinality customization axis alongside the
political dial and delivery frequency. No second content pipeline.

Two house rules carry over: no em-dashes, no emojis.

## The core rule: same Opener, different frame

The daily edition is produced **once**. The audience flag never changes which passage,
which devices, which questions, or which writing prompt a teacher receives. It changes
only the **labels** that name the skills, so an AP teacher sees AP-exam framing and a
general-English teacher sees plain reading/analysis (Common Core) framing.

| Part of the Opener | Changes with audience? |
|---|---|
| The passage (article + headnote) | No. Identical. |
| Rhetorical-device marking + "Devices, and why" | No. Identical (these are general reading-analysis skills, not AP-only). |
| The two reading MCQs (stems, options, key, rationale) | No. Identical. |
| Discussion questions + sample responses | No. Identical. |
| Writing-prompt **text** | No. Identical. |
| Masthead tagline | **Yes** (branding). |
| MCQ section **header** | **Yes** (label only). |
| Writing-prompt **type label** | **Yes** (Q1/Q2/Q3 -> plain name). |
| Skill-alignment section (header + body) | **Yes** (AP-exam framing -> reading/analysis framing). |

So a school running both AP and general English gets the **same student learning** from
the same edition; the only differences are cosmetic labels on the page. (This is why the
student copy is not byte-identical across audiences: a general-English handout must not
say "AP-style" or "Q3." If a truly identical student copy is ever wanted, drop the
audience-aware labels from the student build only.)

## The label map (implemented in render_opener_v2.py)

`AUDIENCE` dict keyed by the piece's `audience` field (`ap_lang` default | `general_english`):

| Slot | `ap_lang` | `general_english` |
|---|---|---|
| `tagline` (masthead) | The daily AP English Language Opener | The daily English Language Opener |
| `mcq_header` | AP-style multiple choice: | Close-reading multiple choice: |
| `alignment_header` | AP exam alignment: | Reading and analysis skills: |

Unknown/missing `audience` falls back to `ap_lang`, so every piece authored before this
field existed renders exactly as before.

## AP reading skills -> general English / Common Core

The four AP reading skills ([[MCQ-Construction-Spec]]) map one-to-one onto general
reading-analysis skills. Same question, different name. Use this table when writing the
`gen_alignment` body and when describing the product to general-English teachers.

| AP skill (CED Skill Cat.) | General-English framing | Common Core (Reading: Informational) |
|---|---|---|
| Rhetorical Situation (SC 1) | Author's purpose, audience, and point of view | RI.6 |
| Claims and Evidence (SC 3) | Central idea and supporting evidence | RI.1, RI.2, RI.8 |
| Reasoning and Organization (SC 5) | Text structure and how ideas develop | RI.3, RI.5 |
| Style (SC 7) | Word choice, tone, and figurative language | RI.4, L.5 |

Writing-prompt types (AP free-response -> general):

| AP FRQ | General-English label | Common Core (Writing) |
|---|---|---|
| Q1 synthesis | synthesis essay | W.7, W.8, W.9 |
| Q2 rhetorical analysis | rhetorical analysis | W.2, W.9 |
| Q3 argument | argument essay | W.1 |

## What the generator must supply (dual-write)

To get clean general-English output (not a Q-label strip), each piece carries an
audience-neutral companion to the two AP-framed teacher fields:

- `gen_alignment` (string): the same analytical value as `ap_alignment`, written in
  reading/analysis terms with **no AP exam labels** (no "Q2," no "rhetorical-analysis
  value"). End with a short parenthetical Common Core tag, e.g. `(Common Core: RI.4, RI.5, W.2.)`
- `writing.gen_type` (string): the plain writing-task name, e.g. `argument essay`,
  parallel to the AP `writing.type` (`Q3 argument`).

**Fallback:** if `gen_alignment` or `gen_type` is absent, the renderer strips the
Q1/Q2/Q3 labels from the AP text (`ap_to_gen`). This keeps old pieces from breaking, but
the AP sentence structure ("a compact text for teaching...") still reads AP-ish, so the
authored `gen_*` fields are preferred for anything shipped to a general-English teacher.

Everything else (masthead, MCQ header, alignment header, the Q-label on the writing line)
is swapped automatically by the renderer from the `audience` flag. The generator does not
write those.

## Where audience comes from (page integration)

`audience` is a per-teacher setting, like the political dial and delivery days:

- Set at **signup** (the teacher identifies as AP Lang or general English).
- Stored on the **Base44 Teacher entity** as a field (`audience`, default `ap_lang`).
- Changeable on the **/manage** preferences page (a two-option selector).
- Read into the render pipeline per teacher: the broadcast edition is rendered with that
  teacher's `audience` flag before send. (One edition authored; rendered per audience.
  In a manual/semi-auto MVP that is two render passes of the same JSON, not two pipelines.)

See [[2026-06-11 - General English expansion build]] for the Base44 build steps.

## Reading-level caveat (open)

Still to verify with a general-English teacher before scaling: the prose is AP-caliber in
sentence craft, fine for 11th-12th grade, possibly a stretch for 9th-grade or lower-track
classes. The neutrality and plain-knowledge gates ([[Editorial-Standards]]) already target
"a high schooler," so vocabulary is in range; the open question is sentence complexity, not
content. Do not assume "just the labels" fully holds until a general-English teacher
confirms the reading level. (Teacher-Feedback-Tracker open action.)

## Marketing framing (not built here)

The signup/marketing copy needs an audience choice too ("AP English Language" vs "any
English class"). That is a website/Base44 copy task, tracked separately; this spec covers
the product mechanics. Keep the launch message AP-Lang-first per the wedge decision; the
general-English framing is a secondary path, not the headline.

## Related

- [[MCQ-Construction-Spec]] - the four AP reading skills this maps from.
- [[Generation-Briefs]] - where `gen_alignment` / `gen_type` get authored.
- [[Headnote-Spec]] - the headnote is audience-neutral (no change).
- [[Editorial-Standards]] - neutrality + plain-knowledge gates (audience-neutral).
- [[Teacher-Feedback-Tracker]] - feedback item #3, origin of this work.
- [[Caught Up AI]] - project root.
