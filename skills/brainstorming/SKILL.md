---
name: brainstorming
description: Use before any feature work — creating features, building components, adding functionality, or changing behavior.
---

# Brainstorming Ideas Into Designs

Turn an idea into an intent-weighted design spec through collaborative dialogue, then hand it to the spec campaign. Output: a spec per the contract below, plus a design digest for major designs. Terminal state: invoke `crucible:redteaming` — never an implementation or planning skill. There are two exceptions: the operator-confirmed very-small lane, whose output is a lane note and whose terminal state is SDD's lane section, and an umbrella the operator approves without a campaign, whose terminal state is its landing (§ Handoff).

<HARD-GATE>
Do NOT invoke any implementation skill, write any code (a context-gathering probe aside, § Context gathering), scaffold any project, or take any implementation action until the design is approved, the spec is written (the lane note, on the very-small lane), and the handoff below has run. This applies to EVERY feature regardless of perceived simplicity.
</HARD-GATE>

**"Too simple to need a design" is the anti-pattern.** Simple features are where unexamined assumptions waste the most work. The design can be a few sentences — but it goes through this process.

## Flow

1. **Gather context** — aggressively, before the dialogue
2. **Clarifying dialogue** — one question at a time; scope-decomposition check early
3. **Propose 2–3 approaches** — trade-offs, lead with your recommendation
4. **Present the design in sections** — approval per section, closing with the proposed arrangement (the operator confirms or vetoes its preset here); where the effort takes several features, an umbrella and its review
5. **Write the spec** — in the feature worktree, established first; shape per the spec contract below, or the combined spec+plan document on the folded lane, or the lane note on the very-small lane, or `<feature-folder>/umbrella.md` for an umbrella; the first write creates the feature folder (§ Spec contract)
6. **Spec self-review** — five checks, fix inline; on the very-small lane, and for an umbrella approved without a campaign, it ran on the draft before step 4's answer, and the file is written as approved
7. **Provision the feature workspace**
8. **Author the design digest** — derived; major designs only
9. **Digest gate** — operator reviews digest + open decision asks + campaign shape; none on the very-small lane or for an umbrella approved without a campaign
10. **Hand off** — invoke `crucible:redteaming` for the spec campaign, or SDD's lane section on the very-small lane, or, for an umbrella approved without a campaign, its landing

## Context gathering (before any question)

Explore the project state first: files, docs, recent commits, existing specs and plans, backlog items touching the area. The operator's steering time is expensive — arrive at the dialogue already knowing what the repo knows. Every question the repo can answer is a question you don't ask. A throwaway probe outside the tracked tree, in the host's temporary directory, that answers a question (run a command, try a library call) is context gathering, not the code the HARD-GATE forbids: it is never committed, and what it showed enters the dialogue.

**An incoming document** — a requirements document, an issue, a plan crucible did not write — is the brainstorm's input: what it settles stays settled, the dialogue asks only what it leaves open, and what you write still gets its route's review. A foreign plan takes the route that fits it, proposed at step 4 like any other; the spec adds the sections reviewers bind to, and the plan's tasks are reused where the route carries a plan — on the standard route, keep the plan in the feature folder under a descriptive name for `crucible:writing-plans` to read beside the spec. A child's entry in its umbrella is such a document, and a session resuming an effort an umbrella holds starts from that umbrella: both by `skills/brainstorming/references/umbrellas.md`.

## The dialogue

- **One question per message.** Prefer multiple choice where it fits; open-ended is fine too. If a topic needs more exploration, break it into successive questions.
- **Scope-decomposition check, early:** if the request spans multiple independent subsystems, flag it before refining details. Help decompose into sub-features — what are the independent pieces, how do they relate, what order — then brainstorm the first one. Each sub-feature gets its own spec → campaign → plan cycle. Where the sub-features share decisions, an order, or both, brainstorm the umbrella that holds them first (§ Umbrellas — an effort that takes several features).
- Focus on understanding: purpose, constraints, success criteria.

**Approaches:** propose 2–3 with trade-offs; lead with your recommendation and why. YAGNI ruthlessly — cut unnecessary features from every approach.

**Presenting the design:** sections scaled to their complexity (a few sentences to a few hundred words); ask after each section whether it looks right. Cover architecture, component boundaries, data flow, error handling, testing. Prefer small units with one clear purpose and well-defined interfaces — if internals can't change without breaking consumers, the boundaries need work. In existing codebases: follow existing patterns; include targeted improvements where existing problems affect the work; no unrelated refactoring. Close the presentation by naming the feature worktree, and its base where the git fallback sets it: the operator's approval of that message is the request `crucible:using-git-worktrees` needs.

### Proposing the arrangement (step 4)

