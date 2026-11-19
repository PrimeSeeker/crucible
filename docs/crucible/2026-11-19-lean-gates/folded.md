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

- G1. The cleanup wave stops taking wording in documents that instruct no
  agent.
- G2. A literal-reading finding no longer always costs a fresh seat.
- G3. An implementer whose change no test can see does not run the full
  suite for it.
- G4. A choice reaches the operator only where their answer could matter;
  the controller makes the rest and reports them.
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
- Landing asks, premise asks, `unstated break` asks, drift asks and the
  very-small lane's upgrade hatch.
- How the very-small lane is entered: the operator approves its note.
- How an umbrella's review is chosen
  (`skills/brainstorming/references/umbrellas.md`).
- A release: it follows the landing as its own step.

### Breaks

None. No path a session can reach today fails after this landing; what
changes is which choices wait for the operator, stated under Decisions.

### What is not measured

Whether fewer cleanup waves lose catches of the kind the two later-pass
MAJORs were, and whether the test of D4 withholds a choice the operator
needed. Acceptance A6 leaves a readout owed on the next features run on the
landed text.

## Decisions

Each is lightly held. D1, D2 and D5 are the operator's choices among options
the controller put; the rest are the controller's proposals the operator
accepted with the design.

- **D1. The cleanup wave takes what changes behaviour, a test, or text that
  instructs agents.** Of the minors and the CONFIRMED or RECOMMENDED leads a
  review leaves, the one cleanup wave per branch takes only those whose fix
  changes what the code does, what a test checks, or text that instructs
  agents (the kinds `crucible:writing-skills` names in its trigger). The
  rest stay listed in the close readout, unfixed. *Rationale:* the loop of
  later passes was fed by cleanup waves of document wording; narrowing what
  the wave takes removes waves without removing the pass that follows one,
  which found real defects. It withdraws part of the 2026-10-30 loosening,
  under which the controller could take any minor it judged worth fixing.
- **D2. The controller rules on a literal-reading finding.** A reviewer's
  finding that a binding item's literal reading reaches a case its author
  did not consider is ruled on by the controller, with its evidence, where
  the ruling leaves the binding text as it stands. A fresh adjudicator rules
  where the ruling would change the binding text, and, as today, on every
  dispute about a diff the controller wrote. Who rules on any other dispute
  is unchanged. The ruling passes the containment test as today. *Rationale:* 11 of 13 such findings were
  dismissed, and the branch reviewer already checks every ruling against the
  final code.
- **D3. An implementer runs the full suite only for a change a test can
  see.** Where its change touches no code, no test and nothing a test or
  check of the project reads, the implementer runs the checks that read what
  it changed in place of the full suite, and says so in its report.
  *Rationale:* full-suite runs after documentation-only commits were a
  generalization of a rule written for code.
- **D4. The test for an ask no skill names.** A choice that no skill names
  as a decision ask reaches the operator only where it does one of these:
  changes something observable in what the product does or a run produces;
  spends money outside the session, cannot be undone, or faces outward;
  changes the scope of the work; reverses something the operator ruled;
  changes a standing rule or sets aside a step a skill requires. Any other
  choice is the controller's: it makes the call and names it among its own
  calls in its next readout. An ask a skill names reaches the operator as
  that skill states. *Rationale:* the operator's input fell on product and
  scope choices and almost never on housekeeping; the fifth clause is the
  kind of housekeeping where it did.
- **D5. The route and the campaign's shape are the controller's calls.** The
  controller chooses the preset by the overturn question and states it, with
  its reasons, as it closes the design presentation; the operator may veto
  it like anything they are told, and their approval of the design carries
  it. The campaign's shape (seats, lenses, models, expected rounds) is
  stated when the campaign launches, and nothing waits for an approval of
  it. The very-small lane is still entered only by the operator's approval
  of its note. *Rationale:* 56 such asks, no departure. The stop rule
  already makes a further round the controller's judgment, and the terminal
  pass's stop check still sends a wrong stop to the operator.
- **D6. Leftover items are the controller's to keep or drop.** In the close
  readout the controller says which open items it keeps and which it drops,
  and why, as its call; the operator's answer to the readout may change any
  of them. *Rationale:* 29 such choices, one departure.
