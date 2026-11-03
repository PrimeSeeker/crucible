# Compaction fit — implementation plan

Spec: `docs/crucible/2026-11-03-compaction-fit/design.md` @ `9e90380` — binding: its Constraints & invariants (moved text keeps what it requires, with the rule changes it lists; the spine of D3 stays in each `SKILL.md`; every body at or under 18,000 characters and no new skill; headings stay citable); it records no firm decision and declares no binding preamble convention; through its `Umbrella:` line, this feature's own entry (`compaction-fit`) in `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md` and that umbrella's Constraints & invariants (C1–C4), each seat reading them in its worktree. A task calling for a change to those Constraints, or to the entry other than its mark, is a plan defect.

## Goal

Every `SKILL.md` body is at or under 18,000 characters, held by a structural test: SDD, redteaming and brainstorming keep their spine (D3) and move long step bodies into references read at their step, under one statement per skill of what a stub means (D4). The authoring rule, its decision record, writing-skills and `AGENTS.md` state the line and the widened rule; the branch reviewer takes § The arrangement questions only on the very-small lane; resident tokens per route are counted at `a3db87f`, `d78398c` and the head; the resident-cost trigger is retired and the backlog says what stays open; the prose budget's sum is no higher than at `d78398c`.

## Task dependency order

T1 → T2 → T3 → T4 → T5 → T6, one at a time. T1 writes D4's statement, which T2, T3 and T4 consume; T1–T3 each fit one skill and keep the suite green on their own; T4 lands the size test once all three fit, with the rule sites; T5 depends on none of T1–T4 and runs after them only to keep one writer on the tree; T6 measures the head the other five leave and closes the records and the prose-budget sum.

## File ownership + overlap census

Each file has one owning task (first column); a file another task also edits is listed with that task. Rendered templates and `agents/` are generator output: the task that changes a source regenerates them, and the generator's check mode is their test. Every task that edits a decision record takes `.crucible/compaction-fit/brainstorm-decisions.md` as an input, for each position's basis.

| File | Owner | Also edited by |
|---|---|---|
| `skills/subagent-driven-development/SKILL.md` | T1 | — |
| new references under `skills/subagent-driven-development/references/` (names deferred, T1) | T1 | — |
| `skills/redteaming/SKILL.md` | T2 | — |
| new references under `skills/redteaming/references/` (names deferred, T2) | T2 | — |
| `skills/brainstorming/SKILL.md` | T3 | — |
| new reference under `skills/brainstorming/references/` (name deferred, T3) | T3 | — |
| `tests/test_skill_references.py` | T1 (its `EXPECTED` pairs) | T2, T3 (their pairs); T4 (docstring) |
| `tests/prose-budget.txt` | T1 (SDD line) | T2 (redteaming), T3 (brainstorming), T4 (writing-skills), T5 (requesting-code-review) — each its own line only |
| the structural size test (new; name deferred, T4) | T4 | — |
| `tests/skill_corpus.py` (docstring) | T4 | — |
| `docs/decisions/authoring-crucible.md` | T4 (the rule paragraph, D4's convention, the line's measurement, the "byte or word target" entry, its Changes line) | T6 (the resident-token figures, the full-rewrite entry and the trigger, its Changes line) |
| `skills/writing-skills/SKILL.md` | T4 | — |
| `AGENTS.md` | T4 | — |
| `docs/upstream.md` | T4 | — |
| `skills/requesting-code-review/code-reviewer.source.md`, `code-reviewer.slots.md`; rendered `code-reviewer.md`; `agents/branch-reviewer.md` | T5 | — |
| `docs/decisions/instruments.md` | T5 | — |
| `docs/backlog/skill-size-after-compaction.md`, `docs/backlog/skill-text-rewrite.md`, `docs/backlog/skill-rewrite-reaudit.md` | T6 | — |
| the resident-token manifests, figures and, if committed, the counting script (new; location deferred, T6) | T6 | — |

Overlaps are ordered by the dependency order: `tests/test_skill_references.py` T1 → T2 → T3 → T4; `tests/prose-budget.txt` T1 → T2 → T3 → T4 → T5, each task its own line; `docs/decisions/authoring-crucible.md` T4 → T6. The existing route references (`very-small-lane.md`, `plan-phase.md`, `folded-lane.md`, `flip-paths.md`, `folded-lane-document.md`, `lane-note.md`, `umbrellas.md`) are not edited: only their stubs in the owning `SKILL.md` change. Citations elsewhere of a moved section's heading resolve through the stub and change nowhere (spec, Interfaces & boundaries).

