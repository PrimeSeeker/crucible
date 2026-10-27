"""A skill's text as a controller reads it: its SKILL.md plus every
on-demand reference a stub in it sends the controller to read in full.

Route-conditional sections live in `skills/<skill>/references/` and are
loaded only on their route. A stub keeps
the section's heading in SKILL.md and names its reference in the form
``read `skills/<skill>/references/<file>.md` in full``. Tests that read a
skill's text read this corpus, so a check follows its text into the
reference instead of passing vacuously once the text has moved.

``STUB_RE`` finds a stub by that sentence shape: it is how this helper
locates the references, and a stub reworded past it drops out of the
corpus loudly -- ``tests/test_skill_references.py`` holds the stub set to
the extraction's file pairs.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

STUB_RE = re.compile(
    r"read `(skills/[a-z0-9-]+/references/[A-Za-z0-9._-]+\.md)` in full"
)
_HEADING_RE = re.compile(r"^#{1,4} .+$", re.MULTILINE)


def _raw(relpath: str, root: Path) -> str:
    return (root / relpath).read_text("utf-8").replace("\r\n", "\n")


def stub_references(skill_md: str, root: Path = REPO_ROOT) -> list[tuple[str, str]]:
    """(stub heading, reference path) for each stub in *skill_md*, the
    heading being the nearest one above the stub's read-in-full sentence."""
    text = _raw(skill_md, root)
    found = []
    for m in STUB_RE.finditer(text):
        headings = _HEADING_RE.findall(text[: m.start()])
        found.append((headings[-1] if headings else "", m.group(1)))
    return found


def is_skill_md(relpath: str) -> bool:
    return relpath.startswith("skills/") and relpath.endswith("/SKILL.md")


def skill_corpus(skill_md: str, root: Path = REPO_ROOT) -> str:
    """*skill_md*'s text followed by each stub-named reference's text."""
    parts = [_raw(skill_md, root)]
    parts += [_raw(ref, root) for _, ref in stub_references(skill_md, root)]
    return "\n\n".join(p.rstrip("\n") for p in parts) + "\n"
