# Evidence and findings

## Decision

**Finding hygiene.** Panel seats, the terminal pass and the execution
reviewers stake a severity on each finding, BLOCKER, MAJOR or MINOR. In
the spec campaign and the plan phase, a BLOCKER without a reproduction
or evidence is a question, a code-shaped claim in a finding (what a
regex, a command or the code does) carries a run transcript or the tag
`UNVERIFIED`, and an `UNVERIFIED` finding never enters a fix list as it
stands: the controller verifies or discards it
(`skills/redteaming/seat-prompt.md`; `crucible:redteaming § Merge and
finding hygiene`). The task reviewer and the branch reviewer cite
file:line evidence for every finding and treat a BLOCKER without
evidence as a question; the re-reviewer cites file:line for its verdicts
and any new breakage; none of the three uses the `UNVERIFIED` tag.
Improvements and style are not findings, and the execution reviewers
raise no formatting that no repo tool enforces: where a tool enforces
it, the tool's failure is the finding
(`skills/subagent-driven-development/task-reviewer-prompt.md` § Finding
Hygiene and Severity; `skills/requesting-code-review/code-reviewer.md` §
Calibration).

**Evidence on the author's side.** Whoever writes the text under review
carries the seats' rule. A spec's author checks each claim about
existing code, files or tool behaviour as it is written, reading the
file or running the command, or writes it with `UNVERIFIED`, and treats
an unverified draft claim as wrong until checked; the self-review's
evidence check resolves the tags or leaves them as declared input for
the campaign (`crucible:brainstorming § Spec contract`;
`crucible:brainstorming § Spec self-review`). A plan's author reads
every signature, format and pin from the code, never from memory
(`crucible:writing-plans § Self-review`). The controller's fix lists,
merged entries, rulings, verification outcomes, readouts and decision
asks show the evidence for each code-shaped claim or carry `UNVERIFIED`,
and a decision ask resting on an untagged, unverified mechanical fact is
a defect in the ask. The implementer's report gives each code-shaped
claim its command and output, or `UNVERIFIED`
(`skills/subagent-driven-development/implementer-prompt.md` § Report
Format). Before a fix list freezes, each item names every artifact site
restating the content it changes, and a fix landing at fewer sites than
its item names has not landed (`crucible:redteaming § Fix application
and blind verification`). `UNVERIFIED` is the one marker; it tags a
claim and never admits a finding to a fix list.

**Evidence before claims.** Before saying work is complete, fixed or
passing, an agent runs the check that shows it and reports what its
output said (`crucible:using-crucible § The Rule`). Where a fix item's
substance is a predicate (an acceptance check, a gate, a grep), the
controller runs it at the tree state it will run against before
recording the item applied, with the command and output under the item;
a check of a state not yet reached must fail on today's tree, and a
check taken from a seat's remedy is run the same way. The implementer
quotes each test result from the run's own output, the tool result or a
background run's output file, and until that output is read the outcome
is unknown, whatever a notification promised
(`skills/subagent-driven-development/implementer-prompt.md` § Tests:
Test-First, Evidence Before Done). The task reviewer takes that reported
output as given; which seats run the full suite is stated in
`docs/decisions/spec-campaign.md`.

## Why

### Review that holds without a human reader

No step requires the operator to read code or a diff
(`docs/decisions/operator-steering.md`), so human review is not the
backstop and crucible's review has to hold on its own: claims are run,
not read, fixes are verified blind, and severities are staked
(2026-08-06). In "FactReview: Evidence-Grounded Peer Review with
Execution-Based Claim Verification", removing execution evidence changed
17.0% of claim statuses, more than removing any other single evidence
source (https://arxiv.org/abs/2604.04074). (Basis: judgment, accepted by
the maintainer; external.)

