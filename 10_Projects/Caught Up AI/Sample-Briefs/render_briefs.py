# -*- coding: utf-8 -*-
"""
Caught Up AI - daily lesson-opener PDF generator.

Emits, per morning edition, two PDFs:
  - Teacher copy: passage with rhetorical devices highlighted inline and
    color-keyed to a legend, plus AP-style MCQs, discussion questions, a
    rhetorical-analysis prompt, and an answer key.
  - Student copy: clean passage (no highlights, no legend), the questions and
    prompt, no answer key.

Device labels are drawn ONLY from the approved AP device vocabulary and are
applied only where the device is genuinely present. No em-dashes, no emojis.
"""
import os, re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, Image)

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(OUT_DIR, "caughtup-logo.png")

PURPLE = HexColor("#5B3FD6")
CORAL  = HexColor("#FF6B5C")
GREY   = HexColor("#666666")
RULE   = HexColor("#D9D9D9")
HL = {1:"#CFE2F3", 2:"#FFF2A8", 3:"#CFEFD0", 4:"#FCE5CD", 5:"#F4CCCC", 6:"#E6D5F2"}

# logo geometry (preserve aspect)
_ir = ImageReader(LOGO); _iw, _ih = _ir.getSize()
LOGO_H = 0.52*inch
LOGO_W = LOGO_H * _iw / _ih

ss = getSampleStyleSheet()
body_style = ParagraphStyle("body", parent=ss["Normal"], fontName="Times-Roman",
                            fontSize=11, leading=16, alignment=TA_JUSTIFY, spaceAfter=8)
head_style = ParagraphStyle("headline", parent=ss["Title"], fontName="Times-Bold",
                            fontSize=20, leading=23, textColor=black, spaceAfter=2, alignment=TA_LEFT)
sub_style  = ParagraphStyle("sub", parent=ss["Normal"], fontName="Helvetica-Oblique",
                            fontSize=9.5, textColor=GREY, spaceAfter=2)
section_style = ParagraphStyle("section", parent=ss["Normal"], fontName="Helvetica-Bold",
                               fontSize=11, textColor=CORAL, spaceBefore=14, spaceAfter=6, leading=13)
mast_style = ParagraphStyle("mast", parent=ss["Normal"], fontName="Helvetica-Bold",
                            fontSize=16, textColor=PURPLE, leading=17)
mast_tag   = ParagraphStyle("masttag", parent=ss["Normal"], fontName="Helvetica",
                            fontSize=8.5, textColor=GREY, leading=10)
mast_date  = ParagraphStyle("mastdate", parent=ss["Normal"], fontName="Helvetica",
                            fontSize=8.5, textColor=GREY, leading=11, alignment=2)
dev_text   = ParagraphStyle("devtext", parent=ss["Normal"], fontName="Times-Roman",
                            fontSize=9.5, leading=12.5, spaceAfter=2)
q_style    = ParagraphStyle("q", parent=body_style, spaceAfter=3, alignment=TA_LEFT)
opt_style  = ParagraphStyle("opt", parent=body_style, leftIndent=16, spaceAfter=1, alignment=TA_LEFT)
key_style  = ParagraphStyle("key", parent=ss["Normal"], fontName="Times-Roman",
                            fontSize=9.5, leading=13, spaceAfter=2)

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def render_body(text, highlight=True):
    text = esc(text)
    if highlight:
        def repl(m):
            n = int(m.group(1)); inner = m.group(2)
            return ('<font backColor="%s">%s</font>'
                    '<super><font size="7" color="#888888">[%d]</font></super>'
                    % (HL[n], inner, n))
    else:
        def repl(m):
            return m.group(2)
    return re.sub(r"\[\[(\d+)\]\](.*?)\[\[/\1\]\]", repl, text, flags=re.S)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE); canvas.setLineWidth(0.5)
    canvas.line(0.8*inch, 0.6*inch, letter[0]-0.8*inch, 0.6*inch)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(0.8*inch, 0.45*inch, "Caught Up AI   .   caughtupai.com   .   Daily AP English Language lesson opener")
    canvas.drawRightString(letter[0]-0.8*inch, 0.45*inch, "p. %d" % canvas.getPageNumber())
    canvas.restoreState()

