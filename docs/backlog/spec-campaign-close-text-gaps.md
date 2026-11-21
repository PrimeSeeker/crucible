# Spec-campaign close: two small gaps left in the text

## Observation

- **The terminal-pass record's state order.** A record's states advance
  strictly in order, `… fix-applied → verified → readout`, each written only
  after its phase's outputs are on disk
  (`skills/redteaming/references/round-record.md`, field 2). For the
  terminal-pass record the same file defines `verified` as the second
  read's report being on disk, and has the close recorded before any second
  read and delivered after it. Where a second read runs, the record
  therefore reaches `readout` before `verified` can be written. One spec
  campaign's second read noted it (2026-11-20): its record stood at
  `state: readout` with `verified` never reached, and nothing went wrong in
  that run. The state line's one reader is a controller resuming after
  compaction, which at `state: readout` delivers the recorded readout again
  (`crucible:redteaming` § Inputs and state). Read literally, a resume
  between the close's recording and the second read's return would deliver
  a close whose second read is still owed. No run on record has hit it.
- **A decision record restates the late-ruling rule without its ordering.**
  `docs/decisions/fix-verification-and-merge.md`, § Decision, "A ruling
  after the last round", says a ruling later than the rulings list waits for
  the campaign's close. The procedure
  (`skills/redteaming/references/round-readout.md`, last paragraph) sends it
  there only where no numbered round's fix list can still take it: after a
  rulings list that re-shapes a major mechanism another round follows, and
  that round's list takes the ruling. The record kept the flat wording when
  the procedure gained its "Otherwise,". A branch review found it
  (2026-11-21); no controller acts on the record, the skill text governing.

## Follow-up

- State the terminal-pass record's order for a close with a second read, and
  what a resume does at each state: for example, `readout` written there
  only at delivery, or a state of its own for a close recorded with its
  second read still out. A few words in `round-record.md`; it can ride the
  next change to that file.
- In the record, say "a ruling no numbered round's list can then take", or
  cut the sentence to its pointer.
