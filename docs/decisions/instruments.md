# Instruments

## Decision

**Seven instruments, generated as agents.** Seven templated seats are
instruments: the redteam seat, the blind verifier, the terminal pass, the
implementer, the task reviewer, the re-reviewer and the branch reviewer
(`INSTRUMENTS` in `tools/instrument_agents.py`). Each has a template and
a sibling slot card (`<template>.slots.md`) holding every dispatch-time
slot with its fill rule, its selectors and its dispatch parameters. A
passage the card does not select is inert: neither performed, attested
nor mentioned. The template is rendered from a hand-edited source beside
it (`seat-prompt.source.md` for `seat-prompt.md`), the one home of the
seat's own text: the generator splices in each section of the shared
seat reference
(`skills/subagent-driven-development/references/seat-rules.md`) the
source names by its heading, and writes the template at the path every
host reads. For Claude Code it renders each template into
`agents/<name>.md`, filling only the runtime name. Templates and agents
are committed and never edited by hand, and the suite runs the
generator's check mode; the splice's rules are in the generator's
docstring. An agent's frontmatter carries a name, a description and a
default model alias, and no tool restriction. On Claude Code a dispatch names `crucible:<name>` and its
model and sends the filled card as the whole prompt; on Codex, and on
Claude Code where the agent is not offered, the controller fills the card
and the template and dispatches both
(`skills/using-crucible/references/claude-code-dispatch.md`,
`skills/using-crucible/references/codex-dispatch.md`).

**One dispatch composition.** Every fresh seat, whether an instrument, a
template-path dispatch or a controller-composed dispatch no template
serves (the round-0 pre-pass, the adjudicator, the snapshot-blessing
agent), carries the same seven items, stated once and runtime-neutral in
`skills/subagent-driven-development/references/dispatch-composition.md`:
the worktree path, the input paths, the runtime name, the pointer to the
binding content with a one-line mandate, the report path and return
contract, the instruction never to touch another checkout, and the
no-delegation instruction. Its § Models and effort holds the rules every
dispatch shares (`docs/decisions/model-roles-and-effort.md`). The skills
that dispatch point at it and state only where a seat departs from it. A
seat gets the runtime name and no adapter text, and never re-runs the
router.

**Seats start no agents of their own,** unless delegation is explicitly
part of the assignment: the composition's seventh item, and a line in
every template.

**Report files.** Every instrument writes its own report file, a write
its template names, and if the host refuses the write it returns the
report as text and says so. Review seats and the adjudicator write under
the feature workspace's `sdd/reports/` and `sdd/branch-review/`
(`crucible:subagent-driven-development § Finish`). When a seat that owes a
report returns, the controller confirms the file is on disk; if it is
missing and no refusal was reported, it resumes the seat once; if it is
still missing, or the write was refused, it persists the latest full
return unchanged under a first line saying the controller saved it and
why (`skills/redteaming/references/formats.md` § Feature workspace root
and layout). Report names stay clear of Claude Code's subagent write
filter, which `tests/test_report_filenames.py` checks for every card.

**The plugin root.** The implementer's, task reviewer's, re-reviewer's
and branch reviewer's cards carry `[PLUGIN_ROOT]`, filled with the
plugin root the controller read the card from. Through it the
implementer reads systematic-debugging, `writing-good-tests.md` and
writing-skills, and the reviewers read `writing-good-tests.md`, in any
repository. No templated seat reads the shared seat reference
`skills/subagent-driven-development/references/seat-rules.md`, so the
redteam seat's and the terminal pass's cards carry no plugin root: each
template takes by splice the sections its seat follows, as its source
names them, among them what a seat may raise beyond a defect in the work
(`docs/decisions/evidence-and-findings.md`) and the arrangement
questions (`docs/decisions/routes.md`). A section reaches only seats
that follow every rule in it; a rule some of its takers lack stays in
the templates that carry it or takes a section of its own, so sharing
adds no rule to a seat. The redteam seat takes § The goal check only
where its card's `goal-check` selector is on, set for each seat of a
spec campaign's round 1 (`docs/decisions/evidence-and-findings.md`).
The branch reviewer takes § The arrangement questions only where its
card's `lane` selector is `very-small`, beside a line saying what the
section serves there: the lane's upgrade hatch, which keys on a
reviewer's finding or question. An umbrella's closing-review seats, composed by the controller, take
§ Premise findings, § Binding items and unrecorded choices, § Questions
and § Location (`skills/brainstorming/references/umbrellas.md`).