- **D7. The closing check reports what would change a conclusion.** The
  terminal pass's decision-ask fidelity mandate reports a mismatch only
  where it meets the existing `CONCLUSION-CHANGING` test, or where a call
  the record gives as the operator's ruling or choice was the controller's.
  Its template tells the seat that a lean toward the controller's own
  recommendation in asks and records is expected, and is reported only
  through those two kinds of correction. The bias line goes. *Rationale:*
  reporting every mismatch did not reduce the lean and rarely changed what
  happened; a call wrongly recorded as the operator's is kept because a
  decision recorded as firm is shielded from ordinary findings.
- **D8. The second read, and what the pass leaves open.** A second read runs
  after the pass's further fix wave or repair, and, record-only, where the
  controller puts a decision ask to the operator again; a reported
  correction by itself no longer causes one. Of what the pass or its second
  read leaves open, a MINOR against binding text becomes a scoped amendment
  the controller confirms where the containment test finds it contained, and
  a decision ask otherwise. *Rationale:* second reads of the artifact found
  no BLOCKER or MAJOR, while second reads of a close that put an ask again
  produced the conclusion-changing flags; a one-word minor against binding
  text waited hours for the operator because the allowance was spent.
- **D9. The premise line.** The design presentation states the observation
  the feature rests on and whether it was measured, and the spec's Intent
  records both. A measurement that fits a context-gathering probe runs
  before the design is presented; one that spends money outside the session
  or touches production is a decision ask. *Rationale:* a measurement taking
  minutes redirected work after it was built.

## Constraints & invariants

- **C1. A skill-named ask is never withheld by D4.** D4's test applies only
  to a choice no skill names as a decision ask. The asks this document
  changes are changed at their own sites, by D5, D6 and D8.
- **C2. The full-scope pass after every wave stays.** No decision here adds
  a condition under which a wave is not followed by one.
- **C3. Nothing converts a feature to a lighter route after step 4.** The
  fold and the lane are entered only at brainstorming's present-the-design
  step, through the route entry; the paths out of a preset stay the unfold,
  the late split and the upgrade hatch.
- **C4. The decision record keeps its vocabulary.** The statuses `open`,
  `accepted` and `firm` and the proposer forms stay as
  `crucible:brainstorming` § Workspace provisioning states them; the route
  entry and the campaign-shape entry are still written.
- **C5. Fixed names stay.** `second-read.md`, the report's
  `Record corrections: <N>` line, the `CONCLUSION-CHANGING` flag, the
  `literal-reading` label and the `Lane: very-small (operator-confirmed
  <date>)` line keep their spelling: other files and a test read them.
- **C6. The budgets hold.** `TOTAL_CAP` in `tests/test_prose_budget.py` is
  not raised; every `SKILL.md` stays at or under 18,000 characters; the
  SessionStart envelope stays under 10,000.
- **C7. Templates are edited at their sources.** A change to a seat template
  is made in its `.source.md` or a shared reference and rendered with
  `python tools/instrument_agents.py write`; `agents/` is never hand-edited.
- **C8. Skills stay runtime-neutral, and committed text carries no local
  context.** Figures about the project read are aggregate; its name, domain
  and content appear nowhere.

## Interfaces & boundaries

- **The route entry** in `brainstorm-decisions.md` is written at step 4 for
  every preset, as today. `skills/redteaming/SKILL.md` § The folded lane and
  `skills/redteaming/references/folded-lane.md` read it to enter the fold;
  after this change they name the entry, not an operator's confirmation.
- **The campaign-shape entry** in the same record is written when the
  campaign launches; `skills/redteaming/references/panels.md` § Launch reads
  it and names any departure in the campaign-start readout.
- **The terminal pass's report** keeps its three sections and its count
  line; the count is of corrections reported under D7.
  `skills/redteaming/references/plan-phase.md` and the round records read
  that line.
- **The close readout** (`skills/subagent-driven-development/references/finish.md`)
  still lists every open item with its source; step 4 still sends them as
  the operator's answer left them.

## Acceptance

- **A1.** `python -m pytest tests/` passes on the branch tip.
- **A2.** `python tools/instrument_agents.py check` passes: the rendered
  templates and `agents/` match their sources.
- **A3.** No shipped skill text still states a rule this document retires.
  Each of these searches of `skills/` finds a match on the base and none on
  the tip: `confirms or vetoes the preset`; `material or not`; `bias line`;
  `Wait for the operator` in `skills/brainstorming/SKILL.md`;
  `a literal-reading finding always does`.
- **A4.** `tests/prose-budget.txt` matches the tip's word counts, and the
  skills' total is at or under `TOTAL_CAP` as it stood on the base.
- **A5.** Each decision record whose position changed carries a dated line
  under `## Changes` saying what changed and why, and states the measured
  figures behind it as aggregates.
