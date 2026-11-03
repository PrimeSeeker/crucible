# Slot card — branch-reviewer

## Slots

- [WORKTREE_PATH]: the reviewed branch's worktree, absolute.
- [PLUGIN_ROOT]: the plugin root you read this card from, absolute.
- [MANDATE_REMINDER]: one line restating the review's binding output: the goal check; full-scope findings with staked severity, evidence and location; questions; the ledger triage with a ruling per lead; a merge verdict; all in the report file, then a reply of the verdict and the file's path; in standalone mode, the report as the final message.
- [SPEC_POINTER]: the spec path at its pinned revision, as the plan's header carries it, or "none" without a spec; on the very-small lane, the lane note at its pinned revision.
- [UMBRELLAS]: per the dispatch composition's item 2; else "none".
- [REQUEST_FILE]: the workspace's `request.md`, absolute; "none" if absent, standalone mode included.
- [DESCRIPTION]: what was built, briefly.
- [REQUIREMENTS]: what it should do: the plan's path, task text or requirements; on the very-small lane, the lane note at its pinned revision.
- [LEDGER_MINORS]: the ledger's `## Deferred minors` verbatim, its leads included, never its `## Questions`; "none" in standalone mode.
- [RULINGS]: execution's adjudication rulings and the branch review's own so far, then, on the very-small lane, the ledger's `Departure:` lines, all verbatim; "none" in standalone mode.
- [FIRST_REVIEW_TASKS]: each task whose latest `Task <N>` line under `## Progress` is `Task <N>: complete (commits <base7>..<head7>, branch review only)`, with that range; its latest report, `sdd/reports/task-<N>-report.md`; the brainstorm decision record its plan section names, if any; and its range's amendment commits (`skills/redteaming/references/flip-paths.md`, step 3) or "no amendment commits". No such task: "none".
- [REPORT_FILE]: in the feature workspace, `sdd/branch-review/pass-<k>.md` for full-scope pass <k>; "none" in standalone mode.
- [SCRATCH_DIR]: the seat's scratch directory, absolute.
- [BASE_SHA]: the merge base, never `HEAD~1`.
- [HEAD_SHA]: the ending commit.

## Selectors

- lane: very-small | off
  - very-small: the lane passage under Binding Content; on the very-small lane
  - off: none; any other branch, standalone mode included

## Dispatch

- Description: `Whole-branch review`.
- Model: never below the default role.
