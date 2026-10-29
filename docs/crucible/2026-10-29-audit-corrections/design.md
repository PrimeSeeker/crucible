# Audit corrections: premise scope, doubts, finish autonomy, the umbrella's closing review

## Request

The messages that asked for the work, quoted verbatim as evidence of what
was asked, not as the standard. The audit (2026-10-29):

> OK, before we're doing this, let's get back to the umbrella. Please,
> dispatch agents or set up a workflow to investigate misses,
> misalignments or harmonization/improvement opportunities that would
> fall under the umbrella. I'm interested in both the findings and meta:
> what "should have been" found during the development, but wasn't

The corrections, after the audit's report:

> Thanks (sorry about compaction, autocompaction-on-idle is not
> well-suited for investigations). Alright, let's plan corrections;
> backlog everything that doesn't fit.
> I think we also need to add/return more autonomy on finish: "minors
> don't launch a fix wave" is too restrictive (in practice, I approve them
> anyway), and apparently the skill railroads towards the merge very hard

Answering the proposed shape and two rulings (the premise scope, the
campaign stop):

> Note: in-repo backlog is not a universal pattern
>
> Agreed with the recommendations

On a proposed fix-list clause (whether a removing or merging resolution
exists):

> 4: Looks weak indeed, we'll need to restructure this somehow, probably
> later

On the umbrella's last child reviewing the whole effort:

> 6: Might be worth a separate wider review?

## Intent

### Problem

The hypothesis-specs umbrella (`docs/crucible/2026-10-28-hypothesis-specs/`)
shipped three features through the full process. Five fresh auditors read
the shipped tree blind to the review records, and two more traced each
finding back through the records. Of 23 distinct correctness findings, 11
had been raised during development and lost (6 dropped, 3 dismissed, 2
"fixed" into the defect) and 12 were never seen. The design-level findings
were mostly seen and deferred to the skill-text rewrite, whose backlog
item no commit of the effort updated.

The correctness defects this feature fixes:

- **The premise line keys on who proposed a decision.** The spec contract
  makes any decision not firm or marked lightly held, while the shared
  reference makes a finding against "a decision the operator made" an
  operator ask. Seats never see the proposer, the mislabel rule corrects
  one direction only, and the routing reverses a recorded decline: the
  operator declined recording who decided because such a mark invites
  deference (`docs/decisions/evidence-and-findings.md` § What the
  requirements leave unsaid).
- **Doubts stop at the controller.** A question can be dispositioned
  "carried to readout", but the round readout's closed list has no item
  for it, and a doubt about the Intent can be answered or rejected by the
  Intent's own author. Across the three features: 47 answered, 12
  adopted, 1 rejected, 0 carried.
- **A premise ruling in execution has no wave to land in.** It reaches the
  operator only in SDD's close readout, after the review loop ended; SDD
  Setup re-seeds two of the three items the plan phase hands on, not open
  premise asks.
- **A pending premise ask is exempt from the stop judgment**, a sentence
  written when the stop keyed on open BLOCKERs.
- **The very-small lane's inline test is looser than everywhere else**
  (context alone) while the lane's population widened.
- **Branch-reviewer parity is partial**: no "a binding item is itself
  wrong" finding and no consequential-choice clause; concerns that reach
  it as leads lose the task review's guards.
- **An adopted improvement rides a branch fix wave "as one of its
  findings"**, against the fixer's contract to confirm a defect.
- Smaller: a `Review: branch only` mark written in the plan review's last
  wave is graded by nobody; step 4 states the overturn selector absolutely
  and then overrides it; the overturn threshold reads "plausible" where the
  operator's criterion said "reasonably expect"; a decision record
  restates the containment test without its newest exclusion; the plan
  pre-pass owes a goal check the coherence seat already performs.

The patterns behind the misses, from the trace: a fix wave created the
defect and nothing traced its consequences (6 of 10 clusters); findings
arrived after a batched landing approval and were handed over only in chat,
then lost when Finish deleted the ledger (4 of 10); reviewers read the
diff, not the unchanged text it contradicts (5 of 10); nothing read across
the children (5 of 10); the operator's approvals were in no reviewer's
inputs (4 of 10).

