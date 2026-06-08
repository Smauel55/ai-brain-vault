# Builds the AP Lang teacher interview guide PDF.
# Run: python build_interview_guide.py
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether)

OUT = "Caught Up AI - Teacher Interview Guide (2026-06-08).pdf"

INK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#666666")
LIGHT = colors.HexColor("#cfcfcf")
ACCENT = colors.HexColor("#1f4e5f")
BOXBG = colors.HexColor("#eef3f4")

ss = getSampleStyleSheet()

def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10.5, leading=14, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

H_TITLE = style("title", fontName="Helvetica-Bold", fontSize=19, leading=22, textColor=ACCENT)
H_SUB = style("sub", fontSize=10, textColor=GREY, leading=13)
H_BLOCK = style("block", fontName="Helvetica-Bold", fontSize=12.5, leading=15,
                textColor=ACCENT, spaceBefore=10, spaceAfter=3)
H_NOTE = style("note", fontSize=9.5, textColor=GREY, leading=12, leftIndent=18, italic=True)
P_Q = style("q", fontSize=10.5, leading=14, leftIndent=18, firstLineIndent=-18, spaceBefore=6)
P_SAY = style("say", fontSize=10.5, leading=14.5, textColor=INK)
P_SAYQ = style("sayq", fontSize=11, leading=15.5, textColor=ACCENT, fontName="Helvetica-Oblique")
P_BODY = style("body", fontSize=10.5, leading=14)
P_CHK = style("chk", fontSize=10, leading=13.5, leftIndent=20, firstLineIndent=-13)

# patch oblique where needed
H_NOTE.fontName = "Helvetica-Oblique"

def notelines(n=1, gap=0.30):
    out = []
    for _ in range(n):
        out.append(Spacer(1, gap * inch))
        out.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT,
                              spaceBefore=0, spaceAfter=0))
    return out

def q(num, text, cue=None, lines=1):
    items = [Paragraph(f"<b>{num}.</b>&nbsp;&nbsp;{text}", P_Q)]
    if cue:
        items.append(Paragraph(cue, H_NOTE))
    items += notelines(lines)
    return items

story = []

# ---- Header ----
story.append(Paragraph("Caught Up AI", H_TITLE))
story.append(Paragraph("AP Lang Teacher Interview Guide&nbsp;&nbsp;|&nbsp;&nbsp;June 8, 2026&nbsp;&nbsp;|&nbsp;&nbsp;Private guide, Samuel Levy", H_SUB))
story.append(Spacer(1, 0.06*inch))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT, spaceAfter=8))

story.append(Paragraph(
    "<b>What I want out of this meeting:</b> (1) an expert read on whether the Openers hold up, "
    "(2) whether AI authorship matters to a teacher, (3) the real prep pain and what she pays, "
    "(4) recruit her as a pilot teacher and panel judge.", P_BODY))
story.append(Spacer(1, 0.10*inch))

# ---- Opener box ----
opener = ("“I’m Samuel Levy, headed to Northwestern this fall, building this on my own. "
          "I’m not an AP Lang teacher and I’ve never run a classroom, which is exactly why I want your read.<br/><br/>"
          "Caught Up AI is a daily ten-minute lesson opener for AP Lang: a short current-events nonfiction piece "
          "plus the full teaching layer, a student copy and a teacher copy, in your inbox by 6 a.m. "
          "One four-minute setup form, then nothing else to do.<br/><br/>"
          "The thing I want to be straight about up front: the pieces are written by AI from verified facts, "
          "not pulled from real publications. I went down the licensing road and it does not work for a product "
          "that marks up the text. So the real question I need your help with is whether AI-written pieces are good enough, "
          "and honest enough, to put in front of AP students. I would rather you tell me where it breaks than be polite.”")
box = Table([[Paragraph("<b>OPEN WITH THIS &mdash; say it out loud</b>", H_BLOCK)],
             [Paragraph(opener, P_SAY)],
             [Paragraph("Then hand her a <b>teacher-copy Opener</b> and let her read before you say anything else.", P_BODY)]],
            colWidths=[6.5*inch])
box.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BOXBG),
    ("BOX", (0,0), (-1,-1), 0.5, ACCENT),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(box)
story.append(Spacer(1, 0.12*inch))

