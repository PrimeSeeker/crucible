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
- **G3.** The skills shrink (the umbrella's C1 and C2), and the landing
  states the net change and the sizes.

**Non-goals.**

- The execution side of the umbrella's D3, D4 and D6
  (`execution-retirements`): the tree check, the seat-replacement gate,
  the pre-flight scan, the task review's cannot-verify items, snapshot
  blessing, adjudication, revert-and-replan, the fix ladder and breaker,
  Lane Fit and the upgrade hatch, the deferral chain and
  `Review: branch only`, the landing ask after the final pass.
- Consolidating restatements into one owner text (`placement`): where
  this child edits a restatement, it changes its content only.
- New mechanisms beyond the four this child needs: the round-1
  outside-the-frame lens, the `carried` disposition, the second read's
  record-only run and the umbrella's `open ask:` note.

## Decisions

All lightly held. Each names its basis; record numbers are entries of
the brainstorm decision record.

- **R1. Merge conservation retired.** The script
  `skills/redteaming/scripts/conserve.py`, its tests and helper, the
  round record's `conservation:` line and the rules that run or read it
  go. A merged entry keeps its `origins:` element, which the terminal
  pass reads to find the findings behind each decision ask; every seat
  question keeps its disposition; seat ids stay unique within a feature,
  for the same reader. Nothing mechanical checks the merge. Crucible then
  ships no Python script, so the README's Python requirement and the
  Python-floor reasoning tied to the script go. Basis: the umbrella's D3.
- **R2. Small fix lists; MINORs carried.** A fix list — a numbered
  round's, the plan phase's, and the terminal pass's follow-up wave's —
  takes BLOCKER and MAJOR findings and MINOR findings against binding
  text. Any other MINOR takes a new disposition, `carried`, and is not
  fixed in the campaign. Round 0's claim corrections are unaffected: its
  claim table carries no severities. At the close that seeds the SDD
  ledger (the plan phase's, or a folded campaign's), each `carried`
  entry of the spec campaign and the plan phase is seeded under the
  ledger's `## Deferred minors` with its source, `Spec round <n>` or
  `Plan`, where the branch reviewer triages it with the task reviews'
  minors and the cleanup wave can fix it. An umbrella's campaign sends
  its `carried` entries with what it left open to its landing's
  open-items step. Basis: the umbrella's D6 and its interface on
  deferred campaign MINORs; the destination record 3.
- **R3. The terminal pass's wave and its second read.** The pass's
  follow-up wave takes R2's fix list. The second read runs in two cases:
  after that wave, full-scope as now, and as a record-only read whenever
  the pass's report carries a record correction or the controller puts a
  decision ask to the operator again on it, reading the records and asks
  the controller wrote after the pass against the pass's report and the
  seat findings behind each ask. Where both apply, one second read does
  both. This holds in the spec campaign and the plan phase alike. Basis:
  the umbrella's D4.
- **R4. The bias statement folded.** The terminal pass's record check
  closes with one line stating whether its corrections share a direction
  favouring the record's author. It has no escalation rule of its own: a
  correction that changes a conclusion is flagged `CONCLUSION-CHANGING`
  and is a decision ask already. The operating-stance section of the
  redteaming skill keeps its heading, which another skill cites, and
  drops its sentences on the conservation check and the bias statement.
  Basis: the umbrella's D4.
- **R5. Premise findings retired.** The `premise` label, its routing
  and carrying, the hold a pending premise ask put on the campaign's
  stop, and the umbrella's `open premise ask:` note go. A seat's doubt
  about the request, what the Intent asks for (for a child, its
  umbrella's Intent too) or a firm decision is a question, and a
  question of that kind is always carried to the operator verbatim, by
  every seat whose report has questions. An implementer raises such a
  doubt as a concern. The operator's ruling on it takes the route any
  change of its kind takes. The hold goes because an open ask that could
  overturn a major mechanism already keeps the overturn question's
  answer at "still expected". Basis: the umbrella's D4.
- **R6. The outside-the-frame lens.** One seat of a spec campaign's
  round 1 carries a lens that reads the design from outside its frame:
  whether it solves the problem the request poses, and whether another
  framing, or no change, would serve the request better. In a one-seat
  round 1 that seat carries it beside general. Its doubts are questions
  (R5). No later round and no plan-phase seat carries it. Basis: the
  umbrella's D4.
- **R7. The goal check narrowed.** It runs at a spec campaign's round-1
  seats and at the branch review only; later rounds and plan-phase seats
  drop it, with the shared reference's sentence on reviewing a plan.
  Lane Fit's goal half is `execution-retirements`'. Basis: the
  umbrella's D4.
- **R8. Marks retired.** `[LOAD-BEARING]` marks go. What binds in a
  spec is its Constraints & invariants, the preamble conventions it
  declares binding and the decisions it records as the operator's firm
  preference; for a child of an umbrella, also its own entry and its
  umbrella's Constraints & invariants and firm decisions, up the chain.
  Every statement of what binds is updated to that content; the
  containment test judges what builds on any item, with no mark to read
  it from. Basis: the umbrella's D4.
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
- **R11. Decision asks apart.** Every readout that puts a decision ask
  to the operator — round readouts, the closes of the spec campaign and
  the plan phase, SDD's close readout, the branch review's readouts, an
  umbrella's landing ask and its closing review's readout — puts its
  asks in a block of their own after the readout's body, each with its
  options and recommendation. Basis: the umbrella's D6.
- **R12. Round 0 on every spec campaign.** Round 0 runs whatever the
  artifact; with no code baseline it checks the artifact's claims
  against its inputs (the request, the decision record, the documents
  it cites) and the liveness of its mechanisms. The round-1 seat
  variant that hunted those first, with its selector, goes. The folded
  lane's reason for round 0 is corrected: its pre-pass also covers the
  plan half. Basis: record 4.
- **R13. The digest retired; a short gate kept.** The design digest,
  its format and its readout item go. The gate stays: before the
  campaign, the operator sees the decision record's decisions and open
  asks inline and the campaign shape, as a minor design's gate does
  today. A decision ask still open at a spec campaign's close travels in
  its close readout. Basis: the umbrella's D4; the gate record 2.
- **R14. Umbrellas.** The landing's carrier for a decision ask still
  open becomes `open ask: <the ask>`, noted in the first entry with no
  mark of its own Children list, for any decision ask, not only a
  premise ask; the marks' clauses and premise-finding clauses leave
  `skills/brainstorming/references/umbrellas.md`. Basis: the umbrella's
  entry for this child.
- **R15. The vocabulary list.** The labels, record lines and statuses
  this child removes or adds are listed in the backlog's vocabulary
  point (`docs/backlog/skill-text-rewrite.md`). Basis: the umbrella's
  entry for this child.

## Constraints & invariants

- **I1. No finding is dropped silently.** Every finding a campaign does
  not fix reaches a stage that reads it: a `carried` MINOR the branch
  review's triage, or for an umbrella its landing's open-items step; a
  question doubting the request, the Intent or a firm decision the
  operator; any other disposition as today.
- **I2. The kept guards keep their function** (the umbrella's C3): the
  second read in both its runs, the containment test's check-passing
  exclusion, and the rule carrying every doubting question to the
  operator.
- **I3. Nothing states a retired mechanism as current.** After the
  branch, no shipped skill text, template, generated agent, test, live
  decision record, `docs/authoring.md`, `README.md` or `AGENTS.md`
  states one; a decision record may keep it as history. Frozen feature
  folders are exempt.

## Interfaces & boundaries

- **With `execution-retirements`.** This child does not change the
  mechanisms that child owns (Non-goals). Where a passage mixes them,
  this child edits only its own mechanism's words. The seeding of
  `carried` entries into `## Deferred minors` is the carriage that child
  keeps when it simplifies the deferral chain.
- **With `placement`.** Restatements of what binds keep their number
  and place; only their content changes.
- **The umbrella on this branch.** Two lightly held edits to its D4
  (the umbrella's § Edits): the campaign shape stays at the gate (R13),
  and the containment test keeps its check-passing exclusion (R9). The
  entry's `landed` mark comes at Finish.
- **Ledger lines.** A seeded `carried` entry takes the form of a
  `## Deferred minors` line with the source `Spec round <n>` or `Plan`
  beside the existing `Task <N>`, `Lane` and `Branch wave <n>` sources.
- **Anchors.** Removing `skills/redteaming/references/formats.md`
  § Design digest format and
  `skills/subagent-driven-development/references/premise-and-questions.md`
  § Premise findings is an interface change (`docs/authoring.md`
  § Anchor stability): every citation of either is updated in the same
  change, and the anchor test (`tests/test_references.py`) holds it.

## Acceptance

- **A1. No retired mechanism stated.** One-time check: a search of
  `skills/`, `agents/`, `tests/`, `docs/decisions/`,
  `docs/authoring.md`, `README.md` and `AGENTS.md` for `conserve`,
  `conservation:`, `LOAD-BEARING`, `open premise ask`, the `premise`
  label, `digest`, `ordered-first` and `numstat` finds only history in
  decision records; the command and its output are recorded. No later
  change is planned that could undo it.
- **A2. The suite passes.** One-time at Finish: `python -m pytest
  tests/`, its summary line quoted with the skip count; the generated
  agents match their templates (the suite's check mode).
- **A3. The sizes.** One-time at Finish: the sum of
  `tests/prose-budget.txt` at or below 65,978 with the net stated, and
  the subagent-driven-development, redteaming and brainstorming
  `SKILL.md` files each no larger than at `8c14505` (46,565, 40,662 and
  24,257 bytes), by `git cat-file -s`.
- **A4. The campaign paths walked.** One-time, recorded at the branch
  review: for the standard route's spec campaign and plan phase, the
  folded campaign and an umbrella's campaign, where a `carried` MINOR, a
  doubting question, an open decision ask and each second-read run go,
  each ending at a stage that reads it (I1).
- **A5. The backlog.** One-time: each item the umbrella's entry names
  for this child is resolved and deleted, or trimmed to what stays open,
  and the landing says which: the campaign side of
  `docs/backlog/skill-text-rewrite.md` (its vocabulary point, round-0
  finding and containment-test point included), the digest follow-up of
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
conservation (R1); fix lists, `carried`, the terminal pass's wave, the
second read and the bias line (R2–R4); the digest, the gate and the
asks block (R11, R13); round 0 (R12); the containment test and the
re-seat (R9, R10); umbrellas and the umbrella's D4 edits (R14); the
backlog (R15, A5). Each task lowers the prose-budget lines it shrinks.
