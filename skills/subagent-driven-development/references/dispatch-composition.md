# Dispatch composition

Every fresh seat a controller starts — an instrument, a template-path
dispatch, or a controller-composed dispatch no template serves — carries the
same seven items:

1. the **absolute worktree path** it works from;
2. the **exact input artifact paths** — the files the seat reads, as
   paths: never "the plan" in general, never pasted prior history. Where
   the binding artifact's preamble carries an `Umbrella:` line, a seat
   that receives binding content also gets the umbrellas' paths up the
   chain: the one that line names, then the one each umbrella's own line
   names; on an instrument, in its card's umbrella slot;
3. the **runtime identity** — the name of the host the seat runs on. The
   instrument agent carries it; on the template path you fill it into the
   template's runtime slot; a controller-composed dispatch names it and tells
   the seat to use that host's own tools. No adapter text goes with it: a
   dispatched seat is not a router session and never re-runs the top-level
   router;
4. the **pointer to the binding content** and a **one-line mandate reminder** — the path of the artifact that carries what binds, at its pinned revision, with one line naming what the pin makes binding as `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec states it, which an instrument's template carries; and one line naming the seat's binding output, which a card's mandate slot holds. A pointer, never a copied block: a copy drifts against the artifact it copies. The seat's requirements input carries the pin — the spec pointer in a plan's header, which the dispatch points at without restating the revision; for a seat given no plan, the artifact's own path at its pinned revision. A change to binding content that a report leads to passes `skills/redteaming/references/flip-paths.md` § The containment test;
5. the **report path and the return contract** — what goes in the file, what
   comes back in the final message. When a seat that owes a report file
   returns, confirm the file is on disk before taking the returned text as
   the report. If it is missing and the seat reported no refusal, resume the
   seat once to write it; if it is still missing, or the seat reported the
   host refused the write, persist the latest return that carries the full
   report yourself, with the mark `skills/redteaming/references/formats.md`
   § Feature workspace root and layout states;
6. the **never-touch-another-checkout instruction** — no edits, writes or git
   against any other checkout, and no changing directory into one;
7. the **no-delegation instruction** — a seat you start does not start seats
   of its own unless delegation is explicitly part of its assignment.

Each instrument's slot card and template carry all seven together, item 4
through the plan where the seat has one. Fill every slot; never trim one to
shorten a dispatch. Where a seat departs from this list, the skill that
dispatches it says so beside the dispatch.

## Filling a card

An instrument is dispatched from its slot card, the `.slots.md` file beside
its template: read the card, not the template. Replace each slot's rule
with its value, and set each selector to one value, cutting its line to
that value and dropping its sub-bullets: a passage left unselected, `off`
or a value you did not pick, is dropped, not narrated. Dispatch the
instrument with the filled card through your adapter's instrument-dispatch
operation. The card's Model line names the role its seat runs on;
§ Models and effort holds what every dispatch shares, effort included.

A read-only seat's scratch directory, its card's scratch slot, is its report's path within the feature workspace less `.md`, in the workspace's `scratch/` directory; in a standalone branch review, which has no workspace, `review-<base7>..<head7>/` in the host's temporary directory.

## Models and effort

These rules bind every dispatch; each skill names its own seats' rows.

- **Name the model** on every dispatch (`crucible:using-crucible`
  § The Rule, Dispatching an agent).
- **Roles, not rosters.** A row names one of three roles, always with the
  word "role". Your host map's **Model roles** entry names this host's
  model for each, and the floor no dispatch goes below.
  - **The default role** — the strong model almost every seat runs on, and
    the ceiling of the automatic escalation.
  - **The bounded role** — for a clearly bounded task: one step below the
    default role, or the default role's model itself where the host has no
    qualifying tier between. Never dispatch below it.
  - **The alternate role** — the host's other strong model, which no
    escalation reaches. Exactly three triggers select it: round 1's swap
    (`skills/redteaming/SKILL.md` § Panels); work of a kind your host map
    lists as a weak spot of its default role, at any implementer, reviewer
    or redteam seat — never the blind verifier, whose work is checking a
    fix list against a diff; and the operator's request, at any seat. A
    host map naming no alternate skips all three.
- **Effort is the operator's.** Leave a dispatch's reasoning effort unset
  unless the operator asks for one; no flow sets or raises it on its own.
  An escalation is the tier bump alone; where that is not enough, the
  dispatching skill's stop points take it to the operator.

## Shared-tree rules

These bind every controller that dispatches seats into a worktree; the
dispatching skill names its windows.

- **No commits while a seat works.** While a dispatched seat works in the
  worktree, commit nothing there: the index is shared, so a bare commit
  sweeps in whatever it staged. Queue the commit until the seat returns.
- **The status check, after every window your skill names.** Dispatch the
  window's seats with no tracked or staged change, first writing the output
  of `git rev-parse HEAD` and `git status --porcelain --untracked-files=all`
  to `<workspace>/tree-check.txt`, overwriting it, unless a seat still out
  opened the window: seats out at the same time are one window, the file
  written before the first and checked after the last. When the window's
  last seat returns, before the next commit, run the two commands again:
  output differing from the file's voids every report from the window
  until it runs again on a clean tree. Untracked paths present at dispatch,
  such as an implementer's test leftovers, are tolerated. A controller
  resumed after a compaction reads the dispatch-time state in the file.
  Seats' `scratch/` lives in the gitignored workspace and never shows.
- **Replacing a seat.** Never start a replacement until the host confirms
  the first seat has stopped: one started early puts two writers on one
  tree. It writes to a fresh report path, as its skill names it; the
  first's file stays as the record. A seat whose state the host cannot
  confirm is a stop-and-ask.