- **A6.** `docs/backlog/` holds an item for the readout owed: on the next
  features run on the landed text, the asks put to the operator per feature
  and the full-scope passes per branch, against the figures in Intent.
- **A7.** Each of D1 to D9 is stated at the sites the census names, in words
  that say what the decision says.

## Mechanism sketches

Advisory; an implementer may replace any of it.

- D4 fits `skills/using-crucible/SKILL.md` § Decision asks as one added
  paragraph of about seventy words; that section is always loaded, and the
  envelope has about 2,000 characters of headroom.
- D5 fits by rewording, not adding: the sentence in
  `skills/brainstorming/SKILL.md` § Proposing the arrangement that makes the
  preset the operator's, the closing paragraph of
  `skills/brainstorming/references/proposing-the-arrangement.md`, and
  § Campaign gate, which becomes the campaign's launch with no wait. The
  step keeps its place in the flow so later steps keep their numbers.
- D7 and D8 fit the terminal pass's source by cutting: "material or not"
  and the bias line go, and the record read's trigger narrows.
- The words D7, D8 and D5 cut should about pay for those D1, D3, D4 and D9
  add.

## Task dependency order

T1, T2, T3, T4, T5, strictly in this order: the tasks share a tree and some
files.

## File ownership + overlap census

| File | Task |
|---|---|
| `skills/requesting-code-review/SKILL.md` | T1 |
| `skills/subagent-driven-development/references/disputes-and-adjudication.md` | T1 |
| `skills/subagent-driven-development/SKILL.md` | T1 |
| `skills/subagent-driven-development/implementer-prompt.source.md`, and the files rendered from it | T1 |
| `docs/decisions/branch-review.md`, `docs/decisions/adjudication.md` | T1 |
| the decision record holding the implementer's test rules | T1 |
| `skills/using-crucible/SKILL.md` | T2 |
| `skills/brainstorming/references/proposing-the-arrangement.md` | T2 |
| `skills/redteaming/references/panels.md`, `skills/redteaming/references/folded-lane.md` | T2 |
| `skills/subagent-driven-development/references/finish.md` | T2 |
| `docs/decisions/operator-steering.md`, `docs/decisions/routes.md`, `docs/decisions/model-roles-and-effort.md`, `docs/decisions/publication.md` | T2 |
| `skills/redteaming/terminal-pass-prompt.source.md`, and the files rendered from it | T3 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | T3 |
| `skills/redteaming/references/plan-phase.md`, `skills/redteaming/references/round-record.md` | T3 |
| `docs/decisions/terminal-pass.md` | T3 |
| `docs/decisions/the-spec.md` | T4 |
| `docs/backlog/lean-gates-readout.md` (new) | T5 |

Overlaps, each ordered by the task order:

