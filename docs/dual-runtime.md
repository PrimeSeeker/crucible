# Dual-runtime architecture

How one canonical skill tree serves both Claude Code and Codex: what is
canonical, what is adapter-mediated, what each runtime registers, and how
releases, upgrades and rollbacks stay trustworthy.

Companions: `docs/codex.md` (installing crucible on Codex, its checks and
rollback). Hook mechanics: `hooks/README.md`.

## Layout

```
.claude-plugin/plugin.json       # Claude Code plugin manifest
.claude-plugin/marketplace.json  # Claude Code marketplace descriptor
.codex-plugin/plugin.json        # Codex plugin manifest
.agents/plugins/marketplace.json # Codex marketplace descriptor
skills/<name>/SKILL.md           # process skills (+ sibling prompt templates/scripts)
skills/<name>/agents/openai.yaml # Codex presentation metadata, per skill
agents/<name>.md                 # Claude Code instrument agents (generated; never hand-edited)
tools/                           # authoring tools: instrument_agents.py writes/checks agents/
hooks/                           # SessionStart router injection (Claude Code; Codex registers none)
tests/                           # repo test suite (python -m pytest tests/)
docs/                            # runtime docs (this file, codex.md), authoring rules, backlog/
docs/decisions/<slug>.md         # decision records: why crucible is as it is
docs/upstream.md                 # the upstream map: where superpowers' files went
docs/crucible/<date>-<slug>/     # one folder per feature: its spec and plan
```

## The separation

Three layers, deliberately not collapsed into each other:

1. **Canonical skills** — everything under `skills/`. All process rules and
   prompt bodies live here, once. No runtime gets a copied or generated skill
   tree, and no runtime-specific fork of a workflow exists. The one generated
   artifact is Claude Code's instrument agents (layer 2): each is rendered
   from a dispatch template by `tools/instrument_agents.py` and never edited
   by hand, so the template stays the fixed text's only home.
