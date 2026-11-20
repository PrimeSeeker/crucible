# Rulings before the close, the readout record, carried questions: combined spec and plan

Spec: this document. Intent through Acceptance bind as
`skills/subagent-driven-development/references/review-terms.md` § What binds
in a spec states; each task's Contract and Acceptance and the inter-task
contracts bind as `crucible:writing-plans` § Deferring detail states.

## Intent

### The problem

A controller's account of one feature on another project (Python, a
Claude-family controller on 0.33.1, the folded lane) listed places where the
spec campaign's text left it to improvise. This repository's lean-gates
campaign (2026-11-19) met two of them again. Three are taken here.

- **A ruling with no fix list left to ride.** An operator's ruling changes
  the artifact by riding a fix list
  (`skills/redteaming/references/fix-application.md`). Once the last numbered
  round's list is applied and verified, no text says how a ruling on that
  round's asks is applied, and
  `skills/redteaming/references/flip-paths.md` governs only from the
  campaign's close. Three campaigns are known to have met this, and each
  controller did something different: a second wave inside the closed
  round, with a verifier report under a name the record layout does not
  list; the ruling applied after the terminal pass, in its further wave, at
  the cost of a second full re-read; the same followed by a further numbered
  round.
- **The recorded readout was not the delivered one.** In both runs the
  controller wrote a shortened readout into the round record and sent the
  operator a fuller message. The terminal pass reads the record, so it
  reported omissions the delivered asks did not have, and its second read
  could not check the delivered text.
  `skills/redteaming/references/round-readout.md` already says to deliver the
  readout as recorded; `skills/redteaming/references/round-record.md` calls
  the recorded readout "compact".
- **A carried question in the seat's words only.** A seat's question
  doubting a firm decision reaches the operator quoted as written, with its
  ids. In the first run one such question needed translating, and no answer
  to it would have changed anything the document stated.

### What was measured

A script over the seat reports of one code project's campaigns since
2026-11-07, about 20 of them, found 11 fix passes around the terminal pass.
At least 2 carried an operator's ruling; a verifier's report does not always
say where an item came from, so that is a lower bound. With lean-gates that
makes three known cases, the three above. The second and third points rest
on two runs and on one run; neither was counted across those campaigns.

### Goals

- G1. A ruling that changes the artifact has a stated path at every point
  between the last numbered round and the campaign's close.
- G2. The terminal pass, where it can, reads the artifact after the rulings
  on the last round's asks, not before them.
- G3. The round record holds the readout the operator received.
- G4. The operator reads a carried question in plain words beside the
  seat's own, and is told when nothing in the artifact turns on it.

### Non-goals

- Sending a round's decision asks before its blind verifier returns: the
  order of the record's states stays. It would save the operator minutes and
  add a readout delivered in two parts, which G3 removes.
- The baseline run in a fresh worktree
  (`skills/subagent-driven-development/references/setup.md`): the operator
  kept it as it is, since a run in another checkout does not show that this
  worktree is set up.
- What the terminal pass reports: lean-gates narrowed it on 2026-11-19, and
  `docs/backlog/skill-rewrite-reaudit.md` holds the readout owed on it.
- Whether a doubt about the request, the Intent or a firm decision is
  carried, and that it is quoted as written: both stay (C2).
- The plan phase: its decision asks reach the operator in the close
  delivered after its terminal pass, so a ruling on one already goes by
  `flip-paths.md`.
- The very-small lane and SDD's close readout, which is a message and is
  not recorded.
- A check that a delivered message matches its record: no seat sees the
  message (`docs/decisions/operator-steering.md` § Rejected).
- A host's permission checker refusing a dispatch sent beside another tool
  call: not crucible's text.
- A release: it follows the landing as its own step.

### Breaks

None. No path a session can reach today fails after this landing. One thing
a session does today changes: with a decision ask of the last round
unanswered, the terminal pass no longer starts at once (D2).

### What is not measured

- How often a ruling arrives after the terminal pass is dispatched once D2
  holds, and what D1's unverified edit before the pass lets through.
- Whether the wording change of D3 stops controllers shortening the record:
  the existing rule already forbade it. Only a read of transcripts can show
  it; D5 asks for one.

## Decisions

