# Slot card — terminal-pass

## Slots

- {worktree-path}: the absolute worktree path the pass works from.
- {plugin-root}: the absolute path of crucible's plugin root, the one you read this card from.
- {artifact-path}: `spec` phase, the spec; `plan` phase, the amended plan.
- {revision}: the artifact's revision.
- {phase-dir}: `{workspace-path}/campaigns/spec/` or `{workspace-path}/campaigns/plan/`, by `phase`.
- {binding-artifact-path}: `spec` phase, the spec itself; `plan` phase, the spec the plan's header names; never `none`.
- {binding-revision}: that artifact's revision.
- {umbrella-paths}: where the binding artifact's preamble carries an `Umbrella:` line, the umbrella it names and each one up the chain, by path; else `none`.
- {report-path}: `spec` phase, `{workspace-path}/campaigns/spec/terminal-pass/pass.md`; `plan` phase, `{workspace-path}/campaigns/plan/round-01/terminal-pass.md`; a second read, `second-read.md` beside the first report, which it never overwrites.

## Selectors

- phase: spec | plan
  - spec: the spec campaign's opening
  - plan: the plan phase's opening
- fix-wave: yes | no
  - yes: mandate 1 as a full-scope re-read; set when the final round produced a fix wave
  - no: mandate 1 as a confirmation read; set when it produced none
- follow-up: second-read | off
  - second-read: the second-read passage; spec, dispatched after the pass's one further fix wave; plan, stated with the report path in the message resuming the pass after its sanctioned repair
  - off: none; the pass's first dispatch

## Dispatch

- Operation: a fresh-seat dispatch of instrument `terminal-pass` with this card filled — each slot's rule replaced by its value, each selector line cut to its one value and its sub-bullets dropped — through your adapter's instrument-dispatch operation.
- Model: Dispatch it with an explicit model, and an effort level only on the operator's request — see SKILL.md § Panels. The default role, or the alternate role where one of its triggers selects this seat.
