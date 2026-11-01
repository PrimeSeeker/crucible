# Review retirements: the campaign side of the skill text rewrite

Umbrella: `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`

## Intent

**Problem.** The umbrella's audit found campaign mechanisms that catch
little or never ran, and three structural failures (the umbrella's
Intent holds the figures). Its entry for this child lists the campaign
side of what goes: merge conservation, the re-seat line counts, the
design digest, `[LOAD-BEARING]` marks, premise findings, the
directional-bias statement's apparatus, the containment test's
incident exclusions, the goal check outside round 1 and the branch
review, large fix lists, decision asks buried in readout bodies, and a
round-0 inconsistency that predates the audit.

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

- The execution side of the umbrella's D3, D4 and D6
  (`execution-retirements`): the tree check, the seat-replacement gate,
  the pre-flight scan, the task review's cannot-verify items, snapshot
  blessing, adjudication, revert-and-replan, the fix ladder and breaker,
  Lane Fit and the upgrade hatch, the deferral chain and
  `Review: branch only`, the landing ask after the final pass.
- Consolidating existing restatements into one owner text
  (`placement`): where this child edits a restatement, it changes its
  content only.
- New mechanisms beyond the three this child needs: the round-1
  outside-the-frame lens, the `deferred-minor` disposition and the
  second read's record-only run.

## Decisions

All lightly held. Each names its basis; record numbers are entries of
the brainstorm decision record.

- **R1. Merge conservation retired.** The script
  `skills/redteaming/scripts/conserve.py`, its tests and helper, the
  parts of other tests that load it or name it as their reader, the
  round record's `conservation:` line and the rules that run or read it
  go. A merged entry keeps its `origins:` element, which the terminal
  pass reads to find the findings behind each decision ask, and every
  seat question keeps its disposition. Seat ids stay unique within a
  round, since a replacement seat writes to a fresh report path; the
  feature-wide rule and its plan-phase `p0` exception, which served the
  conservation check, go. Nothing mechanical checks the merge. No
  workflow step then runs Python, so the README's Python requirement and
  the Python-floor reasoning tied to the script go. Basis: the
  umbrella's D3.
