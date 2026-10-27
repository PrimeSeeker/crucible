"""Dangling-reference scanner.

Scanned surface: all ``skills/**/*.md``, ``hooks/**`` prose (any text
file under hooks/, e.g. README.md, hooks.json), the decision
records ``docs/decisions/*.md`` and the upstream map ``docs/upstream.md``.
Deliberately NOT ``tests/`` -- test files legitimately contain enforcement
vocabulary (tests/test_router.py names ``superpowers`` strings precisely in
order to ban them).

Violation classes (per ``docs/authoring.md`` section "Reference
convention" -- the positive format this scanner validates against):

1. Retired-namespace invocation strings: any ``superpowers:`` occurrence.
2. Dropped-skill names used as *invocation-shaped* references:
   namespace-qualified (``<ns>:<dropped-name>``), markdown-link targets,
   or ``skills/<dropped-name>`` paths. Bare prose mentions (provenance,
   e.g. the enumeration in docs/authoring.md) are legitimate and do not
   match these shapes; anything that does match but is judged legitimate
   provenance goes in the explicit PROVENANCE_ALLOWLIST.
3. ``crucible:<name>`` invocations that do not name a shipped skill
   (a dir under skills/ carrying a SKILL.md).
4. Plugin-root-anchored file references (``skills/...``, ``hooks/...``,
   ``tests/...``, ``docs/...``) that do not resolve on disk.
5. Relative markdown link targets that do not resolve on disk.
6. Anchor citations (``<file>.md § Heading`` / ``crucible:<skill> §
   Heading``) whose heading does not exist in the cited file.

Scoping decisions:

- Path tokens are only checked when their final segment carries a file
  extension; extensionless mentions (``skills/systematic-debugging``,
  ``docs/backlog/``) are directory/skill-name prose, not
  file citations, and are not resolvable-by-convention.
- Tokens containing template placeholders (``<...>``, ``YYYY``, ``NN``)
  are skipped, as are anchor citations whose heading is a placeholder
  (``README.md § <heading>``); so are tokens inside http(s) URLs.
- Upstream paths carry the prefix ``superpowers/``
  (``superpowers/skills/executing-plans/``): they name upstream's tree, so
  the dropped-skill and anchor checks skip them, and the dropped-skill
  check skips URLs too; the root-path check never matches a path after
  ``/``. A dropped skill named without the prefix is still caught.
- In the records and the map a bare ``README.md § Heading`` cites the
  root README; in skills/ and hooks/ it cites ``hooks/README.md``.
- Bare sibling-file mentions (backticked ``seat-prompt.md``) are not a
  dangling-check surface here (the convention's citable form is the
  plugin-root-anchored path); they are covered by test_structure.py's
  forward/orphan checks.

Scanner helpers take an explicit root so seeded-violation trees under
tmp_path exercise each failure class permanently (a check that never
failed has never been tested).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

DROPPED_SKILLS = (
    "test-driven-development",
    "verification-before-completion",
    "executing-plans",
    "receiving-code-review",
    "using-superpowers",
)

ROOT_DIRS = ("skills", "hooks", "tests", "docs")

#: The decision records and the upstream map: scanned with the skills and
#: hooks, and cite the root README by its bare name.
DECISIONS_DIR = "docs/decisions"
UPSTREAM_MAP = "docs/upstream.md"

#: Upstream paths carry this prefix (``superpowers/skills/executing-plans/``)
#: so the dropped-skill and anchor checks can tell them from crucible's own.
UPSTREAM_PREFIX = "superpowers/"

#: (file posix-relpath, exact matched string) pairs that LOOK like
#: violations but are judged legitimate provenance prose. Keep small and
#: justified; never allowlist a real violation.
PROVENANCE_ALLOWLIST: set[tuple[str, str]] = set()


# --- file collection ----------------------------------------------------


def iter_scan_files(root: Path) -> list[tuple[Path, str]]:
    """All (path, text) scan targets under *root*.

    skills/**/*.md plus every text file under hooks/ (``__pycache__``
    excluded). Files that do not decode as UTF-8 are skipped -- the
    scanner must tolerate binary strays without crashing.
    """
    candidates: list[Path] = []
    skills = root / "skills"
    if skills.is_dir():
        candidates.extend(sorted(skills.rglob("*.md")))
    hooks = root / "hooks"
    if hooks.is_dir():
        candidates.extend(
            p for p in sorted(hooks.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts
        )
    candidates.extend(sorted((root / DECISIONS_DIR).glob("*.md")))
    if (root / UPSTREAM_MAP).is_file():
        candidates.append(root / UPSTREAM_MAP)
    out: list[tuple[Path, str]] = []
    for path in candidates:
        try:
            text = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue  # binary/non-UTF8 stray: skip, never crash
        out.append((path, text.replace("\r\n", "\n")))
    return out


def _rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


# --- check 1: retired namespace ----------------------------------------

_SUPERPOWERS_RE = re.compile(r"superpowers:", re.IGNORECASE)


def find_superpowers_invocations(root: Path) -> list[str]:
    violations = []
    for path, text in iter_scan_files(root):
        for lineno, line in enumerate(text.splitlines(), 1):
            if _SUPERPOWERS_RE.search(line):
                violations.append(
                    f"{_rel(root, path)}:{lineno}: retired-namespace "
                    f"invocation string: {line.strip()[:120]}"
                )
    return violations


# --- check 2: dropped skills as invocation-shaped references ------------


def _dropped_patterns() -> list[tuple[str, re.Pattern[str]]]:
    pats = []
    for name in DROPPED_SKILLS:
        n = re.escape(name)
        # IGNORECASE: case variants (Crucible:Test-Driven-Development) are
        # the same dangling reference; the superpowers check (check 1) is
        # already case-insensitive, this keeps check 2 as wide.
        pats.append((name, re.compile(
            # namespace-qualified invocation: crucible:NAME, foo:NAME
            rf"[A-Za-z0-9_-]+:{n}(?![a-z0-9-])"
            # markdown link target containing the name
            rf"|\]\([^)\n]*(?<![a-z0-9-]){n}(?![a-z0-9-])[^)\n]*\)"
            # plugin-root path into the dropped skill's directory
            rf"|\bskills/{n}(?![a-z0-9-])",
            re.IGNORECASE,
        )))
    return pats


_UPSTREAM_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_/.-])%s[A-Za-z0-9._/-]*" % re.escape(UPSTREAM_PREFIX)
)


def _blank_upstream_refs(line: str) -> str:
    """*line* with URLs and prefixed upstream paths blanked: both name a
    dropped skill where upstream still has it, never a crucible file."""
    return _UPSTREAM_TOKEN_RE.sub(" ", _URL_RE.sub(" ", line))


def find_dropped_invocation_refs(root: Path) -> list[str]:
    violations = []
    patterns = _dropped_patterns()
    for path, text in iter_scan_files(root):
        rel = _rel(root, path)
        for lineno, raw_line in enumerate(text.splitlines(), 1):
            line = _blank_upstream_refs(raw_line)
            for name, pat in patterns:
                for m in pat.finditer(line):
                    if (rel, m.group(0)) in PROVENANCE_ALLOWLIST:
                        continue
                    violations.append(
                        f"{rel}:{lineno}: dropped skill '{name}' used as "
                        f"invocation-shaped reference: {m.group(0)!r}"
                    )
    return violations


# --- check 3: crucible: invocations must name shipped skills ------------

# IGNORECASE so case-variant invocations (Crucible:Some-Skill) are checked
# too; the roster is lowercase directory names, so any non-lowercase
# invocation is reported rather than slipping through unexamined.
_CRUCIBLE_RE = re.compile(r"crucible:([a-z][a-z0-9-]*)", re.IGNORECASE)


def shipped_skills(root: Path) -> set[str]:
    skills = root / "skills"
    if not skills.is_dir():
        return set()
    return {
        d.name for d in skills.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    }


def find_unknown_crucible_invocations(root: Path) -> list[str]:
    roster = shipped_skills(root)
    violations = []
    for path, text in iter_scan_files(root):
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in _CRUCIBLE_RE.finditer(line):
                if m.group(1) not in roster:
                    violations.append(
                        f"{_rel(root, path)}:{lineno}: invocation "
                        f"'crucible:{m.group(1)}' names no shipped skill"
                    )
    return violations


# --- check 4: plugin-root-anchored paths must resolve -------------------

_PATH_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_/.-])(?:%s)/[A-Za-z0-9._/-]*[A-Za-z0-9]"
    % "|".join(ROOT_DIRS)
)
_URL_RE = re.compile(r"https?://\S+")
_PLACEHOLDER_RE = re.compile(r"<[^>]*>|YYYY|\bNN\b")


def _has_extension(token: str) -> bool:
    final = token.rsplit("/", 1)[-1]
    return "." in final and not final.endswith(".")


def find_dangling_root_paths(root: Path) -> list[str]:
    violations = []
    for path, text in iter_scan_files(root):
        rel = _rel(root, path)
        for lineno, raw_line in enumerate(text.splitlines(), 1):
            # Plugin-root substitution prefixes anchor the path that
            # follows them at the plugin root -- unwrap so it is checked.
            # BOTH spellings: `${PLUGIN_ROOT}` is the Codex-native name and
            # `${CLAUDE_PLUGIN_ROOT}` the Claude one, and the scanner accepts
            # a path behind either. Unwrapping only the Claude spelling would
            # leave a Codex-side path unchecked -- silently, and in the
            # direction that never fails.
            line = raw_line.replace("${CLAUDE_PLUGIN_ROOT}/", " ")
            line = line.replace("${PLUGIN_ROOT}/", " ")
            line = line.replace("<plugin-root>/", " ")
            line = _URL_RE.sub(" ", line)
            for m in _PATH_TOKEN_RE.finditer(line):
                token = m.group(0)
                if _PLACEHOLDER_RE.search(token):
                    continue
                # token truncated by a template placeholder right after it
                if line[m.end():m.end() + 1] == "<":
                    continue
                if not _has_extension(token):
                    continue
                if not (root / token).is_file():
                    violations.append(
                        f"{rel}:{lineno}: plugin-root-anchored reference "
                        f"does not resolve: {token}"
                    )
    return violations


# --- check 5: relative markdown links must resolve ----------------------

_MD_LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def find_dangling_links(root: Path) -> list[str]:
    violations = []
    for path, text in iter_scan_files(root):
        rel = _rel(root, path)
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in _MD_LINK_RE.finditer(line):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:",
                                      "#", "/", "${")):
                    continue
                if _PLACEHOLDER_RE.search(target):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (path.parent / target_path)
                if not resolved.is_file():
                    violations.append(
                        f"{rel}:{lineno}: markdown link target does not "
                        f"resolve: {target}"
                    )
    return violations


# --- check 6: anchor citations must hit real headings -------------------

# "<token> § Heading text" where token is an .md path/basename or a
# crucible:<skill> invocation. Matched on whitespace-normalized text so
# citations survive line wrapping. The whole match is a lookahead, so the
# tail of one citation never consumes the next citation's token: every
# citation is examined. The lookbehind starts a token only at its first
# character, never inside a longer path or after ``crucible:``.
_CITE_RE = re.compile(
    r"(?<![A-Za-z0-9._/:-])(?="
    r"(?:crucible:(?P<skill>[a-z][a-z0-9-]*)"
    r"|(?P<path>[A-Za-z0-9._/-]*\.md))"
    r"`?\s*§\s*(?P<tail>[^§]{1,160}))"
)

#: Basename-only citation targets with a fixed repo-level meaning (frozen
#: interfaces on ``docs/authoring.md``'s anchor-stability list).
_FROZEN_BASENAMES = {
    "formats.md": "skills/redteaming/references/formats.md",
    "README.md": "hooks/README.md",
}

#: The records and the map cite the root README by its bare name; the
#: skills and hooks keep the frozen meaning above.
_DOCS_SURFACE_BASENAMES = {**_FROZEN_BASENAMES, "README.md": "README.md"}


def _is_docs_surface(rel: str) -> bool:
    return rel == UPSTREAM_MAP or rel.startswith(DECISIONS_DIR + "/")


def _headings(path: Path) -> list[str]:
    text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
    return [
        re.sub(r"\s+", " ", h).strip()
        for h in re.findall(r"^#{1,4}\s+(.+)$", text, re.MULTILINE)
    ]


def _resolve_citation_target(
    root: Path, source: Path, skill: str | None, path_token: str | None
) -> Path | None:
    if skill is not None:
        return root / "skills" / skill / "SKILL.md"
    assert path_token is not None
    if "/" in path_token:
        return root / path_token
    basenames = (
        _DOCS_SURFACE_BASENAMES if _is_docs_surface(_rel(root, source))
        else _FROZEN_BASENAMES
    )
    if path_token in basenames:
        return root / basenames[path_token]
    return source.parent / path_token


def find_dangling_anchor_citations(root: Path) -> list[str]:
    violations = []
    for path, text in iter_scan_files(root):
        rel = _rel(root, path)
        norm = re.sub(r"\s+", " ", text)
        for m in _CITE_RE.finditer(norm):
            if (m.group("path") or "").startswith(UPSTREAM_PREFIX):
                continue  # upstream's file, not crucible's
            if m.group("tail").lstrip().startswith("<"):
                continue  # template placeholder: `README.md § <heading>`
            target = _resolve_citation_target(
                root, path, m.group("skill"), m.group("path")
            )
            token = m.group("skill") or m.group("path")
            if target is None or not target.is_file():
                violations.append(
                    f"{rel}: anchor citation target missing: "
                    f"{token} § {m.group('tail')[:40].strip()}..."
                )
                continue
            tail = m.group("tail").strip()
            headings = _headings(target)
            if not any(tail.startswith(h) for h in headings):
                violations.append(
                    f"{rel}: anchor citation '{token} § "
                    f"{tail[:60]}' matches no heading in "
                    f"{_rel(root, target) if target.is_absolute() else target}"
                )
    return violations


# --- the real-tree gate -------------------------------------------------


def test_no_superpowers_invocation_strings() -> None:
    assert not find_superpowers_invocations(REPO_ROOT), "\n".join(
        find_superpowers_invocations(REPO_ROOT)
    )


def test_no_dropped_skill_invocation_shaped_references() -> None:
    assert not find_dropped_invocation_refs(REPO_ROOT), "\n".join(
        find_dropped_invocation_refs(REPO_ROOT)
    )


def test_crucible_invocations_name_shipped_skills() -> None:
    assert not find_unknown_crucible_invocations(REPO_ROOT), "\n".join(
        find_unknown_crucible_invocations(REPO_ROOT)
    )


def test_plugin_root_anchored_paths_resolve() -> None:
    assert not find_dangling_root_paths(REPO_ROOT), "\n".join(
        find_dangling_root_paths(REPO_ROOT)
    )


def test_relative_markdown_links_resolve() -> None:
    assert not find_dangling_links(REPO_ROOT), "\n".join(
        find_dangling_links(REPO_ROOT)
    )


def test_anchor_citations_resolve() -> None:
    assert not find_dangling_anchor_citations(REPO_ROOT), "\n".join(
        find_dangling_anchor_citations(REPO_ROOT)
    )


# --- seeded-violation trees: each class demonstrably fires --------------


def _seed_tree(tmp_path: Path, skill_text: str) -> Path:
    root = tmp_path / "plugin"
    skill_dir = root / "skills" / "demo-skill"
    skill_dir.mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(
        "---\nname: demo-skill\ndescription: seeded\n---\n" + skill_text,
        encoding="utf-8",
    )
    return root


def test_seeded_superpowers_string_is_caught(tmp_path: Path) -> None:
    root = _seed_tree(tmp_path, "Use superpowers:brainstorming here.\n")
    hits = find_superpowers_invocations(root)
    assert len(hits) == 1 and "superpowers" in hits[0]


def test_seeded_mixed_case_superpowers_string_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Use Superpowers:Brainstorming here.\n")
    hits = find_superpowers_invocations(root)
    assert len(hits) == 1 and "retired-namespace" in hits[0]


def test_seeded_dropped_namespace_invocation_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Invoke crucible:test-driven-development.\n")
    hits = find_dropped_invocation_refs(root)
    assert len(hits) == 1 and "test-driven-development" in hits[0]


def test_seeded_mixed_case_dropped_invocation_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Invoke Crucible:Test-Driven-Development.\n")
    hits = find_dropped_invocation_refs(root)
    assert len(hits) == 1 and "test-driven-development" in hits[0]


def test_seeded_dropped_link_target_is_caught(tmp_path: Path) -> None:
    root = _seed_tree(
        tmp_path, "See [tdd](../executing-plans/SKILL.md) for more.\n"
    )
    hits = find_dropped_invocation_refs(root)
    assert len(hits) == 1 and "executing-plans" in hits[0]


def test_seeded_dropped_bare_prose_mention_is_not_flagged(
    tmp_path: Path,
) -> None:
    root = _seed_tree(
        tmp_path,
        "Content ported from the old test-driven-development skill.\n",
    )
    assert find_dropped_invocation_refs(root) == []


def test_seeded_unknown_crucible_invocation_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Then run crucible:no-such-skill.\n")
    hits = find_unknown_crucible_invocations(root)
    assert len(hits) == 1 and "no-such-skill" in hits[0]


def test_seeded_mixed_case_unknown_crucible_invocation_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Then run Crucible:No-Such-Skill.\n")
    hits = find_unknown_crucible_invocations(root)
    assert len(hits) == 1 and "No-Such-Skill" in hits[0]


def test_seeded_dangling_root_path_is_caught(tmp_path: Path) -> None:
    root = _seed_tree(
        tmp_path, "Formats: skills/demo-skill/references/gone.md today.\n"
    )
    hits = find_dangling_root_paths(root)
    assert len(hits) == 1 and "gone.md" in hits[0]


def test_seeded_resolving_root_path_passes(tmp_path: Path) -> None:
    root = _seed_tree(tmp_path, "See skills/demo-skill/SKILL.md now.\n")
    assert find_dangling_root_paths(root) == []


def test_seeded_dangling_relative_link_is_caught(tmp_path: Path) -> None:
    root = _seed_tree(tmp_path, "Use the [prompt](missing-prompt.md).\n")
    hits = find_dangling_links(root)
    assert len(hits) == 1 and "missing-prompt.md" in hits[0]


def test_seeded_bad_anchor_citation_is_caught(tmp_path: Path) -> None:
    root = _seed_tree(
        tmp_path,
        "## Real heading\n\nPer SKILL.md § Bogus heading text, act.\n",
    )
    hits = find_dangling_anchor_citations(root)
    assert len(hits) == 1 and "Bogus heading" in hits[0]


def test_seeded_bad_anchor_citation_close_after_a_good_one_is_caught(
    tmp_path: Path,
) -> None:
    root = _seed_tree(
        tmp_path,
        "## Real heading\n\nPer SKILL.md § Real heading and\n"
        "`SKILL.md` § Bogus heading text, act.\n",
    )
    hits = find_dangling_anchor_citations(root)
    assert len(hits) == 1 and "Bogus heading" in hits[0]


def test_seeded_path_inside_a_cited_path_is_not_a_citation(
    tmp_path: Path,
) -> None:
    root = _seed_tree(
        tmp_path,
        "## Real heading\n\nPer `skills/demo-skill/SKILL.md` § Real heading.\n",
    )
    assert find_dangling_anchor_citations(root) == []


def test_seeded_good_anchor_citation_passes(tmp_path: Path) -> None:
    root = _seed_tree(
        tmp_path,
        "## Real heading\n\nPer SKILL.md § Real heading, wrapped\nlines "
        "still resolve.\n",
    )
    assert find_dangling_anchor_citations(root) == []


def _seed_docs_tree(tmp_path: Path, text: str, surface: str) -> Path:
    """A seeded tree with *text* written at *surface* (a posix relpath).

    The tree also carries a root ``README.md`` and a ``hooks/README.md``
    with distinct headings, so a bare ``README.md §`` citation shows which
    of the two it resolved to.
    """
    root = _seed_tree(tmp_path, "## Real heading\n\nSkill prose.\n")
    (root / "README.md").write_text(
        "# demo\n\n## Root heading\n", encoding="utf-8"
    )
    (root / "hooks").mkdir()
    (root / "hooks" / "README.md").write_text(
        "# hooks\n\n## Hook heading\n", encoding="utf-8"
    )
    target = root / surface
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return root


_DOCS_SURFACES = ("docs/decisions/demo-record.md", "docs/upstream.md")


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_dangling_path_in_docs_surface_is_caught(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path, "Per skills/demo-skill/references/gone.md today.\n", surface
    )
    hits = find_dangling_root_paths(root)
    assert len(hits) == 1 and surface in hits[0] and "gone.md" in hits[0]


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_missing_anchor_in_docs_surface_is_caught(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path,
        "Per crucible:demo-skill § Bogus heading, act.\n",
        surface,
    )
    hits = find_dangling_anchor_citations(root)
    assert len(hits) == 1 and "Bogus heading" in hits[0]


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_good_anchor_in_docs_surface_passes(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path, "Per `skills/demo-skill/SKILL.md` § Real heading.\n", surface
    )
    assert find_dangling_anchor_citations(root) == []


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_upstream_prefixed_paths_pass(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path,
        "Upstream's `superpowers/skills/executing-plans/` and\n"
        "`superpowers/skills/test-driven-development/SKILL.md`, per\n"
        "`superpowers/skills/writing-skills/SKILL.md` § Upstream heading.\n",
        surface,
    )
    assert find_dropped_invocation_refs(root) == []
    assert find_dangling_root_paths(root) == []
    assert find_dangling_anchor_citations(root) == []


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_unprefixed_dropped_path_in_docs_surface_is_caught(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path, "See `skills/executing-plans/` for the loop.\n", surface
    )
    hits = find_dropped_invocation_refs(root)
    assert len(hits) == 1 and "executing-plans" in hits[0]


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
def test_seeded_url_into_dropped_skill_passes(
    tmp_path: Path, surface: str
) -> None:
    root = _seed_docs_tree(
        tmp_path,
        "Upstream's https://github.com/obra/superpowers/tree/v6.2.0/"
        "skills/executing-plans and its\n"
        "[TDD skill](https://github.com/obra/superpowers/blob/v6.2.0/"
        "skills/test-driven-development/SKILL.md).\n",
        surface,
    )
    assert find_dropped_invocation_refs(root) == []
    assert find_dangling_links(root) == []


@pytest.mark.parametrize("surface", _DOCS_SURFACES)
@pytest.mark.parametrize(
    ("heading", "resolves"),
    [("Root heading", True), ("Hook heading", False),
     ("Missing heading", False)],
)
def test_docs_surface_bare_readme_citation_targets_root_readme(
    tmp_path: Path, surface: str, heading: str, resolves: bool
) -> None:
    root = _seed_docs_tree(
        tmp_path, f"See `README.md` § {heading} for more.\n", surface
    )
    hits = find_dangling_anchor_citations(root)
    assert (hits == []) is resolves, hits


@pytest.mark.parametrize(
    ("heading", "resolves"),
    [("Hook heading", True), ("Root heading", False)],
)
def test_skill_bare_readme_citation_targets_hooks_readme(
    tmp_path: Path, heading: str, resolves: bool
) -> None:
    root = _seed_docs_tree(tmp_path, "Record prose.\n", _DOCS_SURFACES[0])
    (root / "skills" / "demo-skill" / "notes.md").write_text(
        f"See `README.md` § {heading} for more.\n", encoding="utf-8"
    )
    hits = find_dangling_anchor_citations(root)
    assert (hits == []) is resolves, hits


def test_anchor_citation_with_placeholder_heading_is_skipped(
    tmp_path: Path,
) -> None:
    root = _seed_docs_tree(
        tmp_path,
        "A bare `README.md § <heading>` names the root README.\n",
        _DOCS_SURFACES[0],
    )
    assert find_dangling_anchor_citations(root) == []


def test_scanner_tolerates_binary_and_non_utf8_files(
    tmp_path: Path,
) -> None:
    root = _seed_tree(tmp_path, "Clean prose.\n")
    hooks = root / "hooks"
    hooks.mkdir()
    (hooks / "blob.bin").write_bytes(b"\xff\xfe\x00superpowers:\x9c")
    (root / "skills" / "demo-skill" / "stray.md").write_bytes(
        b"\xff\xfe invalid \x9c utf8"
    )
    # must neither crash nor report from undecodable files
    assert find_superpowers_invocations(root) == []
    scanned = {p.name for p, _ in iter_scan_files(root)}
    assert "blob.bin" not in scanned and "stray.md" not in scanned