Separately, the operator finds finish too rigid: minors never open a wave,
although the operator approves the cleanup wave every time, and the flow
runs from the close readout through workspace deletion to a fixed
integration menu.

### Goals

1. Fix the correctness defects above.
2. Re-point the review stages at the patterns, without new seats in the
   feature's own route.
3. Give the controller a cleanup wave of its own, and make the close
   readout the decision point it already is in practice, with the work left
   open handed over durably instead of through chat.
4. Give an umbrella a closing review across all its children.
5. Backlog what does not fit, as edits to the items that hold it.

### Non-goals

- The design-level findings (growth, separability, signal and vocabulary
  sprawl, the check on a check, the restated binding clause, the
  containment test's incident rules, the request block's copies): the
  skill-text rewrite's, filed there by this feature's backlog edit.
- Restructuring how a found tension gets closed by adding a distinction
  (the operator: "probably later"); filed with the rewrite.
- An outcome record for stopped campaigns, and a check that a readout was
  delivered: filed with their backlog items.
- Two findings that predate the effort (the folded lane's "requires a code
  baseline" claim; the very-small hatch naming no next skill): filed with
  the rewrite.
- Which review methods catch what: the audit's methods the effort's
  reviews never ran (a route walkthrough, a trace from the request, a
  design-smell read) and its comparison of seats by model (four seats on
  the other host, all in first rounds, so stage and model are
  confounded): research, filed with the reviewer-research item.

## Decisions

Every decision here is lightly held unless it says otherwise; none is
firm. Each names the audit finding it answers.

### Premise findings and questions

- **D1 — A premise finding protects the request, what the Intent asks for,
  and firm decisions; nothing else.** (M1.) On the very-small lane the lane
  note's Intent stands for the spec's. Every other decision, accepted from
  whoever proposed it, is lightly held, and a finding against it is
  ordinary; a binding item shown wrong (a Constraint, a mark) keeps the
  route it has now. The text separating findings by "who stands behind
  what you challenge" and "the chosen approach where the operator chose
  it" goes. Rationale: the classification becomes readable from the
  document itself (firm decisions say so in their rationale; the request
  and the Intent are sections), and it matches the operator's stance that
  an approval means "this until new evidence arrives" and the recorded
  decline of attribution as a deference trigger. Accepted, proposed by the
  controller.
- **D2 — The mislabel rule runs both ways.** The controller re-labels a
  finding by D1's test in either direction, its reason recorded with it:
  a `premise` label on an ordinary finding, and no label on a finding
  against the request, the Intent or a firm decision.
- **D3 — The proposer stays in the brainstorm decision record, for
  attribution only.** Decision records attribute each position's basis
  from its entry's proposer and status, as now; no routing reads it.
  The sentence in `docs/decisions/the-spec.md` saying each record entry
  names its proposer is clarified to mean the brainstorm decision record
  (cx-3: ruled so at binding-and-marks' review, the sentence left as
  written).
- **D4 — Doubts about the request, the Intent or a firm decision reach the
  operator.** (M2.) The round readout's list gains one item, the
  questions carried to readout, each quoted verbatim. A seat question that
  doubts the request, the Intent or a firm decision is always carried;
  every other question keeps its four dispositions, as now (an adopted
  improvement with no wave to ride is carried too).
- **D5 — A pending premise ask weighs in the overturn answer.** (M8.) It
  still holds no cap and opens no fix wave; but where upholding it would
  re-shape a major mechanism, overturning one after code stays reasonably
  expected, so the campaign does not stop on it.
- **D6 — The plan phase's mechanical pre-pass owes no goal check.**
  (hm-10.) The coherence seat performs it.

### The arrangement text

- **D7 — One inline test on every route.** (M5.) On the very-small lane the
  controller implements inline only where SDD § Inline mode's test holds,
  the change overdetermined and fitting its context; otherwise it
  dispatches the implementer, as the lane already permits. Inline mode's
  review clause does not apply on the lane, which has no task review; only
  its test does. The lane's context-only sentence goes. Rationale: the
  controller's own brainstorm argument for the widened lane relied on
  this safeguard, which a spec-round fix removed.
- **D8 — The overturn threshold uses the operator's words.** (rf-5.) The
  question asks whether overturning a major mechanism after code is
  **reasonably expected**, replacing "plausible", and the two cases before
  any review (no major mechanism; overdetermined) are the usual ones, not
  the only ones. The seat forecast line's wording follows. The README's
  "likely" already reads so, and the records then agree with the skills.
  Attribution: the operator's original criterion said "reasonably
  expect"; the umbrella the operator approved worded it "plausible"
  (its U3); this returns to the original words on the operator's
  agreement.
- **D9 — Step 4's selector stops contradicting itself.** (hm-7.) "where
  that section's two cases make it not plausible, it takes none" is
  qualified by "where one implementer can carry it"; the unsupported-combinations reason becomes
  "a spec is always campaigned, a note never is". The record's "no known
  use" for a note with a plan is corrected (the settled multi-task change
  is one). The wider separability question is the rewrite's.
