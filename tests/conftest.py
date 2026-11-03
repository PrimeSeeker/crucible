"""Shared fixtures for the crucible repo test suite.

Tests run with any system Python >= 3.10 plus pytest -- stdlib only, no
third-party imports beyond pytest itself.
"""

from __future__ import annotations

import pytest

# The SessionStart hook picks its output by this variable (hooks/README.md
# § SessionStart injection), and a session running the suite passes its own
# value to every hook the tests start.
ATTENDED_VARIABLE = "CLAUDE_CODE_SESSION_ATTENDED"


@pytest.fixture(autouse=True)
def _no_inherited_attended_variable(monkeypatch: pytest.MonkeyPatch) -> None:
    """Every test starts the hook as an attended session does, whatever the
    session running the suite is; a test wanting another value sets it."""
    monkeypatch.delenv(ATTENDED_VARIABLE, raising=False)
