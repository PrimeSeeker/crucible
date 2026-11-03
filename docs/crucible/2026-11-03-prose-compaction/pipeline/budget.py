"""Set tests/prose-budget.txt lines to current counts. Usage: python budget.py <repo-root>"""
import re, sys
from pathlib import Path
root = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(root / "tests"))
import test_prose_budget as t
p = root / "tests" / "prose-budget.txt"
lines = p.read_text("utf-8").split("\n")
out = []
for ln in lines:
    m = re.match(r"^(\S+)\s+(\d+)$", ln)
    if m:
        n = t.count_words(root / "skills" / m.group(1))
        if n != int(m.group(2)):
            print(m.group(1), m.group(2), "->", n)
        ln = f"{m.group(1)} {n}"
    out.append(ln)
open(p, "w", encoding="utf-8", newline="\n").write("\n".join(out))
