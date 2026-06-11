---
created: 2026-06-06
updated: 2026-06-06
tags: [project, caught-up-ai, mcq, assessment, ap-lang]
project: "[[Caught Up AI]]"
---

# MCQ Construction Spec (AP Lang reading questions)

Working checklist for writing the two reading-style multiple-choice questions in each
Caught Up AI Opener, at genuine AP English Language standard. Grounded in the official
College Board AP English Language and Composition Course and Exam Description (CED, 2024):
the released Section I reading sample items (Questions 1 to 7) and the skill-alignment
table. Built 2026-06-06 to lift question quality after early drafts shipped distractors a
student could discard on sight (the fix is craft, not more research).

Two house rules override everything below: no em-dashes, no emojis.

## What an AP reading MCQ is (grounded)

- The exam presents a nonfiction passage and asks students to read and analyze it (Section I has 23 to 25 reading questions per form).
- Many items localize the task to a paragraph or a quoted span, then ask for the function, claim, reasoning, relationship, effect, position, or tone of that unit relative to the whole; others ask about the passage overall.
- Options are four choices, (A) through (D); exactly one is the defensibly best answer, signaled by stems like "best describes," "best characterizes," or "primarily to."
- Function and purpose stems ending in "primarily to" or "in order to" take options that are parallel verb completions (illustrate, emphasize, suggest), so the four read as grammatically parallel phrases sharing the stem's "to."
- Distractors are plausible and partly true: they name a real move in the passage but overstate it, target the wrong span, or name a purpose the text does not primarily serve.

## The four reading skills (rotate across the two questions)

Numbering note: AP labels these four reading skills as CED Skill Categories 1, 3, 5, 7
(the odd numbers; the even numbers are the writing skills). They map one to one with the
four Big Ideas below. Do not read "Skill Category 3" as "Big Idea 3"; Skill Category 3 is
Claims and Evidence.

| Big Idea (Skill Cat.) | What it tests | Example stem |
|---|---|---|
| 1. Rhetorical Situation (SC 1) | how choices reflect writer, audience, purpose, context, exigence | "Which of the following best describes the writer's exigence in the opener?" |
| 2. Claims and Evidence (SC 3) | the claims and the evidence of the argument | "In the third paragraph, which best characterizes the writer's position on X?" |
| 3. Reasoning and Organization (SC 5) | line of reasoning, development, integration of evidence, relationships between parts | "In the second paragraph, the writer introduces a hypothetical primarily to ___ (four verb options)." |
| 4. Style (SC 7) | how diction, syntax, figurative language, and tone serve purpose | "In context, the quoted phrase best supports which claim about the writer's tone?" |

## Stem patterns worth rotating

- Which best describes the writer's exigence / purpose / intended audience in the opener? (Rhetorical Situation; four parallel clauses)
- In the [first / final] paragraph, the writer contrasts [A] with [B] primarily to ___ (Claims and Evidence; four verb completions)
- In the [Nth] paragraph, which best characterizes the writer's position on [subject]? (Claims and Evidence; four matched clauses)
- In the [Nth] paragraph, the writer introduces a hypothetical / anecdote / example primarily to ___ (Reasoning and Organization; four verb completions)
- The relationship between the [Nth] and [Mth] paragraphs is best described as one in which the writer first ___ and then ___ (Reasoning and Organization; paired parallel verbs)
- The writer's use of [the simile / anecdote / parallelism / shift in diction] serves primarily to ___ (Style; four verb completions)
- In context, the quoted phrase best supports which of the following claims about the writer's tone? (Style; four parallel tone descriptors)

## Answer-verb bank (for "primarily to" / "serves to" function stems)

illustrate, explain, emphasize, suggest, question, underscore, highlight, provide, offer,
assert, imply, qualify, concede, anticipate, rebut, reinforce, characterize, dramatize,
undercut, reconcile, establish, convey, clarify, contrast, critique, acknowledge,
downplay, foreshadow, reframe, temper. Options complete the stem's "to," so they stay
parallel verb phrases.

