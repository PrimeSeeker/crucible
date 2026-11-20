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
  ids. In the first run one such question needed translating before the
  operator could answer it.

### What was measured

A script listed, in order, the seat dispatches of one code project's
campaigns since 2026-11-07, about 20 campaigns, and found 11 fix passes
around the terminal pass; each one's report was then searched for an item
naming an operator's ruling. At least 2 carried one; a verifier's report
does not always say where an item came from, so that is a lower bound. With
lean-gates that makes three known cases, the three above. The second and
third points rest on two runs and on one run; neither was counted across
those campaigns.

### Goals

- G1. A ruling that changes the artifact, arriving once the stop round's fix
  list has frozen, has a stated path up to the campaign's close.
- G2. The terminal pass reads the artifact after the rulings on the asks
  that were open when the campaign stopped, not before them.
- G3. The round record holds the readout the operator received.
- G4. The operator reads a carried question in plain words beside the
  seat's own.

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
- Telling the operator that nothing turns on a carried question, or
  answering such a question for them. The one case behind it asked how
  firmly a decision was held, which changes what binds; the judgment would
  be the controller's, on the doubts the carrying rule keeps from the
  controller; and no seat would check it.
- The plan phase. The three known cases were spec campaigns, and D1's
  further round has no counterpart in a phase that never loops. A ruling on
  its readout's ask that arrives before its terminal pass stays without a
  stated path; D5 asks later runs whether one occurs.
- What applies to a change after a campaign's close: D1 sends later rulings
  there and changes nothing in it. For an umbrella's own campaign, the
  stretch between its close and its landing has no stated path today, and
  gets none here.
- The very-small lane and SDD's close readout, which is a message and is
  not recorded.
- A check that a delivered message matches its record: no seat reads the
  operator's messages, and the terminal pass's check stops at the records.
- A host's permission checker refusing a dispatch sent beside another tool
  call: not crucible's text.
- A release: it follows the landing as its own step.

### Breaks

None. No path a session can reach today fails after this landing. Two
things a session does today change. With a decision ask unanswered whose
answer could change the artifact, the terminal pass no longer starts at once
(D2). A ruling that arrives once the terminal pass is dispatched waits for
the campaign's close, where a controller today might add it to the pass's
further wave; after the close a structural change takes a supersede, as
`flip-paths.md` has it (D1).

### What is not measured

- How often a ruling arrives after the terminal pass is dispatched once D2
  holds, and what D1's unverified edit before the pass lets through.
- Whether the wording change of D3 stops controllers shortening the record:
  the existing rule already forbade it. Only a read of transcripts can show
  it; D5 asks for one.

## Decisions

Each is lightly held. All are the controller's proposals, approved by the
operator with the design or at the campaign gate; they chose D2 over never
waiting. D4 is narrower than what they approved, which also marked a
question nothing turns on (Non-goals).

- **D1. Where a ruling's change goes.** In a spec campaign, an operator's
  ruling that changes the artifact goes by when it arrives.
  1. While a numbered round's fix list can still take it: it rides the next
     list to freeze, as today.
  2. Once the stop round's fix list has frozen: it waits for that round to
     close. Then, before the terminal pass is dispatched, the controller
     makes the change itself, held to what `fix-application.md` asks of any
     fix (fix altitude, the propagation sweep, the trace, a predicate run),
     checks that its commit's diff holds that change and nothing else, and
     records beside the ruling a line saying what the change does, the sites
     changed and the commit. The entry goes in the
     `## Rulings and corrections` that `round-readout.md` sends the ruling
     to: the round whose ask it answers, or the stop round's where it
     answers none. No blind verifier runs: the terminal pass is dispatched
     at the new revision, re-reads full-scope, and checks each such entry
     against the artifact. A change that adds, removes or re-shapes a major
     mechanism is first read by a further numbered round, within the cap;
     where the cap is spent, it is the cap's decision ask.
  3. From the terminal pass's dispatch on: the change waits for the
     campaign's close and is handled as a change after the close is. Until
     then its entry says the change is pending.

  A premise ruling's change takes these cases as any other ruling's does.
  *Rationale:* three controllers improvised three procedures. Round 0's
  fixes already run without a verifier because the next full-scope read
  checks them (`skills/redteaming/SKILL.md` § Round 0 — mechanical
  pre-pass); a change made before the terminal pass is in the same
  position, and the pass, which reads the round records, is given the entry
  to check. A ruling that comes after the dispatch has the path every
  change after the close has; applying it in the pass's further wave would
  need a second read that may already be spent, and one that re-shapes a
  major mechanism would need a round and a second pass that the record
  layout has no place for. D2 keeps ordinary asks out of that window. A
  premise ask holds nothing (C1), so its ruling can fall there, as
  `docs/decisions/spec-campaign.md` accepted on 2026-11-02.
