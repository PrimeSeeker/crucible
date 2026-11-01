# Skill text rewrite: retire what does not pay, then place and fit the rest

## Intent

**Problem.** The twelve skills hold 65,978 words at `a3db87f`
(`tests/prose-budget.txt`), up from 62,069 at `dd6897d`;
subagent-driven-development (19,548) and redteaming (19,465) hold
most of it. Three `SKILL.md` files are over the 20,000-byte line
upstream uses for a skill that survives compaction whole:
subagent-driven-development (46,565 bytes), redteaming (40,662) and
brainstorming (24,257) (`docs/backlog/skill-size-after-compaction.md`).
`docs/backlog/skill-text-rewrite.md` records that size follows
mechanisms: placement alone, worth about 11% of the text, will not
reduce it much, and retiring mechanisms that do not pay is the larger
lever.

**The audit behind this umbrella.** Before this umbrella was written, a
read-only audit (2026-11-01) inventoried 147 mechanisms in the shipped
skill text and counted what each caught in recorded runs: about 40
features in another project (a Python codebase, run on pre-0.2.0
versions) and about 25 in crucible's own repository (versions up to
0.9.0), read from session transcripts by three default-role readers
and one reader of the other model family. Its findings, in short:

- Fix waves are the main source of the defects the process itself
  introduces: late-round findings mostly correct earlier waves' text,
  and a branch fix wave once introduced a production defect that its
  re-review, the next full pass and the suite all missed.
- Checks on checks catch little: the merge-conservation script about 1
  trivial catch in about 73 runs, the tree check about 1 in more than
  800, Lane Fit 2 "exceeds" verdicts in about 42, both on one lane.
- Real catches come from first reads of the design (round 0, the first
  panel round), the plan phase, the terminal pass's check of the
  records against the seats' reports, the branch review and
  implementers' concerns.
- Several mechanisms never ran: the breaker, revert-and-replan,
  `Review: branch only`; adjudication ran 5 times and upheld nothing.
- Of 23 defects an after-the-fact audit of one umbrella found, 11 had
  been raised during development and lost, mostly at landing.

The audit's limits: counts are lower bounds; whether a later stage
would have caught a finding is the readers' judgment; the newest
mechanisms ran only on crucible's own text; cost was counted in words,
not tokens.

**Goals.**

- **G1.** Retire or simplify the mechanisms the audit found not to pay,
  as ruled below, keeping a cheap guard wherever the failure a
  mechanism targets would be silent.
- **G2.** Bring the remaining text into line with the placement rule
  (writing-skills' Size and placement bullet; `AGENTS.md`, Where text
  goes).
- **G3.** Fit every `SKILL.md` under the compaction line.
- **G4.** Fix the three structural failures the audit found (D6).

**Non-goals.**

- A total size target. The effort is exploratory: it goes as low as
  the evidence allows (D1).
- Adding mechanisms, apart from the round-1 lens that replaces premise
  findings (D4) and the structural fixes (D6).
- A cross-family branch-review seat (`docs/backlog/second-runtime-seat.md`)
  and the test rules' effect on suite size, whose rules were revised on
  2026-10-15 (`docs/decisions/test-rules.md`); both stay outside this
  effort.
- Slimming the decision records (`docs/backlog/decision-records-upkeep.md`).

## Decisions

All lightly held.

- **D1. Exploratory, evidence-led reduction.** No total target. Hard
  limits are the Constraints below; each child reports its counts, and
  resident tokens per route are measured before and after as the
  effort's outcome. Basis: the maintainer's ruling.
- **D2. Silent and loud failures.** Where a mechanism's target failure
  would be loud, or another mechanism covers it, the mechanism is
  retired outright: the failure shows when it happens, and a release
  restores the text. Where the failure would be silent, a cheap guard
  stays. A mechanism that never ran keeps its trigger as one
  stop-and-ask line, its procedure dropped. Basis: the audit's review of
  where its own evidence is weak, accepted by the maintainer.
