# Compaction fit: every skill whole after compaction

Umbrella: `docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`

## Intent

**Problem.** After compaction, Claude Code re-attaches the most recent
invocation of each skill, cut at a fixed size. Three `SKILL.md` files
are over that size at `d78398c`: subagent-driven-development (37,483
characters of body), redteaming (33,183) and brainstorming (20,959).
A controller working from a cut copy loses the steps past the cut: at
`d78398c`, with a typical header line, SDD's cut falls inside
§ Disputes and adjudication, before drift, inline mode, plan changes
and Finish; redteaming's inside § Fix application and blind
verification, before its readout, stop rule and exit; brainstorming's
at § Handoff. The router tells an agent to invoke
a cut skill again, which loads a second full copy; whether agents
follow it is unmeasured. Upstream met the same failure (a session that
lost the fix loop's cap ran 18 rounds) and moved always-run sections
into references read at their step.

**The line, measured** (2026-11-03). The host's documentation ("Extend
Claude with skills", read 2026-11-03) says the first 5,000 tokens of
each skill are kept, within a combined budget of 25,000 tokens filled
from the most recently invoked skill. In a maintainer session that day
the re-attached copies of SDD and redteaming (0.13.0) were both cut at
exactly 19,902 characters of header and body, before the truncation
notice: the header line (`Base directory for this skill: <path>`), then
the body without its frontmatter. By the real tokenizer those cuts hold
6,775 and 6,620 tokens. Upstream's issue #2481 (obra/superpowers)
records the same cut publicly: each re-attached copy "cut to exactly
20,000 characters", ending in the truncation notice, whose 98
characters bring 19,902 to 20,000. The host's 5,000 tokens are
therefore an estimate at four characters a token, and the line is
about 20,000 characters, counted as the host counts them, not 5,000
tokenizer tokens. Token counts of every `SKILL.md` at `d78398c` (the
token-counting endpoint, Opus and Sonnet identical): SDD 12,898,
redteaming 11,003, brainstorming 6,955, requesting-code-review 4,806,
the other eight between 1,001 and 3,951; 2.66 to 3.18 bytes a token.

**Goals.**

- **G1.** Every `SKILL.md` fits under the line, so the host re-attaches
  it whole; a structural test keeps it there (umbrella G3).
- **G2.** The effort's outcome figure: resident tokens per route before
  the effort, before this child and after it (umbrella D1).
- **G3.** Settle the open items the umbrella entry and `placement` left
  to this child: the authoring rule on what a `SKILL.md` holds, the
  resident-cost re-open trigger, and the branch reviewer's
  arrangement-questions section.

**Non-goals.**

- Changing any rule. Text moves; what it requires stays (umbrella C3).
- New skills. No step becomes a skill of its own (D2).
- The other open items in `docs/backlog/skill-text-rewrite.md`: the two
  rule gaps, the action on a review missing a verdict, the closing-review
  seats' report form, the plugin-root exception, the umbrella-landing
  question. They are not size questions and stay in the backlog.
- Stale skill copies after a plugin update (D10): a separate failure,
  left open.
- Claims about how Codex treats skills across compaction: unknown, and
  not needed by the design (D11).

## Decisions

- **D1. The line and its test.** The line is the host's cut: about
  20,000 characters of re-attached text, the header line with its
  install path, the body without frontmatter and the truncation notice
  counted together. The structural test holds each `SKILL.md` body,
  frontmatter excluded, at or under **18,000 characters**; the margin
  covers long install paths, which the header carries, and small edits.
  The decision record keeps both the documentation's wording and the
  measured cut, with their dates, citing upstream #2481 as the public
  record of the cut. Basis: measured; the controller's proposal,
  accepted by the maintainer.
- **D2. Step references, no split.** An oversized `SKILL.md` keeps its
  spine (D3) and moves long step bodies into references beside it, as
  route-conditional procedures moved before. No step becomes a skill:
  a new skill adds to the always-loaded skill index, spreads the
  combined re-attach budget over more skills, and turns a step into a
  skill invoked mid-flow by name. The one candidate weighed, SDD's
  Finish merged into `finishing-a-development-branch`, would bring that
  skill near the line, and finishing's other callers (an umbrella's
  landing, a standalone branch) have no ledger or workspace to check.
  Basis: the controller's proposal, accepted by the maintainer, who
  asked for split-off candidates; the controller's weighing of them.
