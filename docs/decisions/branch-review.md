# Branch review

## Decision

**One owner.** `crucible:requesting-code-review` owns the branch-review
loop and states it once. It is mandatory when SDD hands over a branch
whose tasks are complete, and before merging any branch. SDD's handoff
passes the ledger's deferred minors, the plan's routed items still open
among them, and the adjudication rulings
(`crucible:subagent-driven-development § Whole-Branch Review`).

**The reviewer.** A fresh branch reviewer reads MERGE_BASE..HEAD
full-scope, for what task-scoped gates cannot see: cross-task
integration, drift accumulated across the branch, and anything the gates
let through. It may read beyond the diff where correctness depends on it,
triages every deferred item (promote, fix in a wave, or leave parked),
a task's routed items aside where that task was completed branch review
only (below),
checks each ruling against the final code, and flags undisclosed drift
from binding content in a completed task as DRIFT. It runs the goal
check, may raise premise findings and writes a `Questions` section
(`docs/decisions/evidence-and-findings.md`), and for each rule the
branch ties to a trigger asks whether every route and phase that must
apply it reaches it when the trigger occurs. It runs on the default
role, never lowered to save cost
(`docs/decisions/model-roles-and-effort.md`).

**Tasks completed branch review only.** For a task the ledger completes
branch review only (`docs/decisions/task-loop.md`), the branch reviewer
is the first review. The controller names each such task in the card's
`[BRANCH_ONLY_TASKS]` slot, with its range, its latest attempt's report,
the brainstorm decision record where the task writes a decision record,
and the amendment commits its range holds. Over that range the reviewer
makes the task review's four judgments, intent, scope (a deleted or
weakened test against the Decision Log included, and a change to the
plan or spec other than a named amendment commit), the deviation audit
and quality, checks each decision-record position's basis against the
brainstorm decision record, judges the task's routed items in its
deviation audit rather than in the sweep, and rules on its leads. The
first full-scope pass after each such completion, the review's first
pass or the pass resuming it after a revert-and-replan, writes one line
per task naming the judgments and what they raised; a pass missing a
line it owes is refused as a review missing a verdict is, and SDD's
Finish reads that line in place of the task's review file. A failed
intent, scope or deviation-audit judgment on such a task opens a wave
whatever its staked severity, as the task loop wires it
(`crucible:requesting-code-review § Tasks completed branch review only`;
`skills/requesting-code-review/code-reviewer.md` § Tasks With No Task
Review).

**Leads and questions.** A task reviewer's and an implementer's
`Questions` items, an implementer's fixes proposed outside its task, the
concerns of a fix report no re-review reads, and on the very-small lane
a dispatched implementer's concerns, reach the branch reviewer as leads:
ledger lines under `## Deferred minors` marked `lead (<kind>)`. It rules
on each lead instead of triaging it: CONFIRMED, a finding at a staked
severity; RECOMMENDED, an improvement it backs, which the controller may
adopt to ride the next fix wave or which reaches the operator in the
close readout; or LEFT, with one line. Its own `Questions` items, and a
branch-review fix report's, go under the ledger's `## Questions` with
the controller's disposition; the close readout lists them, and the
branch reviewer's read scoping excludes that section, so a pass's
questions never become the next pass's input
(`crucible:subagent-driven-development § Setup`;
`skills/requesting-code-review/code-reviewer.md` § Execution Trail).

**The loop.** Only a BLOCKER or MAJOR, or a failed judgment on a task
completed branch review only, opens a fix wave: one fresh
implementer with the complete findings list, then a scoped re-review of
the findings answered fixed, the disputed ones going to the adjudicator
(`docs/decisions/adjudication.md`). A wave that leaves no BLOCKER or
MAJOR open is followed by a full-scope pass, skipped only when nothing
changed since the last one; the pass that ends the review is the branch
review's terminal pass, a branch-reviewer dispatch. The cap is three
waves; a finding that would need a fourth goes to the operator as a
decision ask. A premise finding is a decision ask, not an open BLOCKER
or MAJOR: a pass that leaves only premise findings open ends the review,
and one left open holds no merge gate by itself. The re-reviewer rules
on each concern a fix report raises, and a re-review missing a ruling
is missing a verdict. Off the
very-small lane, a DRIFT finding hands its task to revert-and-replan and
spends a wave; on the lane, drift from the note is a wave finding. A red
suite at SDD's Finish is a BLOCKER that opens a wave. Fixes are never the
controller's, the very-small lane excepted
(`crucible:requesting-code-review § The branch-review loop`).

