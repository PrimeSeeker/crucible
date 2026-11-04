# Slot card — blind-verifier

## Slots

- {worktree-path}: the verifier's absolute worktree path.
- {artifact-path}: the artifact the fix wave was applied to.
- {pre-fix-revision}: its revision before the wave.
- {post-fix-revision}: its revision after the wave.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/verifier.md`; the spec terminal pass's follow-up wave, `{workspace-path}/campaigns/spec/terminal-pass/verifier.md`; a re-check, `verifier-recheck.md` beside the wave's; then the line `Write this file with your <tool> tool before replying.`, `<tool>` being the tool that creates a file in your host map's **Edit** entry.
- {scratch-dir}: the seat's absolute scratch directory.
- {fix-list}: the round record's fix list, verbatim.
- {diff}: the artifact's diff across the wave; in the plan phase the plan's alone, never a contained amendment's spec commit.

## Selectors

none

## Dispatch

- Blind by design: add no input beyond these slots — never the rationale, the seat reports or the round readout. The fix list and the diff are its whole evidence, with the tracked files a delta claim names as that claim's.
- A re-check is this card filled for the repairs alone, on a fresh seat: the fix list one item per repair, stating what the edit lands; the revisions and the diff across the repairs.
- Model: the bounded role, never lower.
