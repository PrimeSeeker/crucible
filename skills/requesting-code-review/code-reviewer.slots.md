# Slot card — branch-reviewer

## Slots

- [WORKTREE_PATH]: the absolute path to the worktree holding the reviewed branch.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [MANDATE_REMINDER]: one line restating this review's binding output: the goal check, full-scope findings with staked severity, evidence and location, questions, the ledger triage with a ruling per lead and a merge verdict, in this pass's report file, replying with the merge verdict and its path; in standalone mode, the report as the final message.
- [SPEC_POINTER]: the spec path at its pinned revision, as the plan's header carries it ("none" where the branch has no spec), never a copied block. On the very-small lane, the lane note at its pinned revision.
- [UMBRELLAS]: where the spec's preamble carries an `Umbrella:` line (on the very-small lane, the note's), the umbrella it names and each one up the chain, by path; else "none".
- [REQUEST_FILE]: the workspace's `request.md`, absolute; "none" if absent, standalone mode included.
- [DESCRIPTION]: a brief summary of what was built.
- [REQUIREMENTS]: what it should do — plan file path, task text, or requirements; on the very-small lane, the lane note at its pinned revision.
- [LEDGER_MINORS]: the SDD ledger's `## Deferred minors`, verbatim with their sources: execution's minors, the `deferred-minor` entries (source `Spec` or `Plan`) and the leads, never its `## Questions`; "none" in standalone mode.
- [RULINGS]: the adjudication rulings from execution and the branch review's own so far, verbatim; on the very-small lane, followed by the ledger's `Departure:` lines, verbatim; "none" in standalone mode.
- [FIRST_REVIEW_TASKS]: each task whose latest `Task <N>` line under `## Progress` is `Task <N>: complete (commits <base7>..<head7>, branch review only)`, with that range; its latest report, `sdd/reports/task-<N>-report.md` or its `-x<X>` form; the brainstorm decision record where its plan section names it; and its range's amendment commits (`skills/redteaming/references/flip-paths.md`, step 3), or "no amendment commits"; else "none".
- [REPORT_FILE]: this pass's output, in the feature workspace: `sdd/branch-review/pass-<k>.md` for full-scope pass <k>. A replacement seat adds `-r<R>` before `.md`. "none" in standalone mode.
- [BASE_SHA]: the merge base, never `HEAD~1`.
- [HEAD_SHA]: the ending commit.

## Selectors

- lane: very-small | off
  - very-small: the lane text under Binding Content; set on the very-small lane
  - off: none; any other branch, standalone mode included

## Dispatch

- Operation: a fresh-seat dispatch of instrument `branch-reviewer`, this card filled (`skills/subagent-driven-development/references/dispatch-composition.md` § Filling a card).
- Description: `Whole-branch review`.
- Model: the default role, this seat's floor, or the alternate role where one of its triggers selects this seat.
