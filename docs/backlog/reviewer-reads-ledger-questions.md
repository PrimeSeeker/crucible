# Branch reviewers read the ledger section their scope excludes

## Observation

- The branch reviewer's template sends it to the SDD ledger and tells it
  not to read the ledger's `## Questions` section, so that one pass's
  questions do not become the next pass's input
  (`skills/requesting-code-review/code-reviewer.source.md` § Read Scoping;
  `docs/decisions/branch-review.md`, Leads and questions).
- On three features of 2026-11-23, each on the very-small lane, a
  full-scope pass's reviewer reported having read that section, one
  "because I read the whole ledger file in one call"; each said its
  findings did not rely on it. Two were second passes and one a first
  pass; the two other first passes reported nothing, though a first
  pass's ledger holds carried questions too.
- The card already hands the reviewer the ledger's deferred minors and
  rulings verbatim. What else it takes from the ledger file itself was
  not checked.
- No effect on a review is on record: a later pass also gets the earlier
  pass's rulings on leads, so its independence is partial either way.

## Follow-up

- Decide whether the exclusion is worth keeping. If it is, check whether
  the reviewer needs the ledger file at all beyond what its card carries,
  and drop the read if not; a section of one file cannot be withheld from
  a seat told to read that file.
