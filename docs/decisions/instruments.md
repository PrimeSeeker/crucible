# Instruments

## Decision

**Seven instruments, generated as agents.** Seven templated seats are
instruments: the redteam seat, the blind verifier, the terminal pass, the
implementer, the task reviewer, the re-reviewer and the branch reviewer
(`INSTRUMENTS` in `tools/instrument_agents.py`). Each has a template, the
one hand-edited home of its fixed text, and a sibling slot card
(`<template>.slots.md`) holding every dispatch-time slot with its fill
rule, its selectors and its dispatch parameters. A passage the card does
not select is inert: neither performed, attested nor mentioned. For
Claude Code the generator renders each template into `agents/<name>.md`,
filling only the runtime name; the agents are committed, never edited by
hand, and the suite runs the generator's check mode. Their frontmatter
carries a name, a description and a default model alias, and no tool
restriction. On Claude Code a dispatch names `crucible:<name>` and its
model and sends the filled card as the whole prompt; on Codex, and on
Claude Code where the agent is not offered, the controller fills the card
and the template and dispatches both
(`skills/using-crucible/references/claude-code-dispatch.md`,
`skills/using-crucible/references/codex-dispatch.md`). The three campaign
templates keep their shared preamble as three copies.

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
and branch reviewer's cards carry `[PLUGIN_ROOT]`, filled with the plugin
root the controller read the card from. Through it the implementer reads
systematic-debugging, `writing-good-tests.md` and writing-skills, and the
reviewers read `writing-good-tests.md`, in any repository.

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

The agents are generated so that the template stays the text's one home;
the check mode catches a stale agent at build time. They carry no adapter
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

The shared preamble of the three campaign templates stays as three
copies (2026-10-13): on Codex the controller fills a
template itself, and an include would add a resolution step there.
(Basis: judgment, accepted by the maintainer.)

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
it is dispatched for ("This seat's independent read is the deliverable",
`skills/redteaming/seat-prompt.md`). On Codex the `ultra` effort level
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
- **A generator include for the campaign templates' shared preamble**: it
  would add a resolution step on Codex (§ Why).
- **A fixed header for a controller-saved report**: its one reader is
  gone; a first-line mark does the remaining job (§ Why).
- **Seat-facing wording against skipped report writes**: a control
  without the host's advice did not reproduce the skip; the controller's
  check and one resume cover it.

## Changes

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
