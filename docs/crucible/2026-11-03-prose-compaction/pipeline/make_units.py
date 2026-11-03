"""Build compact.js args for a list of skill files, and record each file's blob hash.

Usage: python make_units.py <out-args.json> <hashes.json> <path>...
Frames: A+B for all; C added at >= 1200 words. small (no critic, no QA) under 400 words.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # run from <root>/.crucible/prose-compaction/tools/
WS = ROOT / ".crucible/prose-compaction"
out, hashes, paths = sys.argv[1], sys.argv[2], sys.argv[3:]
units, hs = [], {}
for p in paths:
    slug = p.removeprefix("skills/").removesuffix(".md").replace("/", "__")
    brief = WS / "briefs" / f"{slug}.md"
    if not brief.exists():
        sys.exit(f"no brief for {p}")
    w = len((ROOT / p).read_text("utf-8").split())
    u = {"path": p, "brief": brief.as_posix(), "words": w, "frames": ["A", "B"] + (["C"] if w >= 1200 else [])}
    if w < 400:
        u["small"] = True
    units.append(u)
    hs[p] = subprocess.run(["git", "-C", str(ROOT), "hash-object", p], capture_output=True, encoding="utf-8").stdout.strip()
json.dump({"units": units}, open(out, "w", encoding="utf-8"), indent=1)
json.dump(hs, open(hashes, "w", encoding="utf-8"), indent=1)
print(len(units), "units,", sum(u["words"] for u in units), "words,", sum("C" in u["frames"] for u in units), "with C,", sum(bool(u.get("small")) for u in units), "small")
