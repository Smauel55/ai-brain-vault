# -*- coding: utf-8 -*-
"""
One-shot repair for the 28-opener dry run (Issue 1 + Issue 2 from
Opener-Batch-Test-Results.md). Idempotent: safe to re-run; a clean file
produces no changes.

Issue 1 (highlight tags). Two failure shapes:
  (a) Duplicate-closer pieces (ids 1,3,6,9,16,20,25,27,28): each device span
      was closed with a second [[n]] instead of [[/n]], so the renderer's
      MARK regex never matched. Per paragraph, for each n that appears
      exactly twice, the 2nd [[n]] becomes [[/n]]. Verified safe: every such
      piece has each n exactly twice, both occurrences in one paragraph.
  (b) #17: 6 devices but the tags were laid down as 3 open/close pairs, so the
      numbers do NOT map to devices. Cannot be regex-repaired; each span is
      re-placed by hand below from the device 'purpose' text. Done as targeted
      substring swaps with assert-on-count so a non-match fails loudly.

Issue 2 (in-text academic citations, ids 12,24): strip parenthetical
  citations like "(Kahneman and Tversky, 1979)" and tidy the whitespace the
  strip leaves behind. Inline attributions (no parens) are left alone.

Usage:  python fix_openers.py            # edits openers.json in place
        python fix_openers.py --dry      # report only, write nothing
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "openers.json")

DUP_CLOSER_IDS = [1, 3, 6, 9, 16, 20, 25, 27, 28]
CITATION_IDS   = [12, 24]

# A parenthetical that contains a Capitalized name and a 18xx/19xx/20xx year.
CITE = re.compile(r"\s*\([A-Z][^)]*\b(?:18|19|20)\d\d[a-z]?[^)]*\)")


def fix_duplicate_closers(body):
    """For each paragraph, turn the 2nd [[n]] of any number appearing exactly
    twice into [[/n]]. Splitting on the literal '[[n]]' is order-independent
    because [[n]] and [[/n]] for distinct n never collide."""
    out = []
    for para in body:
        nums = sorted({int(x) for x in re.findall(r"\[\[(\d+)\]\]", para)})
        for n in nums:
            tok = "[[%d]]" % n
            parts = para.split(tok)
            if len(parts) == 3:                       # exactly two occurrences
                para = parts[0] + tok + parts[1] + ("[[/%d]]" % n) + parts[2]
        out.append(para)
    return out


def fix_17(body):
    """Re-place all 6 spans in #17 by hand. Each swap asserts it matched once."""
    def swap(paras, old, new):
        hits = sum(p.count(old) for p in paras)
        assert hits == 1, "expected 1 match, got %d for: %.50r" % (hits, old)
        return [p.replace(old, new) for p in paras]

    b = list(body)
    # para 2: device 1 (Juxtaposition) = harm/discomfort sentence;
    #         device 2 (Antithesis)   = the two protection sentences.
    b = swap(b,
        "[[1]]There is a kind of harm a child can suffer from a book, and there is the discomfort a child, or more often an adult, feels at encountering a life unlike their own; these are not the same thing, and the whole question turns on whether we keep them apart.[[2]] The shared premise was that children deserve protection from harm. It was never that children deserve protection from difference.",
        "[[1]]There is a kind of harm a child can suffer from a book, and there is the discomfort a child, or more often an adult, feels at encountering a life unlike their own; these are not the same thing, and the whole question turns on whether we keep them apart.[[/1]] [[2]]The shared premise was that children deserve protection from harm. It was never that children deserve protection from difference.[[/2]]")
    # para 3: device 3 (Logos) = the Tango sentence; device 4 (anecdotal vs
    #         statistical) = the 4,235 / forty-percent sentence.
    b = swap(b,
        "in the country.[[4]] The stated",
        "in the country.[[/3]] The stated")
    b = swap(b,
        "Of 4,235 titles challenged last year, 1,671, about forty percent, told the stories of LGBTQIA+ people and people of color.",
        "[[4]]Of 4,235 titles challenged last year, 1,671, about forty percent, told the stories of LGBTQIA+ people and people of color.[[/4]]")
    # para 4: device 5 (Logos) = the ALA 92-percent sentence; device 6 = the
    #         three-titles aside (currently mis-tagged [[5]]...[[6]]).
    b = swap(b,
        "The record from the American Library Association says otherwise: in 2025, ninety-two percent of challenges came from pressure groups and government officials, up from seventy-two the year before, and fewer than three percent from individual parents.",
        "[[5]]The record from the American Library Association says otherwise: in 2025, ninety-two percent of challenges came from pressure groups and government officials, up from seventy-two the year before, and fewer than three percent from individual parents.[[/5]]")
    b = swap(b,
        "[[5]]The three most challenged titles, for what it is worth, were Sold, The Perks of Being a Wallflower, and Gender Queer.[[6]]",
        "[[6]]The three most challenged titles, for what it is worth, were Sold, The Perks of Being a Wallflower, and Gender Queer.[[/6]]")
    return b


def strip_citations(body):
    out = []
    for para in body:
        new = CITE.sub("", para)
        # tidy whitespace the strip can leave: space before punctuation, runs.
        new = re.sub(r"\s+([.;,:])", r"\1", new)
        new = re.sub(r"[ \t]{2,}", " ", new).strip()
        out.append(new)
    return out


def main():
    dry = "--dry" in sys.argv
    data = json.load(open(SRC, encoding="utf-8"))
    by_id = {p["_meta"]["id"]: p for p in data}
    changed = []

    for pid in DUP_CLOSER_IDS:
        p = by_id[pid]
        new = fix_duplicate_closers(p["body"])
        if new != p["body"]:
            p["body"] = new; changed.append(pid)

    p17 = by_id[17]
    new17 = fix_17(p17["body"])
    if new17 != p17["body"]:
        p17["body"] = new17; changed.append(17)

    for pid in CITATION_IDS:
        p = by_id[pid]
        new = strip_citations(p["body"])
        if new != p["body"]:
            p["body"] = new; changed.append(pid)

    # post-checks: every fixed piece's opens == closers and == device count.
    OPEN = re.compile(r"\[\[(\d+)\]\]"); SLASH = re.compile(r"\[\[/(\d+)\]\]")
    print("post-fix tag balance:")
    for pid in sorted(set(DUP_CLOSER_IDS + CITATION_IDS + [17])):
        full = "\n".join(by_id[pid]["body"])
        o, c = len(OPEN.findall(full)), len(SLASH.findall(full))
        d = len(by_id[pid]["devices"])
        cite = "CITE!" if CITE.search(full) else "ok"
        flag = "" if (o == c == d and cite == "ok") else "  <<< CHECK"
        print("  id=%-2d opens=%d closers=%d devices=%d cites=%s%s" % (pid, o, c, d, cite, flag))

    if dry:
        print("\n[dry run] would change ids:", sorted(set(changed)))
        return
    json.dump(data, open(SRC, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("\nwrote openers.json; changed ids:", sorted(set(changed)))


if __name__ == "__main__":
    main()
