export const meta = {
  name: 'opener-batch-generate',
  description: 'Generate + adversarially verify 28 Caught Up AI openers from a locked matrix',
  phases: [
    { title: 'Source', detail: 'numbered fact list (R: live-sourced 2+ independent) or persona material' },
    { title: 'Draft', detail: 'register prose + friction layer + device tags + full AP apparatus' },
    { title: 'Verify', detail: 'adversarial accuracy/devices/MCQ/mechanical checks, redraft once on fail' },
    { title: 'Cross-check', detail: 'batch-level cross-piece sameness audit' },
  ],
}

const SPECDIR = 'C:/Users/srlev/OneDrive/Documents/Claude/AI Brain 1.0/10_Projects/Caught Up AI'
const F = {
  reg: `${SPECDIR}/Register-Specs.md`,
  pal: `${SPECDIR}/Style-Palette.md`,
  tpl: `${SPECDIR}/Structural-Templates.md`,
  tell: `${SPECDIR}/Anti-Tell-List.md`,
  dev: `${SPECDIR}/Rhetorical-Device-Vocabulary.md`,
  mcq: `${SPECDIR}/MCQ-Construction-Spec.md`,
  acc: `${SPECDIR}/Accuracy-Guardrail.md`,
  same: `${SPECDIR}/Cross-Piece-Sameness-Rubric.md`,
}
const DATE = 'Sunday, June 7, 2026'
const ISO = '2026-06-07'

