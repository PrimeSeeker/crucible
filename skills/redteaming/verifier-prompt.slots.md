# Slot card — blind-verifier

## Slots

- {worktree-path}: the absolute worktree path the verifier works from.
- {artifact-path}: the artifact the fix wave was applied to.
- {pre-fix-revision}: its revision before the wave.
- {post-fix-revision}: its revision after the wave.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/verifier.md`.
- {scratch-dir}: the seat's scratch directory, absolute.
- {fix-list}: evidence input — the round record's fix list, verbatim: enumerated items, each naming the finding or question id(s) it resolves.
- {diff}: evidence input — the diff of the artifact across the wave; in the plan phase the plan's diff alone, never a contained amendment's spec commit.

## Selectors

none

## Dispatch

- Operation: a fresh-seat dispatch of instrument `blind-verifier`, this card filled (`skills/subagent-driven-development/references/dispatch-composition.md` § Filling a card).
- Blind by design: add no input beyond these slots — never the rationale, the seat reports or the round readout. The fix list and the diff are its whole evidence, with the tracked files a delta claim names as that claim's; the other slots only locate.
- Model: the bounded role, never lower: the one redteaming dispatch below the default role.