- **D2. The terminal pass waits for the open asks.** When a round's readout
  finds the campaign stopped, the controller dispatches the terminal pass
  only once every decision ask a round readout of the campaign carries is
  answered, where the ask's answer, in the controller's judgment, could
  change the artifact. The stop round's readout says the pass waits and
  names each ask it waits for, an earlier round's included. An answer that
  defers the decision ends the wait for that ask, which stays open and
  travels on as today. A premise ask holds nothing, as today, and neither
  does a carried question. *Rationale:* a pass that runs before the answer
  reads text that is about to change. It adds a pause of the kind
  `docs/decisions/spec-campaign.md` records as retired on 2026-11-02, when a
  pending premise ask stopped holding the campaign's stop: that hold could
  last as long as the operator took over the premise of the work. This one
  holds one dispatch, for an ordinary ask, and any answer ends it.
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
  its id. The readout states it first in plain words. The terminal pass,
  which checks the quote today, also reads the plain statement: one that
  changes the question's meaning is a correction of the kind it already
  reports. *Rationale:* the quote is there so the operator reads the seat's
  words and not the controller's account of them
  (`docs/decisions/evidence-and-findings.md`: before it, seat questions were
  answered 47 times, adopted 12 and carried never); a plain statement
  beside it takes nothing of that away, and a check on it keeps the
  controller's account from standing in for the seat's.
- **D5. The item is closed and a readout is owed.**
  `docs/backlog/folded-run-process-gaps.md`, which this branch adds, is
  deleted; its remaining points are the non-goals above.
  `docs/backlog/skill-rewrite-reaudit.md` gains these things to read in
  later runs: whether a ruling arriving after the stop round went by D1,
  and whether a change made under its second case left a defect a later
  stage caught; whether recorded readouts match the messages delivered;
  whether a plan phase met a ruling between its readout and its terminal
  pass. It also keeps the item's one figure on the point lean-gates
  addressed, as a figure from before that change: on that run a terminal
  pass and its second read reported seven record corrections and no
  artifact finding, two default-role runs for a feature of about a hundred
  lines of code.

## Constraints & invariants

- **C1. A premise ask holds no gate.** It opens no wave and holds no stop
  and no dispatch, and it is carried as
  `skills/redteaming/references/premise-asks.md` states. Where its ruling's
  change goes in a spec campaign is D1's.
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

- **A ruling's entry under `## Rulings and corrections`** holds the dated
  ruling and, for a change under D1's second case, a line saying what the
  change does, the sites changed and the commit; for one under its third
  case, that the change is pending. Its readers: the terminal pass, below;
  a controller resuming after compaction, which compares the entry with the
  artifact before making the change again.
- **The terminal pass's stop check** counts a change an entry records as
  made after the stop round as it counts that round's fix list: one that
  adds, removes or re-shapes a major mechanism, with no numbered round
  after it, is a mismatch.
- **The terminal pass's decision-record check** reads each entry that
  records a change as made against the artifact: a change the artifact does
  not carry at a site the entry names is a correction flagged
  `CONCLUSION-CHANGING`. An entry marked pending is none.
- **The card's `fix-wave` selector** is `yes` also where a change under D1's
  second case followed the final round.
- **`brainstorm-decisions.md`** takes every operator ruling, as today
  (`skills/redteaming/references/formats.md`).
- **The readout's carried-question item** is read by the terminal pass,
  which checks the quote against the seat's report as today and the plain
  statement before it against the quote.

