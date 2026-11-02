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
  upstream's text": the entry's literal reading reaches a case its
  author did not consider, a standing decision record, and this
  clarification, stated here and changing nothing another entry waits
  on, is the reading the controller chose under the operator's
  delegation. Basis: the controller's proposal, the call delegated by
  the operator.
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
  justifications for a deleted test joins § Tests in review, so it stays
  inside the text of each seat that carries it today. Basis: the entry,
  and the controller's design, accepted by the operator.
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
  clarification of the entry that changes nothing another entry waits
  on, since `compaction-fit` can still move text into or out of the
  shared reference (A8 updates the umbrella's line on it). A seat's rendered text carries the rules
  it carries today and no other (P6). It is build tooling, not a step
  any run performs, so it adds no process mechanism (the umbrella's
  Non-goals). Basis: the operator's question proposing it; the
  mechanism, the controller's, accepted by the operator. Why: a seat
  that skipped a startup read would lose the rules it carries, and
  nothing measures how often that happens; spliced text also gives each
  seat only its sections. The cost: where a controller fills a template
  itself (Codex, and Claude Code's fallback path), each dispatch carries
  the sections that seat used to read at startup, the existing
  § Premise findings and its siblings among them. It reverses the generator include
  `docs/decisions/instruments.md` lists as rejected: that objection, a
  resolution step on Codex, does not arise when the rendered template
  sits at the path Codex dispatch reads.
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
  `skills/subagent-driven-development/references/dispatch-composition.md`,
  which SDD and redteaming already have their controllers read before
  the first dispatch and after compaction, and requesting-code-review
  will (the corrections list): reading the card rather than the template,
  confirming the report file, and the shared-tree rules (the no-commit
  rule, the status check, the replacement line), which the redteaming
  and execution controllers both act on and neither reads from the
  other's skill. Each dispatching skill keeps one line telling its
  controller to read `dispatch-composition.md` and its dispatch reference
  when the skill starts and after compaction, since a reference is not
  re-attached after compaction and only the skill's own line sends the
  controller back to it. Basis: the controller's design, accepted by the
  operator; the shared-tree owner and the kept read line, the
  controller's calls after round 1.
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
- **D10. The adjudicator stays templateless.** It is a dispatch the
  controller composes; its diff procedure becomes the shared reference's
  § Building the diff, which the controller copies into its prompt
  (Interfaces & boundaries, Composed seats), and its mandate stays in
  SDD. Basis: the controller's design, accepted by the operator.
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
- **D16. The prose budget counts hand-edited prose.** Before this child
  every `*.md` under a skill directory was hand-edited, so the budget's
  count was the hand-edited count; from it on, the count takes each
  hand-edited file and no rendered template, and the umbrella's C1 is
  judged on that count. Counting rendered templates beside their sources
  would count spliced text twice and say nothing about what an author
  maintains. What a seat carries at dispatch, the rendered size, is
  reported beside it as information, the umbrella's resident-token
  measure being `compaction-fit`'s. Basis: the controller's call after
  round 1.

## Constraints & invariants

- **P1. No rule is lost or changed.** Every rule a removed or moved
  passage stated is still stated at its owner, reached by the passage's
  reader through a pointer or a splice; the only changes in what a rule
  says are D1's corrections, D2's rulings and the entry's comment-rule
  change.
- **P2. One hand-edited source per spliced clause.** A rendered template
  and a generated agent are never edited by hand; the suite fails one
  that does not match its sources.
- **P3. Kept-close skills change only for the reasons their record
  lists** (`docs/decisions/upstream-skills-kept-close.md`; D3).
- **P4. Host mechanics stay in the adapter pair** (`AGENTS.md`,
  Authoring rules); the claude-ism scanner passes.
- **P5. The SessionStart envelope stays under 10,000 characters.**
- **P6. Sharing adds no rule to a seat.** A template, or a dispatch
  the controller composes, takes a shared section only where each rule in
  it is one that seat follows today, by its own text or by a reference it
  reads today, or one the corrections give it; a rule some of a
  section's seats lack stays in the texts that carry it or takes a
  heading of its own. The rules a seat's rendered text or composed
  prompt states are the rules it follows today, changed only by D1's
  corrections, D2's rulings and the entry's comment-rule change.

The umbrella's Constraints & invariants bind through the umbrella line.

## Interfaces & boundaries

**The splice.** A template source names each shared section it takes by
its heading in the shared seat reference; the generator renders each
template to its current path and each agent from its rendered template.
The rendered templates keep their paths, so every reader of a template
path (the dispatch references, the slot cards, the Codex dispatch, the
tests) is unchanged. Each template source lives under `skills/`, beside
the template it renders, so the claude-ism scanner and the prose budget
reach it; the budget counts as D16 states. A spliced section keeps its
heading in the rendered template, and every citation of a shared
section in a rendered template names a section that template takes.

- Deferred to implementation: the source files' naming, the include
  marker's form, how an include works inside a selector passage and
  beside the cards' slot tokens, how a spliced section states a value
  that differs by seat (the scratch path's example), how the structural
  check that every non-`SKILL.md` file under `skills/` is cited reaches
  a source, and how the existing tests that read template text read it
  after the change.

**The shared seat reference's sections.** Other tasks cite these headings,
so they are pinned. Each names its content and its expected takers, read
from the audit; P6 decides the takers, and where a section's rules reach
different seats it splits under further headings, these staying:

- § Seat conduct — the worktree, other checkouts, no delegation, scoped
  reading; all seven seats;
- § Read-only seats — edit nothing, the scratch directory; the six
  seats other than the implementer;
- § Suite bound — focused checks only, heavy validation recommended;
  the redteam seat, verifier, terminal pass, task reviewer and
  re-reviewer, not the branch reviewer;
- § Review evidence — no re-run of a suite a report evidences,
  truncated evidence re-read at its path; task reviewer and re-reviewer;
- § Report file — the report contract the seven seats share;
- § What binds in a document — redteam seat and terminal pass;
- § What binds in a range — implementer, task reviewer, re-reviewer and
  branch reviewer;
- § Findings — severities, evidence, what is no finding; the seats
  raising findings;
- § Location — kept as today; its takers as today;
- § Finding scope — redteam seat and terminal pass;
- § What shipped work carries — build history (R3) and the comment
  rule; implementer, task reviewer, re-reviewer and branch reviewer;
- § Silence is not permission — task reviewer and branch reviewer;
- § Tests in review — test-first exceptions, a removal's failing step,
  the deleted-test justification list; the seats that state each today;
- § Building the diff — task reviewer, re-reviewer, branch reviewer, and
  the adjudicator;
- § Concerns — task reviewer and re-reviewer;
- the existing § Premise findings, § Binding items and unrecorded
  choices, § The goal check, § Questions and § The arrangement
  questions, the last read by controllers directly.

**Composed seats.** A dispatch the controller composes, with no template
(the round-0 pre-pass, the adjudicator, an umbrella's closing-review
seats), carries the text of the shared sections its seat follows,
copied by the controller from the shared seat reference into the
prompt, so no seat depends on a read at startup; P6 binds what it takes.
The skill that composes the dispatch names the sections, those its seat
follows today: redteaming § Round 0 — mechanical pre-pass (§ Suite
bound, and the scratch rule its prompt carries today), SDD § Disputes
and adjudication (§ Building the diff, § What binds in a range, which
replaces its pointer into SDD's Deviations paragraph, and its read-only
limits), `umbrellas.md` § Closing review (§ Premise findings, § Binding
items and unrecorded choices, § Questions, § Location, as today). The
snapshot-blessing agent takes none: its one-line mandate is all of it.

**The owner map.** Each row: the rule, its owner, and what the other
sites become. A site not named keeps nothing of the rule beyond a
pointer where its reader needs one. The audit reports give the sites by
line at `8332a00`. An owner that is a paragraph rather than a heading is
cited by the heading above it and the paragraph's label, since the
reference scanner checks a `§` citation against headings only.

| Rule | Owner | Other sites |
|---|---|---|
| Seat-side shared clauses (the sections above) | the shared seat reference | spliced into the templates; `dispatch-composition.md` item 4 keeps its pointer and mandate line, and its sentence on what a seat flags under an umbrella goes to the § What binds sections |
| What binds, controller side; "the spec is a hypothesis, read for intent" | `skills/redteaming/references/flip-paths.md`, its opening | brainstorming's spec contract, writing-plans' spec-pointer bullet and Binding vs advisory, the Deviations paragraph of SDD § 2. Handle the report: pointers |
| The umbrella chain and its finding rule (R2) | `umbrellas.md` § Children and § Edits | SDD, requesting-code-review, `very-small-lane.md`, writing-plans: pointers |
| Weakened and deleted tests, the justification list | the shared seat reference, § Tests in review | each code-review template keeps its one-line angle; `writing-good-tests.md` keeps its warning signs |
| Read the card, not the template; card Operation line; how a card's Model and Effort lines state the shared model rules; effort only on request; report file confirmed | `dispatch-composition.md` | SDD, redteaming, requesting-code-review, the seven cards: removed or a pointer; each card keeps the role its seat runs on |
| Read `dispatch-composition.md` and the dispatch reference when the skill starts and after compaction | each dispatching skill, one line (D7) | the three paragraphs it replaces in SDD, redteaming and requesting-code-review |
| Never predict an agent's result; name the model on every dispatch; the decision ask's form (R1) | the router | the adapters keep the mechanics; `dispatch-composition.md` § Models and effort, redteaming, SDD, requesting-code-review, flip-paths, receiving-review: pointers |
| Independent tasks, for fan-out | dispatching-parallel-agents, step 3 | the adapters keep one clause each |
| Card inputs | the slot cards | SDD and requesting-code-review keep what the controller does with each seat's output |
| Task reviewer's rubric; terminal pass's mandates; re-reviewer's verdicts | their templates | SDD and redteaming keep the verdict names, the loop wiring and the inputs |
| Shared-tree rules: the no-commit rule, the status check, the replacement line | `dispatch-composition.md`, a section of its own | SDD keeps its review-seat windows, redteaming its window list and the fresh seat id, requesting-code-review its pointer and its standalone-mode rule that `tree-check.txt` sits in the host's temporary directory; each reaches the rules through its read line (D7) |
| Operator rulings into the decision record and `request.md` | `skills/redteaming/references/formats.md` § Feature workspace root and layout | phase sites: a pointer |
| The delegated answer's entry form | brainstorming § Workspace provisioning (brainstorm exit) | `formats.md`: removed |
| Deferral boundaries; what is never deferrable, with the fuller list of non-local mechanism; naming spec markers in Contracts | writing-plans § Deferring detail; for seats, the shared seat reference's § Finding scope (a paired text) | redteaming keeps the disposition rule, its list replaced by a pointer; brainstorming: a pointer |
| No `Review: branch only` mark added once the plan's review closes | writing-plans § Per-task structure | `plan-phase.md`, `folded-lane.md`, SDD step 2: removed |
| The close readout lists marked tasks | redteaming § Round readout's close | `formats.md`, `plan-phase.md`, `folded-lane.md`: removed |
| Consumer sweep | brainstorming § Spec self-review | writing-plans' Files field: a pointer |
| Standing test and one-time check | writing-plans § Acceptance maps to checks | brainstorming's spec contract: a pointer |
| The plan phase is one round | `plan-phase.md` | redteaming: the read instruction |
| A route's entry in the brainstorm decision record, the upgrade hatch's included | brainstorming § Proposing the arrangement (step 4) | `very-small-lane.md`: a pointer |
| The folded preset | `folded-lane.md` (campaign); brainstorming § Proposing the arrangement (step 4) (entry) | redteaming, writing-plans: pointers |
| Ledger seeding at a close | `plan-phase.md`, its Close paragraph | redteaming § Exit and `folded-lane.md`: one-way pointers |
| An open premise ask at an umbrella's landing | `umbrellas.md` § Landing | flip-paths, redteaming § Exit: pointers |
| A premise ask opens no wave and is never an open finding | flip-paths § Premise findings | redteaming, `formats.md`, SDD, requesting-code-review: pointers |
| Round readout contents | redteaming § Round readout | `formats.md`'s readout field: a pointer |
| Feature-folder birth and resolve | `formats.md` § Feature folder | brainstorming, writing-plans, the lane-note and folded-document references: pointers |
| Feature-worktree mechanics | using-git-worktrees | brainstorming keeps one line |
| The containment test | flip-paths § The containment test | SDD: pointers |
| The controller fixes nothing off the lane | SDD, once | requesting-code-review: a pointer |
| Deferred minors and leads reach the branch reviewer | requesting-code-review, its inputs | SDD: a pointer |
| Finish's red suite | SDD § Finish (classification and dispute); requesting-code-review (the wave) | finishing: a pointer |
| Drift found after the fact | SDD § Drift found after the fact; requesting-code-review (how a repair rides a wave) | — |
| Drift on the lane | `very-small-lane.md` | SDD, requesting-code-review: pointers |
| The umbrella's receiving step | flip-paths § Under an umbrella: binding changes and late splits, its Receiving paragraph | requesting-code-review and SDD keep their checkpoints (before each pass and wave; before each task's BASE); `very-small-lane.md`: a pointer |
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
- The suite bound is the task reviewer's fuller form of the bound
  itself (no package-wide suite, race-detector run or repeated or
  high-count loop; heavy validation recommended instead), not its
  sentence on when to run a test; the terminal pass's findings carry a location
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

**Paired texts.** Three rules are stated twice on purpose, once for the
controllers and authors who act on them and once, spliced, for the seats
that do: what binds and "the spec is a hypothesis, read for intent"
(flip-paths' opening; § What binds in a document and § What binds in a
range), the umbrella finding rule (`umbrellas.md` § Edits; § What binds
in a document and § What binds in a range), and the list of non-local
mechanism (writing-plans
§ Deferring detail; § Finding scope). The controller-side text is the
primary; `docs/authoring.md` lists the pairs, and a change to one side
changes the other in the same commit.

**Not a correction.** The sentence that a report file is required even
where the host advises returning findings as text stays where it stands,
in the verifier and re-reviewer templates alone, not in § Report file:
`docs/decisions/instruments.md` rejects seat-facing wording against
skipped report writes, and those two seats carry it as a targeted fix
(`docs/backlog/review-seat-report-write.md`).

**Renames.** The rename of `premise-and-questions.md` reaches every
file citing it: the skills,
the decision records, `docs/upstream.md`, `docs/backlog/skill-text-rewrite.md`
and the generated `agents/` (no test or tool names the file at
`8332a00`). A renamed heading (D15), and SDD § Shared-tree rules moved
into `dispatch-composition.md` (D7), reach their citers the same way,
`docs/decisions/git-steps.md` among them.

**Template consumers.** The tests that read template text, the
generator's check mode and `agents/` read the rendered files. Three
texts call the template the hand-edited home of its text and `agents/`
the one generated artifact, and change with D5: `AGENTS.md` (Authoring
rules, `agents/` is generated), `docs/dual-runtime.md` (its layout and
its statement that no runtime gets a generated skill tree) and the
generator's own docstring; so do `docs/decisions/runtime-adapters.md`
and the docstring of `tests/test_codex_manifests.py`, which say the
same. The counting basis is stated in `tests/prose-budget.txt`'s header,
`tests/test_prose_budget.py`'s docstring, `AGENTS.md` (The prose budget)
and `docs/decisions/authoring-crucible.md` (The prose budget), which
change with D16; `AGENTS.md`'s Where text goes says the templates
"point to" the shared reference, which changes with D5. Where no seat
reads the shared reference at startup any more, a card's plugin-root
slot whose only use was that read goes, with redteaming § Dispatch
composition's listing of the reference among the seats' inputs and
`docs/decisions/instruments.md`'s reason for the slot; a slot still used
for another file stays.

**Shared files.** Every task edits skill text, and several edit the same
file (SDD, redteaming, `dispatch-composition.md`); the plan orders them.

## Acceptance

- **A1. Removal lists.** Each task's report lists every passage it removed
  or moved, beside the owner site that states its rule (P1), and, for
  each template it renders, any rule the rendered text states that the
  template did not state before, which must be a correction (P6).
  One-time: read by the task's reviewer, or, for a task completed branch
  review only, the branch reviewer.
- **A2. The splice.** Standing tests: the rendered templates and agents
  match their sources; every section a template source names exists in
  the shared seat reference; every citation of a shared section in a
  rendered template names a section that template takes; the prose
  budget counts as D16 states.
- **A3. The corrections.** One-time: for each item of the corrections
  list, the command and output showing the text now says it, and no
  copy says otherwise; for each paired text, that its two sides agree.
- **A4. The suite.** Standing: the full suite passes, the reference
  scanner, the claude-ism scanner and the session-start budget among it.
- **A5. Sizes.** One-time, at the landing: the net word change against
  `8332a00` on D16's count, which C1 is judged on, with each rendered
  template's size beside it, the `SKILL.md` sizes against the 20,000-byte line, the
  envelope's size; `tests/prose-budget.txt` lowered to the new counts.
- **A6. Records and docs.** One-time: every decision record whose
  position moves (the generator and the splice in
  `docs/decisions/instruments.md`, placement of seat rules in
  `docs/decisions/authoring-crucible.md`, the adapters' content in
  `docs/decisions/runtime-adapters.md`, any record receiving moved text)
  carries the change and its Changes line, `instruments.md` dropping its
  rejection of a generator include and stating the verifier and
  re-reviewer exception to its rejected report-write wording; the texts Template
  consumers names say what D5 makes true and D16 changes; every citation of a renamed file or
  heading resolves; `docs/authoring.md` states D14 and lists the paired
  texts.
- **A7. The backlog.** One-time: `docs/backlog/skill-text-rewrite.md`
  keeps only what stays open: the resident-cost reopen trigger, which
  `compaction-fit` restates or retires; the separability and
  tension-closing points; the two rule gaps; the umbrella-landing
  question; and, added, the action on a review missing a verdict. The
  vocabulary-sprawl point goes as settled: the retirements removed the
  labels `review-retirements` listed, and those left belong to
  mechanisms the umbrella keeps (its D4, D5 and D6). `docs/backlog/cross-skill-anchor-citations.md` is deleted
  as resolved.
- **A8. The umbrella.** The umbrella's entry for `placement` is not
  reworded: D3 and D5 state its clarifications here, and the entry takes
  only its mark at the finish. The umbrella's Interfaces & boundaries
  line on what `placement` provides says the templates take the shared
  seat reference by splice, a lightly held edit on this branch.

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
