# Placement: one owner text per rule

Umbrella: `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`

## Intent

**Problem.** The rules crucible's skills state are copied across files,
and the copies drift. A read-only placement audit of the tree at
`8332a00` (2026-11-02; four default-role readers, by area: the seat
templates, review before code, execution with the host adapters, and
the upstream-derived skills) estimated about 8,000 of the skills'
63,732 words removable by placement alone, and found about 25 rules
whose copies differ in substance: one copy stricter, one missing a
case, one contradicting another. The largest restatement is the
statement of what binds, copied into six seat templates and about
eight other sites. The seven seat templates carry about 3,500 words of
clauses that every seat, or every review seat, follows. The audit's
reports are committed beside this spec as advisory input
(`audit-templates.md`, `audit-review.md`, `audit-execution.md`,
`audit-upstream.md`).

**Goals.**

- **G1.** Each rule stated more than once has one owner text, at the
  site where its reader acts; every other site points to it or says
  nothing (Interfaces & boundaries, the owner map).
- **G2.** The clauses the seat templates share have one hand-edited
  source, the shared seat reference, spliced into each template at
  build time (D4, D5).
- **G3.** Text at the wrong level leaves the skills: how a rule was
  learned to the decision records, text about crucible's own text to
  `docs/`, host-neutral rules out of the adapters (D7, D8, D13).
- **G4.** The drifted copies, the stale wording and the slips the entry
  and the backlog list are corrected (D1, D2, the corrections list).
