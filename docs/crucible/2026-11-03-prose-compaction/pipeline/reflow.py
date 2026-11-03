"""Join hard-wrapped Markdown so each paragraph and list item is one line.

Usage: python reflow.py <repo-root> [--check]
Rewrites every tracked hand-edited skills/**/*.md (rendered templates excluded;
regenerate them after). Leaves untouched: frontmatter, fenced code, tables,
headings, '[[' marker lines, HTML-tag lines, blockquotes, blank lines.
A line joins the previous one when both are prose of the same block: the
previous line is a paragraph or list-item line and this line is neither
blank nor a block start. LF output.
"""
import re
import subprocess
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
check = "--check" in sys.argv
sys.path.insert(0, str(root / "tests"))
from test_prose_budget import rendered_templates  # noqa: E402

rendered = rendered_templates()
files = [p for p in subprocess.run(["git", "-C", str(root), "ls-files", "skills"], capture_output=True,
                                    encoding="utf-8", check=True).stdout.split()
         if p.endswith(".md") and p not in rendered]

ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
START = re.compile(r"^\s*(#|\||\[\[|<|>|```|~~~|---\s*$|===\s*$)")


def reflow(text):
    lines = text.split("\n")
    out = []
    i = 0
    # frontmatter
    if lines and lines[0] == "---":
        j = 1
        while j < len(lines) and lines[j] != "---":
            j += 1
        out.extend(lines[: j + 1])
        i = j + 1
    fence = False
    joinable = False  # previous out line is prose that may take a continuation
    for line in lines[i:]:
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            out.append(line)
            joinable = False
            continue
        if fence:
            out.append(line)
            continue
        if not s:
            out.append(line)
            joinable = False
            continue
        if START.match(line):
            out.append(line)
            joinable = False
            continue
        if ITEM.match(line):
            out.append(line.rstrip())
            joinable = True
            continue
        if joinable and not line.endswith("  "):
            out[-1] = out[-1].rstrip() + " " + s
            continue
        out.append(line.rstrip() if not line.endswith("  ") else line)
        joinable = not line.endswith("  ")
    return "\n".join(out)


changed = 0
for f in files:
    p = root / f
    t = p.read_text("utf-8").replace("\r\n", "\n")
    n = reflow(t)
    if n != t:
        changed += 1
        if not check:
            with open(p, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(n)
print(f"{changed} of {len(files)} files {'would change' if check else 'reflowed'}")
