---
created: 2026-06-05
updated: 2026-06-05
tags: [project, caught-up-ai, writing, quality-control, batch-review]
project: "[[Caught Up AI]]"
---

# Cross-Piece Sameness Rubric (D5)

> A no-tooling scoring tool you run over a whole BATCH (one week, about 5 to 7 pieces) before any of it ships. It catches the sameness that a single-piece read cannot see: shared openings, repeated skeletons, recurring phrases, convergent rhythm, and same-close clustering. Each piece can read fine alone and the batch still fails this rubric. That is the point.

## Why this exists (read once)

- A per-piece tell hides inside one essay. A cross-piece tell only appears when you line the pieces up side by side. This rubric is the side-by-side pass.
- Two failure modes this rubric targets:
  - The pieces all open the same way, bend at the same joint, and land the same kind of ending, so the BATCH has a signature even when each piece is clean.
  - The register palette collapses: every piece drifts back to one calm, knowing, mid-Atlantic explainer voice no matter the topic. This is the deepest tell, and the whole palette strategy (see [[Generation-Briefs]]) exists to beat it.
- Best practice: do not rely on catching sameness here. Engineer variety in FIRST by pre-assigning opener, architecture, rhythm, register, and close across the batch (the Variety Matrix, last section). Then this rubric is confirmation, not your only line of defense.
- Companion docs: [[Structural-Templates]] (the architecture and opener menus you draw from), [[Anti-Tell-List]] (the per-piece banned constructions), [[Generation-Briefs]] (the register specs and the matrix you set before writing), [[Writing-Manual]] and [[Content-Sourcing]].

## How to run it (10 to 15 minutes, no tools)

- Lay all 5 to 7 pieces out together. You will read them in slices, not one essay at a time.
- Fill in the one-page Batch Worksheet at the bottom as you go. Each row is one quick pass over the whole batch.
- After the tallies, do the two read tests (blind shuffle, then batch read-aloud). These catch what the tallies miss.
- Any single category that trips its threshold means the batch does NOT ship until the offending pieces are reworked and re-checked. Two or more tripped categories is a signal the generation prompt itself needs adjusting before you regenerate (see remediation).

---

## The ten flags

Each flag below gives you: what the sameness looks like, the eyeball-or-tally signal (no counting beyond a glance), the threshold that triggers a rewrite, and the remediation. The "you have drifted if..." cue is the plain-language version of each threshold.

### 1. Opening-gambit clustering

- What it is: the batch reuses the same first move. The AI defaults are (a) scene-set cold open ("On Tuesday, in a packed hall in Geneva..."), (b) rhetorical question, (c) named-actor-plus-strong-verb ("The Federal Reserve moved..."), (d) abstract-claim-then-pivot ("For decades, X was assumed. That changed this week."), plus stat-lead and quote-lead.
- Signal (Opener Tally): read ONLY the first sentence of every piece, back to back. Sort each into a bucket: scene-set, question, named-actor-verb, abstract-claim, stat-lead, quote-lead. Tally the buckets. Under two minutes.
- Threshold: rewrite if more than 2 of 7 pieces share one opener bucket. Target: no bucket used more than twice; ideally 5 or more distinct opener types across 7 pieces.
- You have drifted if: a third piece opens the same way as two others.
- Remediation: pre-assign each piece a DIFFERENT opener type before regenerating (one scene-set, one in-medias-res action, one historical or contextual frame, one direct stat, one quote-led, one understated declarative, one question; at most one of each). Lock the opener type per piece. Do not let the model pick. Regenerate only the offenders. Opener menu lives in [[Structural-Templates]].

### 2. Identical skeleton (the hidden spine)

- What it is: every piece walks the same arc, e.g. hook, context paragraph, "what happened," "why it matters," forward-looking close. Real source passages vary wildly in architecture (chronological narration, claim-and-refutation, extended analogy, problem-solution, accumulation toward a turn). AI picks one logical engine and repeats it. This is structural, so it survives a single-piece read-aloud.
- Signal: for each piece, jot a one-line spine (3 to 5 beats). Line the spines up. If the beat sequence is the same shape across most pieces, that is the cluster.
- Threshold: rewrite if 4 or more pieces share the same arc shape.
- You have drifted if: you can describe more than half the batch with one sentence ("hook, context, what happened, why it matters, look ahead").
- Remediation: assign each piece a different rhetorical ARCHITECTURE from the fixed menu (chronological narration / claim-and-refutation / problem-then-resolution / extended analogy / accumulation-toward-a-turn / inverted-pyramid reportage / framing-around-a-single-person). Name the architecture in the per-piece instruction so no two pieces share one. Menu in [[Structural-Templates]].

