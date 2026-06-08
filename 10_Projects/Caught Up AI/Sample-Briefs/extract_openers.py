# -*- coding: utf-8 -*-
"""
Harvest the 28 finished opener dicts from the interrupted workflow's on-disk
journal + agent transcripts. NO model calls. Pure parsing.

For each opener id we prefer the redraft result (if the piece was redrafted),
else the draft result. We map agentId -> (role,id) by scanning each agent
transcript's task prompt, and agentId -> result via journal.jsonl.
Writes openers.json (ordered by id, with _meta and a render-safe base/date).
"""
import os, re, json, glob

WF = r"C:\Users\srlev\.claude\projects\C--Users-srlev-OneDrive-Documents-Claude-AI-Brain-1-0\b6aa5509-0e10-45f9-982d-e81f5a8f1ec4\subagents\workflows\wf_8b080f31-5ee"
HERE = os.path.dirname(os.path.abspath(__file__))
MATRIX = json.load(open(os.path.join(HERE, "openers_matrix.json"), encoding="utf-8"))
META = {r["id"]: r for r in MATRIX}
DATE = "Sunday, June 7, 2026"
ISO = "2026-06-07"

DRAFT_RE   = re.compile(r"DRAFT stage for Caught Up AI opener #(\d+)")
REDRAFT_RE = re.compile(r"REDRAFTING Caught Up AI opener #(\d+)")

# 1) journal: agentId -> result value
results = {}
with open(os.path.join(WF, "journal.jsonl"), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or '"type":"result"' not in line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        if o.get("type") == "result" and "agentId" in o:
            results[o["agentId"]] = o.get("result")

# 2) agent transcripts: agentId -> (role,id) by prompt signature
drafts = {}    # id -> [agentId,...]
redrafts = {}  # id -> [agentId,...]
for fp in glob.glob(os.path.join(WF, "agent-*.jsonl")):
    aid = os.path.basename(fp)[len("agent-"):-len(".jsonl")]
    try:
        head = open(fp, encoding="utf-8").read(6000)
    except Exception:
        continue
    m = REDRAFT_RE.search(head)
    if m:
        redrafts.setdefault(int(m.group(1)), []).append(aid)
        continue
    m = DRAFT_RE.search(head)
    if m:
        drafts.setdefault(int(m.group(1)), []).append(aid)

REQ = ["base","edition","date","headline","body","devices","mcq",
       "discussion","sample_responses","writing","misconceptions","ap_alignment"]
TAG = re.compile(r"\[\[(\d+)\]\]")

def valid(d):
    if not isinstance(d, dict):
        return False, "not a dict"
    for k in REQ:
        if k not in d:
            return False, "missing key: " + k
    if not isinstance(d["body"], list) or not d["body"]:
        return False, "empty body"
    ndev = len(d["devices"])
    maxn = 0
    for para in d["body"]:
        for t in TAG.findall(para):
            maxn = max(maxn, int(t))
    if maxn > ndev:
        return False, "body tag [[%d]] exceeds devices(%d)" % (maxn, ndev)
    if not isinstance(d["mcq"], list) or len(d["mcq"]) < 2:
        return False, "mcq<2"
    for q in d["mcq"]:
        if len(q.get("options", [])) != 4:
            return False, "mcq options != 4"
        if q.get("answer") not in ("A","B","C","D"):
            return False, "bad answer letter"
    return True, "ok"

def pick(idn):
    """Return (dict, source) preferring a valid redraft, else valid draft."""
    for aid in redrafts.get(idn, []):
        d = results.get(aid)
        ok, _ = valid(d)
        if ok:
            return d, "redraft"
    for aid in drafts.get(idn, []):
        d = results.get(aid)
        ok, _ = valid(d)
        if ok:
            return d, "draft"
    # report best-effort reason
    for aid in redrafts.get(idn, []) + drafts.get(idn, []):
        d = results.get(aid)
        ok, why = valid(d)
        if not ok:
            return None, "invalid:" + why
    return None, "no result on disk"

final = []
missing = []
print("id  reg            basis src       headline")
for idn in range(1, 29):
    d, src = pick(idn)
    mt = META[idn]
    if d is None:
        missing.append((idn, src))
        print("%2d  %-14s %-5s %-9s  <MISSING: %s>" % (idn, mt["register"], mt["basis"], "-", src))
        continue
    # render-safe base/date/edition fallback
    if not d.get("base"):
        d["base"] = "Caught Up AI Opener - %s - %s (%s)" % (ISO, d.get("headline","Untitled"), mt["register"])
    d.setdefault("edition", "Batch test edition")
    d["date"] = DATE
    d["_meta"] = {"id": idn, "register": mt["register"], "basis": mt["basis"]}
    final.append(d)
    print("%2d  %-14s %-5s %-9s  %s" % (idn, mt["register"], mt["basis"], src, d.get("headline","")[:70]))

print("\nComplete: %d/28   Missing: %s" % (len(final), [m[0] for m in missing] or "none"))
out = os.path.join(HERE, "openers.json")
json.dump(final, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("Wrote", out)