A feature's arrangement is four choices: review before code (a spec campaign, or none), the plan's form (separate with its plan phase, folded into the spec, or none), per-task review (every task, or the branch review alone), and execution (inline or subagent). The branch review is no choice: every arrangement runs it, at full scope. Three presets combine the choices, standard the usual one:

| Preset | Review before code | Plan | Per-task review | Execution |
|---|---|---|---|---|
| standard | spec campaign | separate, with its plan phase | per task, the plan's call | per task |
| folded | spec campaign | folded into the spec, no plan phase | per task, the plan's call | per task |
| very-small | none: a lane note | none: the note's change list | none | inline by default |

Each choice is made where its information exists: the preset here; per-task review in the plan, where a task may carry `Review: branch only` (`crucible:writing-plans` § Per-task structure — four fields, all required); execution per task (`crucible:subagent-driven-development` § Inline mode, and on the very-small lane its reference). A campaign's width, its seats and rounds, is set at the digest gate and by the stop rule (`crucible:redteaming` § Stop rule and terminal pass).

**Unsupported**, each for its reason: per-task review with no plan (there are no tasks); a plan phase without a separate plan (the spec campaign reviews a folded one); a campaign on a lane note, or a spec with no campaign (a design that needs review before code is written as a spec, and one that needs none as a note); a lane note with a plan, or a spec with no plan (work that needs a plan takes a campaign preset, and a campaigned spec is planned); any arrangement without the branch review (it is the one review every arrangement keeps).

**Choose the preset by the overturn question** (`skills/subagent-driven-development/references/premise-and-questions.md` § The arrangement questions): where overturning a major mechanism after code is plausible, the feature takes a spec campaign; where that section's two cases make it not plausible, it takes none. Between the campaign presets, folded fits a plan of one or two tasks with no seam worth its own review, and standard fits the rest. Width is no test of risk, since the branch review reads the whole diff whatever its width, but it shapes the arrangement where work needs coordinating: a settled change one implementer can carry takes the very-small preset, its implementer dispatched where the work would crowd your context; a settled change that needs several coordinated tasks needs a plan, which only the campaign presets carry, so it takes standard, whose campaign can be expected to stop after its first round, the stop still the stop rule's call. File and line counts are not the test and are not offered as one. An umbrella's review is chosen by its content instead (§ Umbrellas — an effort that takes several features): it has no code of its own to review after.

**The proposal.** As you close the design presentation, propose a preset: name it, give the overturn answer with its reason and, for folded, the plan-size reason; recommend one and let the operator rule, presenting a close call as one. The operator confirms the preset. Per-task review is the plan's, reported at the close of the phase that reviews the plan, and execution is chosen per task, so a departure you expect only later ("most tasks will likely be branch review only") is a heads-up, not something to confirm. The preset is never yours to declare.

**Record the operator's answer as the route entry in the brainstorm decision record** (§ Workspace provisioning (brainstorm exit)), whatever the preset. It is how the confirmation reaches the workspace and, from there, the campaign or the lane: a fold or a lane with no entry is one nobody downstream can see, and reads as unconfirmed. There is no entry mid-flight: a feature past this step keeps its preset, the lane's upgrade hatch, an unfold and a late split (`skills/redteaming/references/flip-paths.md`) aside; folding a design whose spec is written is a supersede.

What stays route-specific:

- **Folded.** One combined spec+plan document, written at step 5; `crucible:redteaming` § The folded lane carries the campaign, deferral, exit and unfolding rules. A folded feature is a minor design by construction: its plan is small enough that the decision record's decisions and open asks, presented inline at the digest gate, steer it, so it has no digest.
- **Very-small.** Draft the lane note (§ The very-small lane — the lane note (step 5)) and run the self-review on the draft before proposing, and show it with the proposal: the operator's one answer confirms or vetoes the preset and approves or amends the note, and the file is written only after it; a veto discards the draft. What runs is carried by `crucible:subagent-driven-development § The very-small lane`. It is a minor design by construction, with no digest and no digest gate: the answer here is its gate.

### Umbrellas — an effort that takes several features

Where the sub-features of an effort share decisions, an order, or both, an umbrella (`<feature-folder>/umbrella.md`) holds it, proposed at this step with its review: a spec campaign, or the operator's approval. **Before proposing or writing an umbrella, brainstorming a child of one, or resuming an effort one holds, read `skills/brainstorming/references/umbrellas.md` in full, and re-read it after compaction; it binds as if written here.**

## Spec contract

**Verification happens at the moment of writing.** A sentence claiming something about existing code, files, or tool behavior is checked as it is written — read the file, run the command — never left for a sweep afterwards; what cannot be checked now is written with `UNVERIFIED` on it rather than asserted. Treat every unverified claim in a draft as wrong until checked: a checked sentence beats a fast one.

Audience: the agent fleet. Sections, in order:

