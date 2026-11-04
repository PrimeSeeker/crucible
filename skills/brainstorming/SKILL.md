---
name: brainstorming
description: Use before any feature work — creating features, building components, adding functionality, or changing behavior.
---

# Brainstorming Ideas Into Designs

Turn an idea into an intent-weighted design spec (§ Spec contract) through collaborative dialogue. Terminal state: invoke `crucible:redteaming`, never an implementation or planning skill; § Handoff states the exceptions, none a planning skill.

<HARD-GATE>
Do NOT invoke any implementation skill, write any code (a context-gathering probe aside, § Context gathering), scaffold any project, or take any implementation action until the design is approved, the spec is written (the lane note, on the very-small lane), and the handoff below has run. This applies to EVERY feature regardless of perceived simplicity.
</HARD-GATE>

"Too simple to need a design" is the anti-pattern: simple features are where unexamined assumptions waste the most work. The design can be a few sentences.

**Stubs.** A reference a section names to read in full binds as if written here. Read it when its step comes, unless read since your last compaction; after compaction, re-read the step in progress's reference first.

## Flow

1. Gather context, aggressively
2. Clarifying dialogue
3. Propose 2–3 approaches
4. Present the design in sections
5. Write the spec
6. Spec self-review
7. Provision the feature workspace
8. Campaign gate
9. Hand off

## Context gathering (before any question)

Explore the project state: files, docs, recent commits, existing specs and plans, backlog items touching the area, and open items in their home (`skills/redteaming/references/formats.md` § Open items). Ask nothing the repo can answer: the operator's steering time is expensive. A throwaway probe in the host's temporary directory that answers a question (run a command, try a library call) is context gathering, not code the HARD-GATE forbids: it is never committed, and what it showed enters the dialogue.

**An incoming document** (a requirements document, an issue, a plan crucible did not write) is the brainstorm's input: what it settles stays settled, the dialogue asks only what it leaves open, and what you write still gets its route's review. A foreign plan takes the route that fits it, proposed at step 4; the spec adds the sections reviewers bind to, and the plan's tasks are reused where the route carries a plan. On the standard route, keep the plan in the feature folder under a descriptive name for `crucible:writing-plans` to read beside the spec. A child's entry in its umbrella is such a document, and a session resuming an effort an umbrella holds starts from that umbrella (§ Umbrella children).

## The dialogue

- One question per message, multiple choice preferred where it fits. Break a topic that needs more exploration into successive questions.
- Scope-decomposition check, early: if the request spans multiple independent subsystems, flag it before refining details, help decompose it into sub-features (the independent pieces, how they relate, their order), then brainstorm the first. Each sub-feature gets its own spec → campaign → plan cycle; where § Umbrellas' criterion holds, brainstorm the umbrella first.
- Focus on understanding: purpose, constraints, success criteria.

**Approaches:** propose 2–3 with trade-offs, leading with your recommendation and why. Apply YAGNI ruthlessly: cut unneeded features from every approach.

**Presenting the design:** in sections scaled to their complexity (a few sentences to a few hundred words), asking after each whether it looks right. Cover architecture, component boundaries, data flow, error handling, testing and any break (§ Spec contract). Prefer small units with one clear purpose and well-defined interfaces: if internals can't change without breaking consumers, the boundaries need work. In existing codebases, follow existing patterns and include targeted improvements where existing problems affect the work; no unrelated refactoring.

Close the presentation by naming the feature worktree, and its base where the git fallback sets it: the operator's approval of that message is the request `crucible:using-git-worktrees` needs. Choose `<feature-slug>` before the worktree: it names the branch, the feature folder and the workspace. Before the first write, establish the worktree with that skill's Steps 0–1 on a branch named for the slug (its setup and baseline steps wait for SDD Setup). It is this feature's own even inside another feature's worktree, and the spec, the workspace and the records all live there.

### Proposing the arrangement

