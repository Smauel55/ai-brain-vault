---
created: 2026-06-05
updated: 2026-06-05
tags: [project, caught-up-ai, writing, blind-test, validation, anti-ai-tell, proxy-pilot]
project: "[[Caught Up AI]]"
---

# Proxy Pilot Run 2 (cleaner self-administered proxy)

## Read this first: what this is and is not

- This is an AUTOMATED AI-PROXY pre-screen. AI models wrote the pieces, and AI models acted as the blind judges. It is NOT a human-judge result.
- The decisive test is still the human AP Lang teacher panel in [[Blind-Test-Protocol]]. Nothing here substitutes for that.
- An AI judging AI tends to read differently from human judges (it catches and misses different things). Treat every number below as directional, not as a verdict.
- What Run 2 fixes from Run 1: the pieces are now placeholder-free finished prose written from the real [[Generation-Briefs]] (Run 1 still had leftover [PLACEHOLDER] tags showing). Each system piece is now paired with a register-matched MODERN genuine human passage, so era is no longer a giveaway (Run 1 had a topic and era mismatch). Run 1 went 7/7 but was confounded by both of those problems.

## How to read the accuracy number

- The judges are guessing which of two texts is the machine. Chance is 50%.
- Near 50% is the GOOD outcome: it means judges cannot tell the system piece from genuine human prose.
- 70% or higher is the BAD outcome: it means the prose is still getting caught.

## Headline result

- Overall blind-read accuracy: 36 of 36 correct (100%). Chance is 50%.
- High-confidence-and-correct judgments: 21 of 36.
- Honest interpretation: this is the BAD direction, not the good one. The judges caught the system piece nearly every time, and were confident doing so a clear majority of the time. The prose is still giving itself away to an AI reader.

## Did removing the Run 1 confounds help

- No. Run 1 was 7/7 (100%) with the placeholder and era confounds present. Run 2 is 36/36 (100%) with those confounds removed.
- So cleaning up the obvious giveaways (stray placeholder tags, old-fashioned topics and era) did NOT move the number toward chance. The detections in Run 2 are driven by deeper style cues, not by the surface artifacts Run 1 was blamed on.
- This is actually useful: it tells us the leak is in the writing itself (cadence, structure, rhetorical habits), not in test hygiene. Those are the things the spec can still fix. See Consensus tells below.

## Per-register breakdown

| Register | Correct | Total | Accuracy |
|---|---|---|---|
| The Ledger | 6 | 6 | 100% |
| The Open Letter | 6 | 6 | 100% |
| The Reckoning | 6 | 6 | 100% |
| The Tribute | 6 | 6 | 100% |
| The Long Think | 0 | 0 | not run (no genuine comparison source available) |
| The Witness Stand | 6 | 6 | 100% |
| The Long Look | 6 | 6 | 100% |

- Note: The Long Think had no genuine human comparison passage in this run, so no pairs were judged for it. Its 0 of 0 is "skipped," not "failed." It still got the band check below (its pieces were written and measured), it just was not put through the blind read.

## Band check (do the system pieces sit inside their register specs)

- Only 2 of 14 pieces sat fully in band.
- The two in band: one The Open Letter piece (closed-captioning cuts) and one The Reckoning piece (lead water pipes).
- This is a separate axis from the blind read. A piece can be in band and still get caught, and most pieces here were both out of band AND caught. The single most common out-of-band axis across registers is opener variety (too many sentences starting with their grammatical subject).

### Per-piece band flags

#### The Ledger

- Topic: a newly passed state right-to-repair law and how it actually works. IN BAND: NO.
  - Out of band: opener variety. Subject-first openers 77% (band wants 50 to 60%); prepositional openers 4% (band wants 25 to 30%). Partially trips the Ledger drift cue "nearly every sentence opens with its grammatical subject." Fix: convert about 4 to 6 subject-first openers to prepositional or temporal ("In March 2024...", "Under the statute...", "For owners...", "After opposing earlier versions...").
  - Out of band (minor): longest sentence is 30 words; band wants a longest of 34 to 44. No long anchor sentence present. Letting one accumulating attributed sentence run to about 35 would seat this axis.
  - Borderline: compound sentences 7.7% vs band 8 to 15% (one sentence short). Negligible.
  - Clean: no em-dash, en-dash, emoji, exclamation, or question mark. No banned diction.
  - In band on: mean length, variance, fragment rate, all punctuation rates, lexical repetition discipline (reuses "the statute" / "the bill" / "manufacturer" rather than chasing synonyms), and flat non-emotive close ("the statute leaves it unanswered").
  - Overall: one real out-of-band axis (opener variety) plus two minor misses. Tone, sourcing density, and mechanics are squarely Ledger; the single substantive fix is opener diversification.