### 3. The "why it matters" pivot as a fixed joint

- What it is: a recurring mid-piece hinge that explicitly announces significance, often the same sentence shape ("What makes this notable is...", "The stakes are higher than they appear...", "This is bigger than X."). It tends to land at the same position (start of the penultimate paragraph) across the batch.
- Signal (Pivot Spot Check): scan each piece for an explicit significance-hinge sentence. Mark Y or N, and note its paragraph position. If most pieces have one at the same position, that is the cluster.
- Threshold: rewrite if the explicit hinge appears in 4 or more pieces, especially clustered at the same paragraph position.
- You have drifted if: four pieces stop to tell the reader, in roughly the same spot, why the news matters.
- Remediation: in the offending pieces, delete the explicit hinge and let significance emerge from the facts and their ordering. Vary where, or whether, the stakes surface at all.

### 4. Convergent rhythm signature

- What it is: the same sentence-length contour repeats, typically two or three medium sentences (18 to 28 words) then one short punch (4 to 8 words), recurring every paragraph. Across a batch this is an identical breathing pattern. Real source passages range from long periodic sentences to clipped reportage, so a true palette shows very different average sentence lengths piece to piece.
- Signal (Short-Punch Test): in each piece, mark how many paragraphs END on a short sentence (a glance, under about 9 words). If every piece does it 2 to 3 times, the rhythm is shared. No word-counting needed.
- Threshold: rewrite if 4 or more pieces use the medium-medium-short punch pattern as their dominant contour.
- You have drifted if: every piece "breathes" the same way when you read it aloud.
- Remediation: assign target sentence-length profiles per piece (e.g. "long periodic, average over 30 words" for one; "clipped, average under 14 words" for another). Force at least one piece long and one piece clipped so the average sentence length visibly differs piece to piece. Enforce by eyeballing, not counting. Rewrite the pieces that drifted back to default.

### 5. Pet phrases and connective tics

- What it is: recurring transition vocabulary, the easiest tell to tally. AI clusters on "But," "Yet," "Still," "And that," "Here's the thing," "Make no mistake," "To be clear," "In other words," "At its core," "The reality is." Plus intensifier tics: "increasingly," "remarkably," "notably," "profoundly," "fundamentally." The same 3 or 4 of these appear across most pieces of an untreated batch.
- Signal (Pet-Phrase Checklist): keep the fixed list (below). Put a tick next to a phrase every time it appears in any piece. One sheet, one pass.
- Threshold: rewrite if any single phrase appears in 3 or more pieces, OR if the batch-wide tally exceeds about one hit per piece on average (more than 6 to 7 ticks across 7 pieces), regardless of distribution.
- You have drifted if: the same little glue word is doing work in three different pieces.
- Remediation: add the phrases that tripped the tally to a running ban list and feed it into the next generation as explicit prohibitions. In the current pieces, replace each flagged instance with topic-specific connective logic, not another generic glue word. Master ban list lives in [[Anti-Tell-List]].
- Fixed checklist (copy into the worksheet): But / Yet / Still / Here's the thing / Make no mistake / To be clear / In other words / At its core / The reality is / increasingly / notably / fundamentally.

### 6. First-word-of-paragraph stacking

- What it is: a sharper view of the same tic problem. Connectives ("But," "Yet," "Still," "And") cluster as paragraph openers across the batch.
- Signal (First-Word Scan): list the first word of every paragraph across the batch in one column. Tics stacking up are visible without reading anything else.
- Threshold: rewrite if the same connective opens a paragraph in 3 or more pieces.
- You have drifted if: your first-word column has "But" or "Yet" stacked three or more times.
- Remediation: same as flag 5; rework the paragraph openings into substantive first words tied to the content, not glue.

### 7. Same close-type clustering

