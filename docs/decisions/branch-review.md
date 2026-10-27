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
checks each ruling against the final code, and flags undisclosed drift
from binding content in a completed task as DRIFT. It runs on the default
role, never lowered to save cost
(`docs/decisions/model-roles-and-effort.md`).

**The loop.** Only a BLOCKER or MAJOR opens a fix wave: one fresh
implementer with the complete findings list, then a scoped re-review of
the findings answered fixed, the disputed ones going to the adjudicator
(`docs/decisions/adjudication.md`). A wave that leaves no BLOCKER or
MAJOR open is followed by a full-scope pass, skipped only when nothing
changed since the last one; the pass that ends the review is the branch
review's terminal pass, a branch-reviewer dispatch. The cap is three
waves; a finding that would need a fourth goes to the operator as a
decision ask. Off the
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
deviations as ordinary findings rather than DRIFT. The invoking agent
handles the findings under `crucible:receiving-review`, fixes the
BLOCKERs and MAJORs it confirms and runs the review again after
substantial fixes; there is no wave loop and no cap
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
scoped re-reviews verify waves. The cap of three waves is marked
[LOAD-BEARING] as the loop's only termination guarantee, and a DRIFT pass
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
