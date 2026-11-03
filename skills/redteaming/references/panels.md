## Panels

**Panel size tracks artifact maturity AND artifact size — never a fixed number.** Calibration (advisory): fresh large artifact round 1 = 4–5 seats; small artifact = 1 seat carrying several lenses; a round reading the result of a wave that added, removed or re-shaped a major mechanism (`crucible:redteaming` § Stop rule and terminal pass) = 1–2 seats. A 1-seat round is **general by default**.

**Lens roster** (a lens is a search-ordering hint, never a scope limit):

- **correctness** (does what the artifact says hold, on every path and input it covers)
- **evidence-and-inference** (are its claims verified and its measurements valid, and do its conclusions follow from them)
- **general** (unscoped) — at least one seat with no box on **every multi-seat round**.
- **contract-fidelity** (does each interface match what its producers and consumers do) — when interface density warrants.
- **right-sizing** (cost-benefit scope-cutting) — seated in round 1 and periodically after, not every round: re-seated mid-campaign, or when you judge the artifact has grown far enough to need it; judged by the scope-cut decisions it produces. Its seat carries the **over-subtraction guard**, attesting the areas it examined and judged right-sized (`skills/redteaming/seat-prompt.md`).
- **abstraction-level** — for specs (mechanism detail creeping into binding sections is a finding).
- **outside-the-frame** (does the design solve the request's problem, for a child with its umbrella's Intent and entry, or would another framing, or no change, serve better) — one seat of every spec campaign's round 1 only, beside general in a one-seat round 1.

Rotate lenses across rounds and mix them per artifact; add a lens for whatever this artifact makes load-bearing, its one-line description in the seat's lens slot as for a roster lens.

**Full-scope mandate always**: every seat reads the whole artifact every round; the lens only orders the search. **Agents never see each other's reports.**

**Round 1's swap:** in a spec campaign's round 1 with two or more seats on this host, the seat you judge most architecture-heavy runs on the alternate role in place of the default role; name it in the campaign shape you propose at brainstorming's campaign gate. A seat on another host neither counts toward those two nor is ever the swapped one, so a default-role seat always sits beside the swap; a replacement for a lost swapped seat keeps the alternate role. A one-seat round 1 has no swap, and neither has the plan phase.

Dispatch each seat as instrument `redteam-seat` with its filled slot card (`crucible:redteaming` § Dispatch composition); its report `seat-<id>.md` feeds your merge. **Seat ids are never reused within a feature**: every seat, a replacement included, takes an id no earlier seat of the feature has used, so the stop check traces each seat's forecast across rounds by its id. The one exception is the plan phase's pre-pass, whose fixed id `p0` a successor plan phase under supersede reuses. Seats of one round are independent by construction, so **start every seat the host admits before waiting for any of them**. Record the roster (seat id, model, effort where set, lens) in the round record before or at dispatch.

**Launch:** read the campaign shape the operator approved at brainstorming's campaign gate — the gate entry in the workspace's `brainstorm-decisions.md`, naming the seats with their lenses and models and the expected rounds. Announce the shape in the campaign-start readout, naming any departure from that entry, and **proceed — no approval wait**.

**Quorum and degraded rounds** (producer: the round record's quorum block; consumers: cap arithmetic and the stop rule): record every lost or crashed seat with what happened. A round that lost any dispatched seat is either **topped back up** (the lost seat re-dispatched) or explicitly recorded as **degraded**.

**Topping up** follows the replacement line of the shared-tree rules. The replacement writes a `seat-<id>.md` under a fresh id (above), never the lost seat's file. In-flight seats resume by their recorded identity rather than being re-dispatched, so record each seat's identity in the roster before relying on continuation. A 1-seat round losing its seat is degraded by definition — a crashed seat is never read as a clean pass.