- What it is: the batch ends the same way. AI defaults are (a) zoom-out-to-significance, (b) forward-looking "what to watch next," (c) circular callback to the opening image, (d) the terse one-line "button." When most pieces land the same final beat, the close is a batch fingerprint.
- Signal (Closer Tally): read ONLY the last sentence (or last two) of each piece, back to back. Bucket each: zoom-out, what-to-watch, callback, one-line button, quote. Two-minute pass.
- Threshold: rewrite if more than 2 of 7 share one closer bucket. The one-line button close is capped at ONE piece per batch (Samuel flagged it on 2026-06-04 as over-used).
- You have drifted if: a third piece zooms out to significance, or a second piece ends on a terse button.
- Remediation: pre-assign closing types the way you pre-assign openers (one quiet image, one consequence-statement, one unresolved tension, one factual last beat; at most one terse button). Rewrite the pieces whose endings collided.

### 8. Banned-construction recurrence (project-specific, fatal)

- What it is: model defaults that are per-piece tells but recur across pieces because the model keeps reaching for them: em-dashes (the long dash, hard ban), the "not just X but Y" frame, the "it's not about X, it's about Y" close, parallel triplets, and strained aphoristic wrap-ups. Any appearance is a hard fail.
- Signal: scan each piece for these specific constructions. Mark the piece if it has any.
- Threshold: ZERO tolerance. ANY occurrence triggers an immediate fix of that piece. No batch threshold needed.
- You have drifted if: you find even one. This is a gate, not a judgment call.
- Remediation: hard find-and-fix on every flagged piece before anything else. Replace the long dash with commas, semicolons, colons, or a new sentence. Rewrite "not just / not about" frames and triplets into pairs. Cut aphoristic wrap-ups. Full list and rewrites in [[Anti-Tell-List]].

### 9. Uniform paragraph count and length

- What it is: in a 350 to 600 word range, AI tends to produce the same shape every time, e.g. 5 even paragraphs. Real source passages vary: some are one dense block, some are many short beats. Identical paragraph counts and even block sizes across the batch are an at-a-glance tell.
- Signal (Paragraph-Count Column): write each piece's paragraph count in a single column (e.g. 5, 5, 5, 6, 5). Eyeball the spread. Identical numbers jump out instantly.
- Threshold: rewrite if 4 or more pieces share the identical paragraph count. Target a visible spread (counts ranging across at least 3 different values in a 7-piece batch).
- You have drifted if: your column is mostly the same number.
- Remediation: deliberately vary structure. Collapse two paragraphs into one dense block in one piece, break another into more short beats. Re-count the column afterward to confirm the spread widened.

### 10. Register flattening (the palette collapsing)

- What it is: the deepest tell. The brief demands a PALETTE of distinct professional registers, but the model gravitates to one default "smart-explainer / public-radio" voice regardless of topic. Even when other variables are nudged, the diction, the formality level, and the ethos posture (calm, knowing, lightly authoritative) stay constant.
- Signal (Blind-Shuffle Test, the highest-value no-tool check): strip the titles and topics, lay out just the openings of all 5 to 7 pieces, and ask: do these sound like 5 to 7 DIFFERENT writers, or one writer on 5 to 7 days? If you cannot tell them apart by voice, the palette has collapsed.
- Threshold: rewrite if you cannot confidently attribute the openings to distinct authors, i.e. if 4 or more of 7 feel like the same writer. Target: at least 4 to 5 of 7 read as clearly different registers.
- You have drifted if: shuffled and stripped of topic, the pieces are indistinguishable by voice.
- Remediation (upstream, regenerate not patch): when the blind shuffle fails, the problem is in the prompt, not the pieces. Re-run generation with explicit, distinct register specs per piece (e.g. measured policy-essayist, vivid narrative reportage, dry analytical explainer, reflective long-form) drawn from the palette. Treat each register as a separate ethos and diction brief, not a tone adjective. Register specs and the named palette ([[The Ledger]], [[The Open Letter]], [[The Reckoning]], [[The Tribute]], [[The Long Think]], [[The Witness Stand]], [[The Long Look]]) live in [[Generation-Briefs]].

### Bonus check: evidence-handling sameness

- What it is: facts get introduced and attributed the same way every time (same cadence of "According to X," the appositive gloss, one stat per paragraph). Facts are the only thing pulled from sources, so the FRAMING of facts is where house style leaks, and it leaks identically across pieces.
- Signal: in each piece, note how the first fact is introduced. If the attribution cadence is the same across most pieces, mark it.
- Threshold: treat as a soft flag; rework if 4 or more pieces attribute facts in the same cadence.
- Remediation: vary fact placement and attribution (lead with the fact in one, bury it in another, attribute inline in one and at sentence-end in another).

