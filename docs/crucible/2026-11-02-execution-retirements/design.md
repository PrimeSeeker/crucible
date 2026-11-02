# Execution retirements: the execution side of the skill text rewrite

Umbrella: `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`

## Intent

**Problem.** The umbrella's audit found execution mechanisms that catch
little or never ran (the umbrella's Intent holds the figures): the tree
check's readings around every review window, the seat-replacement
procedure, the pre-flight plan-conflict scan, the task review's
cannot-verify items, the snapshot-blessing procedure, adjudication of
every dispute by a fresh seat, revert-and-replan, the fix ladder's
fresh-implementer waves and its breaker, the very-small lane's Lane Fit
shape verdict and upgrade-hatch procedure, the deferral chain behind
the plan's routing table, and the grading chain of `Review: branch
only`. Its entry for this child names them, the landing ask after the
final pass with parked findings filed first, and three backlog items.

**Goals.**

- **G1.** Each mechanism the entry names ends in the state the
  Decisions below give, keeping the cheap guards the umbrella's D2 keeps
  where a failure would be silent.
- **G2.** The text stays consistent: no shipped skill text, template,
  generated agent, test or live decision record states a retired
  mechanism as current.
- **G3.** The skills do not grow (the umbrella's C1 and C2), and the
  landing states the net change and the sizes.

**Non-goals.**

- The campaign side (`review-retirements`, landed): this child changes
  campaign text only where an execution mechanism the entry names is
  stated there — the tree check and the seat-replacement gate in
  `crucible:redteaming`, the routing table and the mark's grading in the
  plan phase and the folded lane, the deferral disposition's routing.
- Consolidating restatements into one owner text (`placement`): where
  this child edits a restatement, it changes its content only.
- New mechanisms. The one widening is E2's: a dispute on a diff the
  controller wrote keeps its independent read.

## Decisions

All lightly held. Each names its basis; record numbers are entries of
the brainstorm decision record.

- **E1. The fix loop: three resumed waves, then the operator.** A
  task's fix waves resume its recorded implementer, at most three; where
  the host exposes no resume operation, each wave dispatches a fresh
  implementer with the open findings and the task's report file, as
  today's fallback does. Findings still open after the third wave stop
  the task: the controller puts them to the operator as a decision ask
  with a recommendation — park a finding with its reason, block the
  work, or another approach — and records the ask and the answer under
  the ledger's `## Adjudication rulings`. A finding parked on that
  answer keeps the `Task <N>: parked` line and the completion line's
  parked count, and reaches the close readout. The fresh implementer at
  waves 4–5, its tier escalation and the breaker go, and with the
  breaker its sense of "load-bearing". The branch review's own cap of
  three waves is unchanged. Basis: the umbrella's D3; the cap and the
  ask's options, record 0.
- **E2. Disputes: the controller rules, with three independent reads.**
  The controller rules on a disputed finding with its evidence — an
  implementer's NOT CONFIRMED, a finding it judges wrong, a plan
  conflict — and records the ruling, its reason and its evidence under
  `## Adjudication rulings`. A fresh seat on the default role, the
  adjudicator, rules instead where the dispute touches binding text or
  the Intent, or concerns a diff the controller wrote (a task it
  implemented inline, any lane diff). A plan conflict that is a design
  judgment still goes to the operator, and a ruling that touches
  binding text, the adjudicator's included, still passes
  `skills/redteaming/references/flip-paths.md` § The containment test.
  The adjudicator's inputs point to the one full statement of what binds
  (`crucible:subagent-driven-development` § The Task Loop, its
  Deviations paragraph) rather than restating part of it. Every ruling
  the controller makes, and every dismissed BLOCKER or MAJOR, still
  reaches the close readout with its ruling, and an upheld finding
  still re-enters the loop. This holds in
  the task loop, the branch review and on the lane; a red suite at
  Finish that the controller judges not the branch's is a dispute under
  the same rule. Basis: the umbrella's D4; the own-diff read, record 1,
  since a ruling on its own diff that only the close readout lists
  would be silent to an operator who does not read diffs (the
  umbrella's D2).
- **E3. Drift found after the fact: the operator chooses.** Work found
  off-plan without a logged decision — by the task review's deviation
  audit, by the controller, or by a branch-review pass flagging it
  DRIFT — within the materiality bound (an undisclosed deviation from
  binding content, or one with cross-task blast radius) is a decision
  ask to the operator: revert the task and run it again from step 1, or
  repair it in the fix loop or, at the branch review, in a wave counted
  against its cap; the controller recommends one. Below the bound,
  undisclosed advisory choices and disclosed-but-unjustified Decision
  Log entries enter the fix loop, as today. The revert-and-replan
  section, its attempt numbering (the `-x<X>` report names and the
  `reverted` line's attempt number) and the rule that a DRIFT pass
  consumes a wave go. On the very-small lane,
  drift from the note stays a wave finding. Basis: the umbrella's D3;
  resolves `docs/backlog/implementer-dispute-channel.md`.
- **E4. Small retirements.**
  - The pre-flight plan-conflict scan goes; conflicts that emerge are
    the review loop's, as today.
  - The task review's cannot-verify items go, from the skill and the
    task-reviewer template, with the loop trigger they fed.
  - Snapshot blessing becomes one line: a behaviour-preservation claim
    that rests on changed snapshot or golden output is never blessed by
    the controller; a fresh blind seat, on the bounded role or better,
    given the old and new output and the claim, rules on it, and a
    change it finds visible goes to the operator as a decision ask.
  Basis: the umbrella's D3 and D4.
- **E5. The tree check: one status check after each review seat.**
  After a review seat returns — task reviewer, re-reviewer,
  adjudicator, branch reviewer, the snapshot seat, and in a campaign or
  plan phase each panel seat or concurrent batch, the round-0 pre-pass,
  the blind verifier and the terminal pass — and before the next
  commit, the controller confirms HEAD is the commit the seat was
  dispatched on and the status shows no tracked or staged change and no
  untracked path that was not there at dispatch; otherwise the seat's
  report is void until it runs again on a clean tree. The readings are
  no longer recorded around each window, and the round record's fields
  for them go. The rule that nothing is committed while a seat works
  stays. Basis: the umbrella's D4.
- **E6. Seat replacement: one line.** In both skills: a replacement for
  a seat is never started until the host confirms the first has stopped,
  and it writes to a fresh report path. The procedure around it — the
  ambiguous-liveness BLOCKED line and its escalation text — goes; a
  seat whose state the host cannot confirm is a stop-and-ask, as any
  unresolvable state is. A campaign's quorum and degraded-round rules
  are unchanged. Basis: the umbrella's D4.
- **E7. The deferral chain: a marker and its owning task.** A
  `Deferred to implementation:` marker stays the device. A plan's own
  markers sit in the task that owns them; each spec marker is named, by
  its site, in the Contract of the plan task that owns it, and the plan
  phase's mechanical pre-pass checks that every spec marker has an
  owning task, as part of its ownership closure. The deferred-items
  routing table goes, with its row format and owner form, the folded
  lane's per-round appending, the plan phase's appending and seeding,
  the ledger's deferred list, the implementer's one Decision Log entry
  per routed item, the task reviewer's per-row check and its report
  line, and the branch review's sweep of routed items. A deferred call
  is still the implementer's, logged where it departs from advisory
  content. The carriage of `deferred-minor` entries into the ledger's
  `## Deferred minors` for the branch review's triage is unchanged.
  Basis: the umbrella's D4 and its interface on deferred campaign
  MINORs; owners in the task, record 2.
- **E8. `Review: branch only`: one field and its reason.** A task may
  carry the mark, with its reason, when the plan is written; the mark's
  criterion is unchanged. No seat grades marks as such: the plan phase's
  and the folded campaign's grading mandates go, as do the rules on
  which waves may add a mark. Once the plan's review has closed, no mark
  is added: the task keeps its review. The plan phase's close readout
  still lists the marked tasks for the operator. In execution, a marked
  task whose report is DONE and passes the verification gates is
  completed branch review only; a report raising any concern, or
  failing a gate, sends the task to its task review. At the branch
  review, the reports of tasks completed branch review only join the
  branch reviewer's inputs, whose full-scope pass reads each one's
  Decision Log against the diff; its findings open waves by their
  staked severity. The owed per-task line, its slot, its report section,
  the loop-wiring clause that counted its failed judgments as BLOCKER
  or MAJOR, and the Finish record check that reads that line go. Basis:
  the umbrella's D4; the branch review's side and the defaults,
  record 3; the late mark settles the item
  `docs/backlog/skill-text-rewrite.md` left to this child.
- **E9. The very-small lane.** The branch reviewer's Lane Fit section
  goes: its shape verdict is retired and its goal half is the branch
  review's goal check, which runs on the lane with the note's Intent.
  The upgrade hatch becomes one stop-and-ask line: where overturning a
  major mechanism of the change is reasonably expected now that it is
  coded, found by a reviewer or by the controller, the operator chooses
  between staying on the lane and moving to the standard route, which
  starts at `crucible:brainstorming` with the note and the existing diff
  as its incoming document, writing its spec into the lane's feature
  folder beside the note. On the move, the lane ledger is moved aside
  and the standard route's ledger links it as its predecessor
  (`crucible:subagent-driven-development` § Setup), so execution does
  not take it for another run's. The `Hatch:` ledger line and the rest
  of the hatch's procedure go. Basis: the umbrella's D3 and its entry
  (the line names the skill that runs next); the predecessor link,
  the controller's call during spec writing, departing from design
  part 2's presentation.
- **E10. The landing ask after the final pass.** The close readout, the
  landing ask, comes after the branch review's last full-scope pass, and
  the findings parked at triage are filed, as open items, before the
  workspace is deleted (`crucible:subagent-driven-development` § Finish,
  steps 2, 4 and 6). This child checks that the text already does both
  (A5) and changes it only where the check finds a gap. Basis: the
  umbrella's D6.
- **E11. The vocabulary list.** The labels, ledger lines and slots this
  child removes are listed in its landing and in the decision records'
  `## Changes` lines; the backlog's vocabulary point is trimmed to what
  stays. Basis: the umbrella's entry for `review-retirements`, kept by
  this child for its own removals.

## Constraints & invariants

- **I1. No finding is dropped silently.** Every finding the task loop
  or the branch review raises is fixed, ruled on with a recorded
  ruling, parked on the operator's answer, or left open to the close
  readout; every dismissed BLOCKER or MAJOR reaches the close readout
  with its ruling.
- **I2. The kept guards keep their function** (the umbrella's C3): the
  status check after each review seat, the independent read in its
  three cases, the snapshot line, each stop-and-ask line (the fix
  loop's after three waves, drift, the hatch), the seat-replacement
  line, and the carriage of `deferred-minor` entries.
- **I3. Every loop still terminates.** The task loop at three waves and
  the operator's answer; the branch review at its cap.
- **I4. Nothing states a retired mechanism as current.** After the
  branch, no shipped skill text, template, generated agent, test, live
  decision record, `docs/authoring.md`, `README.md` or `AGENTS.md`
  states one; a decision record may keep it as history. Frozen feature
  folders and the scanner's byte-exact corpus
  (`tests/claudeism_scanner_corpus/`) are exempt.

## Interfaces & boundaries

- **With `placement`.** Restatements that survive keep their number and
  place; only their content changes.
- **The ledger.** Fix-wave lines read `<W>/3`. A task is done when its
  latest `Task <N>` line under `## Progress` is a completion line, so a
  revert the operator rules (E3), recorded there as a `Task <N>` line
  naming the ruling, reopens it with no attempt number for the resume
  rule to read. The ledger's deferred list, the ambiguous-liveness
  BLOCKED line and the `Hatch:` line go; the
  predecessor link stays, used by a supersede and by the hatch (E9).
  Report paths keep the rule that each dispatch writes a path no earlier
  dispatch used, which a task run again after a revert follows with no
  attempt numbering.
- **Slot cards, templates and generated agents.** A slot removed or
  reshaped (E8's, the implementer card's fix-only and attempt rules,
  the report-path rules naming `-x<X>`) changes in its card and its
  template together, and `agents/` is regenerated.
- **A removed heading.** `crucible:subagent-driven-development`
  § Revert-and-replan goes; every citation of it changes in the same
  change, which the anchor test (`tests/test_references.py`) holds.
- **The umbrella on this branch.** A lightly held edit to its D4, by
  `skills/brainstorming/references/umbrellas.md` § Edits: a dispute on a
  diff the controller wrote also gets the independent read (E2). The
  entry's `landed` mark comes at Finish.

## Acceptance

- **A1. No retired mechanism stated.** One-time check: a
  case-insensitive search of `skills/`, `agents/`, `tests/` (the
  scanner's corpus excluded), `docs/decisions/`, `docs/authoring.md`,
  `README.md` and `AGENTS.md` for at least `pre-flight`,
  `cannot-verify`, `cannot verify`, `revert-and-replan`, `replanned`,
  `-x<X>`, `breaker`, `wave 4`, `waves 4`, `/5`, `routing table`,
  `routing-table`, `routed`, `T<N>`, `Routed deferred items`,
  `Lane Fit`, `EXCEEDS SHAPE`, `WITHIN SHAPE`, `Hatch:`,
  `ambiguous seat liveness`, `BRANCH_ONLY` and `Task Lines`, with the terms
  the plan names for each Decision's sites, finds only history in
  decision records, the kept one-line forms and senses unrelated to the
  retired mechanisms; the command and its output are recorded. No later
  change is planned that could undo it.
- **A2. The suite passes.** One-time at Finish: `python -m pytest
  tests/`, its summary line quoted with the skip count; the generated
  agents match their templates (the suite's check mode).
- **A3. The sizes.** One-time at Finish: the sum of
  `tests/prose-budget.txt` below 65,246 with the net stated, and the
  subagent-driven-development, redteaming and brainstorming `SKILL.md`
  files each no larger than at `10cd3f5` (46,563, 39,855 and 22,725
  bytes), by `git cat-file -s`.
- **A4. The paths walked.** One-time, by the controller, recorded in
  the branch review's records: for the task loop, inline mode, the
  very-small lane, the branch review and Finish, where a disputed
  finding, a finding open after the third wave, drift found after the
  fact, a deferral marker, a marked task's concern and a hatch trigger
  go, each ending at a stage that reads it or at the operator (I1, I3).
- **A5. The landing check.** One-time: the controller reads
  `crucible:subagent-driven-development` § Finish and
  `crucible:requesting-code-review` § The branch-review loop, and
  records whether the close readout follows the last full-scope pass
  and whether findings parked at triage are written to the open-items
  home before the workspace is deleted, on every route; a gap found is
  fixed on this branch.
- **A6. The backlog.** One-time: each item the umbrella's entry names
  for this child is resolved and deleted, or trimmed to what stays open,
  and the landing says which: `docs/backlog/implementer-dispute-channel.md`;
  the execution side of `docs/backlog/skill-text-rewrite.md` (the late
  mark, the breaker's sense of "load-bearing", the hatch naming no
  skill, the vocabulary point for this child's removals); and the
  bullet of `docs/backlog/umbrella-followups.md` on statements of what
  binds.

## Mechanism sketches

Advisory. One task per mechanism or close cluster, each across every
site that states it, its tests, generated agents and decision records
(each changed record taking its dated `## Changes` line): the fix loop
and drift (E1, E3); disputes (E2); the small retirements and the
snapshot line (E4); the shared-tree rules in both skills (E5, E6); the
deferral chain (E7); the mark (E8); the lane (E9); the landing check,
the backlog and the vocabulary (E10, E11, A5, A6). Each task lowers the
prose-budget lines it shrinks. The sites, by search: `crucible:subagent-driven-development`
and its templates, cards and references; `crucible:requesting-code-review`
and its template and card; `crucible:writing-plans`;
`crucible:redteaming`, `references/plan-phase.md`,
`references/folded-lane.md`, `references/flip-paths.md`,
`references/formats.md` and the seat card; `crucible:brainstorming` and
`references/folded-lane-document.md` and `references/umbrellas.md`;
`README.md`'s line on adjudication; and every decision record that
states them, by search — at least the task loop, adjudication, the
branch review, plans, routes, the shared tree, model roles and effort,
records and workspace, instruments, test rules, the spec, evidence and
findings, and the spec campaign.