**Minors.** A minor rides a wave a BLOCKER or MAJOR opened, and never
opens one. A minor that rode no wave becomes a ledger line listed for the
operator in the close readout, with no ruling per minor, never chased by
the controller.

**Standalone mode.** On a branch with no SDD run, the reviewer gets no
ledger inputs and no report file, returns its report as its final
message, works under the host's temporary directory, and reports
deviations as ordinary findings rather than DRIFT. With no ledger, the
report is the record of everything it raises, its questions included.
The invoking agent handles the findings under `crucible:receiving-review`,
fixes the BLOCKERs and MAJORs it confirms, sends a premise finding to the
operator as a decision ask rather than to a fix, and runs the review
again after substantial fixes; there is no wave loop and no cap
(`crucible:requesting-code-review § Standalone mode`).

**Review seats build their own diff.** The task reviewer, re-reviewer,
branch reviewer and adjudicator each check with `git cat-file -t` that both
ends of their range are commits and with `git merge-base --is-ancestor`
that the base is an ancestor of the head, have git write the commit list and a stat
summary with a `-U10` patch into files in their scratch subdirectory with
`--output`, and read the diff there. An end that is not a commit, a base
that is not an ancestor of the head, or a failing git command, is
reported, never reviewed as an empty diff. The
controller records the base before each dispatch, never uses `HEAD~1`, and
never takes the diff into its own context
(`skills/subagent-driven-development/task-reviewer-prompt.md` § Diff Under
Review; `skills/requesting-code-review/code-reviewer.md` § Git Range to
Review).

## Why

### An iterative loop with a floor and a cap

Upstream's final review gets one fix dispatch with the complete findings
list, one scoped re-review and the controller's adjudication of
residuals: "There is no second fix wave"
(`superpowers/skills/subagent-driven-development/SKILL.md`). Crucible's
first design (2026-08-06) made the loop iterative, because fixes unmask
problems and drift, and stopped it by severity rather than by banning
iteration: the maintainer's intuition was that such a loop "shifts to
lesser and lesser issues". Only a full-scope read clears the branch;
scoped re-reviews verify waves. The cap of three waves is the loop's
only termination guarantee, and a DRIFT pass
spends a wave so that revert-and-replan cycles cannot bypass it. One fixer
with the whole list is upstream's rule: per-finding fixers each rebuild
context and re-run suites, and in a session upstream reports, a final
review's fix wave cost more than all its tasks combined. (Basis:
external; judgment, accepted by the maintainer, for the floor and the
cap, the intuition quoted being the maintainer's.)

Minors stopped opening waves on 2026-10-07, after a prose branch's review
ran two waves of line-wrap fixes, each seeding the next
(`docs/decisions/evidence-and-findings.md`). The guard against chasing
minors was stated outright in the first design, "because common sense
isn't common"; leftover minors reach the operator in the close readout,
because a roll-up nobody reads is a silent discard. (Basis: a single
incident; judgment, accepted by the maintainer.)

### One owner, and a standalone use

