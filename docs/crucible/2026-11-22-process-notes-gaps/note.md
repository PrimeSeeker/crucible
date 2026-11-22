Lane: very-small (operator-confirmed 2026-11-22)

# Process notes: three gaps its build left

## Intent

The process-notes build left three things open
(`docs/backlog/process-notes-open-items.md`). This change closes them.

- Every seat says what was off in its instructions or tools, the seats a
  controller composes itself included. Until now only the seven template
  seats were asked.
- An operator whose instructions ask for no process notes sees none, the
  line saying that no notes were made included. That line is owed in a
  feature's close readout and nowhere else.
- The seats' report-file rule says why the file is the deliverable. The
  host's note to subagents tells them the parent reads their reply and not
  files they create; a crucible controller does the opposite, and the rule
  now says so.

Premise. The first is the maintainer's answer to a question the build left
open, and the second a branch reviewer's literal reading of the rule; no
operator has opted out yet, so neither has anything to measure. The third
was probed and its effect is not measured: two seats of the previous
build, asked what was off, reported the clash with the host's note and
followed the template; nine probe seats on the default role, three to each
of three wordings (the rule as it stands, with "even where your host
advises returning findings as text", and with the reason), all wrote the
file and none reported a clash. It is made because the rule should state
its reason where the host states the opposite one, not because a failure
was observed.

No break.

## Change list

- `skills/subagent-driven-development/references/dispatch-composition.md`,
  item 5's opening: "the **report path and the return contract** (what the
  file holds; what the final message returns, a line on anything off in
  the seat's instructions or tools included, which an instrument's
  template carries)."
- `skills/using-crucible/SKILL.md`, the Process notes paragraph: the
  sentence "With no notes made, say so only at a feature's close." goes,
  and the one line ends "... the count, the main note, an offer of the
  rest or, in a feature's close readout only, that no notes were made."
- `skills/subagent-driven-development/references/finish.md`, step 2: the
  item returns to "the one line on `process-notes.md` that
  `crucible:using-crucible` asks for".
- `skills/subagent-driven-development/references/seat-rules.md` § Report
  file: after "the file is the deliverable", the sentence "Your controller
  reads it, not your reply, and it outlasts the controller's context."
  The seven templates and `agents/` are regenerated.
- `docs/decisions/operator-steering.md`: the Decision and § Process notes
  state the three positions above for the first two, with a `## Changes`
  line. `docs/decisions/instruments.md`: the reason in § Report file, the
  probe as it came out, and a `## Changes` line.
- `docs/backlog/process-notes-open-items.md` is deleted, its items
  resolved. `docs/backlog/skill-rewrite-reaudit.md`: the read of process
  notes also asks whether seats report the host's advice on report files
  as something off.
- `tests/prose-budget.txt`: the changed counts, the commit saying what the
  words buy.

## Acceptance

1. `python -m pytest tests/` passes.
2. `git grep -c "off in the seat's instructions or tools" -- skills/subagent-driven-development/references/dispatch-composition.md`
   prints a count.
3. `git grep -l "controller reads it, not your reply" -- skills/redteaming/seat-prompt.md skills/redteaming/terminal-pass-prompt.md skills/redteaming/verifier-prompt.md skills/requesting-code-review/code-reviewer.md skills/subagent-driven-development/implementer-prompt.md skills/subagent-driven-development/re-review-prompt.md skills/subagent-driven-development/task-reviewer-prompt.md`
   lists all seven templates.
4. `git grep -c "close readout only" -- skills/using-crucible/SKILL.md`
   prints a count, and
   `git grep -c "no notes were made" -- skills/subagent-driven-development/references/finish.md`
   prints nothing.
5. `git ls-files docs/backlog/process-notes-open-items.md` prints nothing.
6. `git grep -n "return contract" -- docs/decisions/operator-steering.md`
   and `git grep -n "outlasts" -- docs/decisions/instruments.md` each
   print a `## Changes` line dated the day the change is committed.

On the tree before the change, checks 2, 3 and 6 print nothing, the first
command of check 4 prints nothing and its second a count, and check 5
prints the path. No test asserts the wording: no code or host reads it.
Whether a composed seat says what was off, and whether the reason changes
what seats do, show only in later sessions, which the re-audit read covers.

## Out of scope

- `seat-rules.md` § Report file required, and the two cards that name the
  host's file-writing tool: unchanged.
- The wording of the seat sentence in § Report file.
- The previous feature's lane note, frozen as it shipped.
- A controller correcting a false statement in a decision record after the
  last full-scope pass without a wave, and who a lane note is for: both
  discussed with the maintainer, neither part of this change.
- The README, unless the change makes a sentence of it false.
