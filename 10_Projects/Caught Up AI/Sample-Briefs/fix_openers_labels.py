# -*- coding: utf-8 -*-
"""
Device-label cleanup (Samuel 2026-06-08). Audit against the controlled vocabulary
in Rhetorical-Device-Vocabulary.md found off-list labels, one wrong device, and two
non-devices. Relabel the fixable ones; drop the two that name no list device.

RELABELS change devices[n-1]['device'] only (span untouched). DROPS remove the
device entry AND its [[n]]...[[/n]] span tags from the body (text kept). Both drops
are the LAST device in their piece, so no renumbering is needed. assert-on-match
so a stale file fails loudly. Idempotent. Usage: python fix_openers_labels.py [--dry]
"""
import json, re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "openers.json")

# (id, n, old_label, new_label)
RELABELS = [
    (1,  5, "Statistical evidence", "Logos"),
    (2,  1, "Periodic sentence",    "Cumulative and periodic sentences"),
    (4,  3, "Allusion",             "Logos"),   # borderline; flagged for override
    (4,  5, "Polysyndeton",         "Asyndeton"),
    (26, 5, "Redefinition",         "Antithesis"),
]
# (id, n, old_label) -- must be the last device in the piece
DROPS = [
    (2,  6, "Charge / obligation"),
    (17, 6, "Syntax"),
]

CANON = {'Ethos','Pathos','Logos','Diction','Syntax','Tone','Parallelism','Anaphora',
'Juxtaposition','Antithesis','Rhetorical question','Metaphor','Simile','Imagery','Allusion',
'Hyperbole','Irony','Repetition','Concession','Concession and refutation','Anecdote',
'Epistrophe','Asyndeton','Polysyndeton','Chiasmus','Analogy','Personification',
'Cumulative and periodic sentences','Telegraphic sentence','Anecdotal vs statistical evidence','Shift / volta'}


def main():
    dry = "--dry" in sys.argv
    data = json.load(open(SRC, encoding="utf-8"))
    by_id = {p["_meta"]["id"]: p for p in data}

    for pid, n, old, new in RELABELS:
        dev = by_id[pid]["devices"][n-1]
        if dev["device"] == new:
            continue                                  # already applied
        assert dev["device"] == old, "id %d dev %d: expected %r, found %r" % (pid, n, old, dev["device"])
        dev["device"] = new

    for pid, n, old in DROPS:
        devs = by_id[pid]["devices"]
        if len(devs) < n or devs[n-1]["device"] != old:
            # tolerate an already-dropped piece (idempotent)
            assert all(d["device"] != old for d in devs), "id %d: unexpected state for drop %r" % (pid, old)
            continue
        assert n == len(devs), "drop must be the last device (id %d, n=%d, count=%d)" % (pid, n, len(devs))
        devs.pop(n-1)
        by_id[pid]["body"] = [par.replace("[[%d]]" % n, "").replace("[[/%d]]" % n, "")
                              for par in by_id[pid]["body"]]

    # post-check: every label now on the controlled list.
    bad = [(p["_meta"]["id"], i, d["device"])
           for p in data for i, d in enumerate(p["devices"], 1) if d["device"] not in CANON]
    print("off-list labels remaining:", bad or "NONE")

    if dry:
        print("[dry run] no write."); return
    assert not bad, "off-list labels still present; not writing"
    json.dump(data, open(SRC, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("wrote openers.json (label cleanup: %d relabels, %d drops)" % (len(RELABELS), len(DROPS)))


if __name__ == "__main__":
    main()