On 2026-10-07 the loop was stated in both SDD and requesting-code-review;
it moved to one statement, and the skill regained upstream's use outside
SDD as a standalone mode, rather than dropping it with no reason. Its
mandatory trigger lost its "substantial" on 2026-10-15 and reads "before
merging any branch", as upstream's "Before merge to main" does: an edit
made under the trivial-edit waiver is already outside the process. (Basis: judgment, accepted by the
maintainer; external, for upstream's trigger.)

### The last line of defence

The maintainer asked for the reviewers' mandate to be extended "to
parity" with the redteam seats', as "the last line of defense" ("maybe only
full-branch, rather than task reviews?"), especially on the very-small
lane, which has no independent review of its premises (2026-10-28). An
escape analysis the same day found the branch review catching both
premise-level MAJORs that task reviews had let through, and 6 of its 11
BLOCKERs or MAJORs on planned routes premise-level or plan-coverage gaps
(`docs/decisions/evidence-and-findings.md`). (Basis: the maintainer's
preference, for the aim; measured.)

Leads carry what task reviewers and implementers voice to the one seat
that sees every task, and a pass's questions stay out of the next
pass's input. The trace question comes from the umbrella-specs
feature (2026-10-28), whose rule fired "at each task or round boundary"
while two phases, the very-small lane and every branch review, have
none; the spec campaign and the plan phase missed it, and the branch
review confirmed it as its one MAJOR. (Basis: a single incident;
judgment, accepted by the maintainer, for the forms.)

### The first review of a task with none

When a plan may route a task's review to the branch review alone
(`docs/decisions/task-loop.md`), every check the task review made needs
an owner, or the mark drops checks rather than moving them. The
controller's gate owns what the report must show; the branch reviewer
owns the judgments, and it is the seat best placed for them, since it
sees every task. It has to know which tasks went unreviewed, hence the
slot; without a per-task line nothing would show that it made the
judgments, and SDD's Finish would find neither a review file nor a
record in its place. The wiring is the task loop's, so a failed intent
or scope judgment is not left to ride a wave as a minor. (Basis:
judgment, accepted by the maintainer, 2026-10-29.)

As first written, only the review's first pass owed the line, so a
marked task redone through revert-and-replan after that pass would get
no judgments at all; a seat of the plan phase found it, and the
line became owed by the first full-scope pass after each such
completion, a redone task's included. A task's routed items were first
to reach the reviewer through the sweep as before; the task that
shipped the reviewer's mandate judged them in the task's own deviation
audit instead, where the task loop checks each routed item at its
task's review, and the controller ruled that reading stands. (Basis:
judgment, accepted by the maintainer, 2026-10-29.)

### Review seats build their own diff

On 2026-10-11 crucible deleted its copy of upstream's `review-package`
script, by then 173 lines, which checked that two refs named commits and
ran three git commands into a file, for a reviewer with a shell of its
own. The seat reads the diff from files because hosts cap inline tool
output below a branch diff's size: Claude Code's shell tool truncates
output past 30,000 characters, by its tool description as read on
2026-10-20. Git's `--output` writes the bytes without passing them
through the seat's shell. `HEAD~1` silently drops all but the last commit
of a multi-commit task, upstream's warning, kept. Anything pasted into the
controller's context stays there for the rest of the session. (Basis:
measured, for the script; external, for the host and upstream; judgment,
accepted by the maintainer.)

## Rejected

- **A single fix wave** for the branch, upstream's rule (§ Why).
- **Minors opening waves** (§ Why).
- **A review-package script** (§ Why).
- **Per-finding fixers** (§ Why).

## Changes

- 2026-10-29: the branch reviewer is the first review of each task
  completed branch review only, named in a new slot: it makes the task
  review's four judgments over the task's range and checks its decision
  record's bases, judges its routed items in its deviation audit, and
  writes a line per task in the first full-scope pass after that
  task's completion, which Finish reads; a failed intent, scope or
  deviation-audit judgment opens a wave at any severity; so that no
  check the task review made goes unowned.
- 2026-10-29: the branch reviewer runs the goal check, raises premise
  findings, which keep no review open and hold no merge, writes
  `Questions` to the ledger's `## Questions`, rules on leads CONFIRMED,
  RECOMMENDED or
  LEFT, and asks the trace question; the re-reviewer rules on a fix
  report's concerns; the standalone report is its own record; after the
  maintainer's request and an escape analysis.
- 2026-10-28: the wave cap lost its [LOAD-BEARING] mark, its wording
  kept: marks are a spec convention, and the skills place none on their
  own text (`docs/decisions/the-spec.md`).
- 2026-10-27: review seats also check that the range's base is an
  ancestor of its head: a range across diverged history would be
  reviewed as a diff of unrelated trees. Upstream's review-package added the same guard
  (superpowers v6.4.1).
- 2026-10-15: the branch-review loop, owned by requesting-code-review:
  mandatory after SDD and before merging any branch, a full-scope reviewer,
  waves opened only by BLOCKER or MAJOR, a full-scope terminal pass, a cap
  of three waves, minors riding waves or listed for the operator, and a
  standalone mode with no loop.
- 2026-10-11: review seats build their own diff into files, refusing a
  range whose ends are not commits.
