# -*- coding: utf-8 -*-
"""
Emit each test-batch opener as a single self-contained HTML file.
Opens in Google Docs (Drive -> Open with Google Docs) with the yellow highlight
and inline device labels preserved. Single source of truth: render_opener_docx.py.
"""
import os, re, html
from render_opener_docx import PIECES, MARK, strip_marks, DATE

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
HL = "#FFF3A0"; LAB = "#1F4E79"

def esc(t): return html.escape(t, quote=False)

def marked(raw, devices):
    out = []; pos = 0
    for m in MARK.finditer(raw):
        if m.start() > pos: out.append(esc(raw[pos:m.start()]))
        k = int(m.group(1)); dev = devices[k-1]["device"]
        out.append('<span style="background-color:%s">%s</span>' % (HL, esc(m.group(2))))
        out.append(' <b style="color:%s;font-size:9px">[%s]</b>' % (LAB, esc(dev)))
        pos = m.end()
    if pos < len(raw): out.append(esc(raw[pos:]))
    return "".join(out)

def render(p):
    S = []
    A = S.append
    A('<html><head><meta charset="utf-8"></head><body>')
    A('<p><i>Caught Up AI &middot; The daily AP English Language Opener &middot; %s &middot; TEST RUN (sample)</i></p>' % esc(DATE))
    A('<h1>%s</h1>' % esc(p["headline"]))
    A('<p><i>Register: %s</i></p>' % esc(p["register"]))

    quotes = {}
    for para in p["body"]:
        for m in MARK.finditer(para):
            quotes[int(m.group(1))] = m.group(2).strip()

    # STUDENT
    A('<h2>Student copy</h2>')
    A('<p><i>Read the passage, then answer the questions.</i></p>')
    for i, para in enumerate(p["body"], 1):
        A('<p><b>%d</b>&nbsp;&nbsp;%s</p>' % (i, esc(strip_marks(para))))
    A('<h3>Multiple choice</h3>')
    for i, it in enumerate(p["mcq"], 1):
        A('<p>%d.&nbsp;&nbsp;%s</p>' % (i, esc(it["stem"])))
        for let, o in zip("ABCD", it["options"]):
            A('<p>&nbsp;&nbsp;&nbsp;&nbsp;%s)&nbsp;&nbsp;%s</p>' % (let, esc(o)))
    A('<h3>Discussion</h3>')
    for i, d in enumerate(p["discussion"], 1):
        A('<p>%d.&nbsp;&nbsp;%s</p>' % (i, esc(d)))
    A('<h3>Writing prompt (%s)</h3>' % esc(p["writing"]["type"]))
    A('<p>%s</p>' % esc(p["writing"]["text"]))

    # TEACHER
    A('<hr>')
    A('<h2>Teacher copy</h2>')
    A('<p><i>Everything in the student copy, plus the marked article, answers, and teaching notes.</i></p>')
    A('<h3>The article, marked for rhetorical devices (one color throughout)</h3>')
    for i, para in enumerate(p["body"], 1):
        A('<p><b>%d</b>&nbsp;&nbsp;%s</p>' % (i, marked(para, p["devices"])))
    A('<h3>Devices, and why they are here</h3>')
    for i, d in enumerate(p["devices"], 1):
        A('<p><b style="color:%s">%s</b> (paragraph %d): &ldquo;%s&rdquo;<br>%s</p>'
          % (LAB, esc(d["device"]), d["para"], esc(quotes.get(i,"")), esc(d["purpose"])))
    A('<h3>Multiple choice answer key</h3>')
    for i, it in enumerate(p["mcq"], 1):
        A('<p><b>%d. Answer %s.</b>&nbsp;&nbsp;%s</p>' % (i, it["answer"], esc(it["rationale"])))
    A('<h3>Sample strong discussion responses</h3>')
    for i, s in enumerate(p["sample_responses"], 1):
        A('<p>%d.&nbsp;&nbsp;%s</p>' % (i, esc(s)))
    A('<h3>Common misconceptions to watch for</h3><ul>')
    for m in p["misconceptions"]:
        A('<li>%s</li>' % esc(m))
    A('</ul>')
    A('<h3>AP exam alignment</h3>')
    A('<p>%s</p>' % esc(p["ap_alignment"]))
    A('<h3>Test-run sourcing note</h3>')
    A('<p><i>%s</i></p>' % esc(p["sourcing"]))
    A('</body></html>')
    return "".join(S)

if __name__ == "__main__":
    for p in PIECES:
        h = render(p)
        f = os.path.join(OUT_DIR, "GDoc - %s.html" % p["slug"])
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(h)
        print("wrote:", os.path.basename(f), "| chars", len(h))
