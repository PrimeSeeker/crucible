# A bad assertion can leave only with its whole test

## Observation

- A deleted test or parametrized case passes review when the Decision Log
  names one justification, a quoted `writing-good-tests.md` warning sign
  among them. A weakened test (more permissive, or an assertion removed)
  is a scope finding whatever the log says
  (`skills/subagent-driven-development/implementer-prompt.md` § Tests:
  Test-First, Evidence Before Done; `task-reviewer-prompt.md` Verdict 2;
  the re-review and branch-review checks).
- `writing-good-tests.md` § Principle 2 tells an author who finds an
  assertion on a mock to "unmock it or delete the assertion". Deleting
  that one assertion is a weakening, so the guide's own remedy fails
  review; deleting the whole test, good assertions included, passes with
  the warning sign "An assertion checks a `*-mock` test ID, or fails if
  you remove the mock" quoted.

## Follow-up

Decide whether a removed assertion takes the deleted-test justification
route (at least the warning-sign justification), or whether the guide's
remedy changes instead. The first changes a binding rule (only deleted
tests take a justification; a weakened one is a scope finding), so it is a
feature of its own, not a fix.