- **D10 — A review mark is never written where no seat grades it.** (M7.)
  A `Review: branch only` mark is added only in an edit a seat with the
  mark mandate reads afterwards. In the edits no such seat reads — the
  last fix wave of the review that grades the plan, a terminal pass's
  follow-up wave, a plan-phase repair — no mark is added, and a seat
  question proposing one there is answered or carried, never adopted. The
  plan stays the one source SDD reads marks from, so execution needs no
  change.
- **D11 — The containment test is stated once.** (hm-2.)
  `docs/decisions/the-spec.md`'s restated list of exclusions becomes a
  pointer to `skills/redteaming/references/flip-paths.md` § The
  containment test.

### The branch review

- **D12 — Parity by moving the clauses to the shared reference.** (M6,
  rf-3.) "A binding item is itself wrong" and "a consequential choice taken
  for granted with no decision recording it" move from the redteam seat's
  template to a section of their own in `premise-and-questions.md`, which
  the branch reviewer already reads. The redteam seat's and the branch
  reviewer's templates name that section; the task reviewer's and the
  implementer's do not, so the record's rejection of a premise mandate for
  task reviewers stands.
- **D13 — Leads keep the task review's guards.** (M6, hm-3.) At the branch
  review, a lead the reviewer confirms as an intent or scope gap opens a
  wave whatever its staked severity, as in a task review; for a task that
  ran branch review only, it also fails that judgment. A pass that leaves
  a lead unruled is refused as missing a verdict, beside the existing
  rule for a missing task line.
- **D14 — An adopted improvement rides a wave as an improvement.** (M4, at
  MINOR.) Its fix-list entry is labelled an improvement; the fixer applies
  it or declines it with a reason, with no defect to confirm and no NOT
  CONFIRMED or adjudication; the re-reviewer checks it landed and broke
  nothing.

### The review stages

- **D15 — Each fix item that adds or changes a rule is traced before its
  wave.** Before every spec-campaign or plan-phase fix list freezes, round
  0's and the terminal pass's follow-up wave included, the controller runs
  brainstorming's self-review trace on each such item: who produces the
  rule's input, who reads its output, which routes and phases reach it.
  What the trace finds lands as sites in the item's existing restating-
  sites element, which the blind verifier already checks landed; no new
  record field. A seat's suggested wording is a proposal, traced like the
  controller's own. Execution's waves are excluded by choice: each is
  followed by a scoped re-review and, at the branch review, a full-scope
  pass, while a campaign's last wave is read only by the verifier and the
  terminal pass.
- **D16 — The spec campaign's terminal pass reads the brainstorm decision
  record.** Its added check: each `accepted` or `firm` entry still holds in
  the artifact, or a later entry, or a round readout naming the change and
  what it withdraws, records its change. That would have caught the
  inline-test reversal, and the stop-rule reversal as far as the records
  go: whether a recorded readout was delivered stays unchecked (a
  non-goal).
