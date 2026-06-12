import json, os
from render_opener_v2 import build, randomize_answers
here = os.path.dirname(os.path.abspath(__file__))
pieces = json.load(open(os.path.join(here, "_batch_pieces.json"), encoding="utf-8"))
out = []
for piece in pieces:
    randomize_answers(piece)
    for role in ("Teacher", "Student"):
        fn, pages = build(piece, role)
        out.append(fn); print("wrote:", fn, "(%d pages)" % pages)
print("TOTAL", len(out))
