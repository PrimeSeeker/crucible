"""Codex packaging, the one registration, presentation metadata.

Covers both hosts' packaging, with Codex registering no hook:

- happy: both plugin manifests (``.claude-plugin/plugin.json``,
  ``.codex-plugin/plugin.json``) and both marketplace entries
  (``.claude-plugin/marketplace.json``, ``.agents/plugins/marketplace.json``)
  validate; required fields resolve; sources point at this repository;
  every version-bearing manifest agrees; every shipped
  ``skills/*/agents/openai.yaml`` validates;
- happy: the Codex manifest declares no hooks -- its ``hooks`` field is
  exactly ``{}``, which suppresses the auto-discovery of
  ``hooks/hooks.json`` that a missing field would trigger -- and no Codex
  registration file exists;
- happy: the Claude registration registers exactly one event,
  SessionStart, with one hook script, ``hooks/session-start``, and is
  pinned whole: its native variables, its ``startup|clear|compact``
  matcher and its shell-form command naming the host;
- edge: the Codex marketplace source and policy metadata validate without
  a marketplace version field (none is invented);
- error: a manifest with a missing required field, a version-mismatched
  manifest pair, or a ``hooks`` value that is neither a contained relative
  path nor exactly ``{}``, fails validation (seeded fixtures under
  ``tests/fixtures/manifests/`` and inline payloads).

Everything here parses files on disk. Nothing launches a model, a
subagent or a host;
the whole file runs unattended in the default suite.

The Codex schema facts asserted here were read off the Codex host's
bundled plugin tooling (the ``plugin-creator`` skill's
``references/plugin-json-spec.md`` and the ``plugin-eval`` plugin's
``src/evaluators/plugin.js`` / ``src/core/budget.js``): plugin.json
requires ``name``/``version``/``description``/``author``/``interface``,
its name is hyphen-case, its path fields start with ``./`` and must
resolve, a marketplace entry carries ``name``/``source``/``policy``/
``category`` and no version field, and ``agents/openai.yaml`` is an
optional presentation/policy document keyed under ``interface`` and
``policy``. The ``hooks: {}`` semantics were measured on codex-cli 0.160.0.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterator
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

CLAUDE_MANIFEST = REPO_ROOT / ".claude-plugin" / "plugin.json"
CLAUDE_MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
CODEX_MANIFEST = REPO_ROOT / ".codex-plugin" / "plugin.json"
CODEX_MARKETPLACE = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"

CLAUDE_HOOKS = REPO_ROOT / "hooks" / "hooks.json"
#: The Codex registration crucible no longer ships. Named only so its
#: absence can be asserted.
RETIRED_CODEX_HOOKS = REPO_ROOT / "hooks" / "codex-hooks.json"

SKILLS_DIR = REPO_ROOT / "skills"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "manifests"

PLUGIN_NAME = "crucible"

#: Top-level plugin.json fields the installed Codex schema requires.
CODEX_REQUIRED_FIELDS = ("name", "version", "description", "author", "interface")

#: Presentation fields every shipped Codex plugin carries under `interface`.
#:
#: SIX, deliberately, where the host's own ``plugin eval`` checks TEN. The
#: shipped ``.codex-plugin/plugin.json`` also carries two of the other four,
#: ``defaultPrompt`` and ``websiteURL`` (the repository URL, the plugin's
#: public home), unchecked here. The last two, ``privacyPolicyURL`` and
#: ``termsOfServiceURL``, are left out: crucible publishes no privacy policy
#: or terms of service, and the repository URL is neither. The evaluator
#: error-fails a missing field, so plugin-eval reports those two as
#: error-severity findings; the omission is intended, recorded here so a
#: reader comparing this tuple against a plugin-eval report is not left to
#: guess whether it is an oversight.
CODEX_REQUIRED_INTERFACE_FIELDS = (
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
)

#: Codex plugin.json fields whose value is a plugin-relative path.
CODEX_PATH_FIELDS = ("skills", "hooks", "mcpServers", "apps")

#: The one non-path value the ``hooks`` field may take: an empty inline
#: hook set, which registers nothing. Exactly ``{}`` -- a manifest with no
#: ``hooks`` field makes Codex auto-discover and run ``hooks/hooks.json``,
#: the Claude registration (measured on codex-cli 0.160.0).
CODEX_NO_HOOKS: dict = {}

CODEX_INSTALL_POLICIES = {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}
CODEX_AUTH_POLICIES = {"ON_INSTALL", "ON_USE"}

_HYPHEN_CASE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# --- loading ------------------------------------------------------------


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _fixture(name: str) -> dict:
    return _load(FIXTURES / name)


# --- validators (shared by the real files and the seeded fixtures) ------


def validate_codex_plugin_manifest(
    data: object, plugin_root: Path | None = None
) -> list[str]:
    """Problems with a Codex ``.codex-plugin/plugin.json`` payload."""
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["plugin.json must be a JSON object"]
    for field in CODEX_REQUIRED_FIELDS:
        if field not in data or data[field] in (None, "", {}, []):
            problems.append(f"plugin.json missing required field: {field}")
    name = data.get("name")
    if isinstance(name, str) and not _HYPHEN_CASE.match(name):
        problems.append(f"plugin name is not hyphen-case: {name!r}")
    author = data.get("author")
    if author is not None and (
        not isinstance(author, dict) or not author.get("name")
    ):
        problems.append("plugin.json author must be an object carrying a name")
    interface = data.get("interface")
    if interface is not None:
        if not isinstance(interface, dict):
            problems.append("plugin.json interface must be an object")
        else:
            for field in CODEX_REQUIRED_INTERFACE_FIELDS:
                if not interface.get(field):
                    problems.append(f"plugin.json interface missing: {field}")
    for field in CODEX_PATH_FIELDS:
        value = data.get(field)
        if value is None:
            continue
        if field == "hooks" and isinstance(value, dict) and value == CODEX_NO_HOOKS:
            continue
        if not isinstance(value, str) or not value.startswith("./"):
            exact = "exactly {} or " if field == "hooks" else ""
            problems.append(f"{field} must be {exact}a plugin-relative ./ path")
            continue
        if plugin_root is None:
            continue
        root = plugin_root.resolve()
        target = (root / value[2:]).resolve()
        if target != root and root not in target.parents:
            problems.append(f"{field} escapes the plugin root: {value}")
        elif not target.exists():
            problems.append(f"{field} points at a missing target: {value}")
    return problems


def validate_codex_marketplace(data: object, plugin_root: Path | None = None) -> list[str]:
    """Problems with a Codex ``.agents/plugins/marketplace.json`` payload."""
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["marketplace.json must be a JSON object"]
    if not data.get("name"):
        problems.append("marketplace.json missing required field: name")
    interface = data.get("interface")
    if interface is not None and not isinstance(interface, dict):
        problems.append("marketplace.json interface must be an object")
    entries = data.get("plugins")
    if not isinstance(entries, list) or not entries:
        return problems + ["marketplace.json plugins must be a non-empty array"]
    for index, entry in enumerate(entries):
        where = f"marketplace entry #{index}"
        if not isinstance(entry, dict):
            problems.append(f"{where} must be an object")
            continue
        if not entry.get("name"):
            problems.append(f"{where} missing required field: name")
        # A marketplace entry carries no version field: the plugin manifest
        # is the single version-bearing document on the Codex side.
        if "version" in entry:
            problems.append(f"{where} invents a marketplace version field")
        source = entry.get("source")
        if not isinstance(source, dict):
            problems.append(f"{where} missing required object: source")
        else:
            if source.get("source") != "local":
                problems.append(f"{where} source.source must be 'local'")
            path_value = source.get("path")
            if not isinstance(path_value, str) or not path_value.startswith("./"):
                problems.append(f"{where} source.path must be a ./ path")
            elif plugin_root is not None and not (
                plugin_root / path_value[2:]
            ).is_dir():
                problems.append(f"{where} source.path does not resolve")
        policy = entry.get("policy")
        if not isinstance(policy, dict):
            problems.append(f"{where} missing required object: policy")
        else:
            if policy.get("installation") not in CODEX_INSTALL_POLICIES:
                problems.append(f"{where} policy.installation is not allowed")
            if policy.get("authentication") not in CODEX_AUTH_POLICIES:
                problems.append(f"{where} policy.authentication is not allowed")
        if not entry.get("category"):
            problems.append(f"{where} missing required field: category")
    return problems


def validate_claude_plugin_manifest(data: object) -> list[str]:
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["plugin.json must be a JSON object"]
    for field in ("name", "version", "description", "author"):
        if not data.get(field):
            problems.append(f"plugin.json missing required field: {field}")
    return problems


def validate_claude_marketplace(data: object, plugin_root: Path | None = None) -> list[str]:
    problems: list[str] = []
    if not isinstance(data, dict):
        return ["marketplace.json must be a JSON object"]
    if not data.get("name"):
        problems.append("marketplace.json missing required field: name")
    entries = data.get("plugins")
    if not isinstance(entries, list) or not entries:
        return problems + ["marketplace.json plugins must be a non-empty array"]
    for index, entry in enumerate(entries):
        where = f"marketplace entry #{index}"
        if not isinstance(entry, dict):
            problems.append(f"{where} must be an object")
            continue
        for field in ("name", "version", "source"):
            if not entry.get(field):
                problems.append(f"{where} missing required field: {field}")
        source = entry.get("source")
        if isinstance(source, str) and plugin_root is not None:
            if not (plugin_root / source).is_dir():
                problems.append(f"{where} source does not resolve: {source}")
    return problems


def validate_version_sync(versions: dict[str, object]) -> list[str]:
    """Problems with the version-bearing metadata set: every member carries
    a version and all of them agree."""
    problems = [
        f"{label} carries no version" for label, v in versions.items() if not v
    ]
    distinct = {v for v in versions.values() if v}
    if len(distinct) > 1:
        problems.append(f"version mismatch across manifests: {versions}")
    return problems


# --- happy: the four shipped documents validate -------------------------


def test_codex_plugin_manifest_validates() -> None:
    problems = validate_codex_plugin_manifest(_load(CODEX_MANIFEST), REPO_ROOT)
    assert not problems, "\n".join(problems)


def test_claude_plugin_manifest_validates() -> None:
    problems = validate_claude_plugin_manifest(_load(CLAUDE_MANIFEST))
    assert not problems, "\n".join(problems)


def test_codex_marketplace_validates() -> None:
    problems = validate_codex_marketplace(_load(CODEX_MARKETPLACE), REPO_ROOT)
    assert not problems, "\n".join(problems)


def test_claude_marketplace_validates() -> None:
    problems = validate_claude_marketplace(_load(CLAUDE_MARKETPLACE), REPO_ROOT)
    assert not problems, "\n".join(problems)


def test_both_plugin_manifests_name_the_same_plugin() -> None:
    """The Codex operand of the ownership predicate is this same name."""
    assert _load(CODEX_MANIFEST)["name"] == PLUGIN_NAME
    assert _load(CLAUDE_MANIFEST)["name"] == PLUGIN_NAME


def test_marketplace_sources_point_at_this_repository() -> None:
    """Both marketplaces are self-hosted: the repo is marketplace + plugin."""
    claude_entry = _load(CLAUDE_MARKETPLACE)["plugins"][0]
    assert claude_entry["name"] == PLUGIN_NAME
    assert claude_entry["source"] == "./"

    codex_entry = _load(CODEX_MARKETPLACE)["plugins"][0]
    assert codex_entry["name"] == PLUGIN_NAME
    assert codex_entry["source"] == {"source": "local", "path": "./"}


def test_codex_manifest_paths_point_at_the_canonical_tree() -> None:
    """No copied or generated skill tree: the Codex package points at the
    one canonical ``skills/`` directory."""
    data = _load(CODEX_MANIFEST)
    assert data["skills"] == "./skills/"
    assert (REPO_ROOT / "skills").is_dir()
    assert not (REPO_ROOT / ".codex-plugin" / "skills").exists()


def test_codex_manifest_declares_no_hooks_and_no_codex_registration_exists() -> None:
    """Crucible registers no hook on Codex: the manifest's ``hooks`` is
    exactly ``{}`` and the old registration file is gone.

    The break: dropping the field instead (Codex then auto-discovers and
    runs ``hooks/hooks.json``, a hook crucible does not register there),
    any non-empty inline hook set, or a Codex registration file left behind
    for a later edit to point at again.
    """
    data = _load(CODEX_MANIFEST)
    assert "hooks" in data, "a missing field auto-discovers hooks/hooks.json"
    assert data["hooks"] == {} and isinstance(data["hooks"], dict)
    assert not RETIRED_CODEX_HOOKS.exists()
    assert sorted(p.name for p in (REPO_ROOT / "hooks").glob("*.json")) == [
        "hooks.json"
    ]


@pytest.mark.parametrize(
    "hooks, reason",
    [
        ({"SessionStart": []}, "plugin-relative ./ path"),
        ([], "plugin-relative ./ path"),
        ("", "plugin-relative ./ path"),
        ("hooks/hooks.json", "plugin-relative ./ path"),
        ("./hooks/absent.json", "missing target"),
        ("./../outside/hooks.json", "escapes the plugin root"),
    ],
    ids=["inline-hook-set", "empty-list", "empty-string", "no-dot-slash",
         "missing-target", "escapes-root"],
)
def test_codex_manifest_declares_no_hooks_rejects_any_other_hooks_value(
    hooks: object, reason: str
) -> None:
    """The validator accepts ``hooks`` only as exactly ``{}`` or a contained
    relative path that resolves; each other shape fails for its own reason.

    The break: a validator that waves through every dict (an inline hook set
    registers a hook) or a path that leaves the plugin tree.
    """
    data = {**_load(CODEX_MANIFEST), "hooks": hooks}
    problems = validate_codex_plugin_manifest(data, REPO_ROOT)
    assert len(problems) == 1 and reason in problems[0], problems


def test_codex_manifest_declares_no_hooks_still_accepts_a_contained_path() -> None:
    """The path form stays valid for a future registration: a ``./`` path
    that resolves inside the plugin root passes."""
    data = {**_load(CODEX_MANIFEST), "hooks": "./hooks/hooks.json"}
    assert validate_codex_plugin_manifest(data, REPO_ROOT) == []


def test_version_bearing_metadata_is_synchronized() -> None:
    versions = {
        ".claude-plugin/plugin.json": _load(CLAUDE_MANIFEST).get("version"),
        ".claude-plugin/marketplace.json": _load(CLAUDE_MARKETPLACE)["plugins"][0].get(
            "version"
        ),
        ".codex-plugin/plugin.json": _load(CODEX_MANIFEST).get("version"),
    }
    assert not validate_version_sync(versions), versions


# --- edge: no invented marketplace version field ------------------------


def test_codex_marketplace_carries_no_version_field_anywhere() -> None:
    """The version rule's negative half: the Codex marketplace schema has no
    version field, so none may be invented at any nesting level.

    Keyed on the parsed KEYS, not on a substring of the raw text: a
    substring check fires on the word appearing inside a description or a
    URL, which is prose about versions, not an invented field.
    """
    keys = [k for k in _keys(_load(CODEX_MARKETPLACE)) if "version" in k.lower()]
    assert keys == [], f"invented version field(s): {keys}"


def test_codex_marketplace_policy_metadata_is_explicit() -> None:
    entry = _load(CODEX_MARKETPLACE)["plugins"][0]
    assert entry["policy"]["installation"] in CODEX_INSTALL_POLICIES
    assert entry["policy"]["authentication"] in CODEX_AUTH_POLICIES
    assert entry["category"]


# --- error: seeded fixtures fail validation -----------------------------


@pytest.mark.parametrize(
    "fixture_name, reason",
    [
        ("codex-plugin-missing-version.json", "missing required field: version"),
        ("codex-plugin-missing-interface-field.json", "interface missing: category"),
        ("codex-plugin-bad-name.json", "not hyphen-case"),
    ],
)
def test_invalid_codex_manifest_fixture_fails_validation(
    fixture_name: str, reason: str
) -> None:
    """Each seeded fixture fails for its own named defect and nothing else,
    so a fixture that stops carrying its defect cannot keep passing on an
    unrelated problem (its ``hooks: {}`` is filler and is valid)."""
    problems = validate_codex_plugin_manifest(_fixture(fixture_name), REPO_ROOT)
    assert len(problems) == 1 and reason in problems[0], (fixture_name, problems)


def test_codex_marketplace_fixture_with_version_field_fails() -> None:
    problems = validate_codex_marketplace(
        _fixture("codex-marketplace-invented-version.json"), REPO_ROOT
    )
    assert any("version" in p for p in problems), problems


def test_version_mismatch_fixture_pair_fails_validation() -> None:
    claude = _fixture("version-mismatch-claude-plugin.json")
    codex = _fixture("version-mismatch-codex-plugin.json")
    problems = validate_version_sync(
        {"claude": claude.get("version"), "codex": codex.get("version")}
    )
    assert any("mismatch" in p for p in problems), problems


def test_missing_version_fails_the_sync_check() -> None:
    assert validate_version_sync({"claude": "0.1.1", "codex": None})


# --- the Claude registration: SessionStart only, pinned whole -----------


#: The one registration crucible ships, as parsed JSON. Pinned whole, and
#: only here: this case catches an added event, an added group, and any
#: drift inside the SessionStart entry itself -- its matcher, and the
#: shell-form command running the hook script, anchored at the plugin
#: root, with its host named as the argument.
_CLAUDE_SESSION_START = {
    "matcher": "startup|clear|compact",
    "hooks": [
        {
            "type": "command",
            "command": 'bash "${CLAUDE_PLUGIN_ROOT}/hooks/session-start" claude-code',
            "timeout": 30,
        }
    ],
}


def test_manifest_registers_session_start_only() -> None:
    """Crucible ships no PreToolUse hook: the Claude registration names
    exactly one event, SessionStart, and its one entry is the router
    injection, unchanged.

    The break: a tool-call hook registered again, or the SessionStart entry
    drifting while the registration is edited.
    """
    # Consumer: the host's plugin hook loader reads hooks/hooks.json.
    data = json.loads(CLAUDE_HOOKS.read_text(encoding="utf-8"))
    assert set(data["hooks"]) == {"SessionStart"}
    assert data == {"hooks": {"SessionStart": [_CLAUDE_SESSION_START]}}


# --- project-agnostic registration -------------------------------------


def _string_values(node: object) -> Iterator[str]:
    """Every string VALUE in a parsed JSON document, at any depth."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for value in node.values():
            yield from _string_values(value)
    elif isinstance(node, list):
        for value in node:
            yield from _string_values(value)