Improvements and style were ruled out of findings on 2026-08-06, with
the adversarial reviewer stance: the hunt is bounded by finding
hygiene, not by softening. Upstream's reviewer filed code style and
optimization under Minor and asked for strengths and recommendations
(`superpowers/skills/requesting-code-review/code-reviewer.md`). The
maintainer has since called the rule probably suboptimal; whether it is
right is open (`docs/backlog/review-improvements.md`). (Basis:
judgment, accepted by the maintainer; external, for upstream; the
maintainer's preference, for reopening it.)

A branch's prose review once ran two waves of line-wrap fixes, each
seeding the next; with formatting no tool enforces out of scope, ragged
lines cost nothing (2026-10-07). (Basis: a single incident.)

### Evidence on the author's side

A classification on 2026-08-27 of about 1,620 findings from the 24
feature records then committed, 6 in crucible and 18 in one other
project, found where review effort went: about 40% of findings corrected
a false, mechanically checkable claim about code, files or tools that
the author could have checked when writing; about 29% surfaced consumers
or producers the author never enumerated; about 19%, and 60 to 90% of
findings from round 2 on in the three campaigns instrumented for it,
were introduced by fix waves, mostly a fix landing at one site while a
sibling statement stood. Only 14% were the design judgments a panel
exists for. Seats were held to evidence; the authors and fixers writing
what they review were not. Of 16 findings that overturned or attacked a
ratified decision or a recorded ruling, 15 overturned either a decision
ratified on a factual premise its author supplied and got wrong, or an
adjudication ruling: an unverified fact in a decision ask is how false
premises reach the operator's rulings. (Basis: measured.) The consumer
sweep that answers the second class is part of the spec contract
(`docs/decisions/the-spec.md`).

The rules shipped as prose, with `UNVERIFIED` the only marker and no
tiers of verified, inferred or guessed. A lint for untagged code-shaped
claims waits until the prose rules are seen eroding
(`docs/backlog/claims-lint-untagged-code-claims.md`), a deferral the
maintainer ratified on 2026-08-27. (Basis: judgment, accepted by the
maintainer.)

### Evidence before claims

Upstream's verification-before-completion skill requires fresh
verification evidence before any claim of success or completion, and
before a commit or the next task: "Evidence before claims, always"
(`superpowers/skills/verification-before-completion/SKILL.md`).
Crucible keeps that as one always-loaded line in the router, added on
2026-10-07, instead of a skill that has to trigger, and each seat states
its own checks; SDD's Finish runs the full suite or the project's
declared merge gate on HEAD (`crucible:subagent-driven-development
§ Finish`). The maintainer confirmed that reason on 2026-10-20; whether
crucible's checks cover upstream's table of common failures is still to
be compared (`docs/upstream.md`). (Basis: external, for upstream;
judgment, accepted by the maintainer.)

Fix items whose substance was a check were twice recorded applied with
nobody having run them (2026-08-21 and 2026-09-24), and a check that
cannot fail on today's tree shows nothing about whether it can fire.
On 2026-10-05 the maintainer ruled that only the part of that item its
evidence supported should land. (Basis: measured; the maintainer's
preference, for the scope.)

Twice an implementer acted on a suite outcome no tool had shown it while
the output file it watched was still empty, which is why a result now
comes from the run's own output (2026-10-14). The rule binds the
implementer alone, the seat the focused-check rule leaves to the full
suite (`docs/decisions/spec-campaign.md`); controllers have the router's
line. (Basis: measured; judgment, accepted by the maintainer,
for the scope.)

## Rejected

- **Tiers of certainty** beside `UNVERIFIED` (§ Why).
- **A lint for untagged code-shaped claims**, until the prose rules are
  seen eroding (§ Why).
- **Recording a predicate's result both before and after the change**,
  with a written argument that it is not vacuous: the rule that it must
  fail first carries both (2026-10-05).

## Changes

- 2026-10-14: evidence before claims: a completion claim rests on a check
  run, a predicate fix is run and must fail before its change, and a test
  result comes from the run's own output, unknown until read.
- 2026-10-07: finding hygiene: staked severity, a BLOCKER without
  evidence is a question, campaign seats' code claims run or tagged
  `UNVERIFIED` and kept out of fix lists, and improvements, style and
  unenforced formatting not findings.
- 2026-08-27: evidence on the author's side: claims checked when written,
  record hygiene for the controller and the implementer, and the
  propagation sweep before a fix list freezes.