### Bonus check: subject-first opener density (v2.1, the #1 Run-2 band miss)

- What it is: across [[Proxy-Pilot-Run-2]], nearly every piece opened most of its sentences on the grammatical subject ("The agency said", "It found", "I felt"), far above each register's band. This is invisible in a single-piece read but glaring across a batch: the whole set "breathes" subject-verb-object. It is the deepest sentence-level tell the proxy named, distinct from the paragraph-opener tic in flag 6.
- Signal (Subject-First Scan): in each piece, read just the first two or three words of every sentence. Estimate at a glance the share that start on the grammatical subject. You are not counting precisely, you are checking whether the piece is dominated by subject-first openers.
- Threshold: each piece must sit inside ITS register's subject-first ceiling (the ceilings differ; see [[Register-Specs]] opener bands). As a rough guide: The Witness Stand wants under about 50%; The Open Letter, Long Think, Reckoning, and Tribute under about 60 to 65%; The Ledger and Long Look up to about 60 to 70%. Rework any piece that visibly runs above its ceiling, and rework the BATCH if four or more pieces are subject-first dominated even where each is borderline.
- You have drifted if: reading only sentence-openings, the batch sounds like one writer who always starts on the subject.
- Remediation: apply the per-register opener fixes from [[Register-Specs]] (dates and rule-clauses for the Ledger; the present-tense pivot for the Reckoning; the And/Yet/But/So coordinator for the Tribute; If/When/Yet subordinators for the Long Think; conversational So/And/But for the Witness Stand; the But/And/Not-only snap for the Long Look). Convert four to six subject-first openers per offending piece to non-subject openers, then re-scan.

### Bonus check: friction uniformity (v2.1)

- What it is: the friction layer ([[Anti-Tell-List]]) puts deliberate roughness back into each piece (an inert detail, an awkward turn, a flat or trailing close). If every piece in the batch carries the SAME roughness in the SAME place, the friction has become its own template, which is a fresh batch-level tell.
- Signal: note, per piece, what the one rough edge is and where it falls. If all the pieces leave their thread hanging at the close, or all carry their off-thesis detail in paragraph two, the friction has converged.
- Threshold: rework if four or more pieces show the same kind of friction in the same position.
- Remediation: redistribute. Let one piece lean its argument, one trail its close, one leave a mid-body thread, one carry an inert specific. Vary the kind and the position.

---

## Two read tests (do these after the tallies)

- Blind-shuffle test: covered in flag 10. The single highest-value check. Strip topic and title, read the openings cold, ask if they sound like different writers.
- Batch read-aloud pass: read all pieces aloud in ONE sitting, not one at a time. A per-piece read-aloud catches per-piece tells; a batch read-aloud surfaces the shared cadence. If you feel deja vu by piece 3 ("I've heard this rhythm already"), that feeling is itself the signal. Trust it and go find the convergent rhythm (flag 4) or register collapse (flag 10).

## The overall gate

- If any single category trips its threshold, the batch does NOT ship until the offending pieces are reworked and re-checked against this rubric.
- Banned constructions (flag 8) are a hard gate on their own: one occurrence, fix it, no threshold.
- Two or more tripped categories means do not just patch the pieces. The generation prompt is producing sameness at the source. Adjust the prompt and the Variety Matrix, then regenerate, before re-checking.

---

## One-page Batch Worksheet

> Fill this in during your passes. Pieces are columns P1 to P7. Photocopy or retype per batch.

**Batch date:** __________   **Pieces in batch:** ____

**Pass 1, Opener Tally** (first sentence only). Write each piece's bucket: scene-set / question / named-actor-verb / abstract-claim / stat-lead / quote-lead.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Any bucket used 3+ times? Y / N   ->   if Y, flag 1 tripped (rewrite).

**Pass 2, Closer Tally** (last sentence only). Bucket: zoom-out / what-to-watch / callback / button / quote.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Any bucket used 3+ times? Y / N. Button used more than once? Y / N   ->   if either Y, flag 7 tripped.

