# Adopt what the v7.0.1 upstream review took

## Observation

The review of superpowers v6.2.0 → v7.0.1 adopted these improvements, in
crucible's form, on the maintainer's rulings of 2026-10-27; each row's
upstream source and reason are in
`docs/crucible/2026-10-27-upstream-review/dispositions.md` § Improvements.
None is made yet.

- The branch and task reviewers: a spec's silence is not permission; a
  failure on an input the spec implies is graded by its effect on a
  reasonable user.
- writing-plans: a task's edge and error scenarios name the inputs the
  spec implies but never names.
- The implementer's report names every failing test, its own or not.
- SDD's close readout lists every ruling the controller made, pre-flight
  and plan patches included.
- The redteam seats' mandate: a consequential choice a spec takes for
  granted with no Decision entry (platform, language, the form of the
  deliverable) is a finding.
- brainstorming: a throwaway probe in scratch that answers a question is
  context gathering, never committed.
- dispatching-parallel-agents: check each agent's diff, not its summary.
- writing-skills' Portability bullet: run bundled scripts through their
  interpreter.
- The task reviewer and re-reviewer re-read evidence that looks truncated
  before reporting it missing.

## Follow-up

One very-small lane, then a release with the review's defect fixes.
