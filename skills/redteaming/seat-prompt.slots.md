# Slot card — redteam-seat

## Slots

- {worktree-path}: the absolute worktree path the seat works from.
- {plugin-root}: the absolute path of crucible's plugin root, the one you read this card from.
- {artifact-kind}: `spec` or `plan`; a folded lane's combined spec+plan document is `spec`.
- {artifact-path}: the artifact under review.
- {revision}: its frozen revision, the same for every seat of the round.
- {supporting-inputs}: verification-only sources (for a plan, the spec it implements; referenced code paths), or `none`.
- {binding-artifact-path}: the artifact carrying what binds; for a plan, the spec its header names.
- {binding-revision}: that artifact's revision.
- {umbrella-paths}: where the binding artifact's preamble carries an `Umbrella:` line, the umbrella it names and each one up the chain, by path; else `none`.
- {mandate-reminder}: one line naming the seat's binding output: a full-scope read of the artifact, findings with staked severity and evidence, written to the report path; for the plan phase's mechanical pre-pass, its liveness, ownership-closure and overlap arithmetic, run rather than read.
- {lens}: a lens from the § Panels roster, or one you add for what this artifact makes load-bearing, and its one-line description.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/seat-{id}.md`; the plan phase's mechanical pre-pass is `seat-p0.md`.

## Selectors

- right-sizing: on | off
  - on: the over-subtraction guard and the `## Right-sized — do not cut` report item; set for a seat carrying the right-sizing lens
  - off: none
- worksheet: ordered-first | pre-pass | off
  - ordered-first: the ordered-first hunt and its `## Worksheet` report item; set for the greenfield round-1 seat (§ Round 0)
  - pre-pass: the pre-pass `## Worksheet` report item; set for the plan phase's mechanical pre-pass
  - off: none

## Dispatch

- Operation: a fresh-seat dispatch of instrument `redteam-seat` with this card filled — each slot's rule replaced by its value, each selector line cut to its one value and its sub-bullets dropped — through your adapter's instrument-dispatch operation.
- Model: Dispatch it with an explicit model, and an effort level only on the operator's request — see SKILL.md § Panels. The default role, or the alternate role where round 1's swap or another of its triggers selects this seat.
