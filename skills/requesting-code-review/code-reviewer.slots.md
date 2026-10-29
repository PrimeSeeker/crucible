# Slot card — branch-reviewer

## Slots

- [WORKTREE_PATH]: the absolute path to the worktree holding the reviewed branch.
- [PLUGIN_ROOT]: the absolute path of crucible's plugin root, the one you read this card from.
- [MANDATE_REMINDER]: one line restating this review's binding output: the goal check, full-scope findings with staked severity, evidence and location, questions, the ledger triage with a ruling per lead, a merge verdict and the task lines owed, in this pass's report file, replying with the merge verdict and its path; in standalone mode, the report as the final message.
- [SPEC_POINTER]: the spec path at its pinned revision, the pointer the plan's header carries ("none" where the branch has no spec) — a pointer, never a copied block. On the very-small lane, the lane note at its pinned revision.
- [UMBRELLAS]: where the spec's preamble carries an `Umbrella:` line (on the very-small lane, the note's), the umbrella it names and each one up the chain, by path; else "none".
- [DESCRIPTION]: a brief summary of what was built.
- [REQUIREMENTS]: what it should do — plan file path, task text, or requirements; on the very-small lane, the lane note at its pinned revision.
- [LEDGER_MINORS]: the SDD ledger's deferred minors, leads included, **and the plan's unresolved routed deferred items**, verbatim, each labelled with its owning task; "none" in standalone mode.
- [RULINGS]: the adjudication rulings from execution and the branch review's own so far, verbatim; on the very-small lane, followed by the ledger's `Departure:` lines, verbatim; "none" in standalone mode.
- [BRANCH_ONLY_TASKS]: the tasks this pass owes a line (`crucible:requesting-code-review` § Tasks completed branch review only), each with its range, its latest attempt's report, the brainstorm decision record where its plan section names it, and its range's amendment commits; else "none".
- [REPORT_FILE]: this pass's output, in the feature workspace: `sdd/branch-review/pass-<k>.md` for full-scope pass <k>. A replacement seat adds `-r<R>` before `.md`. "none" in standalone mode, where the report is the final message.
- [BASE_SHA]: the starting commit — the merge base, never `HEAD~1`.
- [HEAD_SHA]: the ending commit.

## Selectors

- lane: very-small | off
  - very-small: the lane text under Binding Content, which asks for the `### Lane Fit` section; set on the very-small lane
  - off: none; any other branch, standalone mode included

## Dispatch

- Operation: a fresh-seat dispatch of instrument `branch-reviewer` with this card filled — each slot's rule replaced by its value, each selector line cut to its one value and its sub-bullets dropped — through your adapter's instrument-dispatch operation.
- Description: `Whole-branch review`.
- Model: REQUIRED: the default role, this seat's floor, or the alternate role where one of its triggers selects this seat (`skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort).
- Effort: per that section.