**Pass 3, Paragraph-Count Column.** Write each piece's paragraph count.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Same number 4+ times? Y / N. Spread across at least 3 values? Y / N   ->   if same 4+, flag 9 tripped.

**Pass 4, Spine line per piece** (3 to 5 beats each):
- P1: ______________________________
- P2: ______________________________
- P3: ______________________________
- P4: ______________________________
- P5: ______________________________
- P6: ______________________________
- P7: ______________________________
- Same arc shape across 4+ pieces? Y / N   ->   if Y, flag 2 tripped.

**Pass 5, Pet-Phrase Checklist.** Tick once per appearance, any piece.

| Phrase | Ticks | | Phrase | Ticks |
|---|---|---|---|---|
| But |  | | At its core |  |
| Yet |  | | The reality is |  |
| Still |  | | increasingly |  |
| Here's the thing |  | | notably |  |
| Make no mistake |  | | fundamentally |  |
| To be clear |  | | In other words |  |

- Any single phrase in 3+ pieces? Y / N. Total ticks over 6 to 7? Y / N   ->   if either Y, flag 5 tripped.

**Pass 6, First-Word column** (first word of every paragraph, all pieces, one list). Same connective opening a paragraph in 3+ pieces? Y / N   ->   if Y, flag 6 tripped.

**Pass 7, Pivot Spot Check.** Explicit "why it matters" hinge present? Mark Y/N and paragraph position per piece.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Hinge in 4+ pieces (especially same position)? Y / N   ->   if Y, flag 3 tripped.

**Pass 8, Short-Punch Test.** Count (at a glance) paragraphs ending on a short sentence per piece.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Medium-medium-short the dominant contour in 4+ pieces? Y / N   ->   if Y, flag 4 tripped.

**Pass 9, Banned-Construction scan.** Mark any piece containing: em-dash / "not just X but Y" / "it's not about X it's about Y" / parallel triplet / aphoristic wrap-up.
- Any piece flagged? Y / N   ->   if Y, flag 8 tripped (fix immediately, hard gate).

**Pass 10, Blind-Shuffle Test.** Topics and titles covered, openings only. Do they read as distinct writers?
- 4+ of 7 feel like the same writer? Y / N   ->   if Y, flag 10 tripped (regenerate with register specs).

**Pass 11, Batch Read-Aloud.** Read all pieces aloud in one sitting. Deja vu by piece 3? Y / N   ->   if Y, hunt flags 4 and 10.

**Pass 12, Subject-First Scan** (v2.1). Read only the first two or three words of every sentence in each piece. Mark each piece inside its register's subject-first ceiling? Y / N.

| P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|----|----|----|----|----|----|----|
|    |    |    |    |    |    |    |

- Any piece over its ceiling, or 4+ pieces subject-first dominated? Y / N   ->   if Y, opener-density check tripped (apply per-register opener fixes, re-scan).

**Tripped categories total:** ____
- 1 tripped: rework the named pieces, re-check.
- 2+ tripped: adjust the generation prompt and Variety Matrix, regenerate, then re-check.
- Flag 8 tripped: fix now regardless.

---

## Engineer variety in first (the Variety Matrix)

> Best practice, and the reason this rubric should mostly come back clean: never generate a batch from one fixed template. Before any piece is written, fill a matrix that assigns each piece a different opener, architecture, rhythm profile, register, and close. Variety is then built in, and the worksheet above becomes confirmation rather than your only defense. The matrix template and the register palette ([[The Ledger]], [[The Open Letter]], [[The Reckoning]], [[The Tribute]], [[The Long Think]], [[The Witness Stand]], [[The Long Look]]) live in [[Generation-Briefs]]; opener and architecture menus in [[Structural-Templates]]; the banned list in [[Anti-Tell-List]].

| Piece | Opener type | Architecture | Rhythm profile | Register | Close type |
|---|---|---|---|---|---|
| P1 |  |  |  |  |  |
| P2 |  |  |  |  |  |
| P3 |  |  |  |  |  |
| P4 |  |  |  |  |  |
| P5 |  |  |  |  |  |
| P6 |  |  |  |  |  |
| P7 |  |  |  |  |  |

- Rule: no two pieces in a batch share an opener type, architecture, or close type. Force at least one long-periodic and one clipped rhythm. Spread registers across the palette. Cap the terse button close at one per batch.