**The terminal pass's card** also carries `{decision-record-path}`: in
the spec phase the brainstorm decision record, which its decision-record
check reads, and `none` in the plan phase
(`docs/decisions/terminal-pass.md`).

## Why

### Instrument agents

Until 2026-09-30 every templated dispatch was composed by hand: the
controller read the template, filled its slots and pasted the whole into
the dispatch, a copy of the runtime adapter included. A token-cost audit
of crucible's runs (2026-09-27) counted 1,195 dispatch prompts at a
median of 10.8K characters and 1,554 controller reads of crucible's skill
files, all held in the controller's context, and put the controller's
main thread at 27% of the window's spend. An agent per template sends
only the slot values. It raised the always-on session cost from about 721
to about 1,113 tokens (`claude plugin details`, Claude Code 2.1.285), and
one live dispatch passed all four of its smoke criteria. (Basis:
measured; judgment, accepted by the maintainer, for the design.)

The agents are generated so that a seat's text keeps one home; the check
mode catches a stale agent at build time. They carry no adapter
text since 2026-10-07: the generator had spliced the whole Claude Code
adapter into all seven, 27.9% to 46.0% of each file, while a seat's work
is fixed by its template and the host already tells a seat its tools. The
seven files went from 99,549 to 66,378 bytes, and the contract that every
seat held the controller's identical adapter block had lost its digest
and could not be checked anyway. That a template-path Codex seat finds
and reads a named crucible skill on its own was then unverified; a run on
codex-cli 0.162.1 (2026-10-15) saw one do it. (Basis: measured; judgment,
accepted by the maintainer.)

Codex keeps the template path because a plugin cannot ship Codex agent
roles: a probe on codex-cli 0.157.1 (2026-09-28) loaded roles from the
Codex home, a trusted project and the config, and never from a plugin, in
any of three forms. Installing crucible's roles into the user's Codex
configuration waits on a cost audit of Codex controllers
(`docs/backlog/codex-agent-role-install.md`). (Basis: measured.)

From 2026-10-13 the shared preamble of the three campaign templates
stayed as three copies: on Codex the controller fills a template itself,
and an include would have added a resolution step there. (Basis:
judgment, accepted by the maintainer.) The splice removes that objection
(§ The splice).

### The splice

On 2026-11-02 the seat templates gained hand-edited sources and a
build-time splice. The clauses every seat, or every review seat,
follows were copied into the seven templates, and the copies drifted; a
shared reference each seat reads at startup gives them one home, but a
seat that skipped the read would lose the rules it carries, and nothing
measures how often that happens. Spliced at build time, the shared text
reaches each seat inside its own text, and each seat gets only the
sections its source names. The rendered template sits at the path every
host's dispatch already reads, so Codex resolves nothing and the
template-path dispatch is unchanged. The cost: where a controller fills
a template itself (Codex, and Claude Code's fallback path), each dispatch
carries the spliced sections in full. The idea of generating the text
rather than having seats read it was the maintainer's; the mechanism an
agent's design, which the maintainer accepted. (Basis: the maintainer's
preference, for generating the text; judgment, accepted by the
maintainer, for the mechanism.)

