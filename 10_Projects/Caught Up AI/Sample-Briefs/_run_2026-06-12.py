# One-off driver for the 2026-06-12 batch (Long Look, Long Think, Tribute).
# Imports build() and randomize_answers() from render_opener_v2 without modifying it.
import json, os
from render_opener_v2 import build, randomize_answers

here = os.path.dirname(os.path.abspath(__file__))
pieces = json.load(open(os.path.join(here, "_pieces_2026-06-12.json"), encoding="utf-8"))

for piece in pieces:
    randomize_answers(piece)  # shuffle MCQ options; key lands on a random letter
    for role in ("Teacher", "Student"):
        fn, pages = build(piece, role)
        print("wrote: %s  (%d page%s)  answers %s"
              % (os.path.basename(fn), pages, "" if pages == 1 else "s",
                 [it["answer"] for it in piece["mcq"]]))