Each is lightly held. All are the controller's proposals. The operator
approved the design they come from; D2 was put to them as a choice between
waiting and never waiting, twice, the second time with the hold retired on
2026-11-02 named, and they chose the wait. Two decisions differ from the
design as first approved, and the operator accepted both at the campaign
gate: D1's second case runs no blind verifier, where the design had the
change checked as any fix is; D4 keeps the quote in the readout and leaves a
question nothing turns on unanswered, where the design moved the quote to
the record and had the controller answer such a question.

- **D1. Where a ruling's change goes.** An operator's ruling that changes
  the artifact takes the first of these that applies.
  1. A numbered round's fix list is still to be written: it rides that list,
     as today.
  2. No such list remains and the terminal pass is not yet dispatched: the
     controller makes the change itself, held to what
     `fix-application.md` asks of any fix (fix altitude, the propagation
     sweep, the trace, a predicate run), commits it, and records under the
     last numbered round's `## Rulings and corrections` the ruling, the
     sites changed and the commit. No blind verifier runs on it: the
     terminal pass is then dispatched at the new revision as a full-scope
     re-read, and its decision-record check reads the ruling against the
     artifact.
  3. The terminal pass is dispatched and its one further fix wave is not yet
     applied: the change joins that wave's fix list, with the pass's own
     findings if it has any, and is verified and re-read as that wave is.
  4. Later than that: it goes as a change after the campaign's close does,
     by `flip-paths.md`.

  Under 2 or 3, a change that adds, removes or re-shapes a major mechanism
  is read by a further numbered round before the campaign goes on, to the
  terminal pass or to its second read, within the cap; where the cap is
  spent, it is the cap's decision ask. A premise ruling's change in a spec
  campaign goes the same way. *Rationale:* three controllers improvised
  three procedures. Round 0's fixes already run without a verifier because
  the next full-scope read checks them
  (`skills/redteaming/SKILL.md` § Round 0 — mechanical pre-pass); a ruling's
  change before the
  terminal pass is in the same position, and the pass also reads the ruling
  itself, which enters `brainstorm-decisions.md`, against the artifact. The
  path through the pass's further wave is what
  `skills/redteaming/SKILL.md` § Stop rule and terminal pass already gives a
  finding, so it needs no new record.
- **D2. The terminal pass waits for the last round's asks.** Before
  dispatching the terminal pass, where a round readout carries a decision
  ask that is unanswered and whose answer, in the controller's judgment,
  could change the artifact, the controller waits for the answer, and that
  round's readout says the pass waits. A premise ask holds nothing, as today, and neither does a carried
  question. *Rationale:* a pass that runs before the answer reads text that
  is about to change, and the change then costs a verifier and a second
  full re-read. It adds a pause of the kind `docs/decisions/spec-campaign.md`
  records as retired on 2026-11-02, when a pending premise ask stopped
  holding the campaign's stop: that hold could last as long as the operator
  took over the premise of the work, and its late ruling had the flip paths
  to go by. This one holds one dispatch, for an ordinary ask, and its late
  ruling had no path at all.
- **D3. The record holds the readout as delivered.** What the operator
  receives at a round's close or a campaign's is the recorded readout word
  for word, less its trace. The record's format no longer calls the
  readout compact. What a second read adds to a close is written into the
  recorded close before the close is delivered. *Rationale:* two
  controllers shortened the record, and the terminal pass then audited text
  the operator had not seen.
- **D4. A carried question is put in plain words beside the seat's.** A
  question doubting the request, what the Intent asks for or a firm decision
  is still always carried to the readout and still quoted as written with
  its id. The readout states it first in plain words, and where, in the
  controller's judgment, no answer to it would change the artifact, says
  so. A question so marked that the
  operator leaves unanswered is not seeded into the ledger at SDD's Setup.
  *Rationale:* the quote is there so the operator reads the seat's words
  and not the controller's account of them
  (`docs/decisions/evidence-and-findings.md`: before it, seat questions were
  answered 47 times, adopted 12 and carried never); a plain statement
  beside it costs the operator nothing of that, and the mark lets them pass
  over a question nothing turns on without the controller answering it for
  them.
- **D5. The item is closed and a readout is owed.**
  `docs/backlog/folded-run-process-gaps.md`, which this branch adds, is
  deleted: this document carries what it observed, and its remaining points
  are the non-goals above. `docs/backlog/skill-rewrite-reaudit.md` gains
  three things to read in later runs: whether a ruling after the last
  numbered round went by D1, and whether a change made under its second
  case left a defect a later stage caught; whether recorded readouts match
  the messages delivered; whether the operator answered a question marked
  under D4 with a change.

## Constraints & invariants

