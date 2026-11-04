# Seams in a split lane's resume and report rules

## Observation

A split on the very-small lane, and the ledger and report rules around it,
have not run in a session, and no run on record has hit any of these.

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
- **A saved section may not name its part.** A report the controller saves to
  an appended report opens with the mark, while a split's resume keys on a
  heading naming the part. If a returned report lacks that heading, nothing
  says whether the saved section counts as that part's or the part re-runs. It
  needs a seat that fails to write twice on a split.
- **Undispatched parts have no record.** `Implementer:` lines name only the
  parts already dispatched, and `<k>/<n>` gives only a count, so a resumed
  controller re-derives how the rest were cut from the note and `git log`.
- **Whether this mechanism is worth its words.** The feature that added the
  split raised the subagent-driven-development prose budget by 194 words for
  paths no run has hit, and its last full pass found seams of this kind in text
  its previous wave had added.

## Follow-up

Decide between two shapes: finish the mechanics (the section
states the part's status, the wave line covers any fresh seat, the split is
written down once at the stay answer), or replace them with a shorter rule,
such as a resumed controller putting a split in progress to a fresh decision.
The second may also shed words from what is already there.
