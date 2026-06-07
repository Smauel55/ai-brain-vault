# -*- coding: utf-8 -*-
"""
Caught Up AI - daily lesson-opener PDF generator (format v2).

Changes from render_briefs.py (v1), per Samuel 2026-06-06:
  1. ONE highlight color for every device (no more one-color-per-device). A single
     light-blue highlight marks every tagged span; a single dark-blue label names it.
  2. Device labels use ONLY the approved AP device vocabulary, and name the SPECIFIC
     device, never the umbrella category. A short clipped sentence is a "telegraphic
     sentence," not "syntax."
  3. TEACHER copy gets a "Devices, and why they're here" section that, for each tagged
     device, names it, quotes the phrase, and explains its PURPOSE: why the author chose
     it and what it accomplishes. Kept to a line or two so it reads at a glance.

STUDENT copy: clean numbered article, MCQ, discussion, writing prompt. No marks.
TEACHER copy: the marked article (single-color highlight + inline device name), the
  Devices-and-why section, MCQ + answer key, discussion + sample responses, the writing
  prompt, common misconceptions, AP exam alignment.

No em-dashes, no emojis.
"""
import os, re, random
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
HL_BG    = "#FFF3A0"   # single highlight color for every tagged device (yellow)
HL_LABEL = "#1F4E79"   # single label color for every inline device name

_ir = ImageReader(LOGO); _iw, _ih = _ir.getSize()
LOGO_H = 0.40*inch; LOGO_W = LOGO_H*_iw/_ih

ss = getSampleStyleSheet()
# Article body. Teacher uses 'body' (15.5 leading); student uses 'bodystu' (17
# leading) for annotation room between lines. Both 11pt (decided 2026-06-06).
body   = ParagraphStyle("body", parent=ss["Normal"], fontName="Times-Roman",
                        fontSize=11, leading=15.5, alignment=TA_LEFT, spaceAfter=7,
                        allowWidows=0, allowOrphans=0)
bodystu= ParagraphStyle("bodystu", parent=body, leading=17)
# Apparatus (MCQ, discussion, prompt, teacher notes): tighter leading to stay compact.
appb   = ParagraphStyle("appb", parent=body, leading=14.5, spaceAfter=6)
title = ParagraphStyle("title", parent=ss["Title"], fontName="Times-Bold",
                       fontSize=18, leading=21, textColor=black, alignment=TA_LEFT, spaceAfter=3)
roletag = ParagraphStyle("roletag", parent=ss["Normal"], fontName="Helvetica-Bold",
                         fontSize=9, textColor=GREY, spaceAfter=10)
sect  = ParagraphStyle("sect", parent=ss["Normal"], fontName="Helvetica-Bold",
                       fontSize=12, textColor=black, spaceBefore=12, spaceAfter=3, leading=14,
                       keepWithNext=1)
q     = ParagraphStyle("q", parent=appb, spaceAfter=2)
opt   = ParagraphStyle("opt", parent=appb, leftIndent=18, spaceAfter=1)
bullet= ParagraphStyle("bullet", parent=appb, leftIndent=14, spaceAfter=2)
devp  = ParagraphStyle("devp", parent=appb, leftIndent=14, spaceAfter=5)
wordm = ParagraphStyle("wordm", parent=ss["Normal"], fontName="Helvetica-Bold",
                       fontSize=12, textColor=black, leading=13)
wtag  = ParagraphStyle("wtag", parent=ss["Normal"], fontName="Helvetica",
                       fontSize=7.5, textColor=GREY, leading=9)
mdate = ParagraphStyle("mdate", parent=ss["Normal"], fontName="Helvetica",
                       fontSize=8.5, textColor=GREY, leading=11, alignment=2)

def esc(t): return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def _footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(0.9*inch, 0.5*inch, "Caught Up AI   .   caughtupai.com")
    canvas.drawRightString(letter[0]-0.9*inch, 0.5*inch, "p. %d" % canvas.getPageNumber())
    canvas.restoreState()

def make_decorators(running_text):
    """First page: footer only (the logo header is in the flow). Later pages: footer
    plus a small running header so a dropped or mixed print stack stays identifiable."""
    def first(canvas, doc):
        _footer(canvas, doc)
    def later(canvas, doc):
        _footer(canvas, doc)
        canvas.saveState()
        canvas.setFont("Helvetica", 8); canvas.setFillColor(GREY)
        y = letter[1] - 0.45*inch
        canvas.drawString(0.9*inch, y, running_text)
        canvas.setStrokeColor(RULE); canvas.setLineWidth(0.5)
        canvas.line(0.9*inch, y-3, letter[0]-0.9*inch, y-3)
        canvas.restoreState()
    return first, later

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

