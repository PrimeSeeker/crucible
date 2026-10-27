"""The templated instruments as their readers parse them: templates, slot
cards, selector-keyed passages, and the code that consumes them.

A helper module, not a test module (as ``tests/skill_corpus.py`` is): the
instrument tests share one reading of the line grammars here rather than
each carrying a copy. Every grammar below is structure -- a card's ``##``
sections and ``- <slot>: <rule>`` lines, a template's ``[[when ...]]`` /
``[[end]]`` passages -- never a sentence of the shipped prose.

The instrument list and each family's runtime slot are imported from
``tools/instrument_agents.py``, the generator that reads the templates;
nothing here restates them.
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import re
import sys
from pathlib import Path
from types import ModuleType

from skill_corpus import is_skill_md, skill_corpus

REPO_ROOT = Path(__file__).resolve().parent.parent


# --- loading the code that consumes the text ------------------------------


def load_module(relpath: str, name: str) -> ModuleType:
    """A repository script loaded by path (``tools/`` and the skills'
    ``scripts/`` are not packages). Registered in ``sys.modules`` before
    execution: dataclasses resolve their annotations through it."""
    if name in sys.modules:
        return sys.modules[name]
    loader = importlib.machinery.SourceFileLoader(name, str(REPO_ROOT / relpath))
    spec = importlib.util.spec_from_loader(name, loader)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    loader.exec_module(module)
    return module


def load_generator() -> ModuleType:
    """``tools/instrument_agents.py``: the instrument table, the runtime
    slot of each family, and the render the committed agents are checked
    against."""
    return load_module("tools/instrument_agents.py", "crucible_instrument_agents")


def load_conserve() -> ModuleType:
    """``skills/redteaming/scripts/conserve.py``: the conservation
    check that collects seat ids from seat reports."""
    return load_module("skills/redteaming/scripts/conserve.py", "crucible_conserve")


# --- reading files --------------------------------------------------------


def normalize(text: str) -> str:
    """Whitespace-flattened, so a re-wrapped line still matches."""
    return re.sub(r"\s+", " ", text.replace("\r\n", "\n"))


def raw(relpath: str, root: Path = REPO_ROOT) -> str:
    """*relpath*'s text, LF-normalized; a SKILL.md reads as its corpus (the
    file plus the on-demand references its stubs name)."""
    if is_skill_md(relpath):
        return skill_corpus(relpath, root)
    return (root / relpath).read_text("utf-8").replace("\r\n", "\n")


def instruments() -> dict[str, str]:
    """Instrument name -> template path, from the generator."""
    return dict(load_generator().INSTRUMENTS)


def family(template: str) -> str:
    """The template family -- a key of the generator's ``RUNTIME_SLOTS``:
    ``redteaming`` for the redteaming skill's templates, ``sdd`` for the
    rest (the SDD templates and the branch reviewer, which share the
    ``[SLOT]`` spelling)."""
    return "redteaming" if template.startswith("skills/redteaming/") else "sdd"


def runtime_slots(template: str) -> frozenset[str]:
    """The runtime slot tokens *template*'s family spells: one, the
    runtime name."""
    return frozenset(load_generator().RUNTIME_SLOTS[family(template)])


def card_path(template: str) -> str:
    """A template's sibling slot card, ``<stem>.slots.md``."""
    return template[: -len(".md")] + ".slots.md"


# --- the slot card grammar ------------------------------------------------

#: A card's ``##`` sections, in order.
CARD_SECTIONS = ("## Slots", "## Selectors", "## Dispatch")

#: A card is at most this many characters unfilled.
CARD_BUDGET = 3000

#: A slot token as each family spells it: ``{slot}`` / ``[SLOT]``.
SLOT_TOKEN = {"redteaming": r"\{[^{}]+\}", "sdd": r"\[[A-Z][A-Z0-9_]*\]"}
CARD_SLOT_RE = re.compile(
    rf"^- ({SLOT_TOKEN['redteaming']}|{SLOT_TOKEN['sdd']}): (\S.*)$"
)
CARD_SELECTOR_RE = re.compile(r"^- ([a-z0-9-]+): ([a-z0-9-]+(?: \| [a-z0-9-]+)*)$")
CARD_VALUE_RE = re.compile(r"^  - ([a-z0-9-]+): (\S.*)$")


