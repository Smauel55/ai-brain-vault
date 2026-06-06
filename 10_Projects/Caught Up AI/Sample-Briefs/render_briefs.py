# -*- coding: utf-8 -*-
"""
Caught Up AI - daily lesson-opener PDF generator.

Format matches "Teacher Meeting Brief v0.2" (Samuel's reference):
  STUDENT copy: numbered article, Discussion questions, AP-style multiple choice,
    Writing prompt. No marks, no answers.
  TEACHER copy: the article marked for rhetorical devices (highlighted phrase plus an
    inline bracket label, e.g. [paragraph 1: anecdote, pathos]), Quick reference
    (devices used) by paragraph, the MCQ plus answer key, Discussion questions plus
    sample strong responses, the Writing prompt, Common misconceptions, AP exam alignment.

Device labels use ONLY the approved AP device vocabulary, applied only where genuinely
present. No em-dashes, no emojis.
"""
import os, re
from collections import OrderedDict
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, Image)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(OUT_DIR, "caughtup-logo.png")

GREY = HexColor("#666666"); RULE = HexColor("#CCCCCC")
HL  = {1:"#CFE2F3", 2:"#FFF2A8", 3:"#CFEFD0", 4:"#FCE5CD", 5:"#F4CCCC", 6:"#E6D5F2"}
ANN = {1:"#1F5C8A", 2:"#8A6D00", 3:"#2E7D32", 4:"#B5651D", 5:"#B03A48", 6:"#6A3FA0"}

_ir = ImageReader(LOGO); _iw, _ih = _ir.getSize()
LOGO_H = 0.40*inch; LOGO_W = LOGO_H*_iw/_ih

ss = getSampleStyleSheet()
body  = ParagraphStyle("body", parent=ss["Normal"], fontName="Times-Roman",
                       fontSize=11, leading=15.5, alignment=TA_LEFT, spaceAfter=7)
title = ParagraphStyle("title", parent=ss["Title"], fontName="Times-Bold",
                       fontSize=17, leading=20, textColor=black, alignment=TA_LEFT, spaceAfter=3)
roletag = ParagraphStyle("roletag", parent=ss["Normal"], fontName="Helvetica-Bold",
                         fontSize=9, textColor=GREY, spaceAfter=10)
sect  = ParagraphStyle("sect", parent=ss["Normal"], fontName="Helvetica-Bold",
                       fontSize=11, textColor=black, spaceBefore=13, spaceAfter=5, leading=13)
q     = ParagraphStyle("q", parent=body, spaceAfter=2)
opt   = ParagraphStyle("opt", parent=body, leftIndent=18, spaceAfter=1)
bullet= ParagraphStyle("bullet", parent=body, leftIndent=14, spaceAfter=2)
wordm = ParagraphStyle("wordm", parent=ss["Normal"], fontName="Helvetica-Bold",
                       fontSize=12, textColor=black, leading=13)
wtag  = ParagraphStyle("wtag", parent=ss["Normal"], fontName="Helvetica",
                       fontSize=7.5, textColor=GREY, leading=9)
mdate = ParagraphStyle("mdate", parent=ss["Normal"], fontName="Helvetica",
                       fontSize=8.5, textColor=GREY, leading=11, alignment=2)

def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(0.9*inch, 0.5*inch, "Caught Up AI   .   caughtupai.com")
    canvas.drawRightString(letter[0]-0.9*inch, 0.5*inch, "p. %d" % canvas.getPageNumber())
    canvas.restoreState()

def header(date_str, role):
    logo = Image(LOGO, width=LOGO_W, height=LOGO_H)
    left = Table([[logo, [Paragraph("Caught Up AI", wordm),
                          Paragraph("The daily AP English Language Opener", wtag)]]],
                 colWidths=[LOGO_W+8, 3.1*inch])
    left.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                              ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,0),8),
                              ("RIGHTPADDING",(1,0),(1,0),0)]))
    t = Table([[left, Paragraph(date_str + "<br/>" + role, mdate)]],
              colWidths=[4.4*inch, 2.3*inch])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                           ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
    return [t, Spacer(1,5), HRFlowable(width="100%", thickness=0.8, color=RULE), Spacer(1,10)]