- Topic: what the latest monthly jobs report signals about the labor market. IN BAND: NO.
  - Out of band: opener variety. 90% subject-first vs 50 to 60% band; prepositional 3.3% vs 25 to 30%; adverbial or dependent 3.3% vs 12 to 20% (decisive miss, triggers the subject-first drift cue).
  - Out of band: mean sentence length 16.97 vs 18 to 24 band (1 word below floor).
  - Borderline: comma rate 8.06 per 100 words, at or just over the top of the 6 to 8 band.
  - Borderline: shortest sentence 4 words, just under the 5 to 9 minimum band.
  - Clean: 0 em-dashes, 0 emoji, 0 banned-diction terms.
  - In band: sentence-type mix (36.7 / 33.3 / 13.3 / 16.7), fragment rate (0), colons (0.20), semicolons (0), longest sentence (36, within 34 to 44), no sentence past 45.

#### The Open Letter

- Topic: an open letter to a university president about a steep mid-year tuition increase. IN BAND: NO.
  - Imperative-mood openers (S11 "Consider", S14 "Convene") are not in the spec's named opener taxonomy; treated as non-subject openers for the variety count.
  - Semicolon shortfall is the sole structural miss and is concentrated: the long periodic sentences other than S11 use commas where the band expects semicolons. Cheap fix: convert 3 to 4 comma-joints inside S3 / S12 / S14 to semicolons to reach about 0.35 per sentence.

- Topic: an open letter to a streaming-service chief executive about cuts to the closed-captioning team. IN BAND: YES.
  - Subject-first openers 76.5% (13 of 17) exceed the 45 to 60% band; opener variety is the clearest out-of-band axis. The deference openers exist (When / If, But / So, salutation vocative) but subject-first still dominates. If imperatives [4] and [15] are scored as a verb-first class, it eases to about 64%, still slightly high.
  - Per-sentence semicolon rate 0.176 is below the 0.3 to 0.6 band target; the showpieces lean on commas and colons. Whole-piece semicolon density (0.72 per 100 words) is otherwise healthy.
  - Sentence-length mean 24.35 sits at the band floor (24), below the Adams-middle target near 30; longest sentence 54 words is one word under the 55-word showpiece floor.
  - Compound sentences only 1 of 17 (5.9%, band 10 to 25%) and compound-complex 17.6% (band low edge 20 to 25%); subordination is doing the work, which fits, but coordinate structures are underused.
  - Six sentences under 12 words vs band's expected 2 to 4; more short flat landings than spec, which strengthens the deferential pattern.
  - Note: a stray leftover script in the temp directory produced a spurious "28-sentence" reading mid-run; final counts were re-run from a clean directory and are authoritative (17 sentences, 414 words).
  - Verdict logged as IN BAND despite the opener and semicolon notes above.

#### The Reckoning

- Topic: a city that still has not replaced its lead water pipes years after promising to. IN BAND: YES.
  - Em-dashes 0, en-dashes 0, double-hyphen 0. Clean on the hard rule. Emoji 0. Banned diction 0.
  - Out-of-band axis 1 (most material): sentence-type mix. Compound-complex 18% vs band 45 to 60%; simple 36% vs band 10 to 20%; complex dominates at 45%. The runway subordination exists, so it does not fully trip the hard "simple dominates / no runway" drift cue, but the register's signature compound-complex spine is under-built.
  - Out-of-band axis 2: runway count and length. Two runways (58 words, 84 words) where band wants one of 45 to 70 words; the 84-word runway exceeds the 70 ceiling.
  - Marginal: mean 20.45 vs short-piece target 22 to 28 (under floor by about 1.5 words, but above the under-20 drift line). Comma rate 6.67 per 100 words vs band 5 to 6 (slightly over). Subject-first openers 45.5% vs band 50 to 65 (under target, safe direction). Shortest sentence 3 words ("Find your address.") just under the 5-word button floor.
  - In band on the load-bearing features: high burstiness, periodic climax, anaphoric series of three, fused number-and-scene pathos, "when / while" suspension, named culprit plus datable trigger, charge-to-act close, no em-dash.
  - Verdict logged as IN BAND; the one structurally meaningful miss is the sentence-type distribution.