- **Request** — the message that asked for the work, and each later message that changed what was asked, quoted verbatim; a message you are unsure changed it is included. It stands outside the parts any route makes binding: it is evidence of what was asked, not the standard, and seats check the Intent against it (`skills/subagent-driven-development/references/premise-and-questions.md` § The goal check). A part the project's rules for committed text keep out is replaced by `[redacted: <kind>]`; where no rule settles whether a part may be committed, ask the operator once, as you write the section. A child of an umbrella quotes what `skills/brainstorming/references/umbrellas.md` § Shape states.
- **Intent** — problem, goals, non-goals.
- **Decisions** — each with rationale. A decision is lightly held — downstream may flip it with a logged rationale — unless firm or marked. A firm one, recorded `firm` (§ Workspace provisioning (brainstorm exit)), says in its rationale that it is the operator's firm preference. A mark, **`[LOAD-BEARING: <what builds on it>]`**, binds exactly the sentence or bullet it annotates, and is earned only where something beyond that sentence builds on the decision — other tasks, other features or children, an outside commitment — never by a wording, a threshold only this feature uses, or the operator's preference.
- **Constraints & invariants** — binding by construction, with no mark: invariants every task must keep, not a requirement one site meets. Every downstream agent reads it here, in the spec at its pinned revision; plans point at it and never copy it.
- **Interfaces & boundaries**.
- **Acceptance** — observable outcomes; each maps to a **standing test**, where a later change could plausibly break it, or to a **one-time check**, run once and recorded as its command and quoted output; or states why neither. An absence criterion ("X is gone") is one-time unless a named later change could undo it.
- **Mechanism sketches** — advisory; implementers and planners may replace them.

**What binds**, from the spec campaign's close: Constraints & invariants, marks, firm decisions, preamble conventions the spec declares binding, and the umbrella content its umbrella line brings in, firm decisions included. The spec is a hypothesis, probably subtly wrong and certainly locally imperfect: binding text is never changed silently — it changes only by `skills/redteaming/references/flip-paths.md`, whose § The containment test says who confirms — and is read for its intent, a case its literal reading reaches that its author plainly did not consider raised for a ruling, never applied literally.

No code beyond illustrative fragments in advisory sections. Mechanism detail creeping into binding sections is a campaign finding — keep binding sections at intent altitude. **Persistence: the spec is `<feature-folder>/design.md`, in the feature's *feature folder*, by default `docs/crucible/<YYYY-MM-DD>-<feature-slug>/`** — the folder layout and the role names (`<feature-folder>/folded.md` and `<feature-folder>/note.md` on the two small routes) are defined in `skills/redteaming/references/formats.md` § Feature folder; read them there. A child of an umbrella carries the umbrella line in its preamble, on every route (`skills/brainstorming/references/umbrellas.md`). Write it in the **feature worktree**, established before the first write with `crucible:using-git-worktrees` Steps 0–1 on a branch named for `<feature-slug>` (its setup and baseline steps wait for SDD Setup); a linked worktree that belongs to another feature is not this one's, so create this feature's own whatever Step 0 concludes, with Step 1b, from the repo's base branch or a base the operator names, in the main checkout's worktree directory: the spec, the workspace and the records all live in the feature worktree. The **first** spec write creates the folder by the **birth step** of `skills/redteaming/references/formats.md` § Feature folder, which refuses a slug that already has a folder, and writes the spec into it; every later write — a resumed brainstorm, an amendment at the digest gate — finds the folder by its **resolve step**, which creates nothing.