def masthead(date_str, edition):
    word = Paragraph("CAUGHT UP AI", mast_style)
    tag  = Paragraph("A daily AP English Language and Composition lesson opener", mast_tag)
    datep = Paragraph(date_str + "<br/>" + edition, mast_date)
    logo = Image(LOGO, width=LOGO_W, height=LOGO_H)
    t = Table([[logo, [word, tag], datep]], colWidths=[LOGO_W+10, 6.9*inch-(LOGO_W+10)-2.0*inch, 2.0*inch])
    t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                           ("LEFTPADDING",(0,0),(0,0),0),("RIGHTPADDING",(0,0),(0,0),8),
                           ("LEFTPADDING",(1,0),(-1,-1),0),("RIGHTPADDING",(1,0),(-1,-1),0)]))
    return [t, Spacer(1,5), HRFlowable(width="100%", thickness=1.4, color=PURPLE), Spacer(1,10)]

def device_legend(devices):
    rows = []
    for d in devices:
        n = d["n"]
        txt = ('<b>%s</b>  <font color="#888888">[%d]</font><br/><i>&ldquo;%s&rdquo;</i>  %s'
               % (esc(d["name"]), n, esc(d["phrase"]), esc(d["explain"])))
        rows.append([Paragraph("", dev_text), Paragraph(txt, dev_text)])
    t = Table(rows, colWidths=[0.28*inch, 6.6*inch])
    style = [("VALIGN",(0,0),(-1,-1),"TOP"),
             ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
             ("LEFTPADDING",(1,0),(1,-1),8)]
    for i, d in enumerate(devices):
        style.append(("BACKGROUND",(0,i),(0,i), HexColor(HL[d["n"]])))
        style.append(("BOX",(0,i),(0,i),0.5,RULE))
    t.setStyle(TableStyle(style))
    return t

def build(piece, role):
    """role in {'Teacher','Student'}"""
    teacher = (role == "Teacher")
    fname = os.path.join(OUT_DIR, "%s - %s.pdf" % (piece["base"], role))
    doc = SimpleDocTemplate(fname, pagesize=letter, leftMargin=0.8*inch, rightMargin=0.8*inch,
                            topMargin=0.7*inch, bottomMargin=0.8*inch,
                            title="%s (%s copy)" % (piece["headline"], role), author="Caught Up AI")
    s = []
    s += masthead(piece["date"], piece["edition"] + " . " + role + " copy")
    s.append(Paragraph(esc(piece["headline"]), head_style))
    if teacher:
        s.append(Paragraph("Register: <b>%s</b>  .  Focus: %s" % (esc(piece["register"]), esc(piece["focus"])), sub_style))
    else:
        s.append(Paragraph("As you read, mark the rhetorical choices the writer makes and how they shape the passage.", sub_style))
    s.append(Spacer(1,8))
    for para in piece["body"]:
        s.append(Paragraph(render_body(para, highlight=teacher), body_style))

    if teacher:
        s.append(Paragraph("RHETORICAL DEVICES IN TODAY'S PASSAGE", section_style))
        s.append(Paragraph("Highlighted phrases above are keyed by number to the devices below. Labels use the AP rhetorical-device vocabulary.", sub_style))
        s.append(Spacer(1,3))
        s.append(device_legend(piece["devices"]))

    s.append(Paragraph("CHECK FOR UNDERSTANDING  (AP-style multiple choice)", section_style))
    for i, q in enumerate(piece["mcq"], 1):
        block = [Paragraph("<b>%d.</b> %s" % (i, esc(q["stem"])), q_style)]
        for let, opt in zip("ABCD", q["options"]):
            block.append(Paragraph("(%s) %s" % (let, esc(opt)), opt_style))
        s.append(KeepTogether(block)); s.append(Spacer(1,4))

    s.append(Paragraph("DISCUSSION", section_style))
    for i, q in enumerate(piece["discussion"], 1):
        s.append(Paragraph("<b>%d.</b> %s" % (i, esc(q)), q_style))

    s.append(Paragraph("RHETORICAL ANALYSIS PROMPT", section_style))
    s.append(Paragraph(esc(piece["frq"]), body_style))

    if teacher:
        key = [Paragraph("ANSWER KEY  (teacher copy)", section_style)]
        for i, q in enumerate(piece["mcq"], 1):
            key.append(Paragraph("<b>%d. %s</b>  %s" % (i, q["answer"], esc(q["rationale"])), key_style))
        s.append(KeepTogether(key))

    doc.build(s, onFirstPage=footer, onLaterPages=footer)
    return fname

# ================================================================== content
DATE = "Friday, June 5, 2026"