- **D17 — The pre-pass that covers a plan enumerates every set a change
  adds to.** The plan phase's pre-pass, and on the folded lane the round-0
  pre-pass that covers the plan half: for each set the plan adds a member
  to (a disposition, a seeded item, an exclusion, a route, a readout
  item), it lists each place that enumerates the set and that place's
  consumers. The controller's post-wave arithmetic re-run does not repeat
  it.
- **D18 — Attribution stays honest.** A question carried to a readout is
  quoted verbatim (D4). An operator answer leaving a call to the
  controller ("your call") is recorded as delegated to the controller,
  never as the operator's ruling or choice; the decision record's
  `accepted` status still covers it.

### Finish

- **D19 — The controller may run one cleanup wave.** Once the branch
  review has ended with no BLOCKER or MAJOR open, and the wave cap allows,
  the controller may open one cleanup wave of the minors and leads it
  judges worth fixing. It runs as any wave: counted against the cap, its
  scoped re-review, then a full-scope pass. One per branch: minors the
  cleanup wave or its following pass raise open no other; a BLOCKER or
  MAJOR opens a normal wave. The close readout names what was left and
  why. Minors still never open a wave by themselves. It runs wherever the
  branch-review loop runs, the very-small lane included (its fixes inline,
  as for any lane wave); standalone mode has no loop and no cleanup wave.
  Rationale: in the operator's words, "in practice, I approve them
  anyway"; the rule against minors opening waves
  came from one incident of fixes seeding fixes, which the one-per-branch
  limit still guards.
