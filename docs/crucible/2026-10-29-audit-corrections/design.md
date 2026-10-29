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

On the spec campaign's round-1 asks (the closing review a step rather
than a gate; the word target dropped):

> Agreed with the recommendations

On the round-2 ask (work left open written to a file in the feature
folder):

> I tentatively agree with a, but that would fail on a somewhat-planned
> no-commited-intermediaries route. Possibly this by default, overridable
> by instructions?

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
  restates the containment test without its newest exclusion.

The patterns behind the misses, from the trace: a fix wave created the
defect and nothing traced its consequences (6 of 10 clusters); findings
arrived after a batched landing approval and were handed over only in chat,
then lost when Finish deleted the ledger (4 of 10); reviewers read the
diff, not the unchanged text it contradicts (5 of 10); nothing read across
the children (5 of 10); the operator's approvals were in no reviewer's
inputs (4 of 10).

Separately, the operator finds finish too rigid: minors never open a wave,
although "in practice, I approve them anyway", and the flow
runs from the close readout through workspace deletion to a fixed
integration menu.

### Goals

1. Fix the correctness defects above.
2. Re-point the review stages at the patterns, without new seats in the
   feature's own route. The diff-only read is met at the plan stage
   (D17); the branch review already reads the whole branch.
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
- The plan pre-pass's goal check, which duplicates the coherence seat's:
  removing it would cost more template text than it saves, since a
  selector passage tests one value only.
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
  note's Intent stands for the spec's. For an umbrella's child, the
  request includes the effort's request its Request section quotes, and
  the umbrella's Intent is protected as the child's own is; the
  umbrella's § Edits keeps a child's edit to that Intent to corrections
  that leave what it asks for unchanged, and a ruled change to what it
  asks lands as a binding change by § Edits. Every other decision, accepted from
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
  improvement with no wave to ride is carried too). Round 0's questions,
  answered in its readout, follow the same rule.
- **D5 — A pending premise ask can hold the stop.** (M8.) Where upholding
  a pending premise ask would re-shape a major mechanism, the campaign's
  stop waits for its ruling. It still opens no fix wave, holds no cap and
  joins neither cap ask: at the cap it is put to the operator alone, as
  now.

### The arrangement text