const openers = [
{"id":1,"register":"Ledger","basis":"R","topic":"The gap between the headline U-3 unemployment rate (4.3%) and the broader U-6 underemployment measure (8.1%) in the May 2026 BLS release.","angle":"Adjudicate which unemployment measure best captures labor-market reality, and what the headline number routinely conceals about slack.","addressee":"","persona_concept":"","candidate_sources":["BLS Employment Situation, May 2026 release (bls.gov, June 5 2026)","Center for American Progress, analysis of May 2026 jobs numbers and labor-market slack"],"template":"Finding-First / Claim-First Build","open_type":"stat-lead","close_type":"placement/benediction","rhythm_target":"level finding-first, ordered situation-cause-scope, plain status close","fit_rationale":"A disputed, widely misunderstood official record a reasonable person needs adjudicated, with two independent verifiable sources; pure Ledger."},
{"id":2,"register":"Reckoning","basis":"R","topic":"Florida's June 1, 2026 lawsuit naming OpenAI CEO Sam Altman personally, alleging the company marketed ChatGPT as safe for children while concealing internal safety warnings.","angle":"A named culprit and a datable filing: hold the personal-liability claim against the company's own safety promises and force the reader to feel the stake.","addressee":"","persona_concept":"","candidate_sources":["NPR, OpenAI Florida lawsuit on ChatGPT child safety (June 1 2026)","Washington Post, Florida lawsuit accuses OpenAI CEO Sam Altman of endangering children (June 1 2026)"],"template":"Periodic-Build-to-a-Button","open_type":"address/occasion","close_type":"charge/obligation","rhythm_target":"long suspended runway of the company's own promises, hard short button","fit_rationale":"Nameable responsible party (Altman) plus a datable trigger (June 1 filing) and a clear public moral stake; satisfies the Reckoning hard gate with two independent sources."},
{"id":3,"register":"Long Think","basis":"R","topic":"The tension between AI innovation velocity and institutional accountability as multiple 2026 state and federal AI frameworks (NY, CA, CO) take effect.","angle":"Reframe the durable question of speed versus reversibility: when efficiency is promised, what is quietly traded away in haste, and can both goods be honored at once?","addressee":"","persona_concept":"","candidate_sources":["White House National Policy Framework for AI (March 20 2026)","NY Governor's office, RAISE Act AI frameworks legislation; Cooley, 2026 state AI laws status (April 2026)"],"template":"Antithesis-as-Engine","open_type":"concede-first","close_type":"inward-turn","rhythm_target":"even reasoning on one axis (speed vs reversibility), one sharp hinge, short snap","fit_rationale":"A perennial human theme (speed vs. safety, reversibility) sitting behind specific current AI-policy news; reasons to a reframed tension, two independent sources."},
{"id":4,"register":"Open Letter","basis":"R","topic":"OMB Director Russell Vought's withholding of roughly $2 billion in congressionally approved education funding via executive apportionment as of June 1, 2026.","angle":"Hold Vought to his own stated commitment to constitutional governance by appealing to the prohibition on executive impoundment, quoting his principles back at him.","addressee":"Russell Vought, Director of the Office of Management and Budget","persona_concept":"","candidate_sources":["Education Week, White House blocks $2 billion for education programs (May 2026)","Education Week, Trump holds back $2 billion for education grants, what happens next (May 2026)"],"template":"Periodic-Build-to-a-Button","open_type":"address/occasion","close_type":"charge/obligation","rhythm_target":"deferential periodic suspension, semicolon-articulated, resolving to a request","fit_rationale":"A real named, more-powerful addressee held to his own stated values on a recent datable occasion; periodic-build suits the Open Letter, two independent sources."},
{"id":5,"register":"Witness Stand","basis":"R","topic":"A parent waits with a child born with esophageal atresia as a charity-funded team announces a lab-grown esophagus that could heal without immunosuppression.","angle":"The lived experience of medical waiting and fragile hope, voiced by a persona who can credibly say I have stood in that corridor.","addressee":"","persona_concept":"A parent who has spent months in hospital corridors with a child unable to eat normally, now reading of a tissue-engineering breakthrough.","candidate_sources":["Great Ormond Street Hospital Charity, team engineers first lab-grown oesophagus (March 2026)","UCL News, engineered tissue offers hope to babies born missing food-pipe section (March 2026)"],"template":"Narrative-into-Claim","open_type":"in-scene","close_type":"placement/benediction","rhythm_target":"warm conversational, one long looping corridor-scene sentence, short portable close","fit_rationale":"A current marvel touching a shared human experience where a first-person persona credibly stands; persona invented but the science is real and double-sourced."},
{"id":6,"register":"Tribute","basis":"R","topic":"The death of Hall of Fame NBA coach Rick Adelman, winner of more than 1,000 games, on June 1, 2026.","angle":"Consecrate a life of quiet, durable excellence built on consistency and respect rather than flash, placing him in the longer history of the game.","addressee":"","persona_concept":"","candidate_sources":["NBA.com, Hall of Fame coach Rick Adelman, winner of more than 1,000 games, dies at 79 (June 1 2026)","Washington Post, Rick Adelman obituary (June 1 2026)"],"template":"Antithesis-as-Engine","open_type":"flat-fact","close_type":"placement/benediction","rhythm_target":"balanced antithesis of small flash vs large substance, quiet benediction","fit_rationale":"A real recent death of an established milestone figure, an occasion to honor with no culprit; small-flash-versus-large-substance antithesis suits Tribute, two sources."},
{"id":7,"register":"Long Look","basis":"R","topic":"The Artemis II lunar flyby of April 2026, humanity's first crewed return toward the Moon since 1972, carrying the first woman and first non-U.S. citizen beyond low Earth orbit.","angle":"Render the engineering and the system that closed a fifty-year gap, building awe through accumulating technical specifics rather than declaration.","addressee":"","persona_concept":"","candidate_sources":["NASA, Liftoff: NASA launches astronauts on historic Artemis Moon mission (April 2026)","NASA, Artemis II flight day 6 crew wraps historic lunar flyby (April 6 2026)"],"template":"Accumulation under a Repeated Frame","open_type":"named-actor-verb","close_type":"inward-turn","rhythm_target":"short flat declarative then long accumulating technical elaboration","fit_rationale":"A genuine current marvel and how-it-works story with no conflict or blame; accumulation fits Long Look, two independent NASA-primary sources."},
{"id":8,"register":"Ledger","basis":"R","topic":"The Department of Education's admission that a May 2026 report overstated pending student-loan IDR applications by nearly 336,000 because of a servicer data error; the backlog was revised.","angle":"Adjudicate which backlog figure is true and what the correction reveals about the accuracy of benefit administration.","addressee":"","persona_concept":"","candidate_sources":["NASFAA, data error shows slow progress toward IDR application backlog processing (June 2026)","Federal Student Aid / GetOutOfDebt reporting on corrected IDR backlog (June 2026)"],"template":"Dialectic (Reason-Forward from Shared Premises)","open_type":"flat-fact","close_type":"placement/benediction","rhythm_target":"level chain of shared premises, one step at a time, flat status close","fit_rationale":"A factual record under correction where the reader needs the true figure adjudicated; Ledger gate met, two independent sources, distinct from slot 1."},
{"id":9,"register":"Reckoning","basis":"R","topic":"KPMG Australia CEO Andrew Yates and audit head Julian McPherson resigned in late May 2026 amid whistleblower allegations they misused confidential client board papers to win audit contracts.","angle":"Name the two executives and the May 29 resignation trigger, pressing the breach of professional trust as a public accountability stake.","addressee":"","persona_concept":"","candidate_sources":["The New Daily, KPMG boss quits (May 29 2026)","Investing.com, corporate regulator investigating KPMG Australia partners over audit leak scandal (June 2026)"],"template":"Statistic-to-Scene Pivot","open_type":"named-actor-verb","close_type":"charge/obligation","rhythm_target":"pivot between the figure and the breach, fronted fact, hard charge close","fit_rationale":"Two nameable culprits plus a datable trigger and a clear ethics breach; satisfies the Reckoning gate with two independent sources, distinct from slot 2."},
{"id":10,"register":"Long Think","basis":"R","topic":"The paradox of media-literacy curricula as a response to misinformation in an attention-capture economy, amid 2026 reporting that literacy efforts lag.","angle":"Withhold the easy answer (more education) and reframe: is teaching students to spot fakes addressing the real scarcity, attention itself as the exploited resource?","addressee":"","persona_concept":"","candidate_sources":["Education Week, why media-literacy efforts are failing to keep up with misinformation (Feb 2026)","MSU Today, teaching students media literacy (April 2026)"],"template":"Problem-Reframe (Redefinition-as-Engine)","open_type":"concede-first","close_type":"inward-turn","rhythm_target":"unhurried redefinition of the problem, one discovering sentence, short snap","fit_rationale":"A perennial theme (attention) behind current education news, reframing a settled-seeming question; Long Think gate met, two independent sources, distinct from slot 3."},
{"id":11,"register":"Open Letter","basis":"R","topic":"The Supreme Court's Louisiana v. Callais decision (April 29, 2026) weakening Section 2 of the Voting Rights Act weeks before the 2026 midterms.","angle":"Hold Chief Justice Roberts to his own prior statements on deference to congressional fact-finding, quoting his words back as the Court narrows the Act.","addressee":"Chief Justice John G. Roberts Jr., United States Supreme Court","persona_concept":"","candidate_sources":["NPR, Supreme Court Voting Rights Act and state redistricting (June 5 2026)","NBC News, Supreme Court criticism over redistricting and 2026 voting rights (2026)"],"template":"Withheld-Turn","open_type":"address/occasion","close_type":"charge/obligation","rhythm_target":"deferential build that names the expected deference then declines it, request close","fit_rationale":"A named, more-powerful addressee held to his own words on a recent datable decision; Withheld-Turn suits Open Letter, two independent sources, distinct addressee from slot 4."},
{"id":12,"register":"Witness Stand","basis":"E","topic":"Losing a lifelong friendship in adulthood, not through rupture but through accumulated distance, and what it teaches about belonging and forgiveness.","angle":"A narrator learns that some people move through a life in seasons rather than forever, and that acceptance is its own quiet form of affection.","addressee":"","persona_concept":"An adult looking back on a friendship that quietly ended, holding both the gift and the grief without bitterness.","candidate_sources":[],"template":"Problem-Reframe (Redefinition-as-Engine)","open_type":"in-scene","close_type":"inward-turn","rhythm_target":"warm looping middle redefining belonging, clipped landing line","fit_rationale":"Persona-driven evergreen Witness Stand on a universal human experience; no hard facts required, redefines belonging, distinct from slot 5's medical story."},
{"id":13,"register":"Tribute","basis":"R","topic":"The death of Marjane Satrapi, Iranian-French cartoonist and filmmaker whose Persepolis gave a generation language for identity and exile, on June 4, 2026.","angle":"Consecrate a life spent bearing witness across two countries, placing her work in the longer history of graphic literature and film.","addressee":"","persona_concept":"","candidate_sources":["Euronews, Marjane Satrapi, French-Iranian author of Persepolis, dies aged 56 (June 4 2026)","Al Jazeera, French-Iranian Persepolis author Marjane Satrapi dies (June 5 2026)"],"template":"Narrative-into-Claim","open_type":"flat-fact","close_type":"placement/benediction","rhythm_target":"a small Satrapi scene opened to significance, quiet benediction","fit_rationale":"A real recent death of an established cultural figure, an occasion to honor; Narrative-into-Claim is the Tribute signature, two independent sources, distinct from slot 6."},
{"id":14,"register":"Long Look","basis":"E","topic":"How a wetland sustains itself: the intricate exchange of water, nutrients, and species across seasons, and why draining a marsh cascades through a whole landscape.","angle":"Render the marsh as a system of flow and feedback, building awe through accumulating specificity rather than emotional declaration.","addressee":"","persona_concept":"","candidate_sources":["Mitsch, W. J., and Gosselink, J. G. (2015). Wetlands (5th ed.). Wiley.","Verhoeven, J. T. A., and Meuleman, A. F. M. (1999). Wetlands for wastewater treatment. Hydrobiologia."],"template":"Antithesis-as-Engine","open_type":"abstract-claim","close_type":"inward-turn","rhythm_target":"controlling antithesis (drain vs sustain) in clipped declaratives against long lists","fit_rationale":"An evergreen natural marvel illuminated without argument or blame; Long Look gate met, stable science sources, distinct from slot 7's space story."},
{"id":15,"register":"Ledger","basis":"R","topic":"Year-over-year inflation figures flattered by the October 2025 government-shutdown data gap, with the adjusted April 2026 CPI reading running higher than the headline 3.8%.","angle":"Adjudicate which inflation figure captures reality when a methodological artifact distorts the year-over-year comparison.","addressee":"","persona_concept":"","candidate_sources":["BLS, Consumer Price Index news release (bls.gov)","Investing.com, why the 2026 CPI is misleading: the shutdown distortion explained"],"template":"Concession-then-Rebuttal","open_type":"stat-lead","close_type":"placement/benediction","rhythm_target":"level survey, full concession then a qualifying turn, flat close","fit_rationale":"A widely misunderstood statistical record where the headline misleads; Ledger gate met, two independent sources, distinct economic record from slots 1 and 8."},
{"id":16,"register":"Reckoning","basis":"R","topic":"A federal watchdog report released June 6, 2026 found agencies made roughly $186 billion in improper payments in fiscal 2026, with seven agencies exceeding 10% error rates.","angle":"Name the responsible agencies and the June 6 report trigger, pressing the scale of the failure as a public accountability charge.","addressee":"","persona_concept":"","candidate_sources":["Washington Times, federal agencies made $186 billion in improper payments last year (June 6 2026)","Government Accountability Office improper-payments data (gao.gov)"],"template":"Escalating Exemplification","open_type":"flat-fact","close_type":"charge/obligation","rhythm_target":"examples growing in scale and stakes to a hard charge","fit_rationale":"Named institutions plus a datable report trigger and measurable public harm; Reckoning gate met, two independent sources, distinct from slots 2 and 9."},
{"id":17,"register":"Long Think","basis":"R","topic":"The limits of protective authority when adults ban books to safeguard children from difference, amid 2025-2026 record challenge data.","angle":"Grant the protective impulse genuine standing, then reframe the durable question: protecting children from harm, or from the discomfort of encountering difference, and at what long-term cost.","addressee":"","persona_concept":"","candidate_sources":["American Library Association, book-ban data (4,235 titles challenged in 2025)","PEN America, school book-ban report (2024-2025 school year, released May 2026)"],"template":"Dialectic (Reason-Forward from Shared Premises)","open_type":"concede-first","close_type":"inward-turn","rhythm_target":"reason forward from the protective premise to an earned, uncomfortable turn","fit_rationale":"A perennial theme (freedom, what we owe the next generation) behind current data; Long Think gate met, two independent sources, distinct from slots 3 and 10."},
{"id":18,"register":"Open Letter","basis":"R","topic":"President Trump's January 2025 executive order seeking to end birthright citizenship, with a Supreme Court ruling expected by June 30, 2026.","angle":"Reframe the order not as immigration policy but as an attempted constitutional violation, holding Trump to his stated commitment to constitutional governance.","addressee":"President Donald Trump","persona_concept":"","candidate_sources":["NPR, Trump, Supreme Court, and birthright citizenship arguments (April 1 2026)","ACLU, Supreme Court arguments wrap in challenge to Trump birthright-citizenship executive order"],"template":"Concession-then-Rebuttal","open_type":"address/occasion","close_type":"charge/obligation","rhythm_target":"concede the immigration concern, then bind on the constitutional principle, charge close","fit_rationale":"A named, more-powerful addressee held to stated principles on an imminent datable occasion; concede-then-bind Open Letter, two independent sources, distinct addressee from slots 4 and 11."},
{"id":19,"register":"Witness Stand","basis":"E","topic":"Code-switching between home and work, and what shifting language and tone across contexts reveals about identity and belonging.","angle":"A narrator with a multilingual background traces what is gained and lost in each register, redefining the self that appears in each.","addressee":"","persona_concept":"A bilingual or multicultural professional reflecting on the languages they speak and the self they become in each setting.","candidate_sources":[],"template":"Withheld-Turn","open_type":"in-scene","close_type":"inward-turn","rhythm_target":"name the expected lesson, decline it, substitute the lived one; long-then-clipped","fit_rationale":"Persona-driven evergreen Witness Stand on language and belonging, a universal experience; distinct from slots 5 and 12, no current peg required for E variant."},
{"id":20,"register":"Tribute","basis":"E","topic":"A consecration of the handwritten letter as a surviving form of intimacy and attention in an age of instant messaging.","angle":"Honor the letter itself, a practice that demands slowing down and carries weight because it cannot be retracted, placing it in a longer history of how we mark affection.","addressee":"","persona_concept":"","candidate_sources":["Woolf, V. (1932). A Letter to a Young Poet. Hogarth Press.","Hampf, S. (2021). What Letters Could Do. Princeton Architectural Press."],"template":"Periodic-Build-to-a-Button","open_type":"abstract-claim","close_type":"placement/benediction","rhythm_target":"periodic cadenced suspension on the vanishing letter, quiet button","fit_rationale":"An enduring cultural form worth consecrating, no death or event required; Tribute E gate met, distinct from slots 6 and 13."},
{"id":21,"register":"Long Look","basis":"E","topic":"How coral builds its skeleton and sustains symbiosis with zooxanthellae through chemistry, light, and time in patterns repeating across millennia.","angle":"Describe the colony as a system of extraordinary precision where polyps construct architecture and exchange resources in choreography tuned to season and light.","addressee":"","persona_concept":"","candidate_sources":["Muscatine, L., and Falkowski, P. G. (1990). Coral-zooxanthellae symbiosis. In Z. Dubinsky (Ed.), Coral Reefs.","Veron, J. E. N. (2000). Corals of the World. Australian Institute of Marine Science."],"template":"Finding-First / Claim-First Build","open_type":"flat-fact","close_type":"inward-turn","rhythm_target":"finding-first flat declarative then patient accumulating detail, inward close","fit_rationale":"An evergreen biological marvel rendered without argument; Long Look E gate met, stable science sources, distinct from slots 7 and 14."},
{"id":22,"register":"Ledger","basis":"R","topic":"Insulin affordability in 2026: competing claims about whether headline price drops and the $35 federal cap represent genuine relief or mask persistent access barriers under three-manufacturer concentration.","angle":"Adjudicate what affordable actually means for most Americans as of mid-2026, separating the real but narrow cap from the fuller access picture.","addressee":"","persona_concept":"","candidate_sources":["Blue Cross Blue Shield, new era of lower-cost insulin","Baltimore Chronicle, how to save money on insulin in the USA 2026: new price caps and patient programs"],"template":"Statistic-to-Scene Pivot","open_type":"stat-lead","close_type":"placement/benediction","rhythm_target":"move between the $35 cap figure and the access scene, flat status close","fit_rationale":"A misunderstood metric where headline relief is disputed against access reality; Ledger gate met, two independent sources, distinct record from slots 1, 8, 15."},
{"id":23,"register":"Reckoning","basis":"R","topic":"A Boeing 787 nose-gear collapse at Frankfurt on June 4, 2026, against months of FAA audits flagging manufacturing defects in wing splice plates that can cause fatigue cracks.","angle":"Name Boeing's documented quality-control failures and the June 4 incident trigger, pressing accountability for known production risks.","addressee":"","persona_concept":"","candidate_sources":["InformedClearly, Boeing 787 nose-gear collapse at Frankfurt 2026 (June 4 2026)","FAA newsroom, FAA increasing oversight of Boeing production and manufacturing"],"template":"Antithesis-as-Engine","open_type":"flat-fact","close_type":"charge/obligation","rhythm_target":"one opposition held throughout (documented known risk vs continued production), hard charge close","fit_rationale":"A nameable responsible institution plus a datable trigger and documented prior warnings; Reckoning gate met, two independent sources, distinct from slots 2, 9, 16."},
{"id":24,"register":"Long Think","basis":"E","topic":"Why humans grow more risk-averse with age even though older adults often have fewer years to recover from losses.","angle":"Reframe the conventional wisdom that age means caution: explore how time horizon, reference points, and loss aversion reshape the calculus of risk across a lifespan.","addressee":"","persona_concept":"","candidate_sources":["Kahneman, D., and Tversky, A. (1979). Prospect Theory. Econometrica.","Maddox, W. T., et al. (2010). Aging and decision-making competence. Psychology and Aging."],"template":"Concession-then-Rebuttal","open_type":"concede-first","close_type":"inward-turn","rhythm_target":"concede the caution-with-age view, then turn on the reframed calculus, inward close","fit_rationale":"A pure evergreen theme (money, time, risk) with stable established research; Long Think E gate met, distinct from slots 3, 10, 17."},
{"id":25,"register":"Open Letter","basis":"E","topic":"A letter to architects and city planners asking them to honor their own stated commitment to human scale and livability against density-first pressures.","angle":"Hold the design profession to its own principles of walkability and community while granting the genuine urgency of the housing crisis that pushes toward density.","addressee":"Architects and urban planners (and their professional bodies)","persona_concept":"","candidate_sources":["Gehl, J. (2010). Cities for People. Island Press.","Duany, A., et al. (2000). Suburban Nation. North Point Press."],"template":"Periodic-Build-to-a-Button","open_type":"address/occasion","close_type":"charge/obligation","rhythm_target":"deferential periodic build to architects, request handed to them","fit_rationale":"A named enduring addressee/role held to an evergreen professional principle; Open Letter E gate met, distinct from slots 4, 11, 18."},
{"id":26,"register":"Witness Stand","basis":"E","topic":"Learning to work with one's hands as an adult, and how taking up a physical craft as a rank beginner redefined what competence means.","angle":"A lifelong white-collar narrator discovers that mastery differs across domains and that being a beginner again teaches humility and reshapes ambition.","addressee":"","persona_concept":"A skilled professional (writer, manager, or analyst) confronting their own incompetence in physical craft for the first time.","candidate_sources":["Crawford, M. B. (2009). Shop Class as Soulcraft. Penguin Press.","Sennett, R. (2008). The Craftsman. Yale University Press."],"template":"Escalating Exemplification","open_type":"in-scene","close_type":"placement/benediction","rhythm_target":"escalating beginner-failures to a humbling redefinition, benediction close","fit_rationale":"Persona-driven evergreen Witness Stand redefining competence through lived experience; distinct from slots 5, 12, 19."},
{"id":27,"register":"Tribute","basis":"E","topic":"A consecration of the town square or public plaza as the place where strangers meet and citizenship happens, against the retreat to private and digital spaces.","angle":"Honor the plaza as a radical democratic idea where no purchase is required to belong, placing it in a longer history of public life.","addressee":"","persona_concept":"","candidate_sources":["Gehl, J. (2010). Cities for People. Island Press.","Sennett, R. (2018). Building and Dwelling. Farrar, Straus and Giroux."],"template":"Accumulation under a Repeated Frame","open_type":"address/occasion","close_type":"placement/benediction","rhythm_target":"accumulating instances of plaza life under a repeated frame, quiet benediction","fit_rationale":"An enduring civic idea worth consecrating, no event required; Tribute E gate met, distinct from slots 6, 13, 20; separated from slot 25 by consecrating a place rather than petitioning a party."},
{"id":28,"register":"Long Look","basis":"E","topic":"How fermentation works at the microbial level: the chemistry of bacteria and fungi transforming food, the precision of temperature and time, and how a single living culture can remake a harvest.","angle":"Describe fermentation as a controlled partnership between human and microbe, rendering the invisible process with scientific detail and earned awe.","addressee":"","persona_concept":"","candidate_sources":["McGovern, P. E. (2009). Uncorking the Past. University of California Press.","Cziesla, E., et al. (2014). Fermentation Microbiology and Biotechnology. Woodhead Publishing."],"template":"Narrative-into-Claim","open_type":"in-scene","close_type":"inward-turn","rhythm_target":"open on a concrete fermenting vessel, accumulate the chemistry, inward close","fit_rationale":"An evergreen craft-and-biology marvel rendered without argument; Long Look E gate met, stable sources, distinct from slots 7, 14, 21 (description-into-meaning variant)."}
]
if (!openers.length) throw new Error('no openers embedded')

