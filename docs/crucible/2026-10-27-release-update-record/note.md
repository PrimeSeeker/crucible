Lane: very-small (operator-confirmed 2026-10-27)

# Record the cross-release update

## Intent

Record that the update from one release to the next ran on both hosts,
so no doc says it is still waiting.

## Change list

- `docs/dual-runtime.md` § Upgrades and rollback: the update commands ran
  from 0.2.0 to 0.3.0 on both hosts (Claude Code 2.1.311, codex-cli
  0.164.0), and each fetched the new copy.
- `docs/decisions/releases.md`: "an update across releases waits for the
  second release" replaced by the result, with a Changes line.
- `docs/backlog/release-metadata-and-versioning.md`: the update part and
  its follow-up removed. It keeps: whether Codex skips the fetch without
  a version change, the version in two places, record version markers,
  and the trademark check.

## Acceptance

1. `grep -rniE "second release|update across a release" docs` finds
   nothing outside this feature's folder (3 lines before).
2. `python -m pytest tests/` passes.

## Out of scope

- Any skill text, and the backlog item's other questions.
- The annotated-versus-lightweight tag difference.