- **D7 — One test for inline implementation.** (M5.) On the very-small
  lane the controller implements the change inline only where SDD
  § Inline mode's test holds, the change overdetermined and fitting its
  context; otherwise it dispatches the implementer, as the lane already
  permits. Inline mode's review clause does not apply on the lane, which
  has no task review; only its test does. The lane's context-only sentence
  goes, and the preset table's "inline by default" becomes "inline where
  overdetermined". The lane's fix waves stay inline, as the lane's own
  design, a cleanup wave's included. Rationale: the
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
  that section's two cases make it not plausible, it takes none" becomes
  keyed on the answer itself (where overturning is not reasonably
  expected, the reference's two usual cases or another stated reason),
  and qualified by "where one implementer can carry it". The unsupported
  reason "a campaign on a lane note, or a spec with no campaign" becomes
  "a spec is always campaigned, a note never is"; the note-with-a-plan
  reason keeps its text. The record's "no known
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
  the branch reviewer already reads. The redteam seat's, the terminal
  pass's and the branch reviewer's templates name that section; the task
  reviewer's and the implementer's do not, so the record's rejection of a premise mandate for
  task reviewers stands. For the branch reviewer, a consequential choice
  is one the code makes with no decision recording it.
- **D13 — Leads keep the task review's guards.** (M6, hm-3.) At the branch
  review, a lead the reviewer confirms as an intent or scope gap opens a
  wave whatever its staked severity, as in a task review; for a task that
  ran branch review only, it also fails that judgment. A pass that leaves
  a lead unruled is refused as missing a verdict, beside the existing
  rule for a missing task line.
- **D14 — Changes asked for ride a wave as changes, not findings.** (M4,
  at MINOR.) An adopted improvement, an operator's ruling and work the
  operator asked for each enter the wave's findings list labelled as
  such, carrying their own instruction: apply it or decline it
  with a reason, with no defect to confirm and no NOT CONFIRMED or
  adjudication. The implementer card's fix-wave reminder and the
  re-review card's findings slot name the label, so an applied
  improvement reaches the re-review, which checks it landed and broke
  nothing; neither template gains words. A declined improvement joins the
  work left open (D22).

### The review stages

- **D15 — Each fix item that adds or changes a rule is traced before its
  wave.** Before every spec-campaign or plan-phase fix list freezes, round
  0's, the terminal pass's follow-up wave and a plan-phase repair
  included, the controller runs
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
  record.** Its added check, on each `accepted` or `firm` entry whose
  decision the artifact states (process entries such as the route and
  the campaign shape aside): the entry still holds in the artifact, or a
  later entry, or a round readout naming the change and what it
  withdraws, records its change. It reports in its decision-ask fidelity
  part; an approval withdrawn with no such record is flagged
  `CONCLUSION-CHANGING`, so it reaches the operator. That would have
  caught the
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
  `accepted` status still covers it, and a decision record's basis reads
  it as the maintainer leaving the call to the agent, a form
  `docs/decisions/decision-records.md` already uses.

### Finish

- **D19 — The controller may run one cleanup wave.** Once the branch
  review has ended with no BLOCKER or MAJOR open, and a wave remains
  under the cap, the controller may open one cleanup wave of the minors,
  and the leads the reviewer ruled CONFIRMED or RECOMMENDED, that it
  judges worth fixing; a wave of improvements alone may open. Its ledger
  line marks it `cleanup`, so a resumed controller sees it spent. It runs
  as any wave: counted against the cap, its
  scoped re-review, then a full-scope pass. One per branch: minors the
  cleanup wave or its following pass raise open no other; a BLOCKER or
  MAJOR opens a normal wave, and one raised at the cap takes the existing
  escalation. The close readout names what was left and why. Minors still never open a wave by themselves. It runs wherever the
  branch-review loop runs, the very-small lane included (its fixes inline,
  as for any lane wave); standalone mode has no loop and no cleanup wave.
  Rationale: in the operator's words, "in practice, I approve them
  anyway"; the rule against minors opening waves
  came from one incident of fixes seeding fixes, which the one-per-branch
  limit still guards.
- **D20 — The close readout is the decision point.** It comes after the
  last full-scope pass and ends with the controller's recommendation, one
  of the options finishing offers on that branch (merge locally, open a
  pull request, keep the branch; no merge on a detached HEAD) or more
  work, and its reason, naming where the work left open went (D22). The controller waits for the answer; the workspace is
  deleted after it, at SDD's Finish, before finishing runs. Where the
  answer chooses an integration option,
  `crucible:finishing-a-development-branch` carries it out without
  presenting its menu again, and an answer that chooses none gets the
  menu with the recommendation; the menu is no longer
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
- **D21 — The readout's answer can reopen the loop.** (M3.) For a ruling
  given at the close readout, the wave flip-paths gives a ruling "in
  execution" is a wave of the branch-review loop, and Finish's existing
  restart rule follows it; one given during the task loop takes
  flip-paths' route at the next task boundary, as now. Neither rule is
  restated. A ruling that keeps the decision changes nothing and opens no
  wave. A request for more work opens a wave the same way where the work
  is what the spec and plan already require; new scope is a new feature,
  as finishing says now. Where the cap is spent, the operator's answer is
  the escalation's answer and may open the wave (C2). SDD Setup also seeds each open premise ask that the plan record
  or the spec campaign's close carried and the ledger lacks (wt-4), beside
  its two existing backstops.
- **D22 — Work left open goes to the feature folder, unless the
  project's instructions name another home.** At SDD's Finish, the work
  left open — minors, leads, questions, declined improvements, unruled
  asks, parked BLOCKER or MAJOR findings with their rulings, and the
  deferrals D23 brings — is written to `<feature-folder>/open-items.md`,
  each item with its source, and those the controller judges not worth
  keeping named dropped there; no item takes a ruling of its own, so "no
  ruling per minor" stands. It is committed on the branch beside the
  umbrella mark, before the suite, so the suite runs on the tree that
  lands, and any later change to it restarts Finish at the suite. No
  review reads it on a first pass through Finish: the close readout names
  it, and in this repository the controller checks the no-local-context
  rule on it itself; where the loop reopens, the branch reviewer takes
  that commit as in scope, as it takes the umbrella mark. Where the
  project's instructions name another home for deferred work, the items go
  there instead: an in-repository home on the branch as above, an outside
  tracker as the instructions say, which are the operator's word for it.
  A mode that commits no feature-folder files is such a case
  (`docs/backlog/records-retention-config.md`). No item is left only in
  the workspace, which is deleted after the operator's answer to the close
  readout, before finishing runs. Rationale: the operator's ruling at spec
  round 2, "Possibly this by default, overridable by instructions?"; it
  replaces filing into an unknown home, whose authorization and retention
  rules each round found holes in. It reverses two recorded positions:
  that no summary of a feature is committed (this is a list of open items,
  not a summary), and that filing open work is left to the operator or the
  repository's conventions.
- **D23 — A deferral is filed at the close of the phase that made it.** A
  disposition that sends work to a follow-up outside the feature (not
  `deferred-to-implementation`, which the plan routes) goes to D22's home
  at the close of the phase that made it, named in that close's readout:
  a brainstorm's or its spec campaign's at the campaign's close, and a
  plan phase's at its close, committed on the feature branch (Finish then
  adds to the same file); an umbrella's brainstorm's or campaign's at the
  umbrella's landing, in the umbrella's folder, before its workspace is
  deleted; execution's as a lead that reaches SDD's Finish. It never
  counts as done until it is filed or named dropped.
