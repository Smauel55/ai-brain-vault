---
created: 2026-06-10
updated: 2026-06-10
tags: [project, caught-up-ai, generation, headnote, rhetorical-situation, ap-alignment]
project: "[[Caught Up AI]]"
---

# Headnote Spec (D10)

Every Opener carries a one-or-two-sentence **headnote**: a short italic line, set above the piece on both the teacher and student copies, that names the rhetorical situation before the student reads a word of the prose.

## Why this exists

From the first teacher meeting (2026-06-08, Samuel's own AP Lang teacher): the prose quality was strong, but the pieces read as impersonal. His point: a large part of AP Lang is reading for the author's point of view, audience, and purpose, and the underlying tone that those reveal. He cited a Dwight Eisenhower letter to the Allied forces, which he loved precisely because it opened a window onto how Eisenhower saw and addressed his troops. His fix: a short context blurb before each piece telling the reader who is speaking, to whom, and to what end.

Two things make this the right move, not just a nice-to-have:

1. **It is the real exam format.** Every passage on the AP English Language exam opens with a one-sentence italic headnote that supplies speaker, occasion, and audience (for example: *"The following is a letter written by Dwight D. Eisenhower to the Allied Expeditionary Force on June 5, 1944."*). Adopting it makes our stimulus look like the test our customers teach to.
2. **It primes rhetorical reading.** Speaker / audience / purpose (SOAPSTone, the rhetorical triangle) is the analytic frame the whole course runs on. Naming the situation up front is standard AP pedagogy.

What the headnote does **not** do: it does not fix impersonal prose. That is a generation problem governed by [[Register-Specs]] and [[Anti-Tell-List]] (see the [[Proxy-Pilot-Run-2]] diagnosis: too clean, too symmetric, no idiosyncratic point of view). The headnote earns its place only if it is written **first** and the piece is then drafted to earn the situation it names. Bolted on after, it is a caption that masks the symptom. See "Write it first" below.

## Form rules

- **Length:** one sentence, two at most. The moment it becomes a paragraph of invented biography, it has failed.
- **Voice:** the neutral, descriptive third-person voice of an exam headnote, not the voice of the piece. The headnote is the test-writer talking about the piece, never the piece's narrator talking. No first person. No "I", no "we".
- **Placement:** italic, directly above the piece, on **both** copies (it is part of the student's stimulus; they need the situation to do the analysis).
- **Tense:** "The following is..." / "In the following..." present-frame openings, as on the exam.
- **It names the rhetorical situation:** speaker or speaking role, audience, and occasion or purpose. Draw these from the register's **Stance / Audience / Occasion** in [[Register-Specs]], instantiated for the specific piece.
- **It does not give away the analysis.** Do not name the rhetorical devices, state the thesis, or tell the reader what to think or feel. No evaluative adjectives ("this powerful essay", "a moving tribute"). Describe the situation; let the student find the moves.
- **Inherits the hard bans:** no em-dashes, no emojis (use a comma, colon, or semicolon for any turn).

## The two honesty rules (judgment calls, decided 2026-06-10)

These bound how far the headnote may go, and protect the integrity of the exercise.

1. **Never fabricate a named real person or a false specific identity.** For an invented-persona piece, frame the situation by **role and scenario**, exactly as the AP exam frames a fiction excerpt ("In the following passage, the narrator..."). Write "an open letter from a small-town independent pharmacist to the head of a national drug-benefit manager," never "a letter from Jane Doe, a pharmacist in Akron." A constructed scenario described by role is legitimate analytic material; a counterfeit named human asserting real claims is not. For pieces built on **real** subjects (a real person honored in a Tribute, real events in a Ledger or Long Look), name the real entities truthfully, as the exam does with Eisenhower.
2. **The headnote does not announce AI authorship.** Whether and how to disclose that the pieces are AI-written is a teacher-level and product-level matter (the open-about-AI disclosure made to the teacher), not part of the stimulus. Inside the headnote the student analyzes the rhetorical situation as presented, the same way they analyze a constructed AP synthesis scenario or a novel's narrator without being told "this person is fictional."

## Neutrality (inherits [[Editorial-Standards]] Gate 0)

The headnote is held to the same neutrality firewall as the piece. The named speaker, addressee, or subject may not be a sitting or identifiable political officeholder, a candidate, or a partisan body, and the headnote may not take a side. Because the Open Letter addressee and the Reckoning culprit are already constrained to non-partisan targets, the headnote inherits that constraint automatically. A real official may appear as a neutral actor in a Ledger headnote ("following the agency's announcement of the rule"); a stance toward them may not.

## Register-aware content

The headnote names the situation each register actually has. The persona registers get a speaker/audience/purpose line; the impersonal registers get an occasion/context line, because forcing a fake speaker onto a neutral explainer reads as exactly the kind of manufactured thing that tips a reader off.

| Register | Headnote names | Speaker framing |
|---|---|---|
| **The Ledger** | The occasion and the question at issue; the documented matter being laid out. No speaker persona. | Occasion/context line, no "speaker." E.g. *"The following lays out what the May jobs report does and does not show, and where the two parties disagree."* |
| **The Long Look** | The phenomenon or system being examined and why it rewards a close look. No speaker persona. | Occasion/context line. E.g. *"The following examines how a tsunami warning travels from the seafloor to a coastal siren in the minutes after a quake."* |
| **The Long Think** | The durable theme being reconsidered and the writer's analytic purpose. Speaker = an essayist reasoning, no biography. | Theme + purpose. E.g. *"The following is a reflective essay on the disappearance of waiting from everyday life... the writer first grants the gains, then asks what was lost."* |
| **The Tribute** | The real subject honored, the occasion (a death, an anniversary), and the consecratory purpose. | Real named subject (truthful). E.g. *"The following is a tribute to [real person], the [role] who died on [date], reflecting on what their work changed."* |
| **The Reckoning** | The real, datable trigger; the non-partisan party held responsible; a public moral address. | Public address + real occasion + non-partisan responsible party. Names the real institution/practice, never a politician or party. |
| **The Open Letter** | The speaking role, the non-partisan more-powerful addressee, and the precipitating event. | Role + non-partisan addressee (scenario, not a fake name). E.g. *"In the following open letter, a [role] writes to [a company / an industry / a standards body] after [event]."* |
| **The Witness Stand** | The shared experience the first-person voice speaks from, and the occasion licensing the intimacy. | First-person speaking role by scenario, never a fabricated named person. E.g. *"In the following piece, a [hospice nurse / first-generation student] reflects on [experience], occasioned by [real news]."* |

When the speaker, addressee, or subject is invented, the framing is the **role**, not a name. When it is real, name it truthfully.

## Write it first (the forcing function)

The headnote is a **generation input**, not a post-hoc label. Per [[Generation-Briefs]], it is written **before** the prose, as the second slot the drafter fills (after the template/open/close), and the piece is then drafted to earn exactly that speaker, audience, and purpose. Writing it first does real work: it forces the piece to commit to a particular point of view instead of defaulting to the frictionless smart-explainer voice that reads as AI. A piece whose finished prose does not match its own headnote has drifted, and goes back.

## AP-exam style guide (imitate these)

Real AP English Language headnote and prompt patterns to model the cadence on:

- *"The following is a letter written by Dwight D. Eisenhower to the Allied Expeditionary Force on June 5, 1944."*
- *"The passage below is an excerpt from a 2009 nonfiction book about the cultural history of the American lawn."*
- *"In the following passage from her memoir, the writer reflects on her relationship with her father."*
- *"On April 10, 1962, after several major steel companies raised prices, President John F. Kennedy responded at a news conference. The following is an excerpt from his remarks."* (occasion-then-text, the longer two-clause shape)

Common shape: **[form] + [speaker or subject] + [occasion / date] + [audience or purpose]**, in one calm declarative. Keep ours to that.

Banned moves (these break the exam-headnote register):
- Evaluative or hyping adjectives ("powerful", "moving", "searing", "important").
- Naming the devices or the thesis, or otherwise pre-chewing the analysis.
- Second person or any address to the student ("As you read, notice...").
- The piece's own narrating voice leaking into the frame.
- An em-dash or emoji.

## Render

- Field name: `headnote` (string), one or two sentences, on the piece dict consumed by `render_opener_v2.py`.
- Rendered in italic (`Times-Italic`, the `hnote` style) directly above the article on both the Teacher and Student copies.
- The field is **optional** in the renderer for backward compatibility: pieces generated before this field existed still render. Every newly generated piece must include it.
- The Google Docs export paths (`render_opener_html.py`, `render_opener_docx.py`) need the same field added if Openers are delivered via Google Docs; the PDF path (`render_opener_v2.py` / `render_batch.py`) is the primary one and is done.

## Related

- [[Generation-Briefs]] - the headnote is written first, before the prose, and is checked at pre-flight.
- [[Register-Specs]] - the Stance / Audience / Occasion each headnote draws on.
- [[Editorial-Standards]] - the neutrality firewall (Gate 0) the headnote inherits.
- [[Style-Palette]] - register routing.
- [[caughtupai-sampleprompt-V1]] - the sample-generator prompt; its output now includes the headnote.
- [[Caught Up AI]] - project root.