MARK = re.compile(r"\[\[(\d+)\]\](.*?)\[\[/\1\]\]", flags=re.S)

def extract_quotes(bodylist):
    """Pull the inner text of each [[n]]...[[/n]] span, keyed by n, from the raw body."""
    out = {}
    for para in bodylist:
        for m in MARK.finditer(para):
            out[int(m.group(1))] = m.group(2).strip()
    return out

def make_para(raw, idx, devices, highlight):
    text = esc(raw)
    if highlight:
        def repl(m):
            k = int(m.group(1)); inner = m.group(2); d = devices[k-1]
            return ('<font backColor="%s">%s</font> '
                    '<font size="8" color="%s"><b>[%s]</b></font>'
                    % (HL_BG, inner, HL_LABEL, esc(d["device"])))
    else:
        def repl(m): return m.group(2)
    text = MARK.sub(repl, text)
    return '<b><font size="8">%d</font></b>&nbsp;&nbsp;%s' % (idx, text)

def devices_section(devices, quotes):
    """Teacher-only: name each device, quote it, and explain its purpose at a glance."""
    rows = []
    for i, d in enumerate(devices, 1):
        quote = quotes.get(i, "")
        head = ('<b><font color="%s">%s</font></b> (paragraph %d): &ldquo;%s&rdquo;'
                % (HL_LABEL, esc(d["device"]), d["para"], esc(quote)))
        rows.append(Paragraph("%s<br/>%s" % (head, esc(d["purpose"])), devp))
    return rows

def randomize_answers(piece, rng=random):
    """Shuffle each MCQ's four options and recompute the answer letter, so the correct
    choice lands on a random letter, as on the real AP exam (two questions can share a
    letter by chance). Call ONCE per piece BEFORE building the teacher and student
    copies, so both copies get the same option order and the key matches. Rationales
    must reference distractors by content, not by letter, for this to stay correct."""
    for item in piece["mcq"]:
        correct = item["options"][ord(item["answer"]) - 65]
        rng.shuffle(item["options"])
        item["answer"] = chr(65 + item["options"].index(correct))

def sec(title, blocks):
    """A section header with a thin rule. The header style sets keepWithNext and the
    rule is flagged the same way, so the header is never left at the bottom of a page
    without content under it, while a long first block is NOT forced whole (no big gaps)."""
    head = Paragraph(title, sect)
    rule = HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=1, spaceAfter=5)
    rule.keepWithNext = 1
    return [head, rule] + list(blocks)

def build(piece, role):
    teacher = (role == "Teacher")
    art = body if teacher else bodystu
    fname = os.path.join(OUT_DIR, "%s - %s copy.pdf" % (piece["base"], role))
    running = ("Caught Up AI Opener   .   %s   .   %s   .   %s copy"
               % (piece["date"], piece["headline"], role))
    first_fn, later_fn = make_decorators(running)
    doc = SimpleDocTemplate(fname, pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch,
                            topMargin=0.7*inch, bottomMargin=0.75*inch,
                            title="%s (%s copy)" % (piece["headline"], role), author="Caught Up AI")
    s = []
    s += header(piece["date"], piece["edition"] + " . " + role + " copy")
    s.append(Paragraph(esc(piece["headline"]), title))
    s.append(Paragraph("Teacher copy (everything in the student copy, plus answers and teaching notes)"
                       if teacher else "Student copy (project or hand out)", roletag))

    # Article: each paragraph kept intact across page breaks.
    art_paras = [Paragraph(make_para(para, i, piece["devices"], teacher), art)
                 for i, para in enumerate(piece["body"], 1)]
    if teacher:
        s += sec("The article, marked for rhetorical devices (one color throughout):", art_paras)
    else:
        s += art_paras

    # Devices, and why they are here (teacher only): each entry atomic.
    if teacher:
        quotes = extract_quotes(piece["body"])
        dev_blocks = [KeepTogether(r) for r in devices_section(piece["devices"], quotes)]
        s += sec("Devices, and why they are here:", dev_blocks)

    # MCQ: stem plus all four options kept together.
    mcq_blocks = []
    for i, item in enumerate(piece["mcq"], 1):
        blk = [Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(item["stem"])), q)]
        for let, o in zip("ABCD", item["options"]):
            blk.append(Paragraph("%s)&nbsp;&nbsp;%s" % (let, esc(o)), opt))
        blk.append(Spacer(1, 4))
        mcq_blocks.append(KeepTogether(blk))
    s += sec("AP-style multiple choice:", mcq_blocks)

    # Answer key (teacher only): each item atomic.
    if teacher:
        key_blocks = [KeepTogether([Paragraph("<b>%d. Answer %s.</b>&nbsp;&nbsp;%s"
                       % (i, item["answer"], esc(item["rationale"])), q)])
                      for i, item in enumerate(piece["mcq"], 1)]
        s += sec("Multiple choice answer key:", key_blocks)

    # Discussion.
    disc_blocks = [KeepTogether([Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(d)), q)])
                   for i, d in enumerate(piece["discussion"], 1)]
    s += sec("Discussion questions:", disc_blocks)

    # Sample responses (teacher only).
    if teacher:
        sr_blocks = [KeepTogether([Paragraph("<b>%d.</b>&nbsp;&nbsp;%s" % (i, esc(r)), q)])
                     for i, r in enumerate(piece["sample_responses"], 1)]
        s += sec("Sample strong discussion responses:", sr_blocks)

    # Writing prompt.
    s += sec("Writing prompt (%s):" % esc(piece["writing"]["type"]),
             [Paragraph(esc(piece["writing"]["text"]), appb)])

    # Misconceptions and AP alignment (teacher only).
    if teacher:
        mis_blocks = [KeepTogether([Paragraph("&bull;&nbsp;&nbsp;" + esc(m), bullet)])
                      for m in piece["misconceptions"]]
        s += sec("Common misconceptions to watch for:", mis_blocks)
        s += sec("AP exam alignment:", [Paragraph(esc(piece["ap_alignment"]), appb)])

    doc.build(s, onFirstPage=first_fn, onLaterPages=later_fn)
    return fname, doc.page

