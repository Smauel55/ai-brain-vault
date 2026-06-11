---
created: 2026-06-05
updated: 2026-06-08
tags: [project, caught-up-ai, generation, prompts, sample-output]
project: "[[Caught Up AI]]"
---

# Caught Up AI Sample-Generator Prompt (V1)

Reusable prompt that turns the v2 prose engine into finished, inbox-ready lesson-opener
samples. Paste the block below back into a Claude Code session launched from this vault,
set the number, and the full engine runs end to end: real-news sourcing, register
routing, the Variety Matrix, the 4 pre-flight gates, and the batch-sameness pass.

What each sample contains (the inbox lesson-opener package): subject line, headline,
register tag, a one or two sentence headnote naming the rhetorical situation, the 350 to
600 word opener, rhetorical devices highlighted and explained, 2 AP-Lang-style multiple
choice questions, 2 discussion questions, and 1 rhetorical analysis prompt.

How to use:
- Set the number at the bottom and paste the whole block.
- Real-news mode is the slow part (live web search + fact verification per piece). For a
  fast prose-only check, swap the TOPIC MODE block for labeled placeholder topics with
  every invented fact tagged [PLACEHOLDER].
- The scaffolding (devices, questions, prompt) wraps the piece but never touches the
  prose, so the opener still has to pass the anti-tell gates on its own.

Related: [[Generation-Briefs]], [[Style-Palette]], [[Register-Specs]],
[[Structural-Templates]], [[Anti-Tell-List]], [[Cross-Piece-Sameness-Rubric]],
[[Accuracy-Guardrail]], [[Caught Up AI]].

---

## The prompt