- **C1. A premise ask holds no gate.** It opens no wave, holds no stop and
  no dispatch, and its routes in
  `skills/redteaming/references/premise-asks.md` stay.
- **C2. A doubt is always carried, in the seat's words.** D4 adds to the
  readout's item; it removes neither the carrying nor the quote, and the
  three kinds of correction the terminal pass reports stay as they are.
- **C3. Fixed names and states stay.** The round directory's file names, the
  state line's tokens and their order, and the section title
  `## Rulings and corrections` are unchanged; no file name is added.
- **C4. The tail stays bounded.** After the terminal pass, at most one
  further fix wave and one second read.
- **C5. The blind verifier's input stays the fix list and the diff.**
- **C6. The budgets hold.** `TOTAL_CAP` in `tests/test_prose_budget.py` is
  not raised; every `SKILL.md` stays at or under 18,000 characters.
- **C7. Templates are edited at their sources.** A change to a seat
  template is made in its `.source.md` and rendered with
  `python tools/instrument_agents.py write`; `agents/` is never hand-edited.
- **C8. Skills stay runtime-neutral, and committed text carries no local
  context.** Figures about another project are aggregate; its name, domain
  and content appear nowhere.
- **C9. A decision record's existing `## Changes` lines stay.** A task adds
  a dated line; it edits none.

## Interfaces & boundaries

- **The last numbered round's `## Rulings and corrections`** holds, for a
  change under D1's second case, the dated ruling, the sites changed and the
  commit. Its readers: the terminal pass, which reads the round records for
  its stop check; a controller resuming after compaction, which compares the
  entry with the artifact before making the change again.
- **The terminal pass's stop check** counts a ruling's change made after the
  stop round as it counts that round's fix list: one that adds, removes or
  re-shapes a major mechanism, with no numbered round after it, is a
  mismatch.
- **The card's `fix-wave` selector** is `yes` also where a change under D1's
  second case followed the final round.
- **`brainstorm-decisions.md`** takes every operator ruling, as today
  (`skills/redteaming/references/formats.md`); the terminal pass's
  decision-record check reads it against the artifact, also as today.
- **The readout's carried-question item** is read by the terminal pass,
  whose report names a question missing from its readout or changed in
  meaning there; the plain statement is part of what it reads.
- **SDD's Setup** seeds carried questions the operator left unanswered; it
  reads D4's mark in the recorded readout to leave a marked one out.

## Acceptance

- **A1.** `python -m pytest tests/` passes on the branch tip.
- **A2.** `python tools/instrument_agents.py check` passes.
- **A3.** The search `to the operator, compact` over `skills/` finds a
  match on the base and none on the tip.
- **A4.** `tests/prose-budget.txt` matches the tip's word counts, and the
  skills' total is at or under `TOTAL_CAP` as it stood on the base.
- **A5.** Each decision record whose position changed carries a new dated
  line under `## Changes` saying what changed and why.
- **A6.** `docs/backlog/folded-run-process-gaps.md` is absent on the tip,
  and `docs/backlog/skill-rewrite-reaudit.md` asks for D5's three reads,
  naming no project.
- **A7.** Each of D1 to D4 is stated at the sites the census names, in
  words that say what the decision says.

## Mechanism sketches

Advisory; an implementer may replace any of it.

- D1's home is the last paragraph of
  `skills/redteaming/references/round-readout.md`, which a controller
  already reads when a ruling arrives after a round closed; § Stop rule and
  terminal pass points at it for the cases around the pass and carries D2's
  wait in a sentence.
- D3 is a deletion of "compact" and a few words on each of the two
  sentences that deliver a readout.
- D4 is a clause on one bullet of the readout's list and a clause on one
  bullet of Setup's seeding.
- The skills should grow by under 150 words in all; the base total is
  46,632 against a cap of 47,387.

## Task dependency order

T1, T2, T3, strictly in this order: the tasks share a tree and some files.

## File ownership + overlap census

| File | Task |
|---|---|
| `skills/redteaming/references/fix-application.md` | T1 |
| `skills/redteaming/references/premise-asks.md` | T1 |
| `skills/redteaming/terminal-pass-prompt.source.md`, and the files rendered from it | T1 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | T1 |
| `docs/decisions/spec-campaign.md`, `docs/decisions/terminal-pass.md` | T1 |
| `skills/subagent-driven-development/references/setup.md` | T2 |
| `docs/decisions/evidence-and-findings.md` | T2 |
| `docs/backlog/folded-run-process-gaps.md`, `docs/backlog/skill-rewrite-reaudit.md` | T3 |