def make_para(raw, idx, devices, highlight):
    text = esc(raw)
    if highlight:
        def repl(m):
            k=int(m.group(1)); inner=m.group(2); d=devices[k-1]
            return ('<font backColor="%s">%s</font> '
                    '<font size="8" color="%s"><b>[paragraph %d: %s]</b></font>'
                    % (HL[d["color"]], inner, ANN[d["color"]], d["para"], esc(d["label"])))
    else:
        def repl(m): return m.group(2)
    text = re.sub(r"\[\[(\d+)\]\](.*?)\[\[/\1\]\]", repl, text, flags=re.S)
    return '<b><font size="8">%d</font></b>&nbsp;&nbsp;%s' % (idx, text)

def quickref(devices):
    groups = OrderedDict()
    for d in devices:
        groups.setdefault(d["para"], []).append(d["label"])
    return ["Paragraph %d: %s" % (p, "; ".join(ls)) for p, ls in groups.items()]

def build(piece, role):
    teacher = (role == "Teacher")
    fname = os.path.join(OUT_DIR, "%s - %s copy.pdf" % (piece["base"], role))
    doc = SimpleDocTemplate(fname, pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch,
                            topMargin=0.7*inch, bottomMargin=0.75*inch,
                            title="%s (%s copy)" % (piece["headline"], role), author="Caught Up AI")
    s = []
    s += header(piece["date"], piece["edition"] + " . " + role + " copy")
    s.append(Paragraph(esc(piece["headline"]), title))
    s.append(Paragraph("Teacher copy (everything in the student copy, plus answers and teaching notes)"
                       if teacher else "Student copy (project or hand out)", roletag))

    # Article
    if teacher:
        s.append(Paragraph("The article, marked for rhetorical devices:", sect))
    for i, para in enumerate(piece["body"], 1):
        s.append(Paragraph(make_para(para, i, piece["devices"], teacher), body))

    if teacher:
        s.append(Paragraph("Quick reference (devices used):", sect))
        for line in quickref(piece["devices"]):
            s.append(Paragraph("&bull;&nbsp;&nbsp;" + esc(line), bullet))

    # MCQ
    s.append(Paragraph("AP-style multiple choice:", sect))
    for i, item in enumerate(piece["mcq"], 1):
        blk = [Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(item["stem"])), q)]
        for let, o in zip("ABCD", item["options"]):
            blk.append(Paragraph("%s)&nbsp;&nbsp;%s" % (let, esc(o)), opt))
        s.append(KeepTogether(blk)); s.append(Spacer(1,4))

    if teacher:
        key = [Paragraph("Multiple choice answer key:", sect)]
        for i, item in enumerate(piece["mcq"], 1):
            key.append(Paragraph("<b>%d. Answer %s.</b>&nbsp;&nbsp;%s" % (i, item["answer"], esc(item["rationale"])), q))
        s.append(KeepTogether(key))

    # Discussion
    s.append(Paragraph("Discussion questions:", sect))
    for i, d in enumerate(piece["discussion"], 1):
        s.append(Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(d)), q))

    if teacher:
        sr = [Paragraph("Sample strong discussion responses:", sect)]
        for i, r in enumerate(piece["sample_responses"], 1):
            sr.append(Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(r)), q))
        s.append(KeepTogether(sr))

    # Writing prompt
    s.append(Paragraph("Writing prompt (%s):" % esc(piece["writing"]["type"]), sect))
    s.append(Paragraph(esc(piece["writing"]["text"]), body))

    if teacher:
        mis = [Paragraph("Common misconceptions to watch for:", sect)]
        for m in piece["misconceptions"]:
            mis.append(Paragraph("&bull;&nbsp;&nbsp;" + esc(m), bullet))
        s.append(KeepTogether(mis))
        s.append(Paragraph("AP exam alignment:", sect))
        s.append(Paragraph(esc(piece["ap_alignment"]), body))

    doc.build(s, onFirstPage=footer, onLaterPages=footer)
    return fname

