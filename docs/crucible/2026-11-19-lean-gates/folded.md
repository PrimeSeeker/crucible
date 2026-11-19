# Lean gates: combined spec and plan

Spec: this document. Intent through Acceptance bind as
`skills/subagent-driven-development/references/review-terms.md` § What binds
in a spec states; each task's Contract and Acceptance and the inter-task
contracts bind as `crucible:writing-plans` § Deferring detail states.

## Intent

### The problem

A read of sixteen sessions of one code project on crucible 0.33.x, twelve
days of work, measured where review effort and the operator's attention
went. The figures below were counted in this feature's brainstorm, by script
over 640 seat reports and by reader seats over about 400 decisions put to
the operator. They are approximate and cannot be reproduced from this
repository: the transcripts are not in it.

- **Branch review.** Of 32 first full-scope passes, 5 raised a BLOCKER or
  MAJOR. About 35 later passes ran, about 28 of them after a wave that took
  only minors. Two of those 28 raised a MAJOR, each a defect of the branch
  the first pass had missed, neither introduced by the wave. A later pass
  therefore works as a second opinion on the branch, at about half the first
  pass's rate. What multiplied the later passes was the cleanup wave, opened
  for minors that were mostly wording in documents that instruct no agent.
- **Adjudication.** Of 16 adjudicator seats, 13 ruled on a literal-reading
  finding, and 11 of those 13 dismissed it.
- **The closing check.** 32 terminal-pass dispatches ran, 17 of them second
  reads. No second read found a BLOCKER or MAJOR in its artifact. The pass's
  record corrections recurred in nearly every campaign, leaned toward the
  controller's own recommendation, and did not become rarer over the twelve
  days. Of about 24 readouts reporting such corrections, two visibly changed
  what happened next. The corrections flagged `CONCLUSION-CHANGING` that the
  count found came from second reads of a close that put an ask again.
- **Decision asks.** Of about 400 decisions, 217 were about what the product
  does or about scope; the operator departed from the recommendation or
  raised something new on 45 of them. 121 were housekeeping; the operator
  did so on 4, three of which ruled on the process itself. The largest
  housekeeping group, 56, was the route, the campaign's shape and whether to
  run another round, with no departure. About 18 of the product decisions
  were internal choices nothing outside the code could observe.
- **Measurement after the build.** In at least two features a measurement
  taking minutes redirected the work, and it ran after the feature was built.

### Goals

- G1. The cleanup wave stops taking wording in a project's own working
  documents.
- G2. A literal-reading finding no longer always costs a fresh seat.
- G3. A change to documents alone does not get the full suite.
- G4. A choice reaches the operator only where their answer could matter;
  the controller makes the rest and says so.
- G5. The closing check reports what would change a conclusion and stops
  reporting the expected lean.
- G6. A design names the observation it rests on and whether that was
  measured, before the campaign.

### Non-goals

- The task review: of 109 in the read, 29 sent work back and 12 raised a
  MAJOR.
- The full-scope pass after every wave: `docs/decisions/branch-review.md`
  § A wave that changes no rule stands, and the count above supports it.
- The wave caps, and the asks a BLOCKER or MAJOR at a cap raises.
- Any ask, approval or consent a skill prescribes, beyond those D5, D6 and
  D7 change: landing asks, premise asks, `unstated break` asks, drift asks,
  the upgrade hatch, the brainstorm's own questions among them.
- How the very-small lane is entered: the operator approves its note.
- An umbrella's review choice, its Intent and its closing review's readout
  (`skills/brainstorming/references/umbrellas.md`).
- What becomes of a MINOR against binding text that the terminal pass's
  tail leaves open: it stays a decision ask.
- The tests a controller runs for a task it implements inline in the task
  loop: inline mode keeps a dispatched task's review, and its test rule with
  it.
- A release: it follows the landing as its own step.

### Breaks

None. No path a session can reach today fails after this landing; what
changes is which choices wait for the operator, stated under Decisions.