```
Act as the Caught Up AI production generation system. Generate {{N}} finished daily
lesson-opener emails, each functionally identical to what an AP English Language and
Composition teacher would receive in their inbox at 6am.

BEFORE WRITING ANYTHING, load the engine. Read these files in
"10_Projects/Caught Up AI/" and treat them as binding:
- Generation-Briefs.md  (the per-register drafting briefs, the rotation/orchestration
  logic, and the 4-gate pre-flight checklist)
- Style-Palette.md  (register routing: which voice fits which story)
- Register-Specs.md  (the measurable per-register bands)
- Structural-Templates.md  (the 12 skeletons + rotation grid)
- Anti-Tell-List.md  (the per-piece banned-construction gate)
- Cross-Piece-Sameness-Rubric.md  (the batch audit + Variety Matrix)
- Accuracy-Guardrail.md  (fact-sourcing + the expression firewall)
- Editorial-Standards.md  (the neutrality firewall + plain-knowledge accessibility, Gate 0)
- MCQ-Construction-Spec.md  (AP-grounded rules for the two multiple-choice questions: skill spread, stem patterns, distractor traps, the one-best-answer gate, the self-check)
- Rhetorical-Device-Vocabulary.md  (the controlled device list for labeling, plus the single-color highlight and per-device purpose convention)
- Headnote-Spec.md  (the one-or-two-sentence AP-exam-style rhetorical-situation line that opens every piece on both copies; written FIRST, before the prose, as a forcing function)

HARD RULES override everything below: no em-dashes anywhere, no emojis anywhere. And
two editorial gates from Editorial-Standards.md bind every piece (Gate 0): (a) NEUTRALITY
FIREWALL (two modes, REVISED 2026-06-11): NEUTRAL-EXPLAINER mode (every tier; the only
mode on the non-civic tier) takes no side. POINTED-ADVOCACY mode (CIVIC tier only) MAY argue
a position with full force IF it presents a clear rhetorical situation (per Headnote-Spec)
and aims that force at the issue or institution, never a person. VARY THE FORM across the
batch (do not make every pointed piece a named individual testifying to a group, that
sameness is a tell): op-ed/signed column, unsigned editorial in the paper's voice,
first-person essay, open letter to a body, witness account, guest commentary. Speaker framed
by role/relationship, never an invented proper name or a real person; emotion welcome where
the form supports it.
Three hard bans in BOTH modes, EVERY tier: no attack on a specific person (no living
political figure as addressee, villain, or hero; an unnamed "Mr. President" still counts; a
real official may appear only as a neutral sourced actor); no attack on a group (party,
religion, nationality, ideology, demographic); NO SIDE on the national third rails (abortion,
guns, partisan elections/candidates, contested-value immigration like whether birthright
citizenship should exist) which stay neutral-explainer even on the civic tier. Test for what
advocacy unlocks: value-consensus (means/competence/local-impact disputes = advocate;
contested-value disputes = stay neutral). (b) PLAIN-KNOWLEDGE: every
unexplained term must be common knowledge to a typical high schooler; define any specialist
term (program sub-parts like "Part D", procedural rules, financial metrics, acronyms) in a
plain clause on first use or cut it.

TOPIC MODE: real current events. For each piece:
1. Find a genuinely recent, real news story (within the last 5 days of today's date).
   Spread the {{N}} stories across different subject areas (politics, science, business,
   culture, sport, world) so the set does not cluster on one beat. For political stories,
   pick the angle by tier and mode: on the NON-civic tier, report the issue and competing
   positions fairly without taking a side. On the CIVIC tier, a story on a broad civic/policy
   matter (value-consensus: local services, a bill's tradeoffs, school funding, infrastructure,
   governance, civic duty) MAY be drafted in pointed-advocacy mode with a clear role-speaker
   and first-person emotion aimed at the issue or institution. A story that can only be told
   by targeting an identifiable political figure, or by taking one side of a national third
   rail (abortion, guns, partisan elections/candidates, whether birthright citizenship should
   exist), stays neutral and routes to The Ledger or is dropped.
2. Build a numbered, verified fact list per Accuracy-Guardrail BEFORE drafting.
   Web-search and confirm every name, number, date, quote, and causal claim against a
   real source. If you cannot confirm a fact, drop it. Never invent or guess a fact.
   If a whole story cannot be verified, swap it for one that can.
3. Draft only from the fact list, with sources closed (expression firewall).

VARIETY (run the orchestration note in Generation-Briefs.md and the Variety Matrix in
Cross-Piece-Sameness-Rubric.md):
- Fill the Variety Matrix BEFORE drafting: one row per piece, each assigned a different
  register, template, opener type, rhythm profile, and close type.
- No two pieces share a register, template, opener type, or close type. Spread registers
  across the 7-voice palette. Force at least one long-periodic and one clipped rhythm
  into the set. Cap the terse one-line button close at one piece.

GATES (run all five from the Generation-Briefs.md pre-flight before any piece is final):
Gate 0 editorial fit (neutrality firewall + plain-knowledge accessibility), Gate 1 accuracy
+ expression firewall, Gate 2 register-band check, Gate 3 anti-tell scan, Gate 4
batch-sameness across the whole set. A piece that fails a gate goes back before it ships.
Do not show me the gate work; just do not ship a piece that fails.

OUTPUT: present each piece as the full inbox lesson-opener package, in this order:

  SUBJECT LINE: the email subject, the way it lands in the inbox
  HEADLINE: the piece's title
  Register and focus: e.g. "The Reckoning | anaphora and antithesis"

  HEADNOTE: one or two sentences in the neutral voice of an AP exam passage headnote,
  naming the rhetorical situation (speaker or speaking role, audience, occasion or
  purpose) per Headnote-Spec.md. Write it BEFORE the piece, then draft the piece to earn
  exactly that situation. Frame an invented persona by role, never a fabricated name;
  name a real subject truthfully; take no side; name no devices. Goes on both copies.

  THE PIECE
  the 350 to 600 word original opener, clean reading copy, no inline marks

  RHETORICAL DEVICES IN THIS PIECE
  3 to 6 devices that are actually present. For each: quote the exact phrase from the
  piece, name the device, and explain in one or two sentences what it does and the effect
  it creates. Only label devices that are genuinely there.

  MULTIPLE CHOICE (AP Lang style)
  2 questions built to MCQ-Construction-Spec.md. The two MUST target different reading
  skills (for example one Reasoning or Claims item and one Style tone item), not two
  function-of-a-phrase questions. Four options each (A to D), exactly one defensibly best;
  every distractor plausible and partly true and failing by a named trap from the spec, no
  free elimination a student discards on sight. Run the spec self-check before finalizing.
  Add an answer key with a one-line rationale for each.

  DISCUSSION QUESTIONS
  2 open questions a teacher could put on the board

  RHETORICAL ANALYSIS PROMPT
  1 AP Lang Q2-style prompt asking students to analyze the rhetorical choices the writer
  makes in the piece

After all {{N}} packages, give me a one-paragraph batch note: the register, template,
opener, and close used for each piece, and confirmation the batch passed the sameness
rubric (or what you changed to make it pass).

Set {{N}} = ___
```
