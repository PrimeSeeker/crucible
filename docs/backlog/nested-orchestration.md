# A controller one subagent down

## Observation

- Claude Code lets a subagent dispatch subagents of its own, up to three
  layers below the main conversation by default since v2.1.219
  (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` changes it; Claude Code's
  subagent docs, read 2026-10-27).
- Upstream (superpowers v6.4.1) offers an opt-in: one orchestrator
  subagent on a mid-tier model runs SDD end to end, since the controller,
  on the session's strongest model and reading every report, is the
  costliest seat. It reports its rulings when it finishes.
- A crucible controller puts decision asks to the operator mid-run (SDD's
  breaker, a fourth branch-review wave, a change to binding content the
  containment test does not find contained); a nested one cannot reach
  the operator until it returns. The maintainer, 2026-10-27: "the barrier is not
  insurmountable, but I doubt the size of the cost win".
- Crucible's seat agents carry no tool limits, so on Claude Code a seat
  can now nest dispatches; the seat templates ban it in prose. The
  maintainer declined a tool-level ban, doubting it would be used
  unnecessarily.

## Follow-up

Measure the controller's share of a run's cost on both hosts. If it is
large, design how a nested controller hands a decision ask back up and
resumes.
