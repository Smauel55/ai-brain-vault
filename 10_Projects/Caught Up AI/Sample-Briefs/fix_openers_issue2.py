# -*- coding: utf-8 -*-
"""
Issue 2 (widened), Samuel 2026-06-08: openers must carry NO in-text citations of
ANY kind. The earlier fix_openers.py stripped (Author, year) parentheticals; this
removes the remaining INLINE scholarly apparatus (named scholars/studies/journals
and lit-review framing) from #12 and #24, stating each fact plainly. Facts stay
true; device [[n]]...[[/n]] spans are untouched (every edit is outside a span).

Targeted substring swaps with assert-on-count so a non-match fails loudly and
nothing is written. Idempotent. Usage: python fix_openers_issue2.py [--dry]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "openers.json")

# (id, old, new) -- each old must occur exactly once across that piece's body.
EDITS = [
    # --- #12 The Friend I Did Not Lose: one lit-review gesture ---
    (12,
     "just a slow widening of the kind the research describes: shared activity",
     "just a slow widening of the most ordinary kind: shared activity"),

    # --- #24 The Clock, Not the Calendar: four scholarly tells ---
    # p1: drop "Portfolio studies do find that"
    (24,
     "Portfolio studies do find that the share of stocks an investor holds falls with age while the share of bonds rises",
     "The share of stocks an investor holds falls with age while the share of bonds rises"),
    # p3: drop "The finding that ... one of the most replicated results in the study of decision-making"
    (24,
     "Loss aversion itself does not deepen with age. The finding that losses weigh about twice as heavily as equal gains is one of the most replicated results in the study of decision-making, and it shows up at every age, in the young as much as the old.",
     "Loss aversion itself does not deepen with age. Losses weigh about twice as heavily as equal gains, and that holds at every age, in the young as much as the old."),
    # p4: drop the named scholar "Carstensen's work"
    (24,
     "Carstensen's work on how a shrinking sense of time reshapes what people want points the same way: when the runway looks short, goals contract toward the sure thing.",
     "A shrinking sense of how much time is left reshapes what a person wants the same way: when the runway looks short, goals contract toward the sure thing."),
    # p5: cut the "economists publish in journals" academic-framing aside
    (24,
     "so history leaves its own thumbprint on nerve. The economists publish in journals most of us will never open. What survives the qualifications",
     "so history leaves its own thumbprint on nerve. What survives the qualifications"),
]

# Detectors for the post-check: parenthetical cites, et al., journal/working-paper
# tags, and the specific scholar surnames this batch pulled in.
CITE = re.compile(r"\([A-Z][^)]*\b(?:18|19|20)\d\d[a-z]?[^)]*\)")
SCHOLARLY = re.compile(
    r"\bet al\.?|\bNBER\b|\bworking paper\b|\bin the Journal of\b"
    r"|Kahneman|Tversky|Carstensen|Ameriks|Zeldes|Poterba|Samwick"
    r"|Kuhnen|Samanez|Malmendier|Nagel|Carroll|Rawlins|Serafica|Rohlfing"
    r"|Blieszner|Buhrmester|Felmlee|Muraco|Rachuy", re.I)


def apply_edit(body, old, new):
    hits = sum(p.count(old) for p in body)
    assert hits == 1, "expected 1 match, got %d for: %.60r" % (hits, old)
    return [p.replace(old, new) for p in body]


def main():
    dry = "--dry" in sys.argv
    data = json.load(open(SRC, encoding="utf-8"))
    by_id = {p["_meta"]["id"]: p for p in data}

    for pid, old, new in EDITS:
        by_id[pid]["body"] = apply_edit(by_id[pid]["body"], old, new)

    # post-check: no citation patterns or scholar names remain in 12/24; tags intact.
    OPEN = re.compile(r"\[\[(\d+)\]\]"); SLASH = re.compile(r"\[\[/(\d+)\]\]")
    print("post-edit scan:")
    ok_all = True
    for pid in (12, 24):
        full = "\n".join(by_id[pid]["body"])
        cite = CITE.findall(full); schol = SCHOLARLY.findall(full)
        o, c, d = len(OPEN.findall(full)), len(SLASH.findall(full)), len(by_id[pid]["devices"])
        ok = not cite and not schol and o == c == d
        ok_all = ok_all and ok
        print("  id=%-2d paren_cites=%d scholarly=%s opens=%d closers=%d devices=%d  %s"
              % (pid, len(cite), schol or "-", o, c, d, "ok" if ok else "<<< CHECK"))

    if dry:
        print("\n[dry run] no write."); return
    assert ok_all, "post-check failed; not writing"
    json.dump(data, open(SRC, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\nwrote openers.json (Issue 2 inline-citation removal for 12, 24)")


if __name__ == "__main__":
    main()
