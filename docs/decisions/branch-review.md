# Branch review

## Decision

**One owner.** `crucible:requesting-code-review` owns the branch-review loop and states it once. It is mandatory when SDD hands over a branch whose tasks are complete, and before merging any branch (`crucible:subagent-driven-development § Whole-Branch Review`).

**The reviewer.** A fresh branch reviewer reads MERGE_BASE..HEAD full-scope, for what task-scoped gates cannot see: cross-task integration, drift accumulated across the branch, and anything the gates let through. It triages every deferred item, a `deferred-minor` entry for its effect on the code alone, never editing spec or plan text for it (`docs/decisions/fix-verification-and-merge.md`), checks each ruling against the final code, and flags undisclosed drift from binding content in a completed task as DRIFT (`skills/requesting-code-review/code-reviewer.md` § Read Scoping, § Execution Trail, § What to Check). It runs the goal check, may raise premise findings, reports a binding item that is itself wrong and an unrecorded consequential choice, and writes a `Questions` section (`docs/decisions/evidence-and-findings.md`); for each rule the branch ties to a trigger it asks whether every route and phase that must apply it reaches it; a break that follows from what the branch sets out to do, which its spec or requirements source does not state, is labelled for the operator to repair or accept, standing open in the ledger until they answer (`docs/decisions/the-spec.md`; `crucible:requesting-code-review § The branch-review loop`). A review reopened after SDD's Finish has committed reads that commit, the feature's umbrella mark and the open items written to an in-repository home, as part of the branch. Its check for build history exempts decision records, changelogs, the feature folder's files and those open items, all of which exist to hold it (`skills/subagent-driven-development/references/seat-rules.md` § What shipped work carries; `skills/requesting-code-review/code-reviewer.md` § What Was Built, Against What). It runs on the default role, never lowered to save cost (`docs/decisions/model-roles-and-effort.md`).

**Tasks completed branch review only.** For a task the ledger completes branch review only (`docs/decisions/task-loop.md`), the branch reviewer is the first review. The controller names each such task in the card's `[FIRST_REVIEW_TASKS]` slot, and every full-scope pass reads its report and Decision Log against the diff over its range, as the task review would; what it finds opens waves by its staked severity, and no line is owed per task (`crucible:requesting-code-review § Dispatch the branch reviewer`; `skills/requesting-code-review/code-reviewer.md` § Execution Trail).

**Leads and questions.** `Questions` items from task reviewers and implementers, and the other items `skills/subagent-driven-development/references/what-a-report-voices.md` routes as leads, reach the branch reviewer as leads, ledger lines under `## Deferred minors` marked `lead:`. It rules on each, CONFIRMED, RECOMMENDED or LEFT, instead of triaging it; a lead it confirms as an intent or scope gap opens a wave whatever its staked severity, and a pass that leaves one unruled is missing a verdict. Its own `Questions` items go under the ledger's `## Questions`, which its read scoping excludes, so a pass's questions never become the next pass's input (`skills/requesting-code-review/SKILL.md` § The branch-review loop; `skills/requesting-code-review/code-reviewer.md` § Execution Trail; `skills/subagent-driven-development/references/what-a-report-voices.md`).

**The loop.** A fix wave opens on a BLOCKER or MAJOR or a lead confirmed as an intent or scope gap, and otherwise only as the cleanup wave or for a ruling or requested work (below): one fresh implementer with the complete findings list, then a scoped re-review, disputes ruled as `docs/decisions/adjudication.md` states. A wave that leaves no BLOCKER or MAJOR open is followed by a full-scope pass, and the pass that ends the review is the branch review's terminal pass, a branch-reviewer dispatch. The cap is three waves, every wave counting; a finding that would need a fourth goes to the operator as a decision ask. A premise finding is a decision ask, not an open BLOCKER or MAJOR, and holds no merge gate by itself. Off the very-small lane a DRIFT finding is a decision ask to the operator, revert or repair; on the lane, drift from the note is a wave finding. A red suite at SDD's Finish is a BLOCKER that opens a wave. Fixes are never the controller's, the very-small lane excepted (`crucible:requesting-code-review § The branch-review loop`; `skills/subagent-driven-development/references/drift.md`).

**Changes that ride a wave.** An improvement the controller adopts, an operator's ruling and work the operator asked for enter a wave's findings list as labelled changes, applied or declined with a reason; with no defect to confirm, none is answered NOT CONFIRMED or disputed. A declined ruling or requested change goes back to the operator in the next close readout; a declined improvement is work left open (`crucible:requesting-code-review § The branch-review loop`; `skills/subagent-driven-development/references/very-small-lane.md`; `docs/decisions/records-and-workspace.md`).

