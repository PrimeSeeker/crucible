"""Build the corpus map: every hand-edited skill file, its words/chars,
its headings, and for each heading the places outside the file that cite it.

Usage: python corpus_map.py <repo-root> <out.json>
"""
import json
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2])

sys.path.insert(0, str(root / "tests"))
from test_prose_budget import rendered_templates  # noqa: E402

rendered = rendered_templates()
tracked = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True,
                         encoding="utf-8", check=True).stdout.split()
skill_files = sorted(p for p in tracked if p.startswith("skills/") and p.endswith(".md")
                     and p not in rendered)
text_files = [p for p in tracked if p.endswith((".md", ".py", ".txt", ".json", ".toml"))
              or p.startswith("hooks/")]
texts = {}
for p in text_files:
    try:
        texts[p] = (root / p).read_text("utf-8").replace("\r\n", "\n")
    except Exception:
        pass

H = re.compile(r"^(#{1,4}) (.+?)\s*$", re.M)
files = {}
for p in skill_files:
    t = texts[p]
    heads = [(len(m.group(1)), m.group(2)) for m in H.finditer(t)]
    files[p] = {"words": len(t.split()), "chars": len(t), "headings": []}
    skill = p.split("/")[1]
    base = p.rsplit("/", 1)[1]
    for lvl, h in heads:
        hh = h.strip("`")
        cites = []
        pat = re.compile(r"§\s*" + re.escape(hh))
        for q, qt in texts.items():
            if q == p:
                # within-file citations count too (they stay consistent if renamed together)
                pass
            for m in pat.finditer(qt):
                ctx = qt[max(0, m.start() - 120):m.start()]
                # attribute to this file when the preceding context names it
                names = [p, base, f"crucible:{skill}"] if base == "SKILL.md" else [p, base]
                if any(n in ctx for n in names) or q == p:
                    cites.append(q)
        files[p]["headings"].append({"level": lvl, "text": h,
                                     "cited_by": sorted(set(cites))})
out.write_text(json.dumps({"rendered": sorted(rendered), "files": files}, indent=1),
               encoding="utf-8")
tot = sum(f["words"] for f in files.values())
print(len(files), "files", tot, "words")
for p, f in sorted(files.items(), key=lambda kv: -kv[1]["words"]):
    nc = sum(1 for h in f["headings"] if h["cited_by"])
    print(f'{f["words"]:6d} {nc:3d}/{len(f["headings"]):3d} {p}')