// ---------------- schemas ----------------
const SOURCE_SCHEMA = {
  type:'object', additionalProperties:false, properties:{
    id:{type:'integer'}, basis:{type:'string'}, topic_final:{type:'string'},
    fact_list:{type:'array', items:{type:'object', additionalProperties:false, properties:{
      n:{type:'integer'}, fact:{type:'string'},
      sources:{type:'array', items:{type:'string'}},
      primary:{type:'boolean'}, flag:{type:'string'}
    }, required:['n','fact','sources','primary','flag']}},
    persona_material:{type:'string'}, sourcing_notes:{type:'string'}, classroom_safe:{type:'boolean'}
  }, required:['id','basis','topic_final','fact_list','persona_material','sourcing_notes','classroom_safe']
}

const SCAN = {type:'object', additionalProperties:false, properties:{
  first_sentence:{type:'string'}, last_sentence:{type:'string'}, para_count:{type:'integer'},
  approx_sentence_mean:{type:'number'}, device_count:{type:'integer'},
  opener_bucket:{type:'string'}, close_bucket:{type:'string'}, spine:{type:'string'}
}, required:['first_sentence','last_sentence','para_count','approx_sentence_mean','device_count','opener_bucket','close_bucket','spine']}

const DRAFT_SCHEMA = {
  type:'object', additionalProperties:false, properties:{
    base:{type:'string'}, edition:{type:'string'}, date:{type:'string'}, headline:{type:'string'},
    body:{type:'array', items:{type:'string'}},
    devices:{type:'array', items:{type:'object', additionalProperties:false, properties:{
      para:{type:'integer'}, device:{type:'string'}, purpose:{type:'string'}
    }, required:['para','device','purpose']}},
    mcq:{type:'array', items:{type:'object', additionalProperties:false, properties:{
      stem:{type:'string'}, options:{type:'array', items:{type:'string'}},
      answer:{type:'string'}, rationale:{type:'string'}
    }, required:['stem','options','answer','rationale']}},
    discussion:{type:'array', items:{type:'string'}},
    sample_responses:{type:'array', items:{type:'string'}},
    writing:{type:'object', additionalProperties:false, properties:{
      type:{type:'string'}, text:{type:'string'}}, required:['type','text']},
    misconceptions:{type:'array', items:{type:'string'}},
    ap_alignment:{type:'string'},
    _scan: SCAN
  }, required:['base','edition','date','headline','body','devices','mcq','discussion','sample_responses','writing','misconceptions','ap_alignment','_scan']
}

