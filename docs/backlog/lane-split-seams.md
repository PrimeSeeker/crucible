# Seams in a split lane's resume and report rules

## Observation

A split on the very-small lane, and the ledger and report rules around it,
have not run in a session, and no run on record has hit any of these.

- **An appended report can be overwritten on the save path.**
  `skills/subagent-driven-development/references/dispatch-composition.md`
  item 5 counts an appended report without the seat's section as missing, and
  after one resume the controller persists the return itself. The mark's rule
  (`skills/redteaming/references/formats.md` § Feature workspace root and
  layout) describes a whole file and does not say to append. A save written
  as a whole file destroys the earlier sections, and on a split the resume
  rule would then re-run those parts. A fresh fix-wave implementer's report
  has the same exposure. It needs a seat that fails to write twice.
- **A part that stopped has a section.** A split resumes from the first part
  the report file holds no section for
  (`references/very-small-lane.md`), but an implementer writes its report
  whatever its status, and the status appears only in its reply. A part that
  returned NEEDS_CONTEXT or BLOCKED for context reads as finished, and a resume
  before its re-dispatch starts the next part. A re-dispatched seat's missing
  section also passes item 5 on the earlier attempt's section. The routes
  record's "only its report shows it finished" is wrong for these parts.
- **A fresh seat in a fix wave can still lose its wave.**
  `Task <N>: fix wave <W>: implementer <agent id>` (`references/task-loop.md`,
  § The fix loop) is stated only for a host with no resume operation. Step 2
  also starts a fresh seat on a host that can resume: a tier bump after a
  BLOCKED for reasoning, or the alternate role the operator names. Neither has
  a stated wave line, and step 1's line restarts the task on resume. The body
  of commit 538b4a3 says the case cannot arise today, which holds only for the
  host with no resume. In `SKILL.md`'s resume rule, "latest line is a fix wave"
  and the `fix wave <W>: implementer` clause also overlap, though the specific
  clause can be read as governing.
- **Undispatched parts have no record.** `Implementer:` lines name only the
  parts already dispatched, and `<k>/<n>` gives only a count, so a resumed
  controller re-derives how the rest were cut from the note and `git log`.
- **Whether this mechanism is worth its words.** The feature that added the
  split raised the subagent-driven-development prose budget by 194 words for
  paths no run has hit, and its last full pass found three of the seams above
  in text its previous wave had added.

## Follow-up

Fix the save path first: say that a save for an appended report is appended,
its mark opening its section. It is the one seam that loses a record.

Then decide between two shapes for the rest: finish the mechanics (the section
states the part's status, the wave line covers any fresh seat, the split is
written down once at the stay answer), or replace them with a shorter rule,
such as a resumed controller putting a split in progress to a fresh decision.
The second may also shed words from what is already there.