ledger = {
 "base": "Caught Up AI - 2026-06-05 - Ukraine Aid Vote (Ledger)",
 "edition": "Sample edition 1 of 3", "date": DATE,
 "headline": "A Cross-Party Majority, and a Procedural Back Door",
 "register": "The Ledger", "focus": "attribution, concession, the level close",
 "body": [
  "On Thursday the House voted 226 to 195 to send Ukraine [[2]]more than $1 billion in security and reconstruction aid and to open up to $8 billion in defense loans[[/2]], along with new sanctions on key parts of the Russian economy, including its energy sector. The bill passed over the stated objections of President Trump and the House's own Republican leaders.",
  "It reached the floor at all only through a discharge petition, the rarely successful procedure that lets a majority of members force a vote when leadership refuses to schedule one. Two hundred and eighteen signatures are required. [[3]]Supporters got them.[[/3]] Eighteen Republicans then crossed over to join all but one Democrat, Ilhan Omar of Minnesota, who voted no.",
  "The bill's sponsor, [[1]]Representative Gregory Meeks of New York[[/1]], framed the money as overdue. Representative Don Bacon of Nebraska, one of the Republicans who broke ranks, put it in starker terms on the floor: “[[4]]Are we going to stand with good or are we going to stand with evil?[[/4]] That's what this is about tonight.” [[5]]The leadership's case was quieter and procedural.[[/5]] Majority Leader Steve Scalise argued that the administration's own negotiations were already moving, and that legislating around them could set them back: “you set that back,” he said, “if you pass legislation that doesn't go as far as the negotiations are going.”",
  "What the House did on Thursday it cannot finish on its own. The bill goes next to the Senate, where it needs 60 votes, and where the count is not there. A companion measure on Russian tariffs and secondary sanctions has already stalled. By the arithmetic of the chamber the aid does not advance unless Trump endorses it, which he has so far declined to do.",
  "So the vote settles less than its margin suggests. It records that a cross-party majority of one chamber wants the aid sent now, and that the same majority was willing to go around its own leadership to say so. Whether any of the money reaches Ukraine is a separate question. It belongs to the Senate, and to the president the House just voted against.",
 ],
 "devices": [
  {"n":1,"name":"Ethos","phrase":"Representative Gregory Meeks of New York","explain":"The writer earns credibility by tying the claim to a named, checkable official rather than asserting it in the writer's own voice. The piece sources its authority instead of performing it."},
  {"n":2,"name":"Logos","phrase":"more than $1 billion in security and reconstruction aid and to open up to $8 billion in defense loans","explain":"The appeal runs through exact figures and a vote count, evidence a reader can weigh, rather than through emotion."},
  {"n":3,"name":"Syntax","phrase":"Supporters got them.","explain":"A three-word sentence dropped after a long procedural one. The clipped structure makes the fact land flatly, with no comment attached."},
  {"n":4,"name":"Rhetorical question","phrase":"Are we going to stand with good or are we going to stand with evil?","explain":"Quoted from the floor, the question is posed for effect, not for an answer; it reframes a procedural vote as a moral choice."},
  {"n":5,"name":"Concession and refutation","phrase":"The leadership's case was quieter and procedural.","explain":"The opposing (leadership) position is granted plainly, then quietly refuted by the close, which shows the aid stalling without the president the House defied."},
 ],
 "mcq": [
  {"stem":"In the second paragraph, the brief sentence “Supporters got them.” primarily serves to",
   "options":["inject the writer's approval of the bill's passage",
              "mark, without comment, that a difficult procedural threshold was met",
              "question whether the signatures were legitimately obtained",
              "summarize the passage's overall argument"],
   "answer":"B","rationale":"The clipped sentence (syntax) states that 218 signatures were reached and leaves it there, the Ledger's flat-fact habit."},
  {"stem":"The writer juxtaposes Representative Bacon's question about standing “with good” or “with evil” with Majority Leader Scalise's procedural caution mainly to",
   "options":["ridicule Scalise's position as evasive",
              "frame the dispute as moral conviction against procedural caution, without resolving it",
              "prove that the bill's supporters held the stronger argument",
              "build suspense about the final vote count"],
   "answer":"B","rationale":"The neutral juxtaposition sets a pathos-driven appeal beside a procedural one and leaves the reader to weigh them."},
 ],
 "discussion": [
  "The writer never says whether the aid is a good idea. How does the passage still leave you with an impression of where the weight of the argument falls, and through what choices?",
  "Why might a writer reporting a politically charged vote choose to end on procedure (“it belongs to the Senate”) rather than on either side's strongest line?",
 ],
 "frq": "Read the passage carefully. Then write an essay in which you analyze the rhetorical choices the writer makes to convey an impartial stance while still guiding the reader toward an understanding of what the vote does and does not accomplish.",
}

