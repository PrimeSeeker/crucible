---
name: brainstorming
description: Use before any feature work — creating features, building components, adding functionality, or changing behavior.
---

# Brainstorming Ideas Into Designs

Turn an idea into an intent-weighted design spec through collaborative dialogue, then hand it to the spec campaign. Output: a spec per the contract below. Terminal state: invoke `crucible:redteaming` — never an implementation or planning skill. There are two exceptions: the operator-confirmed very-small lane, whose output is a lane note and whose terminal state is SDD's lane section, and an umbrella the operator approves without a campaign, whose terminal state is its landing (§ Handoff).

<HARD-GATE>
Do NOT invoke any implementation skill, write any code (a context-gathering probe aside, § Context gathering), scaffold any project, or take any implementation action until the design is approved, the spec is written (the lane note, on the very-small lane), and the handoff below has run. This applies to EVERY feature regardless of perceived simplicity.
</HARD-GATE>

**"Too simple to need a design" is the anti-pattern.** Simple features are where unexamined assumptions waste the most work. The design can be a few sentences — but it goes through this process.

## Flow

1. **Gather context** — aggressively, before the dialogue
2. **Clarifying dialogue** — one question at a time; scope-decomposition check early
3. **Propose 2–3 approaches** — trade-offs, lead with your recommendation
4. **Present the design in sections** — approval per section, closing with the proposed arrangement (the operator confirms or vetoes its preset here); where the effort takes several features, an umbrella and its review
5. **Write the spec** — in the feature worktree, per the spec contract below, or the combined spec+plan document, lane note or umbrella that takes its place (§ Spec contract)
6. **Spec self-review** — five checks, fix inline; where step 4's answer approved a draft, it ran on the draft
7. **Provision the feature workspace** — its decision record and request file
8. **Campaign gate** — operator reviews the decision record's decisions + open decision asks + campaign shape; none where step 4's answer approved a draft
9. **Hand off** — § Handoff

## Context gathering (before any question)

Explore the project state first: files, docs, recent commits, existing specs and plans, backlog items touching the area, and open items in their home (`skills/redteaming/references/formats.md` § Open items). The operator's steering time is expensive — arrive at the dialogue already knowing what the repo knows. Every question the repo can answer is a question you don't ask. A throwaway probe outside the tracked tree, in the host's temporary directory, that answers a question (run a command, try a library call) is context gathering, not the code the HARD-GATE forbids: it is never committed, and what it showed enters the dialogue.

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
| very-small | none: a lane note | none: the note's change list | none | inline where overdetermined |

Each choice is made where its information exists: the preset here; per-task review in the plan, where a task may carry `Review: branch only` (`crucible:writing-plans` § Per-task structure — four fields, all required); execution per task (`crucible:subagent-driven-development` § Inline mode, and on the very-small lane its reference). A campaign's width, its seats and rounds, is set at the campaign gate and by the stop rule (`crucible:redteaming` § Stop rule and terminal pass).

