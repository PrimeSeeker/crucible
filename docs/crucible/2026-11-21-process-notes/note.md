Lane: very-small (operator-confirmed 2026-11-21)

# Process notes

## Intent

A controller sees much that is off in the process it runs: a missing or
contradictory rule, a step that costs more than it catches, instructions
at odds, a host failure, its own shortcuts and errors. Today this reaches
the operator only when they ask. Every controller notes such things as
they happen and offers them when the work ends; a seat can say what was
off in its own instructions or tools.

- An operator who has said nothing sees one line: the count, the main
  note, an offer of the rest. Their instruction files can ask for the full
  list every time, or for none.
- The full list states each note as an observation about the work, with
  its cause: crucible, the project's or operator's instructions, the host,
  or the agent. The agent's own preferences and remarks on the operator's
  steering are added only where the operator's instructions invite them.
- For a note crucible caused, the full list offers a draft issue for
  crucible's maintainers, without the project's details. Nothing is sent
  without the operator's word.
- Notes nobody takes are deleted with the workspace; this is intended.

Premise, measured in part: a keyword search of 18 sessions over two weeks
found one operator request for a process report; its answer listed nine
things, three of which led to a later feature. Not measured: whether any
had been volunteered earlier.

No break.

## Change list

- `skills/using-crucible/SKILL.md`: a "Process notes" paragraph. Whatever
  is off in the process, in the broadest sense, is noted in a line with
  its cause as it happens, a seat's remark as the seat wrote it: in
  `process-notes.md` in the feature workspace once one exists, else held
  for the last message on the work. When the work ends, and before a
  workspace holding notes is deleted, the controller rereads the notes,
  adds what hindsight shows, and gives the one line; the full list goes
  out where the operator asks or their instructions do, as the new
  reference states.
- `skills/using-crucible/references/process-notes.md` (new), read before
  giving the full list: observations about the work, each with its cause;
  what waits for an invitation; the draft issue offered for a note
  crucible caused.
- `skills/subagent-driven-development/references/seat-rules.md` § Report
  file, which all seven templates take: a seat says in its final reply, in
  a line, anything off in its instructions or tools, normally nothing.
  Then `python tools/instrument_agents.py write`.
- `skills/subagent-driven-development/references/finish.md` step 2: the
  close readout carries the line on `process-notes.md`.
- `skills/redteaming/references/formats.md` § Feature workspace root and
  layout: `process-notes.md` in the layout.
- `docs/decisions/operator-steering.md`: the decision, why, what was
  rejected (no report unless asked, the full report by default, an
  independent reader as a standard step, a store for notes), and a
  `## Changes` line.
- `README.md` § Configuration: what a user sees at the end of the work and
  how their instruction files change it.
- `docs/backlog/skill-rewrite-reaudit.md`: a read of whether notes were
  made and offered, what they held, and whether a seat's remark reached
  them.
- `tests/prose-budget.txt`: the raised counts, the commit saying what the
  words buy.

## Acceptance

1. `python -m pytest tests/` passes: the envelope stays under its budget,
   the prose budget holds under the total cap, the generated templates
   and agents match their sources.
2. `git grep -c "process-notes.md" -- skills/using-crucible/SKILL.md skills/redteaming/references/formats.md skills/subagent-driven-development/references/finish.md`
   prints a count for each of the three files.
3. `git grep -l "off in your instructions or tools" -- skills/redteaming/seat-prompt.md skills/redteaming/terminal-pass-prompt.md skills/redteaming/verifier-prompt.md skills/requesting-code-review/code-reviewer.md skills/subagent-driven-development/implementer-prompt.md skills/subagent-driven-development/re-review-prompt.md skills/subagent-driven-development/task-reviewer-prompt.md`
   lists all seven templates.
4. `git grep -n "rocess notes" -- docs/decisions/operator-steering.md`
   prints a line of the Decision and a `## Changes` line dated the day the
   change is committed.

Checks 2 to 4 print nothing on the tree before the change. No test asserts
the wording: no code or host reads it. Whether controllers make and offer
notes shows only in later sessions, which the re-audit read covers.

## Out of scope

- A store for notes beyond the workspace.
- Filing anything automatically.
- An independent reader of a session's records or transcript as a
  standard step.
- The three seats a controller composes itself (the mechanical pre-pass,
  the adjudicator, a fresh look): they take no seat sentence.
- Any change to round readouts or to a report's format.