longlook = {
 "base": "Caught Up AI - 2026-06-05 - Antarctic Basin (Long Look)",
 "edition": "Sample edition 2 of 3", "date": DATE,
 "headline": "The Shape Under the Ice",
 "register": "The Long Look", "focus": "controlling antithesis, short-against-long rhythm",
 "body": [
  "[[1]]We have better maps of the surface of Mars than of the rock beneath the East Antarctic ice.[[/1]] That is the ordinary condition of the place. Kilometers of ice sit on top of a continent almost nobody has seen, and what is known of the bedrock has been pieced together from radar, gravity readings, and the slow inference of signals the ice does not give up easily.",
  "Now a team writing in the journal Nature Geoscience has put a name to a piece of it. They call it the East Antarctic Fan-shaped Basin Province. It is, on their reading, a single structure: roughly thirty subglacial basins that had been catalogued one at a time, set side by side, turn out to splay from one point [[2]]like the ribs of a fan[[/2]]. The point sits within four degrees of the South Pole. The fan opens out from there toward the coast.",
  "The basins are not minor features. The province gathers in the Wilkes and Aurora basins and the trough that holds Lake Vostok, the largest body of liquid water known to lie under any ice sheet on Earth. These were familiar landmarks. What the study argues is that they were never separate landmarks at all. [[3]]They are fingers of the same hand.[[/3]]",
  "[[4]]The shape has a cause.[[/4]] The lead author, Egidio Armadillo of the University of Genoa, with colleagues including Guy Paxman at Durham, read it as the record of distributed rotational extension: crust that stretched outward from a center, slowly, in more than one episode, as the old supercontinent of Gondwana came apart and Antarctica and Australia went their separate ways. The triangular basins are the gaps that opening left behind.",
  "None of this is dead history. The bed under an ice sheet is not a floor. It is a set of channels and dams. [[5]]Where the rock dips, ice pools and slides; where it rises, ice slows.[[/5]] So a fan drawn into the crust in the deep geological past still has a say in where the ice of East Antarctica travels now, and in which parts of it are most exposed as the climate warms. That last part is where the work goes quiet. The map is new, [[6]]the consequences are not yet drawn, and the authors are careful to say which is which[[/6]].",
 ],
 "devices": [
  {"n":1,"name":"Juxtaposition","phrase":"We have better maps of the surface of Mars than of the rock beneath the East Antarctic ice.","explain":"Two unlike places set side by side, Mars and Antarctica, to sharpen one point: how little of the ground beneath the ice is known."},
  {"n":2,"name":"Simile","phrase":"like the ribs of a fan","explain":"An explicit comparison using 'like' that gives the abstract structure a familiar shape the reader can picture."},
  {"n":3,"name":"Metaphor","phrase":"They are fingers of the same hand.","explain":"An implied comparison with no 'like' or 'as': the basins are not said to resemble fingers, they are called fingers of one hand, fusing separate features into a single body. Compare with the simile in [2]."},
  {"n":4,"name":"Syntax","phrase":"The shape has a cause.","explain":"A four-word sentence set against the long technical sentence that follows. The structure carries the reader from a flat fact to its complicated cause."},
  {"n":5,"name":"Antithesis","phrase":"Where the rock dips, ice pools and slides; where it rises, ice slows.","explain":"Balanced, parallel opposites (dips against rises, slides against slows) holding the two behaviors of the ice in one line."},
  {"n":6,"name":"Ethos","phrase":"the consequences are not yet drawn, and the authors are careful to say which is which","explain":"Credibility built by candor: the writer marks the limit of what is known rather than overclaiming, which makes the rest more trustworthy."},
 ],
 "mcq": [
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
   "answer":"B","rationale":"The deliberate short-against-long sentence structure is the Long Look enacting the passage from the known to the complex."},
 ],
 "discussion": [
  "The writer never uses a word like “astonishing” or “breathtaking,” yet the discovery reads as remarkable. How is that effect produced without those words?",
  "Compare the simile in [2] with the metaphor in [3]. What does each comparison do that the other does not?",
 ],
 "frq": "Read the passage carefully. Then write an essay in which you analyze the rhetorical choices the writer makes to convey the scale and significance of a hidden landscape while withholding any explicit judgment about what it means.",
}

