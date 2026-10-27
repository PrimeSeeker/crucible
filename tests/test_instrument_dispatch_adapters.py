"""The Claude Code dispatch reference names the plugin agents the way the
host exposes them.

Claude Code exposes a plugin's agents as ``<plugin>:<agent name>``: the
plugin name from ``.claude-plugin/plugin.json`` and each agent's
frontmatter ``name``. The dispatch reference tells a controller which agent
to start for an instrument by that pattern, so its prefix must be the
plugin's name. The pattern is all the reference spells: a literal
``crucible:<instrument>``
would name no shipped skill, which ``tests/test_references.py`` already
refuses everywhere under ``skills/``.
"""

from __future__ import annotations

import json
import re

from instrument_corpus import REPO_ROOT, raw

#: The Claude Code reference that spells the instrument-dispatch pattern.
CLAUDE_CODE_REFERENCE = "skills/using-crucible/references/claude-code-dispatch.md"


def test_adapter_instrument_claude_pattern_is_the_hosts_agent_name() -> None:
    """Break: the adapter's agent pattern drifting from the plugin name the
    host prefixes agents with, so the subagent type it names resolves to
    no agent."""
    plugin = json.loads((REPO_ROOT / ".claude-plugin" / "plugin.json").read_text("utf-8"))
    adapter = raw(CLAUDE_CODE_REFERENCE)
    # Consumer: the host's agent dispatch, which resolves the subagent type
    # `<plugin name>:<agent frontmatter name>`; the placeholder stands for
    # the latter (tests/test_instrument_agents.py pins each agent's `name`).
    patterns = set(re.findall(r"`([a-z0-9-]+):<[^<>`]+>`", adapter))
    assert patterns == {plugin["name"]}
