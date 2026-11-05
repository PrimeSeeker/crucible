"""Re-count what controllers load and what seats carry, for the skill text rewrite's re-audit.

Usage:
    python resident_tokens_reaudit.py --out <figures.md> [--key-env NAME]

Sits on the two committed manifests and leaves them unchanged:
``docs/crucible/2026-11-03-compaction-fit/resident-tokens.json`` for the
revisions the decision record first counted, and
``docs/crucible/2026-11-03-prose-compaction/resident-tokens.json`` from there to
the head. Their ``about`` lists state the conventions. To each it adds the two
reads the skill text rewrite's closing review found omitted, as conditional
entries, each only at the revisions whose text sends a controller to it.

Seat text is the generated agent's body. At the first revision five seats also
read a shared reference on every dispatch; from the placement on, that text is
spliced into their bodies, so the table adds it there to keep the columns
comparable. References a seat reads only on some runs are not counted.

Each file's text goes alone to Anthropic's token-counting endpoint, which runs
no inference; the count of a one-word message is subtracted. Identical texts
are counted once. The API key is read from the environment variable
``--key-env`` names (default ``ANTHROPIC_API_KEY``). Stdlib only; run it from
anywhere inside the repository.
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
FIT_MANIFEST = "docs/crucible/2026-11-03-compaction-fit/resident-tokens.json"
PROSE_MANIFEST = "docs/crucible/2026-11-03-prose-compaction/resident-tokens.json"
AT = "5546425"  # the manifests are read as committed here
FIT_REVS = ["a3db87f", "d78398c", "4026f6b"]
PROSE_REVS = ["0deefcf", "56e8475", "5546425"]
PARALLEL = "skills/dispatching-parallel-agents/SKILL.md"
PARALLEL_REVS = ["a3db87f", "d78398c", "4026f6b", "0deefcf"]
TEMPLATE = "skills/subagent-driven-development/implementer-prompt.md"
SHARED_REFERENCE = "skills/subagent-driven-development/references/premise-and-questions.md"
SHARED_REFERENCE_READS = {
    "a3db87f": {"redteam-seat", "terminal-pass", "implementer", "task-reviewer", "branch-reviewer"},
}
SEATS = [
    "redteam-seat", "blind-verifier", "terminal-pass", "implementer",
    "task-reviewer", "re-reviewer", "branch-reviewer",
]
HOOK_OPENING = (
    "You have crucible. Below: the using-crucible skill, then this host's "
    "runtime reference. Read both before acting."
)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(HERE), *args], check=check, capture_output=True, encoding="utf-8",
    )


def exists(rev: str, path: str) -> bool:
    return git("cat-file", "-e", f"{rev}:{path}", check=False).returncode == 0


def show(rev: str, path: str) -> str:
    return git("show", f"{rev}:{path}").stdout.replace("\r\n", "\n")


def body(text: str) -> str:
    """*text* less its frontmatter block, the closing fence's line included."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].rstrip("\n") == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip("\n") == "---":
                return "".join(lines[i + 1:])
    return text


def loaded(rev: str, path: str) -> str:
    if path == "hooks/session-start":
        return (
            HOOK_OPENING + "\n\n" + show(rev, "skills/using-crucible/SKILL.md")
            + "\n---\n\n" + show(rev, "skills/using-crucible/references/claude-code.md")
        )
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
        for attempt in range(6):
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
                if err.code in (429, 500, 502, 503, 529) and attempt < 5:
                    time.sleep(2 ** attempt)
                    continue
                raise
        raise RuntimeError("unreachable")

    def tokens(self, text: str) -> int:
        digest = hashlib.sha256(text.encode()).hexdigest()
        if digest not in self.cache:
            self.cache[digest] = self._count(text) - self.base
        return self.cache[digest]


def add_reads(routes: dict, revs: list[str]) -> None:
    parallel = [r for r in revs if r in PARALLEL_REVS]
    for route, phases in routes.items():
        for phase in phases:
            if phase["phase"] == "spec campaign" and parallel:
                phase["files"].append(
                    {"path": PARALLEL, "only": "seats dispatched in parallel", "revs": parallel})
            if route == "very-small" and phase["phase"] == "execution":
                phase["files"].append({"path": TEMPLATE, "only": "the change implemented inline"})


