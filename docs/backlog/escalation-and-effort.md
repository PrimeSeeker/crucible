# Escalation and effort: no stuck trigger, and an unmeasured unset effort

## Observation

- Nothing escalates a stuck seat to the alternate role. Its three
  triggers are round 1's swap, a weak spot the host map lists and the
  operator's request
  (`skills/subagent-driven-development/references/dispatch-composition.md`
  § Models and effort). SDD's fix loop resumes the task's implementer for
  three waves at most, then puts the findings still open to the operator
  (SDD § The Task Loop, step 5), and a BLOCKED reasoning problem at the
  default role goes to the operator. The maintainer: "Late waves are
  generally not stuck, just slowly mining the residual issues. We'll
  probably introduce a stuck trigger later."
- Effort is the operator's: no flow sets or raises a dispatch's reasoning
  effort on either host. The rule is held lightly (the maintainer: "that
  was an expression of uncertainty"), so a measurement can flip it.
- What a Claude Code seat runs at with effort unset is unmeasured. The
  host's agent-dispatch tool describes a non-fork agent as running at its
  definition's effort or "its usual effort", not the session's, and no
  generated agent under `agents/` sets one, so crucible's seats likely run
  below a session set higher (an inference from the tool's description,
  UNVERIFIED).
- The Codex counterpart is measured, on codex-cli 0.162.1: a seat whose
  dispatch names its model and omits effort runs at
  `[agents] default_subagent_reasoning_effort` from the Codex config, else
  at its model's default, never at the controller's effort; a seat with
  model and effort both omitted runs on the parent's model and effort.
  `docs/codex.md` § Install sets the key.

## Follow-up

- Measure the effort a Claude Code seat runs at with effort unset, under a
  session set higher, from a host record rather than the seat's own
  report.
- From the records of late fix waves and late campaign rounds, decide
  whether a stuck trigger is wanted and how stuck differs from mining
  residual issues.
- If the measurement shows seats running below the session, decide
  whether effort stays the operator's or a rule sets one. A change to the
  operator-only rule, or a new trigger for the alternate role, is a
  decision record of its own.
