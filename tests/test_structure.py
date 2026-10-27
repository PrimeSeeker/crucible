"""Structure checks.

Manifest, layout and frontmatter:

- the plugin manifest exists, parses, and is named ``crucible``;
- the plugin-root layout directories exist;
- every ``SKILL.md`` under ``skills/`` has frontmatter with ``name`` and
  ``description``.

Skill directories, router index and citations:

- directory-completeness: every *immediate* ``skills/*`` directory must
  contain a SKILL.md (reference-only directories like
  ``redteaming/references`` are sub-subdirectories and exempt by
  construction);
- frontmatter ``name`` matches the directory name;
- the router index (``skills/using-crucible/SKILL.md`` section "Skill
  Index") names every shipped skill exactly once, and names nothing
  else;
- forward citations: every bare sibling-file token a SKILL.md cites in
  backticks resolves inside that skill's directory tree (workspace/host
  artifact names that are runtime state, not repo files, are
  allowlisted);
- orphan rule: every
  non-SKILL ``.md`` file under ``skills/`` must be cited -- its basename
  must appear in at least one OTHER ``.md`` file under ``skills/`` or
  ``hooks/``. SKILL.md files and hooks/README.md are roots and need no
  citation; non-md siblings (scripts, examples with other extensions)
  are outside the orphan rule.
"""

import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / ".claude-plugin" / "plugin.json"
CODEX_MANIFEST = REPO_ROOT / ".codex-plugin" / "plugin.json"
SKILLS_DIR = REPO_ROOT / "skills"


def _parse_frontmatter(text: str) -> dict[str, str] | None:
    """Parse a YAML frontmatter block without a YAML dependency.

    Returns a mapping of top-level ``key: value`` pairs, or None when the
    file has no leading ``---`` frontmatter fence. Only flat string keys
    are extracted -- enough for the ``name``/``description`` contract.
    """
    if not text.startswith("---"):
        return None
    match = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.DOTALL)
    if match is None:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


# --- manifest -----------------------------------------------------------


def test_manifest_exists() -> None:
    assert MANIFEST.is_file(), f"missing plugin manifest: {MANIFEST}"


def test_manifest_parses_and_is_named_crucible() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert data["name"] == "crucible"


def test_codex_manifest_parses_and_is_named_crucible() -> None:
    data = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))
    assert data["name"] == "crucible"


# --- layout -------------------------------------------------------------


@pytest.mark.parametrize("dirname", ["skills", "hooks", "tests", "docs"])
def test_plugin_root_layout(dirname: str) -> None:
    assert (REPO_ROOT / dirname).is_dir(), f"missing layout dir: {dirname}/"


def test_license_present() -> None:
    assert (REPO_ROOT / "LICENSE").is_file()


# --- skills frontmatter (only for SKILL.md files that exist) ------------


def _existing_skill_files() -> list[Path]:
    if not SKILLS_DIR.is_dir():
        return []
    return sorted(SKILLS_DIR.rglob("SKILL.md"))


def test_existing_skill_files_have_name_and_description() -> None:
    # Consumer: each host's skill loader reads `name` and `description`
    # from SKILL.md frontmatter to list and select the skill.
    problems: list[str] = []
    for skill_file in _existing_skill_files():
        rel = skill_file.relative_to(REPO_ROOT)
        text = skill_file.read_text(encoding="utf-8")
        fields = _parse_frontmatter(text)
        if fields is None:
            problems.append(f"{rel}: no frontmatter block")
            continue
        for key in ("name", "description"):
            if not fields.get(key):
                problems.append(f"{rel}: frontmatter missing '{key}'")
    assert not problems, "\n".join(problems)


# --- skill directories ------------------------------------------------


def _skill_dirs() -> list[Path]:
    """Immediate subdirectories of skills/ (each must be a skill)."""
    return sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())


def test_every_skill_dir_has_skill_md() -> None:
    missing = [
        d.name for d in _skill_dirs() if not (d / "SKILL.md").is_file()
    ]
    assert not missing, (
        f"skills/* dirs without SKILL.md: {missing}"
    )


def test_frontmatter_name_matches_directory() -> None:
    problems: list[str] = []
    for d in _skill_dirs():
        skill_file = d / "SKILL.md"
        if not skill_file.is_file():
            continue  # covered by test_every_skill_dir_has_skill_md
        fields = _parse_frontmatter(
            skill_file.read_text(encoding="utf-8")
        ) or {}
        if fields.get("name") != d.name:
            problems.append(
                f"skills/{d.name}/SKILL.md: frontmatter name "
                f"{fields.get('name')!r} != directory name {d.name!r}"
            )
    assert not problems, "\n".join(problems)


# --- roster parity: the Codex package ships the canonical tree ----------


def _canonical_roster() -> set[str]:
    return {d.name for d in _skill_dirs() if (d / "SKILL.md").is_file()}


