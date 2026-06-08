---
created: 2026-06-05
updated: 2026-06-08
tags: [project, caught-up-ai, content-engine, accuracy, guardrail]
project: "[[Caught Up AI]]"
---

# Caught Up AI - Current-Events Accuracy Guardrail (D8)

The craft layer never wins over the facts. Caught Up AI writes original prose at AP-Lang source-passage quality, but the prose exists to carry verified current-events facts to a paying reader. A beautifully written piece that misstates a fact is a failure, full stop. It is worse than a plain piece that gets everything right, because polish lends false confidence to a wrong claim. This file is the short protocol that keeps style honest. It binds the [[Generation-Briefs]] (where pieces are drafted) and rests on the sourcing reality in [[Content-Sourcing]] and the legal posture in [[Licensing-Verification]].

## The one rule everything serves

- Facts are not copyrightable; expression is. We harvest facts and write our own sentences. That is the whole legal and editorial model.
- Two separate jobs that must both pass: (1) every fact is true and sourced; (2) every sentence is ours, not a source's. A piece can pass craft and still fail here. Both gates are mandatory before publish.

## How facts get sourced and verified (before any drafting)

- Multiple independent sources for every load-bearing claim. Independent means different reporting, not three outlets all rewriting the same wire story. If you cannot find a second genuinely independent confirmation, the claim is not yet usable.
- Primary where possible. A primary source is the thing itself: the court filing, the agency press release, the earnings report, the official transcript, the data table, the on-record statement. Prefer it over any outlet describing it. When you cite a number or a quote, trace it back to where it originated, not to the article that repeated it.
- No single-source claims. One outlet saying something is a lead, not a fact. The exception is a primary source speaking for itself (an agency announcing its own action), and even then a second source confirms it happened and was not retracted.
- Recency and retraction check. Confirm the fact still holds as of drafting. Stories move. A figure reported Monday can be corrected Tuesday. Check that nothing has been updated, walked back, or superseded.
- You have drifted if: you are working from one tab, or from a single source's framing, or you cannot name where a number first came from. Stop and re-source before writing a word.

## Keeping original prose clear of protected expression

We report facts in our own sentences. We never track a source's expression. The danger is not deliberate copying; it is the quiet drift where a source's phrasing seeps into the draft because you read it just before writing.

- Write from the fact list (next section), not from the source text open beside you. Close the source, then write. This single habit prevents most accidental tracking.
- Never follow a source's sentence structure. If the source builds a sentence one way, build yours a different way. Same fact, your architecture. Matching the order of clauses, the sequence of ideas, or the shape of a sentence is paraphrase-too-close even when no words match.
- Never reuse distinctive phrasing. Ordinary factual wording is fine and often unavoidable (a name, a date, a title, a plain description). What is off limits is a source's memorable, chosen, or coined phrasing: a vivid metaphor, a clever turn, a distinctive label they invented, a quotable line. If a phrase has personality, it is theirs, not a fact.
- No paraphrase-too-close. Swapping synonyms into a source's sentence is not original writing; it is a derivative of their expression. The test: could you have written this sentence knowing only the facts, without the source in front of you? If not, rewrite it.
- Direct quotes are quoted and attributed, never absorbed. If you want a person's exact words, put them in quotation marks, attribute them, and confirm the quote is verbatim and in context against a primary or transcript source. A quote stripped of its marks and folded into your prose is both an accuracy risk and an expression risk.
- No academic citations in the prose. Traceability lives in the fact list, not the text. The published sentences carry no "(Author, year)", no "et al.", no journal or working-paper names, and no inline "Researcher's work" or "studies find" source-naming. Attribute inline only to a named public body where natural ("the GAO reported", "the FAA said"). A scholarly citation in an Opener is an academic/AI tell and off-brand. Sourcing a fact (required) and citing it in the text (banned) are different jobs: do the first in the fact list, never the second in the prose. See [[feedback_openers_no_citations]] and the citation ban in [[Anti-Tell-List]].
- You have drifted if: a sentence reads close to one you saw in a source, or follows its run of ideas in the same order, or carries a phrase you would not have invented from the facts alone. Rewrite from the fact list.

## The numbered pre-draft fact list (do this before drafting)

Before writing any prose, build a plain numbered list of the facts the piece will rest on. This is the bridge between sourcing and writing, and it is what you draft from.

1. List each fact as a flat statement, one per line. Names, numbers, dates, events, causal claims, and any quote you plan to use.
2. After each fact, note its source(s) and whether the source is primary or secondary. Every fact needs its trace attached here, not reconstructed later.
3. Mark any fact with only one source. It does not go in the piece until it has a second independent confirmation or is a primary source speaking for itself.
4. Flag anything uncertain, contested, or still developing. If sources disagree, either resolve it or write around it; do not pick the version that reads better.
5. Draft only from this list. The list is the factual spine; the craft (register, structure, rhythm from [[Generation-Briefs]]) is how you carry it, never what you carry.
- The list also doubles as your protected-expression firewall: because you write from your own flat fact statements rather than from source sentences, the prose comes out original by construction.

## The per-piece fact-check step (pre-flight, before publish)

This runs as part of the per-piece pre-flight in [[Generation-Briefs]], alongside the register-band and anti-tell checks. The piece does not ship until every item below passes.

- Every name: spelled correctly, the right person or entity, correct title or role, traced to a source.
- Every number: figure, unit, date, time period, and magnitude confirmed against the source it came from. Re-read it off the source, do not trust memory or the draft.
- Every date: event dates, "as of" dates, and any sequence or timeline confirmed. Watch tense: do not state as current something that has already changed.
- Every quote: verbatim, in quotation marks, correctly attributed, and not pulled out of a context that flips its meaning. Checked against a primary or transcript source.
- Every causal claim: any "because", "led to", "as a result", "drove", or implied cause-and-effect is supported by a source, not inferred by the writer for narrative neatness. Correlation stated as causation is a failure.
- No orphan facts: nothing in the published prose that is not on the fact list and sourced. If a vivid detail appeared during drafting without a source, it gets cut or sourced before publish.
- Final pass: read the piece once asking only "is each claim here true and traceable," ignoring how it reads. Craft is checked separately. This pass is for fidelity alone.

## Failure definitions (so the standard is unambiguous)

- A factual error in a published piece is a product failure regardless of how well it is written.
- A passage that tracks a source's structure or reuses its distinctive phrasing is an expression failure even if every fact is correct.
- A claim with no traceable source is treated as an error until sourced, never given the benefit of the doubt because it sounds plausible.

## Related

- [[Generation-Briefs]] - where pieces are drafted; this guardrail is the accuracy half of its per-piece pre-flight.
- [[Content-Sourcing]] - what the daily content actually comes from and why facts-only generation is the chosen engine.
- [[Licensing-Verification]] - the legal posture behind facts-not-expression; why staying clear of protected expression matters.
- [[Writing-Manual]] - v1 craft apparatus; the anti-tell and rhythm rules the craft layer follows.