- **R2. Small fix lists; MINORs deferred to the branch review.** A fix
  list — a numbered round's, the plan phase's, the spec terminal pass's
  follow-up wave's — and the plan phase's terminal-pass repair take
  BLOCKER and MAJOR findings and MINOR findings against binding text: a
  MINOR whose fix changes what binds, in a spec what R8 lists, in a plan
  its inter-task contracts and a task's required fields and acceptance.
  For any other MINOR the controller accepts, the dispositions take
  precedence in this order: one whose resolution needs local mechanism
  keeps `deferred-to-implementation`; one that is a design judgment for
  the operator keeps `parked`; the rest take a new disposition,
  `deferred-minor`, and are not fixed in the campaign. The rule that a
  correction of artifact text is `applied` holds for what a fix list
  takes. A MINOR the controller finds wrong, or outside the finding
  scope, stays `rejected`. Round 0's claim corrections are unaffected:
  its claim table carries no severities. The spec terminal-pass record,
  and the plan record's `## Terminal pass`, list their pass's
  `deferred-minor` findings, a second read's included, with their
  dispositions. At the close that seeds the SDD ledger (the plan phase's,
  or a folded campaign's), each `deferred-minor` entry of the spec
  campaign and the plan phase is seeded under the ledger's
  `## Deferred minors` with its source, and SDD's resume check seeds any
  the ledger lacks. The branch reviewer triages it as it triages any
  parked minor (PROMOTE, FIX-IN-WAVE or LEAVE-PARKED); one left parked
  reaches the close readout with the controller's proposal to keep or
  drop it, as today. An umbrella's campaign sends its `deferred-minor`
  entries with what it left open to its landing's open-items step.
  Basis: the umbrella's D6 and its interface on deferred campaign
  MINORs; the destination record 3.
- **R3. The terminal pass's wave and its second read.** The spec pass's
  follow-up wave takes R2's fix list. The second read runs in two cases:
  after that wave (in the plan phase, after the repair), as now; and as
  a record-only read whenever the pass's report carries a record
  correction or the controller's close readout puts a decision ask to
  the operator again on it. The record-only read runs on the recorded
  close readout before it is delivered, reading the records and asks the
  controller wrote after the pass against the pass's report and the
  seat findings behind each ask; its corrections are added to the
  readout before delivery. Where both cases apply, one second read does
  both. Each pass gets at most one second read. Of what it leaves open,
  a MINOR not against binding text takes `deferred-minor` (R2), and the
  rest goes to the operator. This holds in the spec campaign and the
  plan phase alike. Basis: the umbrella's D4.
- **R4. The bias statement folded.** The terminal pass's record check
  closes with one line stating whether its corrections share a direction
  favouring the record's author, and goes to the operator as a decision
  ask only where the pass states the record is materially misleading. A
  correction that changes a conclusion is flagged `CONCLUSION-CHANGING`
  and is a decision ask on its own, so the bias line has no second
  trigger. The operating-stance section of the redteaming skill keeps
  its heading, which another skill cites, and drops its sentences on the
  conservation check and the bias statement. Basis: the umbrella's D4;
  the kept trigger, the umbrella's D2.
- **R5. Premise findings retired.** The `premise` label, its separate
  routing, its mislabel and precedence rules, the holds a pending
  premise ask put on the campaign's stop and on execution work, its open
  entries under the ledger's `## Adjudication rulings` with their
  seeding and resume check, and the umbrella's `open premise ask:` note
  go. A doubt about the request, what the Intent asks for (for a child,
  also what its umbrella's Intent asks for) or a firm decision still
  reaches the operator as a decision ask, quoted as raised, on carriers
  that exist:
  - a seat writes it as a question, the terminal pass in its
    `## Notes`; in a campaign the controller carries it to the readout,
    and the terminal pass's record check counts such a question that
    the records answered instead of carrying as a correction;
  - in execution, an implementer writes it as a concern and a task
    reviewer as a question; the task reviewer and the branch reviewer
    name such a doubt and rule on none, and the controller writes each,
    and the branch reviewer's own, under the ledger's `## Questions` as
    open;
  - a decision ask still open at a phase's close rides the carriage of
    what earlier phases left open
    (`skills/redteaming/references/plan-phase.md`), as an unruled parked
    entry or an unanswered carried question does, into the ledger's
    `## Questions`;
  - the close readout puts each open doubt and each unruled ask to the
    operator as a decision ask.

  The operator's ruling takes the route any change of its kind takes.
  The holds go because a pending ask's failure is loud: it still
  reaches the operator, and a ruling that upholds it after the stop
  takes the flip paths. Basis: the umbrella's D4; the holds' basis, its
  D2.
- **R6. The outside-the-frame lens.** One seat of a spec campaign's
  round 1 carries a lens that reads the design from outside its frame:
  whether it solves the problem the request poses (for a child, with
  its umbrella's Intent and its entry), and whether another framing, or
  no change, would serve it better. In a one-seat round 1 that seat
  carries it beside general. Its doubts follow R5. No later round and no
  plan-phase seat carries it. Basis: the umbrella's D4.
- **R7. The goal check narrowed.** It runs at a spec campaign's round-1
  seats and at the branch review only; later rounds and plan-phase seats
  drop it, with the shared reference's sentence on reviewing a plan.
  Lane Fit's goal half is `execution-retirements`'. Basis: the
  umbrella's D4.
- **R8. Marks retired.** `[LOAD-BEARING]` marks go. What binds in a
  spec is its Constraints & invariants, the preamble conventions it
  declares binding and the decisions it records as the operator's firm
  preference; for a child of an umbrella, also its own entry, what its
  umbrella's Intent asks for, and its umbrella's Constraints &
  invariants and firm decisions, up the chain. A change on a child's
  branch to any of the umbrella's items, or to its entry beyond its own
  mark or a clarification its spec states, is a finding. Every statement
  of what binds is updated to that content; the containment test judges
  what builds on any item, with no mark to read it from. The umbrella
  entry marks (`landed`, `umbrella`, `dropped`) stay. Basis: the
  umbrella's D4.
- **R9. The containment test's exclusions.** It keeps four: a change to
  umbrella content, to a firm decision, a change after which the same
  work passes a check it failed, and a structural change. It drops the
  one on marking `Review: branch only` late. The kept check-passing
  exclusion guards a silent failure — work that should fail lands — so
  the umbrella's D2 keeps it. Basis: record 7, refining the umbrella's
  D4 (Interfaces & boundaries).
- **R10. The right-sizing re-seat by judgment.** Whether the
  right-sizing lens returns in a later round is the controller's
  judgment on how far the artifact has grown; the readout's trace
  records no line counts. Basis: the umbrella's D3.
- **R11. Decision asks apart.** Every readout that puts decision asks to
  the operator — the gate before a spec campaign, round readouts, the
  closes of the spec campaign and the plan phase, SDD's close readout,
  an umbrella's landing ask and its closing review's readout — puts them
  in a block of their own after the readout's body, each with its
  options and recommendation. The rule is stated once, in
  `crucible:redteaming` § Round readout, and the other readouts point to
  it. Basis: the umbrella's D6.
- **R12. Round 0 on every spec campaign.** Round 0 runs whatever the
  artifact; with no code baseline it checks the artifact's claims
  against its inputs (the request, the decision record, the documents
  it cites) and the liveness of its mechanisms. The round-1 seat
  variant that hunted those first goes, with the `ordered-first` value
  of the seat's `worksheet` selector; the selector's `pre-pass` value,
  the plan phase's, stays. The folded lane's stated reason for round 0
  goes, keeping that its pre-pass also covers the plan half. Basis:
  record 4.
- **R13. The digest retired; a short gate kept.** The design digest,
  its format and its readout item go. The gate stays: before the
  campaign, the operator sees the decision record's decisions and open
  asks inline and the campaign shape, as a minor design's gate does
  today. A decision ask still open at a spec campaign's close travels in
  its close readout, then as R5 states. Basis: the umbrella's D4; the
  gate record 2.
- **R14. Umbrellas.** A decision ask still open at an umbrella's
  landing is put to the operator with the landing ask, and an unruled
  one goes with what the campaign left open to the open-items home, by
  the landing's existing step for it: that step is the carrier the entry
  keeps, and no note goes into a Children entry. The `[LOAD-BEARING]`
  marks' clauses and the premise-finding clauses leave
  `skills/brainstorming/references/umbrellas.md`. Basis: the umbrella's
  entry for this child.
- **R15. The vocabulary list.** The labels, record lines and statuses
  this child removes or adds are listed in its landing and in the
  decision records' `## Changes` lines; the backlog's vocabulary point
  (`docs/backlog/skill-text-rewrite.md`) is trimmed to the vocabulary
  that stays. Basis: the umbrella's entry for this child.

## Constraints & invariants

- **I1. No finding is dropped silently.** Every finding a campaign does
  not fix reaches a stage that reads it: a `deferred-minor` the branch
  review's triage and, left parked, the close readout, or for an
  umbrella its landing's open-items step; a doubt about the request,
  the Intent or a firm decision, from any seat or implementer, the
  operator; any other disposition as today.
- **I2. The kept guards keep their function** (the umbrella's C3): the
  second read in both its runs, the containment test's check-passing
  exclusion, the bias line's escalation on a materially misleading
  record, and the route carrying every such doubt to the operator.
- **I3. Nothing states a retired mechanism as current.** After the
  branch, no shipped skill text, template, generated agent, test, live
  decision record, `docs/authoring.md`, `README.md` or `AGENTS.md`
  states one; a decision record may keep it as history. Frozen feature
  folders and the scanner's byte-exact corpus
  (`tests/claudeism_scanner_corpus/`) are exempt.

## Interfaces & boundaries

- **With `execution-retirements`.** This child does not change the
  mechanisms that child owns (Non-goals). Where a passage mixes them,
  this child edits only its own mechanism's words: it drops marks from
  the pre-flight scan's statement of what binds, and leaves the backlog
  bullet on statements of what binds
  (`docs/backlog/umbrella-followups.md`) to that child. The seeding of
  `deferred-minor` entries into `## Deferred minors` is the carriage that
  child keeps when it simplifies the deferral chain.
- **With `placement`.** Existing restatements of what binds keep their
  number and place; only their content changes. The shared reference
  keeps its file name, `premise-and-questions.md`, which `placement`
  renames.
- **The umbrella on this branch.** Lightly held edits by
  `skills/brainstorming/references/umbrellas.md` § Edits: to its D4, the
  campaign shape stays at the gate (R13) and the containment test keeps
  its check-passing exclusion (R9); to its Interfaces & boundaries,
  deferred campaign MINORs reach the branch review's triage through the
  closes that seed the ledger (R2). The carrier for a decision ask open
  at an umbrella's landing is the landing's open-items step, a
  clarification of this child's entry (R14). The entry's `landed` mark
  comes at Finish.
- **Ledger lines and the branch reviewer.** A seeded `deferred-minor`
  is a `## Deferred minors` line whose source is `Spec` or `Plan`,
  beside the existing `Task <N>`, `Lane` and `Branch wave <n>` sources;
  the branch reviewer's ledger input and its triage take that source
  where they now name an owning task. An open doubt (R5) is a
  `## Questions` line of the form `<source>: doubt: <the doubt> — open`,
  which no reviewer rules on and the close readout puts to the operator.
- **Terminal-pass records.** A second read's report is `second-read.md`
  beside the pass's first report, in both its runs. The spec
  terminal-pass record's reachable states gain
  `dispatched → returned → verified → readout` for a record-only read,
  `verified` meaning the second read is on disk; the plan record writes
  `confirmed` after any second read, as now.
- **Removed headings.** `skills/redteaming/references/formats.md`
  § Design digest format is a frozen anchor (`docs/authoring.md`
  § Anchor stability); `premise-and-questions.md` § Premise findings and
  `skills/redteaming/references/flip-paths.md` § Premise findings are
  widely cited. Removing any of them updates every citation in the same
  change, path-form citations, which the anchor test
  (`tests/test_references.py`) holds, and prose forms such as "the
  shared reference's § Premise findings", which only A1's search finds.

## Acceptance

- **A1. No retired mechanism stated.** One-time check: a
  case-insensitive search of `skills/`, `agents/`, `tests/` (the
  scanner's corpus excluded), `docs/decisions/`, `docs/authoring.md`,
  `README.md` and `AGENTS.md` for at least `conserve`, `conservation`,
  `LOAD-BEARING`, `open premise ask`, the premise label's forms
  (`] premise`, `` `premise` ``, `premise finding`, `premise ask`),
  `digest`, `ordered-first`, `numstat`, `line counts` and
  `Python 3.8`, with the terms the plan names for each
  Decision's sites, finds only history in decision records and senses
  unrelated to the retired mechanisms; the command and its output are
  recorded. No later change is planned that could undo it.
- **A2. The suite passes.** One-time at Finish: `python -m pytest
  tests/`, its summary line quoted with the skip count; the generated
  agents match their templates (the suite's check mode).
- **A3. The sizes.** One-time at Finish: the sum of
  `tests/prose-budget.txt` at or below 65,978 with the net stated, and
  the subagent-driven-development, redteaming and brainstorming
  `SKILL.md` files each no larger than at `8c14505` (46,565, 40,662 and
  24,257 bytes), by `git cat-file -s`.
- **A4. The paths walked.** One-time, by the controller, recorded in
  the branch review's records: for the standard route's spec campaign
  and plan phase, the folded campaign, an umbrella's campaign and its
  closing review, the very-small lane, the task loop and the branch
  review, where a `deferred-minor`, a doubt about the request, the
  Intent or a firm decision, an open decision ask and each second-read
  run go, each ending at a stage that reads it (I1).
- **A5. The backlog.** One-time: each item the umbrella's entry names
  for this child is resolved and deleted, or trimmed to what stays open,
  and the landing says which: the campaign side of
  `docs/backlog/skill-text-rewrite.md` (its vocabulary point, round-0
  finding, containment-test point and the mark's half of its two senses
  of "load-bearing" included), the digest follow-up of
  `docs/backlog/lane-entry-and-downshift.md`,
  `docs/backlog/decision-ask-framing.md`, the `conserve` half of
  `docs/backlog/claude-code-mod.md` with its re-open trigger, the
  `conserve` mention in `docs/backlog/second-runtime-seat.md`, and the
  size sentence of `docs/backlog/umbrella-followups.md`.

## Mechanism sketches

Advisory. One task per mechanism or close cluster, each across every
site that states it, its tests, generated agents and decision records
(each changed record taking its dated `## Changes` line), in this order:
marks (R8); premise findings, the lens and the goal check (R5–R7);
conservation (R1); fix lists, `deferred-minor`, the terminal pass's
wave, the second read and the bias line (R2–R4); the digest, the gate
and the asks block (R11, R13); round 0 (R12); the containment test and
the re-seat (R9, R10); umbrellas and the umbrella's edits (R14); the
backlog (R15, A5). Each task lowers the prose-budget lines it shrinks.