def _keys(node: object) -> Iterator[str]:
    """Every object KEY in a parsed JSON document, at any depth."""
    if isinstance(node, dict):
        for key, value in node.items():
            yield key
            yield from _keys(value)
    elif isinstance(node, list):
        for value in node:
            yield from _keys(value)


#: A Windows drive anchor: exactly ONE letter, then a colon and a separator,
#: at the START of the value. Unanchored (``[A-Za-z]:[\\/]``) this matched
#: ``https://`` inside any URL, so the guard would have false-failed the
#: moment a homepage or documentation field was added -- such as the
#: ``homepage``, ``repository`` and ``websiteURL`` fields the manifests carry.
_DRIVE_ANCHOR = re.compile(r"^[A-Za-z]:[\\/]")
#: A UNC root. Also an absolute host path, and not URL-shaped.
_UNC_ANCHOR = re.compile(r"^\\\\[^\\]")


@pytest.mark.parametrize(
    "path",
    [
        CLAUDE_HOOKS,
        CODEX_MANIFEST,
        CLAUDE_MANIFEST,
        CODEX_MARKETPLACE,
        CLAUDE_MARKETPLACE,
    ],
    ids=[
        "claude-hooks",
        "codex-plugin",
        "claude-plugin",
        "codex-market",
        "claude-market",
    ],
)
def test_registration_metadata_bakes_in_no_project_policy(path: Path) -> None:
    """No repository path, branch name or project policy in the shipped
    manifests or registrations -- project policy is the project's own
    business, never baked into the plugin.

    Keyed on the PARSED structure, not on a substring of the raw file: the
    absolute-path check runs per string value and is anchored, so a URL is
    not mistaken for a drive-letter path.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    baked = [
        value
        for value in _string_values(data)
        if _DRIVE_ANCHOR.match(value) or _UNC_ANCHOR.match(value)
    ]
    assert baked == [], f"absolute host path baked into {path.name}: {baked}"
    text = path.read_text(encoding="utf-8")
    for banned in ("protected_branches", "protected_checkouts"):
        assert banned not in text, f"project policy baked into {path.name}: {banned}"


def test_the_absolute_path_guard_still_fires_and_spares_urls() -> None:
    """The guard's own both-directions proof.

    Break caught: an unanchored pattern. ``[A-Za-z]:[\\/]`` matches
    ``https://`` and would false-fail every manifest the moment a URL field
    lands; an over-narrow one would let a real ``C:/Users/...`` through.
    """
    assert _DRIVE_ANCHOR.match("C:/Users/example/repo")
    assert _DRIVE_ANCHOR.match(r"D:\repo")
    assert _UNC_ANCHOR.match(r"\\server\share\repo")
    assert not _DRIVE_ANCHOR.match("https://example.invalid/crucible")
    assert not _DRIVE_ANCHOR.match("file:///C:/Users")  # caught by shape, not path
    assert not _DRIVE_ANCHOR.match("./skills/")
    assert list(_string_values({"a": ["x", {"b": "y"}], "c": 3})) == ["x", "y"]
    assert sorted(_keys({"a": {"b": 1}, "c": [{"d": 2}]})) == ["a", "b", "c", "d"]


# --- presentation metadata: skills/*/agents/openai.yaml -----------------


def _parse_simple_yaml(text: str) -> dict:
    """Parse the two-level ``key:``/``  key: value`` shape these files use.

    Deliberately strict and dependency-free (the suite is stdlib + pytest):
    anything outside that shape raises, which is itself the contract the
    shipped presentation files are held to.
    """
    root: dict[str, object] = {}
    section: dict[str, object] | None = None
    for lineno, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        key, sep, value = raw.strip().partition(":")
        if not sep or not key:
            raise ValueError(f"line {lineno}: not a 'key: value' line: {raw!r}")
        value = value.strip()
        if value[:1] in {'"', "'"} and value[-1:] == value[:1] and len(value) >= 2:
            value = value[1:-1]
        if indent == 0:
            if value:
                root[key] = value
                section = None
            else:
                section = {}
                root[key] = section
        else:
            if section is None:
                raise ValueError(f"line {lineno}: indented key outside a section")
            section[key] = value
    return root


def _shipped_skills() -> list[Path]:
    return sorted(
        d for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()
    )


def _openai_yaml_files() -> list[Path]:
    return sorted(SKILLS_DIR.glob("*/agents/openai.yaml"))


def test_every_shipped_skill_carries_presentation_metadata() -> None:
    """The presentation set is the whole roster: a partial set renders an
    inconsistent skill list on the Codex surface."""
    with_yaml = {p.parent.parent.name for p in _openai_yaml_files()}
    assert with_yaml == {d.name for d in _shipped_skills()}


def test_every_openai_yaml_validates() -> None:
    problems: list[str] = []
    for path in _openai_yaml_files():
        rel = path.relative_to(REPO_ROOT).as_posix()
        try:
            data = _parse_simple_yaml(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            problems.append(f"{rel}: {exc}")
            continue
        interface = data.get("interface")
        if not isinstance(interface, dict):
            problems.append(f"{rel}: no 'interface' mapping")
            continue
        if set(data) - {"interface"}:
            problems.append(f"{rel}: unexpected top-level keys: {set(data)}")
        for field in ("display_name", "short_description"):
            if not interface.get(field):
                problems.append(f"{rel}: interface missing {field}")
    assert not problems, "\n".join(problems)


def test_presentation_metadata_carries_no_policy_override() -> None:
    """These files are presentation only: no invocation-policy key, so the
    host's implicit-invocation default (and the router's index) still
    governs which skills are reachable.

    Keyed on the parsed keys, not on a substring: the word appearing inside
    a description ("the redteam policy this skill enforces") is prose, not a
    policy override, and a substring check would fail on it.
    """
    for path in _openai_yaml_files():
        parsed = _parse_simple_yaml(path.read_text(encoding="utf-8"))
        offenders = [k for k in _keys(parsed) if "policy" in k.lower()]
        assert offenders == [], f"{path}: policy override key(s) {offenders}"