const VERIFY_SCHEMA = {type:'object', additionalProperties:false, properties:{
  dimension:{type:'string'}, pass:{type:'boolean'},
  issues:{type:'array', items:{type:'string'}},
  fixes:{type:'array', items:{type:'string'}}
}, required:['dimension','pass','issues','fixes']}

const CROSS_SCHEMA = {type:'object', additionalProperties:false, properties:{
  flags:{type:'array', items:{type:'object', additionalProperties:false, properties:{
    flag:{type:'string'}, tripped:{type:'boolean'}, detail:{type:'string'},
    offenders:{type:'array', items:{type:'integer'}}
  }, required:['flag','tripped','detail','offenders']}},
  overall:{type:'string'},
  hard_gate_failures:{type:'array', items:{type:'integer'}}
}, required:['flags','overall','hard_gate_failures']}

// ---------------- prompt builders ----------------
function sourcePrompt(row){
  const isR = row.basis === 'R'
  return `You are the SOURCE stage for Caught Up AI opener #${row.id} (${row.register}, basis ${row.basis}).
Topic: ${row.topic}
Angle: ${row.angle}
${row.addressee ? 'Open Letter addressee: ' + row.addressee : ''}
${row.persona_concept ? 'Persona concept: ' + row.persona_concept : ''}

Read ${F.acc} for the sourcing standard. Your job is to build the numbered factual spine the drafter will write from. Do NOT write prose.

${isR ? `This is REAL CURRENT NEWS. Use WebSearch/WebFetch now. For EVERY load-bearing fact:
- find at least 2 INDEPENDENT sources (genuinely different reporting, not one wire rewritten); prefer a primary source (filing, transcript, official release, data table) and trace numbers/quotes to origin.
- confirm it still holds as of ${ISO} (no retraction/correction/superseding update).
- mark primary=true only for genuine primary sources; set flag to "single-source" or "developing" or "contested" where that applies, and the drafter will write around flagged facts.
Drop any fact you cannot independently confirm. If the topic itself does not hold up (stale, single-source, not classroom-safe), say so in sourcing_notes and build the best verifiable adjacent fact list you can.`
: `This is EVERGREEN / PERSONA-SAFE. Assemble stable, well-established facts (with references in sources). ${row.persona_concept ? 'You MAY invent a first-person persona and family/biographical detail (that is allowed); but any HARD fact embedded (statistic, history, science, a real institution) must be real and sourced. Put invented persona material in persona_material and keep the fact_list to verifiable hard facts only.' : 'Use durable, checkable facts; cite stable references.'}`}

Build a numbered fact_list (n starting at 1). 8-16 facts is typical. Keep each fact a flat statement. Confirm classroom_safe (true/false) for a US high-school AP class. Return ONLY the structured object.`
}

