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
- The Repeat hits rule in the same file turns a second hit on a passage into
  a replacement of it. A first hit's fix, and how a tension is closed in
  general, stay as they were.
- Whether branch-review fix waves generate special cases the same way is
  unchecked. Their fixes must name a cause and report sibling instances in the
  diff, but whether that works is unmeasured.
- Whether reviews still close tensions by adding distinctions is unmeasured.

## Follow-up

Weigh the restructuring as a design target of a later rewrite, and first check
whether recent fix lists still close tensions that way, and whether branch
review does.
