# The upstream map

Crucible is forked from [superpowers](https://github.com/obra/superpowers)
and owned outright (`docs/decisions/fork-and-own.md`). This map says where
upstream's files went: the skills renamed or folded, the files not carried
with the reason for each, and the drops not yet decided. A file that maps
one to one, kept or rewritten in place under the same role, has no row.

Upstream paths carry the prefix `superpowers/` and name files at the last
fully reviewed version.

## Base and review state

- **Fork base:** v6.2.0, tag commit `3dcbd5c`.
- **Last fully reviewed version:** v6.2.0.
- **Taken from later releases without a full review:** v6.3.0's Codex
  spawn effort fix (upstream pull requests #2060 to #2062). Upstream pins
  `model` and `reasoning_effort` on every spawn, with
  `[agents] default_subagent_reasoning_effort` as a backstop; crucible
  takes the backstop as the mechanism instead. Its dispatches leave
  effort unset, the user's Codex config sets the key (`docs/codex.md`
  § Install), and the controller says so once when the key is absent
  (`skills/using-crucible/references/codex-dispatch.md`). The rest of
  v6.3.0 and every later release are unreviewed:
  `docs/backlog/upstream-sync-review.md`.

## Upkeep

Each upstream release is reviewed as a diff from the last fully reviewed
version. A completed review advances that version, and rows change only
where a disposition does. A piece taken from a later release on its own
is listed above, apart from the reviewed version, because the rest of that
release was not reviewed.

A row's reason is one recorded when the file was dropped or one the
maintainer confirmed. A drop with neither is listed as not carried,
decision pending, with the backlog item that decides it.

## Renamed or folded

| upstream | in crucible |
|---|---|
| `superpowers/skills/using-superpowers/` | `skills/using-crucible/`, rewritten; its `superpowers/skills/using-superpowers/references/codex-tools.md` became `skills/using-crucible/references/codex.md` and `skills/using-crucible/references/codex-dispatch.md` |
| `superpowers/skills/receiving-code-review/` | `skills/receiving-review/`, a new skill keeping upstream's core |
| `superpowers/skills/executing-plans/` | `crucible:subagent-driven-development § Inline mode` |
| `superpowers/skills/test-driven-development/SKILL.md` | the implementer and task-reviewer prompts (`skills/subagent-driven-development/implementer-prompt.md`, `skills/subagent-driven-development/task-reviewer-prompt.md`) |
| `superpowers/skills/test-driven-development/writing-good-tests.md` | `skills/subagent-driven-development/writing-good-tests.md` |
| `superpowers/skills/verification-before-completion/` | the router's evidence line (`skills/using-crucible/SKILL.md`), the implementer's quoted-run rule, and the full suite run in `crucible:subagent-driven-development § Finish` |
| `superpowers/skills/subagent-driven-development/scripts/sdd-workspace` | the workspace provisioning step in `skills/redteaming/references/formats.md` |

## Not carried

| upstream | where it went | reason |
|---|---|---|
| executing-plans' fallback for a host without subagents (`superpowers/skills/executing-plans/SKILL.md`) | — | Both supported hosts dispatch subagents, and crucible's review gates need a fresh reviewer seat that a host without them cannot supply. |
| verification-before-completion as a skill (`superpowers/skills/verification-before-completion/SKILL.md`) | the router's evidence line, the implementer's quoted-run rule, SDD Finish's suite run | One always-loaded line instead of a skill that has to trigger; each seat states its own checks. |
| test-driven-development's red-green-refactor walkthrough and its "every new function has a test" checklist (`superpowers/skills/test-driven-development/SKILL.md`) | the implementer and task-reviewer prompts | Review checks RED before GREEN, not a coverage checklist, and whether new tests are adequate is the reviewer's judgment. |
| process diagrams (brainstorming, subagent-driven-development) and worked examples (SDD's Example Workflow, requesting-code-review's example, the code reviewer's Example Output) | numbered steps | Every session that loads the skill reads them, and they drew upstream's flow, which the rewrite changed. |
| the reviewers' praise and Strengths sections (`superpowers/skills/requesting-code-review/code-reviewer.md`, `superpowers/skills/subagent-driven-development/task-reviewer-prompt.md`) | — | The reports go to a controller, not a person: praise costs tokens and dilutes the findings. |
| writing-plans' Scope Check and File Structure (`superpowers/skills/writing-plans/SKILL.md`) | the scope check to brainstorming; file structure to the spec's Interfaces & boundaries, the plan's ownership census and inter-task contracts, and brainstorming's "small units" line | Layout that crosses tasks or is a public interface is a seam, carried by those sections; layout inside one task is the implementer's call. |
| brainstorming's "create a task for each item" line, its process digraph and its elements-of-style pointer (`superpowers/skills/brainstorming/SKILL.md`) | the router's checklist rule; numbered steps | The router covers the first; the digraph as the process diagrams above; the pointer names a skill crucible does not ship. |
| the prerequisite `[features] multi_agent = true` in `superpowers/skills/using-superpowers/references/codex-tools.md` | — | Outdated: on codex-cli 0.163.0 (2026-10-20), `codex features list` shows `multi_agent` stable and on by default. |
| the line on closing reviewer agents and the Codex App Finishing section in `superpowers/skills/using-superpowers/references/codex-tools.md` | — | On codex-cli 0.162.1 (2026-10-15), as far as a session's own listing of its tools showed, no tool closes an agent, and a completed seat continues by follow-up (`docs/decisions/runtime-adapters.md`). Crucible is tested on the Codex CLI only (`README.md` § Codex, `docs/codex.md` § Status). |
| `superpowers/.version-bump.json`, `superpowers/scripts/bump-version.sh`, `superpowers/RELEASE-NOTES.md` | the release step in `AGENTS.md` | One manual step; the suite enforces equal versions across the manifests; release notes go in the GitHub release. |
| `superpowers/CODE_OF_CONDUCT.md`, `superpowers/.github/`, and the contribution policy in `superpowers/CLAUDE.md` | `README.md` § Contributing | Issues only, no pull requests yet: nothing to maintain. |
| `superpowers/scripts/package-codex-plugin.sh`, `superpowers/scripts/sync-to-codex-plugin.sh`, `superpowers/tests/codex-plugin-sync/`, and the packaging half of `superpowers/tests/codex/` | — | Crucible installs on Codex from its own repository's marketplace (`docs/codex.md`) and publishes into no other plugin repository. |
| `superpowers/assets/` (icon and logo) | — | Upstream's own branding. |
| `superpowers/docs/superpowers/`, `superpowers/docs/plans/` | — | Upstream's own specs and plans: its project history, not the plugin. |
| `superpowers/docs/porting-to-a-new-harness.md` | `hooks/README.md` § Porting to another host | Crucible serves two hosts; its porting note points at upstream for the others. |
| `superpowers/docs/testing.md` | — | It describes upstream's test directories, none of which is carried. |
| `superpowers/tests/claude-code/`, `superpowers/tests/explicit-skill-requests/` | — | No model-launching tests: they are a maintenance burden and resource-heavy, and audits are the cheaper evidence route. |
| other hosts' files: `superpowers/GEMINI.md`, `superpowers/gemini-extension.json`, `superpowers/package.json`, `superpowers/.cursor-plugin/`, `superpowers/.kimi-plugin/`, `superpowers/.opencode/`, `superpowers/.pi/`, `superpowers/hooks/hooks-cursor.json`, the antigravity, gemini and pi references under `superpowers/skills/using-superpowers/references/`, and their tests and READMEs | — | Host scope: crucible serves Claude Code and Codex. |
| `superpowers/hooks/run-hook.cmd`, `superpowers/docs/windows/` | `hooks/hooks.json` runs bash directly | One bash hook, every failure visible. |
| the visual companion: `superpowers/skills/brainstorming/scripts/`, `superpowers/skills/brainstorming/visual-companion.md`, `superpowers/tests/brainstorm-server/` | — | The maintainer did not use it, and upstream's form is a Node server with a usage ping to strip; restoring it opt-in is open (`docs/backlog/visual-companion.md`). |
| `superpowers/skills/brainstorming/spec-document-reviewer-prompt.md`, `superpowers/skills/writing-plans/plan-document-reviewer-prompt.md` | the spec campaign; the plan phase | Replaced by crucible's own review. |
| SDD's other scripts, `superpowers/skills/subagent-driven-development/scripts/review-package` and `superpowers/skills/subagent-driven-development/scripts/task-brief` | reviewers build their own diff; the plan pointer | Replaced. |
| systematic-debugging's `superpowers/skills/systematic-debugging/CREATION-LOG.md` and its pressure and academic tests (`superpowers/skills/systematic-debugging/test-pressure-1.md` to `superpowers/skills/systematic-debugging/test-pressure-3.md`, `superpowers/skills/systematic-debugging/test-academic.md`) | — | Upstream's skill-development record, read by no workflow step. |
| writing-skills' reference files other than `superpowers/skills/writing-skills/graphviz-conventions.dot` (`superpowers/skills/writing-skills/anthropic-best-practices.md`, `superpowers/skills/writing-skills/persuasion-principles.md`, `superpowers/skills/writing-skills/testing-skills-with-subagents.md`, `superpowers/skills/writing-skills/render-graphs.js`, `superpowers/skills/writing-skills/examples/`) | the hosts' own skill tooling and guidance | writing-skills routes to each host's own tooling. |

## Not carried, decision pending

| upstream | what is open | backlog item |
|---|---|---|
| verification-before-completion's Common Failures table (claim, what proves it, what does not) and its agent-delegation check (`superpowers/skills/verification-before-completion/SKILL.md`) | whether crucible's checks cover the table | `docs/backlog/upstream-sync-review.md` |
| the code reviewer's Recommendations section (`superpowers/skills/requesting-code-review/code-reviewer.md`) | crucible's reviewers report improvements as no finding (`docs/decisions/evidence-and-findings.md`); whether that rule is right | `docs/backlog/review-improvements.md` |
| `superpowers/.pre-commit-config.yaml`, `superpowers/scripts/lint-shell.sh`, `superpowers/tests/shell-lint/` | crucible's bash hook is unlinted: whether to lint it | `docs/backlog/upstream-sync-review.md` |
| `superpowers/tests/systematic-debugging/` | `skills/systematic-debugging/find-polluter.sh` ships verbatim and untested | `docs/backlog/upstream-sync-review.md` |