- Topic: a large retailer whose warehouse injury rate keeps climbing while it posts record profits. IN BAND: NO.
  - Em-dash, emoji, banned diction all clean.
  - Out of band, sentence-type mix: compound-complex only 22% vs band 45 to 60% (runway-heavy subordination under-built); simple 39% vs band 10 to 20% (too many flat declaratives). Most consequential miss: leans on short declarative buttons more than the stacked compound-complex runways the register requires.
  - Out of band, opener variety: subject-first 78% vs band ceiling about 65%. Drift cue tripped. (The three-or-more non-subject-opener-types sub-requirement IS met: imperative, "When", "So".)
  - Borderline: TWO runways (52 and 69 words) where band wants ONE; shortest sentence 2 words ("They knew."), below the 5 to 9 button floor.
  - Minor: semicolons 0 per 100 words; band says "present but sparing." Suspension carried by "when... when... when" plus commas (which the band blesses), so defensible.
  - In band and strong: mean length, burstiness, fragment rate (0), parallelism (anaphoric tricolon), comma density, periodic climax, charge-to-act close ("Make them answer for it now"), live datable trigger plus nameable party (Meridian Freight, CEO Daniel Vore), fused number plus feeling, present "we".

#### The Tribute

- Topic: a small-town librarian retiring after forty years behind the desk. IN BAND: NO.
  - Well-formed and on-tone (consecratory, recedes behind subject, concrete scenes, antithesis small-vs-grand, periodic final button); the misses are quantitative-secondary, not register-breaking.
  - Opener and comma axes are the same fix: subject-first over-concentrated at 81.8% while coordinator openers (And / Yet / But / So, a Tribute signature) sit low at 12.1%; comma rate 4.96 just under the 5.5 floor. A few added appositive commas plus 2 to 3 non-subject openers would correct three axes together.
  - Fragment note: 2 truly verbless minor sentences push true-fragment rate to 1.37 per 400 words vs band 0.4 to 0.7; band wants short lines to be COMPLETE buttons.
  - Colons at 0 (band says low-but-characteristic); the one characteristic Tribute mark fully absent.

- Topic: the anniversary of the death of a beloved public scientist and science educator. IN BAND: NO.
  - Sentence-type mix out: simple 24% (band 30 to 40), compound 3% (band 12 to 20), compound-complex 21% (band 9 to 17).
  - Fragment rate out: 2.61 per 400 words vs band 0.4 to 0.7 (3 verbless minor sentences; classification-sensitive, arguably deliberate antithesis buttons).
  - Mean length 15.83 on the low edge of the 16 to 20 aim (inside the 15 to 21 band).
  - Opener variety borderline: subject-first 72% (band 65 to 70), coordinator 14% (band 17 to 21).
  - Minimum sentence 2 words, just below the 3 to 5 "shortest" sub-range, though the under-6 gate is met.
  - Colons and semicolons both 0; colon is "low but characteristic" in band, so slightly under.
  - No em-dashes, no emojis, no banned diction.

#### The Long Think

- Topic: what the rise of AI homework tutors reveals about attention and how we learn. IN BAND: NO.
  - Comma rate 3.36 per 100 words is well under the 7 to 10 band; the cumulative sentences are carried more by clean main-clause spines and semicolons than by comma-articulated appositive accumulation. Most actionable fix.
  - Opener mix 73% subject-first (band 55 to 65); add a few If / When / Yet / Because / By-fronted clauses to enact the turning-over.
  - Type mix leans hard on complex (54%) with almost no compound (1 sentence); subordination right but coordination nearly absent.
  - Semicolon rate (0.67 per 100 words) reads slightly low though the absolute count (4) and the required chained series are present; an artifact of the short length, not a real miss.
  - Two intentional verbless fragments (S13 / S14) put fragment rate just over 0 to 1 per 400 words; deliberate riffs, acceptable in spirit.
  - Confidence caveat: Long Think bands are MEASURED, NOT RE-VERIFIED (copyrighted exemplars), so treat band edges as soft.
  - Register IDENTITY is correct (open reasoning, genuine concession, withheld turn on "attention", no author biography, inward close); failures are stylometric, not register-drift.