- **D3. What the spine keeps.** A `SKILL.md` keeps what a controller
  needs before it knows which step it is in, and what bounds its loop:
  the overview; the steps in order, each with its trigger and, for a
  moved step, its stub; the resume and rehydration rules; every cap and
  termination guarantee (a loop's cap, the rule that a phase ends with
  its terminal pass); the operator gates, the points where the flow
  itself waits for the operator's answer before going on (brainstorming's
  hard gate and campaign gate, the close readout's answer); the
  rationalization and red-flag tables. A rule that applies only within
  one step moves with that step, a stop-and-ask line that fires on a
  condition met inside the step included (the seat-replacement line
  moves with § Panels; `dispatch-composition.md` § Shared-tree rules
  stays its owner). A moved step's trigger, its cap with what follows
  the cap (SDD's ask after the third fix wave) and its operator gate
  (brainstorming's step-4 confirmation of the preset, the close
  readout's answer) stay as sentences of its stub's one paragraph, and
  the reference does not restate them. Basis:
  the controller's proposal, accepted by the maintainer; caps stay in
  the spine because upstream's incident was a lost cap.
- **D4. The read convention is unchanged.** A moved step keeps its
  heading in the `SKILL.md` with a stub that names the reference, says
  when to read it in full, says it binds as if written there and is
  re-read after compaction: the form route-conditional stubs use, which
  `tests/skill_corpus.py` follows. A reference is read in full when its
  step first comes, not before every round as upstream reads its fix
  loop: it stays in context until compaction, and the stub sends the
  controller back after. Basis: the controller's proposal, accepted by
  the maintainer.
- **D5. The authoring rule widens.** The paragraph "Route-conditional
  procedures live in references" in `docs/decisions/authoring-crucible.md`
  § Decision becomes the rule for both: a `SKILL.md` stays under the line; route-conditional
  procedures live in references, and so do long step bodies where the
  line needs it, the spine (D3) staying. writing-skills' Size and
  placement bullet states the general rule for any skill a host cuts
  after compaction, and `AGENTS.md` states the line beside the
  always-loaded budget. Basis: the umbrella entry leaves the widening
  to this child; the controller's proposal, accepted by the maintainer.
- **D6. The prose budget's offset.** The stubs add words, about 50 to
  80 each (the existing stubs run 29 to 72 words, more where a trigger
  or cap sits in the stub). Umbrella C1 forbids net growth: the offset comes from wording
  the move makes redundant (a pointer between sections that end up in
  one file, a restated context the reference no longer needs), never
  from weakening a rule. Where it cannot be met that way, the shortfall
  goes to the operator as a decision ask. Basis: the controller's
  proposal, accepted by the maintainer.
- **D7. Resident tokens per route.** For each route (standard, folded,
  very-small, an umbrella's own campaign), a manifest lists the files a
  controller loads, by phase: the session-start text (router and host
  map), the skills it invokes, the references that route reads and the
  host's dispatch reference. The same manifest roles are counted at
  `a3db87f` (the effort's baseline), `d78398c` (this child's base) and
  this child's head, with the token-counting endpoint, and the figures
  go into the decision record and the close readout. A file renamed
  between those points is counted under its role. The manifests are
  Claude Code's: the tokenizer is Anthropic's, and the host files
  counted are this host's; the skill text is shared, so Codex's figures
  would differ only by its host map and dispatch reference. Basis: umbrella D1;
  the controller's proposal, accepted by the maintainer.
- **D8. The resident-cost re-open trigger is retired.** It said when a
  full rewrite of the controller skills would be worth reopening; that
  rewrite is this umbrella. Growth is now held word by word by the prose
  budget, per skill by the line's test, and in the router and host maps
  by the session-start budget (`tests/test_session_start.py`, 10,000
  characters), which covers the trigger's second clause, a rule change
  with no headroom left there; D7's figures go into the
  decision record as the baseline a later measurement compares with.
  Basis: the umbrella entry leaves restating or retiring to this child;
  the controller's proposal, accepted by the maintainer.
- **D9. The branch reviewer's arrangement section, on the lane only.**
  Off the very-small lane the branch reviewer has no use for § The
  arrangement questions: since `execution-retirements` it grades no
  `Review: branch only` mark. On the lane it has one: the upgrade hatch
  (`skills/subagent-driven-development/references/very-small-lane.md`)
  fires where "a reviewer's finding or question" shows a major mechanism
  of the change is expected to be overturned. The template takes the
  section only where its `lane` selector is `very-small`, with one line
  saying what it is for; `docs/decisions/instruments.md` records the
  conditional splice beside the redteam seat's goal-check precedent, and
  the reviewer card's `lane` description names the section. Basis: `placement`'s open item, left to this
  child; the controller's proposal, accepted by the maintainer.
- **D10. Backlog dispositions.** `docs/backlog/skill-size-after-compaction.md`
  is resolved but for one point, which it keeps: a session spanning a
  plugin update gets the old version's copies re-attached after
  compaction (seen again in the maintainer session of 2026-11-03,
  copies from 0.13.0 and 0.12.0 re-attached under 0.14.0).
  `docs/backlog/skill-text-rewrite.md` loses its resident-cost
  observation with the trigger (D8) and `placement`'s arrangement item
  (D9), each with its matching Follow-up line, and keeps the rest. Basis: the controller's proposal, accepted
  by the maintainer.
- **D11. The router's re-invoke line stays.** `skills/using-crucible/SKILL.md`
  keeps "a skill whose text came back cut short … is invoked again": a
  skill that grows past the line between test runs, or a host whose cut
  moves, is still caught by it; the host's documentation also says
  invoking a skill again restores its full content. Basis: the
  controller's proposal, accepted by the maintainer at the campaign
  gate.

## Constraints & invariants

- **No rule changes.** Moved text keeps every rule it states; a moved
  passage differs from what left the `SKILL.md` only by wording the move
  makes redundant or a pointer the move needs. The one change of
  substance is D9's, which narrows what an off-lane branch reviewer
  reads, not what any seat does.
- **The spine (D3) stays in each `SKILL.md`**: no trigger, cap,
  termination guarantee, operator gate or resume rule sits only in a
  reference.
- **Every `SKILL.md` body is at or under 18,000 characters** at this
  child's landing, and no new skill is added.
- **Headings stay citable.** A moved section's heading stays in its
  `SKILL.md` as its stub, so citations of the form
  `crucible:<skill> § <heading>` resolve unchanged; a subheading that
  moves and is cited elsewhere is re-cited at its reference
  (`docs/authoring.md` § Reference convention).

## Interfaces & boundaries

- **The stub.** A stub's sentence keeps the form
  ``read `skills/<skill>/references/<file>.md` in full`` that
  `tests/skill_corpus.py` (`STUB_RE`) matches. `tests/test_skill_references.py`
  holds a stub to one paragraph under its heading, each reference to one
  stub (a shared reference aside) and each reference to opening with its
  stub's heading; so each moved heading gets a reference of its own, and
  the spine sentences D3 keeps for a moved step sit in that one
  paragraph. No rule of that test changes; its fixed stub set
  (`EXPECTED`) gains each new pair.
- **The structural test** reads every `skills/*/SKILL.md`; its reader is
  the host's re-attachment after compaction, named in a comment beside
  the assertion (`AGENTS.md`, Tests assert text only where code or the
  host reads it).
- **Rule sites swept with D5**: `docs/decisions/authoring-crucible.md`
  (the rule, the measurement, its `## Changes` line),
  `skills/writing-skills/SKILL.md` (Size and placement), `AGENTS.md`
  (the line beside the always-loaded budget), and the docstrings of
  `tests/skill_corpus.py` and `tests/test_skill_references.py`, which
  describe moved sections as route-conditional. With D8, the record's
  Rejected entry on a full rewrite of the controller skills, which
  points at the trigger, says the rewrite ran as this umbrella and the
  trigger is retired. The record's Rejected entry "A byte or word
  target" is narrowed to a total or reduction target, still declined,
  distinguished from the host-imposed per-skill ceiling D1 sets.
  `docs/upstream.md`'s row for upstream's size test maps it to this
  child's structural test and the decision record, stating the
  difference in line (characters at 18,000 against bytes at 20,000).
- **Readers that reach a moved step through a citation.** Other skills
  and references cite moved sections by heading (the very-small lane's
  reference cites SDD's § Finish; `requesting-code-review` cites SDD's
  § Disputes and adjudication; the plan phase's and folded lane's
  references cite redteaming's sections). The heading stays as the
  stub, so each reader lands on the stub and reads the reference from
  there; citing text outside the moved passages does not change, except
  a citation of a moved subheading, re-cited at its reference. Inside a
  moved passage, a bare `§ <heading>` citation of its own skill becomes
  `crucible:<skill> § <heading>`, since it now sits in another file;
  under A4 that is a needed pointer.
- **The branch reviewer's template** changes in its source,
  `skills/requesting-code-review/code-reviewer.source.md`; the rendered
  template and agent are regenerated (`python tools/instrument_agents.py
  write`), whose include inside a selector passage the generator
  supports. D9's other sites: the reviewer card's `lane` description
  (`code-reviewer.slots.md`) and `docs/decisions/instruments.md` (the
  splice paragraph and a `## Changes` line).
- **Shared with the umbrella.** This child's landing completes the
  umbrella; its close readout names the umbrella's closing review as the
  next step (`skills/brainstorming/references/umbrellas.md` § Closing
  review), and states C1's net change and C2's sizes.

## Acceptance

- **A1.** Each `SKILL.md` body is at or under 18,000 characters, held by
  a standing structural test whose comment names its reader.
- **A2.** The decision record states the line: the documentation's
  wording, the measured cut and the 18,000-character test line, with
  dates. One-time check: the record read in review.
- **A3.** The spine: each moved step's stub carries its trigger; no cap,
  termination guarantee, operator gate or resume rule sits only in a
  reference. Why not a test: prose fidelity, judged by task review and
  the branch review.
- **A4.** No rule changes: a one-time check compares, word by word, each
  passage that left a `SKILL.md` with the reference text it went to,
  and lists every difference; review judges each one redundant wording
  or a needed pointer.
- **A5.** The stub set test passes with the new pairs (standing:
  `tests/test_skill_references.py`).
- **A6.** The prose budget sum at the head is at or below its value at
  `d78398c`, the net change and what offset the stubs stated in the
  close readout (standing: `tests/test_prose_budget.py`; the sum, a
  one-time check).
- **A7.** The rule sites of D5 and D8 state the widened rule and the
  retired trigger, the decision record carrying its `## Changes` line. Why not a test: prose, judged
  in review.
- **A8.** The branch reviewer's rendered template carries § The
  arrangement questions only under `lane = very-small`, with its
  purpose line; the generator's check passes (standing: the suite's
  `check` of generated files).
- **A9.** Resident tokens per route at `a3db87f`, `d78398c` and the
  head, per D7, the manifests and figures committed, in the decision
  record and the close readout. One-time check: the counting run's
  output quoted in its task report.
- **A10.** The backlog matches D10: `skill-size-after-compaction.md`
  holds only the stale-copy point; `skill-text-rewrite.md` holds neither
  the resident-cost observation nor the arrangement item, nor their
  Follow-up lines. One-time check: the files read in review.
- **A11.** The full suite passes on the head.

## Mechanism sketches

Advisory; implementers may replace them.

- **Indicative allocation** (characters of body at `d78398c`; the
  figures moved are net of the spine sentences D3 keeps, and each stub's
  own pointer text is taken at about 400 characters, the existing stubs
  running 210 to 506):
  - SDD (37,483; shed at least 19,483): Setup less its ledger identity,
    sections, resume rule, predecessor links and after-compaction line
    (about 3,900 of 5,658 move); step 2 Handle the report (2,791); step
    3 Review the task (1,176); step 4 Verification gates (946); step 5
    the fix loop, its trigger, cap and after-the-third-wave ask staying
    in the stub (about 1,700 of 3,220); § Disputes and adjudication
    (4,119); § What a report voices (1,347); § Drift found after the
    fact (1,463); § Inline mode (1,077); § Finish, its order rule and
    the answer staying in the stub (about 5,450 of 6,642). Net shed
    about 20,000, leaving a body near 17,500. Further candidates:
    § Instruments and report files (991), § Models (751).
  - Redteaming (33,183; shed at least 15,183): § Panels (5,215),
    § Merge and finding hygiene (5,815; its § Operating stance — baseline
    error rate staying in the spine as its own section, so its two
    citations stand), § Fix application and blind verification (4,563)
    and § Round readout (2,974); § Stop rule and terminal pass stays,
    being mostly spine (trigger, terminal pass, cap). Net shed about
    17,000, leaving a body near 16,200. Further candidate: § Inputs and
    state (2,185), less its rehydration rule.
  - Brainstorming (20,959; shed at least 2,959): § Proposing the
    arrangement (step 4) (5,132), the operator's confirmation of the
    preset staying in its stub. Net shed about 4,300, leaving a body
    near 16,650.

  Deferred to implementation: the exact sections moved and their
  reference file names, within D3, the stub rules (Interfaces & boundaries)
  and the 18,000-character line.
- **Counting.** Characters of the body as Python counts `str`, after the
  closing frontmatter fence; the header and notice the host adds are
  outside the file, hence the margin.
  Deferred to implementation: the exact body boundary (whether the
  closing fence's newline counts), one definition used by the test and
  by the reported figures alike.
- **Resident tokens.** Each manifest file's text sent alone to the
  token-counting endpoint, a one-word message's count subtracted;
  per-route totals summed by phase. Deferred to implementation: where
  the counting script lives (scratch, or the feature folder), so long as
  the manifest and figures are committed.
- **The word-by-word comparison (A4).** Normalise whitespace in the
  removed `SKILL.md` text and in the new references, then diff them.
