# Umbrellas: follow-ups from the first implementation

## Observation

The branch that added umbrellas (`skills/brainstorming/references/umbrellas.md`,
`docs/decisions/umbrellas.md`) closed its review with these left open,
none blocking:

- **A mark can conflict with an appended child.** § Shape says the blank
  line between entries keeps siblings' marks from conflicting in git.
  Where the Children list ends the file, one branch marking the last
  entry and another appending a child conflict; a line after the list
  avoids it (reproduced in throwaway repositories).
- **Two statements of what binds carry it partly by pointer.** SDD's
  pre-flight scan and its adjudicator inputs omit the own-mark and
  base-merge exemptions, against the rule that every statement of what
  binds carries the clause; the adjudicator receives the full clause
  through `dispatch-composition.md` item 4.
- **No text says how a seat finds the feature's own entry** (by its
  slug).
- **Brainstorming's Flow step 4 does not point to the umbrella stub**,
  and the stub's heading lacks the step tag its sibling sections carry.
  Self-review check 3's umbrella sentence also reads oddly against an
  umbrella's own draft.
- **FIX_BASE after a red suite.** SDD § Finish gives a red-suite wave's
  FIX_BASE as the HEAD the suite ran on; the branch review's receiving
  step can merge the base before FIX_BASE is recorded.
- **The `landed` mark lands unreviewed.** It is committed at SDD Finish,
  after the branch review, and for a child with no umbrella line so is
  its base merge. The spec placed it there.
- **An approval-only umbrella still gets a workspace and a decision
  record**, which its landing deletes: ceremony for a document no
  campaign reviews.
- **The implementer slot card is at 2,966 of its 3,000 characters.**

## Follow-up

Fix the first four in one small change; rule on the FIX_BASE wording
and on whether the mark or an approval-only umbrella's workspace should
change. Take the size of the umbrella text into
`docs/backlog/skill-text-rewrite.md`.