- `skills/brainstorming/SKILL.md`: T2 (§ Proposing the arrangement,
  § Campaign gate, the flow list, § The folded lane's opening clause), then
  T4 (§ Presenting the design, § Spec contract's Intent).
- `skills/redteaming/SKILL.md`: T2 (§ The folded lane), then T3 (§ Stop rule
  and terminal pass).
- `tests/prose-budget.txt`: each of T1 to T4 changes only the lines of the
  skill directories it edits, in its own commit, so the suite passes at
  every task.
- A decision record a task finds it must also touch, beyond those named, is
  logged in its Decision Log and reported.

## Inter-task contracts

- **The route entry's name.** T2 makes the fold's readers name "the route
  entry"; T3 does not restate how a route is entered.
- **Reported corrections.** T3 defines which corrections the pass reports.
  T2's D4 paragraph does not mention record corrections; a reported
  correction reaches the operator as `skills/redteaming/SKILL.md` § Stop
  rule and terminal pass states after T3.
- **The readout item.** T5 cites the figures of this document's Intent and
  names no file T1 to T4 created.

## Acceptance mapping

| Criterion | Check | Task |
|---|---|---|
| A1 | standing test: the suite | each task runs it; T5's run is on the tip |
| A2 | standing test: `tests/test_instrument_agents.py` | T1, T3 |
| A3 | one-time check: each search, failing on the base | T1 (`a literal-reading finding always does`), T2 (`confirms or vetoes the preset`, `Wait for the operator`), T3 (`material or not`, `bias line`) |
| A4 | standing test: `tests/test_prose_budget.py` | T1 to T4 |
| A5 | why-not a test: whether a line says what changed and why is prose only review can judge; `tests/test_decision_records.py` holds the section's presence | T1 to T4 |
| A6 | one-time check: the file exists and `git grep` finds no project name in it | T5 |
| A7 | why-not: prose fidelity, judged by the task reviews and the branch review | T1 to T4 |

## Task 1: The review loop

**Why.** D1, D2 and D3 are three narrowings of the execution reviews, each
at one site, with the records that explain them.

**Files.** `skills/requesting-code-review/SKILL.md` (§ The branch-review
loop: the cleanup wave, and the sentence on improvements);
`skills/subagent-driven-development/references/disputes-and-adjudication.md`;
`skills/subagent-driven-development/SKILL.md` (§ Disputes and adjudication,
if its trigger sentence needs it);
`skills/subagent-driven-development/implementer-prompt.source.md` and what
`python tools/instrument_agents.py write` renders from it;
`docs/decisions/branch-review.md`; `docs/decisions/adjudication.md`; the
decision record holding the implementer's test rules; the two lines of
`tests/prose-budget.txt`. Inputs: `.crucible/lean-gates/brainstorm-decisions.md`.
Consumers checked in the brainstorm: `skills/subagent-driven-development/references/very-small-lane.md`
runs the cleanup wave inline and restates no test of what it takes;
`skills/subagent-driven-development/references/finish.md` step 2 already has
the readout say why a cleanup wave left each item; the task reviewer's,
re-reviewer's and branch reviewer's sources name the `literal-reading` label
and are unchanged.

**Contract.** Enacts D1, D2, D3 under C2, C5, C6, C7. D2 leaves
`skills/redteaming/references/flip-paths.md` § The containment test as it is:
a ruling on a literal-reading finding still passes it.
- Deferred to implementation: which decision record takes D3's line, since
  none states the full-suite rule today.
- Deferred to implementation: whether D3's sentence sits in the implementer's
  source or in a shared section it splices.

**Acceptance.**
- Happy: the cleanup wave's paragraph states D1's three kinds and that the
  rest stay listed; the dispute rule sends a literal-reading finding to the
  controller unless its ruling changes binding text; the implementer's test
  paragraph states D3.
- Edge: a wave opened by a BLOCKER or MAJOR still takes trivial minors and
  FIX-IN-WAVE items as today; a lane diff's dispute still goes to the
  adjudicator; a change to a file a test reads, such as a skill in this
  repository, still gets the full suite.
- Error: the search `a literal-reading finding always does` over `skills/`
  matches on the base and not after the task.
- Integration: `python tools/instrument_agents.py check` and the suite pass;
  each of the three records has its `## Changes` line with the figures.

## Task 2: What reaches the operator

**Why.** D4, D5 and D6 decide which choices wait for the operator: one
general test for asks no skill names, and three named sites changed where
they stand.

**Files.** `skills/using-crucible/SKILL.md` (§ Decision asks);
`skills/brainstorming/SKILL.md` (§ Proposing the arrangement, § Campaign
gate, the flow list's step 8, § The folded lane's opening clause, the
Handoff where it names the gate);
`skills/brainstorming/references/proposing-the-arrangement.md`;
`skills/redteaming/references/panels.md` (round 1's swap, § Launch);
`skills/redteaming/references/folded-lane.md`; `skills/redteaming/SKILL.md`
(§ The folded lane); `skills/subagent-driven-development/references/finish.md`
(step 2's open-items line); `docs/decisions/operator-steering.md`;
`docs/decisions/routes.md`; `docs/decisions/model-roles-and-effort.md`;
`docs/decisions/publication.md` (its two mentions of the campaign gate); the
lines of `tests/prose-budget.txt` for the four skill directories. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `skills/redteaming/terminal-pass-prompt.source.md` excepts the
route and campaign-shape entries from its decision-record check already;
`skills/brainstorming/references/umbrellas.md` names "no campaign gate" for
an umbrella approved without a campaign and is re-read for the renamed step;
`skills/brainstorming/references/lane-note.md` and
`skills/subagent-driven-development/references/very-small-lane.md` keep the
lane's entry and its line (C3, C5).

**Contract.** Enacts D4, D5, D6 under C1, C3, C4, C6, C8. Produces the
wording "the route entry" that the fold's two readers use.
- Deferred to implementation: whether § Campaign gate keeps its heading or
  is renamed for the launch; either way step 8 keeps its number, and every
  site citing the heading follows.
- Deferred to implementation: the order of D4's five clauses.

**Acceptance.**
- Happy: § Decision asks carries D4's test and C1's limit; the preset is
  stated as the controller's call at the close of the design presentation;
  the campaign launches on a stated shape with no wait; the close readout
  gives the controller's keep-or-drop call per item.
- Edge: the very-small lane's note is still approved by the operator before
  it is written; a design with an open decision ask of its own still puts
  that ask; an umbrella approved without a campaign still lands as its
  reference says; a route entry is still written for the standard preset.
- Error: the searches `confirms or vetoes the preset` over `skills/` and
  `Wait for the operator` in `skills/brainstorming/SKILL.md` match on the
  base and not after the task.
- Integration: `tests/test_session_start.py`, `tests/test_router.py`,
  `tests/test_skill_size.py` and `tests/test_references.py` pass; the three
  records have their `## Changes` lines with the figures.

## Task 3: The closing check

**Why.** D7 and D8 change what the terminal pass reports, when a second read
runs, and where a minor against binding text goes.

**Files.** `skills/redteaming/terminal-pass-prompt.source.md` and what the
tool renders from it; `skills/redteaming/terminal-pass-prompt.slots.md`;
`skills/redteaming/SKILL.md` (§ Stop rule and terminal pass);
`skills/redteaming/references/plan-phase.md`;
`skills/redteaming/references/round-record.md` where it describes the
pass's outcome; `docs/decisions/terminal-pass.md`; the `redteaming` line of
`tests/prose-budget.txt`. Inputs: `.crucible/lean-gates/brainstorm-decisions.md`.
Consumers checked in the brainstorm: `tests/test_report_filenames.py` reads
`second-read.md` from the slot card and the layout (C5);
`skills/redteaming/references/round-readout.md` writes a record correction
that arrives after a round closed, and stays.

**Contract.** Enacts D7, D8 under C5, C6, C7. The stop check and the
decision-record check keep flagging `CONCLUSION-CHANGING` as today. A minor
against binding text takes
`skills/redteaming/references/flip-paths.md` § The containment test, which is
not edited.
- Deferred to implementation: the sentence telling the seat the lean is
  expected.

**Acceptance.**
- Happy: mandate 2 reports the two kinds of correction and no other; the
  report format has no bias line; § Stop rule and terminal pass states the
  second read's two triggers and the scoped amendment for a contained minor
  against binding text; the plan phase follows.
- Edge: a pass with no reported correction and no fix wave gets no second
  read; a pass whose further fix wave ran gets one with a re-read due; a
  correction naming a call wrongly given as the operator's is reported
  though it changes no conclusion.
- Error: the searches `material or not` and `bias line` over `skills/` match
  on the base and not after the task.
- Integration: `python tools/instrument_agents.py check`,
  `tests/test_report_filenames.py` and the suite pass; the record has its
  `## Changes` line with the figures.

## Task 4: The premise line

**Why.** D9 puts the observation a feature rests on, and whether it was
measured, in front of the operator and the campaign's seats.

**Files.** `skills/brainstorming/SKILL.md` (§ Presenting the design,
§ Spec contract's Intent); `docs/decisions/the-spec.md`; the `brainstorming`
line of `tests/prose-budget.txt`. Inputs:
`.crucible/lean-gates/brainstorm-decisions.md`. Consumers checked in the
brainstorm: `skills/brainstorming/references/lane-note.md` takes Intent "as
the spec contract states it", so the lane note inherits the line with no
edit; `skills/brainstorming/references/folded-lane-document.md` keeps all
six sections.

**Contract.** Enacts D9 under C6, C8. The probe it names is the one
§ Context gathering already permits.

**Acceptance.**
- Happy: the design presentation covers the observation and whether it was
  measured; Intent records both.
- Edge: a feature with nothing to measure says so in a clause; a measurement
  that spends money outside the session is put as a decision ask.
- Integration: `tests/test_skill_size.py` and the suite pass; the record has
  its `## Changes` line.

## Task 5: The readout owed

Review: branch only — it writes one backlog item in the shape of its
neighbours, builds no mechanism, and nothing depends on its wording.

**Why.** What this feature changes can only be measured on later sessions;
A6 leaves the readout owed where open work lives.

**Files.** `docs/backlog/lean-gates-readout.md` (new).

**Contract.** Enacts A6 under C8. Cites the Intent's figures for asks and
full-scope passes as the baseline.

**Acceptance.**
- Happy: the item has a title, an observation and a follow-up, and names
  what to count and against what.
- Error: `git grep` finds no name of the project read in it.
- Integration: the suite passes on the branch tip.