- **D24 — An umbrella gets one closing review, a step after its last
  landing, not a gate.** A review reads the children's landings, from the
  umbrella's own to the one that completed it, unrelated landings on a
  shared base aside, against the umbrella: its request, entries, Constraints and decisions.
  - **When.** Once the umbrella is complete by § Closing's existing rule
    (every entry `landed` or `dropped`, or `umbrella` with that umbrella
    closed). The controller whose landing completes it runs it right
    after, as its call, announced. Where that landing happens outside a
    session (a pull request merged later), the close readout of each child
    whose landing could complete the umbrella, siblings in flight counted,
    says the review is due once they have all landed, and the operator
    starts it by asking for it; the umbrella skill's § Closing review is
    its entry point. A nested
    umbrella's review runs at its own completion; where that completes
    its parent, the parent's runs after it, its range covering the nested
    one again.
  - **Seats.** Two or three controller-composed dispatches on the default
    role, each carrying the seven items of the dispatch composition,
    read-only, each with a lens that reads across children (request
    fidelity, the seams between children, a walkthrough of the workflows
    the effort changed)
    and its own report file; no new instrument or template. The width is
    the controller's call, announced.
  - **Its records.** A workspace under the umbrella's slug in the checkout
    the session works in, one of the workspace's ends in the formats
    reference's Lifecycle. Its readout to the operator lists each finding
    with where it goes: the incoming document of a fixes feature's
    brainstorm, which commits it in that feature's folder; D22's home,
    by default an `open-items.md` in the umbrella's folder committed on a
    branch of its own with a landing ask, only where something is left
    for it; or named dropped. A premise finding from it is a decision ask
    in that readout, its ruling entering the fixes feature's brainstorm
    record or the open items. The workspace is deleted once every finding has gone
    one of those ways.
  - **Closing is unchanged.** It is still read from the marks, and the
    review writes nothing into the umbrella; the umbrella is closed by
    then, so a fixes feature is a feature of its own.
  - An umbrella approved without a campaign gets it too, since it reads
    code the children wrote.

  Rationale: the operator asked "Might be worth a separate wider
  review?" and accepted the detailed proposal; a child's review grades
  against its own plan and would mix siblings' defects into its wave
  cap. At spec round 1 the operator accepted making it a step rather
  than a gate, which withdrew "before the umbrella is marked closed": a
  gate needed a recursive owner, a committed record and a landing ask
  per umbrella, where the step needs a landing ask only when findings are
  left with no fixes feature to carry them. It can be skipped where a landing happens outside a
  session and nobody acts on the readout. A seat on the other host is the
  operator's own instruction where it applies; the skills compose no such
  seat (`docs/backlog/second-runtime-seat.md`).

### Records and size

