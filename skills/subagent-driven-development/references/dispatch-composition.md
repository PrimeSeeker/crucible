# Dispatch composition

Every fresh seat you start carries seven items:

1. the **absolute worktree path** it works from;
2. the **exact input artifact paths**, never "the plan" in general or pasted history; for a seat given binding content, also each umbrella's path up the chain of `Umbrella:` lines from the binding artifact's preamble (an instrument's umbrella slot);
3. the **runtime identity** (the host's name): the instrument agent carries it; on the template path, your adapter's opening line names it; a controller-composed dispatch names it and tells the seat to use that host's tools. Send no other adapter text: a dispatched seat never re-runs the top-level router;
4. the **pointer to the binding content** and a **one-line mandate reminder**: the binding artifact's path at its pinned revision (given a plan, point at its header's spec pointer without restating the revision), never a copied block, which drifts; a line naming what binds (`review-terms.md` § What binds in a spec), which an instrument's template carries; a line naming the seat's binding output, which a card's mandate slot holds; a controller-composed dispatch carries both lines in its prompt;
5. the **report path and the return contract** (what the file holds, what the final message returns). Before taking returned text as the report, confirm any owed report file is on disk. Missing, no refusal reported: resume the seat once to write it. Still missing, or a refused write reported: persist the latest return carrying the full report yourself, with the mark `skills/redteaming/references/formats.md` § Feature workspace root and layout states;
6. the **never-touch-another-checkout instruction**: no edits, writes or git against another checkout, nor changing directory into one;
7. the **no-delegation instruction**: no seats of its own unless its assignment explicitly includes delegation.

An instrument's card and template carry all seven, item 3 on the template path with the adapter's opening line, item 4's pin through the plan where the seat has one. Fill every slot; depart from this list only where the dispatching skill says so beside the dispatch.

## Filling a card

An instrument is dispatched from its slot card, the `.slots.md` beside its template: read the card, not the template. Replace each slot's rule with its value, and set each selector to one value, cutting its line to that value and dropping its sub-bullets; a passage left unselected (`off`, or a value you did not pick) is dropped, not narrated. Dispatch a fresh seat of the instrument the card's title names through your adapter's instrument-dispatch operation, sending only the filled `## Slots` and `## Selectors`, on the template path under the opening line item 3 names; the card's title and `## Dispatch` are yours. `## Dispatch` holds what the dispatch takes beyond this file (a description, a model other than the default role, a rule of the card's own) or `none`. A task run again after a revert or a plan change takes `-x<X>` after `task-<N>` in every report path a card names (`skills/subagent-driven-development/references/drift.md`).

A read-only seat's scratch directory, its card's scratch slot, is its report's path within the feature workspace less `.md`, in the workspace's `scratch/`; in a standalone branch review, which has no workspace, `review-<base7>..<head7>/` in the host's temporary directory.

## Models and effort

These rules bind every dispatch; a slot card's Model line, or a skill's row for a seat with no card, names a seat's own role.

- **Name the model** on every dispatch.
- A row names one of three roles, always with the word "role". Your host map's Model roles entry names this host's model for each, and the floor no dispatch goes below.
  - **The default role**: the strong model every seat runs on unless its card or row names another, and the ceiling of automatic escalation.
  - **The bounded role**, for a clearly bounded task: one step below the default role, or the default role's model where the host has no qualifying tier between. Never dispatch below it.
  - **The alternate role**: the host's other strong model, which no escalation reaches. Exactly three triggers select it: round 1's swap (`crucible:redteaming` § Panels); work of a kind your host map lists as a default-role weak spot, at an implementer, reviewer or redteam seat (never the blind verifier); the operator's request, at any seat. A host map naming no alternate skips all three.
- Leave a dispatch's reasoning effort unset unless the operator asks for one; no flow sets or raises it. An escalation is the tier bump alone; where that is not enough, the dispatching skill's stop points take it to the operator.

## Shared-tree rules

These bind every controller that dispatches seats into a worktree.

- **No commits while a seat works.** Commit nothing in its worktree until it returns: the index is shared, so a bare commit sweeps in whatever the seat staged.
- **The status check, after every window your skill names.** Dispatch a window's seats with no tracked or staged change. Seats out at the same time are one window: before its first seat, write the output of `git rev-parse HEAD` and `git status --porcelain --untracked-files=all` to `<workspace>/tree-check.txt`, overwriting it; when its last returns, before the next commit, run both again and compare. A difference voids every report from the window until the window runs again on a clean tree. Untracked paths present at dispatch are tolerated. After a compaction, read the dispatch-time state from the file.
- **Replacing a seat.** Never start a replacement before the host confirms the first seat stopped, else two writers share one tree. The replacement writes to a fresh report path: in execution and the branch review, the first's with `-r<R>` before `.md`; elsewhere, as its skill names it. The first's file stays as the record. A seat whose state the host cannot confirm is a stop-and-ask.