# ================================================================== content
DATE = "Saturday, June 6, 2026"

longthink = {
 "base":"Caught Up AI Opener - 2026-06-06 - What the Waiting Did (Long Think)",
 "edition":"Sample edition (new format)", "date":DATE,
 "headline":"What the Waiting Did",
 "body":[
  "Waiting used to be the ordinary weather of a life. [[1]]You wrote a letter and waited weeks for the reply. You wanted a song and waited for the radio to play it. You missed a fact and waited, sometimes for years, to learn it.[[/1]] None of this was a virtue. It was the plain cost of being alive, back before that cost was quietly abolished.",
  "The abolition is a gift, and it would be foolish to pretend otherwise. A parent now reaches a child in a held breath. A test result arrives before the dread has time to settle. The busy signal, the layaway counter, the long line at the bank: speed has retired a hundred small daily humiliations, and almost nobody who lived through them misses the waiting itself. [[2]]We bought back the time we used to lose, and we were right to want it.[[/2]]",
  "[[3]]And yet something went out of the world along with the waiting, something we were never given a price for.[[/3]] The wait had never been only an absence; [[4]]it was a room[[/4]]. Inside that room the mind did its slow and unsupervised work, rehearsing and dreading and hoping and changing its own position before anyone else could watch. The letter you waited three weeks for was answered, in part, by the three weeks. Boredom, the most maligned of states, was often just thinking with the lights off.",
  "We did not only lose the wait; we lost what the wait used to make in us. Patience, yes, but also [[5]]the second thought, the cooled temper, the letter never sent[[/5]]. [[6]]Speed keeps its promises.[[/6]] It is the promises of slowness that go unrecorded, because a thing that never happens leaves behind no receipt.",
  "So the real question is not whether to go back. Nobody is going back, and the radio is not returning to make us wait for the song. We are very good now at not waiting. The question is smaller, and harder. It is whether a life that need never pause has quietly stopped doing the work that only the pause once did. And whether we would even notice the loss now, with nothing left in the day to make us wait for it.",
 ],
 "devices":[
  {"para":1,"device":"Anaphora",
   "purpose":"The three sentences all open with “You,” pulling the reader into the habit of waiting and making three unlike losses feel like one shared condition. The repeated opening builds a rhythm that the short line after it (“None of this was a virtue”) then breaks. The repeated word sits at the START of each sentence, which is what makes this anaphora and not parallelism."},
  {"para":2,"device":"Concession",
   "purpose":"The writer grants the other side its strongest case in full: speed retired real miseries and we were right to want it. Note what is NOT the concession: the earlier line “it would be foolish to pretend otherwise” only insists the grant is sincere; the grant itself is the claim highlighted here. Conceding this much, plainly and in good faith, is what lets the later turn read as fair rather than as a reflex complaint."},
  {"para":3,"device":"Shift / volta",
   "purpose":"The turn is the whole highlighted clause, not the connective “And yet” that introduces it. By themselves those two words do nothing; the volta is the claim they open, that something went out of the world with the waiting. This is where the piece pivots from praising speed to counting its cost."},
  {"para":3,"device":"Metaphor",
   "purpose":"Recasting the empty wait as “a room” turns an abstract loss into a space the reader can picture and the mind can occupy. The metaphor carries the essay's central claim: that waiting was where private thinking got done."},
  {"para":4,"device":"Parallelism",
   "purpose":"Three matched noun phrases make the vague idea of “what the wait produced” concrete and countable. Because the repeated structure sits inside the sentence rather than at the start of successive clauses, this is parallelism, not anaphora."},
  {"para":4,"device":"Telegraphic sentence",
   "purpose":"The four-word sentence lands flat and fast, its clipped speed imitating the very thing it names. Its brevity throws the weight onto the long, slower sentence that answers it, where the real point waits."},
 ],
 "mcq":[
  {"stem":"The relationship between the second paragraph and the third paragraph is best described as one in which the writer first",
   "options":["praises the arrival of speed and then predicts that its benefits will soon fade",
              "states a personal grievance and then broadens it into a shared complaint",
              "grants the full value of speed and then identifies a cost that value had concealed",
              "offers a tentative claim and then supplies the evidence that confirms it"],
   "answer":"C","rationale":"Paragraph 2 fully concedes that the end of waiting is a gift and that we were right to want it; paragraph 3 turns on “And yet” to name what went out of the world along with the waiting. The concession is followed by the cost the concession had hidden."},
  {"stem":"Which of the following best characterizes the writer's overall attitude toward the disappearance of waiting?",
   "options":["Nostalgically certain that life before instant access was richer and ought to be restored",
              "Coolly neutral, laying out the trade-off without signaling a preference either way",
              "Sharply alarmed, warning that the end of waiting has already done irreversible harm",
              "Genuinely appreciative of speed yet uneasy that an unnoticed loss may have come with it"],
   "answer":"D","rationale":"The writer calls the end of waiting a gift and grants that we were right to want it, yet turns to what went out of the world and closes by asking whether we have quietly stopped doing the work the pause once did. Appreciation is held in tension with unresolved unease."},
 ],
 "discussion":[
  "The writer spends a whole paragraph agreeing that almost no one misses waiting before arguing that we lost something real. How does conceding the other side first change the way the later claim lands?",
  "The essay reframes waiting as “a room” where the mind works. Find one other place where the writer turns an abstract idea into something concrete, and explain what that lets the reader see or feel.",
 ],
 "sample_responses":[
  "A strong answer notes the concession is strategic: by granting in full that speed retired real humiliations and that no one misses the wait, the writer removes the easy objection that this is mere nostalgia. Having been fair, the later claim that we lost the mind's private work reads as an earned conclusion rather than a complaint.",
  "Besides “a room,” the writer makes the loss concrete in the parallel series “the second thought, the cooled temper, the letter never sent” and in “thinking with the lights off.” Each turns an abstraction (patience, restraint, boredom) into a nameable thing, so the reader feels the loss as specific rather than vague.",
 ],
 "writing":{"type":"homework or extended in-class, Q3 argument",
  "text":"The writer suggests that a life that “need never pause” may have “quietly stopped doing the work that only the pause once did.” Defend, challenge, or qualify the claim that something valuable is lost when waiting disappears from everyday life. Use your own knowledge, observation, or reading."},
 "misconceptions":[
  "Students often call the three “You...” sentences in paragraph 1 parallelism. They are anaphora: the repeated word opens each sentence. Reserve “parallelism” for repeated structure that does not begin the clause, like the series in paragraph 4.",
  "Students may take the concession in paragraph 2 as the writer's settled view. It is ground granted on purpose; the writer agrees in order to turn, not to give up the argument. Watch too for students who point to “it would be foolish to pretend otherwise” as the concession. That line only claims the grant is sincere; the concession is the substance, that speed was a real good worth wanting.",
  "Students often name “And yet” as the shift. The connective only signals that a turn is coming. The volta is the claim that follows it, that something went out of the world with the waiting. Mark the whole clause, not the two words.",
  "Students may label “it was a room” a simile. There is no “like” or “as”; it is a metaphor, an implied identity.",
 ],
 "ap_alignment":"Q2 rhetorical-analysis value: a compact text for teaching a clean concession, the anaphora-versus-parallelism distinction, a clearly marked shift (volta), and a single load-bearing metaphor students can name and defend. The clipped telegraphic sentence set against the long cumulative one is a clean lesson in how sentence length alone creates emphasis.",
}

if __name__ == "__main__":
    randomize_answers(longthink)
    for role in ("Teacher", "Student"):
        fn, pages = build(longthink, role)
        print("wrote: %s  (%d page%s)  answers %s"
              % (os.path.basename(fn), pages, "" if pages == 1 else "s",
                 [it["answer"] for it in longthink["mcq"]]))
