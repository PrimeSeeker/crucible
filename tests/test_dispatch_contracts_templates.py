"""The dispatch templates against the code and host that read them.

The seven instrument templates (``tools/instrument_agents.py``'s
``INSTRUMENTS``) are prose an agent reads, and this module pins none of
their wording. It reads the rendered templates, shared sections spliced
in, as the instruments receive them, not their sources. What it checks is where a template's text meets a reader
that is not a model:

- **the selectors** -- each selector-keyed passage of a template reaches
  the instrument exactly when its card's selector is set to its value,
  checked by resolving the template under every declared value;
- **the fresh-dispatch parameter** -- the Codex host's fork parameter is
  spelled in the adapter that drives that host and nowhere in the
  host-neutral templates.

The card and template grammars themselves (sections, slot lines, keyed
passages, runtime slots) are checked once, over all seven, in
``tests/test_instrument_agents.py``. Nothing here launches a model.
"""

from __future__ import annotations

import pytest

from instrument_corpus import (
    card_path,
    instruments,
    normalize,
    passages,
    raw,
    resolve,
    selector_values,
    template_markers,
)

TEMPLATES = sorted(instruments().values())
CODEX_ADAPTER = "skills/using-crucible/references/codex.md"


# --- selectors: a value's passage reaches the instrument only when set -----


def selection_leaks(template: str, card: str) -> list[str]:
    """Every way *template*'s passages fail to follow *card*'s selectors.

    For each passage and each value its selector declares, the template is
    resolved with that selector at that value (every other selector at its
    first declared value): the passage's block must be in the resolved
    text exactly when the value is the passage's own. A block that shows up
    under another value is text the instrument reads whatever the card
    says -- left unkeyed elsewhere, or keyed twice.
    """
    declared = selector_values(card)
    base = {name: values[0] for name, values in declared.items()}
    problems: list[str] = []
    for selector, value, block in passages(template):
        for candidate in declared.get(selector, ()):
            text = "\n" + resolve(template, {**base, selector: candidate}) + "\n"
            shown = f"\n{block}\n" in text
            own = candidate == value or any(
                (s, v, b) == (selector, candidate, block)
                for s, v, b in passages(template)
            )
            if shown != own:
                problems.append(
                    f"[[when {selector} = {value}]] block "
                    f"{'shown' if shown else 'hidden'} under {selector} = {candidate}"
                )
    return problems


@pytest.mark.parametrize("template", TEMPLATES)
def test_selector_value_passages_appear_only_when_selected(template: str) -> None:
    """Break: a selector value whose text the instrument reads whatever the
    card sets -- a passage also left in the fixed body, or keyed to the
    wrong value -- or one it never reads when the card sets it."""
    assert selection_leaks(raw(template), raw(card_path(template))) == []


@pytest.mark.parametrize("template", [t for t in TEMPLATES if template_markers(raw(t))])
def test_selection_leak_check_fires_on_an_unkeyed_copy(template: str) -> None:
    """The check demonstrably fires: a passage's block copied into the
    fixed body, outside any marker, shows under every value."""
    text = raw(template)
    _, _, block = passages(text)[0]
    seeded = text + "\n" + block + "\n"
    assert selection_leaks(seeded, raw(card_path(template))) != []


# --- the fresh-dispatch parameter lives in the adapter ---------------------


def test_fork_parameter_is_spelled_in_the_codex_adapter_and_no_template() -> None:
    """Break: the Codex fresh-dispatch parameter restated in a host-neutral
    template, or the adapter losing the spelling the host accepts."""
    # Consumer: the Codex host's spawn_agent call, which reads
    # `fork_turns: "none"` as "fork no history" -- the fresh-context
    # dispatch; an omitted value forks the full history.
    assert 'fork_turns: "none"' in raw(CODEX_ADAPTER)
    for template in TEMPLATES:
        for path in (template, card_path(template)):
            assert "fork_turns" not in raw(path), path


# --- the shared helpers ----------------------------------------------------


def test_passage_helpers_read_the_marker_grammar() -> None:
    """``passages``/``resolve``/``normalize`` on a synthetic template:
    passages keep and drop by selection, and malformed markers are
    refused rather than read."""
    text = "a\n[[when s = x]]\nb\n[[end]]\n[[when s = y]]\nc\n[[end]]\nd"
    assert passages(text) == [("s", "x", "b"), ("s", "y", "c")]
    assert resolve(text, {"s": "x"}) == "a\nb\nd"
    assert resolve(text, {"s": "y"}) == "a\nc\nd"
    assert resolve(text, {}) == "a\nd"
    assert normalize("a\r\n  b\tc") == "a b c"
    for bad in (
        "[[when a = b]]\n[[when c = d]]\n[[end]]\n[[end]]\n",
        "[[when a = b]]\ntext\n",
        "[[when a=b]]\n",
        "[[end]]\n",
    ):
        with pytest.raises(AssertionError):
            passages(bad)
