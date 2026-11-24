# Two text gaps the prose cap left open

## Observation

- The branch reviewer's output-format sentence lists what each report line
  may be: "a finding with its location, a question, a triage verdict or a
  check you ran" (`skills/requesting-code-review/code-reviewer.source.md`).
  Since 2026-11-24 the goal check runs only on the very-small lane, and the
  sentence no longer names it, but the lane reviewer's report still opens
  with its `### Goal Check` section. The structure names the section, so
  the contradiction is low in effect.
- The router has the controller reread `process-notes.md` and offer its
  line "before deleting a workspace holding notes"
  (`skills/using-crucible/SKILL.md` § Process notes). Since 2026-11-24 SDD's
  Finish deletes the workspace after finishing, and on a local merge or a
  confirmed discard finishing's worktree removal deletes it first
  (`skills/subagent-driven-development/references/finish.md`, steps 6–7).
  Notes written after the close readout (from the suite, bringing a moved
  base in, or finishing itself) can go unread on the clean path; on the
  loop path Finish restarts and the readout carries them.
- Both were found by the last branch-review pass of the change that made
  them, with the skills' word total at `TOTAL_CAP`, so neither fix had
  words.

## Follow-up

- Name the lane's goal check in the line-kind sentence, inside the `lane`
  selector, or word the sentence to admit the structure's own sections.
- Add a clause at Finish's finishing step: reread the notes before
  finishing removes the worktree; or accept the loss and say so in
  `docs/decisions/records-and-workspace.md`.
- Both need words under the cap: pair them with a compaction or with the
  operator's ruling on the cap.