- **D3. Retired.**
  - Merge conservation and `skills/redteaming/scripts/conserve.py`,
    with the round record's conservation line.
  - The seat-replacement gate (subagent-driven-development § Shared-tree
    rules; redteaming § Panels, Topping up is gated).
  - The terminal pass's second read, together with a rule that the
    terminal pass's follow-up wave fixes only BLOCKER and MAJOR
    findings, its MINORs travelling to execution as notes, so no wave
    is left unread.
  - The wave line counts that signal a re-seat.
  - Lane Fit's shape verdict (its goal half is the branch review's goal
    check, D4); the very-small lane's upgrade hatch becomes one
    stop-and-ask line.
  - The pre-flight plan-conflict scan, and cannot-verify items.
  - Revert-and-replan, and the fix ladder's fresh-implementer steps and
    breaker, each becoming a stop-and-ask line or a short cap with an
    operator ask.

  Basis: the audit's counts, ruled by the maintainer.
- **D4. Simplified.**
  - The tree check: one status check after each review seat, before the
    next commit, in place of readings around every review window;
    reviewers have written into the tree, and an unseen write would land
    unreviewed.
  - Adjudication: the controller rules on a dispute with its evidence,
    and a dispute touching binding text or the Intent gets one
    independent read; the controller's lean toward its own position is
    the best-documented bias in the audit.
  - Snapshot blessing: one line.
  - `[LOAD-BEARING]` marks retired; what binds is Constraints &
    invariants and firm decisions, and, for a child, its umbrella's.
  - The design digest dropped; the campaign shape goes into the
    approval at brainstorming's step 4.
  - Premise findings replaced by one round-1 seat whose lens reads the
    design from outside its frame; a premise doubt is an ordinary
    decision ask, and implementers keep raising one as a concern.
  - The directional-bias statement folded into the terminal pass's
    record check as one line.
  - The containment test keeps its rule and drops the exclusions added
    after single incidents.
  - The goal check runs at round-1 seats and the branch review only.
  - The deferral chain: the marker, and a plan task that owns it; no
    routing-table chain.
  - `Review: branch only`: one plan field with its reason; no grading
    chain.

  Basis: the audit, ruled by the maintainer; for marks, also the
  maintainer's judgment that they were used too liberally.
- **D5. Kept.** Round 0; the first panel round with the right-sizing
  seat and the alternate-role seat; the plan phase; the terminal pass
  with its stop check and the seats' forecast lines; the round cap; the
  blind verifier, its seat text trimmed by placement; task review; the
  branch review with ledger triage and the cleanup wave; implementers'
  status and concerns; the umbrella closing review; umbrellas, condensed.
  Basis: the audit's catches; for the verifier, the maintainer's ruling
  on uncertain evidence (last-wave misses fell when its current form
  arrived; whether it or better fix waves did that is unknown).
- **D6. Structural fixes.**
  - Fix-wave drift: fix lists stay small, MINORs deferred to execution
    rather than fixed in a campaign.
  - Landing: the landing ask comes after the final branch pass, and
    findings parked at triage are filed before the workspace is
    deleted.
  - Readouts: decision asks stand apart from the readout body.

  Basis: the audit's misses, accepted by the maintainer.
- **D7. Order: retire, then place, then fit.** Retiring deletes text,
  so placement does not polish what goes; fit depends on the final
  sizes. Placement and fit are separate children because fit changes
  what loads when, and placement changes no behaviour. Basis: the
  controller's proposal, delegated by the maintainer.
- **D8. Each child runs under its predecessors' rules.** Before a
  child's brainstorm, the maintainer's installs carry every child landed
  before it; "waits on" below means landed and installed. A host
  fetches a new copy only when the version changes, so each install
  bumps it. Basis: the practice of the previous umbrella, accepted by
  the maintainer.
