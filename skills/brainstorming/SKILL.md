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
4. **Present the design in sections** — approval per section; where the change is small, a small lane's entry (the operator confirms or vetoes it here); where the effort takes several features, an umbrella and its review
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

### The folded lane — proposing the fold (step 4)

A small change may **fold its plan into its spec**: one combined spec+plan document, and no plan phase at all. The spec campaign is not lightened for it — `crucible:redteaming § The folded lane` carries the campaign, deferral, exit and unfolding rules for that route. What lives here is the entry, and the entry lives nowhere else.

**Propose the fold at this step, before any artifact is written; the operator confirms or vetoes it here.** Where the design looks small, say so as you close the design presentation: name the fold, give the qualifying rationale, and wait for the ruling. There is no mid-campaign entry and no retroactive fold — a design whose spec is already written is on the standard route, and folding it later is a supersede, not a decision you make in passing.

**Record the operator's answer as an entry in the brainstorm decision record** (§ Workspace provisioning (brainstorm exit)) — the decision, its rationale, settled. That entry is how the confirmation reaches the workspace at provisioning and, from there, the campaign: a fold with no entry in the record is a fold nobody downstream can see, and the campaign reads it as unconfirmed.

**Qualifying shape — advisory, and judgment rather than thresholds:** no new mechanism, no cross-subsystem blast radius, no change to [LOAD-BEARING] content. File counts, line counts and similar mechanical proxies are not the test and are not offered to the operator as one. Where it is a close call, present it as one and let the operator rule.

**A folded feature is a minor design by construction.** It carries no digest, so the digest step is skipped and the digest gate presents the decision record's decisions and open asks inline — the existing minor-design path, unchanged.

### The very-small lane — proposing the lane (step 4)

A third route, alongside the standard route and the folded lane, for a small change with **no design decision worth reviewing before code** — where the diff is the best review object. Its only artifact is a lane note; it runs no spec campaign, no plan and no per-task review. What it does run — inline implementation, the repo's verification gates, the branch-review loop with its fix waves applied inline by the controller, and SDD Finish — is carried by `crucible:subagent-driven-development § The very-small lane`. The entry lives here and nowhere else.

**Entry is the operator's confirmation at this step, and nothing else.** Where the change looks this small, draft the lane note (§ The very-small lane — the lane note (step 5)) and run the self-review on the draft. Then, as you close the design presentation, propose the lane with its qualifying rationale and show the draft in the same message: the operator's one answer confirms or vetoes the lane and approves or amends the note, and the file is written only after it. A veto discards the draft. You never declare the lane yourself, and there is no mid-flight entry — a feature past this step stays on the route it took here. Record the answer in the brainstorm decision record, exactly as for the fold: a lane with no entry in the record is a lane nobody downstream can see.

**Qualifying shape — the folded lane's, judged the same way:** no new mechanism, no cross-subsystem blast radius, no change to [LOAD-BEARING] content; judgment, not thresholds. **What separates the two small routes** is whether the change carries a design decision worth reviewing before code: the folded lane fits a small change that does, the very-small lane one that does not. Recommend one — or the standard route — and let the operator rule.

**A very-small-lane feature is a minor design by construction:** no digest, and no digest gate — the operator's answer at this step is its gate.

### Umbrellas — an effort that takes several features

Where the sub-features of an effort share decisions, an order, or both, an umbrella (`<feature-folder>/umbrella.md`) holds it, proposed at this step with its review: a spec campaign, or the operator's approval. **Before proposing or writing an umbrella, brainstorming a child of one, or resuming an effort one holds, read `skills/brainstorming/references/umbrellas.md` in full, and re-read it after compaction; it binds as if written here.**

## Spec contract

**Verification happens at the moment of writing.** A sentence claiming something about existing code, files, or tool behavior is checked as it is written — read the file, run the command — never left for a sweep afterwards; what cannot be checked now is written with `UNVERIFIED` on it rather than asserted. Treat every unverified claim in a draft as wrong until checked: a checked sentence beats a fast one.

Audience: the agent fleet. Sections, in order:

- **Intent** — problem, goals, non-goals.
- **Decisions** — each with rationale. Decision-weight convention: a **[LOAD-BEARING]** mark binds exactly the sentence or bullet it annotates — that decision holds or forces a supersede/scoped-amendment event; everything unmarked is lightly-held (downstream may flip it with a logged rationale).
- **Constraints & invariants** — load-bearing by construction; the section label is the mark. Every downstream agent reads it here, in the spec at its pinned revision; plans point at it and never copy it.
- **Interfaces & boundaries**.
- **Acceptance** — observable outcomes; each maps to a **standing test**, where a later change could plausibly break it, or to a **one-time check**, run once and recorded as its command and quoted output; or states why neither. An absence criterion ("X is gone") is one-time unless a named later change could undo it.
- **Mechanism sketches** — advisory; implementers and planners may replace them.

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
5. **Evidence check:** every claim the spec makes about existing code, files, or tool behavior was verified when written — you read or ran the thing — or carries `UNVERIFIED`. Resolve the tags now, or leave them standing as declared input for the campaign. Then the **consumer sweep**: for each symbol, file, or interface the design changes, deletes, or constrains, enumerate its existing consumers mechanically — by search, not from memory — and account for each one in the design. A rule stated in more than one place — docs, prompts, templates — is such an interface: its consumers are every site that states it, found by searching its key terms. An unenumerated consumer and an unchecked claim are the two largest measured finding classes; both are cheaper to catch here than to buy a campaign dispatch for.

Fix inline; no re-review loop — fix and move on.

## Workspace provisioning (brainstorm exit)

One workspace per feature, provisioned now by the provisioning step of `skills/redteaming/references/formats.md` § Feature workspace root and layout, living until an end its Lifecycle names — campaigns and SDD store their records in its subdirectories, laid out as that file defines. Then write the **brainstorm dialogue's decision record** to `<workspace>/brainstorm-decisions.md` — one entry per decision made in the dialogue: the decision, rationale, status (settled/open). This record is the digest's first derivation source and must exist on disk before the digest does.

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