def _codex_skills_dir() -> Path:
    """The skills directory the Codex package declares."""
    data = json.loads(CODEX_MANIFEST.read_text(encoding="utf-8"))
    declared = data["skills"]
    assert isinstance(declared, str) and declared.startswith("./"), declared
    return (REPO_ROOT / declared[2:]).resolve()


def test_codex_package_roster_matches_the_canonical_tree() -> None:
    """One canonical skill tree: the roster enumerated through the Codex
    package is the roster enumerated from skills/ -- the same directory,
    not copied or generated content."""
    codex_dir = _codex_skills_dir()
    assert codex_dir == SKILLS_DIR.resolve(), (
        f"Codex package points at {codex_dir}, not the canonical "
        f"{SKILLS_DIR.resolve()}"
    )
    codex_roster = {
        d.name
        for d in codex_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    }
    assert codex_roster == _canonical_roster()


def test_codex_package_carries_no_copied_skill_tree() -> None:
    codex_pkg = REPO_ROOT / ".codex-plugin"
    assert codex_pkg.is_dir()
    copies = [
        p.relative_to(REPO_ROOT).as_posix() for p in codex_pkg.rglob("SKILL.md")
    ]
    assert not copies, f"copied skill content under .codex-plugin/: {copies}"


# --- router index -------------------------------------------------------

ROUTER = SKILLS_DIR / "using-crucible" / "SKILL.md"
#: An index entry: the plugin-namespaced skill name `crucible:<name>`, which
#: the host's skill loader resolves to skills/<name>/SKILL.md.
_INDEX_ENTRY_RE = re.compile(r"^- `crucible:([a-z][a-z0-9-]*)`", re.M)


def _router_index_section() -> str:
    """The router's ``## Skill Index`` section. The heading is this test's
    anchor into the router, not a pinned sentence: renamed, this fails
    loudly rather than passing on an empty section."""
    text = ROUTER.read_text(encoding="utf-8")
    match = re.search(
        r"^## Skill Index\s*$(.*?)(?=^## |\Z)", text, re.M | re.DOTALL
    )
    assert match is not None, "router has no '## Skill Index' section"
    return match.group(1)


def test_router_index_names_every_skill_exactly_once() -> None:
    entries = _INDEX_ENTRY_RE.findall(_router_index_section())
    shipped = {d.name for d in _skill_dirs() if (d / "SKILL.md").is_file()}
    problems: list[str] = []
    for name in sorted(shipped):
        count = entries.count(name)
        if count != 1:
            problems.append(
                f"router index names crucible:{name} {count} times "
                f"(want exactly 1)"
            )
    for name in entries:
        if name not in shipped:
            problems.append(
                f"router index entry crucible:{name} is not a shipped "
                f"skill"
            )
    assert not problems, "\n".join(problems)


# --- forward citations: SKILL.md-cited sibling files exist --------------

#: Backticked file-shaped tokens that are runtime/host artifacts, not
#: repo files: workspace state the skills create at run time, and files
#: living in the host project rather than this plugin.
NON_REPO_FILE_MENTIONS = {
    "ledger.md",              # SDD ledger, created in the feature workspace
    "record.md",              # round record, feature workspace
    "digest.md",              # design digest, feature workspace
    "brainstorm-decisions.md",  # brainstorm record, feature workspace
    "CLAUDE.md",              # host-project instruction files
    "AGENTS.md",
    "GEMINI.md",
}

_BARE_FILE_TOKEN_RE = re.compile(
    r"`([A-Za-z0-9._-]+\.(?:md|sh|ts|js|py|dot|json))`"
)


def test_skill_md_cited_sibling_files_exist() -> None:
    problems: list[str] = []
    for d in _skill_dirs():
        skill_file = d / "SKILL.md"
        if not skill_file.is_file():
            continue
        text = skill_file.read_text(encoding="utf-8")
        in_dir = {p.name for p in d.rglob("*") if p.is_file()}
        for token in _BARE_FILE_TOKEN_RE.findall(text):
            if "<" in token or token in NON_REPO_FILE_MENTIONS:
                continue
            if token == "SKILL.md":
                continue  # self-reference
            if token not in in_dir:
                problems.append(
                    f"skills/{d.name}/SKILL.md cites `{token}` but no "
                    f"such file exists under skills/{d.name}/"
                )
    assert not problems, "\n".join(problems)


# --- orphan rule --------------------------------------------------------


def test_no_orphan_md_files_in_skill_dirs() -> None:
    all_md = sorted(SKILLS_DIR.rglob("*.md"))
    hooks_md = sorted((REPO_ROOT / "hooks").rglob("*.md"))
    corpus = {
        p: p.read_text(encoding="utf-8") for p in all_md + hooks_md
    }
    problems: list[str] = []
    for p in all_md:
        if p.name == "SKILL.md":
            continue  # roots: loaded via the skill mechanism itself
        cited = any(
            p.name in text for other, text in corpus.items() if other != p
        )
        if not cited:
            problems.append(
                f"{p.relative_to(REPO_ROOT).as_posix()}: orphan -- no "
                f"other .md under skills/ or hooks/ cites it"
            )
    assert not problems, "\n".join(problems)
