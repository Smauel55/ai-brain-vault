import json, os
from render_opener_v2 import build, randomize_answers
here = os.path.dirname(os.path.abspath(__file__))
piece = json.load(open(os.path.join(here, "_latest_piece.json"), encoding="utf-8"))
randomize_answers(piece)
for role in ("Teacher", "Student"):
    fn, pages = build(piece, role)
    print("wrote:", fn, "(%d pages)" % pages)