`<feature-slug>` names the branch, the folder and the workspace step 7 provisions, so it is chosen before the worktree. Commit the spec on the feature branch (worktree agents can't read gitignored files). A shipped spec is never silently edited.

**Deferral device.** Detail an implementer at the code will judge better is deferred, not pinned: mark it `Deferred to implementation: <what>` on its own line or bullet, in the section that owns it. The marker is grep-able, so the plan's routing table is assembled from these markers mechanically and each one is assigned an owning task there — until then a deferred item is owner-pending, which is the only stage at which it may be unowned. Binding and cross-task content is never deferrable. How the campaign reviews a deferral is `crucible:redteaming` § Merge and finding hygiene.

### The folded lane — the combined spec+plan document (step 5)

Where the operator confirmed the fold at step 4, this step writes one combined spec+plan document in place of a spec. **Before writing it, read `skills/brainstorming/references/folded-lane-document.md` in full, and re-read it after compaction; it binds as if written here.**

### The very-small lane — the lane note (step 5)

On the very-small lane the lane note takes the spec's place: drafted at step 4, written at this step as the operator approved it. **Before drafting it, read `skills/brainstorming/references/lane-note.md` in full, and re-read it after compaction; it binds as if written here.**

## Spec self-review

After writing, re-read with fresh eyes:

1. **Placeholder scan:** any "TBD", "TODO", incomplete sections, vague requirements? Fix them. An explicit `Deferred to implementation:` marker is exempt — it is a recorded decision about who decides, not an unfinished sentence.
2. **Internal consistency:** do sections contradict each other? Does the architecture match the feature descriptions?
3. **Scope check:** focused enough for a single implementation plan, or does it need decomposition? Parts that share decisions, an order, or both take an umbrella (§ Umbrellas — an effort that takes several features).
4. **Ambiguity check:** could any requirement be read two ways? Pick one and make it explicit — unless it carries a `Deferred to implementation:` marker, where picking is the implementer's job and the marker is what makes that explicit.
5. **Evidence check:** every claim the spec makes about existing code, files, or tool behavior was verified when written — you read or ran the thing — or carries `UNVERIFIED`. Resolve the tags now, or leave them standing as declared input for the campaign. Then the **consumer sweep**: for each symbol, file, or interface the design changes, deletes, or constrains, enumerate its existing consumers mechanically — by search, not from memory — and account for each one in the design. A rule stated in more than one place — docs, prompts, templates — is such an interface: its consumers are every site that states it, found by searching its key terms. Then the **trace**: for each rule the design ties to a trigger ("at each X, do Y"), name every route and phase that must reach the rule — the standard route, the folded lane, the very-small lane, an umbrella; brainstorm, spec campaign, plan phase, execution, branch review, finish — and the moment X occurs in each; where X occurs and nothing reaches the rule, the design has a gap. An unenumerated consumer and an unchecked claim are the two largest measured finding classes; both are cheaper to catch here than to buy a campaign dispatch for.

Fix inline; no re-review loop — fix and move on.

## Workspace provisioning (brainstorm exit)

One workspace per feature, provisioned now by the provisioning step of `skills/redteaming/references/formats.md` § Feature workspace root and layout, living until an end its Lifecycle names — campaigns and SDD store their records in its subdirectories, laid out as that file defines. Then write the **brainstorm dialogue's decision record** to `<workspace>/brainstorm-decisions.md` — one entry per decision made in the dialogue: the decision, its rationale, and its status with its proposer, the operator or the controller (`accepted — proposed by the controller`). Statuses: `open`; `accepted`, the default for any approval ("+", "OK" and "your call" included), meaning "this until new evidence arrives"; `firm`, only on the operator's explicit word, never inferred from an approval. A route entry, written for every preset (§ Proposing the arrangement (step 4)), confirms its preset only when `accepted` or `firm`. Later operator rulings enter this record too (`skills/redteaming/references/formats.md` § Feature workspace root and layout). This record is the digest's first derivation source and must exist on disk before the digest does.

## Design digest

The digest and the decision record exist because crucible's default operator steers by decision asks rather than by reading specs or code: reading those is never required, though never withheld.

**Major designs only** — controller judgment; when in doubt, ask the operator one question. For minor designs, skip the digest.

Write it to `<workspace>/digest.md` in the format `skills/redteaming/references/formats.md` § Design digest format defines, its binding derivation rule included; read it there. At brainstorm exit only the decision record exists to derive from, so the initial digest is derived from it alone; campaigns extend it at round closes.

## Digest gate

The operator reviews the **digest, the open decision asks and the planned campaign shape**; the gate never requires reading the spec file. Present the digest content and every open judgment with its recommendation — for a minor design with no digest, the decision record's decisions and open asks inline — and show whatever part of the spec the operator asks for. The campaign shape is its seats with their lenses and models, and its expected rounds, sized per `crucible:redteaming` § Panels: approving the design approves the launch. Record the approved shape as one gate entry in the decision record; the campaign-start readout names any departure from it.

Wait for the operator. Changes requested → amend the spec, re-run the self-review, update the decision record and digest, re-gate. Approved → hand off.

## Handoff

Invoke `crucible:redteaming` to run the spec campaign; its records live under `<workspace>/campaigns/spec/`. **The campaign is this skill's terminal state.** Do not invoke any planning or implementation skill from here — after the campaign converges, its own close readout names the next handoff (`crucible:redteaming` § Exit).

**On the very-small lane the handoff is to SDD instead:** invoke `crucible:subagent-driven-development § The very-small lane`, with the committed lane note and the decision record's lane entry as its inputs. That section, not the campaign, is this skill's terminal state on the lane — the one implementation handoff this skill makes, licensed by the operator's confirmation at step 4 and by nothing else.

**An umbrella's handoff follows its review.** A campaigned umbrella hands off to `crucible:redteaming` as above, and the campaign's close leads to its landing. An umbrella the operator approved without a campaign has its landing as this skill's terminal state: the steps `skills/brainstorming/references/umbrellas.md` states, then `crucible:finishing-a-development-branch`. Neither invokes a planning or implementation skill; its children write the plans.
