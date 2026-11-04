# Umbrellas: follow-ups from the first implementation

## Observation

The branch that added umbrellas (`skills/brainstorming/references/umbrellas.md`,
`docs/decisions/umbrellas.md`) closed its review with these left open,
none blocking:

- **FIX_BASE after a red suite.** SDD § Finish gives a red-suite wave's
  FIX_BASE as the HEAD the suite ran on; the branch review's receiving
  step can merge the base before FIX_BASE is recorded.
- **The `landed` mark lands unreviewed.** It is committed at SDD Finish,
  after the branch review, and for a child with no umbrella line so is
  its base merge. The spec placed it there.
- **An approval-only umbrella still gets a workspace and a decision
  record**, which its landing deletes: ceremony for a document no
  campaign reviews.
- **A pending open-items ask at an umbrella has no carrier.** With no
  home for open items configured, an umbrella's landing and its closing
  review ask the operator where they go and keep the workspace until the
  answer (`skills/redteaming/references/formats.md` § Open items); an
  umbrella has no ledger, so a session that ends before the answer
  leaves nothing telling the next one the ask is pending.
- **The branch reviewer's build-history exemption covers only Finish's
  open items.** `skills/requesting-code-review/code-reviewer.md` exempts
  the open items the controller's finish wrote; those an umbrella's
  landing or closing review writes to an in-repository home, carrying
  ledger-style sources, would draw findings in a review of those
  branches.

## Follow-up

Rule on the FIX_BASE wording
and on whether the mark or an approval-only umbrella's workspace should
change. Close the two open-items gaps: a carrier for a pending ask
(the umbrella's workspace, or a note in `umbrella.md`) and the
exemption's reach.