2. **Runtime registration** — the manifests and the hook registration that
   tell a host this plugin exists and how to run its hooks
   (`.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, `hooks/hooks.json`
   — Claude Code's; Codex registers no hook, its manifest declaring
   `"hooks": {}` — and the per-skill `agents/openai.yaml` presentation files
   Codex reads), plus the seven generated instrument agents
   under the repo-root `agents/`, which Claude Code's plugin loader offers as
   `crucible:<name>` and Codex ignores.
3. **Runtime mapping** — each runtime's adapter, a pair of references under
   `skills/using-crucible/references/` that say how to *enact* a process rule
   on this host: the **host map**
   (`skills/using-crucible/references/claude-code.md`,
   `skills/using-crucible/references/codex.md`), which every session reads,
   and the **dispatch reference** beside it (`claude-code-dispatch.md`,
   `codex-dispatch.md`), which a skill that dispatches seats reads.

An adapter may map an operation. It may not redefine workflow policy: if a rule
would read differently on the two runtimes, it belongs in neither adapter. The
report-file procedure — confirm an instrument's report is on disk, resume it
once, then persist the text under a mark saying the controller saved it — is
such a rule: it lives in the dispatch composition's report item, and the Claude
Code dispatch reference keeps only the host fact behind it, the report-name
filter.

### Namespace vocabulary

What the adapter mediates is the invocation **mechanism** — the host verb —
never the skill's **name**. The `crucible:<skill-name>` form is crucible's own
namespace vocabulary and stays canonical in shared text on every runtime. It is
not a host-specific construction, and the shared-text scanner does not target
it.

## Adapter references

Each runtime's two references answer the same fixed set of questions, in the
same order, so a workflow can name an operation once and have it resolve on
either host.

- **The host map** — the instruction files the host reads (user-level and
  project); planning mode; then the Operations list — load a skill, track a
  checklist, dispatch a fresh agent, wait, parallel fan-out, select model,
  edit, shell, worktree — then Model roles. It is what every session needs:
  on Claude Code the SessionStart hook inlines it into the session, and a
  Codex session reads it from its path, as the router directs.
- **The dispatch reference** — dispatch an instrument, resume an agent,
  select effort; on Claude Code also the report-name filter and compaction
  (Codex has no compaction entry). It is what a skill that dispatches seats
  needs: SDD, redteaming and requesting-code-review each say near their
  start to read it, and to
  read it again after compaction, since the hook re-injects only the host
  map.

The router's § Runtime reference is the one place that defines the pair as
the runtime adapter, so skill text naming "your adapter's" operation
resolves in whichever file holds it.

Selected divergences worth knowing before reading either runtime's files:

| Operation | Claude Code | Codex |
|---|---|---|
| load a skill | the host's skill-invocation verb, by namespaced name | the session's skill listing; expand the root alias and read that `SKILL.md` in full |
| track a checklist | the host's todo tool | `update_plan`, one step per item, at most one `in_progress`; on codex-cli 0.162.1 only with `[tools.update_plan] enabled = true` in the Codex config |
| dispatch a fresh agent | the host's task-dispatch tool; a dispatch carries none of the session's history | `spawn_agent` with `fork_turns: "none"` — the fresh-context guarantee is **never** left to a host default, since an omitted `fork_turns` forks the full history |
| dispatch an instrument (dispatch reference) | the plugin's instrument agent `crucible:<name>`, with an explicit model and the filled slot card as the whole prompt; where that agent is not offered, the template path | the template path: the filled slot card and template, through `spawn_agent` with `fork_turns: "none"` — a plugin cannot ship Codex agent roles |
| resume an agent (dispatch reference) | follow up to the recorded agent identity where the harness exposes one | `followup_task` (new task, triggers a turn) or `send_message` (message only), addressed by the canonical task name recorded at spawn |
| wait | the dispatch returns the final report | `wait_agent` returns the final status; the answer also arrives as a notification |
| edit | the host's edit/write tools | `apply_patch` |
| shell | the host shell tool | `exec_command` |
| worktree | a native worktree tool where exposed | no native operation; individual Git invocations through the shell |

Two properties are contracts rather than convenience:

- **Persist agent identities before relying on continuation.** On Codex the
  canonical task name is recorded at spawn; on Claude it is whatever identity
  the harness exposes at dispatch. Where a host exposes no resume operation at
  all, a fresh seat is the sanctioned path and the report file is the
  persistent memory.
- **Parallel fan-out is a property of independence, not of packaging.** Fan out
  only where the tasks share no state, impose no ordering, and neither reads
  the other's output. On Codex every agent shares one working directory, so
  tasks touching the same tree are not independent. On Codex this path is
  **unexercised**: crucible's Codex tests dispatched one agent at a time and
  never fanned out. Treat a first fan-out there as unproven.

## Model floor and effort policy

Model selection is written in roles, and each host maps the roles to its
models in one place. This section says where each part lives; it restates
none of it.

- **The rules** —
  `skills/subagent-driven-development/references/dispatch-composition.md`
  § Models and effort: the three roles (default, bounded, alternate), the
  alternate's triggers, naming the model on every dispatch, and effort as
  the operator's. Each skill's seat rows and each slot card name a role and
  point there.
- **The models** — each host map's **Model roles** entry
  (`skills/using-crucible/references/claude-code.md`,
  `skills/using-crucible/references/codex.md`): this host's model for each
  role and the floor no dispatch goes below. Skills and slot cards name no
  model.
- **Effort** — each dispatch reference's **Select effort** entry
  (`claude-code-dispatch.md`, `codex-dispatch.md`): this host's effort
  mechanism and any exception this host makes to the escalation rule,
  which the rules above state.
- **The generator** — `MODELS` in `tools/instrument_agents.py` gives each
  Claude Code instrument agent its role's model alias: the one site outside
  the host maps that names models, since it renders host-specific files.

**A model release** that keeps the roles is an edit to one host's Model
roles entry; on Claude Code, none at all where the generator's alias already
tracks the new model. A new model line name also changes the generator's
alias where a Claude Code role moves to it, and adds a scanner term
(`tests/claudeism_scanner.py`) and an allowlist row
(`tests/claudeism-allowlist.txt`). A change to the roles, the seats'
assignments or the alternate's triggers is recorded, with its reason, in
the project's decision records.

## Runtime identity in seats

A dispatched agent is not a router session, and must never re-run the top-level
router to fetch its host mechanics. It carries no adapter text either: every
fresh seat gets the **runtime name** — the host it runs on — and uses that
host's own tools for editing files, running commands and loading a skill.
Each template's runtime paragraph says exactly that. A seat's work is fixed by
its template, and each host already tells a seat its own tools (for loading
a skill on a template-path Codex seat, measured on codex-cli 0.162.1), so
none of the adapter is the seat's to read. Where the name comes from
depends on the dispatch path:

- **Instrument-agent path** — Claude Code's templated dispatches:
  `tools/instrument_agents.py` fills the template's one runtime slot with
  "Claude Code" when it renders the agent, and the prompt carries only the
  filled slot card. The generator reads no runtime reference.
- **Template path** — Codex, and the Claude Code fallback when an instrument
  agent is not offered: the controller fills the runtime name into the
  template's runtime slot at dispatch.
- **Controller-composed dispatches** no template serves: the controller names
  the host and tells the seat to use its own tools.

When crucible itself is developed in a worktree, the loaded agents come from
the checkout the plugin is loaded from, not from the worktree — as templates
read from the installed plugin already do.

The runtime name is item 3 of the seven-item dispatch composition every fresh
seat gets, defined once in
`skills/subagent-driven-development/references/dispatch-composition.md`. On
the instrument-agent path the agent and the filled slot card carry the seven
together; on the template path the filled card and template do. A seat given
a plan takes item 4's pin from the spec pointer in the plan's header, which
the card points at; any other seat, from the card's own pinned path.

## Release metadata

Constraint: every version-bearing runtime manifest and Claude metadata version
stays synchronized, and the Codex marketplace's source and policy metadata is
validated without inventing a version field the schema does not have.

| File | Carries a version | Notes |
|---|---|---|
| `.claude-plugin/plugin.json` | yes | the plugin version |
| `.claude-plugin/marketplace.json` | yes | the entry's version must equal it |
| `.codex-plugin/plugin.json` | yes | must equal both of the above |
| `.agents/plugins/marketplace.json` | **no** | the Codex marketplace schema has no version field; none may be invented at any nesting level |

The automated suite checks all of it: the three versions are equal and present;
the Codex marketplace file contains no `version` key anywhere; both marketplace
sources point at this repository (`./` / `{"source": "local", "path": "./"}`);
the Codex plugin manifest's `skills` path points at the canonical tree and its
`hooks` field is exactly `{}`, with no Codex hook registration file shipped;
the Codex marketplace entry declares explicit installation and
authentication policy plus a category; every shipped skill carries its
`agents/openai.yaml` presentation metadata; and no registration or presentation
file bakes in any project's policy.

A release bump therefore edits three files together, or fails the suite.

**A release is a promotion to `stable`.** Features land on `master`. A
release lands the version bump on `master` like any change, tags that
commit `v<version>`, fast-forwards `stable` to it and publishes a GitHub
release with a few lines of notes. `stable` is the default branch and
holds only releases, so a plain install from GitHub gets the latest one.
A behaviour change bumps the minor version, fixes the patch version. The
tag is `v<version>`, not the `<plugin>--v<version>` form Claude Code's
`claude plugin tag` creates: other plugins' dependency version ranges
resolve against that form, and no plugin depends on crucible.

**A pre-release tries a change before its release.** Bump `master`'s
version to a pre-release one (`0.3.0-rc.1`), tag that commit
`v0.3.0-rc.1`, and install pinned to the tag (§ Upgrades and rollback);
`stable` does not move. The version change makes a host fetch the new
copy (§ Upgrades and rollback). The repository protects every `v*` tag from deletion, so a
pre-release tag stays, like a release's.

## Upgrades and rollback

**Every release keeps its tag, so rollback is reinstalling the
predecessor's tag;** no archive is needed. Note the installed version
before upgrading: it is the one a rollback returns to.

No step re-observes hook trust. No current install registers a hook that
asks for trust: crucible registers no Codex hook, and Claude Code's docs
describe no per-hook trust step for plugin hooks.

**Upgrade to the latest release.** Both hosts fetch a new copy when an
install moves to a different version (measured on both). Claude Code
fetches only then: a plugin that sets a version stays on it until the
version changes (its plugin manifest reference). The commands below ran
from 0.2.0 to 0.3.0 on both hosts (Claude Code 2.1.311, codex-cli
0.164.0), and each fetched the new copy. Whether Codex skips the
fetch when only the content changes is unverified
(`docs/backlog/release-metadata-and-versioning.md`).

- Claude Code: `claude plugin update crucible@crucible`, then start a new
  session.
- Codex installs a cached copy: refresh the marketplace with
  `codex plugin marketplace upgrade crucible`, then
  `codex plugin remove crucible@crucible` and
  `codex plugin add crucible@crucible`.

**Hold or roll back to a version.** Uninstall, re-add the marketplace
pinned to that version's tag, and install again:

```bash
# Claude Code
claude plugin uninstall crucible@crucible
claude plugin marketplace remove crucible
claude plugin marketplace add PrimeSeeker/crucible#v<version>
claude plugin install crucible@crucible

# Codex
codex plugin remove crucible@crucible
codex plugin marketplace remove crucible
codex plugin marketplace add PrimeSeeker/crucible --ref v<version>
codex plugin add crucible@crucible
```

**Try a pre-release** the same way, with its tag (`v0.3.0-rc.1`) in
place of `v<version>`. To go back, pin a release tag, or re-add the
marketplace without a tag to track `stable` again.

After any install, upgrade or rollback, check routing in a new session. On
Claude Code, no `crucible: router not loaded` notice means the router
loaded (`hooks/README.md` § SessionStart injection). On Codex, run
`docs/codex.md` § Check: routing.

A version rollback leaves crucible on. Switching back to another router is
a separate step: on Claude Code, `claude plugin disable crucible@crucible`
and re-enable the other; on Codex, `docs/codex.md` § Rollback.

On Codex all of this is per surface: the CLI is the one tested, and the
desktop app and IDE extension are untested (`docs/codex.md` § Status).