function draftPrompt(src, row){
  return `You are the DRAFT stage for Caught Up AI opener #${row.id}. Produce ONE complete opener as the structured object (it must match the renderer schema exactly).

READ THESE SPECS LIVE before drafting (do not work from memory):
- ${F.reg}  -> find the section for THE ${row.register.toUpperCase()}; hit its bands and honor its drift cues.
- ${F.tpl}  -> use the template "${row.template}"; open_type "${row.open_type}"; close_type "${row.close_type}". Engine = exactly one.
- ${F.tell}  -> apply the FRICTION / ANTI-SYMMETRY layer (read first) AND obey the mechanical blocklist. ZERO em-dashes, ZERO emojis.
- ${F.dev}  -> device labels may ONLY come from this controlled list; tag the WHOLE move, not its trigger word; be exact about look-alikes (anaphora vs parallelism, simile vs metaphor). Understatement/litotes is removed; allusions must be widely recognizable.
- ${F.mcq}  -> the two MCQs and the FRQ selection follow this spec.

FACT SPINE (draft ONLY from this; never track a source's sentences):
${JSON.stringify(src)}

WRITE:
1) headline: short, specific, no clickbait.
2) body: an array of paragraphs, 350-450 words total, in THE ${row.register} register, built on the ${row.template} template with a "${row.open_type}" opening and a "${row.close_type}" close, rhythm target: ${row.rhythm_target}. Vary sentence length hard (at least one under ~8 words, at least one over ~30; no three same-length sentences in a row). Apply the friction layer: lopsided structure, at least one inert/off-thesis true detail, not every paragraph ending on a button, no mirror-the-opening close, no reader-directing signposting. Inside the body, mark 4 to 6 GENUINELY PRESENT devices with [[n]]...[[/n]] spans, n = 1,2,3... in order of appearance, each span covering the whole device. Every load-bearing fact must trace to the fact spine; do not invent stats/history/science.
3) devices: one entry per [[n]] span IN THE SAME ORDER (devices[n-1] matches span n). Each entry: para (the paragraph number the span sits in, 1-based), device (exact controlled-list name), purpose (1-2 lines: why the author chose it and what it accomplishes).
4) mcq: exactly 2 questions, each 4 options, targeting TWO DIFFERENT AP reading skills (e.g. one Reasoning/Claims, one Style/tone). Each distractor must fail by a named trap from the MCQ spec; exactly one defensibly-best answer. Author by marking the correct option; set "answer" to the LETTER of the correct option AS YOU ORDERED THEM (the renderer reshuffles, so do not pattern letters). Rationales reference distractors BY CONTENT, never by letter.
5) writing: pick the FRQ that genuinely fits. Q2 rhetorical analysis fits any passage; Q3 argument ONLY for argument-bearing passages (Reckoning, Long Think, Ledger, Open Letter); observational/consecratory passages (Long Look, Tribute, usually Witness Stand) take Q2. Never Q1. "type" = e.g. "Homework or extended in-class, Q2 rhetorical analysis". "text" = the full prompt.
6) discussion: 2 questions. sample_responses: 2 strong model responses. misconceptions: 3-4 student misconceptions to watch (tie at least one to the marked devices). ap_alignment: 1-3 sentences on what this opener teaches.
7) base: "Caught Up AI Opener - ${ISO} - <Headline> (${row.register})". edition: "Batch test edition". date: "${DATE}".
8) _scan: first_sentence, last_sentence, para_count, approx_sentence_mean (your estimate), device_count, opener_bucket (scene-set/question/named-actor-verb/abstract-claim/stat-lead/quote-lead/flat-fact/address), close_bucket (zoom-out/what-to-watch/callback/button/quote/inward-turn/charge/benediction), spine (3-5 beat one-line description of the structure).

Return ONLY the structured object.`
}

