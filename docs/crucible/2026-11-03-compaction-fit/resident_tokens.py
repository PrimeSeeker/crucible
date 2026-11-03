"""Count the resident tokens of each route's manifest at given revisions.

Usage:
    python resident_tokens.py <rev> [<rev> ...] --out <figures.md> [--key-env NAME]

Reads ``resident-tokens.json`` beside this file (its ``about`` list states
the manifests' conventions). Each file's text is taken from git at each
revision and sent alone to Anthropic's token-counting endpoint, which runs
no inference; the count of a one-word message is subtracted, leaving the
text's own tokens. Identical texts are counted once. The API key is read
from the environment variable ``--key-env`` names (default
``ANTHROPIC_API_KEY``). Writes the figures as markdown to ``--out``.

Stdlib only; run it from anywhere inside the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENDPOINT = "https://api.anthropic.com/v1/messages/count_tokens"
MODEL = "claude-opus-5-5"
SESSION_START = "hooks/session-start"
# The SessionStart hook's opening line and separator, as hooks/session-start
# composes them; checked against the hook at each revision.
HOOK_OPENING = (
    "You have crucible. Below: the using-crucible skill, then this host's "
    "runtime reference. Read both before acting."
)
HOOK_LINE = (
    'json_string context "' + HOOK_OPENING + '"$\'\\n\\n\'"$router"$\'\\n\'"---"'
    '$\'\\n\\n\'"$host_map"'
)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(HERE), *args],
        check=True, capture_output=True, encoding="utf-8",
    ).stdout


def exists(rev: str, path: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(HERE), "cat-file", "-e", f"{rev}:{path}"],
        capture_output=True,
    ).returncode == 0


def show(rev: str, path: str) -> str:
    return git("show", f"{rev}:{path}").replace("\r\n", "\n")


def body(text: str) -> str:
    """*text* less its frontmatter block, the closing fence's line included
    (the boundary ``tests/test_skill_size.py`` uses)."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].rstrip("\n") == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip("\n") == "---":
                return "".join(lines[i + 1:])
    return text


def loaded_text(rev: str, path: str) -> str:
    if path == SESSION_START:
        hook = show(rev, SESSION_START)
        if HOOK_LINE not in hook:
            sys.exit(f"{rev}: the hook's composition differs from HOOK_LINE")
        router = show(rev, "skills/using-crucible/SKILL.md")
        host_map = show(rev, "skills/using-crucible/references/claude-code.md")
        return HOOK_OPENING + "\n\n" + router + "\n---\n\n" + host_map
    text = show(rev, path)
    return body(text) if path.endswith("/SKILL.md") else text


class Counter:
    def __init__(self, key: str) -> None:
        self.key = key
        self.cache: dict[str, int] = {}
        self.calls = 0
        self.base = self._count("x")

    def _count(self, text: str) -> int:
        data = json.dumps({
            "model": MODEL,
            "messages": [{"role": "user", "content": text}],
        }).encode()
        for attempt in range(5):
            req = urllib.request.Request(ENDPOINT, data=data, headers={
                "x-api-key": self.key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            })
            try:
                with urllib.request.urlopen(req) as resp:
                    self.calls += 1
                    return json.load(resp)["input_tokens"]
            except urllib.error.HTTPError as err:
                if err.code in (429, 500, 502, 503, 529) and attempt < 4:
                    time.sleep(2 ** attempt)
                    continue
                raise
        raise RuntimeError("unreachable")

    def tokens(self, text: str) -> int:
        digest = hashlib.sha256(text.encode()).hexdigest()
        if digest not in self.cache:
            self.cache[digest] = self._count(text) - self.base
        return self.cache[digest]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("revs", nargs="+")
    parser.add_argument("--out", required=True)
    parser.add_argument("--key-env", default="ANTHROPIC_API_KEY")
    args = parser.parse_args()
    key = os.environ.get(args.key_env)
    if not key:
        sys.exit(f"no API key in ${args.key_env}")

    manifest = json.loads((HERE / "resident-tokens.json").read_text(encoding="utf-8"))
    aliases = manifest["aliases"]
    counter = Counter(key)

    def at(rev: str, path: str) -> str | None:
        """The path holding *path*'s role at *rev*, or None where absent."""
        real = aliases.get(path, {}).get(rev, path)
        if real == SESSION_START or exists(rev, real):
            return real
        return None

    per_file: dict[str, dict[str, int | None]] = {}
    for route, phases in manifest["routes"].items():
        seen: set[str] = set()
        for phase in phases:
            for entry in phase["files"]:
                path = entry["path"]
                if path in seen:
                    sys.exit(f"{route}: {path} listed twice")
                seen.add(path)
                per_file.setdefault(path, {})
    for path in per_file:
        for rev in args.revs:
            real = at(rev, path)
            per_file[path][rev] = (
                None if real is None else counter.tokens(loaded_text(rev, real))
            )

    out: list[str] = []
    cols = " | ".join(f"`{r}`" for r in args.revs)
    rule = "|".join(["---"] * (len(args.revs) + 1))
    for route, phases in manifest["routes"].items():
        out += [f"### {route}", "", f"| Phase | {cols} |", f"|{rule}|"]
        totals = {r: [0, 0] for r in args.revs}
        for phase in phases:
            cells = []
            for rev in args.revs:
                every = sum(per_file[e["path"]][rev] or 0
                            for e in phase["files"] if "only" not in e)
                cond = sum(per_file[e["path"]][rev] or 0
                           for e in phase["files"] if "only" in e)
                totals[rev][0] += every
                totals[rev][1] += cond
                cells.append(f"{every:,}" + (f" (+{cond:,})" if cond else ""))
            out.append(f"| {phase['phase']} | " + " | ".join(cells) + " |")
        out.append("| **total** | " + " | ".join(
            f"**{t[0]:,}**" + (f" (+{t[1]:,})" if t[1] else "")
            for t in totals.values()) + " |")
        out.append("")
    out += ["### Per file", "", f"| File | {cols} |", f"|{rule}|"]
    for path, counts in per_file.items():
        name = f"`{path}`"
        if path in aliases:
            name += " (" + "; ".join(
                f"`{p}` at `{r}`" for r, p in aliases[path].items()) + ")"
        out.append(f"| {name} | " + " | ".join(
            "absent" if counts[r] is None else f"{counts[r]:,}"
            for r in args.revs) + " |")
    out.append("")
    Path(args.out).write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{counter.calls} counting calls; one-word base {counter.base}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
