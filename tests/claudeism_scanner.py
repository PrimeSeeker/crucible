"""Claude-ism scanner. stdlib only.

No unallowlisted Claude-ism may survive in shared workflow text **or in the
text the hook emits**. Prose specification of that rule failed three times,
so the vocabulary lives here, in code, and the cases that broke it live in
``tests/claudeism_scanner_corpus/``.

Scan corpus:

- every ``.md`` file under ``skills/`` and under ``hooks/``;
- the repository ``README.md``;
- the SessionStart hook script, ``hooks/session-start``, as a source file.
  The envelope it emits is the two router files, already scanned as
  ``.md`` sources under ``skills/``, plus a lead line that lives only in
  the script; scanning the script covers that line without running bash.

``docs/`` is **excluded**: specs and plans are forensic artifacts that quote
Claude-isms deliberately, so scanning them would make every quotation a
finding.

Two properties are worth stating because they are easy to lose:

1. **Terms are matched case-insensitively and across quoting.** The router
   quotes its vocabulary (```Skill` tool``, ``"Skill" tool``), so
   the pattern matches ``Skill`` *adjacent to* ``tool``, not the bare
   phrase.
2. **Allowlisting is per term per location, never whole-file.** Files that
   must carry terms by design (a host map's Model roles entry, a provider
   reference) still have to report every OTHER term they carry -- three of
   the four pre-adaptation positives sat in files that also carried
   model-policy prose naming models.

Two things are deliberately NOT terms:

- ``crucible:<skill-name>`` -- crucible's own namespace vocabulary, canonical
  on every runtime;
- a **hyphenated basename naming a file this repository ships**
  (``claude-code.md``, ``claude-code-dispatch.md``) -- a path reference,
  which is what lets the router cite its host maps and dispatch references
  by name. Masked before matching, so a bare-``claude`` pattern cannot reach
  inside one.
  ``CLAUDE.md`` is not hyphenated and stays a term.

Run it: ``python tests/claudeism_scanner.py`` (exit 1 on any unallowlisted
match). ``tests/test_acceptance_gate.py`` runs it over the live tree.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

REPO_ROOT = Path(__file__).resolve().parent.parent
ALLOWLIST_PATH = Path(__file__).resolve().parent / "claudeism-allowlist.txt"

#: The SessionStart hook script: the one non-``.md`` source scanned, since
#: the envelope's lead line lives in it.
HOOK_SCRIPT = "hooks/session-start"


# --- vocabulary ----------------------------------------------------------


@dataclass(frozen=True)
class Term:
    id: str
    pattern: str
    why: str


#: Ordered longest-first: alternation picks the first alternative that
#: matches at a position, so ``Claude Code`` is one ``claude-code`` hit and
#: not additionally a bare ``claude`` one. One hit per span keeps the
#: per-term-per-location allowlist grammar meaningful.
TERMS: tuple[Term, ...] = (
    Term(
        "claude-plugin-root",
        r"\$?\{?CLAUDE_PLUGIN_ROOT\}?",
        "the host plugin-root variable outside Claude registration or "
        "compatibility docs",
    ),
    Term(
        "claude-home-path",
        r"~/\.claude(?:/[\w.-]*)*/?",
        "`~/.claude/skills/` as the only personal skill location",
    ),
    Term("claude-md", r"\bCLAUDE\.md\b", "the Claude host's project-instruction file"),
    Term("claude-ai", r"\bclaude\.ai\b", "provider product noun"),
    Term("claude-code", r"\bclaude\s+code\b", "provider product noun"),
    Term("anthropic", r"\banthropic\b", "provider noun"),
    Term("claude", r"\bclaude\b", "bare provider noun"),
    Term(
        "skill-tool",
        # The separator class is QUOTING, not "any non-word character":
        # `\W{0,4}` also spanned a comma, so "a skill, tool, or command" --
        # ordinary English listing two nouns -- was reported as the host's
        # invocation verb. And both nouns take a plural: "Skill tools" is
        # the same construction, and `tool\b` rejected it.
        r"\bskills?[\s`'\"*_-]{0,4}tools?\b",
        "the `Skill tool` invocation verb in any quoting",
    ),
    Term(
        "subagent-general-purpose",
        r"\bsubagent\W{0,4}\(\s*general[-\s]purpose\s*\)",
        "`Subagent (general-purpose)`, one host's dispatch spelling",
    ),
    Term(
        "before-entering-plan-mode",
        r"\bbefore\W{1,4}entering\W{1,4}plan\W{1,4}mode\b",
        "`before entering plan mode`, one host's mode name",
    ),
    Term(
        "one-response-parallelism",
        r"(?:dispatch\w*|calls?|invocations?|tool\s+uses?)[^.\n]{0,80}"
        r"\bin\s+(?:one|a\s+single)\s+(?:response|message)\b"
        r"|\bin\s+(?:one|a\s+single)\s+(?:response|message)\b[^.\n]{0,80}"
        r"(?:parallel|concurrent)",
        "multiple dispatch calls in one response = parallel "
        "execution, and its variants",
    ),
    Term(
        "bash-script-entrypoint",
        r"\bbash\s+\S*(?:<plugin-root>|\$?\{?CLAUDE_PLUGIN_ROOT\}?|/skills/)\S*",
        "a Bash-only core-coordination entrypoint in shared text",
    ),
    Term("opus", r"\bopus\b", "provider model name outside the model mapping"),
    Term("sonnet", r"\bsonnet\b", "provider model name outside the model mapping"),
    Term("haiku", r"\bhaiku\b", "provider model name outside the model mapping"),
    Term("fable", r"\bfable\b", "provider model name outside the model mapping"),
    # Codex model lines. A slug match starts earlier and consumes the line
    # name inside it, so `gpt-6.1-sol` is one slug hit and not also a bare
    # `sol` one; the slug also catches a line no term below names yet. Word
    # boundaries keep "Solve", "terrain", "lunar" and "astral" out.
    Term(
        "codex-model-slug",
        r"\bgpt-(?:[\w.-]*\w)?",
        "Codex model slug outside the model mapping",
    ),
    Term("sol", r"\bsol\b", "Codex model line outside the model mapping"),
    Term("terra", r"\bterra\b", "Codex model line outside the model mapping"),
    Term("astra", r"\bastra\b", "Codex model line outside the model mapping"),
    Term("luna", r"\bluna\b", "Codex model line outside the model mapping"),
)

TERM_IDS = frozenset(term.id for term in TERMS)

_TERM_RE = re.compile(
    "|".join(f"(?P<{term.id.replace('-', '_')}>{term.pattern})" for term in TERMS),
    re.IGNORECASE,
)
_GROUP_TO_TERM = {term.id.replace("-", "_"): term.id for term in TERMS}

#: Spans blanked before matching. A hyphenated BASENAME with a source-file
#: extension names a file this repository ships, so it is a path reference
#: and not a term (`claude-code.md`, `claude-code-dispatch.md`).
#: `CLAUDE.md` has no hyphen and is untouched.
#:
#: The mask covers the FINAL path component only -- never the directory
#: segments in front of it. Widening it to the whole path token is a false
#: negative on the `~/.claude/...` construction itself, which is a
#: term standing in a prefix and not inside any basename:
#: `~/.claude/skills/using-crucible.md` must report `~/.claude/skills/`
#: while `using-crucible.md` stays masked. The lookbehind admits `/` (and
#: quoting punctuation) precisely so the basename can be reached inside a
#: longer path while its prefix is left visible.
_MASKS: tuple[re.Pattern[str], ...] = (
    re.compile(
        r"(?<![\w-])[\w.]*-[\w.-]*\.(?:md|py|json|ya?ml|txt|sh)(?![\w-])"
    ),
)


def _mask(text: str) -> str:
    """Blank path references, preserving every offset and line break."""
    chars = list(text)
    for pattern in _MASKS:
        for found in pattern.finditer(text):
            for index in range(found.start(), found.end()):
                if chars[index] != "\n":
                    chars[index] = "\x00"
    return "".join(chars)


@dataclass(frozen=True)
class Match:
    term: str
    location: str
    line: int
    column: int
    text: str
    source_line: str

    def render(self) -> str:
        return f"{self.location}:{self.line}:{self.column}: {self.term}: {self.text!r}"


def find_matches(text: str, location: str) -> list[Match]:
    """Every scanner term in ``text``, reported at ``location``."""
    masked = _mask(text)
    lines = text.splitlines()
    line_starts = []
    offset = 0
    for line in text.splitlines(keepends=True):
        line_starts.append(offset)
        offset += len(line)

    matches: list[Match] = []
    for found in _TERM_RE.finditer(masked):
        group = found.lastgroup
        # A nested group inside a term pattern would report itself; walk to
        # the outer term group instead.
        term_id = _GROUP_TO_TERM.get(group or "")
        if term_id is None:
            term_id = next(
                _GROUP_TO_TERM[name]
                for name, value in found.groupdict().items()
                if value is not None and name in _GROUP_TO_TERM
            )
        index = _line_index(line_starts, found.start())
        matches.append(
            Match(
                term=term_id,
                location=location,
                line=index + 1,
                column=found.start() - line_starts[index] + 1,
                text=text[found.start() : found.end()],
                source_line=lines[index] if index < len(lines) else "",
            )
        )
    return matches


def _line_index(line_starts: list[int], offset: int) -> int:
    low, high = 0, len(line_starts) - 1
    while low < high:
        mid = (low + high + 1) // 2
        if line_starts[mid] <= offset:
            low = mid
        else:
            high = mid - 1
    return low


# --- allowlist -----------------------------------------------------------


class AllowlistError(ValueError):
    """The allowlist file violates the grammar."""


@dataclass(frozen=True)
class Entry:
    klass: int
    term: str
    location: str
    rationale: str


@dataclass(frozen=True)
class Allowlist:
    entries: tuple[Entry, ...]

    def _pairs(self) -> frozenset[tuple[str, str]]:
        return frozenset((e.term, e.location) for e in self.entries)

    def allows(self, term: str, location: str) -> bool:
        return (term, location) in self._pairs()


def parse_allowlist(text: str) -> Allowlist:
    """Parse the ``class | term | location | rationale`` grammar.

    Blank lines and ``#`` comments are ignored, so classes can be sectioned
    and appended to.
    """
    entries: list[Entry] = []
    seen: set[tuple[str, str]] = set()
    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        fields = [field.strip() for field in line.split("|")]
        if len(fields) != 4:
            raise AllowlistError(
                f"line {number}: expected 4 fields "
                f"(class | term | location | rationale), got "
                f"{len(fields)}: {line!r}. A location without a term is a "
                f"whole-file entry and is never valid."
            )
        klass_field, term, location, rationale = fields
        try:
            klass = int(klass_field)
        except ValueError as exc:
            raise AllowlistError(f"line {number}: class {klass_field!r} is not a number") from exc
        if klass not in (2, 3):
            raise AllowlistError(f"line {number}: unknown class {klass}")
        if term in ("", "*"):
            raise AllowlistError(
                f"line {number}: {term!r} is a whole-file entry; allowlisting "
                f"is per term per location"
            )
        if term not in TERM_IDS:
            raise AllowlistError(f"line {number}: unknown term {term!r}")
        if location in ("", "*"):
            raise AllowlistError(f"line {number}: {location!r} is not a location")
        if not rationale:
            raise AllowlistError(f"line {number}: an entry needs a rationale")
        pair = (term, location)
        if pair in seen:
            raise AllowlistError(f"line {number}: duplicate entry for {pair}")
        seen.add(pair)
        entries.append(Entry(klass, term, location, rationale))
    return Allowlist(tuple(entries))


def load_allowlist(path: Path = ALLOWLIST_PATH) -> Allowlist:
    return parse_allowlist(Path(path).read_text(encoding="utf-8"))


# --- the scan ------------------------------------------------------------


def collect_sources(root: Path) -> dict[str, str]:
    """The scan corpus, keyed by repo-relative location."""
    root = Path(root)
    paths: list[Path] = []
    for directory in ("skills", "hooks"):
        paths.extend(sorted((root / directory).rglob("*.md")))
    for name in ("README.md", HOOK_SCRIPT):
        if (root / name).is_file():
            paths.append(root / name)
    return {
        path.relative_to(root).as_posix(): path.read_text(encoding="utf-8")
        for path in paths
        if path.is_file()
    }


def scan_sources(sources: Mapping[str, str]) -> list[Match]:
    matches: list[Match] = []
    for location, text in sources.items():
        matches.extend(find_matches(text, location))
    return matches


def scan_tree(root: Path) -> list[Match]:
    """Every term in the whole scan corpus for ``root``."""
    return scan_sources(collect_sources(root))


def unallowlisted(matches: Iterable[Match], allowlist: Allowlist) -> list[Match]:
    return [m for m in matches if not allowlist.allows(m.term, m.location)]


def main(argv: list[str] | None = None) -> int:
    root = Path(argv[0]) if argv else REPO_ROOT
    allowlist = load_allowlist()
    reported = unallowlisted(scan_tree(root), allowlist)
    for match in reported:
        print(match.render())
    print(f"\n{len(reported)} unallowlisted match(es); {len(allowlist.entries)} allowlist entries")
    return 1 if reported else 0


if __name__ == "__main__":  # pragma: no cover - CLI
    sys.exit(main(sys.argv[1:]))