## Acceptance

- **A1.** `python -m pytest tests/` passes on the branch tip.
- **A2.** `python tools/instrument_agents.py check` passes.
- **A3.** The search `to the operator, compact` over `skills/` finds a
  match on the base and none on the tip.
- **A4.** The prose-budget test passes on the tip, and
  `tests/test_prose_budget.py` is unchanged from the base, so `TOTAL_CAP` is
  the base's.
- **A5.** Each decision record whose position changed carries a new dated
  line under `## Changes` saying what changed and why.
- **A6.** `docs/backlog/folded-run-process-gaps.md` is absent on the tip,
  and `docs/backlog/skill-rewrite-reaudit.md` asks for D5's reads and holds
  its figure, naming no project.
- **A7.** Each of D1 to D4 is stated at the sites the census names, in
  words that say what the decision says.

## Mechanism sketches

Advisory; an implementer may replace any of it.

- D1's home is the last paragraph of
  `skills/redteaming/references/round-readout.md`, which a controller
  already reads when a ruling arrives after a round closed; § Stop rule and
  terminal pass points at it and carries D2's wait in a sentence or two.
- The terminal pass's two added checks are a sentence each, in the stop
  check and the decision-record check of its source.
- D3 is a deletion of "compact" and a few words on each of the two
  sentences that deliver a readout.
- D4 is a clause on one bullet of the readout's list and a clause on the
  sentence of the pass's source that checks the quote.
- The skills should grow by under 150 words in all; the base total is
  46,632 against a cap of 47,387.

## Task dependency order

T1, T2, T3, strictly in this order: the tasks share a tree and some files.

## File ownership + overlap census

| File | Task |
|---|---|
| `skills/redteaming/references/fix-application.md` | T1 |
| `skills/redteaming/references/premise-asks.md` | T1 |
| `skills/redteaming/references/flip-paths.md` | T1 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | T1 |
| `docs/decisions/spec-campaign.md` | T1 |
| `docs/backlog/folded-run-process-gaps.md`, `docs/backlog/skill-rewrite-reaudit.md` | T3 |

Overlaps, each ordered by the task order:

- `skills/redteaming/SKILL.md`: T1 (§ Stop rule and terminal pass: the
  wait, when the pass re-reads full-scope, the cap's ask; § Inputs and
  state's Rehydration, as T1's deferral decides), then T2 (the sentence of
  § Stop rule and terminal pass that delivers the close).
- `skills/redteaming/references/round-readout.md`: T1 (its last paragraph;
  the decision-asks bullet, for the line saying the pass waits), then T2
  (the carried-questions bullet, the sentence that records and delivers).