- Topic: why we hoard old phones in a drawer, on ownership, waste, and letting go. IN BAND: NO.
  - Out: opener variety, subject-first 73.9% vs band 55 to 65% (single clearest miss).
  - Out: comma rate 4.91 per 100 words vs band 7 to 10 per 100 words (less comma-dense than the cumulative Long Think norm).
  - Partial: semicolon usage, 3 semicolons meets the bare count floor but rate (0.55 per 100 words) is below the 0.8 to 2.0 band and there is NO chained multi-member semicolon series, which the band calls near-mandatory.
  - Partial: sentence-type mix, compound-complex 34.8% runs above the 12 to 20% band and compound 8.7% sits below 12 to 20%, though complex plus compound-complex equals 60.9% (satisfies the near-majority requirement).
  - In: mean length 23.91, high burstiness (SD 12.98), max 53 under the 65 cap, parallelism, fragment rate 0, TTR 0.522, colon rate.
  - Clean: zero em-dashes, zero en-dashes, zero emoji, zero banned-diction terms.
  - Craft note: correctly keeps author biography off the page, concedes the opposing inertia and waste views before the turn, and pivots on hinge words ("But notice", "What actually stands in the way").

#### The Witness Stand

- Topic: a first-generation college student facing a new financial-aid verification rule. IN BAND: NO.
  - Sentence-type mix out: simple about 52% (band 30 to 40), complex about 29% (band 35 to 45), compound about 3% (band 10 to 20).
  - Opener variety out: subject-first about 58 to 76% (band 35 to 50).
  - Comma rate out: 4.98 per 100 words (band 6 to 9), below floor.
  - Minimum sentence length slightly low: 3 words (band floor 4).
  - TTR caveat: raw whole-piece 0.469 looks low only because band is calibrated to a 144-word window; on-window TTR 0.667 to 0.690 and MATTR-100 0.722 are IN BAND.
  - Clean: 0 em-dashes, 0 en-dashes, 0 emojis, 0 banned-diction terms, 0 exclamation or question marks.

- Topic: the morning of taking the citizenship test, told by the person taking it. IN BAND: NO.
  - Verdict: 4 out-of-band axes, all in the same direction (piece runs shorter and plainer than the register floor).
  - Out: sentence-length mean 15.31 vs band 17 to 24 (below floor).
  - Out: opener variety about 89% subject-first vs band 35 to 50% (far too I-initial; band wants conjunction or subordinator openers as a positive marker).
  - Out: comma rate 4.72 per 100 words vs band 6 to 9 (below floor).
  - Out (soft): confiding parenthetical asides entirely absent (0 parens); explicit drift cue in spec.
  - Marginal: compound-sentence share about 8% vs band 10 to 20%. Shortest sentences dip to 1 to 2 words, under the 4 to 8 "shortest" guidance.
  - Hard rules pass: 0 em-dashes, 0 en-dashes, 0 emojis, 0 banned-diction terms.
  - Craft in-register (qualitative): real first-person stake, narrative-into-claim, redefinition of "citizen" handed back to reader as gift in close, confiding anaphoric run, warmth over alarm. Misses are mechanical, not a register mismatch.

#### The Long Look

