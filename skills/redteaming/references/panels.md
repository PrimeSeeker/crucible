## Panels

Panel size tracks both artifact maturity and artifact size, never a fixed number. Calibration (advisory): fresh large artifact round 1 = 4–5 seats; small artifact = 1 seat carrying several lenses; the round after a wave that added, removed or re-shaped a major mechanism = 1–2 seats.

**Lens roster** (a lens orders the search, never limits its scope: every seat reads the whole artifact every round):

- **correctness** (does what the artifact says hold on every path and input it covers)
- **evidence-and-inference** (are its claims verified and its measurements valid, and do its conclusions follow from them)
- **general** (unscoped) — at least one seat on every multi-seat round; a 1-seat round is general by default.
- **contract-fidelity** (does each interface match what its producers and consumers do) — when interface density warrants.
- **right-sizing** (cost-benefit scope-cutting) — round 1, then re-seated mid-campaign or when you judge the artifact has grown enough to need it, not every round; judged by the scope-cut decisions it produces.
- **abstraction-level** — for specs (mechanism detail creeping into binding sections is a finding).
- **outside-the-frame** (does the design solve the request's problem, for a child with its umbrella's Intent and entry, or would another framing, or no change, serve better) — one seat of every spec campaign's round 1 only, beside general in a one-seat round 1.

Rotate lenses across rounds and mix them per artifact; add a lens for whatever this artifact makes load-bearing, its one-line description in the lens slot as for a roster lens.

**Round 1's swap:** in a spec campaign's round 1 with two or more seats on this host, the seat you judge most architecture-heavy runs on the alternate role instead of the default; a seat on another host never counts toward those two and is never the swapped one, so a default-role seat always sits beside the swap; name it in the campaign shape you propose at brainstorming's campaign gate. A replacement for a lost swapped seat keeps the alternate role. No swap in a one-seat round 1 or the plan phase.

**Launch:** read the operator-approved campaign shape from the campaign-gate entry in the workspace's `brainstorm-decisions.md`, announce it in the campaign-start readout, naming any departure from that entry, and proceed without waiting for approval.

Dispatch each seat as instrument `redteam-seat` from its slot card; its report `seat-<id>.md` feeds your merge. Seats never see each other's reports, and a round's seats are independent: start every seat the host admits before waiting for any of them, and the rest as capacity frees. Record the roster (seat id, model, effort where set, lens) in the round record before or at dispatch, and each seat's identity in it before relying on continuation: an in-flight seat resumes by that identity rather than being re-dispatched.

**Quorum and degraded rounds:** record every lost or crashed seat, and what happened, in the round record's quorum block (cap arithmetic and the stop rule read it). A round that lost any dispatched seat, a seat on another host aside (below), is either topped back up (the lost seat re-dispatched) or explicitly recorded as degraded.

**Topping up** follows `skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules. The replacement takes a fresh id and writes its own `seat-<id>.md`, never the lost seat's file. A 1-seat round that loses its seat is degraded by definition: a crashed seat is never read as a clean pass.

**A seat on another host** runs only where the operator's instructions or request ask for one: never propose one. It is an extra seat: the round's seats on this host stay complete without it, required lenses included. It takes a lens and slot card like theirs; start it by your dispatch reference's **Seat on another host** entry. A run has no report where its report path holds no file, or one with no `## Index`, or where you stop it after 30 minutes. It goes in the quorum block as `not replaced`: no top-up, and it leaves `degraded` as it stands.

**Lens text**, filled verbatim into two seats' lens slots after the lens and its description. The right-sizing seat's:

> **Over-subtraction guard:** attest, in a dedicated `## Right-sized — do not cut` section last in your report, each area you examined and judged right-sized, and no area you did not examine. Fix waves consult that section before cutting: an area judged sound but not attested there is unprotected, and silence is never read as an attestation.

The plan phase's mechanical pre-pass's:

> **Ownership closure:** every file in the plan's census has exactly one owning task, and every `Deferred to implementation:` marker, the spec's and the plan's, at least one: a plan marker sits in its owning task; a spec marker is named by its site in the Contract of each task that owns it. A marker no task owns is a finding.
>
> **Set census:** for each set the plan adds a member to (an enumeration value, a case a dispatch or table handles, an item of a list spelled out in several places), list every place that enumerates the set, and that place's consumers, searching tracked files only (`git grep`), never the feature workspace. A place where the new member belongs that the plan's file census leaves out is a finding.
>
> **`## Worksheet`**, in your report between `## Index` and `## Findings`, holds your worked liveness, ownership-closure and overlap arithmetic and set census; tables, lists and sub-headings are fine. Enter each finding the work turns up under `## Findings`, not here.
