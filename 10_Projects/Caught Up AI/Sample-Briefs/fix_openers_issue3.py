# -*- coding: utf-8 -*-
"""
Issue 3: #2 and #4 have full devices arrays but ZERO [[n]] spans in the body, so
the teacher copy's marked-article section points at nothing. Hand-place one span
per device, located from each device's stated para + purpose, in device order.
Spans are non-overlapping and match the existing devices[n-1]. Facts untouched.

Targeted wraps with assert-on-count (each target must occur exactly once in that
piece's body) so a non-match fails loudly and nothing is written. Idempotent:
if a piece is already tagged it is skipped. Usage: python fix_openers_issue3.py [--dry]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "openers.json")

# (id, n, target) -> wrap target with [[n]]...[[/n]]. Order = device order.
WRAPS = [
    # ---- #2 The First State to Name the Man (6 devices) ----
    (2, 1, "Citizens of a state that let a product into the hands of its children, hear what was filed in your name."),
    (2, 2, "We told ourselves the machine was tested. We told ourselves someone responsible had read the warnings."),
    (2, 3, "A sixteen-year-old boy named Adam Raine talked to a chatbot for weeks, and in April of 2025 he died by his own hand, and the complaint alleges the chatbot helped him plan his death and drafted the note he left behind. The same April, the complaint alleges, the same kind of conversation guided a gunman onto the campus of Florida State University, where two people were killed and six more were carried away wounded."),
    (2, 4, "four counts of deceptive and unfair trade practices, two of negligence, two under product liability, one of fraudulent misrepresentation, one of public nuisance."),
    (2, 5, "A company that says it leads the industry in protecting children, and a sixteen-year-old whose suicide note, the state alleges, was written for him by the product."),
    (2, 6, "refuse to call a thing safe for a child until someone has staked their own name on it being true."),

    # ---- #4 The Purse You Promised to Guard (5 devices) ----
    (4, 1, "You have called your project radical constitutionalism. You have said your aim is to restore the document to its original meaning and to hold the federal government to the limits the founders set down."),
    (4, 2, "It speaks plainly about money."),
    (4, 3, "no money shall be drawn from the Treasury but in consequence of appropriations made by law"),
    (4, 4, "You have argued, candidly, that the Impoundment Control Act is itself unconstitutional, and you are entitled to believe it."),
    (4, 5, "spent on nothing, helping no child, vindicating no principle"),
]


def wrap_in_body(body, n, target):
    open_t, close_t = "[[%d]]" % n, "[[/%d]]" % n
    hits = sum(par.count(target) for par in body)
    assert hits == 1, "id-span %d: expected 1 match, got %d for %.50r" % (n, hits, target)
    return [par.replace(target, open_t + target + close_t) for par in body]


def main():
    dry = "--dry" in sys.argv
    data = json.load(open(SRC, encoding="utf-8"))
    by_id = {p["_meta"]["id"]: p for p in data}

    for pid in (2, 4):
        if any("[[" in par for par in by_id[pid]["body"]):
            print("id=%d already has tags; skipping (idempotent)." % pid); continue
        for (epid, n, target) in WRAPS:
            if epid != pid:
                continue
            by_id[pid]["body"] = wrap_in_body(by_id[pid]["body"], n, target)

    # render-truth crosscheck on the two pieces.
    import render_opener_v2 as r
    OPEN = re.compile(r"\[\[(\d+)\]\]"); SLASH = re.compile(r"\[\[/(\d+)\]\]")
    MARK = re.compile(r"\[\[(\d+)\]\](.*?)\[\[/\1\]\]", flags=re.S)
    print("post-tag crosscheck:")
    ok_all = True
    for pid in (2, 4):
        body = by_id[pid]["body"]; full = "\n".join(body)
        o, c, d = len(OPEN.findall(full)), len(SLASH.findall(full)), len(by_id[pid]["devices"])
        matches = sum(len(MARK.findall(par)) for par in body)
        leak = any("[[" in r.make_para(par, i, by_id[pid]["devices"], True)
                   or "]]" in r.make_para(par, i, by_id[pid]["devices"], True)
                   for i, par in enumerate(body, 1))
        ok = (o == c == d == matches) and not leak
        ok_all = ok_all and ok
        print("  id=%-2d opens=%d closers=%d devices=%d parsed=%d leak=%s  %s"
              % (pid, o, c, d, matches, leak, "ok" if ok else "<<< CHECK"))

    if dry:
        print("\n[dry run] no write."); return
    assert ok_all, "crosscheck failed; not writing"
    json.dump(data, open(SRC, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\nwrote openers.json (Issue 3 spans placed for #2, #4)")


if __name__ == "__main__":
    main()