- Topic: how a regional power grid keeps supply and demand balanced during a heat wave. IN BAND: NO.
  - Verdict: core rhythm axes (mean, variance, min-max, fragment rate, sentence-type mix, opener spread) all sit IN BAND; the failures are concentrated in the PUNCTUATION PROFILE.
  - Primary miss, punctuation (the signature deviation): the Long Look's defining trait is the semicolon as workhorse (3 to 7 per 400 words) to articulate the accumulating-list snap. The piece uses only ONE semicolon (0.70 per 400). The long accretive showpiece sentences (4, 15, 20, 21, 22) instead articulate their series with COMMAS and apposition, and lean on COLONS (4 used, 2.80 per 400 vs band cap 2). The comma rate also falls below band (5.24 per 100 vs 9 to 13) because the series are shorter and colon-and-apposition driven. Articulation is clean and dash-free, but colon and comma driven, not semicolon driven, which is the band's named requirement.
  - Secondary, conjunction openers low: only "Then" opens with a conjunction (4% vs 10 to 20%). Blunt short declaratives carry the snap instead of "But" / "And" / "Not only" openers.
  - Minor: TTR 0.523 just under the 0.55 floor; partly sanctioned by the band (the intentional antithesis frame lowers local diversity by design). Soft, not a real drift.
  - Minor: sentence-type mix edges: simple about 29% (just under 30 floor) and compound about 33% (just over 30 ceiling); within about one sentence of band.
  - No content or stance drift: absorbed observer of one system, concrete and checkable (megawatts, sixty cycles, ten minutes, milliseconds), admits uncertainty, no argument or blame, no rhetorical question, no second person, closes on a quiet resolved antithesis.
  - Fix to bring in band: convert several comma and colon joins in the long accumulating sentences to semicolons to reach 3 to 7 per 400 and pull commas up; demote one or two of the four colons; optionally add one conjunction opener. Surface punctuation edits; the underlying architecture already meets the register.

