# -*- coding: utf-8 -*-
"""
Three more sample Openers, rendered through the verified v2 layout engine
(render_opener_v2.build). Registers chosen for variety and accuracy-safety:
  1. The Ledger      - "The Penny Question"  (sourced, low device density)
  2. The Tribute     - "Free to All"          (cadence, short buttons)
  3. The Long Look   - "No Bird in Charge"    (high variance, accretive lists)

On-spec against Register-Specs, Rhetorical-Device-Vocabulary (controlled list),
MCQ-Construction-Spec, Anti-Tell-List (friction layer), Accuracy-Guardrail.
No em-dashes, no emojis. Facts are well-established and stated with honest hedging;
a real published Ledger would still need the full multi-source sourcing pass.

Revisions (2026-06-06, per Samuel):
  - MCQ answer keys distributed across A/B/C/D (was always A).
  - Removed the niche "Free to All" carved-motto allusion (not widely known).
  - Removed Understatement / litotes (dropped from the controlled device list).
"""
from render_opener_v2 import build, randomize_answers

DATE = "Saturday, June 6, 2026"
EDITION = "Sample edition (new format)"

# ============================================================ 1. THE LEDGER
ledger = {
 "base": "Caught Up AI Opener - 2026-06-06 - The Penny Question (The Ledger)",
 "edition": EDITION, "date": DATE,
 "headline": "The Penny Question",
 "body": [
  "The United States Mint has reported for years that the one-cent coin costs more to make than it is worth. [[1]]A penny buys nothing on its own, yet it now costs more than a penny to strike and ship, lately closer to three cents than to one.[[/1]] The figure has stayed above face value every year since 2006. The nickel fails the same test, costing the Mint more than five cents to put a five-cent coin into circulation. Per coin the loss is trivial. In aggregate it is not, because the coins are made by the billions.",
  "Other countries have already run the experiment. In its 2012 budget the Canadian government announced it would stop making the penny, and the Royal Canadian Mint ended distribution the following February. Cash purchases in Canada are now rounded to the nearest five cents, while electronic payments, which cost nothing to round, still settle to the exact cent. Australia withdrew its one and two-cent coins decades earlier. None of these governments has moved to bring the small coin back.",
  "The case for keeping the penny is not empty. [[2]]Rounding falls only on cash, which is used more by people with the least, so a price rounded up at the register is a small tax on exactly those buyers.[[/2]] Pennies still fill charity jars and school fundraisers. And a currency carries habits and attachments that a balance sheet does not record; the one-cent coin has worn Lincoln's profile since 1909.",
  "The evidence has not been kind to that case. [[3]]Studies of cash transactions have found that rounding to the nearest five cents nets out close to zero for buyers over time, because prices round down about as often as they round up.[[/3]] Electronic payment, now most of retail, is untouched either way. The charities that once counted pennies increasingly ask for a card instead. [[4]]The coin has become a rounding error in the economy it was built to serve.[[/4]]",
  "What keeps it in circulation is mostly inertia. Ending the penny would take an act of Congress, which has not come, while the Mint goes on striking a coin it loses money on and a lobbying group funded in part by the zinc that goes into the blanks argues for keeping it. In Ottawa, the missing coin has not been missed. The American penny stays in production, by default rather than decision.",
 ],
 "devices": [
  {"para":1,"device":"Antithesis",
   "purpose":"Setting the coin's worth against its cost in one balanced line (worth a penny, costs nearly three) states the whole problem before any argument begins. The two facts are opposed and weighted evenly, which is antithesis, not irony: there is no gap here between what is said and what is meant, only two true figures pushed against each other."},
  {"para":3,"device":"Concession",
   "purpose":"The writer grants the strongest case for keeping the penny in full and in good faith: rounding lands on cash, and cash is used most by those with the least. Conceding this plainly, before answering it, is what lets the later turn read as fair rather than as a thumb on the scale. Tag the granted claim itself, not any signal word."},
  {"para":4,"device":"Anecdotal vs statistical evidence",
   "purpose":"To answer the concession the writer reaches for statistical evidence, studies of many transactions, rather than a single hard-luck story. The choice of evidence type is deliberate: a number drawn from many cases rebuts a worry about fairness more convincingly than one anecdote could, and it holds the register's sourced, disinterested tone."},
  {"para":4,"device":"Metaphor",
   "purpose":"Calling the penny a rounding error in the economy it was built to serve turns an abstract claim about irrelevance into a single concrete figure of speech. It is a metaphor, an implied identity with no like or as, and it carries the piece's verdict in a handful of words without the writer stating an opinion."},
 ],
 "mcq": [
  {"stem":"The relationship between the third paragraph and the fourth is best described as one in which the writer first",
   "options":[
     "raises the main objections to the penny, then concedes that they are valid",
     "grants the strongest case for keeping the penny, then turns the evidence against it",
     "states a personal preference for the penny, then supports it with statistics",
     "presents two competing studies, then explains why their findings conflict"],
   "answer":"B",
   "rationale":"Paragraph 3 makes the best case for keeping the penny (rounding as a tax on cash buyers, sentiment, charity); paragraph 4 opens with 'The evidence has not been kind to that case' and answers it with data. That is concession followed by an evidence-driven turn. The piece does not raise objections to the penny and then call them valid (that reverses which side paragraph 3 takes); it states no personal preference, since the register stays disinterested; and it offers one line of evidence, not two studies in conflict."},
  {"stem":"In context, the final sentence ('The American penny stays in production, by default rather than decision') primarily serves to",
   "options":[
     "predict that Congress will vote to eliminate the coin in the near future",
     "credit lawmakers with deliberately preserving a familiar tradition",
     "concede that the penny still serves a genuine practical purpose",
     "frame the penny's survival as the result of inaction rather than deliberate choice"],
   "answer":"D",
   "rationale":"The close caps a paragraph about inertia (no act of Congress, the Mint striking at a loss, lobbying) and names the cause of the penny's survival as default, not decision. The text makes no prediction about a future vote; it does not credit lawmakers with deliberate preservation (the point is that no decision was made); and it does not concede a practical purpose, since paragraph 4 has just shown the practical case failing."},
 ],
 "discussion": [
  "The writer never says outright that the penny should be abolished, yet most readers finish the piece thinking it should. How does building the case almost entirely from costs, precedents, and figures, rather than from open argument, shape the way the conclusion lands?",
  "Paragraph 3 spends its length making the best case for keeping the penny before paragraph 4 answers it. What does the writer gain by stating the opposing case fairly, and at length, first?",
 ],
 "sample_responses": [
  "A strong answer notes that by withholding an explicit 'should,' the writer makes the conclusion feel discovered rather than argued. The named body (the Mint), the dated figures (above face value since 2006), and the foreign precedent (Canada) do the persuading, so the reader reaches the verdict and credits it to the evidence rather than to the writer's opinion. The restraint is the persuasion.",
  "By granting that rounding can fall hardest on cash users and that the coin carries real attachment, the writer removes the easy charge of bias. Having been fair to the other side, the statistical turn in paragraph 4 reads as a correction of the record rather than a partisan jab, which makes it much harder to wave away.",
 ],
 "writing": {"type":"homework or extended in-class, Q2 rhetorical analysis",
  "text":"Read the opener closely and write an essay analyzing the rhetorical choices the writer makes to build a case against the penny while appearing only to report on it. Consider the writer's use of attribution, figures, concession, and tone."},
 "misconceptions": [
  "Students may call the contrast in paragraph 1 (a coin worth one cent that costs nearly three to make) irony. It is closer to antithesis: two opposed facts set in balanced form. Reserve irony for a gap between what is said and what is meant.",
  "Students often read paragraph 3 as the writer's real position because it argues for the penny. It is a concession: the writer grants the opposing case in good faith in order to answer it in paragraph 4, not to endorse it.",
  "Students may treat 'the coin has become a rounding error' as a literal accounting term. In context it is a metaphor for irrelevance: the penny now matters about as little as a sum too small to bother counting.",
  "Students may assume the second multiple-choice answer is wrong because the closing line sounds neutral. Its job is to characterize the penny's survival as the product of inaction, which is exactly what 'by default rather than decision' states.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a clean model of persuasion by restraint, where attribution, dated figures, and a fairly stated concession do the arguing in place of overt opinion. Good for teaching antithesis versus irony, a concession that precedes a turn, and the deliberate choice of statistical over anecdotal evidence.",
}

# ============================================================ 2. THE TRIBUTE
tribute = {
 "base": "Caught Up AI Opener - 2026-06-06 - Free to All (The Tribute)",
 "edition": EDITION, "date": DATE,
 "headline": "Free to All",
 "body": [
  "There is a building in almost every town that will take you in and ask for nothing. [[1]]You do not have to buy anything. You do not have to believe anything. You do not have to be anyone in particular.[[/1]] You walk in, and you are simply welcome. We built thousands of them, in nearly every town, and then half forgot that we had.",
  "Think of who is inside on a cold afternoon. A child carries a stack of books taller than her arms. A man with nowhere warmer to be reads the paper front to back, because the room is his too. Someone fills out the forms that will decide a year of their life, and a librarian leans in to help, for nothing. [[2]]It is the smallest thing a town builds, and close to the largest in what it hands out.[[/2]]",
  "The promise is strange when you say it plainly. Walk in with a question, any question, and a person whose job is to care about the answer will help you find it. [[3]]The library does not ask whether the question is worth asking.[[/3]] A scholar and a kid doing a report on volcanoes get the same patient attention and the same chair. The building keeps no record of which of them deserved it.",
  "And it does all this quietly, [[4]]without a slogan, without a campaign, without anyone needing to be persuaded[[/4]] that a warm room and a free book and a person who knows where to look might be worth keeping, which is perhaps why it has been so easy to let the hours shrink and the branches dim while we were busy admiring louder things. The library has never been good at selling itself.",
  "So before we let it go without thanks, it is worth saying plainly what it was: a place that believed, in brick and oak and a stamped card, that a person's worth did not depend on their purse. We will not build many things like that again. The lights are still on, in most towns, for now.",
 ],
 "devices": [
  {"para":1,"device":"Anaphora",
   "purpose":"The three sentences open on the same phrase ('You do not have to'), and each completes it with a larger surrender: buy, believe, be anyone. Because the repeated words sit at the START of successive sentences, this is anaphora, not parallelism, and the rising order, from a purchase to a person's whole identity, builds the welcome from small to total."},
  {"para":2,"device":"Antithesis",
   "purpose":"The smallest thing a town builds, and close to the largest in what it hands out sets small against large in balanced form. The antithesis compresses the tribute's whole claim, that a modest civic building gives out something close to immeasurable, into one line whose shape the reader can feel."},
  {"para":3,"device":"Personification",
   "purpose":"Giving the building human acts (the library does not ask whether the question is worth asking) is personification. It lets the writer credit the institution itself with the welcome and the lack of judgment, so the value seems to live in the place rather than in any single librarian."},
  {"para":4,"device":"Parallelism",
   "purpose":"The repeated frame 'without a slogan, without a campaign, without anyone needing to be persuaded' lines up three things the library never does to promote itself. Because the repeated structure sits inside the sentence rather than opening successive sentences, it is parallelism, not anaphora, and the accumulation quietly explains how something this useful could be so easy to overlook."},
 ],
 "mcq": [
  {"stem":"In the first paragraph, the repetition of 'You do not have to' (buy anything, believe anything, be anyone in particular) primarily serves to",
   "options":[
     "list the specific services the library provides to its visitors",
     "criticize people who expect public spaces to charge a fee",
     "convey that the library places no condition of any kind on who may enter",
     "trace the steps a visitor follows to obtain a library card"],
   "answer":"C",
   "rationale":"The escalating repetition strips away conditions one by one (commerce, belief, identity) to establish an unconditional welcome. It does not list services, since none are named; it does not criticize people, since no one is faulted; and it does not trace a procedure for getting a card, which the paragraph never describes."},
  {"stem":"Which of the following best characterizes the writer's overall stance toward the public library?",
   "options":[
     "reverent esteem for an institution the writer treats as plainly worth keeping",
     "cautious optimism that the library can modernize enough to survive",
     "a balanced weighing of the library's costs against its public benefits",
     "nostalgic regret for an institution the writer says has already vanished"],
   "answer":"A",
   "rationale":"The piece consecrates the library as a settled good, anchoring its worth in concrete scenes rather than arguing for it. There is no optimism about modernizing to survive (the text never raises modernization); no claim that the library has already vanished (the lights are 'still on, for now'); and no balanced cost-benefit weighing, which a tribute deliberately avoids."},
 ],
 "discussion": [
  "The writer praises the library entirely through concrete scenes (a child with a stack of books, a man with nowhere warmer to be) rather than through adjectives like 'important' or 'valuable.' What does the piece gain by showing the library's worth this way instead of asserting it?",
  "The closing line says the lights are 'still on, in most towns, for now.' How do those three small qualifications change the feeling of the ending, even though the writer never issues a warning or a call to action?",
 ],
 "sample_responses": [
  "By rooting each value-claim in a scene, the writer lets the reader feel the worth and reach the judgment, which is more persuasive than being told the library matters. The man reading the paper in the warm room proves the claim that the place asks nothing of anyone, so the abstraction (a place free to all) arrives already cashed out in a person.",
  "The qualifications quietly carry the loss the piece never states. 'Still' and 'for now' admit the lights could go off; 'in most towns' admits some already have. The restraint lets the reader supply the alarm, so the ending consecrates the library and mourns it at once, without lecturing.",
 ],
 "writing": {"type":"homework or extended in-class, Q2 rhetorical analysis",
  "text":"Write an essay analyzing how the writer uses concrete detail, repetition, and a restrained tone to honor the public library and to suggest, without ever stating it, that the institution is at risk."},
 "misconceptions": [
  "Students often call the repeated 'You do not have to...' parallelism. It is anaphora: the repeated phrase opens each successive sentence. Reserve parallelism for repeated structure that does not begin the clause, like the 'without a slogan, without a campaign' series in paragraph 4.",
  "Students may take lines like 'the library does not ask whether the question is worth asking' literally. The library cannot ask anything; this is personification, giving the building a human judgment it then declines to make.",
  "Students may look for an opposing side the writer argues against. There is none. A tribute consecrates a settled worth; it does not rebut critics, so reading paragraph 2 as a rebuttal misreads the register.",
  "Students may assume the correct stance answer must mention the library's problems. The piece never weighs costs and benefits; it consecrates, so the best answer names reverent esteem, not balance.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a compact model of praise built from concrete scenes rather than adjectives. Useful for teaching anaphora versus parallelism within a single piece, personification of an institution, and antithesis that compresses a claim. The long accumulation sentence set against short buttons is a clean lesson in cadence.",
}

# ============================================================ 3. THE LONG LOOK
longlook = {
 "base": "Caught Up AI Opener - 2026-06-06 - No Bird in Charge (The Long Look)",
 "edition": EDITION, "date": DATE,
 "headline": "No Bird in Charge",
 "body": [
  "At dusk in late autumn the starlings gather above their roost and begin to move as one body. There may be a thousand of them, or fifty thousand. The flock [[1]]climbs, folds, pours sideways, thins to a gray ribbon, knots into a fist[[/1]]. [[2]]It has no leader.[[/2]] No single bird decides the shape, and none is told it.",
  "How a crowd that large turns without colliding was a real puzzle until recently. The current answer is that each bird is not watching the whole flock at all, but only its handful of nearest neighbors, about seven of them, matching their speed and heading whatever the distance between them. A turn begun at one edge passes inward, neighbor to neighbor, so a ripple of banking can cross the entire flock faster than any one starling flies. The order is real, and it is built entirely from the bottom.",
  "The effect is sharpest when a predator arrives. [[3]]A peregrine falcon stoops at the edge, and the flock answers not by scattering but by tightening, the threatened side pulling inward so fast it darkens like a bruise spreading under skin.[[/3]] [[4]]Thousands of separate animals, and not one collision; total panic, and perfect order.[[/4]] The falcon, built to pick a single target, loses the single target in the boil of bodies.",
  "Why they do it at all is not fully settled. The safety of the crowd is part of it, surely; but researchers have also tied the evening gatherings [[5]]to warmth, to the trading of word about where the food was that day, to the simple pull of a good roost, and to reasons no one has yet named[[/5]]. The murmuration is not a decision and not a message. It is what happens when ten thousand small rules, each followed by a bird watching only its neighbors, add up in the cold air over a winter field.",
  "From the ground it looks like a single mind choosing where to go. [[6]]There is no mind, and there is nothing choosing; there is only each bird, and its seven neighbors, and the dusk coming on.[[/6]]",
 ],
 "devices": [
  {"para":1,"device":"Asyndeton",
   "purpose":"The piled verbs with the conjunctions stripped out (climbs, folds, pours sideways, thins to a gray ribbon, knots into a fist) speed the line so its rhythm imitates the quick, continuous changing of the flock. Dropping the and's is asyndeton; compare the deliberate opposite in the final paragraph."},
  {"para":1,"device":"Telegraphic sentence",
   "purpose":"It has no leader is four words, dropped hard after a long accumulating sentence. The telegraphic sentence lands the central fact of the whole piece with maximum emphasis precisely because it is so short against what comes before it."},
  {"para":3,"device":"Simile",
   "purpose":"Darkens like a bruise spreading under skin compares the fast inward turn of the threatened flock to a spreading bruise. The like makes it a simile, not a metaphor, and it is chosen for precision: it renders the speed and the spreading at once, without claiming the birds are hurt."},
  {"para":3,"device":"Antithesis",
   "purpose":"Thousands of separate animals, and not one collision; total panic, and perfect order is built on two opposed pairs held in balance. It is antithesis rather than plain parallelism because the force of the line is the contradiction it names: chaos and order in the same instant."},
  {"para":4,"device":"Parallelism",
   "purpose":"The series to warmth, to the trading of word..., to the simple pull of a good roost, and to reasons no one has yet named repeats the same grammatical shape to pile up possible causes. The repeated structure sits inside the sentence, so it is parallelism, not anaphora, and the accumulation enacts how many reasons may be at work at once."},
  {"para":5,"device":"Polysyndeton",
   "purpose":"The closing only each bird, and its seven neighbors, and the dusk coming on adds and's where none are needed. This is polysyndeton, the deliberate opposite of the asyndeton in the first paragraph: the extra conjunctions slow the line to a stop and give each of the three plain things its own weight."},
 ],
 "mcq": [
  {"stem":"In the third paragraph, the comparison of the tightening flock to 'a bruise spreading under skin' primarily serves to",
   "options":[
     "suggest that the flock has been injured by the diving falcon",
     "give the flock's sudden, spreading reaction a precise and physical image",
     "register the writer's sympathy for the hunted birds",
     "compare the starlings unfavorably with their predator"],
   "answer":"B",
   "rationale":"The simile translates an abstract speed-and-spread into something the reader can see. Reading the bruise as a real injury is the too-literal trap; the sympathy reading imports a feeling the observational register never states; and the unfavorable comparison invents a contrast the line does not make."},
  {"stem":"The writer follows the long sentence describing the flock's motion with the short sentence 'It has no leader.' This juxtaposition primarily functions to",
   "options":[
     "stress that the flock's intricate order arises without anything directing it",
     "signal that the writer will next explain how a leader is chosen",
     "concede that the flock's movements are ultimately random",
     "summarize a scientific debate introduced earlier in the passage"],
   "answer":"A",
   "rationale":"The blunt short sentence lands hard against the long one, setting the flock's visible order against the absence of any director. The passage insists there is no leader, so the reading that a leader will be explained is inverted; the piece argues for order, not randomness; and the debate appears later, in paragraph 4, so there is nothing earlier to summarize."},
 ],
 "discussion": [
  "The writer describes the murmuration almost entirely through precise physical detail and never once calls it beautiful or amazing. How does withholding those words change the way the wonder of the scene reaches the reader?",
  "Twice the writer admits the science is unsettled ('was a real puzzle until recently,' 'reasons no one has yet named'). How does admitting what is not known affect your trust in the writer as an observer?",
 ],
 "sample_responses": [
  "By refusing the adjectives, the writer makes the reader do the marveling. The accumulating verbs (climbs, folds, pours, thins, knots) and the falcon losing its target in 'the boil of bodies' enact the wonder, so the awe feels earned by the facts rather than asserted. Telling the reader it is amazing would shrink the effect, because the reader would receive a claim instead of seeing the thing.",
  "Admitting the limits of the science makes the writer more credible, not less. An observer who claims to have explained everything invites doubt; one who says the safety theory is only 'part of it' and that some reasons are still unnamed sounds like someone reporting honestly from inside a real question. The candor signals that the precise claims, like the seven neighbors, can be trusted because the writer marks where the knowledge stops.",
 ],
 "writing": {"type":"homework or extended in-class, Q2 rhetorical analysis",
  "text":"Write an essay analyzing how the writer uses imagery, sentence variety, and a restrained, observational tone to convey the wonder and the order of a starling murmuration without ever asserting that it is wondrous."},
 "misconceptions": [
  "Students often label both list-sentences the same way. Paragraph 1's 'climbs, folds, pours sideways...' is asyndeton: the conjunctions are dropped to speed the rhythm. Paragraph 5's 'each bird, and its seven neighbors, and the dusk coming on' is polysyndeton: the extra and's slow it down. The two are opposites, not the same device.",
  "Students may read 'darkens like a bruise spreading under skin' as a claim that the birds are hurt. It is a simile for the speed and spread of the flock's turn, not a literal injury.",
  "Students may call 'Thousands of separate animals, and not one collision; total panic, and perfect order' parallelism. The point of the line is the opposition between its halves, so it is antithesis: contrasting ideas set in balanced form.",
  "Students may treat the short sentence 'It has no leader' as throwaway. It is a telegraphic sentence placed for emphasis, landing the piece's central fact hard against the long sentence before it.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a clean model of wonder conveyed through precise detail rather than asserted with adjectives. Strong for teaching asyndeton against polysyndeton, a simile read in context rather than literally, antithesis as a structural engine, and the telegraphic sentence as emphasis. The wide swing between short declaratives and long accumulating sentences is a clear lesson in how sentence length creates effect.",
}

# ============================================================ render
if __name__ == "__main__":
    import os
    for piece in (ledger, tribute, longlook):
        randomize_answers(piece)
        for role in ("Teacher", "Student"):
            fn, pages = build(piece, role)
            print("wrote: %s  (%d page%s)  answers %s"
                  % (os.path.basename(fn), pages, "" if pages == 1 else "s",
                     [it["answer"] for it in piece["mcq"]]))
