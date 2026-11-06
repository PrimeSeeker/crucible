# Blind verifiers return reports as text: the latest fix is untested on them

## Observation

- On four runs of Claude Code, blind verifiers returned without writing their
  report file: once in the first run; both verifiers in the second and two of
  three in the third, each writing it when resumed once; two in the fourth,
  saying no write tool was available, each saved by the controller under its
  mark. The pattern matches the host's prose advice that subagents return
  findings as text, which `skills/using-crucible/references/claude-code-dispatch.md`
  records.
- Since 2026-11-04 the verifier's and the re-reviewer's cards have the
  controller name the host's file-writing tool in the report slot, with no
  "if you have it". No verifier has run under it. The re-reviewer, which
  missed on three of those runs, wrote 23 of 23 without a resume through 2026-11-05,
  all on the very-small lane (`docs/decisions/instruments.md`, Rejected,
  § Seat-facing wording). 21 of those ran on the bounded role, the
  verifier's, so the role alone does not produce a miss. The next, also on
  the bounded role (2026-11-06), ended its run without the Write call and
  wrote on one resume. Later ones that day wrote without one, but their
  dispatches reminded them to make the call, so they are no clean sample.
- The check on an appended report asks that it hold the seat's section
  (`skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5), and nothing marks whose section is whose. A seat re-dispatched
  to the same report whose own write failed passes on the earlier attempt's
  section. No run on record has hit it.

## Follow-up

- On the next spec campaigns, count verifier report-file misses, and
  re-reviewer ones on the first full routes.
- If they persist, carry the report path too as an absolute path in the slot
  card, as the scratch directory now is.
