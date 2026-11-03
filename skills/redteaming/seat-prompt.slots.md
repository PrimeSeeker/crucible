# Slot card — redteam-seat

## Slots

- {worktree-path}: the absolute worktree path the seat works from.
- {artifact-kind}: `spec` or `plan`; a folded lane's combined spec+plan document is `spec`.
- {artifact-path}: the artifact under review.
- {revision}: its frozen revision, the same for every seat of the round.
- {supporting-inputs}: verification-only sources (for a plan, the spec it implements; referenced code paths; for the plan phase's mechanical pre-pass, also the repository's tracked text, for its set census), or `none`.
- {binding-artifact-path}: the artifact carrying what binds; for a plan, the spec its header names.
- {binding-revision}: that artifact's revision.
- {request-path}: `{workspace-path}/request.md`, the request; `none` where the workspace holds none.
- {umbrella-paths}: per the dispatch composition's item 2; else `none`.
- {mandate-reminder}: one line naming the seat's binding output: a full-scope read of the artifact, findings with staked severity and evidence, written to the report path; for the plan phase's mechanical pre-pass, its liveness, ownership-closure and overlap arithmetic and its set census, run rather than read.
- {lens}: a lens from the § Panels roster, or one you add for what this artifact makes load-bearing, and its one-line description; for the right-sizing seat and the plan phase's mechanical pre-pass, then their lens text from § Panels, verbatim.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/seat-{id}.md`; the plan phase's mechanical pre-pass is `seat-p0.md`.
- {scratch-dir}: the seat's scratch directory, absolute.

## Selectors

- goal-check: on | off
  - on: the goal check and its `## Goal check` report item; set for each seat of a spec campaign's round 1
  - off: none

## Dispatch

none