Overlaps, each ordered by the task order:

- `skills/redteaming/SKILL.md`: T1 (§ Stop rule and terminal pass: the
  wait, the further wave, the cap's ask; § Inputs and state's Rehydration,
  if the entry of D1's second case needs a clause there), then T2 (the
  sentence of § Stop rule and terminal pass that delivers the close).
- `skills/redteaming/references/round-readout.md`: T1 (its last paragraph;
  the decision-asks bullet, for the line saying the pass waits), then T2
  (the carried-questions bullet, the sentence that records and delivers).
- `skills/redteaming/references/round-record.md`: T1 (what
  `## Rulings and corrections` holds; the terminal-pass record's sentence on
  when its fix list and verifier block appear), then T2 (field 8; the
  terminal-pass record's sentence on the close).
- `docs/decisions/fix-verification-and-merge.md`: T1 (rulings riding a fix
  list, and the change that runs without a verifier), then T2 (its Readout
  coverage position).
- `tests/prose-budget.txt`: T1 and T2 each change only the lines of the
  skill directories they edit, in their own commits, so the suite passes at
  every task.
- A decision record a task finds it must also touch, beyond those named, is
  logged in its Decision Log and reported.

## Inter-task contracts

- **D1's home.** T1 states D1 once and has every other site point at it; T2
  restates none of it.
- **The delivered close.** T1 leaves the sentences that record and deliver
  a readout or a close as they are; T2 owns them.
- **The item's deletion.** T3 deletes the backlog item; T1 and T2 cite this
  document for what was observed, never that file.

## Acceptance mapping

| Criterion | Check | Task |
|---|---|---|
| A1 | standing test: the suite | each task runs what the installed implementer template asks; T3's run is on the tip |
| A2 | standing test: `tests/test_instrument_agents.py` | T1 |
| A3 | one-time check: the search, failing on the base | T2 |
| A4 | standing test: `tests/test_prose_budget.py` | T1, T2 |
| A5 | why-not a test: whether a line says what changed and why is prose only review can judge; `tests/test_decision_records.py` holds the section's presence | T1, T2 |
| A6 | one-time check for the file's absence; why-not a test for the item's three reads, prose only review can judge | T3 |
| A7 | why-not: prose fidelity, judged by the task reviews and the branch review | T1, T2 |

## Task 1: A ruling's path, and the wait

**Why.** D1 and D2 give a ruling that changes the artifact a path at every
point of the campaign's tail, and put the terminal pass after the answers
it can wait for.

**Files.** `skills/redteaming/SKILL.md` (§ Stop rule and terminal pass;
§ Inputs and state's Rehydration paragraph if needed);
`skills/redteaming/references/round-readout.md` (its last paragraph; the
decision-asks bullet of its list, which closes with "nothing else", for the
line saying the pass waits);
`skills/redteaming/references/round-record.md` (the sentence on
`## Rulings and corrections`; the terminal-pass record's sentence on fields
6 and 7); `skills/redteaming/references/fix-application.md` (the sentence
listing what rides a fix list);
`skills/redteaming/references/premise-asks.md` (the ruling's route in a
spec campaign); `skills/redteaming/terminal-pass-prompt.source.md` (the
stop check) and what `python tools/instrument_agents.py write` renders from
it; `skills/redteaming/terminal-pass-prompt.slots.md` (the `fix-wave`
selector); `docs/decisions/spec-campaign.md` (its Stop rule and cap
position, and the reasoning on the hold retired on 2026-11-02);
`docs/decisions/terminal-pass.md` (the stop check and the tail);
`docs/decisions/fix-verification-and-merge.md` (what rides a fix list, and
which applies run a verifier); the `redteaming` line of
`tests/prose-budget.txt`. Inputs:
`.crucible/controller-process-gaps/brainstorm-decisions.md`. Consumers
checked in the brainstorm: `skills/redteaming/references/flip-paths.md`
starts at the campaign's close and is unchanged;
`skills/redteaming/references/plan-phase.md` has no numbered rounds and its
asks are delivered at its close; `skills/redteaming/references/folded-lane.md`
applies the spec campaign unchanged; `tests/test_report_filenames.py` reads
the round directory's layout, to which no name is added (C3).

**Contract.** Enacts D1 and D2 under C1, C3, C4, C5, C6, C7, C8, C9.
Produces the one statement of D1 that the other sites point at, and the
entry form of Interfaces & boundaries' first item.
- Deferred to implementation: whether the Rehydration paragraph needs a
  clause for an entry recorded with no commit beside it.

**Acceptance.**
- Happy: a controller with a ruling in hand finds, from
  § Stop rule and terminal pass or the readout reference, which of D1's four
  cases it is in and what to do; § Stop rule and terminal pass states the
  wait and that the readout says so; the stop check counts a ruling's
  change after the stop round.
- Edge: a ruling on a premise ask arriving before the terminal pass changes
  the artifact by D1's second case and held nothing meanwhile; a ruling
  that arrives while the pass is reading waits for the pass to return and
  joins its wave, the artifact frozen meanwhile; a ruling that keeps the
  decision changes nothing and opens nothing; a ruling's change that
  re-shapes a major mechanism at a spent cap is the cap's ask; a ruling
  arriving while a later numbered round is still to write its list rides
  that list and no wait applies.
- Error: an ask the controller judged could not change the artifact is
  answered with a change after the pass was dispatched: the third or fourth
  case takes it, and no text sends it back to the second.
- Integration: `python tools/instrument_agents.py check` and the suite pass;
  each of the three records has its new `## Changes` line; the record for
  D2 says what it adds back beside the hold retired on 2026-11-02.

## Task 2: The readout's record and its questions

**Why.** D3 makes the record the text the operator received; D4 changes how
that text puts a carried question.

**Files.** `skills/redteaming/references/round-readout.md` (the
carried-questions bullet; the sentence that records and delivers the
readout); `skills/redteaming/references/round-record.md` (field 8; the
terminal-pass record's sentence on the close);
`skills/redteaming/SKILL.md` (the sentence of § Stop rule and terminal pass
that delivers the close, its corrections added);
`skills/subagent-driven-development/references/setup.md` (the bullet
seeding what earlier phases left open);
`docs/decisions/fix-verification-and-merge.md` (its Readout coverage
position); `docs/decisions/evidence-and-findings.md` (its Questions
position); the `redteaming` and `subagent-driven-development` lines of
`tests/prose-budget.txt`. Inputs:
`.crucible/controller-process-gaps/brainstorm-decisions.md`. Consumers
checked in the brainstorm: the terminal pass's source still asks that each
carried question be quoted verbatim and reports one missing or changed in
meaning, and is unchanged; `docs/decisions/terminal-pass.md` states the same
and is unchanged; `skills/redteaming/references/merge-and-finding-hygiene.md`
keeps "always carried"; § Inputs and state's Rehydration paragraph already
has a resume deliver the recorded readout again;
`skills/redteaming/references/plan-phase.md` delivers its close as § Stop
rule and terminal pass states, so D3 reaches it through that sentence.

**Contract.** Enacts D3 and D4 under C2, C3, C6, C8, C9. Consumes T1's
edits to the three shared files without restating D1.

**Acceptance.**
- Happy: field 8 names the readout word for word as delivered and no longer
  "compact"; the carried-questions item asks for the plain statement, then
  the quote with its id, and the mark where no answer would change the
  artifact; Setup leaves a marked, unanswered question unseeded.
- Edge: round 0's questions, answered in its readout, follow the same item;
  a close to which a second read's corrections are added is recorded with
  them before it is delivered; a marked question the operator does answer
  is recorded as any ruling is; a carried question with no mark and no
  answer is still seeded.
- Error: the search `to the operator, compact` over `skills/` matches on
  the base and not after the task.
- Integration: the suite passes; each of the two records has its new
  `## Changes` line, the one for D4 keeping the 2026-10-30 reasoning for
  the quote.

## Task 3: The item and the readout owed

Review: branch only — it deletes one backlog item and adds a paragraph to
another, builds no mechanism, and nothing depends on its wording.

**Why.** D5 closes the item this branch brought and leaves the readout owed
where the next read of real runs will find it.

**Files.** `docs/backlog/folded-run-process-gaps.md` (deleted);
`docs/backlog/skill-rewrite-reaudit.md`.

**Contract.** Enacts D5 under C8.

**Acceptance.**
- Happy: the re-audit item asks for D5's three reads, each against what
  this document observed, and says only a read of transcripts can show the
  second.
- Edge: it names no project and gives aggregate figures only.
- Error: `docs/backlog/folded-run-process-gaps.md` exists on the base of
  the task and not after it.
- Integration: the suite passes on the tip.
