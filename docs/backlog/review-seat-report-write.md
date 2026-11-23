# Seats on the bounded role end without writing their report file

## Observation

- On four runs of Claude Code before 2026-11-04, blind verifiers returned
  without writing their report file, two saying no write tool was
  available. The pattern matches the host's prose advice that subagents
  return findings as text, which
  `skills/using-crucible/references/claude-code-dispatch.md` records.
- Since 2026-11-04 the verifier's and the re-reviewer's cards have the
  controller name the host's file-writing tool in the report slot
  (`docs/decisions/instruments.md`, Rejected, § Seat-facing wording). On one
  code project's runs under it, on crucible 0.33.1 (the re-audit of
  2026-11-23), 4 of 72 blind verifiers missed the owed file at first: two
  wrote it under the workspace's `scratch/` instead and two returned the
  report as text. One controller then recorded a verifier report file that
  was never written, and nothing later noticed.
- In the same runs 3 of 56 re-reviewers and 2 of 10 implementers on the
  bounded role ended without the write, against 0 of 37 re-reviewers on the
  default role; no seat on another role missed except after an interrupted
  run or a failed start. On crucible's own runs through 2026-11-05, 23 of 23
  re-reviewers wrote without a resume, 21 of them on the bounded role, so
  the role alone does not produce a miss. All five ended on the host's hand-back call carrying the report. Two
  said they had no write tool, which their recorded tool lists contradict,
  and their controllers saved the reports without checking; one cited a
  rule against report files that no crucible template states. Every seat
  also receives the host's reminder that its final report goes through that
  call, against the template's short reply.
- The check on an appended report asks that it hold the seat's section
  (`skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5), and nothing marks whose section is whose. A seat re-dispatched
  to the same report whose own write failed passes on the earlier attempt's
  section. No run on record has hit it.
- Since 2026-11-22 every template's § Report file gives the reason the
  file is the deliverable (`docs/decisions/instruments.md` § Why › Report
  files). No run counted above had it. Whether a reason reduces seats
  ending without the write is untested: nine probe seats on small tasks all
  wrote, with or without it.

## Follow-up

- Count report-file misses on runs after 2026-11-22, by role. If they
  persist, carry the report path too as an absolute path in the slot card,
  as the scratch directory now is.