def card_sections(card: str) -> dict[str, list[str]]:
    """*card*'s raw, non-blank lines under each ``##`` heading."""
    sections: dict[str, list[str]] = {}
    current: list[str] | None = None
    for line in card.replace("\r\n", "\n").split("\n"):
        if line.startswith("## "):
            current = sections.setdefault(line.strip(), [])
        elif line.strip() and current is not None:
            current.append(line.rstrip())
    return sections


def card_slots(card: str) -> dict[str, str]:
    """``{token: fill rule}`` for each ``## Slots`` line of *card*."""
    slots = {}
    for line in card_sections(card).get("## Slots", []):
        m = CARD_SLOT_RE.match(line)
        if m:
            slots[m.group(1)] = m.group(2)
    return slots


def card_selectors(card: str) -> dict[str, dict[str, str]]:
    """``{selector: {value: passages}}`` from *card*'s ``## Selectors``.

    Raises ``AssertionError`` on any line that is neither a selector line
    nor one of its value sub-bullets, so a caller reads the grammar rather
    than skipping what it does not recognize.
    """
    selectors: dict[str, dict[str, str]] = {}
    declared: tuple[str, ...] = ()
    current: str | None = None
    for line in card_sections(card).get("## Selectors", []):
        if line.strip() == "none" and not selectors:
            continue
        sel = CARD_SELECTOR_RE.match(line)
        val = CARD_VALUE_RE.match(line)
        if sel:
            current = sel.group(1)
            declared = tuple(sel.group(2).split(" | "))
            selectors[current] = {}
        elif val and current is not None:
            assert val.group(1) in declared, line
            selectors[current][val.group(1)] = val.group(2)
        else:
            raise AssertionError(f"not a selector line: {line!r}")
    return selectors


def selector_values(card: str) -> dict[str, tuple[str, ...]]:
    """``{selector: values}`` as each selector line declares them."""
    out = {}
    for line in card_sections(card).get("## Selectors", []):
        m = CARD_SELECTOR_RE.match(line)
        if m:
            out[m.group(1)] = tuple(m.group(2).split(" | "))
    return out


# --- the template's selector-keyed passages -------------------------------

MARKER_OPEN_RE = re.compile(r"^\[\[when ([a-z0-9-]+) = ([a-z0-9-]+)\]\]$")
MARKER_END = "[[end]]"


def passages(template: str) -> list[tuple[str, str, str]]:
    """``(selector, value, block)`` for every passage of *template*'s raw
    text, in order, *block* being its lines between the markers. Asserts
    the passages are closed and never nest, and that no line outside a
    code span half-writes a marker."""
    found: list[tuple[str, str, str]] = []
    open_: tuple[str, str] | None = None
    body: list[str] = []
    for line in template.replace("\r\n", "\n").split("\n"):
        m = MARKER_OPEN_RE.match(line)
        if m:
            assert open_ is None, f"nested passage at {line!r}"
            open_ = (m.group(1), m.group(2))
            body = []
        elif line == MARKER_END:
            assert open_ is not None, "[[end]] with no open passage"
            found.append((*open_, "\n".join(body)))
            open_ = None
        else:
            if "[[" in line:
                assert "`[[" in line, f"malformed passage marker: {line!r}"
            if open_ is not None:
                body.append(line)
    assert open_ is None, f"unclosed passage {open_}"
    return found


def template_markers(template: str) -> list[tuple[str, str]]:
    """The ``(selector, value)`` of every passage, in order."""
    return [(sel, val) for sel, val, _ in passages(template)]


def resolve(template: str, selection: dict[str, str]) -> str:
    """*template*'s raw text as an instrument reads it under *selection*:
    each passage kept where the selection sets its selector to its value,
    dropped otherwise, the marker lines removed."""
    kept: list[str] = []
    keep = True
    for line in template.replace("\r\n", "\n").split("\n"):
        m = MARKER_OPEN_RE.match(line)
        if m:
            keep = selection.get(m.group(1)) == m.group(2)
        elif line == MARKER_END:
            keep = True
        elif keep:
            kept.append(line)
    return "\n".join(kept)
