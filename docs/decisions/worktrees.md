# Worktrees

## Decision

**Worktree first, on the operator's request.** Brainstorming establishes
the feature worktree before its first durable write, with
`crucible:using-git-worktrees` Steps 0–1, on a branch named for the
feature's slug, and names the worktree, with its base where the git
fallback sets one, in the message that closes its design presentation
(`crucible:brainstorming § The dialogue`). The operator's approval of
that message, or a worktree preference declared in the instruction
files, is the explicit request worktree creation needs; where neither
exists, the skill names the worktree and its base in one line and asks.
Work happens in place only where the instructions or the operator say so
(`crucible:using-git-worktrees § Step 0: Detect Existing Isolation`).

**Native tool or git fallback.** The host's own worktree tool is
preferred. The git fallback runs where there is none, where brainstorming
starts a feature inside another feature's linked worktree, or where the
instruction files declare a worktree directory, since the native tools
the skill knows of take no base or directory. From another feature's
worktree, the new worktree is cut from the repository's base branch or a
base the operator names, in the main checkout's worktree directory, and
a worktree directory found not ignored there is reported to the operator,
never fixed by a commit.

**Native tools named in a shared skill.** Step 1a lists what a native
worktree tool may be called, `EnterWorktree` among them, and the
rationalization table uses it as its example. It is an exception to
`AGENTS.md`'s rule that host tool names live only in the adapter pair;
the claude-ism scanner has no term for it.

**The fallback's checks.** The ignore check runs against the directory
actually selected, with its trailing slash:
`git -C <project-root> check-ignore -q <worktree-dir>/`. A directory not
ignored is added to `.gitignore` and committed, and the same directory
is checked again. `git worktree add -b` refusing a branch name that already
exists is the answer: the agent picks a fresh name or checks out the
existing branch deliberately, never forcing past it
(`crucible:using-git-worktrees § 1b. Git Worktree Fallback`).

**Setup and baseline at SDD Setup.** Brainstorming runs Steps 0–1 only.
SDD Setup runs the worktree skill's Steps 2–3, project setup and the
clean baseline, in the checkout it works from, unless that skill just
ran them creating the worktree there, and records
`Baseline: <result> at <sha7>` in the ledger; a resumed controller that
finds the line skips both (`crucible:subagent-driven-development
§ Setup`).

## Why

### Worktree first

Before 2026-10-07 brainstorming wrote where it started: a user who began
on the main branch got the spec, the review commits and the workspace
there. Establishing the worktree before the first durable write keeps
all three on the feature branch. (Basis: judgment, accepted by the
maintainer, 2026-10-07.)

That change made a worktree the default with no question asked. On
Claude Code the native tool, `EnterWorktree`, says of itself (checked
2026-10-20): "Never use this tool unless 'worktree' is explicitly
mentioned by the user or in CLAUDE.md / memory instructions." Upstream's
design note, "Worktree Rototill: Detect-and-Defer", answers that by
framing the user's consent as the authorization the tool requires, and
reports that this consent bridge, naming the native tools explicitly and
a red-flag line together took its tests of the step from 2/6 passes to
50/50 (`superpowers/docs/superpowers/specs/2026-04-06-worktree-rototill-design.md`).
The bridge had gone out with the consent question, unrecorded, and came
back on 2026-10-12 through the approved design message, so the operator
is not asked twice. Its effect on today's tool text is unmeasured, and
use gives no evidence either: crucible's own repository declares
`.worktrees/`, which sends every creation to the git fallback. A
repository that declares a worktree directory but no preference now gets
a one-line ask where it used to get a worktree by default. (Basis:
external; judgment, accepted by the maintainer.)

### The git fallback

A linked worktree that belongs to another feature is not this one's, and
a new feature started there needs its own base. `EnterWorktree` takes a
name or a path, places a new worktree under `.claude/worktrees/` and
takes its base from a setting (checked 2026-10-20), so it cannot be given
either. From another feature's worktree the project root resolves to the
main checkout, and committing an ignore fix there would land on whatever
branch the main checkout has out; reporting instead leaves that to the
operator (2026-10-12). From the main checkout itself the fallback still
commits the fix, as upstream does, an accepted residual with finishing's
cleanup of default-named directories only
(`docs/backlog/declared-worktree-directory-residuals.md`). (Basis:
external, for the tool; judgment, accepted by the maintainer.)

