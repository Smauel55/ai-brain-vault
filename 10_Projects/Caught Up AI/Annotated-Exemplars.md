---
created: 2026-06-05
updated: 2026-06-12
tags: [project, caught-up-ai, writing, exemplars, style]
project: "[[Caught Up AI]]"
---

# Annotated Exemplars (D6)

> Worked, fully annotated model pieces for the [[Caught Up AI]] content engine. Each one shows a single register in action with the craft moves named, the quantitative bands hit, the AI tells dodged, and the v2.1 friction layer applied. Read these as imitation targets, not as templates to copy literally.

> REGENERATED 2026-06-12 (v2.1). All seven pieces and the Before/After were rewritten from the updated specs after [[Proxy-Pilot-Run-2]]: each now carries a headnote written first per [[Headnote-Spec]], is clean on Gate 0 (neutrality + plain knowledge per [[Editorial-Standards]]), is friction-layer compliant per [[Anti-Tell-List]], sits inside its (revised) bands in [[Register-Specs]], and fixes the #1 Run-2 miss, subject-first openers. The Ledger additionally reflects the 2026-06-12 readability revision (plainer, shorter, no long anchor sentence).

## How to use these

- These are the imitation models for the registers defined in [[Style-Palette]] and [[Register-Specs]]. When a [[Generation-Briefs]] brief calls for a register, the matching exemplar here is the concrete target the model should write toward.
- Read the piece first, then the annotation. The annotation names the move so you can recognize it and ask for it again in plain language ("open on a date, not the subject," "concede then turn," "let the close trail").
- Imitate the craft, never the topic or the specific wording.
- **Specifics are now inline and deliberately un-tidy (changed in v2.1).** The earlier exemplars bracketed every fact as [PLACEHOLDER], which sanitized the prose and modeled exactly the "too-tidy specific" tell Run 2 caught. These versions instead write real-feeling, messy, illustrative specifics straight into the prose (1.9 not 2; "about nine dollars" not "$9.00"; dull institution names; invented people framed by role, not by fabricated personal names). Every such specific is INVENTED and ILLUSTRATIVE. The bold banner above each piece says so. In production, each is replaced by a verified fact per [[Accuracy-Guardrail]]; verified facts are naturally messy, which is the whole point. Never ship a number or name from these files.
- The structural skeleton each piece uses is described in [[Structural-Templates]]. The tells each piece avoids are catalogued in [[Anti-Tell-List]]; the friction layer is at the top of that file. If a draft drifts, diagnose against those two files first.
- **The friction is placed differently in each piece on purpose.** One leans an argument, one trails its close, one leaves a thread hanging, one carries an inert off-thesis detail. If you imitate them all with the same single roughness in the same spot, the friction becomes its own template, which is a fresh tell ([[Cross-Piece-Sameness-Rubric]], the friction-uniformity check).
- You have drifted if a draft reads like every other piece in the batch. Spread the registers, and spread the friction.
- The before/after repair at the end shows the same news written first in full AI-tell mode, then repaired into a clean (and now plainer) Ledger.

---

## The Ledger

**Register:** The Ledger (with the 2026-06-12 readability revision: shorter sentences, shallow subordination, no long periodic anchor, plainer diction).
**Template used:** Finding-First / Claim-First Build (10). Situation, cause, scope, the two live disputes, current status. Define-then-apply is nested for the per-mile-fee gloss.
**Topic label:** a federal per-mile road-usage charge pilot, public-finance / transportation domain.

> ILLUSTRATIVE: every name, number, and date below is invented and deliberately un-tidy, to model real reported particulars. Replace each with a verified fact before anything ships.

*The following lays out how a new per-mile driving fee works, why some states are testing it as the gas tax falls behind, and where its costs and privacy questions still stand.*

In four states this spring, a little over five thousand drivers began paying for the roads by the mile instead of the gallon. They report their mileage with a plug-in device or a once-a-year odometer photo. In exchange they skip the federal gas tax at the pump. The fee runs about a penny and a half per mile. For most of them it comes out close to a wash, give or take a few dollars a month.

The reason is not hard to find. The federal gas tax has sat at 18.4 cents a gallon since 1993, while the cost of building a road has roughly doubled. The fund it feeds, the one that pays for interstates and big bridges, has needed repeated bailouts from general taxes to stay solvent. Electric cars use the roads and buy no gas, and they were about one new car in nine sold last year. A tax on gallons brings in less as the cars sip less.

So a few states are testing a charge on distance instead. The open question is whether it can be collected cheaply, and without tracking where people drive. On cost, the early figures are not flattering. The pilots spend close to a dime to bring in a dollar, against well under a penny for the gas tax. Officials say most of that gap is the price of running something small and new.

Privacy is the harder problem, and it deserves its strongest form. A device that counts miles can, if it also notes location, record everywhere a car goes. Drivers in the pilots can pick a version that logs no location at all, and state law tells the contractor to delete location data after a few weeks. Whether those rules would survive the jump from a few thousand volunteers to every driver in the country is the one thing a pilot cannot tell you.

