---
created: 2026-06-11
updated: 2026-06-11
tags: [project, caught-up-ai, generation, prompts]
project: "[[Caught Up AI]]"
---

# Caught Up AI Quick-Opener Prompt (V1)

On-demand companion to [[caughtupai-sampleprompt-V1]]. That one is for batch sample
runs (set N, Variety Matrix, batch audit). This one is for building an Opener on a
whim: paste it into a Claude Code session launched from this vault, optionally fill
the inputs, and get a finished Opener with teacher and student PDFs.

How it differs from the batch prompt:
- Defaults to ONE Opener; you can name a topic, a register, both, or neither.
- Leave every input blank and it still works: Claude picks a real story from the
  last 5 days and routes the register by Style-Palette.
- The batch-sameness gate is replaced by a recency check against the most recent
  rendered editions, so back-to-back whims do not come out as twins.
- Renders the real PDFs by default through render_opener_v2.py (teacher copy with
  highlights, answer key, misconceptions; student copy clean).
- Bakes in model routing: the drafting (step 3) and Gate 0 editorial judgment stay
  on the strongest model (Fable 5), because AI-sameness and the neutrality calls are
  what the human AP-Lang panel and the teacher customer judge. Fact verification
  (step 1) and PDF rendering (step 6) are tagged offloadable to a cheaper subagent.

Related: [[Generation-Briefs]], [[Editorial-Standards]], [[Headnote-Spec]],
[[MCQ-Construction-Spec]], [[Rhetorical-Device-Vocabulary]], [[Accuracy-Guardrail]].

---

## The prompt

```
Act as the Caught Up AI production system and build me a finished Opener right now.

MY INPUTS (any of these may be blank; blank means you decide):
- TOPIC: ___        (a specific story, a subject area like "science" or "sports", or
                     blank = pick a real story from the last 5 days that makes a
                     strong rhetorical teaching text)
- REGISTER: ___     (one of the 7 palette voices, or blank = route by Style-Palette)
- COUNT: ___        (blank = 1)
- OUTPUT: ___       (blank = PDFs; "package" = text in chat only)

LOAD THE ENGINE FIRST. Read these files in "10_Projects/Caught Up AI/" and treat
them as binding: Generation-Briefs.md, Style-Palette.md, Register-Specs.md,
Structural-Templates.md, Anti-Tell-List.md, Accuracy-Guardrail.md,
Editorial-Standards.md, MCQ-Construction-Spec.md, Rhetorical-Device-Vocabulary.md,
Headnote-Spec.md. Where this prompt is silent, those files govern.

HARD RULES: no em-dashes anywhere, no emojis anywhere, no in-text citations of any
kind in the piece. Gate 0 from Editorial-Standards.md binds in full: the neutrality
firewall (neutral-explainer everywhere; pointed persona advocacy allowed only on the
civic tier, aimed at the issue or institution, never a person or group, and never a
side on the national third rails) and the plain-knowledge rule (every unexplained
term must be common knowledge to a typical high schooler; gloss or cut anything
else).

MODEL ROUTING. Run this session on the strongest available model (Fable 5). The two
load-bearing parts are the drafting in step 3 and the editorial judgment in Gate 0
(neutrality calls + the friction/anti-symmetry that keeps the prose from reading as
AI). AI-sameness and the neutrality calls are exactly what the human AP-Lang panel
and the teacher customer judge, and they reward model capability most, so KEEP THOSE
ON THE STRONGEST MODEL, always. The fact verification in step 1 and the PDF rendering
in step 6 are process discipline and deterministic code; to save cost you MAY
delegate them to a cheaper subagent (e.g. Haiku) via the Agent tool. Never delegate
the drafting, the anti-tell/register judgment, or the Gate 0 editorial calls.

BUILD STEPS, in order:
1. [offloadable to a cheaper subagent] Pick the story (or take my TOPIC).
   Web-search and build a numbered, verified fact list per Accuracy-Guardrail before
   drafting. Every name, number, date, quote, and causal claim confirmed against a
   real source; unverifiable facts get dropped, unverifiable stories get swapped.
   Invented personas are fine; framed by role, never a fabricated proper name. Hard
   facts must be real. (If delegated, the subagent returns only the verified fact
   list; the drafting stays on the strongest model.)
2. Route the register (or take mine), then check the most recent rendered editions
   in "10_Projects/Caught Up AI/Sample-Briefs/" and pick a register, template,
   opener type, and close type that do not repeat the latest one. If COUNT is more
   than 1, no two pieces in this run may share any of those either.
3. [KEEP ON STRONGEST MODEL] Write the headnote FIRST per Headnote-Spec.md (one or
   two italic sentences, neutral AP-exam voice, naming speaker role, audience,
   occasion). Then draft the 350 to 600 word piece to earn exactly that situation,
   from the fact list only, with sources closed.
4. [KEEP ON STRONGEST MODEL] Run the pre-flight gates from Generation-Briefs.md
   (editorial fit, accuracy and expression firewall, register band, anti-tell scan).
   Fix and re-run until clean. Do not show me the gate work.
5. Build the apparatus: device tags only from Rhetorical-Device-Vocabulary.md and
   only where genuinely present (3 to 6, with quoted phrase and purpose); 2 MCQs to
   MCQ-Construction-Spec.md targeting different AP reading skills, answer keys
   randomized; 2 discussion questions with sample responses; 1 AP Q3-style writing
   prompt; misconceptions; AP alignment note.
6. [offloadable to a cheaper subagent] If OUTPUT is PDFs: do not modify
   render_opener_v2.py. Write a small one-off driver in Sample-Briefs/ that imports
   build() and randomize_answers() from render_opener_v2 and passes the new piece
   dict, then run it and confirm the teacher and student PDFs were written. Tell me
   the two file names.

SHOW ME, per piece: subject line, headline, register and focus, the headnote, the
full piece, the devices with explanations, the MCQs with answer key and rationales,
the discussion questions, and the writing prompt. Then one sentence on which
register, template, opener, and close you used and why it differs from the previous
edition.
```