### Native tools named

Upstream's design note credits naming the tools with turning "do I have a
native tool?" from interpretation into a lookup in the agent's tool list;
agents given the abstract wording anchored on the fallback's git
commands. Moving the names into the adapters would lose that, so the
pre-move audit kept them in the shared skill, at upstream's two sites, as
a recorded exception. (Basis: external; judgment, accepted by the
maintainer, 2026-10-17.)

### The fallback's checks

Upstream checked `git check-ignore -q .worktrees || git check-ignore -q
worktrees` (`superpowers/skills/using-git-worktrees/SKILL.md`), which
passes when either directory is ignored, whichever one is used, and
queries both without a trailing slash. A `.gitignore` entry written the
usual way, `.worktrees/`, matches directories only, and git knows a path
that does not exist yet is a directory only from the slash: checked on
2026-10-20 with git 2.56.0, against `.worktrees/`, `.worktrees` exits 1,
`.worktrees/` exits 0 and `worktrees/` exits 1. The implementer
rewriting the skill as single invocations fixed both, the slash first
and the selected directory in its fix round, each as a disclosed
departure, and the fixes landed with that feature on 2026-08-15. (Basis: measured; judgment, accepted by the maintainer.)

`git worktree add -b` with an existing branch name fails and creates
nothing (checked on 2026-10-20: "a branch named 'feat' already exists").
Its forcing form, `-B`, resets the existing branch to the start point,
moving it off the commits it held. (Basis: measured.)

### Setup and baseline

Setup and the baseline were left to SDD Setup on 2026-10-07, where
running the suite is worth its cost. The pre-move audit found
that SDD Setup ran them only when it created the worktree itself, so on
the usual path, after brainstorming had made one, no step ran them; on
2026-10-17 the maintainer chose to run them there over dropping the
promise ("Agree with a"). A dirty baseline makes every later failure
ambiguous. On 2026-10-19 the result became a ledger line, since "unless
that skill already ran them" left a resumed controller unable to tell.
(Basis: judgment, accepted by the maintainer.)

## Rejected

- **A worktree by default, with no request**: the native tool's own
  description forbids its use without an explicit mention, and the
  bridge supplies one (§ Why).
- **A separate consent question after the design is approved**: the
  approved message already names the worktree (§ Why).
- **Moving `EnterWorktree` and its siblings out of the shared skill** to
  keep host tool names in the adapters: the names are what lets an agent
  recognise a native tool (§ Why).
- **Setup and the baseline at brainstorming**: the suite run is worth
  its cost at execution, not before (§ Why).

## What a project may change

- Work in place instead of in a worktree, by saying so in its
  instruction files.
- A worktree preference, which stands in for the operator's approval,
  and a worktree directory, which sends creation to the git fallback.
- A worktree mechanism of its own, such as a provisioning script, named
  in its instruction files, which outrank the skill
  (`crucible:using-crucible § The Rule`).

## Changes

- 2026-10-19: setup and the baseline run at SDD Setup in the checkout it
  works from, recorded as a ledger `Baseline:` line that a resumed
  controller skips on.
- 2026-10-17: `EnterWorktree` kept in the shared worktree skill, in Step
  1a's list and the rationalization table, an exception to host tool
  names living in the adapters.
- 2026-10-12: worktree creation: before the first durable write, on the
  slug's branch, on the operator's explicit request through the approved
  design message or a declared preference, else a one-line ask; the git
  fallback for a declared directory or a feature started in another
  feature's worktree, cut from the base branch or a named base in the
  main checkout's worktree directory, reporting a not-ignored directory
  there.
- 2026-08-15: the fallback's ignore check against the selected
  directory with its trailing slash, re-checked after a fix, and
  `worktree add -b`'s refusal of an existing branch name taken as the
  answer.
