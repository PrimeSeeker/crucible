"""SessionStart hook: the spill budget.

``tests/test_router.py`` owns the router content, and
``tests/test_hook_script.py`` the registration, the document and the
failure posture. What remains here is the budget: the rendered envelope
stays under 10,000 characters, Claude Code's threshold for writing a hook's
``additionalContext`` to disk (basis in the budget test's docstring).
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(TESTS_DIR))

import hook_runner as hr  # noqa: E402  (path inserted above; not a package)

# Claude Code's hook-output persistence threshold; basis in
# test_session_start_rendered_envelope_stays_under_the_spill_budget.
SPILL_BUDGET_CHARS = 10_000


@pytest.mark.skipif(hr.find_bash() is None, reason=hr.no_bash_reason())
def test_session_start_rendered_envelope_stays_under_the_spill_budget() -> None:
    """The rendered SessionStart context stays under the length at which
    Claude Code stops putting it in the session whole.

    Basis, read in the Claude Code 2.1.292 binary: the hook-output
    persistence function returns the text unchanged while ``length <=
    threshold`` and its default threshold is ``1e4``; the command-hook
    ``additionalContext`` call passes no threshold of its own. Above it the
    host writes the text to disk, logs the ``tengu_hook_output_persisted``
    event and leaves a stand-in in the session; where the write fails it
    cuts the text inline, with a "truncated at ... chars -- persist-to-disk
    failed" message. Those two strings survive minification; locate the
    function by them, not by its identifiers, and re-measure on a host
    upgrade.

    An overrun is remediated in the router and host-map prose, never by
    raising this bound past the host's threshold.
    """
    size = len(hr.envelope())
    assert size < SPILL_BUDGET_CHARS, (
        f"the envelope is {size} characters; trim the router or "
        f"host-map prose to stay under the host's "
        f"{SPILL_BUDGET_CHARS}-character threshold"
    )
