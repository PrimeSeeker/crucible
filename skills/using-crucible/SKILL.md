---
name: using-crucible
description: Use when starting any conversation.
---

<SUBAGENT-STOP>
If you were dispatched as a subagent to execute a specific task, ignore this skill.
</SUBAGENT-STOP>

## The Rule

Before acting on a request — clarifying questions and exploration included — check the Skill Index below and invoke every skill whose trigger matches, and any the operator names. The skills carry the process; work started without them usually has to be redone. One exception: for a change you judge trivial, offer the waiver below first. A loaded skill whose trigger turns out not to match is set aside, saying so; one that applies is skipped only on the operator's explicit word.

Then announce "Using [skill] to [purpose]" and follow the skill exactly. If it has a checklist, track a todo per item.

The operator is the human you work with, whom inherited skill text calls "your human partner".

Your instruction files — user-level, project and any other the host loads (your runtime reference names them) — and the operator's direct requests take precedence over skills, which override default behavior; this is how a preference a skill states is overridden.

**Trivial-edit waiver.** For a change you judge trivial — a typo, a comment, wording the operator dictated — you may offer in one line to make it without crucible's process. The operator's yes, a direct request, covers that edit as offered; if the work turns out larger — another file, a behavior change, a second fix — stop and return to the operator. The project's own rules (worktrees, tests) still apply.

**Brainstorm before planning:** before entering the host's planning mode (your runtime reference names it), invoke the brainstorming skill if you haven't already.

**Evidence before claims:** before saying work is complete, fixed or passing, run the check that shows it and report what its output said.

## Skill Priority

When several skills apply, process skills come first: brainstorming before building, systematic-debugging before fixing; implementation and domain skills follow.

## Red Flags

These thoughts usually precede a skipped skill check; make the check instead:

| Thought | Check |
|---|---|
| "This is just a simple question" | Questions are tasks: check the index. |
| "I need more context first" | The check comes before clarifying questions. |
| "Let me explore the codebase first" | Skills say how to explore: check first. |
| "I can check git/files quickly" | Files lack the conversation's context: check first. |
| "Let me gather information first" | Skills say how to gather it: check first. |
| "This doesn't need a formal skill" | If one matches, load it. |
| "I remember this skill" | Skills change: read the current version. |
| "This doesn't count as a task" | Any action is a task: check the index. |
| "The skill is overkill" | A small change has the lanes, a trivial one the waiver: offer one. |
| "I'll just do this one thing first" | Check before doing anything. |
| "This feels productive" | Unrouted action is usually redone: check first. |
| "I know what that means" | Knowing the concept is not using the skill: load it. |

## Runtime reference

Host mechanics are adapter-mediated, never assumed. Your runtime adapter is a pair of files under `skills/using-crucible/references/` from the plugin root. The **host map** (`claude-code.md`, `codex.md`) carries what every session needs and is your runtime reference: your host's is appended below at session start, else read it from there before dispatching or planning. The **dispatch reference** beside it (`claude-code-dispatch.md`, `codex-dispatch.md`) carries what a skill that dispatches seats needs; those skills say when to read it. Where a rule here and a mechanic there seem to conflict, the rule governs.

## Skill Index

- `crucible:using-crucible` — this skill; re-read it after compaction.
- `crucible:brainstorming` — before any feature work or behavior change.
- `crucible:writing-plans` — when a spec has closed its redteam campaign and needs a plan.
- `crucible:subagent-driven-development` — when executing a plan or a very-small-lane note.
- `crucible:redteaming` — on a just-written spec or plan, before accepting it.
- `crucible:requesting-code-review` — when a branch's tasks are complete or before merging.
- `crucible:receiving-review` — when review feedback arrives from outside crucible's review loops, before acting on it.
- `crucible:dispatching-parallel-agents` — for 2+ independent tasks with no shared state.
- `crucible:systematic-debugging` — on any bug, test failure or unexpected behavior, before proposing fixes.
- `crucible:using-git-worktrees` — before feature work or plan execution that needs isolation.
- `crucible:finishing-a-development-branch` — when tested work needs integration.
- `crucible:writing-skills` — when creating, editing or verifying skills or other text that instructs agents.
