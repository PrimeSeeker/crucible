"""Count tokens of every tracked skills/**/*.md file at one or more revisions.

Usage: python count_corpus.py <out.json> <rev> [<rev> ...]
A rev of WORKTREE reads the working tree. Uses Anthropic's count_tokens
endpoint (no inference), the key from the env var ANTHROPIC_API_KEY; subtracts a
one-word message's count. Identical texts are counted once (cache file).
"""
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # run from <root>/.crucible/prose-compaction/tools/
CACHE = ROOT / ".crucible/prose-compaction/token-cache.json"
cache = json.loads(CACHE.read_text("utf-8")) if CACHE.exists() else {}
KEY = os.environ["ANTHROPIC_API_KEY"]


def count(text):
    h = hashlib.sha256(text.encode()).hexdigest()
    if h in cache:
        return cache[h]
    body = json.dumps({"model": "claude-opus-5-5",
                       "messages": [{"role": "user", "content": text}]}).encode()
    for attempt in range(6):
        req = urllib.request.Request("https://api.anthropic.com/v1/messages/count_tokens", data=body,
                                     headers={"x-api-key": KEY, "anthropic-version": "2023-06-01",
                                              "content-type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                n = json.load(r)["input_tokens"]
                break
        except urllib.error.HTTPError as e:
            if e.code in (429, 529, 500) and attempt < 5:
                time.sleep(2 ** attempt)
                continue
            raise
    cache[h] = n
    CACHE.write_text(json.dumps(cache), encoding="utf-8")
    return n


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, encoding="utf-8",
                          check=True).stdout


def files_at(rev):
    if rev == "WORKTREE":
        out = git("ls-files", "skills")
        fs = [f for f in out.split() if f.endswith(".md") and (ROOT / f).exists()]
        # include untracked new skill files too
        extra = git("ls-files", "--others", "--exclude-standard", "skills").split()
        fs += [f for f in extra if f.endswith(".md")]
        return {f: (ROOT / f).read_text("utf-8").replace("\r\n", "\n") for f in sorted(set(fs))}
    out = git("ls-tree", "-r", "--name-only", rev, "skills")
    return {f: git("show", f"{rev}:{f}").replace("\r\n", "\n") for f in out.split() if f.endswith(".md")}


def main():
    out = Path(sys.argv[1])
    base = count("Hi")
    res = {"base": base, "revs": {}}
    for rev in sys.argv[2:]:
        fs = files_at(rev)
        res["revs"][rev] = {f: count(t) - base for f, t in fs.items()}
    out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    sys.path.insert(0, str(ROOT / "tests"))
    from test_prose_budget import rendered_templates
    rendered = rendered_templates()
    for rev, d in res["revs"].items():
        hand = sum(v for f, v in d.items() if f not in rendered)
        seat = sum(v for f, v in d.items() if f in rendered)
        print(f"{rev}: hand-edited {hand}, rendered templates {seat}, files {len(d)}")


main()