tribute = {
 "base": "Caught Up AI - 2026-06-05 - Marjane Satrapi (Tribute)",
 "edition": "Sample edition 3 of 3", "date": DATE,
 "headline": "She Drew Small",
 "register": "The Tribute", "focus": "small-and-large antithesis, parallelism, restraint",
 "body": [
  "She told the story of a revolution in the drawings of a child, and that turned out to be the truest way to tell it. Marjane Satrapi, who died in Paris on Thursday at fifty-six, made her name with a black-and-white comic about a girl in Tehran. The girl was herself.",
  "Persepolis began appearing in 2000, four slim volumes of line drawings: a daughter of educated, watchful parents growing up as the Iran of her childhood was remade around her, then sent abroad to Europe, alone and young. [[2]]The drawings were plain.[[/2]] [[3]]A veil, a schoolyard, a soldier at a corner.[[/3]] Out of those small panels came a portrait of a country that years of reporting had left, for most outside readers, a blur.",
  "That was her method, and her quiet argument: that [[1]]the enormous is best approached through the small[[/1]]. [[4]]A revolution rendered as a quarrel with her grandmother. Exile rendered as a teenager friendless in a borrowed language.[[/4]] She trusted the particular to carry the general, and it did.",
  "And in 2007 she and Vincent Paronnaud turned the books into an animated film, keeping the stark black and white when color would have been easier and more salable. It shared the Jury Prize at Cannes. It was nominated for the Academy Award for best animated feature, and with that nomination Satrapi became the first woman the category had ever named. She went on to other things: a novel and film called Chicken with Plums, books drawn at a kitchen table, films in registers far from where she began, and, near the end, a book that gathered Iranian artists under the slogan woman, life, freedom.",
  "Her family said she died of grief, a year after the death of her husband, Mattias Ripa. It is the kind of cause a doctor does not certify and a reader of her work does not doubt. She had always written as if private feeling and public history were the same material, seen at different distances.",
  "[[1]]She drew small so that the world could see something large.[[/1]] Her books remain [[5]]the clearest window many readers will ever have[[/5]] onto [[6]]a place they were taught to fear[[/6]], and they will go on doing that work quietly, in black and white, long after the hand that drew them is still.",
 ],
 "devices": [
  {"n":1,"name":"Antithesis","phrase":"the enormous is best approached through the small","explain":"Contrasting ideas in balanced form, small against large. Set up here and paid off at the close (“She drew small so that the world could see something large”), it is the engine of the whole tribute."},
  {"n":2,"name":"Understatement / litotes","phrase":"The drawings were plain","explain":"Calling drawings that carried a nation's story 'plain' deliberately downplays them, so the smallness of the means magnifies the result."},
  {"n":3,"name":"Asyndeton","phrase":"A veil, a schoolyard, a soldier at a corner.","explain":"Three images listed with no conjunction, which speeds the line and lets the concrete pictures pile up."},
  {"n":4,"name":"Parallelism","phrase":"A revolution rendered as a quarrel with her grandmother. Exile rendered as a teenager friendless in a borrowed language.","explain":"Repeated grammatical structure across two sentences ('[X] rendered as [a scene]'). Note it is parallelism, not anaphora: the repeated element falls in the middle, not at the start of each clause."},
  {"n":5,"name":"Metaphor","phrase":"the clearest window many readers will ever have","explain":"Her books are called a window, an implied comparison that turns the comics into a way of seeing a place."},
  {"n":6,"name":"Pathos","phrase":"a place they were taught to fear","explain":"An appeal to the reader's emotion: naming the country as one readers were taught to fear invites sympathy and a change of feeling."},
 ],
 "mcq": [
  {"stem":"The three-word sentence “The girl was herself.” most directly functions to",
   "options":["cast doubt on the accuracy of Satrapi's account",
              "reveal the autobiographical basis of the work in a single, quiet stroke",
              "introduce a fictional character for contrast",
              "shift the passage from praise to complaint"],
   "answer":"B","rationale":"The clipped sentence (syntax) delivers the key fact, that the memoir is her own life, with the restraint the tribute prizes."},
  {"stem":"Describing “private feeling and public history” as “the same material, seen at different distances” chiefly serves to",
   "options":["state the governing antithesis that small personal scenes can carry large historical meaning",
              "criticize historians for neglecting private life",
              "summarize the plot of Persepolis for the reader",
              "urge readers to write their own memoirs"],
   "answer":"A","rationale":"It restates the small-and-large antithesis that organizes the tribute, a claim the piece has already demonstrated rather than asserted."},
 ],
 "discussion": [
  "The writer handles an unverifiable cause of death (“her family said she died of grief”) in a single sentence. How does the next line turn that uncertainty into a statement about her work?",
  "A tribute risks tipping into sentimentality. Point to two specific choices here (consider the understatement in [2]) that keep the praise restrained rather than gushing.",
 ],
 "frq": "Read the passage carefully. Then write an essay in which you analyze the rhetorical choices the writer makes to honor Marjane Satrapi and to argue, without stating it outright, that her small and personal art carried large public meaning.",
}

if __name__ == "__main__":
    for p in (ledger, longlook, tribute):
        for role in ("Teacher", "Student"):
            print("wrote:", build(p, role))
