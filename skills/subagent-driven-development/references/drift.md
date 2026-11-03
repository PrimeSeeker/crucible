### Drift found after the fact

Work found off-plan without a logged decision — by the task review's deviation audit, by you, or by a branch-review pass flagging it DRIFT in a completed task — within the **materiality bound**, an undisclosed deviation from *binding* content or one with cross-task blast radius, is a decision ask to the operator:

- **Revert** the task, with the later tasks the ask names as building on it, by `git revert` of each one's range, never a reset, and run them again from step 1 of the task loop. Append `Task <N>: reverted — <the ruling>` for each, which reopens it. A task run again takes `-x<X>` after `task-<N>` in every report path, `<X>` one more than its `reverted` lines, so its reports and wave numbers start fresh. Reverted at the branch review, return the branch to `crucible:requesting-code-review` once the re-run tasks complete; it resumes with a full-scope pass.
- **Repair** it: in its own fix loop while the task is open; for a completed task, recorded under `## Adjudication rulings`, which the resume rule does not read, and riding a branch-review fix wave as a ruling change counted against its cap, as `crucible:requesting-code-review` § The branch-review loop states.

Below the bound, undisclosed advisory choices (implementers do not log every micro-choice) and *disclosed-but-unjustified* Decision Log entries enter the fix loop. On the very-small lane, drift goes as `skills/subagent-driven-development/references/very-small-lane.md` states.
