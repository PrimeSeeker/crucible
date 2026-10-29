# Test rules

## Decision

**Two kinds of acceptance check.** Each acceptance criterion maps to a
standing test, kept in the suite where a plausible later change could
break the outcome, or to a one-time check, run once by the implementer
and recorded as its command and quoted output, which review reads rather
than re-runs; or it states why neither applies. A one-time check of a
state the change brings about is also run before the change, where it
must fail. An absence criterion is one-time unless the plan names the
later change that could undo it, and outcomes seen on one run are one
test's assertions (`crucible:writing-plans § Acceptance maps to checks`).

**Test-first.** The implementer writes the failing test, watches it fail
for the reason it expects, then implements. Code written before its test
is redone test-first or logged as an exception: no test seam, generated
code, prose-only work, a removal. A removal's failing step is the removed
path's own tests failing or deleted with it, never a new test that the
thing is absent. The task reviewer's deviation audit checks RED output
before GREEN, or the logged exception, and is the one seat that checks
it, but for a task completed branch review only, where the controller's
gate checks the evidence is in the report and the branch reviewer's
deviation audit judges it (`docs/decisions/task-loop.md`;
`skills/subagent-driven-development/implementer-prompt.md` § Tests:
Test-First, Evidence Before Done). Outside SDD, systematic-debugging
writes the failing test before the fix and says why where no test or
script can reproduce the bug.

**Weakened and deleted tests.** A weakened test, made more permissive or
with an assertion removed, is always a finding, at the task review, the
re-review and the branch review. A deleted test, or a deleted case of a
parametrized one, is a finding unless one justification holds: the
subject the change removed; a remaining test covering the behavior; the
requirement or review finding the deletion fulfils; or a warning sign from
`skills/subagent-driven-development/writing-good-tests.md` that the test
shows. The task reviewer checks the Decision Log's justification against
the code, the re-reviewer the fix report's, and the branch reviewer judges
from the code and the requirements, and checks the Decision Log's
justification itself for a task completed branch review only
(`skills/subagent-driven-development/task-reviewer-prompt.md` § Verdict 2:
Scope; `skills/subagent-driven-development/re-review-prompt.md` § Scope;
`skills/requesting-code-review/code-reviewer.md` § What to Check).

**Adequacy, and no gate.** New-test adequacy is the task reviewer's own
judgment, and the branch reviewer's for a task completed branch review
only. There is no mutation gate; the test guide's mutation check is
a manual practice
(`skills/subagent-driven-development/writing-good-tests.md` § The
Mutation Check).

**No test locks.** No hook, script or template makes test files
read-only: weakening is detected by the reviewers, not prevented.

## Why

### Two kinds of check, and removals

From crucible's first design, every acceptance criterion mapped to an
executable check or said why not (2026-08-05). A census of another
project's suite (2026-10-15) traced three patterns of tests nobody needed
to three of crucible's rules. Nothing separated a check run once at review
from a test kept forever, so an "X is gone" criterion became a permanent
test, and each acceptance bullet its own test re-running the same setup.
Test-first had no exception for a removal, so the only test that can fail
first, one asserting the thing is absent, was written and kept. And every
deleted test was a scope finding whatever the report said, so an obsolete
test was kept or flipped rather than deleted. The narrowed rules defer to
the test guide, which already counts an assertion that a removed symbol
stays removed as a warning sign and says a test written to satisfy
process costs maintenance forever. A one-time check still leaves its
evidence, in the implementer's report. (Basis: measured; judgment,
accepted by the maintainer.)

### Test-first

Upstream's TDD skill makes test-first an iron law: code written before its
test is deleted, and exceptions need the human partner's permission
(`superpowers/skills/test-driven-development/SKILL.md`). Crucible folded it
into the implementer and task-reviewer templates at its first design
(2026-08-06), with exceptions logged in the Decision Log in place of a
partner's permission. On 2026-10-07 two upstream rules came back in compact
form: watch the test fail for the reason you expect, since a failure from
a typo or an import error proves nothing, and delete or log code written
first; upstream's delete-only form did not, since work with no test seam,
generated code and prose-only work keep the logged exception. The same
day the deviation audit began checking RED before GREEN, which nobody had
checked. Only an implementer's report carries that evidence, so the
check stays with the seat that reads the report: the task reviewer, or,
for a task completed branch review only, the branch reviewer, whose slot
names that report (2026-10-29). Outside SDD, systematic-debugging's skip
narrowed on 2026-10-15 from any stated reason to a bug no test or script
can reproduce, an observable condition. (Basis: external; judgment,
accepted by the maintainer.)

### Weakened and deleted tests

Weakened and deleted tests were scope findings from the first design
(2026-08-05). Making every deletion a finding made keeping an obsolete
test the cheapest compliant move, so on 2026-10-15 a deletion became a
finding only without a justification, the reviewer checking the named
covering test or warning sign against the code. The same day the check
reached the re-reviewer and the branch reviewer: until then only a task's
first review looked for a weakened or deleted test, and a fix wave can
weaken a test to pass, while on the very-small lane the branch review is
the diff's first review. The three reviewers' dispatches carry the plugin
root, so each can read the test guide in a repository other than
crucible's. A weakened test stays a finding even where the
test guide's own remedy, deleting one bad assertion, is the weakening;
that gap is open (`docs/backlog/weakened-test-justification.md`). (Basis:
measured, for the census; judgment, accepted by the maintainer.)

### Adequacy and the mutation gate

The first design made scoped mutation runs the test-adequacy verdict
(2026-08-06). Measured on 2026-08-21: in repositories with no mutation tooling the
mandate produced only per-task waiver boilerplate, about 40 lines in the
surveyed window, and never a run, so mutation became an optional gate a
repository declared. A declared gate ran after the review and could be
waived, so it backed nothing at review time, and on 2026-10-07 adequacy
became the reviewer's own judgment. The optional gates went on
2026-10-12: no gate declaration was ever committed in crucible's history
or in the one other project checked, and a project that wants mutation
testing says so in its instruction files. (Basis: measured; judgment,
accepted by the maintainer.)

### No locks

The maintainer ruled out read-only test files and lockdown hooks
(2026-08-05): too hard a constraint for strong models, and persistent
agents defeat it anyway. Detection over prevention: the first design
named mutation runs and snapshot blessing as the compensating controls,
and of those snapshot blessing remains (`docs/decisions/task-loop.md`),
with the three reviewers' test checks. (Basis: the maintainer's
preference.)

## Rejected

- **Read-only test files or lockdown hooks** (§ Why).
- **A mutation gate**, mandatory or declared per repository (§ Why).
- **An absence test as a removal's failing step** (§ Why).
- **Every deleted test a finding**, whatever its justification (§ Why).

## What a project may change

A project's instruction files outrank the skills
(`crucible:using-crucible § The Rule`): a project that wants mutation
testing, or other test gates, states them there.

## Changes

- 2026-10-29: for a task completed branch review only, the branch
  reviewer takes the task reviewer's test checks, RED before GREEN, a
  deleted test's justification and new-test adequacy, the controller's
  gate first checking the evidence is in the report; since such a task
  has no task review.
- 2026-10-15: test rules for reviewed work: standing tests or one-time
  checks, test-first with logged exceptions including removals, RED
  before GREEN checked by the task reviewer, weakened tests always a
  finding and deleted ones unless justified at all three reviewers,
  adequacy the reviewer's judgment, the mutation check a manual practice,
  and debugging's test-first skip only for an unreproducible bug.
- 2026-08-05: no read-only test files or lockdown hooks: test weakening is
  detected by reviewers, not prevented.