The generator stays standard-library Python: it fills one slot and
splices named sections. A template engine (Jinja2) is to be adopted once
it needs conditionals or loops, or card filling moves into a script;
dev-time dependencies are acceptable to the maintainer, so a dependency
is no bar then. An agent's proposal, which the maintainer accepted, and
reconfirmed after saying such dependencies were acceptable. (Basis:
judgment, accepted by the maintainer.)

Instrument agents carry no `tools` or `disallowedTools`: a reviewer needs
to write, and correct, its own report file, so read-only stays a conduct
rule in the template (2026-09-28). (Basis: judgment, accepted by the
maintainer.)

### One composition

The composition was written for crucible's Codex support (2026-08-09),
and by 2026-10-07 several skills each restated it. It moved into one
runtime-neutral file under SDD's references, since
`skills/using-crucible/references/` holds one file per host, and the
skills kept only their own departures. The report procedure moved into
it at the same time: confirming, resuming and persisting a report is
workflow policy, which an adapter may not carry, so the Claude Code
dispatch reference kept only the host fact behind it
(`docs/decisions/runtime-adapters.md`). (Basis: judgment, accepted by the
maintainer.)

### No delegation

The 2026-08-09 design made every fresh seat self-contained and isolated,
and the no-delegation instruction part of that: a seat's own read is what
it is dispatched for ("Your independent read is the value you
produce", `skills/redteaming/seat-prompt.md`). On Codex the `ultra` effort level
carries automatic task delegation, which Codex's own model metadata
stated on codex-cli 0.146.1, so no flow selects it
(`skills/using-crucible/references/codex-dispatch.md`). Work that needs
fresh agents, such as a skill evaluation, goes back to the controller
(`docs/decisions/task-loop.md`). (Basis: judgment, accepted by the
maintainer; external, for Codex's description of `ultra`.)

### Report files

On 2026-08-21 report writes were made explicit: each template's read-only
line states that writing its one report path is authorized. A campaign
had ruled out a fallback in its first round; at its close the maintainer
reversed that, because its own terminal pass had its write refused
despite the authorization wording, so a refusal was not only a prompt
defect. The controller would persist the returned report, marked.
(Basis: a single incident; judgment, accepted by the maintainer.)

The cause was found on 2026-10-05. For a subagent, Claude Code's Write
tool refuses any file whose basename matches
`^(REPORT|SUMMARY|FINDINGS|ANALYSIS).*\.md$`, whatever the dispatch
authorized (read in the 2.1.289 binary). Every recorded subagent
transcript agreed: 83 refusals, all on matching basenames, 78 of them
`report.md`, and no matching name ever accepted. The spec terminal pass's
`report.md` was refused on every dispatch; it became `pass.md`, and the
test keeps every name clear. The host also advises subagents in prose to
return findings as text, which sometimes leads a seat to return without
writing; a control without that advice (10 of 10 verifier seats wrote)
did not reproduce it, so no seat-facing wording was added, and the
controller confirms the file and resumes the seat once instead. It then
persists the text without asking: the maintainer saw no point in asking
for bookkeeping. (Basis: measured; the maintainer's preference, for not
asking.)

On 2026-10-13 a first-line mark replaced the fixed header format, from
options an agent put to the maintainer: the format's reader, the
committed feature summary's verbatim trail, had gone on 2026-10-10, and
the mark still tells a reader of the workspace which text is the seat's
own. The redteam seat's template (2026-10-16) and the implementer's
(2026-10-17) then gained the refused-write fallback their siblings
carried. (Basis: judgment, accepted by the maintainer.)

### The plugin root

On 2026-10-08 the implementer's template named systematic-debugging and
`writing-good-tests.md` by paths that resolved to nothing in a user's
repository, and the generated agent's relative link to
`writing-good-tests.md` pointed at a missing file. A slot the controller
fills fixes both: a per-dispatch context line is easy to forget, and
loading by skill name leaves `writing-good-tests.md`, which is not a
skill, unreached, and was unverified on Codex. The reviewers' cards
gained the slot on 2026-10-15, so each reviewer can read
`writing-good-tests.md` when the reviewed repository is not crucible. On
2026-10-16 the slot's definition, "the `<plugin-root>` your own script
calls use", had no referent in SDD, which runs no script, and became the
root the controller read the card from. (Basis: judgment, accepted by the
maintainer.)

On 2026-10-29 the rules for premise findings, the goal check, questions
and a finding's location went into one shared reference, which four
seats' templates point to, under `AGENTS.md`'s rule that rules every
seat follows live in one shared reference; the redteam seat, which had
no plugin-root slot, gained one to reach it. An agent's proposal, which
the maintainer accepted. (Basis: judgment, accepted by the maintainer.)
The reference's first name matched Claude Code's subagent write filter,
which would have refused every later seat's write to that shipped file,
so it was renamed in the task that wrote it. (Basis: a single
incident, 2026-10-29; judgment, accepted by the maintainer, for the
rename.) On 2026-11-02 it was renamed `seat-rules.md`, a name clear of
that filter, as it became the home of the clauses the seat templates
share. An agent's proposal, which the maintainer accepted. (Basis:
judgment, accepted by the maintainer.) The same day its sections moved
into the templates by splice (§ The splice), and the redteam seat's and
the terminal pass's cards, whose plugin-root slot reached only the
reference, lost it. (Basis: judgment, accepted by the maintainer.)

The arrangement questions, the overturn question, "overdetermined" and
the mark's criterion, went into the same reference on 2026-10-29: seats
apply them, so do the controllers that propose an arrangement, stop a
campaign, mark a plan's tasks or work a task inline, and one home every
reader already reaches keeps them stated once. The terminal pass, which
checks the stop against them, gained the plugin-root slot to reach it.
(Basis: judgment, accepted by the maintainer.) On 2026-11-03 the branch
reviewer's template came to take them only on the very-small lane. Off
it the reviewer grades no `Review: branch only` mark and has no use for
them; on it the upgrade hatch
(`skills/subagent-driven-development/references/very-small-lane.md`)
fires where a reviewer's finding or question shows that overturning a
major mechanism of the change is reasonably expected now that it is
coded. An agent's proposal, which the maintainer accepted. (Basis:
judgment, accepted by the maintainer.)