## How a distractor should fail (the only legitimate traps)

Every wrong option must fail by one of these. If a wrong option is none of these, it is
probably a free elimination and must be rewritten.

| Trap | How it fails | Mini example |
|---|---|---|
| Right device, wrong effect | names a move that is present, but assigns a purpose the text does not primarily serve | calls the anecdote a bid to amuse when it grounds the claim in lived stakes |
| Right effect, wrong location | states a true purpose, but ties it to a different span than the stem cites | describes the closing appeal's job when the stem asked about the opening |
| True but not the function asked | an accurate observation that does not answer the function or position requested | notes the writer cites a statistic when the stem asks what the contrast accomplishes |
| Too literal | reads a figurative phrase at face value, missing the meaning in context | treats a metaphorical "wall" as an actual barrier rather than resistance to change |
| Over-broad or extreme | absolute wording (always, proves, entirely) or a claim larger than the text supports | says the writer condemns all reformers when she faults one group's reasoning |
| Inverted relationship | reverses the stance or swaps which side holds the position, while sounding on-topic | says the writer endorses the view she is actually criticizing |
| Out-of-passage import | brings in outside knowledge the passage never states, however reasonable | cites a historical fact the opener itself does not raise |

## The one-best-answer gate

- Write the keyed answer first, then test each distractor: if a second option is also fully defensible against the exact stem, tighten the stem or revise the distractor until only one survives.
- The key must be the strongest reading, not the only conceivable one, and it must answer precisely what the stem asks (function vs claim vs tone vs relationship), not an adjacent question.
- Every distractor must be plausible and anchored to something real in the passage. Ban any option a prepared student discards on sight.
- No free elimination by form: keep all four parallel in grammar, comparable in length and specificity, with no conspicuously longer or more hedged giveaway.
- Each distractor should fail by a named trap above, not by being empty filler.

## Self-check (run on every question before it ships)

1. Does the stem cite a specific unit (a paragraph and, where useful, a quoted phrase) so the task span is unambiguous?
2. Is there exactly one defensibly best answer, with no second option equally defensible against this stem?
3. Do all four options share parallel grammatical form (verb completions for "primarily to" stems; matched clauses for claim, reasoning, or tone stems)?
4. Are the four options comparable in length and specificity, with no giveaway by length or hedging?
5. Is each distractor plausible and traceable to a real move in the passage, with no on-sight throwaway?
6. Does each distractor fail by a named trap rather than by being irrelevant filler?
7. Does the keyed answer match the skill the stem targets, not an adjacent skill?
8. Is the answer verifiable from the opener text alone, with no outside knowledge required?
9. For a function stem, do all four choices read as parallel verb completions of the stem?
10. Zero em-dashes and zero emojis in stem and options?
11. Is the correct option marked by content rather than hand-placed at a fixed letter? Option order is randomized at render time, so do not pattern the keys; an occasional repeated letter by chance is expected and fine.

## Do not

- Do not let the two questions in one opener test the same skill; pair a reading skill with a different one (for example one Reasoning, one Style).
- Do not include a throwaway distractor a student eliminates on sight; all four must be plausible.
- Do not mix grammatical forms within one item's options (some verbs, some clauses).
- Do not write a giveaway that is conspicuously longer, more hedged, or more detailed than the others.
- Do not use absolute wording (always, never, proves, entirely) in the key unless the text genuinely supports it.
- Do not require outside knowledge or import facts the opener does not state.
- Do not reuse the same stem shape for both questions; rotate the patterns.
- Do not key an answer that is true about the passage but does not answer the exact function, position, or tone the stem asks for.
- Do not pattern the keyed letter, neither all-A nor a forced even A/B/C/D rotation. The renderer (render_opener_v2.randomize_answers) shuffles each question's options at render time so the key lands on a random letter, exactly as on the real AP exam; two questions sharing a letter by chance is fine and is not a design flaw. Author each question by marking the single correct option; never hand-place it at a chosen letter. (Early samples keyed every question to A, the giveaway this fixes.)