# ================================================================== content
DATE = "Friday, June 5, 2026"

ledger = {
 "base":"Caught Up AI Opener - 2026-06-05 - Ukraine Aid Vote (Ledger)",
 "edition":"Sample edition 1 of 3", "date":DATE,
 "headline":"A Cross-Party Majority, and a Procedural Back Door",
 "body":[
  "On Thursday the House voted 226 to 195 to send Ukraine [[1]]more than $1 billion in security and reconstruction aid and to open up to $8 billion in defense loans[[/1]], along with new sanctions on key parts of the Russian economy, including its energy sector. The bill passed over the stated objections of President Trump and the House's own Republican leaders.",
  "It reached the floor at all only through a discharge petition, the rarely successful procedure that lets a majority of members force a vote when leadership refuses to schedule one. Two hundred and eighteen signatures are required. [[2]]Supporters got them.[[/2]] Eighteen Republicans then crossed over to join all but one Democrat, Ilhan Omar of Minnesota, who voted no.",
  "The bill's sponsor, [[3]]Representative Gregory Meeks of New York[[/3]], framed the money as overdue. Representative Don Bacon of Nebraska, one of the Republicans who broke ranks, put it in starker terms on the floor: “[[4]]Are we going to stand with good or are we going to stand with evil?[[/4]] That's what this is about tonight.” [[5]]The leadership's case was quieter and procedural.[[/5]] Majority Leader Steve Scalise argued that the administration's own negotiations were already moving, and that legislating around them could set them back: “you set that back,” he said, “if you pass legislation that doesn't go as far as the negotiations are going.”",
  "What the House did on Thursday it cannot finish on its own. The bill goes next to the Senate, where it needs 60 votes, and where the count is not there. A companion measure on Russian tariffs and secondary sanctions has already stalled. By the arithmetic of the chamber the aid does not advance unless Trump endorses it, which he has so far declined to do.",
  "So the vote settles less than its margin suggests. It records that a cross-party majority of one chamber wants the aid sent now, and that the same majority was willing to go around its own leadership to say so. Whether any of the money reaches Ukraine is a separate question. It belongs to the Senate, and [[6]]to the president the House just voted against[[/6]].",
 ],
 "devices":[
  {"para":1,"color":1,"label":"statistics, logos"},
  {"para":2,"color":2,"label":"short declarative, syntax"},
  {"para":3,"color":3,"label":"named attribution, ethos"},
  {"para":3,"color":4,"label":"rhetorical question"},
  {"para":3,"color":5,"label":"concession and refutation"},
  {"para":5,"color":6,"label":"irony"},
 ],
 "mcq":[
  {"stem":"In the second paragraph, the brief sentence “Supporters got them.” primarily serves to",
   "options":["inject the writer's approval of the bill's passage",
              "mark, without comment, that a difficult procedural threshold was met",
              "question whether the signatures were legitimately obtained",
              "summarize the passage's overall argument"],
   "answer":"B","rationale":"The clipped sentence (syntax) states that 218 signatures were reached and leaves it there, the impartial habit of the piece."},
  {"stem":"The writer juxtaposes Bacon's question about “good” and “evil” with Scalise's procedural caution mainly to",
   "options":["ridicule Scalise's position as evasive",
              "frame the dispute as moral conviction against procedural caution, without resolving it",
              "prove that the bill's supporters held the stronger argument",
              "build suspense about the final vote count"],
   "answer":"B","rationale":"The neutral juxtaposition sets a pathos-driven appeal beside a procedural one and leaves the reader to weigh them."},
 ],
 "discussion":[
  "The writer never says whether the aid is a good idea. How does the passage still leave you with an impression of where the weight of the argument falls, and through what choices?",
  "Why might a writer reporting a politically charged vote choose to end on procedure (“it belongs to the Senate”) rather than on either side's strongest line?",
 ],
 "sample_responses":[
  "A strong answer notes the piece never editorializes but stacks choices that tilt it: it gives Bacon's vivid moral line more room than Scalise's procedural caution, ends on the aid stalling, and frames the holdouts as going 'around its own leadership.' The lean is built from arrangement and emphasis, not from stated opinion.",
  "Ending on the Senate and the president keeps the register impartial: it reports the state of play rather than rooting for an outcome, and it quietly lands the irony that the aid now depends on the very president the House just defied.",
 ],
 "writing":{"type":"homework or extended in-class, Q3 argument",
  "text":"The passage describes a chamber registering a position it may lack the power to enact. Defend, challenge, or qualify the claim that a symbolic vote a legislature cannot turn into law is still a meaningful political act. Use your own knowledge, observation, or reading."},
 "misconceptions":[
  "Students may call the dollar figures 'pathos' because the topic feels emotional. The numbers are logos: evidence to be weighed, not feeling.",
  "Students may read the Bacon quote as the writer's own view. It is attributed; the writer reports it, and balances it against the leadership's case.",
  "'Concession' is not the same as 'both sides.' Here the leadership's case is granted, then refuted by the close.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a compact study of how attribution, the juxtaposition of opposing sources, and sentence length build an impartial ethos. Useful for teaching that tone is constructed by arrangement, not only by word choice.",
}

longlook = {
 "base":"Caught Up AI Opener - 2026-06-05 - Antarctic Basin (Long Look)",
 "edition":"Sample edition 2 of 3", "date":DATE,
 "headline":"The Shape Under the Ice",
 "body":[
  "[[1]]We have better maps of the surface of Mars than of the rock beneath the East Antarctic ice.[[/1]] That is the ordinary condition of the place. Kilometers of ice sit on top of a continent almost nobody has seen, and what is known of the bedrock has been pieced together from radar, gravity readings, and the slow inference of signals the ice does not give up easily.",
  "Now a team writing in the journal Nature Geoscience has put a name to a piece of it. They call it the East Antarctic Fan-shaped Basin Province. It is, on their reading, a single structure: roughly thirty subglacial basins that had been catalogued one at a time, set side by side, turn out to splay from one point [[2]]like the ribs of a fan[[/2]]. The point sits within four degrees of the South Pole. The fan opens out from there toward the coast.",
  "The basins are not minor features. The province gathers in the Wilkes and Aurora basins and the trough that holds Lake Vostok, the largest body of liquid water known to lie under any ice sheet on Earth. These were familiar landmarks. What the study argues is that they were never separate landmarks at all. [[3]]They are fingers of the same hand.[[/3]]",
  "[[4]]The shape has a cause.[[/4]] The lead author, Egidio Armadillo of the University of Genoa, with colleagues including Guy Paxman at Durham, read it as the record of distributed rotational extension: crust that stretched outward from a center, slowly, in more than one episode, as the old supercontinent of Gondwana came apart and Antarctica and Australia went their separate ways. The triangular basins are the gaps that opening left behind.",
  "None of this is dead history. The bed under an ice sheet is not a floor. It is a set of channels and dams. [[5]]Where the rock dips, ice pools and slides; where it rises, ice slows.[[/5]] So a fan drawn into the crust in the deep geological past still has a say in where the ice of East Antarctica travels now, and in which parts of it are most exposed as the climate warms. That last part is where the work goes quiet. The map is new, [[6]]the consequences are not yet drawn, and the authors are careful to say which is which[[/6]].",
 ],
 "devices":[
  {"para":1,"color":1,"label":"juxtaposition"},
  {"para":2,"color":2,"label":"simile"},
  {"para":3,"color":3,"label":"metaphor"},
  {"para":4,"color":4,"label":"short declarative, syntax"},
  {"para":5,"color":5,"label":"antithesis"},
  {"para":5,"color":6,"label":"candor, ethos"},
 ],
 "mcq":[
  {"stem":"The opening sentence comparing maps of Mars to maps beneath the Antarctic ice chiefly functions to",
   "options":["argue that planetary science is overfunded relative to polar research",
              "establish, through juxtaposition, how little of the continent's bedrock is known",
              "introduce a personal anecdote about the writer's fieldwork",
              "predict that the ice sheet will soon be fully mapped"],
   "answer":"B","rationale":"The juxtaposition of two unlike places sets the scale of ignorance the rest of the piece works against, using fact rather than adjectives."},
  {"stem":"The short sentences such as “The shape has a cause.” set against the longer technical sentences primarily create an effect of",
   "options":["hesitation about whether the findings are sound",
              "a measured alternation in syntax that carries the reader from plain fact to its complicated explanation",
              "impatience with a reader who is slow to understand",
              "an emotional plea to protect the ice sheet"],
   "answer":"B","rationale":"The deliberate short-against-long sentence structure carries the reader from the known to the complex."},
 ],
 "discussion":[
  "The writer never uses a word like “astonishing” or “breathtaking,” yet the discovery reads as remarkable. How is that effect produced without those words?",
  "Compare the simile in paragraph 2 with the metaphor in paragraph 3. What does each comparison do that the other does not?",
 ],
 "sample_responses":[
  "The awe comes from facts and structure: the Mars comparison sets the scale of ignorance, precise particulars (thirty basins, four degrees from the Pole, Lake Vostok) do the work an adjective would, and the short-against-long rhythm makes each fact land. The writer trusts the reader to feel the scale.",
  "The simile ('like the ribs of a fan') keeps the basins and the fan separate, helping the reader picture a shape. The metaphor ('fingers of the same hand') collapses the comparison: the basins are not like fingers, they are one body, which is the article's whole claim that the separate features form a single structure.",
 ],
 "writing":{"type":"homework or extended in-class, Q3 argument",
  "text":"The article devotes great effort to mapping a landscape no one can see or use directly. Defend, challenge, or qualify the claim that there is real value in studying things we cannot yet put to use. Use your own knowledge, observation, or reading."},
 "misconceptions":[
  "Students may label any comparison a metaphor. Cue them to check for 'like' or 'as' (simile) versus an implied identity (metaphor).",
  "Students may call the piece persuasive. It withholds argument; its aim is to render, not to convince. The candor at the close is ethos, not a thesis.",
  "The 'juxtaposition' here is the Mars and Antarctica pairing, not a contrast inside a single sentence.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a clean text for distinguishing the comparison devices (simile, metaphor, juxtaposition) and for analyzing how syntax, short against long sentences, controls pace and emphasis.",
}

tribute = {
 "base":"Caught Up AI Opener - 2026-06-05 - Marjane Satrapi (Tribute)",
 "edition":"Sample edition 3 of 3", "date":DATE,
 "headline":"She Drew Small",
 "body":[
  "She told the story of a revolution in the drawings of a child, and that turned out to be the truest way to tell it. Marjane Satrapi, who died in Paris on Thursday at fifty-six, made her name with a black-and-white comic about a girl in Tehran. The girl was herself.",
  "Persepolis began appearing in 2000, four slim volumes of line drawings: a daughter of educated, watchful parents growing up as the Iran of her childhood was remade around her, then sent abroad to Europe, alone and young. [[1]]The drawings were plain.[[/1]] [[2]]A veil, a schoolyard, a soldier at a corner.[[/2]] Out of those small panels came a portrait of a country that years of reporting had left, for most outside readers, a blur.",
  "That was her method, and her quiet argument: that [[3]]the enormous is best approached through the small[[/3]]. [[4]]A revolution rendered as a quarrel with her grandmother. Exile rendered as a teenager friendless in a borrowed language.[[/4]] She trusted the particular to carry the general, and it did.",
  "And in 2007 she and Vincent Paronnaud turned the books into an animated film, keeping the stark black and white when color would have been easier and more salable. It shared the Jury Prize at Cannes. It was nominated for the Academy Award for best animated feature, and with that nomination Satrapi became the first woman the category had ever named. She went on to other things: a novel and film called Chicken with Plums, books drawn at a kitchen table, films in registers far from where she began, and, near the end, a book that gathered Iranian artists under the slogan woman, life, freedom.",
  "Her family said she died of grief, a year after the death of her husband, Mattias Ripa. It is the kind of cause a doctor does not certify and a reader of her work does not doubt. She had always written as if private feeling and public history were the same material, seen at different distances.",
  "[[5]]She drew small so that the world could see something large.[[/5]] Her books remain [[6]]the clearest window many readers will ever have[[/6]] onto [[7]]a place they were taught to fear[[/7]], and they will go on doing that work quietly, in black and white, long after the hand that drew them is still.",
 ],
 "devices":[
  {"para":2,"color":1,"label":"understatement / litotes"},
  {"para":2,"color":2,"label":"asyndeton"},
  {"para":3,"color":3,"label":"antithesis (small vs large)"},
  {"para":3,"color":4,"label":"parallelism (not anaphora)"},
  {"para":6,"color":3,"label":"antithesis (payoff)"},
  {"para":6,"color":5,"label":"metaphor"},
  {"para":6,"color":6,"label":"pathos"},
 ],
 "mcq":[
  {"stem":"The three-word sentence “The girl was herself.” most directly functions to",
   "options":["cast doubt on the accuracy of Satrapi's account",
              "reveal the autobiographical basis of the work in a single, quiet stroke",
              "introduce a fictional character for contrast",
              "shift the passage from praise to complaint"],
   "answer":"B","rationale":"The clipped sentence (syntax) delivers the key fact, that the memoir is her own life, with the restraint the piece prizes."},
  {"stem":"Describing “private feeling and public history” as “the same material, seen at different distances” chiefly serves to",
   "options":["state the governing antithesis that small personal scenes can carry large historical meaning",
              "criticize historians for neglecting private life",
              "summarize the plot of Persepolis for the reader",
              "urge readers to write their own memoirs"],
   "answer":"A","rationale":"It restates the small-and-large antithesis that organizes the piece, a claim already demonstrated rather than asserted."},
 ],
 "discussion":[
  "The writer handles an unverifiable cause of death (“her family said she died of grief”) in a single sentence. How does the next line turn that uncertainty into a statement about her work?",
  "A tribute risks tipping into sentimentality. Point to two specific choices here (consider the understatement in paragraph 2) that keep the praise restrained rather than gushing.",
 ],
 "sample_responses":[
  "The writer reports the family's claim ('died of grief') rather than asserting it, then turns it: a doctor 'does not certify' the cause but a reader 'does not doubt' it. The move converts an uncertain fact into a statement about her art, that she treated private feeling and public history as one material.",
  "Restraint shows in the understatement ('the drawings were plain'), the refusal to pile on superlatives, and a close that places her in a longer history rather than issuing a call to action. The praise is carried by concrete images, not by adjectives.",
 ],
 "writing":{"type":"homework or extended in-class, Q3 argument",
  "text":"The writer claims that private feeling and public history are 'the same material, seen at different distances.' Defend, challenge, or qualify this claim, using your own reading, study, or experience."},
 "misconceptions":[
  "Students often mislabel the 'rendered as ... rendered as ...' run as anaphora. It is parallelism: the repeated element falls in the middle, not at the start of each clause.",
  "Calling the drawings 'plain' is understatement, not literal description; the point is that small means carry large meaning.",
  "'Pathos' here lives in concrete nouns ('a place they were taught to fear'), not in emotion-words.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: strong for teaching antithesis as a structural engine and for the parallelism-versus-anaphora distinction. The epideictic (tribute) mode is a useful contrast to argument passages.",
}

if __name__ == "__main__":
    for p in (ledger, longlook, tribute):
        for role in ("Teacher", "Student"):
            print("wrote:", build(p, role))
