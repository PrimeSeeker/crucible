"""Resident tokens per route, with per-entry aliases.

Usage: python resident_ws.py <manifest.json> <rev>... --out <file> --key-env NAME

Reuses docs/crucible/2026-11-03-compaction-fit/resident_tokens.py (git access,
load forms, the count_tokens counter); the manifest format is the same, except
that an entry may carry "was": {"<rev>": "<path at that rev>"} for a file whose
role another path held at that revision.
"""
import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "docs/crucible/2026-11-03-compaction-fit"))
import resident_tokens as rt  # noqa: E402

p = argparse.ArgumentParser()
p.add_argument("manifest")
p.add_argument("revs", nargs="+")
p.add_argument("--out", required=True)
p.add_argument("--key-env", required=True)
a = p.parse_args()
key = os.environ.get(a.key_env) or sys.exit("no key")
man = json.load(open(a.manifest, encoding="utf-8"))
counter = rt.Counter(key)
cache = {}


def count(rev, entry):
    real = entry.get("was", {}).get(rev, entry["path"])
    if real != rt.SESSION_START and not rt.exists(rev, real):
        return None
    k = (rev, real)
    if k not in cache:
        cache[k] = counter.tokens(rt.loaded_text(rev, real))
    return cache[k]


out = []
cols = " | ".join(f"`{r}`" for r in a.revs)
rule = "|".join(["---"] * (len(a.revs) + 1))
for route, phases in man["routes"].items():
    out += [f"### {route}", "", f"| Phase | {cols} |", f"|{rule}|"]
    tot = {r: [0, 0] for r in a.revs}
    for ph in phases:
        cells = []
        for r in a.revs:
            ev = sum(count(r, e) or 0 for e in ph["files"] if "only" not in e)
            co = sum(count(r, e) or 0 for e in ph["files"] if "only" in e)
            tot[r][0] += ev
            tot[r][1] += co
            cells.append(f"{ev:,}" + (f" (+{co:,})" if co else ""))
        out.append(f"| {ph['phase']} | " + " | ".join(cells) + " |")
    out.append("| **total** | " + " | ".join(f"**{t[0]:,}**" + (f" (+{t[1]:,})" if t[1] else "") for t in tot.values()) + " |")
    out.append("")
out += ["### Per file", "", f"| File | {cols} |", f"|{rule}|"]
seen = set()
for route, phases in man["routes"].items():
    for ph in phases:
        for e in ph["files"]:
            k = (e["path"], json.dumps(e.get("was", {}), sort_keys=True))
            if k in seen:
                continue
            seen.add(k)
            name = f"`{e['path']}`" + ("".join(f" (`{p}` at `{r}`)" for r, p in e.get("was", {}).items()))
            out.append(f"| {name} | " + " | ".join("absent" if count(r, e) is None else f"{count(r, e):,}" for r in a.revs) + " |")
open(a.out, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
print(counter.calls, "calls")
print("\n".join(out))
