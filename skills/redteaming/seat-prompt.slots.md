# Slot card — redteam-seat

## Slots

- {worktree-path}: the seat's worktree, absolute.
- {artifact-kind}: `spec` or `plan`; `spec` for a folded lane's combined spec+plan.
- {artifact-path}: the artifact under review.
- {revision}: its frozen revision, the same for the whole round.
- {supporting-inputs}: verification-only sources (for a plan, the spec it implements; referenced code paths; for the plan phase's pre-pass, also the repository's tracked text, for its set census), or `none`.
- {binding-artifact-path}: the artifact carrying what binds; for a plan, the spec its header names.
- {binding-revision}: that artifact's revision.
- {request-path}: `{workspace-path}/request.md`, or `none` if absent.
- {umbrella-paths}: per the dispatch composition's item 2; else `none`.
- {mandate-reminder}: one line naming the seat's binding output: a full-scope read, findings with staked severity and evidence, at the report path; for the plan phase's pre-pass, its liveness, ownership-closure and overlap arithmetic and set census, run, not read.
- {lens}: a lens from § Panels, or one you add for what this artifact makes load-bearing, and its one-line description; for the right-sizing seat and the plan phase's pre-pass, then their lens text from § Panels, verbatim.
- {report-path}: `{workspace-path}/campaigns/{phase}/round-{NN}/seat-{id}.md`; the plan phase's pre-pass is `seat-p0.md`.
- {scratch-dir}: the seat's scratch directory, absolute.

## Selectors

- goal-check: on | off
  - on: the goal check and its `## Goal check` report item; set for each seat of a spec campaign's round 1, or of the next round where a degraded round 1 hands it on (`skills/redteaming/references/panels.md`)
  - off: none

## Dispatch

none