- **D25 — The campaign stop stays the controller's call.** The
  arrangements spec as approved at its digest gate made the campaign stop
  a downshift "the operator's to confirm" (its D13, with C4 "a downshift
  is never the controller's alone"); its round-0 fixes (`c271155`) made
  the stop the controller's judgment, and the change was never put to the
  operator. The operator has now confirmed it. Only the record changes:
  `docs/decisions/spec-campaign.md` states the confirmation.
- **D26 — The word delta is reported, not targeted.** The feature is
  expected to add roughly a thousand words of skill text, most of it in
  D19–D24; the cuts are the skill-text rewrite's. Each task reports its
  word delta, and the prose budget moves with the commits. D15–D17 and
  D22 also add a little work on every feature (a trace per fix item, one
  terminal-pass check, one pre-pass table, one filing commit), which word
  counts do not show; the decision records say so. The operator accepted
  dropping the earlier no-growth target at spec round 1.
- **D27 — The backlog edits come first.** One commit at the start of the
  branch edits the backlog items that take this feature's non-goals
  (§ Non-goals), with the audit's figures, so the deferrals are recorded
  before any work depends on them: D23 applied to this feature, whose
  repository's instructions name `docs/backlog/` as the home.

## Constraints & invariants

- **C1 — Integration stays the operator's decision.** No step lands,
  pushes, opens a pull request or discards work without the operator's
  answer.
- **C2 — Every wave the controller opens counts against the branch-review
  cap**, a cleanup wave and a ruling's wave included; the cap stays three,
  and a wave beyond it opens only on the operator's answer.
- **C3 — Nothing left open at a phase's close, SDD's Finish or an
  umbrella's closing review is silently discarded**: each item is filed
  or named dropped (D22–D24).
- **C4 — No outward action without the operator's word**: filing outside
  the repository is one.
- **C5 — No rule routes on a decision's proposer.**
- **C6 — The blind verifier's inputs gain nothing.**
- **C7 — Shipped skill text names no project-specific home for deferred
  work**: its default is the feature folder, which every project crucible
  runs in has, and a project's instructions may name another.
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
  definition); `skills/brainstorming/references/umbrellas.md` § Edits (the
  umbrella's Intent). The attribution uses of the proposer
  (`implementer-prompt.md`, `task-reviewer-prompt.md`, `code-reviewer.md`,
  `writing-plans`, `docs/decisions/decision-records.md`) stay.
- **D4, D18:** `skills/redteaming/SKILL.md` § Round readout and § Merge and
  finding hygiene (question dispositions); `skills/redteaming/references/formats.md`
  (question dispositions; the decision record's statuses);
  `skills/brainstorming/SKILL.md` § Workspace provisioning;
  `skills/redteaming/terminal-pass-prompt.md` where it checks readouts.
- **D5:** `skills/redteaming/SKILL.md` § Stop rule and terminal pass.
- **D17:** `skills/redteaming/seat-prompt.md` (the pre-pass worksheet);
  `skills/redteaming/references/plan-phase.md`, `folded-lane.md`.
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
  the consequential-choice clause's home); `terminal-pass-prompt.md`. The
  branch reviewer's slot
  card is at 2,991 of 3,000 characters: the wording belongs in the
  template.
- **D14:** `skills/requesting-code-review/SKILL.md` § The branch-review
  loop; `skills/subagent-driven-development/implementer-prompt.md`;
  `implementer-prompt.slots.md` (its fix-wave reminder) and
  `re-review-prompt.slots.md` (its findings slot); the templates are
  unchanged. Measured headroom: 53 and 136 characters.
- **D15, D16:** `skills/redteaming/SKILL.md` (fix application; terminal
  pass inputs); `terminal-pass-prompt.md` and its slot card;
  `skills/brainstorming/SKILL.md` § Spec self-review, read only;
  `docs/decisions/terminal-pass.md` (it lists the pass's inputs);
  `docs/decisions/decision-records.md` (D18's basis form).
- **D19–D23:** `skills/requesting-code-review/SKILL.md` (Minors, Questions
  and leads, the loop); `skills/subagent-driven-development/SKILL.md`
  § Setup and § Finish; `skills/finishing-a-development-branch/SKILL.md`
  (Step 4's menu and its rationalization rows);
  `skills/redteaming/references/flip-paths.md` § Premise findings (the
  ruling's route, carrying an open ask); `very-small-lane.md` step 4;
  `skills/redteaming/references/formats.md` § Lifecycle (deletion
  timing); `docs/decisions/records-and-workspace.md` (Finish's order and
  deletion, its "filing that work is left to the operator", and its
  "No committed summary"); `skills/redteaming/references/formats.md`
  § Feature folder (the files named by role gain `open-items.md`);
  `README.md` (its "deleted at finish", and § What it writes into your
  repository); `skills/requesting-code-review/code-reviewer.md` (the
  filing commit in scope, beside the umbrella mark);
  `skills/redteaming/SKILL.md` § Exit and `references/plan-phase.md`
  (D23 at a phase's close); `skills/brainstorming/references/umbrellas.md`
  § Landing (D23 at an umbrella's landing).
- **D24:** `skills/brainstorming/references/umbrellas.md` § Closing;
  `skills/redteaming/references/formats.md` § Lifecycle;
  `skills/subagent-driven-development/SKILL.md` § Finish (the close
  readout saying the review is due); `docs/decisions/umbrellas.md`;
  `docs/decisions/records-and-workspace.md`.
- **Generated:** `agents/` from the changed templates, by
  `python tools/instrument_agents.py write`.
- **Records** (each with a Changes line): `evidence-and-findings.md`,
  `the-spec.md`, `routes.md`, `spec-campaign.md`, `branch-review.md`
  (the rejection of minors opening waves revised by D19), `umbrellas.md`,
  `task-loop.md`, `terminal-pass.md`, `records-and-workspace.md`, and any
  other the plan's census finds.
- **Backlog** (D27): `docs/backlog/skill-text-rewrite.md`,
  `campaign-early-stop-investigation.md`, `decision-ask-framing.md`,
  `reviewer-research-reach.md`, and `records-retention-config.md` (its
  mode must say where open items go).

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
  readout (D26 sets no target, so the check reports rather than fails).
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
  mark and the open-items file, the suite, the close readout with the
  recommendation, the operator's answer, workspace deletion, then
  finishing; the cleanup wave sits in `requesting-code-review` beside
  § Minors.
- D24: a short § Closing review in `umbrellas.md`, after § Closing.

Deferred to implementation: the closing review's report file names
inside its workspace.