On 2026-10-30 the two clauses that a binding item may itself be wrong
and that a consequential choice taken for granted is a finding moved
from the redteam seat's template into a section of the shared
reference, so the branch reviewer, which had neither, gained them by a
pointer and the template text stayed in one home
(`docs/decisions/evidence-and-findings.md`). The redteam seat's, the
terminal pass's and the branch reviewer's templates name the section;
the task reviewer's and the implementer's do not. An agent's proposal,
which the maintainer accepted. (Basis: judgment, accepted by the
maintainer.) The terminal pass, which re-reads the artifact and raises
findings as a seat does, also gained § Premise findings, so that it
classes a premise finding as the other seats do: a controller's ruling
during the execution of the feature that moved the clauses, when the
task that wrote the section found the pass reading the arrangement
questions alone.
(Basis: judgment, an agent's call the maintainer has not ruled on: a
controller's ruling within that feature.) The
pass's card gained the decision-record slot the same day, for its check
of the operator's approvals (`docs/decisions/terminal-pass.md`). (Basis:
judgment, accepted by the maintainer.)

## Rejected

- **Composing every dispatch by hand**: the measured cost of carrying
  each template's fixed text through the controller's context (§ Why).
- **Adapter text in seats**, and a digest to compare it: a seat's tools
  come from its host, and no seat could check the copy (§ Why).
- **Tool restrictions on instrument agents**: a seat must write and
  correct its own report file.
- **Detecting skew between an agent and its card**: an agent loads at
  session start and its card at each dispatch, so a plugin change
  mid-session can skew them, as it can any session-start text; a new
  session clears it (declined 2026-09-30).
