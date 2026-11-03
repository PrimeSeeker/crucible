# Test justifications: two follow-ups

## Observation

- Since 2026-11-04 a deleted test, case or assertion, and any other
  change making a test more permissive, is a finding unless one of four
  justifications holds for what was deleted or loosened
  (`skills/subagent-driven-development/references/seat-rules.md` § Tests
  in review; `docs/decisions/test-rules.md`).
- The third justification reads "the change fulfils a requirement or
  review finding". Beside the first, "the change removed its subject",
  where "the change" is the work under review, it can be read as the
  work fulfilling a requirement, which every task's work does; only the
  list's lead-in, "for what was deleted or loosened", ties it to the
  removed or loosened part. Before 2026-11-04 it read "the deletion
  fulfils".
- On the very-small lane the controller writes its fix waves' reports
  itself, answering findings as the implementer template's § After
  Review Findings asks
  (`skills/subagent-driven-development/references/very-small-lane.md`).
  The duty to log a justification for each deletion or loosening sits in
  that template's test section, which the lane's controller is not
  pointed at, while the re-reviewer counts a justification only where
  the fix report names it.

## Follow-up

- Write "the deletion or loosening fulfils a requirement or review
  finding", in the seat rule and the record.
- Point the very-small lane's inline fix waves at the duty to log each
  deletion's or loosening's justification.