**As the design presentation closes, before choosing the preset to propose, read `skills/brainstorming/references/proposing-the-arrangement.md` in full.** The operator confirms or vetoes the preset; it is never yours to declare. Record their answer, whatever the preset, as the route entry in the brainstorm decision record (§ Workspace provisioning). The entry confirms its preset only when `accepted` or `firm`; a fold or a lane with no entry reads downstream as unconfirmed. A feature past step 4 keeps its preset, except through an unfold, a late split (§ Umbrella children) or the lane's upgrade hatch (`skills/subagent-driven-development/references/very-small-lane.md`). The hatch is the one route entry mid-flight: its answer to move is recorded in the same record. Folding a design whose spec is written is a supersede.

### Umbrellas

Where an effort's sub-features share decisions, an order, or both, an umbrella (`<feature-folder>/umbrella.md`) holds it, proposed at step 4 with its review: a spec campaign or the operator's approval. **Before proposing or writing an umbrella, read `skills/brainstorming/references/umbrellas.md` in full, and re-read it after compaction.**

### Umbrella children

**Before writing an umbrella, brainstorming a child of one, or resuming an effort one holds, read `skills/brainstorming/references/umbrella-children.md` in full, and re-read it after compaction.**

## Spec contract

**Verification at the moment of writing.** Check each sentence claiming something about existing code, files or tool behavior as you write it (read the file, run the command), never in a later sweep; mark what cannot be checked now `UNVERIFIED` rather than asserting it. Treat every unverified claim in a draft as wrong until checked.

Audience: the agent fleet. The spec quotes no operator message: the Intent states the goal in its own words, and the asking messages go to the request file (§ Workspace provisioning). Sections, in order:

- **Intent** — problem, goals, non-goals, and any break this landing makes, saying until when or that it is permanent: something the base does today stops working, or a path someone can reach fails. Work nobody can reach yet is not a break.
- **Decisions** — each with rationale. A decision is lightly held (downstream may flip it with a logged rationale) unless firm; a firm one, recorded `firm` (§ Workspace provisioning), says in its rationale that it is the operator's firm preference.
- **Constraints & invariants** — binding by construction: invariants every task must keep, not a requirement one site meets. Every downstream agent reads it here, in the spec at its pinned revision.
- **Interfaces & boundaries**.
- **Acceptance** — observable outcomes, each mapping to a standing test or a one-time check (`crucible:writing-plans` § Acceptance maps to checks) or stating why neither.
- **Mechanism sketches** — advisory; implementers and planners may replace them.

