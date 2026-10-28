# What reviews catch, and the implementer's part in it

## Observation

- On crucible's own umbrella-specs feature (2026-10-28, five tasks, all
  prose), the issues that mattered surfaced in the implementers'
  `DONE_WITH_CONCERNS` reports: a duplicated rule, ceremony for an
  approval-only document, a rule two phases could never reach, and
  wrong Basis tags in a decision record. The five task reviewers
  approved every task and raised only minors; the branch review
  confirmed the unreachable rule as its one MAJOR.
- The spec campaign and the plan phase missed that rule. It was
  triggered "at each task or round boundary", and two phases (the very-small
  lane and every route's branch review) have none. The brainstorm's
  consumer sweep finds existing sites that state a rule; it does not
  ask whether every flow reaches a rule's trigger.
- The task that wrote the decision record could not see the brainstorm
  decision record, so it tagged every position "judgment, accepted by
  the maintainer", including positions that were the maintainer's own.
- The maintainer's view (2026-10-28): work on what the campaign
  catches, and probably empower implementers further.

## Follow-up

- **A trace check for trigger-shaped rules.** Where a spec adds a rule
  tied to a trigger ("at each X, do Y"), one seat traces every route
  and phase that must reach it and confirms each has an X. Conditional:
  a change adding no such rule needs no trace. In ordinary code the
  same shape is an invariant every write path must keep, a check every
  endpoint must run, or a cleanup every exit path must hit.
- **Per-task review as a plan choice** (maintainer agreed): for tasks
  that are sequential on shared files and low in mechanism, such as
  prose, the plan may route review to the branch review alone, keeping
  the implementer's concerns as the per-task net.
- **Decision-record tasks take the brainstorm decision record** as an
  input (maintainer agreed), so each Basis tag is attributed when
  written.
- **Implementers' standing.** Decide what more an implementer may do
  with a concern beyond reporting it: for example, raise it as a
  finding the task review must rule on, or propose a fix to a site
  outside its task.