def resolve(entry: dict, aliases: dict, rev: str) -> str | None:
    if "revs" in entry and rev not in entry["revs"]:
        return None
    path = entry["path"]
    real = (entry.get("was") or {}).get(rev) or aliases.get(path, {}).get(rev, path)
    return real if real == "hooks/session-start" or exists(rev, real) else None


def route_tables(manifest: dict, revs: list[str], counter: Counter, out: list[str]) -> None:
    aliases = manifest.get("aliases", {})
    head = "| Phase | " + " | ".join(f"`{r}`" for r in revs) + " |"
    rule = "|" + "|".join(["---"] * (len(revs) + 1)) + "|"
    for route, phases in manifest["routes"].items():
        out += [f"### {route}", "", head, rule]
        totals = {r: [0, 0] for r in revs}
        for phase in phases:
            cells = []
            for rev in revs:
                every = cond = 0
                for entry in phase["files"]:
                    real = resolve(entry, aliases, rev)
                    if real is None:
                        continue
                    count = counter.tokens(loaded(rev, real))
                    if "only" in entry:
                        cond += count
                    else:
                        every += count
                totals[rev][0] += every
                totals[rev][1] += cond
                cells.append(f"{every:,}" + (f" (+{cond:,})" if cond else ""))
            out.append(f"| {phase['phase']} | " + " | ".join(cells) + " |")
        out.append("| **total** | " + " | ".join(
            f"**{t[0]:,}** ({t[0] + t[1]:,})" for t in totals.values()) + " |")
        out.append("")


def seat_table(revs: list[str], counter: Counter, out: list[str]) -> None:
    out += ["| Seat | " + " | ".join(f"`{r}`" for r in revs) + " |",
            "|" + "|".join(["---"] * (len(revs) + 1)) + "|"]
    sums = {r: [0, 0] for r in revs}
    for seat in SEATS:
        cells = []
        for rev in revs:
            text = body(show(rev, f"agents/{seat}.md"))
            if seat in SHARED_REFERENCE_READS.get(rev, ()):
                text += show(rev, SHARED_REFERENCE)
            tokens, words = counter.tokens(text), len(text.split())
            sums[rev][0] += tokens
            sums[rev][1] += words
            cells.append(f"{tokens:,} ({words:,})")
        out.append(f"| {seat} | " + " | ".join(cells) + " |")
    out.append("| **one of each** | " + " | ".join(
        f"**{s[0]:,}** ({s[1]:,})" for s in sums.values()) + " |")
    out.append("")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    parser.add_argument("--key-env", default="ANTHROPIC_API_KEY")
    args = parser.parse_args()
    key = os.environ.get(args.key_env)
    if not key:
        sys.exit(f"no API key in ${args.key_env}")
    counter = Counter(key)

    out = [
        "# Re-audit figures: tokens loaded per route and carried per seat",
        "",
        f"Counted by `resident_tokens_reaudit.py` (its docstring states the method), tokenizer `{MODEL}`.",
        "A route's total reads **every run** (with every conditional file added).",
        "",
        "## Controller loads, compaction-fit manifest, with the two omitted reads",
        "",
    ]
    fit = json.loads(show(AT, FIT_MANIFEST))
    add_reads(fit["routes"], FIT_REVS)
    route_tables(fit, FIT_REVS, counter, out)

    out += ["## Controller loads, prose-compaction manifest, with the two omitted reads", ""]
    prose = json.loads(show(AT, PROSE_MANIFEST))
    add_reads(prose["routes"], PROSE_REVS)
    route_tables(prose, PROSE_REVS, counter, out)

    listed = {e["path"] for phases in prose["routes"].values() for p in phases for e in p["files"]}
    files = git("ls-tree", "-r", "--full-tree", "--name-only", AT, "skills").stdout.splitlines()
    if not files:
        sys.exit("no skill files listed: the coverage check cannot run")
    missing = [f for f in files if ("/references/" in f or f.endswith(".slots.md")) and f not in listed]
    out += ["## Head references and cards in no route's manifest", "", *[f"- `{f}`" for f in missing], ""]

    out += ["## Seat text per dispatch: tokens (words)", ""]
    seat_table(FIT_REVS + PROSE_REVS, counter, out)

    Path(args.out).write_text("\n".join(out), encoding="utf-8", newline="\n")
    print(f"{counter.calls} counting calls; one-word base {counter.base}")


if __name__ == "__main__":
    main()