**Unsupported**, each for its reason: per-task review with no plan (there are no tasks); a plan phase without a separate plan (the spec campaign reviews a folded one); a campaign on a lane note, or a spec with no campaign (a feature's spec is always campaigned, a note never is; an umbrella approved without a campaign is a spec of its own kind); a lane note with a plan, or a spec with no plan (work that needs a plan takes a campaign preset, and a campaigned spec is planned); any arrangement without the branch review (it is the one review every arrangement keeps).

**Choose the preset by the overturn question** (`skills/subagent-driven-development/references/seat-rules.md` § The arrangement questions): where overturning a major mechanism after code is reasonably expected, the feature takes a spec campaign; where it is not, for one of that section's two usual cases or another stated reason, it takes none where one implementer can carry it. Between the campaign presets, folded fits a plan of one or two tasks with no seam worth its own review, and standard fits the rest. Width is no test of risk, since the branch review reads the whole diff whatever its width, but it shapes the arrangement where work needs coordinating: a settled change one implementer can carry takes the very-small preset, implemented inline only where `crucible:subagent-driven-development` § Inline mode's test holds, its implementer dispatched otherwise; a settled change that needs several coordinated tasks needs a plan, which only the campaign presets carry, so it takes standard, whose campaign can be expected to stop after its first round, the stop still the stop rule's call. File and line counts are not the test and are not offered as one. An umbrella's review is chosen by its content instead (§ Umbrellas — an effort that takes several features): it has no code of its own to review after.

**The proposal.** As you close the design presentation, propose a preset: name it, give the overturn answer with its reason and, for folded, the plan-size reason; recommend one and let the operator rule, presenting a close call as one. The operator confirms the preset. Per-task review is the plan's, reported at the close of the phase that reviews the plan, and execution is chosen per task, so a departure you expect only later ("most tasks will likely be branch review only") is a heads-up, not something to confirm. The preset is never yours to declare.

**Record the operator's answer as the route entry in the brainstorm decision record** (§ Workspace provisioning (brainstorm exit)), whatever the preset. It is how the confirmation reaches the workspace and, from there, the campaign or the lane: a fold or a lane with no entry is one nobody downstream can see, and reads as unconfirmed. There is no entry mid-flight: a feature past this step keeps its preset, an unfold and a late split (`skills/redteaming/references/flip-paths.md`) aside, and the lane's upgrade hatch (`skills/subagent-driven-development/references/very-small-lane.md`), whose answer to move is recorded as a route entry in the same record; folding a design whose spec is written is a supersede.

What stays route-specific:

- **Folded.** One combined spec+plan document, written at step 5; `crucible:redteaming` § The folded lane carries the campaign, deferral, exit and unfolding rules.
- **Very-small.** Draft the lane note (§ The very-small lane — the lane note (step 5)) and run the self-review on the draft before proposing, and show it with the proposal: the operator's one answer confirms or vetoes the preset and approves or amends the note, and the file is written only after it; a veto discards the draft. What runs is carried by `crucible:subagent-driven-development § The very-small lane`. It has no campaign gate: the answer here is its gate.

### Umbrellas — an effort that takes several features

Where the sub-features of an effort share decisions, an order, or both, an umbrella (`<feature-folder>/umbrella.md`) holds it, proposed at this step with its review: a spec campaign, or the operator's approval. **Before proposing or writing an umbrella, brainstorming a child of one, or resuming an effort one holds, read `skills/brainstorming/references/umbrellas.md` in full, and re-read it after compaction; it binds as if written here.**

## Spec contract

**Verification happens at the moment of writing.** A sentence claiming something about existing code, files, or tool behavior is checked as it is written — read the file, run the command — never left for a sweep afterwards; what cannot be checked now is written with `UNVERIFIED` on it rather than asserted. Treat every unverified claim in a draft as wrong until checked: a checked sentence beats a fast one.

Audience: the agent fleet. The spec quotes no message from the operator: the Intent states the goal in its own words, and the messages that asked for the work go to the workspace's request file (§ Workspace provisioning (brainstorm exit)). Sections, in order:

- **Intent** — problem, goals, non-goals.
- **Decisions** — each with rationale. A decision is lightly held — downstream may flip it with a logged rationale — unless firm. A firm one, recorded `firm` (§ Workspace provisioning (brainstorm exit)), says in its rationale that it is the operator's firm preference.
- **Constraints & invariants** — binding by construction: invariants every task must keep, not a requirement one site meets. Every downstream agent reads it here, in the spec at its pinned revision.
- **Interfaces & boundaries**.
- **Acceptance** — observable outcomes; each maps to a standing test or a one-time check (`crucible:writing-plans` § Acceptance maps to checks), or states why neither.
- **Mechanism sketches** — advisory; implementers and planners may replace them.

**What binds** in a spec, how binding text is read, and how it changes from the spec campaign's close: the opening of `skills/redteaming/references/flip-paths.md` § Flip paths — scoped amendment and supersede.

No code beyond illustrative fragments in advisory sections. Mechanism detail creeping into binding sections is a campaign finding — keep binding sections at intent altitude. **Persistence: the spec is `<feature-folder>/design.md`, in the feature's *feature folder*, by default `docs/crucible/<YYYY-MM-DD>-<feature-slug>/`** — the folder layout and the role names (`<feature-folder>/folded.md` and `<feature-folder>/note.md` on the two small routes) are defined in `skills/redteaming/references/formats.md` § Feature folder; read them there. A child of an umbrella carries the umbrella line in its preamble, on every route (`skills/brainstorming/references/umbrellas.md`). Write it in the **feature worktree**, established before the first write with `crucible:using-git-worktrees` Steps 0–1 on a branch named for `<feature-slug>` (its setup and baseline steps wait for SDD Setup), this feature's own even inside another feature's worktree: the spec, the workspace and the records all live there. The **first** spec write creates the folder by the **birth step** of `skills/redteaming/references/formats.md` § Feature folder; every later write — a resumed brainstorm, an amendment at the campaign gate, the hatch's spec — finds it by the **resolve step**.

`<feature-slug>` names the branch, the folder and the workspace step 7 provisions, so it is chosen before the worktree. Commit the spec on the feature branch (worktree agents can't read gitignored files). A shipped spec is never silently edited.

**Deferral device.** Detail an implementer at the code will judge better is deferred, not pinned: mark it `Deferred to implementation: <what>` on its own line or bullet, in the section that owns it. What is never deferrable, and how the plan gives each marker an owning task, is `crucible:writing-plans` § Deferring detail; until the plan names it, a deferred item is owner-pending, the only stage at which it may be unowned. How the campaign reviews a deferral is `crucible:redteaming` § Merge and finding hygiene.

### The folded lane — the combined spec+plan document (step 5)

Where the operator confirmed the fold at step 4, this step writes one combined spec+plan document in place of a spec. **Before writing it, read `skills/brainstorming/references/folded-lane-document.md` in full, and re-read it after compaction; it binds as if written here.**

### The very-small lane — the lane note (step 5)

On the very-small lane the lane note takes the spec's place. **Before drafting it, read `skills/brainstorming/references/lane-note.md` in full, and re-read it after compaction; it binds as if written here.**

## Spec self-review

After writing, re-read with fresh eyes:

1. **Placeholder scan:** any "TBD", "TODO", incomplete sections, vague requirements? Fix them. An explicit `Deferred to implementation:` marker is exempt — it is a recorded decision about who decides, not an unfinished sentence.
2. **Internal consistency:** do sections contradict each other? Does the architecture match the feature descriptions?
3. **Scope check:** focused enough for a single implementation plan, or does it need decomposition? Parts that share decisions, an order, or both take an umbrella (§ Umbrellas — an effort that takes several features).
4. **Ambiguity check:** could any requirement be read two ways? Pick one and make it explicit — unless it carries a `Deferred to implementation:` marker, where picking is the implementer's job and the marker is what makes that explicit.
5. **Evidence check:** every claim the spec makes about existing code, files, or tool behavior was verified when written — you read or ran the thing — or carries `UNVERIFIED`. Resolve the tags now, or leave them standing as declared input for the campaign. Then the **consumer sweep**: for each symbol, file, or interface the design changes, deletes, or constrains, enumerate its existing consumers mechanically — by search, not from memory — and account for each one in the design. A rule stated in more than one place — docs, prompts, templates — is such an interface: its consumers are every site that states it, found by searching its key terms. Then the **trace**: for each rule the design ties to a trigger ("at each X, do Y"), name every route and phase that must reach the rule — the standard route, the folded lane, the very-small lane, an umbrella; brainstorm, spec campaign, plan phase, execution, branch review, finish — and the moment X occurs in each; where X occurs and nothing reaches the rule, the design has a gap.

Fix inline; no re-review loop — fix and move on.

## Workspace provisioning (brainstorm exit)

One workspace per feature, provisioned now by the provisioning step of `skills/redteaming/references/formats.md` § Feature workspace root and layout, living until an end its Lifecycle names — campaigns and SDD store their records in its subdirectories, laid out as that file defines. Then write the **brainstorm dialogue's decision record** to `<workspace>/brainstorm-decisions.md` — one entry per decision made in the dialogue: the decision, its rationale, and its status with its proposer, the operator or the controller (`accepted — proposed by the controller`). Statuses: `open`; `accepted`, the default for any approval ("+", "OK" and "your call" included), meaning "this until new evidence arrives"; `firm`, only on the operator's explicit word, never inferred from an approval. An answer that leaves the call to you ("your call") is recorded `accepted — delegated to the controller`, in the proposer's place, never as the operator's ruling or choice. A route entry, written for every preset (§ Proposing the arrangement (step 4)), confirms its preset only when `accepted` or `firm`. Later operator rulings enter this record too (`skills/redteaming/references/formats.md` § Feature workspace root and layout).

Then write the **request** to `<workspace>/request.md`: the message that asked for the work, and each later message that changed what was asked, quoted verbatim; a message you are unsure changed it is included. A child of an umbrella quotes only the messages of its own brainstorm. It is evidence of what was asked, not the standard, and seats check the Intent against it (`skills/subagent-driven-development/references/seat-rules.md` § The goal check); it lives and is deleted with the workspace, which is never committed, so nothing in it is redacted. Later messages that change what was asked are appended to it (`skills/redteaming/references/formats.md` § Feature workspace root and layout).

## Campaign gate

The operator reviews the **decision record's decisions, its open decision asks and the planned campaign shape**, presented inline; the gate never requires reading the spec file, and shows whatever part of it the operator asks for. The open asks stand apart, as `crucible:redteaming` § Round readout states. The campaign shape is its seats with their lenses and models, and its expected rounds, sized per `crucible:redteaming` § Panels: approving the design approves the launch. Record the approved shape as one gate entry in the decision record; the campaign-start readout names any departure from it.

Wait for the operator. Changes requested → amend the spec, re-run the self-review, update the decision record, re-gate. Approved → hand off.

## Handoff

Invoke `crucible:redteaming` to run the spec campaign; its records live under `<workspace>/campaigns/spec/`. **The campaign is this skill's terminal state.** Do not invoke any planning or implementation skill from here — after the campaign converges, its own close readout names the next handoff (`crucible:redteaming` § Exit).

**On the very-small lane the handoff is to SDD instead:** invoke `crucible:subagent-driven-development § The very-small lane`, with the committed lane note and the decision record's lane entry as its inputs. That section, not the campaign, is this skill's terminal state on the lane — the one implementation handoff this skill makes, licensed by the operator's confirmation at step 4 and by nothing else.

**An umbrella's handoff follows its review.** A campaigned umbrella hands off to `crucible:redteaming` as above, and the campaign's close leads to its landing. An umbrella the operator approved without a campaign has its landing as this skill's terminal state: the steps `skills/brainstorming/references/umbrellas.md` states, then `crucible:finishing-a-development-branch`. Neither invokes a planning or implementation skill; its children write the plans.
