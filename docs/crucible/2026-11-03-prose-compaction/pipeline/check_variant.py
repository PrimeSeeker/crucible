"""Mechanical check of a rewritten skill file against its original.

Usage (from anywhere):
    python check_variant.py <repo-relative original path> <variant file>

Prints JSON: sizes, and a list of violations (each must be fixed) and
warnings (judge them). The original is read from the worktree as it stands.
Checks: SKILL.md body cap; frontmatter fields kept; headings removed or
renamed that are cited ('§ <heading>') anywhere else, included by a
template source, or required by a stub; stub sentences kept; '[[' marker
lines kept; protected strings from the constraints map kept; repo paths
named in the variant exist; 'crucible:<skill> § <heading>' citations resolve.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # run from <root>/.crucible/prose-compaction/tools/
WS = ROOT / ".crucible/prose-compaction"
STUB_RE = re.compile(r"read `(skills/[a-z0-9-]+/references/[A-Za-z0-9._-]+\.md)` in full")
H_RE = re.compile(r"^(#{1,4}) (.+?)\s*$", re.M)
PATH_RE = re.compile(r"(?<![\w/.-])((?:skills|docs|tests|hooks|tools|agents)/[A-Za-z0-9._/<>-]+\.(?:md|py|txt|json|dot|sh))")
CITE_RE = re.compile(r"crucible:([a-z-]+) § ([^\n`*]+)")


def norm(t):
    return t.replace("\r\n", "\n")


def body(t):
    lines = t.splitlines(keepends=True)
    if lines and lines[0].rstrip("\n") == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip("\n") == "---":
                return "".join(lines[i + 1:]), "".join(lines[: i + 1])
    return t, ""


def all_text_except(rel):
    out = {}
    for p in list(ROOT.glob("skills/**/*.md")) + list(ROOT.glob("docs/**/*.md")) + \
            list(ROOT.glob("hooks/*")) + list(ROOT.glob("tests/*.py")) + \
            list(ROOT.glob("agents/*.md")) + [ROOT / "README.md", ROOT / "AGENTS.md"]:
        if not p.is_file():
            continue
        r = p.relative_to(ROOT).as_posix()
        if r == rel or r.startswith("docs/crucible/"):
            continue
        try:
            out[r] = norm(p.read_text("utf-8"))
        except Exception:
            pass
    return out


def main():
    rel, var = sys.argv[1], Path(sys.argv[2])
    orig = norm((ROOT / rel).read_text("utf-8"))
    new = norm(var.read_text("utf-8"))
    viol, warn = [], []
    res = {"file": rel, "words_orig": len(orig.split()), "words_new": len(new.split()),
           "chars_orig": len(orig), "chars_new": len(new)}
    res["ratio"] = round(res["words_new"] / max(1, res["words_orig"]), 3)
    ob, ofm = body(orig)
    nb, nfm = body(new)
    if rel.endswith("/SKILL.md"):
        res["body_chars_new"] = len(nb)
        if len(nb) > 18000:
            viol.append(f"SKILL.md body {len(nb)} chars > 18000")
        if ofm and not nfm:
            viol.append("frontmatter missing")
        for key in ("name:", "description:"):
            o = [l for l in ofm.splitlines() if l.startswith(key)]
            n = [l for l in nfm.splitlines() if l.startswith(key)]
            if o and not n:
                viol.append(f"frontmatter {key} missing")
            elif o != n:
                warn.append(f"frontmatter {key} changed (descriptions are trigger text; change only deliberately)")
    others = all_text_except(rel)
    oh = [m.group(2) for m in H_RE.finditer(orig)]
    nh = set(m.group(2) for m in H_RE.finditer(new))
    includes = set()
    for t in others.values():
        includes.update(m.group(1) for m in re.finditer(r"^\[\[include (.+)\]\]$", t, re.M))
    for h in oh:
        if h in nh:
            continue
        hh = h.strip("`")
        citers = sorted(r for r, t in others.items() if "§ " + hh in t)
        if rel.endswith("references/seat-rules.md") and h in includes:
            viol.append(f"heading removed/renamed but included by a template source: '{h}'")
        elif citers:
            viol.append(f"heading removed/renamed but cited elsewhere: '{h}' (by {', '.join(citers[:5])})")
        else:
            warn.append(f"heading removed/renamed (not cited elsewhere): '{h}'")
    # stubs in a SKILL.md
    for m in STUB_RE.finditer(orig):
        if m.group(1) not in [x.group(1) for x in STUB_RE.finditer(new)]:
            viol.append(f"stub sentence for {m.group(1)} missing (form: read `<path>` in full)")
    # a reference that a stub points to must open with the stub's heading
    if "/references/" in rel:
        oheads = H_RE.findall(orig)
        nheads = H_RE.findall(new)
        if oheads and (not nheads or nheads[0] != oheads[0]):
            warn.append(f"first heading changed: was '{oheads[0][1]}' (a stubbed reference must open with its stub's heading)")
    # marker lines
    om = [l for l in orig.splitlines() if l.startswith("[[")]
    nm = [l for l in new.splitlines() if l.startswith("[[")]
    if om != nm:
        missing = [l for l in om if l not in nm]
        added = [l for l in nm if l not in om]
        if missing or added:
            viol.append(f"'[[' marker lines changed: missing {missing}, added {added}")
        else:
            warn.append("'[[' marker lines reordered")
    # protected strings
    cm = WS / "constraints.json"
    if cm.exists():
        data = json.loads(cm.read_text("utf-8"))
        for f in data.get("files", []):
            if f["path"] != rel:
                continue
            for p in f["protected"]:
                t, k = p["text"], p["kind"]
                if k == "literal" and t not in new:
                    viol.append(f"protected literal missing: {t!r} (read by {p['reader']})")
                elif k == "regex":
                    try:
                        if not re.search(t, new, re.M):
                            viol.append(f"protected regex no longer matches: {t!r} (read by {p['reader']})")
                    except re.error:
                        warn.append(f"protected regex unparsable, check by hand: {t!r}")
                elif k == "heading" and t.lstrip("# ").strip() not in nh and t not in new:
                    viol.append(f"protected heading missing: {t!r} (read by {p['reader']})")
                elif k == "structure":
                    warn.append(f"structural constraint, check by hand: {t} ({p['reader']})")
    # paths exist
    for m in PATH_RE.finditer(new):
        p = m.group(1)
        if "<" in p or "*" in p:
            continue
        if not (ROOT / p).exists() and p not in orig:
            viol.append(f"path does not exist in the repo: {p}")
    # cross-skill citations resolve
    for m in CITE_RE.finditer(new):
        skill, h = m.group(1), m.group(2).strip()
        target = ROOT / "skills" / skill / "SKILL.md"
        if not target.exists():
            viol.append(f"citation to unknown skill crucible:{skill}")
            continue
        th = [x.group(2) for x in H_RE.finditer(norm(target.read_text("utf-8")))]
        if rel == f"skills/{skill}/SKILL.md":
            th = list(nh)
        if not any(h.startswith(x) for x in th):
            if m.group(0) in orig:
                continue
            viol.append(f"citation does not resolve: crucible:{skill} § {h[:60]}")
    res["violations"] = viol
    res["warnings"] = warn
    print(json.dumps(res, indent=1))


main()
