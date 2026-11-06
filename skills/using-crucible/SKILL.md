---
name: using-crucible
description: Use when starting any conversation.
---

<SUBAGENT-STOP>Dispatched as a subagent for a specific task? Ignore this skill.</SUBAGENT-STOP>

## The Rule

Before acting on a request, clarifying questions and exploration included, check the Skill Index and invoke every skill whose trigger matches, and any the operator names. One exception: for a trivial change, offer the waiver first. A loaded skill whose trigger turns out not to match is set aside, saying so; one that applies is skipped only on the operator's explicit word.

Then announce "Using [skill] to [purpose]", follow the skill exactly, and track a todo per checklist item.

The operator is the human you work with, whom inherited skill text calls "your human partner".

Your instruction files (user-level, project and any other the host loads) and the operator's direct requests outrank skills, which outrank default behavior.

If another process router (a skill that, like this one, decides which workflow a session follows) also reached this session at its start, stop before acting and ask the operator to turn one off and start a new session: two routers fight over the session.

**Trivial-edit waiver.** For a change you judge trivial (a typo, a comment, wording the operator dictated), you may offer in one line to make it without crucible's process. The operator's yes, a direct request, covers that edit as offered; if the work grows (another file, a behavior change, a second fix), stop and return to the operator. The project's own rules (worktrees, tests) still apply.

Before entering the host's planning mode, invoke brainstorming if you haven't.

Before claiming work is complete, fixed or passing, run the check that shows it and report what its output said.

Dispatching any agent: name its model (an omitted model silently inherits the session's), and never predict or paraphrase its result before it returns.

**A fresh look.** At any phase, where the design or code seems overfitted, fragile, finicky, jagged, inelegant or otherwise wrong, or the operator asks for one, read `skills/subagent-driven-development/references/fresh-look.md` and dispatch its seat before going on. Signs include a second patch to one passage, a fix that adds a special case, a rule you cannot state without its exceptions, and a seat saying so.

After compaction, re-invoke any skill you are still working under that came back cut short (ending in a truncation notice) or did not come back, before acting on it.

## Decision asks

A decision ask puts a choice to the operator in analyst language with your recommendation and the strongest case against it: it never requires reading the spec, plan, code or a diff, may quote the few lines it turns on, lists every option its findings propose, and states what its change withdraws from an earlier operator approval. Where a message to the operator carries anything else, its decision asks come last, in a block of their own.

## Skill Priority

When several skills apply, process skills come first: brainstorming before building, systematic-debugging before fixing; implementation and domain skills follow.

## Red Flags

These thoughts usually precede a skipped check; check instead:

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
| "The skill is overkill" | Brainstorming offers lighter arrangements, a trivial change the waiver: offer one. |
| "I'll just do this one thing first" | Check before doing anything. |
| "This feels productive" | Unrouted action is usually redone: check first. |
| "I know what that means" | Knowing the concept is not using the skill: load it. |

## Runtime reference

Host mechanics come from your runtime adapter, a pair of files under `skills/using-crucible/references/` from the plugin root; never assume them. The **host map** (`claude-code.md`, `codex.md`), your runtime reference, carries what every session needs: your host's is appended below at session start, else read it there before dispatching or planning. The **dispatch reference** (`claude-code-dispatch.md`, `codex-dispatch.md`) carries what seat-dispatching skills need; they say when to read it. Where a rule here and a mechanic there seem to conflict, the rule governs.

## Skill Index

- `crucible:using-crucible` — this skill; re-read it after compaction.
- `crucible:brainstorming` — before any feature work or behavior change.
- `crucible:writing-plans` — when a spec has closed its redteam campaign and needs a plan.
- `crucible:subagent-driven-development` — when executing a plan or a very-small-lane note.
- `crucible:redteaming` — on a just-written spec or plan, before accepting it.
- `crucible:requesting-code-review` — when a branch's tasks are complete or before merging.
- `crucible:receiving-review` — when review feedback arrives from outside crucible's review loops, before acting on it.
- `crucible:dispatching-parallel-agents` — for 2+ independent tasks with no shared state, outside crucible's own seat dispatches.
- `crucible:systematic-debugging` — on any bug, test failure or unexpected behavior, before proposing fixes.
- `crucible:using-git-worktrees` — before feature work or plan execution that needs isolation.
- `crucible:finishing-a-development-branch` — when tested work needs integration.
- `crucible:writing-skills` — when creating, editing, checking or compacting skills or other text that instructs agents.