function verifyPrompt(dim, dict, row, src){
  const heads = {
    accuracy:`ACCURACY checker. Be adversarial: try to find a false or untraceable claim. Read ${F.acc}. ${row.basis==='R' ? 'Use WebSearch/WebFetch to spot-check every name, number, date, quote, and causal claim against independent sources; flag anything single-sourced, stale, or not on the fact spine (orphan fact).' : 'Verify every embedded HARD fact (stat/history/science/real institution) is true and traceable; invented persona/family detail is allowed and is NOT an accuracy failure.'} Check the fact spine: ${JSON.stringify(src).slice(0,8000)}`,
    devices:`DEVICES checker. Be adversarial. Read ${F.dev}. For each tagged device: is the label from the controlled list, correct, and genuinely present? Are look-alikes right (anaphora needs repetition at the START of successive clauses; simile needs like/as; antithesis needs balanced opposition)? Does each [[n]] span cover the whole move (not just a trigger word)? Does devices[n-1] match span n and is "para" correct? Are there 4-6 devices? Flag any mislabel, any forced/absent device, any tag-count or ordering mismatch.`,
    mcq:`MCQ checker. Be adversarial. Read ${F.mcq}. For EACH question: is there exactly ONE defensibly-best answer (try to defend a second option; if you can, it fails)? Does every distractor fail by a named trap (no free-elimination throwaway)? Are all four options parallel in grammar and comparable in length? Do the two questions test DIFFERENT reading skills? Do rationales reference distractors by CONTENT not letter? Is each answerable from the opener alone? Also check the FRQ type genuinely fits the passage (no Q3 on a non-argument piece; no Q1).`,
    mechanical:`MECHANICAL / ANTI-TELL checker. Be adversarial. Read ${F.tell} and the bands in ${F.reg} for THE ${row.register}. Checks: (1) ZERO em-dashes and ZERO emojis anywhere (hard fail on any hit). (2) Anti-tell sweep: significance-inflation, copula-avoidance, Family A-F words, sentence-head transition reflex (>1), elegant variation. (3) Friction layer present: not all paragraphs balanced, not every paragraph ends on a button, at least one inert/off-thesis detail, ending does not mirror opening, no reader-directing signposting, "not X but Y" capped. (4) Burstiness: at least one sentence <8 words and one >30; no three same-length in a row. (5) Register bands roughly in range; close type matches the assigned "${row.close_type}". (6) Word count 350-450. (7) Body device tags [[n]] are well-formed and sequential.`
  }
  return `${heads[dim]}

OPENER UNDER REVIEW (#${row.id}, ${row.register}):
${JSON.stringify({headline:dict.headline, body:dict.body, devices:dict.devices, mcq:dict.mcq, writing:dict.writing}).slice(0, 24000)}

Return ONLY the structured verdict: dimension="${dim}", pass (true only if it meets the standard), issues (specific), fixes (concrete, actionable). Default to pass=false if a real flaw exists; do not rubber-stamp.`
}

