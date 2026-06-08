# Builds the AP Lang teacher interview guide PDF (bullet coverage sheet).
# Run: python build_interview_guide.py
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                HRFlowable, KeepTogether)

OUT = "Caught Up AI - Teacher Interview Guide (2026-06-08).pdf"

INK = colors.HexColor("#1a1a1a")
GREY = colors.HexColor("#777777")
LIGHT = colors.HexColor("#d2d2d2")
ACCENT = colors.HexColor("#1f4e5f")

def style(name, **kw):
    base = dict(fontName="Helvetica", fontSize=11, leading=14.5, textColor=INK)
    base.update(kw); return ParagraphStyle(name, **base)

H_TITLE = style("title", fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=ACCENT)
H_SUB = style("sub", fontSize=9.5, textColor=GREY, leading=12)
H_BLOCK = style("block", fontName="Helvetica-Bold", fontSize=12, leading=15,
                textColor=ACCENT, spaceBefore=11, spaceAfter=4)
P_BULL = style("bull", fontSize=11, leading=14.5, leftIndent=20, firstLineIndent=-14)
P_SUB = style("subb", fontSize=9.8, leading=13, leftIndent=40, firstLineIndent=-12, textColor=INK)
P_HINT = style("hint", fontSize=9.5, leading=12, leftIndent=20, textColor=GREY,
               fontName="Helvetica-Oblique")

def cue(text):
    return f' <font size=8 color="#888888"><i>{text}</i></font>'

def bullet(text, note=False, gap=0.26):
    items = [Paragraph("[ &nbsp; ]&nbsp;&nbsp;" + text, P_BULL)]
    if note:
        items.append(Spacer(1, gap*inch))
        items.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT))
    return items

def sub(text):
    return Paragraph("&ndash;&nbsp;&nbsp;" + text, P_SUB)

story = []
story.append(Paragraph("Caught Up AI &mdash; AP Lang Teacher Interview Guide", H_TITLE))
story.append(Paragraph("June 8, 2026&nbsp;&nbsp;|&nbsp;&nbsp;Points to cover", H_SUB))
story.append(Spacer(1, 0.05*inch))
story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT))

# Block 1
story.append(Paragraph("Discovery: workflow, pain, spend", H_BLOCK))
for b in [
    "How he builds an opener / bell-ringer now; where the time goes",
    "With a current-events piece, what he still builds himself (questions, device markup, key, alignment); what eats most time",
    "Tools he pays for out of pocket; anything cancelled this year and why (factual error, pedagogical miss, unreliability)",
]:
    for it in bullet(b, note=True): story.append(it)

# Block 2
story.append(Paragraph("The Opener + expert review  (hand him the teacher copy first)", H_BLOCK))
for b in [
    "First reaction; would he teach it tomorrow; what is wrong with it",
    "Length and reading level right for AP Lang; register variety across days useful or noise",
]:
    for it in bullet(b, note=True): story.append(it)
chk = [Paragraph("Walk the teacher copy with him &mdash; yes/no + a fix on each:" , P_HINT)]
for s in [
    "Device labels correct and actually present; any mislabels (anaphora vs parallelism); anything obvious unmarked",
    "MCQs: one defensibly-best answer; each distractor fails for a real reason; AP-valid in form",
    "Answer-key reasoning holds up against a sharp student",
    "Sample strong responses would actually earn the points",
    "Common misconceptions are the real ones, not invented",
    "AP alignment accurate (Q1/Q2/Q3; better for analysis, argument, or synthesis)",
]:
    chk.append(sub(s))
story.append(KeepTogether(chk))
story.append(Spacer(1, 0.14*inch))

# Block 3
story.append(Paragraph("AI, authenticity, accuracy", H_BLOCK))
for it in bullet("Would he have known it is AI; does it read machine-written anywhere, and where", note=True): story.append(it)
for it in bullet("Does AI authorship bother him / students / department / admin", note=True): story.append(it)
for it in bullet("Pedagogy: analyzing an AI's choices with no real author or occasion &mdash; still teaches the skill or undercuts it; better for argument/reading practice than rhetorical analysis"
                 + cue("don't argue it; let him draw the line"), note=True): story.append(it)
for it in bullet("Tolerance for a single factual error (one and out, or is a correction fine)", note=True): story.append(it)

# Block 4
story.append(Paragraph("Product fit", H_BLOCK))
for it in bullet("Charged topics: how he handles them now; would a one-time neutral-vs-civic setting earn trust, or need per-piece control", note=True): story.append(it)
for it in bullet("Optional support layer (glossary, FRQ sentence starters, vocab pre-list) &mdash; useful or unnecessary for AP", note=True): story.append(it)

# Block 5
story.append(Paragraph("Pricing", H_BLOCK))
for it in bullet("What it is worth per month; out of pocket or through the school" + cue("let him name a number first"), note=True): story.append(it)
for it in bullet("Reaction to $19.99/mo solo, $190/yr" + cue("only after his own number"), note=True): story.append(it)
for it in bullet("What would make him cancel after a month", note=True): story.append(it)

# Block 6
story.append(Paragraph("The ask", H_BLOCK))
for it in bullet("Fall pilot: real Openers in class ~4 weeks + honest feedback", note=True): story.append(it)
for it in bullet("Blind-read panel of AP Lang teachers to settle whether the AI pieces pass", note=True): story.append(it)
for it in bullet("Referrals: AP Lang teachers or coordinators whose read on tools he trusts", note=True): story.append(it)

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        topMargin=0.6*inch, bottomMargin=0.6*inch,
                        leftMargin=0.85*inch, rightMargin=0.85*inch,
                        title="Caught Up AI - Teacher Interview Guide")
doc.build(story)
print("wrote", OUT)