# ---- Run of show ----
story.append(Paragraph("Run of show", H_BLOCK))
rows = [["#", "Block", "Time"],
        ["0", "Opener (say it)", "2 min"],
        ["1", "Discovery: workflow, pain, spend", "8-10 min"],
        ["2", "The Opener + expert review  (most important)", "15-20 min"],
        ["3", "AI, authenticity, accuracy", "8-10 min"],
        ["4", "Product fit: topics + support", "5 min"],
        ["5", "Pricing", "5 min"],
        ["6", "The ask: pilot, panel, referrals", "5 min"]]
t = Table(rows, colWidths=[0.4*inch, 4.6*inch, 1.5*inch])
t.setStyle(TableStyle([
    ("FONT", (0,0), (-1,0), "Helvetica-Bold", 9.5),
    ("FONT", (0,1), (-1,-1), "Helvetica", 10),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("BACKGROUND", (0,0), (-1,0), ACCENT),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f4f7f8")]),
    ("LINEBELOW", (0,0), (-1,-1), 0.4, LIGHT),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING", (0,0), (-1,-1), 4),
    ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 0.06*inch))
story.append(Paragraph("<b>If it compresses to 25 min:</b> Opener &rarr; Block 2 &rarr; Q8 (the pedagogy question) &rarr; the ask. Block 2 is non-negotiable.", H_SUB))
story.append(Paragraph("<b>Say before the questions:</b> “These are about what you have actually done, not what you’d hypothetically do. Pull a real example if you can.”", H_SUB))

# ---- Blocks ----
story.append(Spacer(1, 0.10*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 1 &mdash; Discovery: workflow, pain, spend", H_BLOCK))
for it in q(1, "Walk me through how you build a lesson opener or bell-ringer now. Where does the time actually go?",
            "(her real workflow, not the ideal one)"): story.append(it)
for it in q(2, "When you use a current-events nonfiction piece, what do you still have to build yourself: the questions, the device markup, the answer key, the alignment? Which eats the most time?",
            "(isolates the layer the product sells)"): story.append(it)
for it in q(3, "What teaching tools do you pay for out of pocket? Have you cancelled one this past year, and what made you cancel: a factual error, a pedagogical miss, unreliability?",
            "(real spend + the error category that sets the QA bar)"): story.append(it)

story.append(Spacer(1, 0.06*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 2 &mdash; The Opener + expert review  (most important)", H_BLOCK))
story.append(Paragraph("Hand her a <b>teacher-copy</b> Opener (lead with the Ledger). Let her read first.", H_NOTE))
for it in q(4, "First reaction. Would you put this in front of students tomorrow? What is wrong with it?",
            "(unprompted, before you steer)"): story.append(it)
for it in q(5, "Is the length and reading level right for AP Lang? Is the register variety across days useful, or noise?"): story.append(it)

# expert checklist
chk = [Paragraph("<b>Expert-validation checklist</b> &mdash; walk the teacher copy with her; get a yes/no + a fix on each. This is the read I can’t do myself.", H_BLOCK)]
checks = [
 "<b>Device labels:</b> every marked device named correctly and actually present? Any mislabels (anaphora vs parallelism)? Anything obvious left unmarked?",
 "<b>MCQs:</b> one defensibly-best answer each? Does every distractor fail for a real reason, or can a student eliminate by feel? AP-exam-valid in form?",
 "<b>Answer key reasoning:</b> does it hold up, or would it lose an argument with a sharp student?",
 "<b>Sample strong responses:</b> would these actually earn the points?",
 "<b>Common misconceptions:</b> the real ones students hit, or invented?",
 "<b>AP exam alignment:</b> is the Q1/Q2/Q3 framing accurate? Better for analysis, argument, or synthesis?",
]
for c in checks:
    chk.append(Paragraph("[ &nbsp; ]&nbsp;&nbsp;" + c, P_CHK))
chk.append(Paragraph("2+ objections on any one layer = that layer needs rework before pilot. Capture exact fixes in her words.", H_NOTE))
story.append(KeepTogether(chk))
story.append(Spacer(1, 0.18*inch))

story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 3 &mdash; AI, authenticity, accuracy", H_BLOCK))
for it in q(6, "Knowing these are AI-written, would you have known? Does it read as machine-written anywhere, and where?",
            "(she is primed, so this is a ceiling; the clean test is the blind panel. Optional: show 2 pieces, ask which feels more human.)"): story.append(it)
for it in q(7, "Does it bother you that the piece is AI-written? Would it bother your students, your department, or your admin?"): story.append(it)
for it in q(8, "<b>The sharp one.</b> AP rhetorical analysis asks students to analyze the choices a real writer made for a real audience and purpose. An AI piece has no real author and no real occasion. Does analyzing an AI’s “choices” still teach the skill, or undercut it? Would you use these more for argument and reading practice than for pure rhetorical analysis?",
            "(deepest risk to the concept. Do not argue it. Let her draw the line.)", lines=2): story.append(it)
for it in q(9, "How much would a single factual error cost you in trust? One error and you are out, or is a correction fine?",
            "(prices the per-piece fact-verification we already do)"): story.append(it)

story.append(Spacer(1, 0.06*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 4 &mdash; Product fit: topics + support", H_BLOCK))
for it in q(10, "How do you handle politically charged topics now? Would a one-time signup setting &mdash; neutral vs includes civic/current-events &mdash; earn your trust, or do you need per-piece control?",
            "(validates the political-intensity dial direction)"): story.append(it)
for it in q(11, "Would an optional support layer &mdash; glossary of hard terms, FRQ sentence starters, vocab pre-list &mdash; be useful, or unnecessary for AP students?",
            "(tests scaffolding-layer demand)"): story.append(it)

story.append(Spacer(1, 0.06*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 5 &mdash; Pricing", H_BLOCK))
for it in q(12, "If this landed ready-to-teach in your inbox every morning, what is it worth per month? Would you pay out of pocket, or does it have to go through the school?",
            "(let her name a number first)"): story.append(it)
for it in q(13, "Reaction to $19.99/month solo, $190/year? Too high, too low, about right?",
            "(only after she names her own number)"): story.append(it)
for it in q(14, "After a month of using it, what would make you cancel?"): story.append(it)

story.append(Spacer(1, 0.06*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))
story.append(Paragraph("Block 6 &mdash; The ask", H_BLOCK))
for it in q(15, "Would you be a fall pilot: use real Openers in class for about four weeks and give me honest feedback?",
            "(the primary ask)"): story.append(it)
for it in q(16, "Would you sit on a small panel of AP Lang teachers doing a blind read, to settle whether the AI pieces pass?",
            "(the decisive validation instrument)"): story.append(it)
for it in q(17, "Who else should I talk to: AP Lang teachers or AP coordinators whose read on teaching tools you trust?"): story.append(it)

# ---- Footer cards ----
story.append(Spacer(1, 0.12*inch))
story.append(HRFlowable(width="100%", thickness=1.0, color=ACCENT))

risk = Table([[Paragraph("<b>The one risk to keep in mind</b>", H_BLOCK)],
              [Paragraph("Q8 (AI author vs real author) can sink the concept, and she will have a real opinion. Do not defend it. "
                         "If she says AI authorship undercuts rhetorical analysis, that is signal: it may push the product toward "
                         "argument (Q3) and reading practice over authorial-intent analysis (Q2), and toward honest “practice text” framing.", P_BODY)]],
             colWidths=[6.5*inch])
risk.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#fbf3e7")),
    ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#c79a4b")),
    ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story.append(risk)
story.append(Spacer(1, 0.12*inch))

story.append(Paragraph("Bring / do before the meeting", H_BLOCK))
for c in [
  "Print 2-3 <b>teacher-copy</b> Openers across registers (lead Ledger; one hotter register for range) + their student copies.",
  "Read them end to end. Own every device label, MCQ, and answer-key line as if you wrote it.",
  "Have the pilot ask and the panel ask ready to say in one sentence each.",
  "Decide your real price floor before Block 5 so her number does not anchor you.",
  "Bring this guide on paper and write on it.",
]:
    story.append(Paragraph("[ &nbsp; ]&nbsp;&nbsp;" + c, P_CHK))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        topMargin=0.6*inch, bottomMargin=0.6*inch,
                        leftMargin=0.85*inch, rightMargin=0.85*inch,
                        title="Caught Up AI - Teacher Interview Guide")
doc.build(story)
print("wrote", OUT)