### What is not measured

- What the narrowed steps cost. The read counted what each step found, not
  its cost; reader seats noted full-scope passes at roughly 150,000 to
  400,000 tokens each and full-suite runs of about nine minutes.
- What every pass missed: the project read has not yet run end to end, so
  the catch counts have no ground truth behind them.
- Whether fewer cleanup waves lose catches of the kind the two later-pass
  MAJORs were, and whether D4's test withholds a choice the operator needed.
  Acceptance A6 leaves a readout owed on later features; it can show what
  the remaining passes caught and what the operator objected to, never a
  defect that a pass not run would have caught.

## Decisions

Each is lightly held. D1 and D2 are the operator's choices among options the
controller put, their wording since refined by the controller. D5 is the controller's proposal; the operator ruled for its
conditional stop, over no stop and over the stop as it stood. D7's
target is the operator's proposal, its conditions the controller's. The rest
are the controller's proposals.

- **D1. The cleanup wave does not take rewording of the project's own
  working documents.** Of the minors, the CONFIRMED or RECOMMENDED leads and
  the improvements a review leaves, the one cleanup wave per branch takes
  none whose fix only rewords or reformats one of the project's own working
  documents (decision records, backlog items, specs, plans, comments) and
  leaves what it states unchanged; the rule that trivial minors ride an open
  wave does not admit such a fix to the cleanup wave. Everything else it may
  take as today: a fix to code, to a test, to text that instructs agents, to
  documentation written for the product's users, and to a working document
  that states something false or lacks something a rule requires. What the
  wave leaves is listed in the close readout as any deferred minor is.
  *Rationale:* the loop of later passes was fed by cleanup waves of document
  wording; narrowing what the wave takes removes waves without removing the
  pass that follows one, which found real defects. It withdraws part of the
  2026-10-30 loosening, under which the controller could take any minor it
  judged worth fixing.
