# Slot card — terminal-pass

## Slots

- {worktree-path}: the pass's absolute worktree path.
- {artifact-path}: the spec; `plan` phase, the amended plan.
- {revision}: its revision.
- {phase-dir}: `{workspace-path}/campaigns/{phase}/`.
- {binding-artifact-path}: the spec; `plan` phase, the spec the plan's header names; never `none`.
- {binding-revision}: that artifact's revision.
- {decision-record-path}: `{workspace-path}/brainstorm-decisions.md`; `plan` phase, `none`.
- {umbrella-paths}: per the dispatch composition's item 2; else `none`.
- {re-read}: `due` where the pass's further wave or repair landed after its first report, else `not due`; a first dispatch, `none`.
- {report-path}: under `{phase-dir}`, `terminal-pass/pass.md`; `plan` phase, `round-01/terminal-pass.md`; a second read, `second-read.md` beside the first report, which it never overwrites.
- {scratch-dir}: the seat's absolute scratch directory.

## Selectors

- phase: spec | plan
  - spec: the spec campaign
  - plan: the plan phase
- fix-wave: yes | no
  - yes: mandate 1 as a full-scope re-read; set when the final round produced a fix wave or `{re-read}` is `due`
  - no: mandate 1 as a confirmation read; set otherwise
- follow-up: second-read | off
  - second-read: the pass's one second read; spec, a fresh dispatch; plan, stated with the report path and `{re-read}` in the message resuming the pass
  - off: none; the first dispatch

## Dispatch

none