function redraftPrompt(dict, row, src, problems){
  return `You are REDRAFTING Caught Up AI opener #${row.id} (${row.register}) to fix verifier findings. Keep everything that passed; change only what the findings require. Obey the same specs (${F.reg}, ${F.tpl}, ${F.tell}, ${F.dev}, ${F.mcq}, ${F.acc}). Zero em-dashes/emojis. Keep facts traceable to the spine.

VERIFIER FINDINGS TO RESOLVE:
${JSON.stringify(problems)}

CURRENT OPENER:
${JSON.stringify(dict).slice(0, 30000)}

FACT SPINE:
${JSON.stringify(src).slice(0, 8000)}

Return the COMPLETE corrected opener as the same structured object (all fields incl. _scan), ids/format unchanged.`
}

// ---------------- pipeline ----------------
phase('Source')
const results = await pipeline(
  openers,
  // stage 1: SOURCE
  (row) => agent(sourcePrompt(row), {
    label:`source#${row.id}:${row.register}`, phase:'Source',
    agentType:'Explore', schema: SOURCE_SCHEMA
  }).then(src => ({row, src})),

  // stage 2: DRAFT
  ({row, src}) => agent(draftPrompt(src, row), {
    label:`draft#${row.id}:${row.register}`, phase:'Draft', schema: DRAFT_SCHEMA
  }).then(dict => ({row, src, dict})),

  // stage 3: VERIFY (4 adversarial) -> redraft once on any fail
  async ({row, src, dict}) => {
    const dims = ['accuracy','devices','mcq','mechanical']
    const verdicts = await parallel(dims.map(d => () =>
      agent(verifyPrompt(d, dict, row, src), {
        label:`verify:${d}#${row.id}`, phase:'Verify', schema: VERIFY_SCHEMA,
        agentType: d==='accuracy' ? 'Explore' : undefined
      })
    ))
    const v = verdicts.filter(Boolean)
    const failed = v.filter(x => !x.pass)
    let finalDict = dict, redrafted = false, residual = []
    if (failed.length){
      redrafted = true
      const problems = failed.map(x => ({dimension:x.dimension, issues:x.issues, fixes:x.fixes}))
      finalDict = await agent(redraftPrompt(dict, row, src, problems), {
        label:`redraft#${row.id}:${row.register}`, phase:'Verify', schema: DRAFT_SCHEMA
      })
      // single consolidated confirmation pass over the redraft
      const conf = await agent(
        `CONFIRMATION pass over a redrafted Caught Up AI opener #${row.id} (${row.register}). The prior issues were:\n${JSON.stringify(problems)}\nCheck the redraft below ONLY for: em-dashes/emojis (hard fail), the specific prior issues resolved, device tag/array integrity, exactly-one-best-answer per MCQ, two different skills, facts traceable. Read ${F.tell} and ${F.dev} if needed.\nREDRAFT:\n${JSON.stringify({headline:finalDict.headline, body:finalDict.body, devices:finalDict.devices, mcq:finalDict.mcq, writing:finalDict.writing}).slice(0,24000)}\nReturn dimension="confirmation", pass, issues, fixes.`,
        {label:`confirm#${row.id}`, phase:'Verify', schema: VERIFY_SCHEMA}
      )
      if (conf && !conf.pass) residual = conf.issues
    }
    return {
      id: row.id, register: row.register, basis: row.basis, topic: row.topic,
      dict: finalDict, redrafted, residual,
      verdicts: v.map(x => ({dimension:x.dimension, pass:x.pass, issues:x.issues}))
    }
  }
)

