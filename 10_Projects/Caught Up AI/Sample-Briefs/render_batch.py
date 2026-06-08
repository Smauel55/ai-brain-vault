# -*- coding: utf-8 -*-
"""
Batch render driver for the 28-opener dry run.

Loads a JSON array of opener dicts (schema = render_opener_v2.build's input),
calls render_opener_v2.randomize_answers(piece) ONCE per piece, then builds the
Teacher and Student PDFs. Prints a per-opener table: id, register, basis,
headline, FRQ type, the two answer letters (post-shuffle), and page counts.

Usage:  python render_batch.py openers.json

Determinism note: randomize_answers uses the module `random`. We seed once so a
re-run reproduces the same key letters; remove the seed for true per-run shuffle.
"""
import os, sys, json, random, re, time
import render_opener_v2 as r

ILLEGAL = '\\/:*?"<>|'

def build_with_retry(piece, role, attempts=6):
    """OneDrive intermittently locks a file mid-write (OSError errno 22) because
    this folder is sync-backed. Retry with a short backoff; the lock clears in a
    moment. Without this, a single transient lock leaves the 56-PDF batch half
    rendered (some fresh, some stale)."""
    for k in range(attempts):
        try:
            return r.build(piece, role)
        except OSError:
            if k == attempts - 1:
                raise
            time.sleep(0.7)

def normalize_closers(piece):
    """Self-heal the Issue-1 duplicate-closer bug: a span closed with a second
    [[n]] instead of [[/n]] never matches render_opener_v2.MARK, so it prints raw.
    Per paragraph, for any n that appears exactly twice as [[n]] (and has no
    [[/n]] yet), rewrite the 2nd [[n]] as [[/n]]. Returns the count repaired so
    the driver can warn. Does NOT touch pieces whose tags are already balanced,
    and cannot fix mis-numbered tags (e.g. the old #17), which must be repaired
    at the source. Keeps the renderer itself strict."""
    fixed = 0
    for i, para in enumerate(piece.get("body", [])):
        for n in sorted({int(x) for x in re.findall(r"\[\[(\d+)\]\]", para)}):
            tok = "[[%d]]" % n
            if ("[[/%d]]" % n) in para:
                continue                              # already has a real closer
            parts = para.split(tok)
            if len(parts) == 3:                       # exactly two bare opens
                para = parts[0] + tok + parts[1] + ("[[/%d]]" % n) + parts[2]
                fixed += 1
        piece["body"][i] = para
    return fixed

def safe_base(base):
    """Make piece['base'] safe as a Windows filename stem. Display fields
    (headline, date, edition) are untouched; only the filename stem changes."""
    out = base
    out = out.replace(':', ' -').replace('"', "'")
    for ch in ILLEGAL:
        out = out.replace(ch, '-')
    # collapse runs of spaces/dashes that the swaps can create
    while '  ' in out:
        out = out.replace('  ', ' ')
    return out.strip()

def main():
    if len(sys.argv) < 2:
        print("usage: python render_batch.py openers.json"); sys.exit(2)
    path = sys.argv[1]
    with open(path, 'r', encoding='utf-8') as f:
        openers = json.load(f)

    random.seed(20260607)  # stable keys across re-runs of this batch
    rows = []
    for piece in openers:
        meta = piece.pop('_meta', {})           # id/register/basis carried alongside
        healed = normalize_closers(piece)       # belt-and-suspenders for Issue 1
        if healed:
            print("  [normalize] id %s: repaired %d duplicate-closer tag(s) at render"
                  % (meta.get('id', '?'), healed))
        piece['base'] = safe_base(piece['base'])
        r.randomize_answers(piece)              # ONCE, before both roles
        answers = [it['answer'] for it in piece['mcq']]
        pages = {}
        for role in ('Teacher', 'Student'):
            fn, npages = build_with_retry(piece, role)
            pages[role] = npages
        frq = piece.get('writing', {}).get('type', '')
        rows.append({
            'id': meta.get('id', ''),
            'register': meta.get('register', ''),
            'basis': meta.get('basis', ''),
            'headline': piece['headline'],
            'frq': frq,
            'answers': answers,
            'teacher_pages': pages['Teacher'],
            'student_pages': pages['Student'],
        })
        print("[%2s] %-13s %s  ans=%s  T=%dp S=%dp  | %s"
              % (str(meta.get('id','')), meta.get('register',''), meta.get('basis',''),
                 answers, pages['Teacher'], pages['Student'], piece['headline']))

    with open(os.path.join(os.path.dirname(os.path.abspath(path)), 'render_report.json'),
              'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2)
    print("\nRendered %d openers (%d PDFs). Report -> render_report.json"
          % (len(rows), len(rows) * 2))

if __name__ == '__main__':
    main()