- **D2. The controller rules on a literal-reading finding.** A reviewer's
  finding that a binding item's literal reading reaches a case its author
  did not consider is the controller's to rule on, with its evidence. Two
  cases go to a fresh adjudicator instead: a finding on a diff the
  controller wrote (an inline task, Finish's open items, any lane diff), as
  every dispute about such a diff does today; and a finding on which the
  controller concludes that the binding text itself must change. Who rules
  on any other dispute is unchanged, and the ruling passes the containment
  test as today. *Rationale:* 11 of 13 such findings were dismissed. The
  branch reviewer checks every ruling of the task loop against the final
  code; a ruling made in the branch review, which no later pass reads,
  reaches the operator in the close readout with every other ruling the
  controller made.
- **D3. A change to documents alone does not get the full suite.** An
  implementer whose change touches only documents, files the product neither
  runs nor loads, runs in place of the full suite the tests and checks of
  the project that read those files, if any, and says so in its report. The
  same holds for the controller on the very-small lane, at its
  implementation and at each wave's fixes. Finish's run on the commit that
  lands is unchanged. *Rationale:* full-suite runs after documentation-only
  commits were a generalization of a rule written for code.
- **D4. The test for a choice no skill puts to the operator.** An ask,
  approval or consent that a skill prescribes, whatever the skill calls it,
  reaches the operator as that skill states. Any other choice the controller
  would put to them reaches them only where it does one of these: changes
  something observable in what the product does or outputs; spends
  money outside the session, cannot be undone, or faces outward; changes the
  scope of the work; reverses something the operator ruled; changes a
  standing rule or sets aside a step a skill requires. The rest are the
  controller's: it makes the call and states it, in a line, in its next
  message to the operator. A call that changes a decision the record holds
  is noted under that entry as the controller's, and is no approval. *Rationale:* the operator's input fell on product
  and scope choices and almost never on housekeeping; the fifth clause is
  the kind of housekeeping where it did. Saying the call in the next message
  needs no record to carry it and leaves the operator a prompt veto.
- **D5. The route and the campaign's shape are the controller's calls, and
  the campaign gate waits only for an ask.** The controller chooses the
  preset by the overturn question and states it, with its reasons and the
  campaign's shape (seats, lenses, models, expected rounds), as it closes
  the design presentation; the operator may veto either like anything they
  are told, and their approval of the design carries both. The campaign gate
  presents what it presents today (the record's decisions, its open decision
  asks, the shape) and says what changed in the spec since the design as the
  operator approved it, or since their last answer at the gate. It waits for
  the operator only where that message carries a decision ask: one the
  record holds open, or a change that D4's test sends to them. Otherwise the
  campaign launches. An umbrella's campaign passes the same gate. The
  very-small lane is still entered only by the operator's approval of its
  note. *Rationale:* 56 asks about the route, the shape or a further round
  drew no departure, which is also the rate a stop kept for a rare pivot
  would show. The gate therefore keeps its stop for a pivot the controller
  can see, a spec that changed or a decision still open, and gives it up for
  one only the operator could see, who is still told and may interrupt the
  round. The stop rule already makes a further round the controller's
  judgment, and the terminal pass's stop check still sends a wrong stop to
  the operator. It narrows the unconditional stop before the campaign that
  `docs/decisions/operator-steering.md` records the maintainer keeping "in
  case of something coming up".
- **D6. Leftover minors, leads and questions are the controller's to keep or
  drop.** In SDD's close readout the controller says which deferred minors,
  leads and `## Questions` items it keeps and which it drops, and why, as
  its call; the operator's answer to the readout may change any of them. A
  parked BLOCKER or MAJOR, an unruled premise ask and an open `unstated
  break` ask are listed as today and are never the controller's to drop.
  *Rationale:* 29 such choices, one departure.
- **D7. The closing check reports what would change a conclusion.** The
  terminal pass's decision-ask fidelity mandate, its stop check, its
  decision-record check and its Notes report a mismatch only where it is one
  of three kinds: one that meets the existing `CONCLUSION-CHANGING` test, or
  that the decision-record check flags today, an approval withdrawn with no
  record of it; a decision whose record misstates who made it or how firmly
  the operator holds it; a seat's question carried to readout that is
  missing there or changed in meaning. Its template tells the seat that a
  lean toward the controller's own recommendation in asks and records is
  expected, and is reported only through those kinds. In place of the bias
  line, the report closes its corrections with one line only where the pass
  finds the record materially misleading as a whole, saying in what way and
  naming the entries it rests on; that line is a decision ask, as the bias
  line's statement of it is today. The controller's duty not to shade a
  record stays; the pass reports a breach of it through those kinds and that
  line, and no longer as a pattern. The artifact re-read, the pass's other
  mandate, is unchanged. *Rationale:* reporting every mismatch did not
  reduce the lean and rarely changed what happened. A misrecorded decision
  is kept because a decision recorded as firm is shielded from ordinary
  findings, and one recorded as less is not; a dropped question is kept
  because nothing else carries a seat's doubt past the controller.
- **D8. The second read keeps its triggers.** It runs after the pass's
  further fix wave or repair, and, record-only, where the pass's report
  carries a correction or its line on a misleading record, or the controller
  puts a decision ask to the operator again. No trigger is cut: with D7
  fewer passes report a correction, so fewer second reads run.
  *Rationale:* a correction D7 still reports is one whose delivery matters,
  and nothing but the record-only read checks that the controller's close
  carries it.
- **D9. The premise line.** The design presentation states the observation
  the feature rests on and whether it was measured; a spec's Intent and a
  lane note's record both. A measurement that fits a context-gathering probe
  runs before the design is presented, and one that fails or settles nothing
  is reported as not measured; one that spends money outside the session or
  touches production is a decision ask. *Rationale:* a measurement taking
  minutes redirected work after it was built.

## Constraints & invariants

- **C1. D4 withholds nothing a skill prescribes.** An ask, approval or
  consent a skill prescribes reaches the operator as that skill states,
  whatever the skill calls it. The prescribed asks this document changes are
  changed at their own sites, by D5, D6 and D7.
- **C2. The full-scope pass after every wave stays.** No decision here adds
  a condition under which a wave is not followed by one.
- **C3. Nothing converts a feature to a lighter route after step 4.** The
  fold and the lane are entered only at brainstorming's present-the-design
  step, through the route entry; the paths out of a preset stay the unfold,
  the late split and the upgrade hatch.
- **C4. The decision record keeps its vocabulary.** The statuses `open`,
  `accepted` and `firm` and the proposer forms stay as
  `crucible:brainstorming` § Workspace provisioning states them; the route
  entry and the gate entry are still written, under those names, and record
  what the operator's approval of the design carried.
- **C5. Fixed names stay.** `second-read.md`, the report's
  `Record corrections: <N>` line, the `CONCLUSION-CHANGING` flag and its
  test, the `literal-reading` label, the `Lane: very-small
  (operator-confirmed <date>)` line and the heading `## Campaign gate` keep
  their spelling and meaning: other files, and for the first a test, read
  them.
- **C6. The budgets hold.** `TOTAL_CAP` in `tests/test_prose_budget.py` is
  not raised; every `SKILL.md` stays at or under 18,000 characters; the
  SessionStart envelope stays under 10,000.
- **C7. Templates are edited at their sources.** A change to a seat template
  is made in its `.source.md` and rendered with
  `python tools/instrument_agents.py write`; `agents/` is never hand-edited.
- **C8. Skills stay runtime-neutral, and committed text carries no local
  context.** Figures about the project read are aggregate; its name, domain
  and content appear nowhere.
- **C9. A decision record's existing `## Changes` lines stay.** A task adds
  a dated line; it edits none.

## Interfaces & boundaries

- **The route entry** in `brainstorm-decisions.md` is written at step 4 for
  every preset, as today. `skills/redteaming/SKILL.md` § The folded lane and
  `skills/redteaming/references/folded-lane.md` read it to enter the fold;
  after this change they name the entry, not an operator's confirmation.
- **The gate entry** in the same record is written at brainstorming's
  campaign gate, as today, from the shape the design presentation stated;
  `skills/redteaming/references/panels.md` (its Launch paragraph) reads it
  and names any departure in the campaign-start readout.
- **The terminal pass's report** keeps its three sections and its count
  line; the count is of corrections of D7's three kinds, and the line on a
  misleading record is not one of them.
  `skills/redteaming/references/plan-phase.md` and the plan record read the
  count line.
- **The close readout** (`skills/subagent-driven-development/references/finish.md`)
  lists open items with their sources as today; step 4 still sends the work
  as the operator's answer left it.

## Acceptance

- **A1.** `python -m pytest tests/` passes on the branch tip.
- **A2.** `python tools/instrument_agents.py check` passes: the rendered
  templates and `agents/` match their sources.
- **A3.** No shipped skill text still states a rule this document retires.
  Each of these searches of `skills/` finds a match on the base and none on
  the tip: `never yours to declare`; `material or not`; `bias line`;
  `a literal-reading finding always does`.
- **A4.** `tests/prose-budget.txt` matches the tip's word counts, and the
  skills' total is at or under `TOTAL_CAP` as it stood on the base.
- **A5.** Each decision record whose position changed carries a new dated
  line under `## Changes` saying what changed and why, and states the
  measured figures behind it as aggregates.
- **A6.** `docs/backlog/skill-rewrite-reaudit.md`, which already gathers
  what to read in the next real-code runs, also asks for: the share of
  decisions put to the operator that are housekeeping, against about 30% in
  the read; later full-scope passes per first pass, against about 1.1; any
  MAJOR a later pass raised; any choice the operator said they should have
  been asked; and any controller ruling on a literal-reading finding that a
  later pass or the operator reversed. It says what such a read cannot show.
- **A7.** Each of D1 to D9 is stated at the sites the census names, in words
  that say what the decision says.

## Mechanism sketches

Advisory; an implementer may replace any of it.

- D4 fits `skills/using-crucible/SKILL.md` § Decision asks as one added
  paragraph of about seventy words; that section is always loaded, and the
  envelope has about 2,000 characters of headroom.
- D5 fits mostly by rewording: the sentence in
  `skills/brainstorming/SKILL.md` § Proposing the arrangement that makes the
  preset the operator's, the sentence "The operator rules; present a close
  call as one" in `skills/brainstorming/references/proposing-the-arrangement.md`,
  and § Campaign gate, whose wait becomes conditional and whose re-gate loop
  stays for the case that waits.
- D7 fits the terminal pass's source by cutting: "material or not" and the
  bias line go.
- The words D7 and D5 cut should about pay for those D1, D3, D4 and D9 add.

## Task dependency order

T1, T2, T3, T4, T5, strictly in this order: the tasks share a tree and some
files.

## File ownership + overlap census

| File | Task |
|---|---|
| `skills/requesting-code-review/SKILL.md` | T1 |
| `skills/subagent-driven-development/references/disputes-and-adjudication.md` | T1 |
| `skills/subagent-driven-development/references/very-small-lane.md` | T1 |
| `skills/subagent-driven-development/SKILL.md` | T1 |
| `skills/subagent-driven-development/implementer-prompt.source.md`, and the files rendered from it | T1 |
| `docs/decisions/branch-review.md`, `docs/decisions/adjudication.md`, `docs/decisions/task-loop.md` | T1 |
| `skills/using-crucible/SKILL.md` | T2 |
| `skills/brainstorming/references/proposing-the-arrangement.md` | T2 |
| `skills/redteaming/references/panels.md`, `skills/redteaming/references/folded-lane.md` | T2 |
| `skills/subagent-driven-development/references/finish.md` | T2 |
| `docs/decisions/operator-steering.md`, `docs/decisions/routes.md`, `docs/decisions/records-and-workspace.md` | T2 |
| `README.md` | T2 |
| `skills/redteaming/terminal-pass-prompt.source.md`, and the files rendered from it | T3 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | T3 |
| `skills/redteaming/references/plan-phase.md`, `skills/redteaming/references/round-record.md` | T3 |
| `docs/decisions/terminal-pass.md` | T3 |
| `skills/brainstorming/references/lane-note.md` | T4 |
| `docs/decisions/the-spec.md` | T4 |
| `docs/backlog/skill-rewrite-reaudit.md` | T5 |

Overlaps, each ordered by the task order:

- `skills/brainstorming/SKILL.md`: T2 (the close of the Presenting the
  design passage, § Proposing the arrangement, § Campaign gate, § The folded
  lane's opening clause), then T4 (what the design presentation covers,
  § Spec contract's Intent).
- `skills/redteaming/SKILL.md`: T2 (§ The folded lane), then T3 (§ Stop rule
  and terminal pass, and § Operating stance if its sentence needs it).
- `docs/decisions/spec-campaign.md`: T1 (its Focused checks position, for
  D3), then T3 (its Operating stance reasoning, which names the bias line).
- `tests/prose-budget.txt`: each of T1 to T4 changes only the lines of the
  skill directories it edits, in its own commit, so the suite passes at
  every task.
- A decision record a task finds it must also touch, beyond those named, is
  logged in its Decision Log and reported.

## Inter-task contracts

- **The route entry's name.** T2 makes the fold's readers name "the route
  entry"; T3 does not restate how a route is entered.
- **`README.md` is T2's.** T2 rewords both of its sentences this document
  makes false: the one on who rules on disagreements, for T1's D2, and the
  one on confirming the arrangement, for D5.
- **Reported corrections.** T3 defines which corrections the pass reports
  and what its closing line is. T2's D4 paragraph does not mention record
  corrections; what the pass reports reaches the operator as
  `skills/redteaming/SKILL.md` § Stop rule and terminal pass states after
  T3.

## Acceptance mapping

| Criterion | Check | Task |
|---|---|---|
| A1 | standing test: the suite | each task runs it as the installed implementer template asks; T5's run is on the tip |
| A2 | standing test: `tests/test_instrument_agents.py` | T1, T3 |
| A3 | one-time check: each search, failing on the base | T1 (`a literal-reading finding always does`), T2 (`never yours to declare`), T3 (`material or not`, `bias line`) |
| A4 | standing test: `tests/test_prose_budget.py` | T1 to T4 |
| A5 | why-not a test: whether a line says what changed and why is prose only review can judge; `tests/test_decision_records.py` holds the section's presence | T1 to T4 |
| A6 | why-not a test: whether the item asks for the five things and names no project is prose only review can judge | T5 |
| A7 | why-not: prose fidelity, judged by the task reviews and the branch review | T1 to T4 |

## Task 1: The review loop

**Why.** D1, D2 and D3 are three narrowings of the execution reviews, with
the records that explain them.

**Files.** `skills/requesting-code-review/SKILL.md` (§ The branch-review
loop: the cleanup wave, the sentence on improvements, what rides the open
wave);
`skills/subagent-driven-development/references/disputes-and-adjudication.md`;
`skills/subagent-driven-development/SKILL.md` (§ Disputes and adjudication,
if its trigger sentence needs it);
`skills/subagent-driven-development/references/very-small-lane.md` (its
implementation step and its fix waves, which run the repository's gates);
`skills/subagent-driven-development/implementer-prompt.source.md` and what
`python tools/instrument_agents.py write` renders from it;
`docs/decisions/branch-review.md`; `docs/decisions/adjudication.md`;
`docs/decisions/task-loop.md` (its Task review position sends a
literal-reading finding to the adjudicator); `docs/decisions/spec-campaign.md`
(its Focused checks position states the implementer's full-suite rule); the
two lines of `tests/prose-budget.txt`. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `skills/subagent-driven-development/references/finish.md` step 2
already has the readout say why a cleanup wave left each item, and the
sentence of `skills/requesting-code-review/SKILL.md` that lists every minor
that rode no wave for the operator stays; the
task reviewer's, re-reviewer's and branch reviewer's sources name the
`literal-reading` label and are unchanged;
`docs/decisions/evidence-and-findings.md` points at `spec-campaign.md` for
which seats run the full suite and needs no edit.

**Contract.** Enacts D1, D2, D3 under C2, C5, C6, C7, C8, C9. D2 leaves
`skills/redteaming/references/flip-paths.md` § The containment test as it is:
a ruling on a literal-reading finding still passes it. D3's sentence goes in
the implementer's source, beside the full-suite sentence it qualifies, not in
a section another template splices.

**Acceptance.**
- Happy: the cleanup wave's paragraph states what D1 has it leave; the
  dispute rule gives a literal-reading finding to the controller, with D2's
  two cases for the adjudicator; the implementer's test paragraph and the
  lane's two gate sentences state D3.
- Edge: a wave opened by a BLOCKER or MAJOR still takes trivial minors and
  FIX-IN-WAVE items as today, and the cleanup wave takes none D1 excludes;
  an improvement to a working document's wording opens no cleanup wave,
  while a decision record missing a required line or stating a wrong
  position may be taken; a literal-reading finding on an inline task, on
  Finish's open items or on a lane diff goes to the adjudicator; a change to
  a skill in this repository, or to a prompt or configuration file the
  product loads, gets the full suite.
- Error: the search `a literal-reading finding always does` over `skills/`
  matches on the base and not after the task.
- Integration: `python tools/instrument_agents.py check` and the suite pass;
  each of the four records has its new `## Changes` line with the figures.

## Task 2: What reaches the operator

**Why.** D4, D5 and D6 decide which choices wait for the operator: one
general test for choices no skill puts to them, and the named sites changed
where they stand.

**Files.** `skills/using-crucible/SKILL.md` (§ Decision asks);
`skills/brainstorming/SKILL.md` (the close of the Presenting the design
passage, § Proposing the arrangement, § Campaign gate, § The folded lane's
opening clause);
`skills/brainstorming/references/proposing-the-arrangement.md`;
`skills/redteaming/references/panels.md` (round 1's swap, the Launch
paragraph); `skills/redteaming/references/folded-lane.md`;
`skills/redteaming/SKILL.md` (§ The folded lane);
`skills/subagent-driven-development/references/finish.md` (step 2's
open-items line); `docs/decisions/operator-steering.md` (its campaign-gate
position, the reasoning that kept the stop, and its Rejected entry);
`docs/decisions/routes.md`; `docs/decisions/records-and-workspace.md` (its
Finish position names a keep-or-drop proposal); `README.md` (the sentence on
who rules on disagreements, the sentence on confirming the arrangement); the
lines of `tests/prose-budget.txt` for the four skill directories. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `skills/redteaming/terminal-pass-prompt.source.md` excepts the
route and campaign-shape entries from its decision-record check already;
sites that cite the campaign gate by name
(`skills/brainstorming/references/umbrellas.md`,
`docs/decisions/spec-campaign.md`, `docs/decisions/model-roles-and-effort.md`,
`docs/decisions/publication.md`, § Spec contract's Persistence line) stay
true, since the heading and the entry keep their names (C5);
`skills/brainstorming/references/lane-note.md` and
`skills/subagent-driven-development/references/very-small-lane.md` keep the
lane's entry and its line (C3, C5).

**Contract.** Enacts D4, D5, D6 under C1, C3, C4, C5, C6, C8, C9. Produces
the wording "the route entry" that the fold's two readers use.
- Deferred to implementation: the order of D4's five clauses.

**Acceptance.**
- Happy: § Decision asks carries D4's test, its extent as C1 states it, and
  the line in the next message; the preset and the campaign's shape are
  stated as the controller's calls at the close of the design presentation;
  the campaign gate presents what it does today, says what changed, and
  waits only for an ask; the close readout gives the controller's
  keep-or-drop call for minors, leads and questions.
- Edge: the very-small lane's note is still approved by the operator before
  it is written, and the line saying so keeps its sense; a spec changed
  since approval in a way D4's test sends to the operator waits at the gate,
  and the amend-and-re-gate loop still serves it, measuring the next change
  from the operator's gate answer; an umbrella's campaign
  passes the same gate; an umbrella approved without a campaign still lands
  as its reference says; a route entry is still written for the standard
  preset; a parked BLOCKER, an unruled premise ask and an open `unstated
  break` ask are still listed and not the controller's to drop; a session
  with no feature in flight states a call of D4's in its next message.
- Error: the search `never yours to declare` over `skills/` matches on the
  base and not after the task.
- Integration: `tests/test_session_start.py`, `tests/test_router.py`,
  `tests/test_skill_size.py` and `tests/test_references.py` pass; the three
  records have their new `## Changes` lines with the figures, the
  operator-steering line saying what became of the stop before the campaign
  and on whose word.

## Task 3: The closing check

**Why.** D7 changes what the terminal pass reports; D8 keeps the second
read's triggers, which D7's wording must not narrow by accident.

**Files.** `skills/redteaming/terminal-pass-prompt.source.md` and what the
tool renders from it; `skills/redteaming/terminal-pass-prompt.slots.md`;
`skills/redteaming/SKILL.md` (§ Stop rule and terminal pass; § Operating
stance, if its sentence needs it);
`skills/redteaming/references/plan-phase.md`;
`skills/redteaming/references/round-record.md` where it describes the
pass's outcome; `docs/decisions/terminal-pass.md` (its positions on counted
corrections, the bias line and the second read, and the reasoning that kept
the materially-misleading trigger); `docs/decisions/spec-campaign.md` (its
Operating stance reasoning names the bias line as the instrument that
detects shading); the `redteaming` line of `tests/prose-budget.txt`. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `tests/test_report_filenames.py` reads `second-read.md` from the
slot card and the layout (C5);
`skills/redteaming/references/round-readout.md` writes a record correction
that arrives after a round closed, and stays.

**Contract.** Enacts D7, D8 under C5, C6, C7, C8, C9. The
`CONCLUSION-CHANGING` test is not changed, and the stop check and the
decision-record check flag as today, an approval withdrawn with no record
included; a mismatch of theirs that is none of D7's kinds is no longer
reported. The line on a misleading record is no
flagged correction and sits outside the count. § Operating stance keeps the
controller's duty not to shade a record; the records say which instrument
reports a breach of it after this change. What the pass's tail does with a
finding it leaves open is unchanged.
- Deferred to implementation: the sentence telling the seat the lean is
  expected.

**Acceptance.**
- Happy: mandate 2 reports the three kinds of correction and no other; the
  report format has no bias line and closes with the misleading-record line
  only where it applies, saying in what way and naming its entries; § Stop
  rule and terminal pass states that line as a decision ask and keeps the
  second read's triggers; the plan phase follows.
- Edge: a pass with no reported correction and no fix wave gets no second
  read; a pass whose further fix wave ran gets one with a re-read due; a
  pass reporting a correction of any of the three kinds gets a record-only
  read of the close; an operator's firm word recorded as `accepted` is
  reported; a carried question missing from its readout is reported, one
  reworded with its meaning intact is not; a leaning mismatch in Notes that
  is none of the three kinds is not reported.
- Error: the searches `material or not` and `bias line` over `skills/` match
  on the base and not after the task.
- Integration: `python tools/instrument_agents.py check`,
  `tests/test_report_filenames.py` and the suite pass; the two records have
  their new `## Changes` lines with the figures.

## Task 4: The premise line

**Why.** D9 puts the observation a feature rests on, and whether it was
measured, in front of the operator and the campaign's seats.

**Files.** `skills/brainstorming/SKILL.md` (what the design presentation
covers, § Spec contract's Intent);
`skills/brainstorming/references/lane-note.md` (its Intent part);
`docs/decisions/the-spec.md`; the `brainstorming` line of
`tests/prose-budget.txt`. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `skills/brainstorming/references/folded-lane-document.md` keeps
all six spec sections, so a folded document inherits the Intent's line.

**Contract.** Enacts D9 under C6, C8, C9. The probe it names is the one
§ Context gathering already permits. An umbrella's Intent is not changed.

**Acceptance.**
- Happy: the design presentation covers the observation and whether it was
  measured; a spec's Intent and a lane note's record both.
- Edge: a feature with nothing to measure says so in a clause; a measurement
  that spends money outside the session is put as a decision ask.
- Error: a probe that fails or settles nothing is reported as not measured,
  never as a measurement.
- Integration: `tests/test_skill_size.py` and the suite pass; the record has
  its new `## Changes` line.

## Task 5: The readout owed

Review: branch only — it adds paragraphs to one backlog item in the shape of
those already there, builds no mechanism, and nothing depends on its wording.

**Why.** What this feature changes can only be measured on later sessions;
A6 leaves the readout owed in the item that already gathers what to read in
the next real-code runs.

**Files.** `docs/backlog/skill-rewrite-reaudit.md`.

**Contract.** Enacts A6 under C8. States A6's five things to read and their
baselines from this document's Intent, and what such a read cannot show.

**Acceptance.**
- Happy: the item's Follow-up asks for each of the five and gives the two
  baselines.
- Edge: the item's existing paragraphs are unchanged.
- Error: the item names no project and gives only aggregate figures.
- Integration: the whole suite passes on the branch tip.
