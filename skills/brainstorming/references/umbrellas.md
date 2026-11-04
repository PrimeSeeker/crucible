### Umbrellas

An **umbrella** holds an effort too large for one feature: what its parts share, what each delivers, in what order, and which have landed, readable in its current state from one file. When to propose one: `crucible:brainstorming` § Umbrellas; sub-features that fail its test are separate features.

#### Shape

An umbrella is a spec of its own kind, with a feature's slug, branch, worktree, workspace and feature folder, but takes none of the three routes (§ Review). Its file is `umbrella.md` in its feature folder, born by the birth step of `skills/redteaming/references/formats.md` § Feature folder and written under the spec contract's sections:

- **Intent** — the effort's goal and non-goals.
- **Decisions**, **Constraints & invariants**, **Interfaces & boundaries** (what children provide each other) and **Mechanism sketches**, where it has them. Interfaces & boundaries only describe; a contract between children that must bind goes in Constraints & invariants.
- **Acceptance** — the Children list, stating that each child's own Acceptance carries the checks.

A campaigned umbrella carries every section, so its seats grade it as a spec. No `Deferred to implementation:` marker: detail it leaves open goes in the owning child's entry.

**The Children list** is ordered, one entry per child, with a blank line between entries. An entry names the child's slug, what it must deliver, what it waits on, and its mark (`skills/brainstorming/references/umbrella-children.md` § Marks):

    - `cache-layer` — a read-through cache behind the store interface; waits on nothing — landed

    - `cache-metrics` — hit-rate metrics for the cache layer; waits on `cache-layer`

**Recursion.** A child that splits becomes an umbrella over its own children; its entry in its parent says so. Each umbrella holds only what its children share; what one child alone needs moves down into that child's entry. No depth cap.

**Folders stay flat.** A child's feature folder is born at the root and resolved like any other; the Children list indexes an umbrella's children, and a child's umbrella line names its parent.

#### Review

An umbrella with Decisions, Constraints & invariants or Interfaces & boundaries takes a spec campaign: steps 5–9 as a spec does, the campaign's close handing off to its landing.

One without them (Mechanism sketches aside) is approved by the operator as a lane note is: drafted, self-reviewed and shown with the proposal at step 4, written as approved at step 5, its workspace provisioned at step 7; with no campaign gate, its handoff is its landing.

Propose which at step 4; the operator's ruling is an entry in the brainstorm decision record. This classifies an umbrella at birth; the operator rules whether a later binding change (`umbrella-children.md` § Edits) takes a campaign. Neither kind takes a plan phase or SDD: its children write the plans.

#### Landing

An umbrella lands before its first child, through `crucible:finishing-a-development-branch`, so children branch from a base that holds it. Before it lands:

1. Where a campaign ran, check its round records and readouts and name any gap in the campaign's close readout.
2. Note each premise finding still open as `open premise ask: <the ask>` in the first unmarked entry of the umbrella's own Children list, after what that child must deliver, and add it to the landing ask (`skills/redteaming/references/premise-asks.md` § Premise findings, The ask and The ruling). The landing does not wait for a ruling; one given before landing takes its route there and drops the note.
3. Add every other open decision ask to the landing ask. Send the work left open (the kinds under **What earlier phases left open** in `skills/subagent-driven-development/references/setup.md`, the campaign's `deferred-minor` entries, and those asks unruled at the landing) where `formats.md` § Open items sends it, an in-repository home's committed on this branch; if the project names no home, the landing ask asks where, and step 4 waits for the answer.
4. Delete the umbrella's workspace (`formats.md` § Feature workspace root and layout, Lifecycle).
5. For a nested umbrella, mark its entry in its parent `umbrella`, in the same landing.

The landing ask's decision asks stand apart (`crucible:redteaming` § Round readout).

After the landing, the effort resumes at its first child (`umbrella-children.md` § Resuming).

#### Closing

An umbrella is closed when every entry is marked `landed`, `dropped`, or `umbrella` with that umbrella itself closed: closure is read recursively, never written upward. Once closed, the umbrella is frozen. Whether a dropped child becomes a backlog item is the operator's call.

#### Closing review

Once an umbrella is complete (§ Closing), one review reads its children's landings, from the umbrella's own to the completing one (unrelated landings on a shared base aside), against the umbrella's Intent, entries, Constraints & invariants and decisions. It is a step after the last landing, not a gate: closing is still read from the marks, nothing waits on it, and it writes nothing into `umbrella.md`. An umbrella approved without a campaign takes it too: it reads code the children wrote.

**When.** If your landing completes the umbrella, a landed drop included, announce the review and run it right after; its width is your call, the review is not optional. A completing child's close readout (`crucible:subagent-driven-development` § Finish) names it as the next step. Where the completing landing may happen outside a session, the close readout of every child that could complete it, siblings in flight counted, names it as due once all have landed; the operator starts it by asking. A nested umbrella's review runs at its own completion, before its parent's, whose range covers it again.

**Seats.** Provision a workspace under the umbrella's slug in the session's checkout (`formats.md` § Feature workspace root and layout). Compose two or three dispatches on the default role, each carrying the seven items of `skills/subagent-driven-development/references/dispatch-composition.md`, read-only but for its report file, each with a lens reading across children: fidelity to the umbrella's Intent, the seams between children, a walkthrough of the workflows the effort changed. Copy into each prompt `skills/subagent-driven-development/references/seat-rules.md` § Premise findings, § Binding items and unrecorded choices, § Questions and § Location. Each seat writes `.crucible/<umbrella-slug>/closing-<lens>.md` (as `closing-seams.md`), the `closing-` prefix fixed. Their window takes the dispatch composition's status check.

**Its records.** The readout lists each finding (each `Questions` item counting as one throughout) with your keep-or-drop proposal; a premise finding gets one too and is a decision ask, its asks standing apart (`crucible:redteaming` § Round readout). If the project names no open-items home and any finding is listed, it also asks where kept ones go (`formats.md` § Open items). After the answer, kept findings and every premise finding with its ruling go where that section sends them, an in-repository home's committed on a branch of their own and landed on the operator's go-ahead. Nothing kept and no premise finding: nothing is written, the readout naming each dropped finding. Then delete the workspace. Fixing the findings is a feature of its own, taking them as its incoming document.