- **A template engine for the generator**, until it needs conditionals
  or loops, or card filling moves into a script (§ The splice).
- **A fixed header for a controller-saved report**: its one reader is
  gone; a first-line mark does the remaining job (§ Why).
- **Seat-facing wording against skipped report writes**: a control
  without the host's advice did not reproduce the skip; the controller's
  check and one resume cover it. The exception: the verifier's and the
  re-reviewer's templates say the report file is required even where the
  host advises returning findings as text, a targeted fix for the two
  seats whose misses persisted
  (`docs/backlog/review-seat-report-write.md`); the shared seat
  reference's § Report file does not carry it.

## Changes

- 2026-11-03: the branch reviewer takes § The arrangement questions
  only where its card's `lane` selector is `very-small`, with a line
  saying it serves the lane's upgrade hatch, and the card's `lane`
  description names it; because off the lane the reviewer has no use
  for the section.
- 2026-11-02: the clauses the seven templates copied move into the
  shared seat reference, each template taking by splice the sections its
  seat follows; the redteam seat's and the terminal pass's cards lose the
  plugin-root slot, whose one use was reading the reference; the
  rejected report-write wording names the verifier and re-reviewer
  exception; so that a seat no longer depends on a startup read and the
  copies stop drifting.
- 2026-11-02: each template is rendered from a hand-edited source beside
  it, the generator splicing in the shared seat reference's sections the
  source names and writing the template at its path, checked by the
  generator's check mode; the rejected generator include is dropped, its
  objection gone; no template engine until the generator needs one; so
  that the clauses the seat templates share have one hand-edited home.
- 2026-11-02: the shared reference renamed `seat-rules.md`, as it becomes
  the home of the clauses the seat templates share.
- 2026-11-02: the redteam seat's card gains the `goal-check` selector
  (`on`, `off`), on for each seat of a spec campaign's round 1, keying
  the goal check and its `## Goal check` report item; the seat keeps the
  request file among its inputs either way; because the goal check
  narrowed to a spec campaign's round 1 and the branch review.
- 2026-10-30: the shared reference gains § Binding items and unrecorded
  choices, the clauses moved from the redteam seat's template, read by
  the redteam seat, the terminal pass and the branch reviewer; the
  terminal pass also reads § Premise findings, and its card gains
  `{decision-record-path}`; the record names what each seat reads of
  the reference; after an audit found the branch reviewer without the
  clauses. The basis for the terminal pass reading § Premise findings
  is labelled an agent's call the maintainer has not ruled on.
- 2026-10-29: the shared reference also holds the arrangement questions,
  and the terminal pass's card gains `{plugin-root}` to read them for its
  stop check, so each definition has one home every reader reaches.
- 2026-10-29: the shared reference's rename, an agent's call, gains the
  basis judgment, accepted by the maintainer: the maintainer accepted it.
- 2026-10-29: the redteam seat's card gains the plugin-root slot, and
  four seats read the shared reference
  `skills/subagent-driven-development/references/seat-rules.md`
  through it, so the rules for premise findings, the goal check and
  questions are stated once.
- 2026-10-17: report files: every instrument writes its own, its template
  naming the write and a refused-write fallback; the controller confirms
  the file, resumes once and persists under a mark; names kept clear of
  Claude Code's subagent write filter.
- 2026-10-16: `[PLUGIN_ROOT]` on the implementer's and the three
  reviewers' cards, filled with the root the controller read the card
  from.
- 2026-10-13: one runtime-neutral dispatch composition of seven items for
  every fresh seat, with the rules every dispatch shares.
- 2026-10-07: seven instruments, each a template with a slot card,
  generated as Claude Code agents with only the runtime name filled; the
  template path on Codex and as Claude Code's fallback.
- 2026-09-28: no tool restrictions on instrument agents; read-only is a
  conduct rule.
- 2026-08-09: seats start no agents of their own unless delegation is
  part of the assignment.
