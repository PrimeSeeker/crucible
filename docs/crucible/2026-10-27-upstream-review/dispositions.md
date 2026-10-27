# Upstream review, v6.2.0 → v7.0.1: dispositions

superpowers' changes from v6.2.0 to v7.0.1 (five releases, 146 files), read
against crucible at 6fd3b2d by four readers, one per area and a second,
independent reader of the execution area on another model family. Each
change got one disposition: **adopt** (take it close to upstream's form),
**adapt** (the problem exists here; take the idea in crucible's form),
**covered** (crucible already handles it), **decline** (with the reason),
**out of scope** (other hosts, upstream's own branding and tooling).

The maintainer ruled on 2026-10-27: the recommendations below stand, except
where a row says otherwise. **Lane A** is this feature's note; **lane B**
is the next lane; **backlog** names the item that holds it.

Where the two execution readers disagreed, the row gives the one the
controller confirmed against the files.

## Defects crucible carried (lane A)

| upstream change | disposition |
|---|---|
| `find-polluter.sh` run through `bash`, since packagers strip the exec bit (v6.4.1, #2301) | adopt: crucible's copy was committed without the exec bit, and its `./` form resolved against the user's project |
| `root-cause-tracing.md`'s two diagrams disagree on a dead end (unchanged at v7.0.1) | adapt: a dead end goes to instrumentation, then to `SKILL.md`'s "No Root Cause" |
| hooks read files with bash builtins, no `cat` or `dirname` from `PATH` (v7.0.0, #2310) | adapt: crucible's hook read with `cat`; with `PATH` empty, a `cat` in the working directory ran |
| `hooks.json` and the Windows launcher avoid a `bash` lookup on `PATH` | adapt, docs only: no form avoids the lookup on every host, so `hooks/README.md` states it |
| `CLAUDE.md` removed: Claude Code reads `AGENTS.md` where no `CLAUDE.md` exists (v2.1.277) | adapt: the Claude Code host map named only `CLAUDE.md` |
| `codex-tools.md`: a full-history fork accepts model and effort overrides (source reading) | adapt: crucible's dispatch reference said the opposite, unmeasured; removed, since crucible never forks with history |
| `review-package` rejects a range whose head does not descend from its base (v6.4.1) | adapt: the four diff-building seats check ancestry |

## Improvements (lane B)

| upstream change | disposition |
|---|---|
| the code reviewer: a spec's silence is not permission; grade a failure by its effect on a reasonable user (v6.4.1) | adapt: the branch and task reviewers |
| writing-plans' Review Focus: inputs the spec implies but never names (v7.0.1) | adapt: the plan's edge and error scenarios name them |
| TDD: the project's suite defines green; report every failure by name, yours or not (v6.4.1) | adapt: the implementer's report |
| the final message lists every ruling the controller made | adapt: the close readout lists the controller's own rulings, pre-flight and plan patches included; the cost-if-wrong field declined |
| brainstorming: record which choices the person made and which the agent made (v7.0.0) | declined by the maintainer: a "decided by the operator" mark invites deference. In its place, the redteam seats' mandate: a consequential choice a spec takes for granted with no Decision entry (platform, language, the form of the deliverable) is a finding |
| brainstorming's spike: a throwaway build on the person's yes | adapt, narrower: a throwaway probe in scratch that answers a question is context gathering, never committed |
| verification-before-completion: on an agent's success report, check its diff | adapt: dispatching-parallel-agents checks each agent's diff, not its summary |
| writing-skills: run bundled scripts through their interpreter | adapt: its Portability bullet |
| the task reviewer re-reads evidence that looks truncated before reporting a gap | adapt: task reviewer and re-reviewer |

## Routed elsewhere

| upstream change | disposition |
|---|---|
| SDD's always-run sections moved into references, read at their step; a 20,000-character `SKILL.md` ceiling (v7.0.1, #2565) | adapt, backlog `skill-size-after-compaction.md`: crucible's redteaming and SDD `SKILL.md` are past it; the authoring rule sends only route-conditional text to references and has to widen |
| `codex-tools.md`: wait in long stretches, never short-poll, reconcile live children | adapt after measuring, backlog `codex-wait-cadence.md` |
| an opt-in nested SDD controller one subagent down, on a mid-tier model (v6.4.1) | decline now; backlog `nested-orchestration.md`. A nested controller cannot put a decision ask to the operator mid-run |

## Declined

| upstream change | reason |
|---|---|
| the controller rules on a load-bearing finding at the cap and carries on | `docs/decisions/task-loop.md` and `docs/decisions/branch-review.md` stop there; the maintainer noted that crucible may mark too much as load-bearing: backlog `load-bearing-marks-audit.md` |
| Native inline execution: no per-task review, one final review | `docs/decisions/task-loop.md`; the very-small lane already runs that shape. The maintainer: not extended for now |
| executing-plans' `task-start` and `task-done` scripts | crucible's plans have no step scripts, and completion follows review |
| the final review's single fix wave, its fixes verified by tests alone | `docs/decisions/branch-review.md` |
| execution without subagents, the final review as self-review | `docs/decisions/task-loop.md` § Rejected |
| a pre-flight table of task pairs sharing a seam | the plan phase's pre-pass already checks ownership and overlap |
| batching small tasks at execution | covered: tasks are sized at plan time |
| a "declined to judge" list from reviewers | a new ruling class for the controller; the spec-silence rule takes its root cause |
| the executor re-grades the reviewer's severities | contested findings go to the adjudicator |
| brainstorming for any creative work, beyond software | crucible's brainstorm produces a spec for an agent fleet |
| open questions over multiple choice | `docs/decisions/brainstorming-first.md` keeps multiple choice |
| offering "just dive in" when brainstorming started on its own | `docs/decisions/routes.md`: no agent-declared route; the operator can skip |
| the builder-check prompt in place of the spec reviewer | covered by the spec campaign |
| diagnosing-superpowers: a post-mortem of session transcripts, issue filing, scrubbed bundles | triage for upstream's issue tracker; crucible's audits are the maintainer's |
| `emit_json` piped through `cat` to absorb a Git Bash EPIPE | it hides a failed write, which crucible's hook reports |
| the Windows launcher's fixes (per-user Git, WSL launchers, exit code) | crucible has no launcher |
| fix-wave reports quote the reproducing test's red run | the re-reviewer already requires the defect gone |
| `.pre-commit-config.yaml`, `scripts/lint-shell.sh`, `tests/shell-lint/` | the config lints no shell (it runs ruff and ty on `evals/`); the lint needs ShellCheck, wired to nothing upstream; the hook is behavior-tested on every failure path |
| `tests/systematic-debugging/` | the script is upstream's blob, its pattern fix included; the script is advisory |
| verification-before-completion's Common Failures table | covered: the router's evidence line, the implementer's quoted run, the task reviewer's verdicts, SDD Finish, and (lane B) the parallel-agents diff check |

## Covered or out of scope, in short

Covered: continuous execution and its stop set; spec pointers in plans;
the no-delegation line in every seat template; merge-base review ranges;
workspace collisions and `.gitignore` preservation; worktree removal never
forced; lean plans; `fork_turns: "none"`; resuming a fix-wave implementer;
no close-agent tool; per-version model lists; the effort backstop (taken
before this review); look before you ask; play back in chunks; size the
work at the design step; a design approved before building; secrets not
printed; writing-skills' slimming (crucible's form is leaner).

Out of scope: Hermes, Muse, Devin, Antigravity and OpenCode support;
upstream's release tooling, contribution templates, README, Code of
Conduct and logo; the visual companion's server (backlog
`visual-companion.md`); upstream's specs, plans and eval lab.
