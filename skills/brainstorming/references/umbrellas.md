### Umbrellas

An **umbrella** holds an effort too large for one feature: what its parts share, what each part delivers, in what order, and which parts have landed, readable in its current state from one file. Propose one where the scope-decomposition check, self-review check 3 or the design at step 4 finds sub-features that share decisions, an order, or both; sub-features that share neither are separate features.

#### Shape

An umbrella is a spec of its own kind. It has a slug, a branch, a worktree, a workspace and a feature folder like a feature, and takes none of the three routes: its review is the one § Review states. Its file is `umbrella.md` in its feature folder, born by the birth step of `skills/redteaming/references/formats.md` § Feature folder and written under the spec contract's sections:

- **Intent** — the effort's goal and non-goals.
- **Decisions**, **Constraints & invariants**, **Interfaces & boundaries** (what children provide each other) and **Mechanism sketches**, where it has them. Its Interfaces & boundaries describe; a contract between children that must bind is one of its Constraints & invariants.
- **Acceptance** — the Children list, stating that each child's own Acceptance carries the checks.

A campaigned umbrella carries every section, so its seats grade it as the spec it is. It carries no `Deferred to implementation:` marker: detail it leaves open goes into the entry of the child that owns it.

**The Children list** is ordered, one entry per child, with a blank line between entries. An entry names the child's slug, what it must deliver, what it waits on, and its mark (`skills/brainstorming/references/umbrella-children.md` § Marks):

    - `cache-layer` — a read-through cache behind the store interface; waits on nothing — landed

    - `cache-metrics` — hit-rate metrics for the cache layer; waits on `cache-layer`

**Recursion.** A child that splits becomes an umbrella and the parent of its own children; its entry in its parent says so. Each umbrella holds only what its children share: what one child alone needs moves down into that child's entry. There is no depth cap.

**Folders stay flat.** A child's feature folder is born at the root like any other; the Children list is the index of an umbrella's children, and a child's umbrella line names its parent. Birth and resolve are unchanged.

#### Review

An umbrella carrying Decisions, Constraints & invariants or Interfaces & boundaries takes a spec campaign; one without them (Mechanism sketches aside) is approved by the operator, as a lane note is: drafted, self-reviewed and shown with the proposal at step 4, and written as approved. Propose which at step 4; the operator rules, and the ruling is an entry in the brainstorm decision record. Neither takes a plan phase or SDD: its children write the plans. This classifies an umbrella at its birth; the operator's ruling on a later binding change (`skills/brainstorming/references/umbrella-children.md` § Edits) says whether that change takes a campaign.

A campaigned umbrella takes steps 5–9 as a spec does, and the campaign's close hands off to its landing. An approval-only umbrella is written at step 5 as approved and its workspace provisioned at step 7; it takes no campaign gate, and its handoff is its landing.

#### Landing

An umbrella lands before its first child, through `crucible:finishing-a-development-branch`, so children branch from a base that holds it and other sessions can read it. Before it lands, its controller:

1. where a campaign ran, checks its records — round records and readouts — and names any gap in the campaign's close readout;
2. notes each premise finding still open in the first entry with no mark in its own Children list, after what that child must deliver, as `open premise ask: <the ask>`, and puts it to the operator with the landing ask, the ask itself as for any premise finding (`skills/redteaming/references/flip-paths.md` § Premise findings, The ask and The ruling); the landing does not wait for a ruling, and one given before it lands takes its route there and drops the note;
3. puts each decision ask still open, premise asks aside, to the operator with the landing ask, and sends what its brainstorm and campaign left open, of the kinds `skills/subagent-driven-development/references/setup.md` lists under **What earlier phases left open**, and its campaign's `deferred-minor` entries, where `skills/redteaming/references/formats.md` § Open items sends it, an in-repository home's items committed on its branch; an ask unruled at the landing goes with those items, and one ruled before it leaves them; where the project's instructions name no home, the landing ask lists them and asks where they go, with that section's offer to record the answer, and step 4 waits for the answer;
4. deletes the umbrella's workspace, an end of a workspace's life that the Lifecycle of `skills/redteaming/references/formats.md` § Feature workspace root and layout names;
5. for a nested umbrella, marks its entry in its parent `umbrella`, in the same landing.

The landing ask's decision asks stand apart, as `crucible:redteaming` § Round readout states.

After the landing, the effort resumes at its first child (`skills/brainstorming/references/umbrella-children.md` § Resuming).

#### Closing

An umbrella is closed when every entry is marked `landed` or `dropped`, or `umbrella` with that umbrella itself closed. Anyone reading it sees that, recursively; nothing is written upward. Whether a dropped child becomes a backlog item is the operator's call. From its close the umbrella is frozen.

#### Closing review

Once an umbrella is complete by § Closing's rule, one review reads its children's landings, from the umbrella's own to the one that completed it, unrelated landings on a shared base aside, against the umbrella: its Intent, its entries, its Constraints & invariants and its decisions. It is a step after the last landing, not a gate: closing is still read from the marks, nothing waits on the review, and it writes nothing into `umbrella.md`. An umbrella approved without a campaign takes it too, since it reads code the children wrote.

**When.** The controller whose landing completes the umbrella, a landed drop included, announces the review and runs it right after; its width is your call, the review itself is not optional. Where a child's landing completes it, that child's close readout (`crucible:subagent-driven-development` § Finish) names the review as the step after the landing. Where the completing landing may happen outside a session, such as a pull request merged later, the close readout of each child whose landing could complete the umbrella, siblings in flight counted, says the review is due once they have all landed, and the operator starts it by asking for it. A nested umbrella's review runs at its own completion; where that completes its parent, the parent's runs after it, its range covering the nested one again.

**Seats.** Two or three dispatches you compose on the default role, each carrying the seven items of `skills/subagent-driven-development/references/dispatch-composition.md`, read-only but for its report file, each with a lens that reads across children: fidelity to the umbrella's Intent, the seams between children, a walkthrough of the workflows the effort changed. Into each prompt you copy, from `skills/subagent-driven-development/references/seat-rules.md`, its sections § Premise findings, § Binding items and unrecorded choices, § Questions and § Location. Each writes its report to `.crucible/<umbrella-slug>/closing-<lens>.md` (`closing-seams.md`), the `closing-` prefix fixed: the workspace this review provisions under the umbrella's slug, in the checkout the session works in, by the provisioning step of `skills/redteaming/references/formats.md` § Feature workspace root and layout.

**Its records.** The review's readout lists each finding, each item of the seats' `Questions` counting as one throughout this paragraph, with your proposal to keep or drop it; a premise finding is a decision ask in it, its asks standing apart as `crucible:redteaming` § Round readout states. Where the project's instructions name no home for open items and the readout lists any finding, it also asks where those kept go, with the offer to record the answer (`skills/redteaming/references/formats.md` § Open items). After the operator's answer, the findings kept and each premise finding with its ruling go where that section sends them; an in-repository home's are committed on a branch of their own and landed on the operator's go-ahead. Where nothing is kept and no premise finding was raised, nothing is written, and the readout names each finding dropped. Then the workspace is deleted. A feature that fixes the findings is a feature of its own, taking them as its incoming document.