- `skills/redteaming/references/round-record.md`: T1 (what
  `## Rulings and corrections` holds), then T2 (field 8; the terminal-pass
  record's sentence on the close).
- `skills/redteaming/terminal-pass-prompt.source.md`, and the files rendered
  from it: T1 (the stop check, the decision-record check), then T2 (the
  sentence of mandate 2 that checks a carried question's quote). Each runs
  `python tools/instrument_agents.py write` in its own commit.
- `docs/decisions/fix-verification-and-merge.md`: T1 (rulings riding a fix
  list, and the change that runs without a verifier), then T2 (its Readout
  coverage position).
- `docs/decisions/terminal-pass.md`: T1 (the stop check, the
  decision-record check), then T2 (its sentences on recording and
  delivering the close, and on the carried-question check).
- `docs/decisions/evidence-and-findings.md`: T1 (the 2026-11-02 passage
  saying where a later premise ruling goes), then T2 (its Questions
  position).
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
- **The pass's source.** T1 edits the stop check and the decision-record
  check and leaves mandate 2's sentence on carried questions as it is; T2
  edits that sentence and nothing T1 wrote.
- **The item's deletion.** T3 deletes the backlog item; T1 and T2 cite this
  document for what was observed, never that file.

## Acceptance mapping

| Criterion | Check | Task |
|---|---|---|
| A1 | standing test: the suite | each task runs what the installed implementer template asks; T3's run is on the tip |
| A2 | standing test: `tests/test_instrument_agents.py` | T1, T2 |
| A3 | one-time check: the search, failing on the base | T2 |
| A4 | standing test: `tests/test_prose_budget.py`, at T1 and T2; one-time check: `git diff 1f02fc9 -- tests/test_prose_budget.py` prints nothing | T2 |
| A5 | why-not a test: whether a line says what changed and why is prose only review can judge; `tests/test_decision_records.py` holds the section's presence | T1, T2 |
| A6 | one-time check for the file's absence; why-not a test for the item's reads and figure, prose only review can judge | T3 |
| A7 | why-not: prose fidelity, judged by the task reviews and the branch review | T1, T2 |

## Task 1: A ruling's path, and the wait

**Why.** D1 and D2 give a ruling that changes the artifact a path from the
stop round's frozen list to the campaign's close, and put the terminal pass
after the answers it can wait for.

**Files.** `skills/redteaming/SKILL.md` (§ Stop rule and terminal pass, its
sentence on when the pass re-reads full-scope and the cap's ask included;
§ Inputs and state's Rehydration paragraph, as the deferral below decides);
`skills/redteaming/references/round-readout.md` (its last paragraph; the
decision-asks bullet of its list, which closes with "nothing else", for the
line saying the pass waits);
`skills/redteaming/references/round-record.md` (the sentence on
`## Rulings and corrections`);
`skills/redteaming/references/fix-application.md` (the sentence listing
what rides a fix list; the sentence that dispatches the blind verifier
after every apply but round 0's);
`skills/redteaming/references/premise-asks.md` (the ruling's route in a
spec campaign); `skills/redteaming/references/flip-paths.md` (its sentence
on what corrects binding content before the campaign closes);
`skills/redteaming/terminal-pass-prompt.source.md` (the stop check, the
decision-record check) and what `python tools/instrument_agents.py write`
renders from it; `skills/redteaming/terminal-pass-prompt.slots.md` (the
`fix-wave` selector); `docs/decisions/spec-campaign.md` (its Stop rule and
cap position, and the reasoning on the hold retired on 2026-11-02);
`docs/decisions/terminal-pass.md` (the stop check, the decision-record
check); `docs/decisions/fix-verification-and-merge.md` (what rides a fix
list, and which applies run a verifier);
`docs/decisions/evidence-and-findings.md` (the 2026-11-02 passage saying
where a later premise ruling goes); the `redteaming` line of
`tests/prose-budget.txt`. Inputs:
`.crucible/controller-process-gaps/brainstorm-decisions.md`. Consumers
checked in the brainstorm: the stub of `skills/redteaming/SKILL.md` § Flip
paths starts at the campaign's close, where D1's third case hands over, and
is unchanged; the sentence of § Stop rule and terminal pass on the pass's
further wave is unchanged, since no ruling joins it;
`skills/redteaming/references/plan-phase.md` is out of scope (Non-goals);
`skills/redteaming/references/folded-lane.md` applies the spec campaign
unchanged; `tests/test_report_filenames.py` reads the round directory's
layout, to which no name is added (C3).

**Contract.** Enacts D1 and D2 under C1, C3, C4, C5, C6, C7, C8, C9.
Produces the one statement of D1 that the other sites point at, and the
entry form of Interfaces & boundaries' first item. Each text it adds to a
file the plan phase also reads (`round-readout.md`, `fix-application.md`)
says it applies to a spec campaign, so the plan phase gets no path from it.
- Deferred to implementation: whether the Rehydration paragraph needs a
  clause for an entry recorded with no commit beside it.

**Acceptance.**
- Happy: a controller with a ruling in hand finds, from § Stop rule and
  terminal pass or the readout reference, which of D1's three cases it is
  in and what to do; § Stop rule and terminal pass states the wait, what
  ends it and what the stop round's readout says; the pass's stop check
  and decision-record check read an entry's change.
- Edge: a ruling arriving after the stop round's list froze and before that
  round closed waits for the close and then goes by the second case; an
  ask of an earlier round still open at the stop holds the pass and is
  named in the stop round's readout; an answer that defers a decision ends
  the wait and changes nothing; a ruling on a premise ask arriving before
  the dispatch goes by the second case and held nothing meanwhile, and one
  arriving after it waits for the close; a ruling that keeps the decision
  changes nothing; a change under the second case that re-shapes a major
  mechanism at a spent cap is the cap's ask; a ruling arriving while a
  later numbered round can still take it rides that round's list, and no
  wait applies.
- Error: an ask the controller judged could not change the artifact is
  answered with a change after the pass was dispatched: its entry says
  pending, the pass reports nothing for it, and the change waits for the
  close; a change the controller recorded as made and did not land at a
  named site is a flagged correction of the pass.
- Integration: `python tools/instrument_agents.py check` and the suite pass;
  each of the four records has its new `## Changes` line; the record for
  D2 says what it adds back beside the hold retired on 2026-11-02.

## Task 2: The readout's record and its questions

**Why.** D3 makes the record the text the operator received; D4 changes how
that text puts a carried question, and has the terminal pass read the new
part.

**Files.** `skills/redteaming/references/round-readout.md` (the
carried-questions bullet; the sentence that records and delivers the
readout); `skills/redteaming/references/round-record.md` (field 8; the
terminal-pass record's sentence on the close);
`skills/redteaming/SKILL.md` (the sentence of § Stop rule and terminal pass
that delivers the close, its corrections added);
`skills/redteaming/terminal-pass-prompt.source.md` (the sentence of mandate
2 that checks a carried question's quote) and what
`python tools/instrument_agents.py write` renders from it;
`docs/decisions/fix-verification-and-merge.md` (its Readout coverage
position); `docs/decisions/terminal-pass.md` (its sentences on recording
and delivering the close, and on the carried-question check);
`docs/decisions/evidence-and-findings.md` (its Questions position); the
`redteaming` line of `tests/prose-budget.txt`. Inputs:
`.crucible/controller-process-gaps/brainstorm-decisions.md`. Consumers
checked in the brainstorm: the pass's list of the kinds it reports already
names a carried question "changed in meaning" in its readout, and is
unchanged; `skills/redteaming/references/merge-and-finding-hygiene.md`
keeps "always carried"; § Inputs and state's Rehydration paragraph already
has a resume deliver the recorded readout again;
`skills/redteaming/references/plan-phase.md` delivers its close as § Stop
rule and terminal pass states, so D3 reaches it through that sentence.

**Contract.** Enacts D3 and D4 under C2, C3, C6, C7, C8, C9. Consumes T1's
edits to the shared files without restating D1.

**Acceptance.**
- Happy: field 8 names the readout word for word as delivered and no longer
  "compact"; the carried-questions item asks for the plain statement, then
  the quote with its id; the pass's source has it read the plain statement
  against the quote.
- Edge: round 0's questions, answered in its readout, follow the same item;
  a close to which a second read's corrections are added is recorded with
  them before it is delivered; a carried question the operator leaves
  unanswered is still seeded into the ledger at SDD's Setup.
- Error: the search `to the operator, compact` over `skills/` matches on
  the base and not after the task; a plain statement that softens a seat's
  doubt is a correction the pass reports, the quote beside it exact or not.
- Integration: `python tools/instrument_agents.py check` and the suite
  pass; each of the three records has its new `## Changes` line, the one
  for D4 keeping the 2026-10-30 reasoning for the quote.

## Task 3: The item and the readout owed

Review: branch only — it deletes one backlog item and adds a paragraph to
another, builds no mechanism, and nothing depends on its wording.

**Why.** D5 closes the item this branch brought and leaves the readout owed
where the next read of real runs will find it.

**Files.** `docs/backlog/folded-run-process-gaps.md` (deleted);
`docs/backlog/skill-rewrite-reaudit.md`.

**Contract.** Enacts D5 under C8.

**Acceptance.**
- Happy: the re-audit item asks for D5's reads, each against what this
  document observed, says only a read of transcripts can show the second,
  and holds the figure D5 names as one from before lean-gates.
- Edge: it names no project and gives aggregate figures only.
- Error: `docs/backlog/folded-run-process-gaps.md` exists on the base of
  the task and not after it.
- Integration: the suite passes on the tip.
