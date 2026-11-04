### Drift found after the fact

Drift is work found off-plan without a logged decision — by the task review's deviation audit, by you, or by a branch-review pass flagging it DRIFT in a completed task. Within the **materiality bound** (an undisclosed deviation from *binding* content, or one with cross-task blast radius) it is a decision ask:

- **Revert** the task and the later tasks the ask names as building on it, by `git revert` of each one's range, never a reset. Append `Task <N>: reverted — <the ruling>` for each, which reopens it, and run them again from step 1 of the task loop. A re-run task takes `-x<X>` after `task-<N>` in every report path, `<X>` one more than its `reverted` and `plan changed` lines, so its reports and wave numbers start fresh. Reverted at the branch review, return to `crucible:requesting-code-review` once the re-run tasks complete, resuming with a full-scope pass that re-grades the rest of the flagging pass's findings.
- **Repair** an open task in its own fix loop; a completed one by a ruling under `## Adjudication rulings` that rides a branch-review fix wave as a ruling change, counted against the cap (`crucible:requesting-code-review` § The branch-review loop).

Below the bound, undisclosed advisory choices and *disclosed-but-unjustified* Decision Log entries enter the fix loop. On the very-small lane, drift goes as `skills/subagent-driven-development/references/very-small-lane.md` states.
