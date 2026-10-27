# Working on crucible

Instructions for agents (and people) changing this repository. Crucible is a
process plugin for Claude Code and Codex: one canonical skill tree serves
both hosts, and per-host adapters map the host mechanics. What it is and how
to install it: `README.md`; the layout: `docs/dual-runtime.md`.

## Where things are

- `docs/dual-runtime.md` — the runtime separation, adapter references, model
  floor, upgrades and rollback.
- `docs/authoring.md` — rules for writing crucible's own files: anchor
  stability and the reference convention.
- `docs/decisions/` — the decision records: why crucible is as it is, one
  record per family of decisions, named by slug. A record states the
  current position and is edited in place when the decision changes; the
  same commit adds a line to its `## Changes`,
  `<YYYY-MM-DD>: <what changed, and why>`, which the branch reviewer
  checks. Git history is the log. The record shape and the rest of the
  rules: `docs/decisions/decision-records.md`.
- `docs/backlog/` — deferred work, one file per item. Copy the shape of an
  existing item: title, observation, follow-up, and a link to the GitHub
  issue where one exists. An item states the current state, not a progress
  log. A resolved item is deleted; a partly resolved one keeps only what
  remains open.
- `docs/crucible/<date>-<slug>/` — one folder per feature: its spec, plan or
  lane note. Frozen once the feature ships; follow-ups go to the backlog.

## You are editing the process you run under

- The crucible your session runs is an installed copy, not this checkout.
  An edit here reaches no session until the install picks it up, so the
  current session never shows whether a skill change works.
- A skill change can change the rules under a feature in flight elsewhere.
  Update an install only when no feature is between its brainstorm and its
  finish.

## Authoring rules

- **Skills stay runtime-neutral.** Host mechanics (tool names, dispatch,
  model names) live only in the adapter pair
  `skills/using-crucible/references/<runtime>.md` and
  `<runtime>-dispatch.md`. Skills name a model role; the host map's
  **Model roles** entry names the models, and the one other site naming
  them is the agent generator's alias map (`MODELS` in
  `tools/instrument_agents.py`). `skills/writing-skills/SKILL.md` routes
  to each host's own skill tooling and guidance, so it names the hosts,
  and no model. The claude-ism scanner (`tests/claudeism_scanner.py`, run
  by `tests/test_claudeism_scanner.py`) checks shipped text for
  host-specific terms, Claude and Codex model names included; its
  allowlist is `tests/claudeism-allowlist.txt`.
- **`agents/` is generated.** Never edit it by hand: edit the dispatch
  template under `skills/`, then run `python tools/instrument_agents.py
  write`. The suite runs its `check` mode.
- **Interpreters.** A hook's script is bash: a hook runs with no agent
  around it to recover from a missing interpreter. A script a workflow step
  runs may be stdlib Python, since the agent running it sees a failure and
  stops.
- **Always-loaded text has a budget.** The SessionStart envelope (router
  plus host map) stays under 10,000 characters, Claude Code's threshold for
  hook output (`hooks/README.md`; `tests/test_session_start.py`).
- **Where text goes.** writing-skills' Size and placement bullet states
  the general rules. Their homes here: how a rule was learned (incidents,
  measurements, accepted trade-offs) goes in the decision records
  (`docs/decisions/`); host mechanics in the adapter pair (above); text
  about crucible's own text (where a rule lives, why a template omits
  something) in `docs/`. A seat template holds what its seat does and
  produces; rules every seat follows go in one shared reference the
  templates point to, once one exists.
- **The prose budget.** `tests/prose-budget.txt` holds each skill
  directory's word count, and the suite fails when a count rises above it
  or falls more than 50 words below it. A commit that grows a skill raises
  its number, and its body says what the words buy or what went in
  exchange; one that shrinks a skill lowers it.
- **No local context in committed text.** What this repository commits
  carries no personal paths, account names or email addresses, no
  description of a private install or setup, and nothing from the
  authors' other projects; examples use generic names and paths. The one
  exception: about a project, aggregate figures (its language, model
  family, sizes and duration, and measurements of crucible's own runs on
  it, such as token costs, rates, ratios and counts) and a description of
  what crucible itself did in a run on it may be published, never the
  project's name, domain, content or implementation details. Notes private
  to one machine go in the user-level instruction files. The branch
  reviewer checks it.
- **Tests assert text only where code or the host reads it,** and name that
  reader in a comment beside the assertion. Everything else is a structural
  check (a file, heading or anchor exists; references resolve; generated
  files match their source) or no test at all.

## Tests

`python -m pytest tests/` from the repo root: Python 3.10 or newer with
pytest, stdlib otherwise. The hook tests need bash; without it they skip and
print why. A skip is not a pass. The suite launches no model.

## Git

- Work in a worktree under `.worktrees/` (gitignored), on a branch named for
  the feature; never commit on `master` directly.
- One commit per logical change: a short subject, and a body saying what
  changed and why.
- Land on `master` by merging the branch, and only on the operator's
  go-ahead for that landing.
- A release: bump the version in the three manifests on a branch and land
  it on `master` as above; tag that commit `v<version>`; fast-forward
  `stable` to it; publish a GitHub release with a few lines of notes.
  Minor for a behaviour change, patch for fixes. `stable`, the default
  branch, holds only releases, and the maintainer's own install tracks it
  (`docs/dual-runtime.md` § Release metadata).
- Line endings are LF. `hooks/session-start` and `*.sh` must stay LF
  (`.gitattributes`); writers that emit CRLF on Windows will break the hook.