What binds in a spec and how binding text is read: `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec; how the spec changes after the campaign's close: `skills/redteaming/references/flip-paths.md`.

No code beyond illustrative fragments in advisory sections. Keep binding sections at intent altitude: mechanism detail in them is a campaign finding.

**Persistence:** the spec is `<feature-folder>/design.md`, the folder by default `docs/crucible/<YYYY-MM-DD>-<feature-slug>/`; the folder layout, the role names `<feature-folder>/folded.md` and `<feature-folder>/note.md` (the two small routes), and the birth and resolve steps are in formats.md § Feature folder. A child of an umbrella carries the umbrella line in its preamble on every route (§ Umbrella children). The first spec write creates the folder by the birth step; every later write (a resumed brainstorm, an amendment at the campaign gate, the hatch's spec) finds it by the resolve step. Commit the spec on the feature branch: worktree agents can't read gitignored files. A shipped spec is never silently edited.

**Deferral device.** Detail an implementer at the code will judge better is deferred, not pinned: mark it `Deferred to implementation: <what>` on its own line or bullet, in the section that owns it. Until the plan names its owner, a deferred item is owner-pending, the only stage at which it may be unowned. What is never deferrable, and how the plan gives each marker an owning task: `crucible:writing-plans` § Deferring detail.

### The folded lane — the combined spec+plan document (step 5)

Where the operator confirmed the fold at step 4, this step writes one combined spec+plan document in place of a spec. **Before writing it, read `skills/brainstorming/references/folded-lane-document.md` in full.**

### The very-small lane

On the very-small lane the lane note takes the spec's place. **Before drafting it, read `skills/brainstorming/references/lane-note.md` in full.**

## Spec self-review

After writing, re-read with fresh eyes (where step 4's answer approved a draft, this ran on the draft):

1. **Placeholder scan:** fix any "TBD", "TODO", incomplete section or vague requirement. A `Deferred to implementation:` marker is exempt: it records who decides, not an unfinished sentence.
2. **Internal consistency:** do sections contradict each other? Does the architecture match the feature descriptions?
3. **Scope check:** focused enough for a single implementation plan, or does it need decomposition? Parts meeting § Umbrellas' criterion take an umbrella.
4. **Ambiguity check:** where a requirement reads two ways, pick one and make it explicit, unless it carries a `Deferred to implementation:` marker; then picking is the implementer's job.
5. **Evidence check:** every claim § Spec contract's verification rule covers was verified when written or carries `UNVERIFIED`; resolve the tags now, or leave them standing as declared input for the campaign. Then the **consumer sweep**: for each symbol, file or interface the design changes, deletes or constrains, find its existing consumers by search, not from memory, and account for each in the design. A rule stated in more than one place (docs, prompts, templates) is such an interface: its consumers are every site stating it, found by searching its key terms. Then the **trace**: for each rule the design ties to a trigger ("at each X, do Y"), name every route (standard, folded lane, very-small lane, umbrella) and phase (brainstorm, spec campaign, plan phase, execution, branch review, finish) that must reach it, and the moment X occurs in each; where X occurs and nothing reaches the rule, the design has a gap.

Fix inline; no re-review loop.

## Workspace provisioning

Provision one workspace per feature now, by the provisioning step of formats.md § Feature workspace root and layout. Then write the **brainstorm dialogue's decision record** to `<workspace>/brainstorm-decisions.md`: one entry per dialogue decision, with the decision, its rationale, and its status with its proposer, the operator or the controller (`accepted — proposed by the controller`). Statuses: `open`; `accepted`, the default for any approval ("+", "OK" and "your call" included), meaning "this until new evidence arrives"; `firm`, only on the operator's explicit word, never inferred from an approval. An answer that leaves the call to you ("your call") is recorded `accepted — delegated to the controller`, in the proposer's place, never as the operator's ruling or choice.

Then write the request to `<workspace>/request.md`: the message that asked for the work and each later message that changed what was asked, quoted verbatim, a message you are unsure changed it included. A child of an umbrella quotes only its own brainstorm's messages. Redact nothing: like the workspace, the file is never committed. Later messages changing the ask are appended to it, and later operator rulings enter the decision record, as formats.md § Feature workspace root and layout states.

## Campaign gate

None where step 4's answer approved a draft. Otherwise the operator reviews the decision record's decisions, its open decision asks and the planned campaign shape, presented inline; the gate never requires reading the spec file, and shows whatever part of it the operator asks for. The open asks stand apart (`crucible:redteaming` § Round readout). The campaign shape is its seats with their lenses and models, and its expected rounds, sized per `crucible:redteaming` § Panels; approving the design approves the launch. Record the approved shape as one gate entry in the decision record; the campaign-start readout names any departure from it. Wait for the operator. Changes requested → amend the spec, re-run the self-review, update the decision record, re-gate. Approved → hand off.

## Handoff

Invoke `crucible:redteaming` to run the spec campaign; its records live under `<workspace>/campaigns/spec/`. After it converges, its own close readout names the next handoff (`crucible:redteaming` § Exit).

On the very-small lane, invoke `crucible:subagent-driven-development § The very-small lane` instead, with the committed lane note and the decision record's lane entry as its inputs: the lane's terminal state, and the one implementation handoff this skill makes, licensed by the operator's confirmation at step 4 and by nothing else.

An umbrella's handoff follows its review (`skills/brainstorming/references/umbrellas.md` § Review); one approved without a campaign has its landing as its terminal state.
