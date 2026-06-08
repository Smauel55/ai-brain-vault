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

const openers = __MATRIX__
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
2) body: an array of paragraphs, 350-450 words total, in THE ${row.register} register, built on the ${row.template} template with a "${row.open_type}" opening and a "${row.close_type}" close, rhythm target: ${row.rhythm_target}. Vary sentence length hard (at least one under ~8 words, at least one over ~30; no three same-length sentences in a row). Apply the friction layer: lopsided structure, at least one inert/off-thesis true detail, not every paragraph ending on a button, no mirror-the-opening close, no reader-directing signposting. Inside the body, mark 4 to 6 GENUINELY PRESENT devices with highlight spans. EXACT TAG SHAPE (a strict renderer parses these character-for-character, so get it perfect): open a span with [[n]] and CLOSE it with [[/n]] -- a forward slash before the number, in the closing tag only. Worked example for device 1: [[1]]the whole tagged phrase[[/1]]. The closing tag is [[/1]]; it is NEVER a second [[1]]. Number the spans 1,2,3... in order of appearance, each span covering the whole device move. SELF-CHECK before you return: every [[n]] open has exactly one matching slashed [[/n]] close; the count of opens equals the count of closes equals the length of your devices array; and no bare [[n]] is ever used as a closer. Every load-bearing fact must trace to the fact spine; do not invent stats/history/science.
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
    devices:`DEVICES checker. Be adversarial. Read ${F.dev}. For each tagged device: is the label from the controlled list, correct, and genuinely present? Are look-alikes right (anaphora needs repetition at the START of successive clauses; simile needs like/as; antithesis needs balanced opposition)? Does each [[n]] span cover the whole move (not just a trigger word)? Is each span CLOSED with a slashed [[/n]] (never a second bare [[n]])? Does devices[n-1] match span n and is "para" correct? Are there 4-6 devices, with opens = slashed closes = devices length? Flag any mislabel, any forced/absent device, any unclosed/mis-closed span, any tag-count or ordering mismatch.`,
    mcq:`MCQ checker. Be adversarial. Read ${F.mcq}. For EACH question: is there exactly ONE defensibly-best answer (try to defend a second option; if you can, it fails)? Does every distractor fail by a named trap (no free-elimination throwaway)? Are all four options parallel in grammar and comparable in length? Do the two questions test DIFFERENT reading skills? Do rationales reference distractors by CONTENT not letter? Is each answerable from the opener alone? Also check the FRQ type genuinely fits the passage (no Q3 on a non-argument piece; no Q1).`,
    mechanical:`MECHANICAL / ANTI-TELL checker. Be adversarial. Read ${F.tell} and the bands in ${F.reg} for THE ${row.register}. Checks: (1) ZERO em-dashes and ZERO emojis anywhere (hard fail on any hit). (2) Anti-tell sweep: significance-inflation, copula-avoidance, Family A-F words, sentence-head transition reflex (>1), elegant variation. (3) Friction layer present: not all paragraphs balanced, not every paragraph ends on a button, at least one inert/off-thesis detail, ending does not mirror opening, no reader-directing signposting, "not X but Y" capped. (4) Burstiness: at least one sentence <8 words and one >30; no three same-length in a row. (5) Register bands roughly in range; close type matches the assigned "${row.close_type}". (6) Word count 350-450. (7) Body device tags are renderer-valid: every span opens with [[n]] and closes with a SLASHED [[/n]] (a second bare [[n]] used as a closer is a HARD FAIL); the number of [[n]] opens equals the number of [[/n]] closes equals the length of the devices array; numbering is sequential 1,2,3... in order of appearance; no span is left unclosed.`
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

// ---------------- deterministic tag gate (Issue 1 permanent fix) ----------------
// A model verifier reads [[1]]..[[1]] as "span 1" and is blind to the defect; only a
// strict count catches it. This runs on the JS side so it cannot be rubber-stamped.
function normalizeClosers(dict){
  let fixed = 0
  dict.body = (dict.body||[]).map(para => {
    const nums = [...new Set([...para.matchAll(/\[\[(\d+)\]\]/g)].map(m=>+m[1]))].sort((a,b)=>a-b)
    for (const n of nums){
      const tok = `[[${n}]]`
      if (para.includes(`[[/${n}]]`)) continue          // already has a real closer
      const parts = para.split(tok)
      if (parts.length === 3){                           // exactly two bare opens
        para = parts[0]+tok+parts[1]+`[[/${n}]]`+parts[2]; fixed++
      }
    }
    return para
  })
  return fixed
}
function tagLint(dict){
  const b = (dict.body||[]).join('\n')
  const opens = (b.match(/\[\[\d+\]\]/g)||[]).length
  const closes = (b.match(/\[\[\/\d+\]\]/g)||[]).length
  const ndev = (dict.devices||[]).length
  const ok = opens === closes && opens === ndev
  return {ok, opens, closes, ndev,
    detail: ok ? '' : `opens=${opens} closes=${closes} devices=${ndev} (must be equal)`}
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
    // Deterministic tag gate FIRST: auto-repair duplicate-closers, then lint.
    // A residual imbalance (e.g. mis-numbered spans like the old #17) cannot be
    // regex-fixed, so it becomes a hard verdict that forces a redraft.
    const healed = normalizeClosers(dict)
    const lint = tagLint(dict)
    const tagVerdict = {
      dimension:'tags', pass: lint.ok,
      issues: lint.ok ? [] : [`Device highlight tags do not balance: ${lint.detail}. Likely a span opened with [[n]] but not closed with a slashed [[/n]], or a span count that does not match the devices array.`],
      fixes: lint.ok ? [] : ['Re-tag the body so every device move is wrapped [[n]]...[[/n]] with a slashed close, numbered in order, one span per devices entry.']
    }
    if (healed) log(`[tag-gate] id ${row.id}: auto-repaired ${healed} duplicate-closer tag(s)`)

    const dims = ['accuracy','devices','mcq','mechanical']
    const verdicts = await parallel(dims.map(d => () =>
      agent(verifyPrompt(d, dict, row, src), {
        label:`verify:${d}#${row.id}`, phase:'Verify', schema: VERIFY_SCHEMA,
        agentType: d==='accuracy' ? 'Explore' : undefined
      })
    ))
    const v = [tagVerdict, ...verdicts.filter(Boolean)]
    const failed = v.filter(x => !x.pass)
    let finalDict = dict, redrafted = false, residual = []
    if (failed.length){
      redrafted = true
      const problems = failed.map(x => ({dimension:x.dimension, issues:x.issues, fixes:x.fixes}))
      finalDict = await agent(redraftPrompt(dict, row, src, problems), {
        label:`redraft#${row.id}:${row.register}`, phase:'Verify', schema: DRAFT_SCHEMA
      })
      // re-run the deterministic tag gate on the redraft so it cannot reintroduce the bug
      normalizeClosers(finalDict)
      const lint2 = tagLint(finalDict)
      if (!lint2.ok) residual.push(`tags still unbalanced after redraft: ${lint2.detail}`)
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