## Scale for a two-question opener

Each opener carries exactly two reading MCQs, so make them count and make them differ.
Reference the passage by paragraph and short quoted phrase, never by line number (openers
are not line-numbered). Target two different reading skills (for example one Reasoning or
Claims item and one Style tone or diction item) so the pair samples the passage broadly.
Keep each to a four-option set with parallel grammar and comparable length, exactly one
defensibly best answer, and distractors that are partly true but fail by a named trap.
A student should be able to answer each from the opener alone in under a minute.

## Writing prompt (FRQ) selection

Each opener also carries one writing prompt tied to an AP free-response type. AP English Language has three FRQs:

- Q1 synthesis: requires 6 to 7 provided sources and an argument that cites them. It does NOT fit a single-passage opener unless an edition is deliberately built with multiple sources.
- Q2 rhetorical analysis: analyze the rhetorical choices the writer makes in the passage. Fits any marked opener, since every opener is a passage of rhetorical choices.
- Q3 argument: defend, challenge, or qualify a debatable claim, no sources. Fits only openers whose passage advances a contestable position; a Q3 prompt generalizes the passage's theme into a debatable proposition.

Rules:
- Choose the type that genuinely FITS the passage. Do not default every opener to Q2, and do not force a rotation. Fit always beats forced variety (the same principle as the answer-key fix: vary by fit, never by pattern).
- Argument-driven registers (The Reckoning, The Long Think, The Ledger, The Open Letter) support both Q2 and Q3; rotate them across a batch. Observational or consecratory registers (The Long Look, The Tribute) usually support only Q2, because there is no contestable claim to argue.
- Across a batch, vary the FRQ type wherever the passages allow, the way registers are varied, but never staple a Q3 argument onto a piece that argues nothing.

## General-English framing (audience = general_english)

The same two MCQs and the same writing prompt ship to non-AP English teachers unchanged;
only the skill LABELS are renamed (see [[General-English-Mode-Spec]]). The four AP reading
skills and the three FRQ types map one-to-one onto general reading/analysis (Common Core)
labels:

| AP reading skill | General-English label | Common Core (RI/L) |
|---|---|---|
| Rhetorical Situation (SC 1) | Author's purpose, audience, point of view | RI.6 |
| Claims and Evidence (SC 3) | Central idea and supporting evidence | RI.1, RI.2, RI.8 |
| Reasoning and Organization (SC 5) | Text structure and how ideas develop | RI.3, RI.5 |
| Style (SC 7) | Word choice, tone, figurative language | RI.4, L.5 |

| AP FRQ | General label | Common Core (W) |
|---|---|---|
| Q1 synthesis | synthesis essay | W.7, W.8, W.9 |
| Q2 rhetorical analysis | rhetorical analysis | W.2, W.9 |
| Q3 argument | argument essay | W.1 |

Build the questions to the AP standard above; the general-English version is a relabel,
not a different question. The renderer swaps the section headers automatically; the
generator supplies the `gen_alignment` / `gen_type` text per [[General-English-Mode-Spec]].

## Sourcing and confidence

- Grounded against the official CED (2024) reading samples Q1 to Q7 and the skill-alignment table (Skills 1.A, 3.A, 7.A, 5.A, 5.C, 7.B). Exam structure: Section I = 45 multiple choice in 60 minutes (45% of score), 23 to 25 reading plus 20 to 22 writing questions across 5 passage sets.
- An automated summary of the CED initially returned "52 questions"; that is false and was corrected against the primary PDF. The exam has 45 MCQ, and the reading/writing split is published only as ranges (23 to 25 and 20 to 22), so do not cite a single fixed number for either type.

## Related

- [[Rhetorical-Device-Vocabulary]] - the controlled device list the questions may name.
- [[Generation-Briefs]] - the drafting layer the opener prose comes from.
- [[caughtupai-sampleprompt-V1]] - the production prompt that should load this spec.
- [[Caught Up AI]] - project root.
