# Slot card — blind-verifier

## Slots

- {worktree-path}: the absolute worktree path the verifier works from.
- {artifact-path}: the artifact the fix wave was applied to.
- {pre-fix-revision}: its revision before the wave.
- {post-fix-revision}: its revision after the wave.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/verifier.md`.
- {fix-list}: evidence input — the round record's fix list, verbatim: enumerated items, each naming the finding id(s) it resolves.
- {diff}: evidence input — the diff of the artifact across the wave.

## Selectors

none

## Dispatch

- Operation: a fresh-seat dispatch of instrument `blind-verifier` with this card filled — each slot's rule replaced by its value — through your adapter's instrument-dispatch operation.
- Blind by design: add no input beyond these slots — never the rationale, the seat reports or the round readout. The fix list and the diff are its whole evidence, with the tracked files a delta claim names as that claim's; the other slots only locate.
- Model: Dispatch it with an explicit model, and an effort level only on the operator's request — see SKILL.md § Panels. The bounded role, never lower: the one redteaming dispatch below the default role.