- **G5.** The skills shrink; the landing states the net change and the
  `SKILL.md` sizes (the umbrella's C1, C2).

**Non-goals.**

- Changing a rule, beyond the corrections D1 and D2 admit and the one
  change the entry names (the re-reviewer's full comment rule).
- Filling the rule gaps the earlier children left open (the operator's
  answer to an "another approach" ask by a plan change; the kind of a
  lane lead carried past the upgrade hatch), the umbrella-landing
  question, the action on a review missing a verdict, and the
  separability and tension-closing points of
  `docs/backlog/skill-text-rewrite.md`: they stay in the backlog (D1).
- Moving always-run sections out of a `SKILL.md` to fit the compaction
  line: `compaction-fit`'s.
- Generating skill text: skills stay hand-written (D12).
- Slimming the decision records; they may grow by what moves into them.

## Decisions

All lightly held. Each records its basis.

- **D1. Corrections, not rule changes.** Placement corrects text that
  disagrees with rules already in force (stale wording) and restores a
  drifted copy to its evident intended version; where the intended
  version is not evident, the operator rules (D2). Fills of rule gaps
  stay in the backlog. Basis: the controller's proposal, the call
  delegated by the operator; the drift extension, the controller's call
  under that delegation.
- **D2. The drift rulings.** Four drifts whose intended version was not
  evident, ruled:
  - **R1.** One definition of a decision ask, holding redteaming's two
    obligations (list every option the findings behind it propose;
    state what the change withdraws from an earlier operator approval),
    applies to every decision ask, execution and branch review
    included.
  - **R2.** What a reviewer flags under an umbrella is the full set
    `skills/brainstorming/references/umbrellas.md` § Edits names as a
    binding change, an edit to another started child's entry included.
  - **R3.** The build-history rule exempts the feature folder's files for
    every reviewer, and the open items Finish wrote for the branch
    reviewer only.
  - **R4.** The `literal-reading` label is the execution seats' (task
    reviewer, re-reviewer, branch reviewer); the shared reference scopes
    its sentence on the label to them, and redteam seats keep raising
    such a case as a finding naming the item and the case.

  Basis: the controller's proposals, accepted by the operator.
- **D3. Upstream skills kept close stay close.**
  `docs/decisions/upstream-skills-kept-close.md` stands:
  systematic-debugging and dispatching-parallel-agents change only for
  its listed reasons, a defect among them, so placement fixes their
  drifted copies and leaves their grain. using-git-worktrees, outside
  that record, is brought to crucible's grain. writing-skills keeps its
  wording-test measurements (`docs/decisions/authoring-crucible.md`).
  The entry's "upstream-derived supporting files brought to crucible's
  grain" reads, for this child, "where no decision record keeps
  upstream's text": a clarification of its own entry that changes
  nothing another entry waits on. Basis: the controller's proposal, the
  call delegated by the operator.
- **D4. The shared seat reference.**
  `skills/subagent-driven-development/references/premise-and-questions.md`
  grows into the shared seat reference and is renamed
  `skills/subagent-driven-development/references/seat-rules.md`, a
  basename clear of the host's report-name filter. It holds the clauses
  the seat templates share (the sections are pinned in Interfaces &
  boundaries) beside its existing sections. Each template keeps what
  only its seat does: its mandate line, which keeps "edit nothing but
  your report" inline for a read-only seat, its own read list, its
  route for a literal-reading case, its seat-specific lines and the
  paragraph telling the seat how to read the template. The list of
  justifications for a deleted test moves to
  `skills/subagent-driven-development/writing-good-tests.md`, which the
  four code-review seats already read. Basis: the entry, and the
  controller's design, accepted by the operator.
- **D5. Shared clauses are spliced at build time.** A seat receives the
  shared sections inside its own text, never by reading a file at
  startup: each template has a hand-edited source naming the shared
  sections it takes, and the generator, `tools/instrument_agents.py`,
  splices them in, writes the template file every host reads at its
  current path, and renders the Claude Code agents from it, as today.
  The suite's check mode fails a rendered file that is stale. Codex
  dispatch, which fills and sends the template file, is unchanged. The
  blind verifier's inputs are unchanged: its sections arrive spliced.
  This is the entry's "one shared seat reference ... in place of the
  clauses copied into the templates", held at the source: a
  clarification of the entry. Basis: the operator's proposal; the
  mechanism, the controller's, accepted by the operator. Why: a seat
  that skipped a startup read would lose the rules it carries, and
  nothing measures how often that happens; spliced text also gives each
  seat only its sections.
- **D6. Stdlib generator, no template engine.** The generator stays
  standard-library Python: it fills one slot and splices named sections.
  Reopen: adopt a template engine (Jinja2) once the generator needs
  conditionals or loops, or card filling moves into a script. Dev-time
  dependencies are acceptable to the operator, so a dependency is no
  bar then. Basis: the controller's proposal, accepted by the operator.
- **D7. Controllers keep only what they do.** A controller skill keeps
  the steps the controller takes and the inputs it fills; a seat's
  rubric and verdicts live in its template, a card's inputs on the
  card, and the rules every controller dispatch shares in
  `skills/subagent-driven-development/references/dispatch-composition.md`:
  reading the dispatch reference at the start and after compaction,
  reading the card rather than the template, confirming the report file.
  Basis: the controller's design, accepted by the operator.
- **D8. Host-neutral rules leave the adapters.** "Never predict an
  agent's result" and "name the model on every dispatch" go to the
  router, `skills/using-crucible/SKILL.md`, which every session loads,
  so an ad hoc dispatch is covered too; the definition of independent
  tasks goes to dispatching-parallel-agents' step 3, crucible's own text
  in that skill; "effort only on the operator's request" goes to
  `dispatch-composition.md`. The `ultra` effort level, a Codex term,
  leaves host-neutral text for the Codex dispatch reference. The adapters
  keep the mechanics. Basis: the controller's design, accepted by the
  operator.
- **D9. The router owns the decision ask's form.** Every route asks
  the operator something and every session loads the router, so the
  definition R1 settles lives there, in one sentence; redteaming,
  SDD, requesting-code-review, flip-paths and receiving-review point to
  it. Basis: the controller's call under D2's ruling.
- **D10. The adjudicator stays templateless.** It is the dispatch the
  controller composes; its diff procedure becomes the shared
  reference's, which the controller reads when composing it, and its
  mandate stays in SDD. Basis: the controller's design, accepted by the
  operator.
- **D11. Rationalization tables and red-flag lists stay** as a form
  writing-skills endorses; only an exact duplicate goes
  (requesting-code-review's Red Flags list, finishing's Quick
  Reference), and a rule found only in a table row, finishing's
  force-push rule, moves into the body first. Basis: the controller's
  design, accepted by the operator.
- **D12. Skills stay hand-written.** A controller loads several skills
  into one context and can follow a pointer; splicing a shared rule into
  each would put it before the controller once per skill and grow the
  `SKILL.md` files `compaction-fit` must fit. Basis: the controller's
  recommendation on the operator's question, accepted by the operator.
- **D13. Wrong-level text.** A passage telling how a rule was learned,
  or explaining a file's own design, is deleted where a decision record
  already holds it, and otherwise moves to the record that owns its
  topic, with that record's Changes line, or to `docs/authoring.md`.
  Basis: the placement rule (writing-skills' Size and placement bullet;
  `AGENTS.md`, Where text goes).
- **D14. Cross-skill anchor citations.** `docs/authoring.md`'s
  restriction of the `crucible:<skill> § <heading>` form to a frozen
  list is retired; the reference scanner, which fails a citation whose
  heading does not exist, is the guard. A heading rename stays an edit
  the suite checks. Basis: the controller's call; placement moves
  enough text that a hand-kept list would lag
  (`docs/backlog/cross-skill-anchor-citations.md`).
- **D15. Step names.** The two numbered step lists reached at one Finish
  are told apart by name: finishing-a-development-branch's Step 6 becomes
  "Remove the worktree" and says worktree where it means one, SDD
  § Finish's step 6 is named for deleting the feature workspace, and
  cross-references cite a step by its name and file. Basis: the
  controller's design, accepted by the operator.

## Constraints & invariants

- **P1. No rule is lost or changed.** Every rule a removed or moved
  passage stated is still stated at its owner, reached by the passage's
  reader through a pointer or a splice; the only changes in what a rule
  says are D1's corrections, D2's rulings and the entry's comment-rule
  change.
- **P2. One hand-edited source per spliced clause.** A rendered template
  and a generated agent are never edited by hand; the suite fails one
  that does not match its sources.
- **P3. Kept-close skills change only for defects** (D3).
- **P4. Host mechanics stay in the adapter pair** (`AGENTS.md`,
  Authoring rules); the claude-ism scanner passes.
- **P5. The SessionStart envelope stays under 10,000 characters.**

The umbrella's Constraints & invariants bind through the umbrella line.

## Interfaces & boundaries

**The splice.** A template source names each shared section it takes by
its heading in the shared seat reference; the generator renders each
template to its current path and each agent from its rendered template.
The rendered templates keep their paths, so every reader of a template
path (the dispatch references, the slot cards, the Codex dispatch, the
tests) is unchanged. The prose budget counts each hand-edited file once
and no rendered file.

- Deferred to implementation: the source files' naming and location, the
  include marker's form, and how the existing tests that read template
  text read it after the change.

**The shared seat reference's sections.** Other tasks cite these headings,
so they are pinned:

- § Seat conduct — all seats;
- § Read-only seats — all seats but the implementer: scratch, the suite
  bound, no re-run of a suite a report evidences, truncated evidence;
- § Report file — all seats;
- § What binds — every seat but the blind verifier, in a form for a seat
  reviewing a document and one for a seat reviewing a range;
- § Findings — severities, evidence, what is no finding, location;
- § Finding scope — redteam seat and terminal pass;
- § What shipped work carries — build history (R3), the comment rule,
  silence is not permission;
- § Tests in review — test-first exceptions, a removal's failing step;
- § Building the diff — task reviewer, re-reviewer, branch reviewer, and
  the adjudicator through its controller;
- § Concerns — task reviewer and re-reviewer;
- the existing § Premise findings, § Binding items and unrecorded
  choices, § The goal check, § Questions and § The arrangement
  questions, the last read by controllers directly.

**The owner map.** Each row: the rule, its owner, and what the other
sites become. A site not named keeps nothing of the rule beyond a
pointer where its reader needs one. The audit reports give the sites by
line at `8332a00`.

| Rule | Owner | Other sites |
|---|---|---|
| Seat-side shared clauses (the sections above) | the shared seat reference | spliced into the templates; `dispatch-composition.md` item 4 keeps its pointer and mandate line |
| What binds, controller side; "the spec is a hypothesis, read for intent" | `skills/redteaming/references/flip-paths.md`, its opening | brainstorming's spec contract, writing-plans' spec-pointer bullet and Binding vs advisory, SDD § Deviations: pointers |
| The umbrella chain and its finding rule (R2) | `umbrellas.md` § Children and § Edits | SDD, requesting-code-review, `very-small-lane.md`, writing-plans: pointers |
| Weakened and deleted tests, the justification list | `writing-good-tests.md` | each code-review template keeps its one-line angle |
| Dispatch reference read at start and after compaction; read the card, not the template; card Operation line; card Model and Effort lines; effort only on request; report file confirmed | `dispatch-composition.md` | SDD, redteaming, requesting-code-review, the seven cards: removed or a pointer |
| Never predict an agent's result; name the model on every dispatch; the decision ask's form (R1) | the router | the adapters keep the mechanics; redteaming, SDD, requesting-code-review, flip-paths, receiving-review: pointers |
| Independent tasks, for fan-out | dispatching-parallel-agents, step 3 | the adapters keep one clause each |
| Card inputs | the slot cards | SDD and requesting-code-review keep what the controller does with each seat's output |
| Task reviewer's rubric; terminal pass's mandates; re-reviewer's verdicts | their templates | SDD and redteaming keep the verdict names, the loop wiring and the inputs |
| Shared-tree rules; the replacement line | SDD § Shared-tree rules | redteaming keeps its window list and the fresh seat id |
| Operator rulings into the decision record and `request.md` | `skills/redteaming/references/formats.md` § Feature workspace root and layout | phase sites: a pointer |
| The delegated answer's entry form | brainstorming § Workspace provisioning (brainstorm exit) | `formats.md`: removed |
| Deferral boundaries; what is never deferrable; naming spec markers in Contracts | writing-plans § Deferring detail, with the fuller list of non-local mechanism | redteaming keeps the disposition rule; brainstorming: a pointer |
| No `Review: branch only` mark added once the plan's review closes | writing-plans § Per-task structure | `plan-phase.md`, `folded-lane.md`, SDD step 2: removed |
| The close readout lists marked tasks | redteaming § Round readout's close | `formats.md`, `plan-phase.md`, `folded-lane.md`: removed |
| Consumer sweep | brainstorming § Spec self-review | writing-plans' Files field: a pointer |
| Standing test and one-time check | writing-plans § Acceptance maps to checks | brainstorming's spec contract: a pointer |
| The plan phase is one round | `plan-phase.md` | redteaming: the read instruction |
| The folded preset | `folded-lane.md` (campaign); brainstorming § Proposing the arrangement (step 4) (entry) | redteaming, writing-plans: pointers |
| Ledger seeding at a close | `plan-phase.md` § Close | redteaming § Exit and `folded-lane.md`: one-way pointers |
| An open premise ask at an umbrella's landing | `umbrellas.md` § Landing | flip-paths, redteaming § Exit: pointers |
| A premise ask opens no wave and is never an open finding | flip-paths § Premise findings | redteaming, `formats.md`, SDD, requesting-code-review: pointers |
| Round readout contents | redteaming § Round readout | `formats.md`'s readout field: a pointer |
| Feature-folder birth and resolve | `formats.md` § Feature folder | brainstorming, writing-plans, the lane-note and folded-document references: pointers |
| Feature-worktree mechanics | using-git-worktrees | brainstorming keeps one line |
| The containment test | flip-paths § The containment test | SDD: pointers |
| The controller fixes nothing off the lane | SDD, once | requesting-code-review: a pointer |
| Deferred minors and leads reach the branch reviewer | requesting-code-review, its inputs | SDD: a pointer |
| Finish's red suite | SDD § Finish (classification and dispute); requesting-code-review (the wave) | finishing: a pointer |
| Drift found after the fact | SDD § Drift; requesting-code-review (how a repair rides a wave) | — |
| Drift on the lane | `very-small-lane.md` | SDD, requesting-code-review: pointers |
| The umbrella's receiving step | requesting-code-review (branch side); SDD (task side) | `very-small-lane.md`: a pointer |
| A lost workspace | `formats.md` | SDD: a pointer |

**The corrections.** What the text says after placement, where the copies
disagree today. Each is D1's correction or D2's ruling; a site the audit
names that is not listed here is a restatement only.

- The re-reviewer takes the full comment rule (the entry).
- The decision ask (R1), the umbrella finding rule (R2), the build-history
  exemption (R3) and the `literal-reading` label (R4).
- `formats.md`'s "delegated status" becomes brainstorming's entry form,
  `accepted — delegated to the controller` in the proposer's place.
- What is never deferrable: the fuller list of non-local mechanism.
- Where the trace carries decision-ask ids: `formats.md`'s scope, the
  numbered round record and the plan record.
- `folded-lane.md`'s "the round-1 seat carries the right-sizing and
  outside-the-frame lenses" goes: the lens roster applies unchanged.
- Lane drift: drift from the note's binding parts is a wave finding.
- Fan-out independence: no shared state, no ordering, neither reading the
  other's output.
- A controller filling a task-review or re-review card fills its
  amendment-commit slot (the cards' version).
- The report-file check covers every seat that owes a report file;
  requesting-code-review's controller reads `dispatch-composition.md`.
- A red-suite failure ruled not the branch's is recorded and not raised
  again while it fails the same way, in the branch review too.
- Every report-writing seat writes its report file even where the host
  advises returning findings as text; the suite bound is the task
  reviewer's fuller form; the terminal pass's findings carry a location
  (`docs/decisions/evidence-and-findings.md`).
- systematic-debugging's test-first copies follow its conditional line
  (`docs/decisions/upstream-skills-kept-close.md`).
- using-git-worktrees' Step 0 sends a feature started inside another
  feature's worktree to Step 1b, and its Quick Reference rows follow its
  body (instruction-file priority, the other-feature case of the ignore
  check, the five setup markers).
- The stale wording: flip-paths step 3's "scope finding" for a change on
  a task completed branch review only; the shared reference's pointer
  from § Premise findings into § The goal check; the plan-phase second
  read's "re-read the entire artifact" beside its narrower scope;
  brainstorming's open-items reader points to `formats.md` § Open items.

**Renames.** The rename of `premise-and-questions.md` reaches every file
citing it: the skills, the decision records and `docs/upstream.md` (no
test or tool names it at `8332a00`).

**Template consumers.** A template source is a new non-`SKILL.md` file
under `skills/`, so the structural checks that every such file is cited
and the claude-ism scanner reach it; the tests that read template text,
the generator's check mode and `agents/` read the rendered files.

**Shared files.** Every task edits skill text, and several edit the same
file (SDD, redteaming, `dispatch-composition.md`); the plan orders them.

## Acceptance

- **A1. Removal lists.** Each task's report lists every passage it removed
  or moved, beside the owner site that states its rule (P1). One-time:
  read by the task's reviewer, or, for a task completed branch review
  only, the branch reviewer.
- **A2. The splice.** Standing tests: the rendered templates and agents
  match their sources; every section a template source names exists in
  the shared seat reference; the prose budget counts each hand-edited
  file once and no rendered file.
- **A3. The corrections.** One-time: for each item of the corrections
  list, the command and output showing the text now says it, and no
  copy says otherwise.
- **A4. The suite.** Standing: the full suite passes, the reference
  scanner, the claude-ism scanner and the session-start budget among it.
- **A5. Sizes.** One-time, at the landing: the net word change against
  `8332a00`, the `SKILL.md` sizes against the 20,000-byte line, the
  envelope's size; `tests/prose-budget.txt` lowered to the new counts.
- **A6. Records and docs.** One-time: every decision record whose
  position moves (the generator and the splice in
  `docs/decisions/instruments.md`, placement of seat rules in
  `docs/decisions/authoring-crucible.md`, the adapters' content in
  `docs/decisions/runtime-adapters.md`, any record receiving moved text)
  carries the change and its Changes line; `docs/authoring.md` states
  D14.
- **A7. The backlog.** One-time: `docs/backlog/skill-text-rewrite.md`
  keeps only what stays open (the separability and tension-closing
  points, the two rule gaps, the umbrella-landing question, the
  missing-verdict action); `docs/backlog/cross-skill-anchor-citations.md`
  is deleted as resolved.
- **A8. The entry.** The umbrella's entry for `placement` carries D3's and
  D5's clarifications as this spec states them, and its mark at the
  finish.

## Mechanism sketches

Advisory.

- The include marker may be one line in a template source naming a
  section of the shared seat reference by its heading, replaced by that
  section's body; a missing heading fails generation.
- The task split, as a heads-up for the plan: the generator, the shared
  seat reference and the seven templates with their cards; redteaming
  and planning; brainstorming and its references; SDD,
  requesting-code-review, finishing and receiving-review; the router,
  adapters, `dispatch-composition.md` and dispatching-parallel-agents;
  using-git-worktrees and systematic-debugging; the docs and backlog.
- The audit reports' per-file estimates (templates about 3,500 words,
  review before code about 2,300, execution about 1,650, using-git-worktrees
  about 490) are where each task can expect its savings; they are no
  target.