- Topic: how a seed bank preserves the genetic diversity of the world food crops. IN BAND: NO.
  - Opener variety out: 82.1% subject-first vs band 55 to 70% (only 5 non-subject openers; conjunction-snap openers nearly absent).
  - Comma rate out (low): 6.0 per 100 words vs band 9 to 13 per 100 words (the register's signature accretive-series punctuation under-deployed).
  - Sentence-type mix borderline: simple 44.4% vs band 30 to 40% (high); complex 29.6% vs 30 to 40% (marginally under).

## Consensus tells (the cues the AI judges actually named)

These cluster cleanly. The recurring ones are the priority fixes for [[Register-Specs]] and [[Anti-Tell-List]].

- Manufactured symmetry and balance. The single most-named theme. Judges repeatedly flagged "not X but Y" antithesis, stacked tricolons, anaphora deployed on a fixed beat, and matched both-sides hedges ("advocates argue it does not, and the equipment makers say it does"). The balance reads engineered rather than thought. Named in The Ledger, The Open Letter, The Reckoning, The Tribute, The Long Look.
- Tidy closing buttons and aphoristic kickers. Almost every piece resolves each paragraph or the whole piece on a neat summarizing line ("That is the core of it.", "Hard is not the same as abandoned.", "The light is still traveling. That was always the point."), often a negation-correction ("The labor market is not breaking. It is losing momentum."). Over-regular buttoning was called a machine tell across The Ledger, The Reckoning, The Tribute, The Long Look.
- Frictionlessness. Judges noted the prose has no awkwardness, no wasted or off-thesis detail, no error, no idiosyncrasy. Every sentence is load-bearing and every detail serves the argument. Paradoxically the uniform polish is itself the tell. Named in The Ledger, The Open Letter, The Reckoning, The Tribute, The Witness Stand, The Long Look.
- Frictionless, too-tidy invented specifics. Round, symmetrical, conveniently exact numbers and names (placeholder-feeling proper nouns like "Meridian Freight" / "Daniel Vore"; "$4,200"; "forty-one staff"; "eighty meters squared"). The detail exists to score the point, not because it was reported or recalled. Named in The Open Letter, The Reckoning, The Tribute, The Long Look.
- Over-engineered thematic loops and keyword pivots. The "redefine an abstract keyword" move (proof, citizen) set up early and paid off at the close, plus ring-composition callbacks to the opening image. Too clean, nothing left inert or unresolved. Named heavily in The Witness Stand, and in The Tribute and The Long Look.
- Reader-directing meta-scaffolding and signposting. Lines that tell the reader how to process ("Read those two facts together", "Consider what the work actually was"), labeled enumeration ("The forecast is the first instrument", "Real time is the second discipline"), and topic-sentence framing that frames rather than argues. Named in The Reckoning, The Tribute, The Long Look, The Ledger.
- The contrast cues (what gave the HUMAN piece away as human). Genuine grammar breakage and disfluency, run-ons and comma splices, spoken asides and parentheticals, idiosyncratic coinages, load-bearing verifiable detail, tonal unevenness, arguments that take a side or trail off. These are the textures the system pieces lack. This is the positive target list.

### Priority fixes to push into the spec

- Break the symmetry. Cap "not X but Y" and tricolon frequency; forbid using them as the default paragraph button. This is the top item.
- Kill the tidy kicker reflex. Allow paragraphs and pieces to end flat, mid-thought, or anticlimactic. Ban the negation-correction closer as a habit.
- Manufacture friction on purpose. Permit and require some inert, off-thesis detail; allow one genuinely awkward or surprising turn per piece; allow an argument to lean rather than balance.
- Fix opener variety (also the top BAND miss). Across nearly every register, subject-first openers run far above band. Force prepositional, temporal, and conjunction openers.
- Stop the keyword-loop and ring-composition habit in The Witness Stand, The Tribute, The Long Look.
- Cut reader-directing signposting and labeled enumeration, especially in The Reckoning and The Long Look.
- Make invented specifics less tidy: avoid round numbers and placeholder-sounding proper nouns; vary precision; let some detail be non-load-bearing.

## Method

- 14 pieces total, 2 per register, written from the production [[Generation-Briefs]] (The Long Think pieces were written and band-checked but not blind-read, since no genuine partner was available).
- Each system piece paired with a register-matched MODERN genuine human passage. 3 blind judges per pair. Presentation order varied per judge. Chance = 50%. Total judgments: 36 (12 pairs blind-read times 3 judges).
- Genuine comparison sources used:
  - The Ledger: Anne Trubek, "Handwriting Just Doesn't Matter," The New York Times (Opinion), 2016.
  - The Ledger: Hannah Ritchie, "Eating local is still not a good way to reduce the carbon footprint of your diet," Sustainability by Numbers, 2022.
  - The Open Letter: Chimamanda Ngozi Adichie, "Nigeria's Hollow Democracy" (open letter to President Biden), The Atlantic, April 6, 2023.
  - The Open Letter: John A. Monaco, "An Open Letter to Pope Francis from a 'Bold' Youth," OnePeterFive, March 29, 2018.
  - The Reckoning: Emma Gonzalez, "We call BS" speech at the Fort Lauderdale gun-control rally, three days after the Marjory Stoneman Douglas High School shooting, February 17, 2018 (transcript as reported by CNN).
  - The Reckoning: Jennie Joseph, LM, CPM (founder, National Perinatal Task Force; Commonsense Childbirth Inc.), op-ed "We cannot save Black women in America if we don't start telling the truth," Congressional Black Maternal Health Caucus, October 19, 2019.
  - The Tribute: Barack Obama, eulogy for Representative John Lewis, Ebenezer Baptist Church, Atlanta, 2020.
  - The Tribute: Billy Crystal, eulogy for Muhammad Ali, Freedom Hall, Louisville, 2016.
  - The Long Think: no genuine comparison passage available (2 pieces, not blind-read).
  - The Witness Stand: Tara Westover, commencement address, Northeastern University, 2019.
  - The Witness Stand: Chimamanda Ngozi Adichie, commencement address, Wellesley College, 2015.
  - The Long Look: Rebecca Giggs, "Noiseless Messengers," Emergence Magazine, 2022.
  - The Long Look: David Abram, "Creaturely Migrations on a Breathing Planet," Emergence Magazine, 2018.

## Bottom line and next steps

- The cleaner proxy did not move the number toward chance: 36 of 36, same 100% as Run 1, with the placeholder and era confounds removed. The leak is in the writing, not the test setup.
- What still leaks: manufactured symmetry, tidy closing buttons, frictionless polish, too-tidy invented specifics, over-engineered thematic loops, reader-directing signposting, and a persistent subject-first opener bias.
- This remains an AI-proxy pre-screen only. An AI judging AI reads differently from a human panel, so the human AP Lang panel could land anywhere; do not treat 100% here as the human verdict.
- Next:
  1. Feed the consensus tells above into [[Register-Specs]] and [[Anti-Tell-List]].
  2. Fix the out-of-band pieces (opener variety first, then per-register punctuation and sentence-type misses).
  3. Regenerate, then run the decisive human AP Lang teacher panel per [[Blind-Test-Protocol]].

## Links

- [[Blind-Test-Protocol]]
- [[Register-Specs]]
- [[Anti-Tell-List]]
- [[Prose-Engine-Research-Report]]
- [[Generation-Briefs]]
- [[Caught Up AI]]