## Inter-task contracts

- **D4's statement.** T1 writes it near the top of the SDD `SKILL.md`; T2 and T3 write the same statement in theirs, changed only where a skill's own noun differs; T4 records the convention, quoting no wording that diverges from T1's. Its content is D4's; its wording is T1's.
- **The stub.** Every new stub is one paragraph under the moved heading, carrying a sentence `tests/skill_corpus.py`'s `STUB_RE` matches (``read `skills/<skill>/references/<file>.md` in full``), its trigger and any spine item of D3 its step keeps; its reference opens with the stub's heading and has no other stub, and its basename does not open with REPORT, SUMMARY, FINDINGS or ANALYSIS, case-blind (the host refuses a subagent's write to such a file: `skills/using-crucible/references/claude-code-dispatch.md`, Report-name filter). Each task adds its pairs to `EXPECTED` in `tests/test_skill_references.py`.
- **The body measure.** T1–T3 measure a body as the characters after the frontmatter's closing fence and hold it at or under 17,999, so it passes whichever boundary T4 fixes; T4's test fixes the boundary (its marker) and reads every `skills/*/SKILL.md`.
- **The prose budget.** Each of T1–T5 offsets its own additions within its skill directory by D6's rule and lowers or raises its own line to the new count, stating its net in its report; T6 checks the sum against `d78398c`'s (56,979). A task that cannot offset within its skill reports its net, and the sum carries it: only a sum above 56,979 at T6 is a shortfall, which goes to the operator as D6 states, never as an edit to the umbrella on this branch.
- **The counted head.** T6 counts the HEAD at its start, which carries T1–T5.
- **The reviewer's selector.** T5 keys the splice on the branch reviewer card's existing `lane` selector, value `very-small`.

## Acceptance mapping

| Spec criterion | Task | Check |
|---|---|---|
| A1 body at or under 18,000, standing test naming its reader | T4 (T1–T3 bring the bodies there) | standing test (new); T1–T3 a one-time measurement each |
| A2 the decision record states the line | T4 | why not a test: prose, read in review |
| A3 the spine stays; each stub carries its trigger | T1, T2, T3 | why not a test: prose fidelity, judged by task review and the branch review |
| A4 moved text compared word by word; offset removals listed | T1, T2, T3 (T4, T5 for their removals, if any) | one-time check each |
| A5 the stub set test passes | T1, T2, T3 | standing test (`tests/test_skill_references.py`) |
| A6 the prose budget sum at or below `d78398c` | T6 (each of T1–T5 its own line) | standing test (`tests/test_prose_budget.py`) per line; one-time check of the sum |
| A7 the rule sites of D4, D5 and D8 | T4 (D4, D5), T6 (D8) | why not a test: prose, read in review |
| A8 the reviewer's section only under the lane selector | T5 | standing test (the generator's check) for the rendering; a read in review for the placement |
| A9 resident tokens per route, manifests and figures committed | T6 | one-time check (the counting run's output) |
| A10 the backlog matches D10 | T6 | one-time check (the files read in review) |
| A11 the full suite passes on the head | every task; Finish | the suite's run |

## Tasks

### T1 — SDD under the line

**Why.** SDD is the largest skill (37,483 characters of body) and the one whose cut has lost its cap upstream. It moves § The Task Loop (as one reference), Setup's step-local text, § Disputes and adjudication, § What a report voices, § Drift found after the fact, § Inline mode and § Finish into references, keeping its spine (D3): the ledger rules and the rules binding every dispatch or resume as a kept section, the cap of three fix waves and its ask and the close readout's answer in their stubs, the main/master consent, the dispatch-references line, the rationalization table. It writes D4's statement, which the other skills copy.

**Files.** `skills/subagent-driven-development/SKILL.md`; its new references; `tests/test_skill_references.py` (`EXPECTED`); `tests/prose-budget.txt` (SDD line). Consumers checked, none edited: `skills/subagent-driven-development/references/very-small-lane.md` and `skills/requesting-code-review/SKILL.md` (they cite § Finish, § Disputes and adjudication and § The Task Loop, step N, which resolve through the kept headings); `skills/redteaming/references/flip-paths.md` (line 54) and `very-small-lane.md` (line 11), which cite § Setup for the ledger rules and are reached because those rules stay under § Setup (Contract); `tests/test_instrument_dispatch_skills.py` (reads the skill through its stub corpus).

**Contract.** Enacts D3, D4 (writes the statement; the very-small-lane stub drops what it carries; the flip-paths stub keeps its after-compaction line), D6 (SDD's offsets). Produces the statement (Inter-task contracts) and SDD's `EXPECTED` pairs. The ledger rules and the rules binding every dispatch or resume stay within § Setup, under a subheading directly below its stub (the stub test allows one paragraph under the stub's heading), so citations of `crucible:subagent-driven-development` § Setup reach them. Owns the spec's marker at Mechanism sketches § Indicative allocation, for SDD's sites.

Deferred to implementation: the reference file names and the exact text boundaries, within D3 and the stub contract.

**Acceptance.**
- Happy: the body measures at or under 17,999 characters (one-time measurement); the suite passes; every moved heading keeps a stub that names its reference and trigger.
- Edge: a compaction mid-task — the statement sends the controller to the task loop's reference before it acts, and the cap and its ask are in the stub; the very-small lane's citation of § Finish lands on the stub; `§ The Task Loop, step N` citations still resolve.
- Error: a bare `§` citation inside moved text left unqualified is a finding; a stub of two paragraphs fails `tests/test_skill_references.py`.
- Integration: the A4 comparison of every passage that left the `SKILL.md` against its reference, each difference listed, and each offset removal listed with the passage that still states it; the SDD prose line and its net reported (Inter-task contracts, The prose budget).

### T2 — Redteaming under the line

**Why.** Redteaming (33,183 characters) moves § Panels (its degraded-round escalation kept in the stub), § Merge and finding hygiene (§ Operating stance — baseline error rate staying as its own section, so its two citations stand), § Fix application and blind verification and § Round readout; § Stop rule and terminal pass, § Inputs and state's rehydration, artifact freeze and shared-tree rules, and the round cap stay (D3).

**Files.** `skills/redteaming/SKILL.md`; its new references; `tests/test_skill_references.py` (`EXPECTED`); `tests/prose-budget.txt` (redteaming line). Consumers checked, none edited: `skills/redteaming/references/plan-phase.md` (it cites § Panels, § Merge and finding hygiene, § Fix application and blind verification, § Inputs and state and § Stop rule and terminal pass, which resolve through the kept headings); `folded-lane.md` (it cites § Exit and § Flip paths, which stay).

**Contract.** Enacts D3, D4 (consumes T1's statement; the plan-phase and folded-lane stubs drop what it carries; the flip-paths stub keeps its line), D6. Owns the allocation marker for redteaming's sites.

Deferred to implementation: the reference file names and the exact text boundaries, within D3 and the stub contract.

**Acceptance.**
- Happy: the body at or under 17,999 characters (one-time measurement); the suite passes.
- Edge: a compaction mid-campaign — the rehydration rule and the statement send the controller to the reference of the phase in progress; two consecutive degraded rounds still escalate from the spine.
- Error: as T1's.
- Integration: the A4 comparison as in T1; the redteaming prose line and its net reported.

### T3 — Brainstorming under the line

**Why.** Brainstorming (20,959 characters) moves § Proposing the arrangement (step 4), the operator's confirmation of the preset staying in its stub (D3); its hard gate and campaign gate stay.

**Files.** `skills/brainstorming/SKILL.md`; its new reference; `tests/test_skill_references.py` (`EXPECTED`); `tests/prose-budget.txt` (brainstorming line). Consumers checked, none edited: the sites citing `crucible:brainstorming` § Proposing the arrangement (step 4) (they resolve through the kept heading).

**Contract.** Enacts D3, D4 (consumes T1's statement; the folded-lane-document and lane-note stubs drop what it carries; the umbrellas stub keeps its line), D6. Owns the allocation marker for brainstorming's site.

Deferred to implementation: the reference file name and the exact text boundary, within D3 and the stub contract.

**Acceptance.**
- Happy: the body at or under 17,999 characters (one-time measurement); the suite passes.
- Edge: the step-4 stub states that the operator confirms the preset and that the route entry is recorded; the very-small lane's draft-and-show sequence is reached through it.
- Error: as T1's.
- Integration: the A4 comparison as in T1; the brainstorming prose line and its net reported.

### T4 — The line's test and the rule sites

**Why.** With the three skills under the line, a standing test holds every `SKILL.md` there, and the texts that state the authoring rule say what it now is: the line (D1), the widened rule (D5) and the read convention (D4).

**Files.** The new structural size test; `tests/skill_corpus.py` and `tests/test_skill_references.py` (docstrings); `docs/decisions/authoring-crucible.md` (the Route-conditional procedures paragraph of § Decision, with D4's convention in place of the per-stub re-read; the line's measurement with the documentation's wording, the measured cut, upstream #2481, the unit and the 18,000 line; the Rejected entry "A byte or word target", narrowed; its `## Changes` line); `skills/writing-skills/SKILL.md` (Size and placement); `AGENTS.md` (the line beside the always-loaded budget); `docs/upstream.md` (the row for upstream's size test); `tests/prose-budget.txt` (writing-skills line). Input: `.crucible/compaction-fit/brainstorm-decisions.md` (entries 4, 7, 20 for the positions' bases).

**Contract.** Enacts D1, D4 (records it), D5. Consumes T1's statement. Owns the spec's marker at Mechanism sketches § Counting (the body boundary).

Deferred to implementation: the test's file name and how it reports a failing skill.

**Acceptance.**
- Happy: the test passes on the head and its comment names the host's re-attachment after compaction as its reader; the record states the line (A2).
- Edge: a `SKILL.md` with no frontmatter, or one exactly at the line.
- Error: the test fails, naming the skill and its size, when a body is grown past 18,000 (shown by a one-time run against a padded copy outside the tracked tree, or before T1–T3's state, recorded in the report).
- Integration: the scanner (`tests/test_references.py`) passes over the edited records and docs.

### T5 — The branch reviewer's arrangement section, on the lane only
Review: branch only — one splice moved inside an existing selector passage, its line of purpose and two record sites; nothing later builds on how it is done.

**Why.** Off the very-small lane the branch reviewer has no use for § The arrangement questions; on the lane the upgrade hatch keys on the reviewer's finding or question (D9).

**Files.** `skills/requesting-code-review/code-reviewer.source.md`; `code-reviewer.slots.md` (the `lane` description); the rendered `code-reviewer.md` and `agents/branch-reviewer.md` (regenerated); `docs/decisions/instruments.md` (the splice paragraph and a `## Changes` line); `tests/prose-budget.txt` (requesting-code-review line). Input: `.crucible/compaction-fit/brainstorm-decisions.md` (entry 12).

**Contract.** Enacts D9. Consumes the card's `lane` selector.

**Acceptance.**
- Happy: the rendered template carries the section only inside the `lane = very-small` passage, with its line of purpose; `python tools/instrument_agents.py check` passes.
- Edge: the rendering with `lane` set `off` holds no part of the section.
- Error: the source edited but the rendered template or agent not regenerated fails `python tools/instrument_agents.py check`.
- Integration: the suite passes.

### T6 — Resident tokens, the retired trigger and the backlog

**Why.** The umbrella's outcome figure (D1 of the umbrella; spec D7), the trigger's retirement (D8) and the backlog's dispositions (D10) close the child; the prose-budget sum closes C1.

**Files.** The resident-token manifests and figures (new, committed) and, if committed, the counting script; `docs/decisions/authoring-crucible.md` (the figures as the baseline; the Rejected full-rewrite entry and the trigger; its `## Changes` line); `docs/backlog/skill-size-after-compaction.md`, `docs/backlog/skill-text-rewrite.md`, `docs/backlog/skill-rewrite-reaudit.md`. Input: `.crucible/compaction-fit/brainstorm-decisions.md` (entries 10, 11, 13).

**Contract.** Enacts D7, D8, D10. Consumes the head T1–T5 leave. Owns the spec's marker in D7 (the manifests' file lists) and the resident-token sketch's marker (where the counting script lives). The token-counting endpoint is reached with an Anthropic API key held in an environment variable the controller names at dispatch; the endpoint is the only API call made. The figures name the revision they count.

Deferred to implementation: the manifests' location in the feature folder and their format.

**Acceptance.**
- Happy: per-route, per-phase totals at `a3db87f`, `d78398c` and the head, the head named by its revision, the counting run's output quoted in the report (A9); the backlog files read as D10 states (A10); the prose-budget sum at or below 56,979 (A6, one-time).
- Edge: a file renamed between the counted points counted under its role; a route reference that does not exist at `a3db87f` counted as absent.
- Error: a sum above 56,979 is reported as the shortfall D6 routes to the operator, not committed around.
- Integration: the full suite passes on the head.