- **D20 — The close readout is the decision point.** It comes after the
  last full-scope pass and ends with the controller's recommendation (land,
  hold, or more work) and its reason. Where the operator's answer chooses
  an integration option, `crucible:finishing-a-development-branch` carries
  it out without presenting its menu again; the menu is no longer
  presented "exactly as written". Where loop activity follows the answer,
  the next readout reports what changed, and the earlier answer stands
  only where nothing new was left open. Integration stays the operator's
  decision. Finishing asks only what the operator's answer left open (the
  base branch where it is unconfirmed, whether the feature folder's files
  go into a pull request). Where no close readout precedes it (an
  umbrella's landing, a standalone review), finishing presents its options
  with a recommendation, which it does not do today; its rationalization
  rows that say "present the menu and wait" and "the menu is complete as
  written" change with it.
- **D21 — An operator ruling at the readout reopens the loop.** (M3.) A
  ruling on a premise ask, or a request for more work, opens a wave of the
  branch-review loop, counted against its cap, followed by a full-scope
  pass; Finish then restarts at step 1. At the cap the existing escalation
  applies. SDD Setup also seeds each open premise ask that the plan record
  or the spec campaign's close carried and the ledger lacks (wt-4), beside
  its two existing backstops.
- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, each item left open (a minor, a
  lead, a question, an unruled ask) is filed in the project's home for
  deferred work, or named as dropped in the readout. In the repository:
  filed as an edit committed on the branch beside the umbrella mark,
  before the suite, so the suite runs once on the tree that lands; like
  that mark it is read by no review, and the close readout names each
  item filed so the operator sees it. Outside the repository (an issue
  tracker): listed in the readout for filing, and filed only on the
  operator's word. No home known: the readout lists the items and
  proposes what to do. A later answer that asks for more work revises
  the filing when Finish restarts. The workspace is deleted once the
  operator's integration decision has been carried out. The other two
  ends of a workspace keep their rules: at an umbrella's landing an open
  premise ask already passes to the first child, and abandonment is the
  operator's call.
- **D23 — A deferral to a follow-up is a D22 filing.** A disposition that
  sends work to a follow-up, at any phase, names the item, and the item
  reaches the close readout's list of what was left open, where D22 files
  it; a deferral never counts as done until it is filed or named dropped.
- **D24 — An umbrella gets one closing review.** A review reads the whole
  range from the umbrella's landing to its last child's landing, against
  the umbrella: its request, entries, Constraints and decisions.
  - **Owner and moment.** The session whose landing leaves every entry
    marked runs it, once that landing is done: the last child's
    controller after its finish, or the session that landed a drop. A
    session resuming the effort that finds every entry marked and no
    closing-review line runs it then.
  - **Seats.** Two or three controller-composed dispatches, each carrying
    the seven items of the dispatch composition, read-only, each with a
    lens that reads across children (request fidelity, the seams between
    children, a walkthrough of the routes) and its own report file; no new
    instrument or template. The width is the controller's call, announced,
    with no approval gate.
  - **Where it runs.** A workspace provisioned under the umbrella's slug
    in the checkout the session works in; the closing review is one of
    the workspace's ends in the formats reference's Lifecycle, deleted
    when its findings have been filed or entered.
  - **What it leads to.** Its findings feed a fixes feature on whatever
    route fits, entered as a child of the umbrella, so the umbrella stays
    open until it lands; what is not fixed is filed or named dropped as
    D22 states. One per umbrella: a child entered from its findings does
    not trigger another.
  - **Closing.** An umbrella is closed when every entry is marked and its
    closing-review line is written: a new edit kind in the umbrella
    skill's § Edits, a line in the umbrella itself naming the date and
    the outcome, committed on the fixes child's branch, or, where nothing
    is to be fixed, on a branch of its own landed on the operator's
    go-ahead. This reverses the recorded position that closing takes no
    write of its own; "nothing is written upward" still holds, since the
    line is the umbrella's own. A nested umbrella runs its own at its
    close, and its parent's range covers it again. Umbrellas already
    closed when this lands stay closed.
  - An umbrella approved without a campaign gets it too, since it reads
    code the children wrote.

  Rationale: the operator asked for a separate, wider review rather than
  the last child's review widened; a child's review grades against its
  own plan and would mix siblings' defects into its wave cap. A seat on
  the other host is the operator's own instruction where it applies; the
  skills compose no such seat (`docs/backlog/second-runtime-seat.md`).

### Records and size

- **D25 — The campaign stop stays the controller's call.** The
  arrangements spec as approved at its digest gate made the campaign stop
  a downshift "the operator's to confirm" (its D13, with C4 "a downshift
  is never the controller's alone"); its round-0 fixes (`c271155`) made
  the stop the controller's judgment, and the change was never put to the
  operator. The operator has now confirmed it. Only the record changes:
  `docs/decisions/spec-campaign.md` states the confirmation.
- **D26 — No net growth in skill words, as a target.** Lightly held, not
  binding: sections D1–D14 are expected to remove more than they add, D15
  –D18 to add a little, D19–D24 to add the most. Each task reports its word
  delta; the prose budget moves with the commits.
- **D27 — The backlog edits come first.** One commit at the start of the
  branch edits the backlog items that take this feature's non-goals
  (§ Non-goals), with the audit's figures, so the deferrals are recorded
  before any work depends on them (D22's in-repository case applied to
  this feature).

## Constraints & invariants

- **C1 — Integration stays the operator's decision.** No step lands,
  pushes, opens a pull request or discards work without the operator's
  answer.
- **C2 — Every wave counts against the branch-review cap**, a cleanup wave
  and a ruling's wave included; the cap stays three.
- **C3 — Nothing left open at SDD's Finish or by an umbrella's closing
  review is silently discarded**: each item is filed or named dropped
  (D22, D24).
- **C4 — No outward action without the operator's word**: filing outside
  the repository is one.
- **C5 — No rule routes on a decision's proposer.**
- **C6 — The blind verifier's inputs gain nothing.**
- **C7 — Shipped skill text names no project-specific home for deferred
  work**: it refers to the project's own convention.
- **C8 — Each new or moved rule has one home**; other sites point to it.

## Interfaces & boundaries

The sites each part touches, found by search at `dd6897d`; the plan's
census is the authoritative list.

- **D1–D3:** `skills/subagent-driven-development/references/premise-and-questions.md`
  § Premise findings; `skills/redteaming/references/flip-paths.md`
  § Premise findings (the mislabel paragraph); `docs/decisions/evidence-and-findings.md`
  (its restatement of the premise definition and of who stands behind a
  decision, and the decline's Changes line); `docs/decisions/the-spec.md`
  (the proposer sentence, and its restatement of the premise
  definition). The attribution uses of the proposer
  (`implementer-prompt.md`, `task-reviewer-prompt.md`, `code-reviewer.md`,
  `writing-plans`, `docs/decisions/decision-records.md`) stay.
- **D4, D18:** `skills/redteaming/SKILL.md` § Round readout and § Merge and
  finding hygiene (question dispositions); `skills/redteaming/references/formats.md`
  (question dispositions; the decision record's statuses);
  `skills/brainstorming/SKILL.md` § Workspace provisioning;
  `skills/redteaming/terminal-pass-prompt.md` where it checks readouts.
- **D5:** `skills/redteaming/SKILL.md` § Stop rule and terminal pass.
- **D6, D17:** `skills/redteaming/seat-prompt.md` (the goal check and its
  report item, the pre-pass worksheet) and `seat-prompt.slots.md`;
  `skills/redteaming/references/plan-phase.md`, `folded-lane.md`;
  `premise-and-questions.md` § The goal check (its plan paragraph);
  `docs/decisions/evidence-and-findings.md` (its plan-phase goal-check
  sentence).
- **D7:** `skills/subagent-driven-development/references/very-small-lane.md`
  (What runs, step 2); `skills/brainstorming/SKILL.md` step 4 (the lane's
  dispatch clause); `skills/subagent-driven-development/SKILL.md`
  § Inline mode, read only; `docs/decisions/task-loop.md` and
  `routes.md` (their statements of the lane's inline test).
- **D8:** every site of the overturn wording: `premise-and-questions.md`
  § The arrangement questions, `brainstorming/SKILL.md` step 4,
  `redteaming/SKILL.md`, `formats.md`, `seat-prompt.md`,
  `terminal-pass-prompt.md`, `code-reviewer.md`, `very-small-lane.md`,
  `flip-paths.md`, `docs/decisions/routes.md`,
  `docs/decisions/spec-campaign.md`, `docs/decisions/umbrellas.md`,
  `README.md` (read only: its "likely" already agrees); the forecast
  line's two forms in `seat-prompt.md`, which `terminal-pass-prompt.md`
  and `formats.md` read.
- **D9:** `skills/brainstorming/SKILL.md` § Proposing the arrangement;
  `docs/decisions/routes.md`.
- **D10:** `skills/writing-plans/SKILL.md` (the review mark);
  `skills/redteaming/references/plan-phase.md`, `folded-lane.md`;
  `skills/redteaming/SKILL.md` § Merge and finding hygiene (an adopted
  question rides the wave); `flip-paths.md` (the late-mark exclusion
  beside it).
- **D11:** `docs/decisions/the-spec.md`.
- **D12, D13:** `premise-and-questions.md`; `skills/redteaming/seat-prompt.md`;
  `skills/requesting-code-review/code-reviewer.md` and `SKILL.md`;
  `docs/decisions/evidence-and-findings.md` (it names the seat template as
  the consequential-choice clause's home). The branch reviewer's slot
  card is at 2,991 of 3,000 characters: the wording belongs in the
  template.
- **D14:** `skills/requesting-code-review/SKILL.md` § The branch-review
  loop; `skills/subagent-driven-development/implementer-prompt.md`;
  `re-review-prompt.md`. The implementer's slot card is at 2,947 of 3,000
  characters: the wording belongs in the template.
- **D15, D16:** `skills/redteaming/SKILL.md` (fix application; terminal
  pass inputs); `terminal-pass-prompt.md` and its slot card;
  `skills/brainstorming/SKILL.md` § Spec self-review, read only;
  `docs/decisions/terminal-pass.md` (it lists the pass's inputs).
- **D19–D23:** `skills/requesting-code-review/SKILL.md` (Minors, Questions
  and leads, the loop); `skills/subagent-driven-development/SKILL.md`
  § Setup and § Finish; `skills/finishing-a-development-branch/SKILL.md`
  (Step 4's menu and its rationalization rows);
  `skills/redteaming/references/flip-paths.md` § Premise findings (the
  ruling's route, carrying an open ask); `very-small-lane.md` step 4;
  `skills/redteaming/references/formats.md` § Lifecycle (deletion
  timing); `docs/decisions/records-and-workspace.md` (Finish's order and
  deletion); `README.md` (its "deleted at finish").
- **D24:** `skills/brainstorming/references/umbrellas.md` § Edits,
  § Closing, § Resuming, § Landing and § Children;
  `skills/redteaming/references/formats.md` § Lifecycle;
  `skills/subagent-driven-development/SKILL.md` § Finish step 2, where the
  last mark is written; `docs/decisions/umbrellas.md` (its "closing takes
  no write of its own"); `docs/decisions/records-and-workspace.md`;
  `README.md` (when an umbrella closes).
- **Generated:** `agents/` from the changed templates, by
  `python tools/instrument_agents.py write`.
- **Records** (each with a Changes line): `evidence-and-findings.md`,
  `the-spec.md`, `routes.md`, `spec-campaign.md`, `branch-review.md`
  (the rejection of minors opening waves revised by D19), `umbrellas.md`,
  `task-loop.md`, `terminal-pass.md`, `records-and-workspace.md`, and any
  other the plan's census finds.
- **Backlog** (D27): `docs/backlog/skill-text-rewrite.md`,
  `campaign-early-stop-investigation.md`, `decision-ask-framing.md`,
  `reviewer-research-reach.md`.

## Acceptance

- **A1 — The suite passes on the branch's HEAD**, the prose budget, the
  claude-ism scanner and the agent generator's check among it: a standing
  test (`python -m pytest tests/`), its summary line quoted.
- **A2 — Routing on the proposer is gone:** one-time check, a search of
  `skills/` for "who stands behind", "where the operator chose it" and
  "only accepted from", returning hits before the change and none after.
- **A3 — No shipped skill names a project-specific home for deferred
  work (C7):** prose fidelity, judged by review; a search of `skills/` for
  `docs/backlog` already returns nothing today, so a one-time run of it
  could not fail and is no check.
- **A4 — "Plausible" no longer states the overturn threshold:** one-time
  check, a search of `skills/` and `docs/decisions/` for "plausib",
  every hit read against the round-0 census of the overturn wording:
  hits on that wording before the change, none on it after (the
  unrelated "plausibly" sites stay).
- **A5 — The word delta is reported:** one-time check, skill word counts at
  `dd6897d` against HEAD, from `tests/prose-budget.txt`, in the close
  readout (D26 is a target, so the check reports rather than fails).
- **A6 — Each decision lands where its Interfaces entry says, with no new
  contradiction:** prose fidelity, which only review can judge (task
  reviews and the branch review); no test.

## Mechanism sketches

Advisory; the plan and implementers may replace them.

- D1: § Premise findings shrinks to the three protected items, the lane's
  Intent, and the literal-reading label; the paragraph on who stands
  behind a decision becomes one sentence: everything else is lightly held
  and a finding against it is ordinary.
- D4: the readout item could read "the questions carried to readout,
  verbatim, each with what it doubts"; the disposition rule gains one
  sentence in § Merge conservation.
- D10: one sentence in `writing-plans` beside "graded by the review that
  grades the plan", and one in the adopted-question rule.
- D14: a fix-list label such as `Improvement:`; one sentence each in the
  implementer and re-review templates' fix-wave passages.
- D19–D22: the Finish order could become record checks, the umbrella
  mark and the in-repository filing, the suite, the close readout with the
  recommendation, then the integration step, then workspace deletion;
  the cleanup wave sits in `requesting-code-review` beside § Minors.
- D24: a short § Closing review in `umbrellas.md`.

Deferred to implementation: the closing review's report file names
inside its workspace, and the wording of the closing-review line.
