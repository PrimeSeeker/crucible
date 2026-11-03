"""Check each unit's final against its original, then copy it over the original.

Usage: python apply_finals.py <args.json> [<args.json> ...] [--dry] [--only=<prefix>,<prefix>]
Refuses to copy any unit whose check reports violations, or whose original's blob hash
differs from the one recorded at the wave's launch (hashes-*.json beside the args).
"""
import json
import subprocess
import sys
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
ROOT = WS.parents[1]
dry = "--dry" in sys.argv
only = [a.split("=",1)[1].split(",") for a in sys.argv if a.startswith("--only=")]
only = only[0] if only else None
hashes = {}
for h in WS.glob("hashes-*.json"):
    hashes.update(json.load(open(h, encoding="utf-8")))
units = []
for a in [x for x in sys.argv[1:] if not x.startswith("--")]:
    units += [u for u in json.load(open(a, encoding="utf-8"))["units"] if not only or any(u["path"].startswith(o) for o in only)]
bad = 0
for u in units:
    p = u["path"]
    s = p.removeprefix("skills/").removesuffix(".md").replace("/", "__")
    fin = WS / "units" / s / "final.md"
    now = subprocess.run(["git", "-C", str(ROOT), "hash-object", p], capture_output=True, encoding="utf-8").stdout.strip()
    if hashes.get(p) != now:
        print("ORIGINAL CHANGED", p); bad += 1; continue
    r = json.loads(subprocess.run([sys.executable, str(WS / "tools/check_variant.py"), p, str(fin)], capture_output=True, encoding="utf-8").stdout)
    if r.get("violations"):
        print("VIOLATIONS", p, r["violations"]); bad += 1; continue
    for w in r.get("warnings", []):
        print("warn", p, str(w)[:200])
    if not dry:
        text = fin.read_text("utf-8").replace("\r\n", "\n").rstrip("\n") + "\n"
        open(ROOT / p, "w", encoding="utf-8", newline="\n").write(text)
print(len(units), "units;", bad, "refused;", "dry run" if dry else "applied")
