# Slot card — blind-verifier

## Slots

- {worktree-path}: the verifier's absolute worktree path.
- {artifact-path}: the artifact the fix wave was applied to.
- {pre-fix-revision}: its revision before the wave.
- {post-fix-revision}: its revision after the wave.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/verifier.md`.
- {scratch-dir}: the seat's absolute scratch directory.
- {fix-list}: the round record's fix list, verbatim.
- {diff}: the artifact's diff across the wave; in the plan phase the plan's alone, never a contained amendment's spec commit.

## Selectors

none

## Dispatch

- Blind by design: add no input beyond these slots — never the rationale, the seat reports or the round readout. The fix list and the diff are its whole evidence, with the tracked files a delta claim names as that claim's.
- Model: the bounded role, never lower.