- **D9. A re-audit follows.** After the retirement children have run on
  a few features, the audit is repeated on the new runs to check
  whether a retired mechanism's failure reached a later stage. It is an
  open item the umbrella's landing files, not a child. Basis: the
  controller's proposal, accepted by the maintainer.

## Constraints & invariants

- **C1. No child grows the skills.** Each child's landing leaves the
  sum of `tests/prose-budget.txt` at or below its value before the
  child, and states its net change and what it removed.
- **C2. No `SKILL.md` over the compaction line grows**, in any child;
  at the effort's close each is under it (`compaction-fit`).
- **C3. A kept mechanism keeps its function.** A child may move,
  reword or merge a mechanism D5 keeps; removing or weakening one, or
  a guard D2 keeps, takes an operator ruling.
- **C4. The branch review stays mandatory on every arrangement, at full
  scope.**

## Interfaces & boundaries

- **The retirement children provide** the mechanism set the later
  children work on; `placement` starts from the text they leave.
- **`placement` provides** the shared seat reference the templates
  point to, which `compaction-fit` may move text into or out of.
- **Shared files.** All four children edit the same skills; they run in
  order, each from a base that holds its predecessors (D8).
- **Evidence.** The audit's inventory and readers' reports are kept in
  this umbrella's workspace while it lives; children cite this
  umbrella's figures, never the reports, which name a private project.

## Acceptance

The Children list, in order:

- `review-retirements` — the campaign side of D3, D4 and D6: merge
  conservation and its script, the second read with the terminal pass's
  MAJOR-only wave, the re-seat line counts, the digest, `[LOAD-BEARING]`
  marks, premise findings replaced by the round-1 lens, the bias
  statement folded, the containment test's exclusions, the goal check's
  narrower reach, small fix lists, and decision asks apart from every
  readout body, close readouts included. Takes up the mechanism part of
  `docs/backlog/skill-text-rewrite.md` on this side, the digest
  follow-up of `docs/backlog/lane-entry-and-downshift.md` and the size
  part of `docs/backlog/umbrella-followups.md`. Waits on nothing

- `execution-retirements` — the execution side of D3, D4 and D6: the
  tree check simplified, the seat-replacement gate, the pre-flight scan,
  cannot-verify items, snapshot blessing, adjudication, revert-and-replan,
  the fix ladder and breaker, Lane Fit and the upgrade hatch, the
  deferral chain, `Review: branch only`, and the landing ask after the
  final pass with parked findings filed first. Takes up
  `docs/backlog/implementer-dispute-channel.md` and the rest of the
  mechanism part of `docs/backlog/skill-text-rewrite.md`. Waits on
  `review-retirements`

- `placement` — G2 on the text the retirements leave: one owner text
  per rule; one shared seat reference in place of the clauses copied
  into the templates; history and long rationale to the decision
  records; host-neutral rules out of the adapters; upstream-derived
  supporting files brought to crucible's grain; the verifier's seat
  text trimmed; the slips, the numbering and naming defects and the
  open-items pointer `docs/backlog/skill-text-rewrite.md` lists. No
  behaviour changes. Takes up the rest of `skill-text-rewrite.md` and
  `docs/backlog/cross-skill-anchor-citations.md`. Waits on
  `execution-retirements`

- `compaction-fit` — G3: token counts measured with a tokenizer and the
  line checked against the host's current documentation; each
  `SKILL.md` brought under it by moving always-run sections into
  references read at their step; a structural test holding each
  `SKILL.md` under the line; resident tokens per route before and after,
  reported as the effort's outcome (D1). Takes up
  `docs/backlog/skill-size-after-compaction.md`. Waits on `placement`

Each child's own Acceptance carries the checks. A child taking up a
backlog item resolves it or trims it to what stays open, and says
which; an item shared between children is trimmed by each and deleted
once nothing in it stays open.

## Mechanism sketches

None at umbrella level: design detail is each child's, in its entry and
its own spec.