**Rulings in execution.** A premise ruling the operator gives during the task loop lands as a plan change at the next task boundary; one given at the branch review or its close readout opens a branch-review wave, counted against the cap, and SDD's Finish restarts after it. Work the operator's close-readout answer asks for opens a wave the same way where the spec and plan already require it or the readout listed it; other work is new scope, a feature of its own (`skills/redteaming/references/premise-asks.md` § Premise findings; `crucible:subagent-driven-development § Plan changes mid-execution`; `crucible:requesting-code-review § The branch-review loop`).

**Minors.** A minor rides a wave something else opened, and never opens one by itself. A minor that rode no wave becomes a ledger line listed for the operator in the close readout, with no ruling per minor, never chased by the controller (`skills/requesting-code-review/SKILL.md` § The branch-review loop).

**The cleanup wave.** Once the review has ended with no BLOCKER or MAJOR open and a wave remains under the cap, the controller may open one cleanup wave per branch of the minors, and of the leads the reviewer ruled CONFIRMED or RECOMMENDED, that it judges worth fixing, a wave of improvements alone included. It runs as any wave, counted against the cap (`crucible:requesting-code-review § The branch-review loop`), and the close readout says why each minor and lead it left was left (`skills/subagent-driven-development/references/finish.md`).

**Standalone mode.** On a branch with no SDD run, the reviewer gets no ledger inputs and returns its report as its final message, and the invoking agent handles the findings under `crucible:receiving-review`, with no wave loop, no cap and no cleanup wave (`crucible:requesting-code-review § Standalone mode`; `skills/requesting-code-review/code-reviewer.md` § Standalone Mode).

**Review seats build their own diff.** The task reviewer, re-reviewer, branch reviewer and adjudicator each check that both ends of their range are commits and the base an ancestor of the head, have git write the diff into files in their scratch subdirectory, and read it there; a failed check is reported, never reviewed as an empty diff. The controller records the base before each dispatch, never uses `HEAD~1`, and never takes the diff into its own context (`skills/subagent-driven-development/references/seat-rules.md` § Building the diff; `skills/subagent-driven-development/task-reviewer-prompt.md` § Diff Under Review; `skills/requesting-code-review/code-reviewer.md` § Git Range to Review).

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
only termination guarantee. Until 2026-11-02 a DRIFT pass spent a wave
so that revert-and-replan cycles could not bypass it; since a revert
became the operator's answer each time, drift adds no cycle the operator
did not choose, and the pass spends none
(`docs/decisions/task-loop.md`). One fixer
with the whole list is upstream's rule: per-finding fixers each rebuild
context and re-run suites, and in a session upstream reports, a final
review's fix wave cost more than all its tasks combined. (Basis:
external; judgment, accepted by the maintainer, for the floor, the
cap and drift's operator ask, the intuition quoted being the
maintainer's.)

Minors stopped opening waves on 2026-10-07, after a prose branch's review
ran two waves of line-wrap fixes, each seeding the next
(`docs/decisions/evidence-and-findings.md`). The guard against chasing
minors was stated outright in the first design, "because common sense
isn't common"; leftover minors reach the operator in the close readout,
because a roll-up nobody reads is a silent discard. (Basis: a single
incident; judgment, accepted by the maintainer.)

