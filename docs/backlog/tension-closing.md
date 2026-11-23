# How a tension gets closed

## Observation

- When the maintainer remarked on it (2026-10-29), a tension a review found
  was closed by adding a distinction. On a proposed fix-list clause asking
  whether a removing or merging resolution exists, the maintainer said: "Looks weak indeed, we'll need to restructure
  this somehow, probably later"
  (`docs/crucible/2026-10-29-audit-corrections/design.md`).
- The fix list takes fix-by-deletion as a first-class resolution
  (`skills/redteaming/references/fix-application.md`), but that rule predates
  the remark, so it does not answer it.
- The Repeat hits rule in the same file turns a second hit on a passage, in a
  campaign's fix list, into a rewrite or removal of it; a first hit's fix there
  stays as it was. `crucible:writing-skills`' fix sentence now also allows
  restating over the whole class, at any hit, for any fix to agent-read text, a
  branch-review wave's included. How a tension is closed in general stays as it
  was.
- Reviews still close tensions mostly by adding distinctions. In the
  re-audit of 2026-11-23, over one code project's runs on crucible 0.33.1, a
  sample of 69 items from 37 spec-round fix lists in 21 campaigns, taken by
  position, held 32 that added a distinction, condition or special case, 12
  rewrites (4 of them generalising a rule), 5 deletions or merges and 20
  others, mostly bookkeeping.
- Branch-review fix waves do the same. In a sample of 75 finding fixes from
  20 fix files, 29 added a condition, special case or guard, 5 restructured,
  4 deleted and 37 were other corrections. In the two classes of finding
  that recurred across passes, each wave's special case met a further case
  at the next read, and the one restructure in either came from a fresh
  look. Implementer-written fix reports named a cause for about 28% of
  their items and sibling instances for about 70%, by keyword, so lower
  bounds; the controller's own fix reports on the very-small lane, 32
  items, named no cause and siblings for 5, though the lane holds them to
  the same contract. The classification is one reader's.

## Follow-up

Weigh the restructuring as a design target of a later rewrite. The checks
this item first asked for, on fix lists and on branch review, are the
figures above.