Rural drivers were supposed to be the losers here, since they cover more miles. For many of them the interim report found the reverse. They drove more, but in older trucks that guzzle, so under the gas tax they were already paying more than a per-mile fee would charge. The plug-in device, for what it is worth, is about the size of a garage remote.

For now it stays a pilot. Congress has funded the studies through 2027 and has not voted to make the fee real or national. The gas tax keeps falling short. The trust fund keeps drawing on general money. Whether a per-mile charge is the fix it was built to be is still an open question on the evidence.

*(about 415 words.)*

### Annotation

HEADNOTE (written first, per [[Headnote-Spec]]): an occasion/context line, no speaker persona, because forcing a fake voice onto a neutral explainer is itself a tell. It names the matter being laid out and the open questions, takes no side, and names no devices.

OPENER FIX (the #1 Run-2 miss): the Run-2 Ledgers ran 77% and 90% subject-first. Here the openers are spread off the subject: "In four states this spring" (temporal), "In exchange" (prepositional), "For most of them" (prepositional), "So a few states" (coordinator), "On cost" (prepositional), "For many of them" (prepositional), "Whether those rules..." (dependent), "For now" (prepositional). Roughly half the sentences still open on the subject, which is in band; the cure is converting four to six per piece, not all of them.

READABILITY (the 2026-06-12 revision, load-bearing here): sentences are short and plain. Mean lands near 16 to 17. There is NO long periodic anchor sentence; the longest is in the low 30s. Subordination is shallow, mostly one clause or none, because stacked clauses were the wordiness Samuel flagged. The diction prefers the plain word ("brings in" not "generates", "a wash" not "revenue-neutral"). This deliberately overrides the proxy, which wanted a longer anchor.

FRICTION (v2.1), placed as one inert detail: "The plug-in device, for what it is worth, is about the size of a garage remote." It does not advance the argument; it is just true. The Ledger absorbs an inert particular better than any register because its posture is "here is the record." The concession is also lopsided on purpose: privacy gets a full paragraph at its strongest, equity gets a single turn that overturns the expected story. Not every paragraph buttons.

UN-TIDY SPECIFICS (illustrative): "a little over five thousand," "about a penny and a half," "about one new car in nine," "close to a dime," "a few weeks." The two real-world anchors that happen to be exact (18.4 cents, 1993) stay exact because reality is sometimes exact; the invented figures are messy.

CLOSE: a flat status report, not a button: "is still an open question on the evidence." No uplift, no image, no call to action, and crucially no long re-marshalling sentence.

TELLS DODGED: no cosmic-frame or question opener; no Family A through F diction; no significance-inflation; plain copula throughout ("is not hard to find", "is a pilot"); no autopilot tricolon; no false balance (concede-then-advance instead); no signposting ("read these together"); zero em-dashes.

---

## The Open Letter

**Register:** The Open Letter
**Template used:** Quote-the-addressee-back, nested in Concession-then-bind. The engine is the addressee's own printed value ("a place that treats its staff like family"), set against its conduct, so the contradiction reads as theirs.
**Topic label:** a hospital system ending the flexible scheduling its nurses relied on, while still advertising itself as family-first. Labor / health-care domain.

> ILLUSTRATIVE: the health system, the persona, the date, and the figure below are invented and deliberately un-tidy. The persona is framed by role, not given a fabricated personal name; the addressee is an institution, not a real or identifiable person. Replace specifics with verified facts before shipping.

*In the following open letter, a hospital night nurse writes to the chief executive of the health system that employs her, after the system ends the flexible scheduling its nurses had relied on.*

To the chief executive of Halsted Health, from one of the nurses on your night shift, set down where the rest of the building can read it.

Having read the notice twice, I would not write to you over the heads of my managers if the thing were small. On the second of June your office said that the flexible scheduling our floor kept after the pandemic will end in September, and that all of us go back to fixed rosters. The notice ran four paragraphs. It did not use the word nurse once.

There is a sentence you have printed in three annual reports and laminated on the wall above the cafeteria line, and I have it by heart: that Halsted is, before it is anything else, a place that treats its staff like family. I do not bring it up to embarrass you. I bring it up because I think you meant it, and because some of us stayed here, at pay we could beat across town, on the strength of it.

Consider what the fixed roster actually asks. It asks the nurse raising a child alone to choose, every week, between the shift on the board and the kid she cannot leave at home; it asks the one nursing her own mother through chemo to file that mother under scheduling conflict; it asks all of us to hear the word family from this building and understand the building did not mean ours. I am not saying you intend that. I am saying the roster will do it whether you intend it or not.

Your own exit survey has a number in it I did not have to dig for. Two of every five nurses who quit last year named the schedule as the reason. You have seen that figure. Your name is on the page it sits on. I am asking you to read it once more, beside the sentence on the wall.

I am not asking you to be generous. Generosity would put me in your debt, and I am asking for nothing that is not already yours: the sentence you printed, the people who believed it, the staff you have said you cannot afford to lose. Keep those, and the schedule more or less keeps itself.

So I will not make a demand. The policy takes effect in September. If, before then, you decide the wall meant what it says, the night floor will know, and remember, and stay. If it did not, we will learn that too, and quietly make our own arrangements.

A nurse on your night service

*(about 440 words.)*

### Annotation

HEADNOTE (written first): names the speaking role (a hospital night nurse), the addressee (the chief executive of the employing system, an institution), and the occasion (the end of flexible scheduling). It frames the persona by role with no fabricated name, takes no side, names no devices.

NEUTRALITY (Gate 0): pointed advocacy is allowed on the civic tier when it is aimed at an institution over a documented practice. The force here lands on the roster and the institution, never on a person; the addressee is an office and a company, not a named or identifiable individual. This is exactly the civic-tier latitude in [[Editorial-Standards]].

OPENER FIX: Run 2 had this register at 76.5% subject-first. The opener is where the deference belongs, so the cure is also the craft: a vocative opener; "Having read the notice twice" (participial); "On the second of June" (temporal); "There is a sentence" (existential); "Consider what" (imperative); "So I will not" (coordinator). The "I" sentences cluster where the writer lowers their own standing, which is in register.

LOAD-BEARING CRAFT: the quote-back ("a place that treats its staff like family") is the whole engine; deleting it collapses the letter. The one periodic showpiece is the "It asks... ; it asks... ; it asks..." sentence, articulated with semicolons (the register's structural mark) and answered by short flat landings ("It did not use the word nurse once." / "You have seen that figure."). Pathos is rationed to two concrete scenes (the single mother, the parent in chemo).

FRICTION (v2.1), placed as an un-tidy statistic plus an inert image: the figure is "two of every five," not a tidy "41 percent," and it is attributed to the addressee's own document. The laminated sentence "above the cafeteria line" is a concrete particular that is just true. The single anaphoric tricolon is capped at one and its members differ in length; a second balanced run would read engineered.

CLOSE: the consequence is handed to the addressee as their choice, not a demand, and a thread is left open ("quietly make our own arrangements"), so the letter does not ring shut.

TELLS DODGED: no direct attack on the addressee (the move is "you said X; this contradicts X"); no sarcasm; plain copula; no significance-inflation; no fabricated personal name for the addressee; zero em-dashes (turns carried by colon, semicolon, comma).

---

## The Reckoning

**Register:** The Reckoning
**Template used:** Periodic-Build-to-a-Button, braided with Antithesis-as-engine (the few in the room against the many households) and a Charge-to-act close.
**Topic label:** a regional water authority that let lead exceed the federal limit for months while its board knew. Municipal / public-health accountability.

> ILLUSTRATIVE: the authority, the figures, the dates, and the geography below are invented and deliberately un-tidy. The culprit is a body (the board), not a fabricated named individual. Replace specifics with verified facts before shipping.

*In the following address, a resident speaks to fellow residents after a regional water authority disclosed that it had let lead levels exceed the federal limit for months while its board knew.*

On Tuesday, the Hartwell Valley Water Authority told the households it serves, roughly seventy thousand of them, that the water they had been drinking, cooking with, and stirring into baby formula had run above the federal limit for lead for nineteen months, and that its board had known for at least fourteen of them.

Sit with that, because the authority would rather you skimmed it.

When we are told that a treatment chemical was quietly dropped to save something like half a million dollars a year, and that the engineer who put her warning in writing was moved to another desk a few weeks later, and that the same board approved its own performance pay in the quarter the lead readings were climbing, we are not looking at bad luck or hard chemistry. We are looking at a choice. Nine people in a room decided what the health of those households was worth, and the figure they settled on was smaller than their own bonus.

Lead does its quietest work on the smallest bodies. While the board sleeps tonight in the parts of the valley that were never on the bad line, a child somewhere on the east side is drinking from a cup his mother filled at a tap she was promised was safe. The metal does not rinse out when the boil notice lifts. It settles into bone. It comes back years on, in a classroom, as the page he cannot read and a teacher who cannot say why.

None of us who pays a water bill here gets to stand fully outside this. We paid for the authority. We picked the commissioners who seat its board, and then we let the meeting minutes go unread. The board was counting on exactly that. Being ignored is the cheapest thing a public body can buy, and we kept it cheap.

There is a tidy telling of this in which the science was hard and everyone meant well. The memo, the transfer, and the bonuses are what that telling has to leave out.

So the question is not whether the board failed. The readings already answered that. The question is what we do in the forty days before its members come up for reappointment. We can let the notices lapse and the minutes go unread again. Or we can fill the commission chamber on the fourteenth and make that reappointment the most expensive vote those commissioners have ever cast. The pipes will take years. This can start in forty days. We should not give them one more than that.

*(about 425 words.)*

### Annotation

HEADNOTE (written first): names a public-address situation, a real datable occasion (the disclosure), and the responsible body (the authority and its board, an institution, never a named politician). No side named beyond what the facts compel, no devices named.

NEUTRALITY (Gate 0): the culprit is an institution and a documented practice, which the civic tier permits. The blame is never forced onto a named person; "nine people in a room" is the board acting as a body. If the only available culprit were a politician, this would route to The Ledger.

OPENER FIX: Run 2 had a Reckoning at 78% subject-first. The register's own devices are the cure: "On Tuesday" (temporal), "Sit with that" (imperative), "When we are told" and "While the board sleeps" (the present-tense pivot and the suspended subordinator), "So the question is not" (coordinator). Subject-first lands in the low 60s, in band, with five non-subject opener types.

LOAD-BEARING CRAFT: ONE runway (the "When we are told that... and that... and that..." sentence, about sixty words, periodic, landing on "we are not looking at bad luck"), articulated by "when/and that" clauses and commas, never a dash. The statistic-to-scene pivot fuses logos and pathos: the dropped chemical and the bonus become one child at one tap. The "we" is implicated even as the few are charged.

FRICTION (v2.1), placed at the specifics and the buttoning: the figures are un-tidy ("roughly seventy thousand," "something like half a million dollars," "a few weeks later"), the culprit is a body rather than an invented CEO, and the close is the one earned hard button this register is licensed. The button is a CHARGE ("We should not give them one more than that"), not a negation-correction kicker, and not every paragraph buttons. The "the question is not X, the question is Y" pivot is used exactly once, at the turn.

CLOSE: a charge to act with a concrete deadline. It tightens rather than opens, which is the register's signature and is earned by the datable trigger.

TELLS DODGED: no negation-correction closer; one runway, not two; no fabricated named villain; no round-tidy numbers; no labeled enumeration; no name-calling (the word that could be "lie" is avoided, the facts carry it); zero em-dashes.

---

## The Tribute

**Register:** The Tribute
**Template used:** Antithesis-as-engine (small means against large result) braided with Narrative-into-claim (the flatlining screen, the seven-word line) and a Placement-into-permanence close.
**Topic label:** the controlled end of a long-running deep-space probe's mission. Science / commemoration. The subject is a thing, not a person, which keeps the exemplar from fabricating a human.

> ILLUSTRATIVE: the mission, its length, and its details below are invented. In production a Tribute names a REAL subject truthfully (per [[Headnote-Spec]]); this stand-in is illustrative only.

*The following is a tribute to a deep-space probe at the end of its mission, reflecting on the work of the people who kept it running.*

This week, a machine died, and it is not foolish to feel it.

The probe carried no crew. It flew no flag, won no argument, settled nothing that divided the people who paid for it. It was a box of instruments about the size of a refrigerator, stamped with a build date and a serial number, and one morning last week, after twenty-two years in the dark, it sent its last full report home and went silent.

Think how little it was, to do so much. Its final signal crossed the distance at the speed of light and still took most of a day to reach the dish in the desert that was listening for it. The engineers on shift did not cheer. They logged the carrier tone, checked the last packet, and watched a line on a screen go flat the way a pulse does. One of them said, later, only that they had kept it warm as long as they could. That is the whole tribute, in the words of someone who would never call it one.

And the line carries more than it says. A craft built to last five years had worked for twenty-two. It saw what no one had seen. It sent back the first clear pictures of a ring around a far planet, long after most of the people who designed it had retired or moved on or died. It outlived its makers' careers. It did not outlive their care.

Yet some lives get measured by their noise. This one is measured by the quiet, and by what filled the long middle before the quiet came. We are clumsy, as a country, with that middle. We turn out for the launch and the first picture and the press conference. We have no ceremony for the years of someone arriving before dawn to nudge an antenna a fraction of a degree, so that a faint voice from very far off can still be heard.

So we mark the day, not as an ending but as a handoff. The probe is gone, drifting now on a course it will hold for longer than there have been people to track it. But the patience did not drift off with it. It got handed down. And the students who plotted the last maneuver were not born when the thing left the ground, and some morning they will be the ones arriving before light, for something none of us will live to see go quiet.

We have its example. We could do worse than to keep it.

*(about 440 words.)*

### Annotation

HEADNOTE (written first): names the subject (the probe), the occasion (the mission's end), and the consecratory purpose. No evaluative adjective ("moving", "remarkable"), no devices named. Because the subject is invented for this exemplar, the banner flags it illustrative; a production Tribute names a real subject truthfully.

OPENER FIX and CADENCE (the same move): Run 2 had the tributes at 72% to 82% subject-first with the coordinator opener, the register's own signature, sitting at 12%. Here And/Yet/But/So open about one sentence in five ("And the line carries more", "Yet some lives", "But the patience did not drift", "So we mark the day", "And the students"), which both fixes the opener miss and chains the cadence the way the register wants.

LOAD-BEARING CRAFT: narrative-into-claim (the logged carrier tone and the seven-word line opened into "That is the whole tribute"); antithesis as the engine, but VARIED in shape so two balanced antitheses never run back to back ("outlived their careers / not their care"; "measured by their noise / measured by the quiet"; "the launch / the long middle"). Grandeur comes from understatement ("a box of instruments about the size of a refrigerator"), not piled superlatives. The speaker recedes into a communal "we."

FRICTION (v2.1), placed at the close: the benediction is earned and stays, but there is NO ring composition. The last line ("We could do worse than to keep it") does not answer the first line ("a machine died"), and a melancholy thread is left open ("for something none of us will live to see go quiet"). Short lines are complete buttons, not verbless fragments.

CLOSE: placement-into-permanence plus a quiet benediction, the long cadence resolving into a short complete line. No call to action, no reveal-kicker.

TELLS DODGED: no significance-inflation (the stakes are shown through the flatlining screen, never asserted); plain copula ("It was a box of instruments"); no superlative-piling; no ring close; no fabricated human subject; zero em-dashes (the appositive accumulation handled by commas and sentence breaks, this register's highest dash risk).

---

## The Long Think

**Register:** The Long Think
**Template used:** Problem-Reframe (redefinition-as-engine) run through Concession-then-rebuttal with a withheld turn on the hinge word "Yet."
**Topic label:** the word "agent" as a software industry now uses it. Language / jargon behind an AI-product news cycle.

> ILLUSTRATIVE: the company, the conference, and the "forty-some agents" claim below are invented and un-tidy. The reframe works on the true meaning of the word; replace the news specifics with verified facts before shipping.

*In the following essay, the writer reconsiders what we now mean by the word "agent," granting the case for the new usage before turning to what it leaves out.*

The case for calling these things agents is easy to make, and worth making before quarreling with it. When a program schedules your meetings, drafts your replies, and reorders your grocery delivery without checking first, it does seem to act for you. It has goals, after a fashion, and room to chase them. The word fits the way a glove fits the hand it was cut for. So when a software company stood up at its spring conference and said its products now ship with forty-some autonomous agents inside, the claim was not, on its face, false. Something was automated. Something now runs while you sleep.

Yet the older sense of the word keeps tugging at me, the one a translator has, or a literary agent, or the people a government used to send abroad to act in its name where it could not go itself. An agent in that sense is trusted because it can be held to account; it carries your interests into a room you cannot enter; it can be recalled, or blamed, or fired when it carries them badly. The trust and the accountability are one thing seen from two sides. Nobody calls a thermostat an agent, though it has a goal and changes the room to reach it, because nobody pictures the thermostat answering for the cold.

This is the half of the word the marketing quietly spends. Sell software as an agent and you borrow the warm part, the part that sounds like something is looking after you, and you leave the answerable part on the shelf. The grocery list reorders itself, and when forty pounds of flour arrive nobody is recalled. The reply goes out under your name, and when it offends a client the company points to a settings page you were free to change. We are handed the language of a delegate and the workings of a vending machine.

What the inflation costs is more than neatness. A word that means anything that runs by itself can no longer pick out the thing we might actually need to name, the rare program answerable enough to trust with something that matters. Call the dishwasher an agent and the spy an agent and the autocomplete an agent, and you have not raised the dishwasher. You have flattened the spy.

There is a plainer word sitting right there for most of what is being sold. Automation. It promises nothing it cannot do; it does not claim to look after you, only to repeat. Maybe that is why nobody wants it on the box. Maybe the word will keep slipping the way words do, and we will get used to meaning "on" when we say "agent." I would rather we kept the older one a while longer. I am not sure we will.

*(about 480 words.)*

### Annotation

HEADNOTE (written first): names an essayist reasoning, the theme (the word "agent"), and the analytic purpose (grant the case, then turn). No biography, no devices named.

OPENER FIX and COMMA DENSITY (one move): Run 2 had the Long Think at 73% subject-first AND thin on commas. The cure is the same: front "When", "So", "Yet", "Sell", "Call", "Maybe", which are comma-articulated subordinator and imperative openers, so the opener spread and the comma density come up together.

LOAD-BEARING CRAFT: the withheld turn on "Yet" is the pivot, and it rests on a distinction (answerability), not new evidence. The "I" reasons and never remembers; there is no personal scene, which keeps it out of The Witness Stand. The mandatory chained-semicolon cumulative sentence is "it is trusted because it can be held to account; it carries your interests into a room you cannot enter; it can be recalled, or blamed, or fired." Pathos rides inside the analytic sentences ("forty pounds of flour", "a settings page you were free to change"), never declared.

FRICTION (v2.1), placed at the close (different from the other six): the redefinition engine stays, but the ending does NOT cash the keyword in as a crisp aphorism. It trails on doubt ("Maybe... Maybe... I would rather we kept the older one a while longer. I am not sure we will."), leaves a thread open, and admits probable defeat. That unresolved edge is the deliberate roughness, and it is at the close here, not mid-body.

CLOSE: inward, on a turn of thought that declines to resolve. No "in conclusion", no exhortation, no neat button.

TELLS DODGED: no "not only... but also"; no "it is not X, it is Y" reveal; plain copula throughout ("An agent in that sense is trusted", "It is automation" sense carried plainly); no sentence-head transition reflex; no significance-coda; the key noun "agent" repeated rather than synonym-cycled; zero em-dashes (the dry aside carried by a comma, the pivot by a sentence break).

---

## The Witness Stand

**Register:** The Witness Stand
**Template used:** Redefinition-as-engine on the ordinary word "ask," carried inside a Narrative-into-claim spine, with a gift-close.
**Topic label:** a new state pay-transparency law requiring salary ranges on job posts. Work / personal experience.

> ILLUSTRATIVE: the law, the ages, and the scene below are invented. The first-person voice is a constructed persona framed by role, not a real person. Replace specifics with verified facts before shipping.

*In the following piece, a worker reflects on years of underselling herself, occasioned by a new state law requiring employers to post salary ranges.*

There is a number in my head I have never said out loud, and a law just made keeping it pointless.

This month a state law took effect where I live. Every employer over a certain size now has to print a pay range on the job post. When I read that on my phone in a parking lot, the relief I was supposed to feel did not come. What came instead was the feeling of being found out.

So here is the number, more or less. The first real job I was offered, the kind with a badge and an assigned spot in the lot, the man across the desk asked what I expected to make. Twenty-four years old, and I had practiced the line in the car on the way over. Then the moment came and I said a figure so low he actually paused, and for years I told myself that pause was respect. It was closer to pity. I took the offer. I was grateful. I told my mother I had negotiated.

I had not negotiated. I had asked permission to be paid.

And let me tell you what I think asking really is now, because I had it wrong a long time. I used to think asking was the small voice, the apology tucked into the request, the way you make yourself a little smaller so the no lands softer. That is not asking. That is flinching with words.

What a printed range does is take away the part of the talk where I always lost. It does not make me brave. (I should be honest, I am not sure anything makes a person brave; I think I just got older.) It only removes the guessing, and the guessing, it turns out, was where all the shrinking happened. With the range hidden, I filled the dark with the lowest version of my own worth. A lot of us do.

Since then I have done some hiring myself. I have sat on the far side of that desk and watched someone say a number, then flinch, then talk themselves down before I had said a word, and I wanted to lean over and tell them, stop, you are bidding against yourself, no one in this room needs you to be cheap. I never said it. The desk does something to you. Some part of me still keeps that figure from twenty years ago folded up small, and I cannot quite throw it out.

The law will not fix the gap. The people who study these things will argue for years about what it changed. I do not have a study. I have a parking lot, and a number I was ashamed of, and a wish I will hand you instead of advice: the plain ask. Not the brave one. Just the figure, said once, with the quiet after it belonging to you.

*(about 490 words.)*

### Annotation

HEADNOTE (written first): names a first-person speaking role by scenario (a worker), the shared experience (underselling herself), and the occasion (the pay-transparency law). No fabricated personal name, no devices named.

OPENER FIX (the worst case in Run 2): the citizenship-test piece ran 89% I-initial. This register's openers are supposed to be conversational, so the cure is also the voice: "There is a number" (existential), "This month" (temporal), "When I read that" (subordinator), "What came instead" (wh-cleft), "So here is the number" (coordinator), "And let me tell you" (coordinator), "With the range hidden" (absolute), "Since then" (temporal). The "I" still opens many sentences, but well under half.

LOAD-BEARING CRAFT: the redefinition of "ask" is the engine, tested against its common meaning ("flinching with words") and handed back at the close. Fused pathos-and-ethos: the scene at twenty-four IS both the feeling and the proof of standing. The one long looping sentence (the hiring-desk sentence, about fifty words) swings against the four-word line right after it ("I never said it."). The confiding parenthetical "(I should be honest, ...)" carries the intimacy AND the comma density Run 2 found thin.

FRICTION (v2.1), placed as an un-tidy unresolved detail (different again from the other pieces): "Some part of me still keeps that figure from twenty years ago folded up small, and I cannot quite throw it out." It is odd, a little off-thesis, and left unexplained. The redefinition gift-close stays, but it does not ring the opening shut tidily; it adds something the opening did not promise.

CLOSE: the redefined word handed back as a wish, not a directive. Forward-facing, with the thread of the kept number still hanging.

TELLS DODGED: no significance-inflation (it refuses to narrate importance: "I do not have a study"); plain copula; no vague authority; no tidy three-point bow; no "Here's the thing" pivot; "ask" and "number" repeated rather than synonym-cycled; zero em-dashes (asides in parentheses, the delivered turn with a comma).

---

## The Long Look

**Register:** The Long Look
**Template used:** Accumulation under a repeated frame, braided with Antithesis-as-engine (control against uncertainty) and a patient build to a quiet culminating claim.
**Topic label:** how a regional power grid keeps electricity supply and demand balanced second by second during a heat wave. Energy / infrastructure, a how-it-works marvel.

> ILLUSTRATIVE: the numbers and mechanisms below are written to be checkable-feeling but are invented and un-tidy. The physical relationships are real craft; the figures are illustrative. Replace with verified facts before shipping.

*The following examines how a regional power grid keeps electricity supply and demand in balance, second by second, during the strain of a heat wave.*

The grid keeps almost nothing in reserve. Electricity is made and used in the same instant, so somewhere a control room has to match supply to demand every second of every day, and on the third afternoon of a heat wave that job stops being routine.

Demand climbs through the morning as air conditioners switch on across a few million homes. The operators watch it come. They have a forecast built the night before from the weather, the day of the week, the slow habits of a region, and they have learned roughly how wrong it tends to run; on a mild day it misses by a percent or two, on the fourth day of a heat dome it can miss by much more, because nobody quite knows the hour when everyone reaches for the thermostat at once.

So they hold plants back. Some generators run below their limit on purpose, spinning, burning fuel to make nothing, so that the instant demand jumps they can lift output in seconds; other plants sit cold and take minutes to wake, which in a fast climb is sometimes too slow to matter; and out past the visible plants are the smaller levers, a contract that pays a refinery to drop load on ten minutes' notice, a small dip in voltage that shaves demand without anyone at home noticing, a line borrowed from the next grid over, if the next grid over is not also baking.

But the frequency is how they read the balance. The whole network hums at very close to sixty cycles a second, and that pitch is a kind of gauge; when demand outruns supply the spin of every generator drags a hair slower and the number slips below sixty, and when supply runs ahead it climbs. A drop of a few hundredths of a hertz is the room starting to lose its footing. The operators spend the afternoon nudging a machine the size of several states back toward sixty, working against a number that tells them where things stood a moment ago, not where they will stand next.

And none of it is certain. A forecast is a good guess wearing a decimal point. A plant can trip offline without warning. The wind that was meant to help can fall still at the worst hour. What keeps the lights on is not control in the tidy sense; it is a hundred small corrections made faster than the imbalance can grow, by people who have made peace with never quite knowing what the next ten minutes will ask of them.

And then the sun goes down, the air conditioners ease, and the number drifts back toward sixty on its own, until tomorrow, which is forecast hotter.

*(about 445 words.)*

### Annotation

HEADNOTE (written first): an occasion/context line naming the phenomenon (a grid balancing supply and demand) and why it rewards a close look (the second-by-second strain). No speaker persona, no devices named.

OPENER FIX and PUNCTUATION (the register's own devices): Run 2 had a Long Look at 82% subject-first and, worse, leaning on commas and colons where the register's signature is the semicolon. Both are fixed with the register's tools: the conjunction snap opens several sentences ("So they hold plants back", "But the frequency", "And none of it is certain", "And then the sun goes down"), and the accumulating series are carried on SEMICOLONS, not colons. Colons are held to one or two.

LOAD-BEARING CRAFT: the short-flat-against-long-accumulating rhythm ("The operators watch it come." / "So they hold plants back." snapped against the sixty-word "levers" sentence). The accretive list enacts the complexity, the reader feels the difficulty because the sentence keeps adding parts. Wonder is a byproduct of precision; there are no wonder-words.

CANDOR ABOUT UNCERTAINTY (the register's strongest ethos signature, load-bearing): "they have learned roughly how wrong it tends to run", "A forecast is a good guess wearing a decimal point", "never quite knowing what the next ten minutes will ask of them." Mastery that admits its edges reads as more trustworthy than mastery that performs total command.

FRICTION (v2.1), placed at the close and the signposting (different again): NO labeled enumeration. Run 2 named "The forecast is the first instrument. Real time is the second discipline." as the tell; here the parts are simply set side by side and the reader joins them. The close lands slightly OFF the opening, not as a ring: it opens on "keeps almost nothing in reserve" and ends on the number drifting back "until tomorrow, which is forecast hotter," a small forward shadow rather than a callback.

CLOSE: a quiet culminating sentence that resolves the control/uncertainty antithesis without moralizing and without a rousing button.

TELLS DODGED: no argued claim or blame (it renders, it does not vote); no asserted wonder ("astonishing"); plain copula; no rhetorical question; the frame words repeated rather than synonym-cycled; un-tidy figures ("a few million", "a percent or two", "a few hundredths of a hertz"); zero em-dashes (every snap carried by a semicolon or a sentence break).

---

## Before / After repair exemplar

**Register:** The Ledger (post-readability-revision)
**Purpose:** the same news written first in full AI-tell mode, then repaired into a clean and now plainer Ledger. Read the WHAT CHANGED list as a checklist of the most common tells and their fixes.
**Topic label:** a regional utility raising electricity rates to fund grid upgrades, current-week news.

> ILLUSTRATIVE: every specific in the AFTER is invented and un-tidy. Replace with verified facts before shipping.

BEFORE:
What does it really mean for a community to keep the lights on? In today's world, the answer is rarely simple. This week, a regional utility announced a rate increase, a pivotal decision that underscores the crucial role infrastructure plays in modern life. The move is not just a price change, it is a testament to the enduring challenge of balancing reliability and affordability. Studies show that aging grids face mounting pressure, and experts agree that investment is overdue. The utility's plan showcases a comprehensive strategy. It will fund upgrades. It will harness new technology. It will bolster resilience against extreme weather. Regulators offered cautious support. Consumer advocates raised concerns. Both sides made compelling points. The increase will cost the average household more each month, a striking figure that reflects a broader trend across the sector. Critics argue the timing is poor. Supporters note the necessity. Ultimately, this decision is a powerful reminder that infrastructure, affordability, and accountability must work hand in hand. Despite the challenges, with continued investment and oversight, the future of the grid looks bright. At the end of the day, what matters most is that the community stays connected, resilient, and ready for whatever comes next.

AFTER:
Branford Power wants about nine dollars more a month from the average home. It filed for the raise on March 3rd, and the state utility board rules by July. The math is worth following, because the people who pay are not the people who vote on it. The company says the money rebuilds aging lines and hardens them against the kind of windstorm that cut power to a quarter-million homes last August. That outage is the strongest thing in the filing. The timing is the weakest. Nine dollars is close to a tenth of the median monthly bill on the east side, where the company's own filing admits a rising share of customers are already behind. A consumer advocate told the local paper the raise lands before the last one, eighteen months ago, has cleared most budgets. So grant the company its case. The grid is old. The August storm proved it, and someone pays for new wire either way. The question the board has to answer is narrower than whether the grid needs money. It is whether this house, in this year, is the one that should front it.

*(about 195 words across both bodies.)*

### What changed

- Cut the throat-clearing rhetorical-question opener ("What does it really mean...?") and the "In today's world" cosmic frame. Replaced with the concrete fact: a specific (un-tidy) dollar figure the utility wants, plus the filing date and the ruling deadline.
- Removed "pivotal", "crucial role", "comprehensive", "harness", "bolster", "showcases", "compelling", "striking". (Lexical Families A, B, F.)
- Killed the significance-inflation verbs and codas: "underscores the crucial role", "a testament to the enduring challenge", "reflects a broader trend", "a powerful reminder that". The stake is now shown (the outage, the arrears) instead of asserted.
- Replaced copula-avoidance ("plays a vital role", "showcases a strategy") with plain verbs: "wants", "says", "rebuilds", "is".
- Deleted "studies show" and "experts agree". Every claim now routes to a named, checkable source: the filing, the named advocate in the local paper, the board's deadline. Serves the accuracy gate as well as the AI-tell rule.
- Broke the autopilot tricolons. "Fund X. Harness Y. Bolster Z.", "infrastructure, affordability, and accountability", and "connected, resilient, and ready" were decorative threes. The one surviving series ("the grid is old, the storm proved it, and someone pays either way") is a real escalating concession, not a rhythm.
- Converted the false-balance mush ("Both sides made compelling points... Critics argue... Supporters note...") into a genuine concession that resolves: grant the company its case, then turn to the narrower question. Concede-then-advance, not concede-then-balance.
- Cut both filler frames: "At the end of the day" and the "Despite the challenges, the future looks bright" speculative both-handed coda.
- Replaced the tidy three-point bow with a plain narrowing of the question to one house in one year.
- READABILITY (the 2026-06-12 revision, applied here): the AFTER is deliberately PLAIN and SHORT, not engineered for burstiness. The old version of this repair praised a 40-plus-word periodic sentence; that now violates the Ledger's lowered ceiling. The AFTER's longest sentence stays in the low 30s, subordination is shallow, and the rhythm comes from short verdict lines ("The timing is the weakest.") against medium ones, with openers varied off the subject ("So grant the company its case", "It is whether this house...").
- Register hit (The Ledger): an accounting frame throughout (who pays versus who votes; the math "worth following"), neutral-to-pointed, with the authorial vantage that the burden's distribution, not the grid's age, is the real question. The close is a plain status sentence, not a fragment-button.

### Annotation

BANDS HIT (revised Ledger): plain and fast, mean in the mid-teens, longest sentence in the low 30s, no long anchor, shallow subordination, grade 10 to 12. The cool accounting vantage runs end to end. CRAFT: opener anchors on an un-tidy number plus filing date plus deadline; the stake is shown (the outage count, the arrears) not asserted; a genuine concession that turns; openers varied off the subject; a plain status close. TELLS DODGED: rhetorical-question and "In today's world" openers; Families A/B/C/D/F; significance codas; copula-avoidance; "studies show"/"experts agree"; autopilot tricolons; false balance; "At the end of the day" filler; "Challenges and Future Directions" coda; tidy three-point bow. UN-TIDY SPECIFICS: "about nine dollars", "a quarter-million homes", "March 3rd", "close to a tenth", "eighteen months ago". EM-DASHES: none (commas, colons, periods only).

---

## Related files

- [[Style-Palette]] - the full register set these exemplars instantiate
- [[Register-Specs]] - the per-register specs (bands, opening/closing moves, drift cues, v2.1 friction cues)
- [[Anti-Tell-List]] - the catalogue of AI tells these pieces dodge, and the Friction Layer at the top
- [[Proxy-Pilot-Run-2]] - the diagnosis these regenerations answer
- [[Structural-Templates]] - the skeletons each piece is built on
- [[Headnote-Spec]] - the headnote written first for each piece
- [[Editorial-Standards]] - Gate 0 (neutrality + plain knowledge) every piece clears
- [[Generation-Briefs]] - the briefs that point the model at a register and its exemplar
- [[Cross-Piece-Sameness-Rubric]] - the batch audit, including the v2.1 opener-density and friction-uniformity checks
- [[Caught Up AI]] - project root