On 2026-10-30 the rule loosened, without returning to minors opening
waves by themselves. The maintainer found finish too rigid: "'minors
don't launch a fix wave' is too restrictive (in practice, I approve them
anyway)". The controller may now open one cleanup wave of the minors
and leads it judges worth fixing, after the review has ended clean. The
incident's danger was fixes seeding fixes; the one-per-branch limit
still guards against it, since what the cleanup wave raises at MINOR
opens nothing, and the cap counts the wave like any other. (Basis: the
maintainer's preference, for loosening the rule; judgment, accepted by
the maintainer, for the wave's form.)

### Changes that ride a wave

An adopted improvement used to ride a fix wave "as one of its
findings", but the fixer's contract is to confirm a defect before
editing and to answer NOT CONFIRMED where there is none. An
improvement has no defect, so a fixer following its contract could
send it to the adjudicator, which rules on defects. The audit of the
hypothesis-specs umbrella found this
(`docs/decisions/evidence-and-findings.md` § The audit of the
hypothesis-specs umbrella). A labelled change carries its own
instruction, apply or decline with a reason. Operator rulings and
requested work ride the same way, since they too have no defect to
confirm. The cards carry the label, so for labelled items they
override their templates' two-answer rule, and the templates gained no
words. A declined ruling or requested change goes back to the operator
in the next readout rather than into the open items. (Basis:
measured, for the audit's finding; judgment, accepted by the
maintainer.)

### Leads keep the task review's guards

In a task review, an intent or scope gap fails its judgment and opens a
wave at any severity. The audit found that concerns reaching the branch
reviewer as leads lost that guard
(`docs/decisions/evidence-and-findings.md` § The audit of the
hypothesis-specs umbrella): a lead was confirmed at a staked severity,
so an intent gap staked MINOR rode no wave. A lead confirmed as such a
gap now opens a wave as the task review's judgment would, and a pass
that leaves a lead unruled is refused as a review missing a verdict is.
(Basis: measured, for the audit's finding; judgment, accepted by the
maintainer.)

### Rulings in execution

A premise ruling given in execution had no wave to land in: the
operator met the finding only in SDD's close readout, after the loop had
ended (`docs/decisions/evidence-and-findings.md` § The audit of the
hypothesis-specs umbrella). Since 2026-10-30, a ruling at the close
readout opens a branch-review wave and Finish restarts after it, and
one given during the task loop lands as a plan change at the next task
boundary, the plan's own route for a change mid-execution. A ruling's
wave counts against the cap like any other, and past the cap the
operator's answer opens it, as an escalation's answer does. Work the
answer asks for opens a wave the same way only where it is already the
branch's, required by the spec and plan or listed in the readout;
anything else is new scope, as finishing already held. (Basis:
measured, for the audit's finding; judgment, accepted by the
maintainer.)

### A wave that changes no rule

A full-scope pass costs what the branch's size costs, however small the
wave before it. Nine such passes ran after waves on earlier text branches of
2026-11-04 and 2026-11-05, at about 116k to 199k tokens each. One, after a
wave of six minors and four small wording and rule changes, found a MAJOR, in
a rule that wave had just added: seeing it needed the reviewer's card, outside
the fix diff, so the wave's scoped re-review could not. The other eight found
only MINORs, often in rules the previous wave had added. Two lanes of
2026-11-04 skipped the pass, the maintainer leaving the call to the agent, one
saving about 275k tokens; neither shows what it would have found.

A skip for a wave that took no BLOCKER or MAJOR and changes no rule or
behavior, judged in a new line of the re-review's verdict, was built on
2026-11-05 and withdrawn before landing. Over four waves and five full passes,
about 865k tokens, each pass found another hole: the re-reviewer could not see
the rule its answer rested on, a base merge lay outside its range, a minor
left open or upheld in a dispute could vanish, a lead could go unruled. Its two
conditions became six and its 106 words 194, and no wave of that branch, nor of
the two batches before it, would have qualified. So every wave that changes
text keeps its pass. (Basis: measured, for the passes and the withdrawal;
judgment, for keeping the pass. An agent's proposal, which the maintainer
accepted.)

### The feature folder's files are not shipped history

The branch reviewer flags build history (task numbers, wave names,
rulings carrying dates) in what a branch ships, decision records and
changelogs exempt (`docs/decisions/authoring-crucible.md`). Once a
review that reopens after Finish reads the open items Finish wrote,
they would be flagged every time, since each item names its source by
the ledger's prefixes; the spec and plan are build records too. The
task that wired Finish's commit into the reviewer's range widened the
exemption to the feature folder's files, which the build-history rule
already names as a home for that history, and the open items were then
one of them. (Basis: judgment, an agent's call the maintainer has not
ruled on: an implementer's, in that feature, that its task review
upheld.) When open items moved out of the feature folder to the
project's own home (2026-11-01), the exemption followed them, for the
same reason. (Basis: judgment, an agent's call the maintainer has not
ruled on: the implementer's, in that feature.)

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
preference, for the aim; measured.) The audit of the hypothesis-specs
umbrella found that parity partial: the reviewer had no finding for a
binding item that is itself wrong and no clause for an unrecorded
consequential choice. Both moved from the redteam seat's template into
the shared reference the reviewer already reads, where for this seat
the choice is one the code makes (`docs/decisions/evidence-and-findings.md`).
(Basis: measured, for the audit's finding; judgment, accepted by the
maintainer.)

Leads carry what task reviewers and implementers voice to the one seat
that sees every task, and a pass's questions stay out of the next
pass's input. The trace question comes from the umbrella-specs
feature (2026-10-28), whose rule fired "at each task or round boundary"
while two phases, the very-small lane and every branch review, have
none; the spec campaign and the plan phase missed it, and the branch
review confirmed it as its one MAJOR. (Basis: a single incident;
judgment, accepted by the maintainer, for the forms.)

Until 2026-11-03 each lead carried a kind, `question`, `proposal` or `concern`, whose one consumer was the rule that a concern is CONFIRMED or LEFT, never RECOMMENDED. Both went: the one-liner still says what the lead is, and a concern ruled RECOMMENDED is harmless, the controller adopting it or not as any improvement. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

### The first review of a task with none

When a plan may route a task's review to the branch review alone
(`docs/decisions/task-loop.md`), every check the task review made needs
an owner, or the mark drops checks rather than moving them. The
controller's gate owns what the report must show; the branch reviewer,
the seat best placed for the rest since it sees every task, reads the
report against the diff. It has to know which tasks went unreviewed,
hence the slot. (Basis: judgment, accepted by the maintainer,
2026-10-29.)

As first written, the branch reviewer made the task review's four
judgments over each such task's range and wrote a line per task, which
SDD's Finish read in place of the task's review file, and a failed
intent, scope or deviation-audit judgment opened a wave whatever its
staked severity, as the task loop wires it. Only the review's first pass
owed the line at first, so a marked task redone through
revert-and-replan after that pass would get no judgments at all; a seat
of the plan phase found it, and the line became owed by the first
full-scope pass after each such completion. The skill text rewrite
retired the owed line, its report section and that wiring: every
full-scope pass reads the reports of such tasks, a redone task's
included, and its findings open waves by their staked severity, as any
pass's do. (Basis: the skill-text-rewrite umbrella's D4, with the
maintainer's judgment that marks were used too liberally; judgment, the
controller's proposal accepted by the maintainer, 2026-11-02.) A task's routed items were first
to reach the reviewer through the sweep as before; the task that
shipped the reviewer's mandate judged them in the task's own deviation
audit instead, where the task loop then checked each routed item at
its task's review, and the controller ruled that reading stands; routed
items retired with the plan's routing table on 2026-11-02
(`docs/decisions/plans.md`). (Basis:
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

- **A single fix wave** for the branch, upstream's rule: fixes unmask
  problems and drift, and only a full-scope read clears the branch (§ Why).
- **Minors opening waves by themselves**: the one cleanup wave per
  branch is the controller's call, never a minor's (§ Why).
- **An adopted improvement riding a wave as a finding**: the fixer's
  contract is to confirm a defect, and an improvement has none (§ Why).
- **Skipping the full-scope pass after a wave that changes no rule**: it took six conditions, each pass found another hole, and it would rarely apply (§ Why).
- **A wave's size as the test for its full pass**, in files, lines or tasks: a wave of small changes that added a rule produced a MAJOR (§ Why).
- **A review-package script**: 173 lines for what a reviewer with a shell
  of its own runs in a few git commands (§ Why).
- **Per-finding fixers**: each rebuilds context and re-runs suites, and in
  a session upstream reports, a final review's fix wave cost more than all
  its tasks combined (§ Why).

## Changes

- 2026-11-05: a skip of the full-scope pass after a wave that changes no rule was built and withdrawn before landing, and is rejected, its evidence recorded; because it took six conditions, each pass found another hole, and it would rarely apply. The loop is unchanged.
- 2026-11-04: an `unstated break` is written open under `## Adjudication rulings` and named in the close readout among the work left open, because an ask lost to compaction would leave nothing telling Finish it was pending, and an integration answer would delete it with the workspace; the reviewer's report format and verdict line name its label beside `premise`, because a reviewer staking one at MAJOR would answer No on a pass the loop treats as ending the review.
- 2026-11-04: the branch reviewer labels a break that follows from what the branch sets out to do, which its spec or requirements source does not state, and the operator repairs it or accepts it by a ruling; an ordinary defect stays an ordinary finding (`docs/decisions/the-spec.md`).
- 2026-11-04: the branch reviewer's check of a branch-review-only task's Decision Log covers a loosening's justification beside a deletion's, since a removed assertion and any other loosening now take the deleted test's justifications (`docs/decisions/test-rules.md`).
- 2026-11-03: the `## Questions` line forms are cited at `skills/requesting-code-review/SKILL.md` § The branch-review loop, which holds them since they left SDD's § Setup.
- 2026-11-03: the premise-finding route is cited at `skills/redteaming/references/premise-asks.md`, where flip-paths' § Premise findings moved, so a controller handling a premise finding no longer loads the flip paths (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: a lead no longer carries a kind (`question`, `proposal`, `concern`), and the rule that a concern is CONFIRMED or LEFT goes, so the reviewer may rule any lead RECOMMENDED; because the kind's one consumer was that rule, and a concern ruled RECOMMENDED is harmless.
- 2026-11-03: the findings a very-small lane's last pass left open no longer reach the standard route's branch reviewer as `Lane:` leads at their staked severity after the lane's upgrade hatch, nor a BLOCKER or MAJOR one it leaves the close readout; the brainstorm the hatch invokes takes them in its incoming document instead, because the carry-over sat in text every standard run reads to serve a rare move (`docs/decisions/routes.md`).
- 2026-11-02: the build-history exemption for the feature folder's
  files is every execution reviewer's, the one for Finish's open items
  the branch reviewer's alone, the shared rule and the diff procedure
  cited at their one home in the shared seat reference; because the
  task reviewer's and re-reviewer's copies exempted only decision
  records and changelogs.
- 2026-11-02: after the very-small lane's upgrade hatch, the findings
  the lane's last pass left open reach the standard route's branch
  reviewer as `Lane:` leads at their staked severity, a confirmed one
  standing at it and a BLOCKER or MAJOR left reaching the close
  readout; because the move to the standard route would otherwise drop
  them (`docs/decisions/routes.md`).
- 2026-11-02: for a task completed branch review only, every full-scope
  pass reads its report's Decision Log against the diff, its findings
  opening waves by their staked severity; the per-task line a pass owed,
  the template's `### Task Lines` report section and its
  `## Tasks With No Task Review` section,
  `crucible:requesting-code-review`'s section on such tasks, and the
  wiring that counted a failed judgment on one as a BLOCKER or MAJOR
  retired; the card's `[BRANCH_ONLY_TASKS]` slot renamed
  `[FIRST_REVIEW_TASKS]`, listing every such task, and its
  `[MANDATE_REMINDER]` no longer names task lines. After the
  skill-text-rewrite umbrella reduced the mark to one field and its
  reason.
- 2026-11-02: the handoff and the triage no longer take the plan's
  routed items still open, and a task completed branch review only no
  longer has its routed items judged in its deviation audit: routed
  items retired with the plan's routing table
  (`docs/decisions/plans.md`); the `[LEDGER_MINORS]` slot lost its
  clause on routed deferred items.
- 2026-11-02: a wave's disputed findings are ruled as
  `docs/decisions/adjudication.md` now states, by the controller or,
  where a dispute touches binding content or the Intent or concerns a
  diff the controller wrote, the adjudicator; no longer always the
  adjudicator.
- 2026-11-02: a DRIFT finding is an operator ask, revert or repair, a
  repair riding a fix wave against the cap; the rule that a DRIFT pass
  spends a wave (its `Branch wave` line with `commits none`) and the
  hand-off to revert-and-replan retired, after the skill-text-rewrite
  umbrella's audit found revert-and-replan never ran.
- 2026-11-02: the handoff and the triage take the spec and plan
  reviews' `deferred-minor` entries, ledger lines with source `Spec` or
  `Plan`, each judged for its effect on the code alone; because fix
  lists no longer take the review MINORs not against binding text
  (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-01: a reopened range holds the open items Finish wrote to an
  in-repository home, and the build-history check exempts them, since
  open items no longer live in the feature folder whose files it
  exempted (`docs/decisions/records-and-workspace.md`).
- 2026-10-30: the rejection of minors opening waves is narrowed to
  minors opening them by themselves: the controller may open one
  cleanup wave per branch, counted against the cap, after the
  maintainer found the rule too restrictive. Improvements, rulings and
  requested work ride a wave as labelled changes, applied or declined,
  never adjudicated; a lead confirmed as an intent or scope gap opens a
  wave and an unruled lead is a missing verdict; a premise ruling in
  execution lands as a plan change during the task loop and as a
  branch-review wave after it, as does a listed minor the operator's
  answer asks to fix; the reviewer reports a wrong binding
  item and an unrecorded consequential choice; these close gaps the
  audit of the hypothesis-specs umbrella found. The reviewer also takes
  Finish's open-items commit as part of a reopened range and exempts
  the feature folder's files from its build-history check, since that
  file names each item's source; that exemption's basis is labelled an
  agent's call the maintainer has not ruled on.
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