const finals = results.filter(Boolean)
log(`Drafted+verified ${finals.length}/28 openers; ${finals.filter(f=>f.redrafted).length} needed a redraft`)

// ---------------- cross-piece sameness audit ----------------
phase('Cross-check')
const scans = finals.map(f => ({
  id: f.id, register: f.register, basis: f.basis,
  first_sentence: f.dict._scan?.first_sentence,
  last_sentence: f.dict._scan?.last_sentence,
  para_count: f.dict._scan?.para_count,
  approx_sentence_mean: f.dict._scan?.approx_sentence_mean,
  device_count: f.dict._scan?.device_count,
  opener_bucket: f.dict._scan?.opener_bucket,
  close_bucket: f.dict._scan?.close_bucket,
  spine: f.dict._scan?.spine,
  headline: f.dict.headline
})).sort((a,b)=>a.id-b.id)

const audit = await agent(
  `You are the CROSS-PIECE SAMENESS critic for a 28-opener batch. Read ${F.same} for the ten flags and thresholds. Using the per-piece scans below (opener bucket, closer bucket, paragraph count, approx sentence mean, device count, spine, first/last sentence), run the rubric across the whole batch. Report each of the ten flags: tripped (true/false), a one-line detail, and the offending ids. Note register rotation is fixed-even by construction; focus on opener-gambit clustering, identical skeleton, the "why it matters" pivot, convergent rhythm, pet phrases (from first/last sentences), close-type clustering, banned constructions, uniform paragraph count, and register flattening (blind-shuffle judgment from the first sentences). Put any banned-construction (flag 8) offender ids in hard_gate_failures.
SCANS:
${JSON.stringify(scans)}
Return ONLY the structured audit.`,
  {label:'cross-piece-critic', phase:'Cross-check', schema: CROSS_SCHEMA}
)

return {
  openers: finals.map(f => ({id:f.id, register:f.register, basis:f.basis, redrafted:f.redrafted, residual:f.residual, verdicts:f.verdicts, dict:f.dict})),
  audit,
  redraftCount: finals.filter(f=>f.redrafted).length,
  count: finals.length
}

