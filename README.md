# crucible

Crucible is a set of process skills for AI coding agents, for Claude Code
and, experimentally, Codex. It turns "I want to build X" into a reviewed
design, a plan, an implementation by fresh agents and a reviewed branch,
with you steering through plain-language decisions along the way.

It is one person's workflow for building projects meant to be maintained
for a long time, shared because frameworks for individual-scale autonomous
agentic development are scarce. It is not a product: there is no support
promise, and you should not expect the polish of a professional project.
Take what is useful.

## Who it is for

People who build software by steering an AI agent rather than by writing
the code themselves. Crucible asks you for decisions, not reviews: when a
judgment is needed, you get a **decision ask**, a plain-language question
with the options and a recommendation. You are never required to read a
spec, a plan, code or a diff, and nothing is withheld: ask to see any of
it and you will.

If you like to read and approve every plan by hand, crucible will still
work, but much of its machinery exists so that you don't have to.

## How it compares

These are the maintainer's impressions, not measurements: comparisons on
vibes.

- **Against your host with no process plugin:** large gains in
  requirements elicitation, in the agent doing what you meant, and in code
  quality, at about 5–10× the tokens in the typical case.
- **Against [superpowers](https://github.com/obra/superpowers):**
  significantly more autonomy (no need to review specs and plans by hand,
  as superpowers intends you to) and/or better intent alignment and code
  quality when run without much oversight, depending on your skill and
  involvement, at about 1.5–2× the tokens.
- **Against superpowers plus a generic skill that has subagents redteam
  your documents iteratively:** essentially that, packaged and
  streamlined, with somewhat better autonomy and feel. A look back over
  one project's history found no detectable difference in how often work
  needed repair late, so settling this would take a controlled trial.

**Calibration.** Crucible's numbers (how many reviewers a round seats, how
many rounds a review may take, how large a plan gets) come from one
personal Python project built on Claude models over about eight months:
about 80,000 lines of application code and about 175,000 lines of tests,
counted without blank, comment or docstring lines, plus about 9,000 lines
of prompt files. They may not fit your project; your project's instruction
files can override them (§ Configuration).

## Platforms and prerequisites

- **Hosts:** Claude Code, tested on 2.1.310; Codex, experimentally,
  tested on codex-cli 0.162.1 (§ Codex).
- **Operating systems:** the startup hook is measured on Windows (Git
  Bash) and Linux, not yet on macOS.
- **git:** crucible works on branches and worktrees.
- **bash 3.2 or newer**, on Claude Code only: the startup hook is a bash
  script. On Windows it is Git Bash's.
- **Python 3.8 or newer:** one review step runs a small standard-library
  script.

## Quickstart

1. **Turn off any other process plugin first** (§ Coming from superpowers).
2. **Install** (Claude Code):

   ```bash
   claude plugin marketplace add PrimeSeeker/crucible
   claude plugin install crucible@crucible
   ```

   To try it without installing, clone the repository and load it for one
   session only:

   ```bash
   git clone https://github.com/PrimeSeeker/crucible
   claude --plugin-dir ./crucible
   ```

   On Codex, follow `docs/codex.md`.
3. **Start a new session in your project.** On Claude Code, crucible's
   hook loads its router (the skill that decides which workflow applies)
   when a session starts, is cleared or is compacted. Success is silent.
   If it fails, you see a hook-error notice reading
   `crucible: router not loaded: <reason>`, and that session runs without
   crucible. So no notice means it loaded. A session that was already open
   when you installed never ran the hook: start a new one. On Codex,
   crucible registers no hook; check that its sessions reach the router
   with `docs/codex.md` § Check: routing.
4. **Say what you want to build**, for example "I'd like to add CSV export
   to the reports page". Crucible asks questions one at a time, proposes
   approaches with a recommendation, presents the design in sections for
   your approval, and from then on comes back to you only with decision
   asks and short readouts.

## Coming from superpowers

Crucible began as a rewrite of the superpowers skills it used, and it
replaces them rather than sitting beside them. Each has a router that
decides which workflow a session follows, and two routers in one session
fight over that. Never start a session with two routers on, or with any
other skill or plugin that does the router's job.

Before installing crucible, turn superpowers off. On Claude Code,
`claude plugin list` shows its exact name; then
`claude plugin disable superpowers@<its-marketplace>`. Uninstalling works
as well; either way, what counts is that no session starts with both. On
Codex, `docs/codex.md` § Turning another router off gives the config.

## How it works

**The flow.** You describe what you want. Brainstorming turns it into a
written spec through a dialogue with you. A **spec campaign** then sends a
panel of fresh agents, each with its own review angle, to attack the spec
in rounds: their findings are merged and fixed, and another fresh agent
checks the fixes. After each round you get a readout and any decision
asks. A campaign stops at the first round that finds no serious or
structural problem, or at four rounds, when what is still open comes to
you. A final **terminal pass** re-reads the whole spec and checks that the
readouts you were given were faithful to the findings. Then a plan is
written and checked once, and execution starts: a fresh agent implements
each task, a fresh reviewer checks it, and disagreements go to an
adjudicator. A whole-branch review closes the work, and you choose whether
to merge, open a pull request or keep the branch.

**Three routes.** At the end of the design dialogue crucible recommends a
route, and you confirm or veto it:

- **Standard:** spec, spec campaign, plan, a single verification round of
  the plan, execution.
- **Folded:** for a small change that still carries a design decision
  worth reviewing: one document holding both spec and plan, the same spec
  campaign, no separate plan step.
- **Very small:** for a small change with no design decision worth
  reviewing before code: a short lane note, implemented directly, then the
  branch review.

**The skills**, one line each:

- `using-crucible` — the router: at the start of every session, it decides
  which skills apply.
- `brainstorming` — turns an idea into a spec through dialogue with you.
- `redteaming` — runs the spec campaign, and the plan's one verification
  round.
- `writing-plans` — turns a reviewed spec into a lean plan: who does what,
  in what order, checked how.
- `subagent-driven-development` — executes the plan with a fresh
  implementer and reviewer per task.
- `requesting-code-review` — reviews the whole branch before it merges.
- `receiving-review` — handles review feedback from outside crucible, such
  as a pull request's reviewers.
- `dispatching-parallel-agents` — runs independent tasks side by side.
- `systematic-debugging` — finds the root cause before any fix.
- `using-git-worktrees` — sets up an isolated working copy for a feature.
- `finishing-a-development-branch` — merges, opens a pull request or keeps
  the branch, as you choose.
- `writing-skills` — writes and checks text that instructs agents,
  crucible's own included.

The repository's layout and the line between shared skills and per-host
adapters are in `docs/dual-runtime.md`.

## What it writes into your repository

- **A feature folder,** `docs/crucible/<date>-<feature-name>/`, holding
  the spec and the plan (`design.md` and `plan.md`; `folded.md` or
  `note.md` on the two small routes). They are committed on the feature
  branch, so they merge with the work.
- **An umbrella,** `umbrella.md` in a feature folder of its own, for an
  effort too large for one feature: what its features share, what each
  delivers, in what order, and which have landed. Each feature names it
  and is reviewed against it. Unlike a spec, it stays open after it
  merges, updated as its features land, until each has landed or been
  dropped.
- **A workspace,** `.crucible/<feature-name>/`, holding the review rounds'
  records, agents' reports and the execution ledger. It is untracked
  (crucible writes a `.crucible/.gitignore` that ignores it all) and is
  deleted when the feature finishes.
- **Worktrees.** By default every feature gets its own worktree, a
  separate working copy on the feature's branch, unless your project's
  instructions say to work in place. Crucible uses your host's own
  worktree tool where one exists. Where it creates one itself, it goes
  under `.worktrees/`; if that folder is not already ignored by git,
  crucible adds it to `.gitignore` and commits that change.

Once a feature finishes, its process records (review rounds, reports,
rulings) live only in your host's session transcripts, so they last only
as long as your host keeps those.

## Configuration

Crucible has no config file. Your instruction files (`CLAUDE.md` on Claude
Code, `AGENTS.md` on Codex, user-level or the project's) and your direct
requests outrank the skills, so that is how you change a default: name
another folder for feature folders, say to work in place rather than in
worktrees, name a worktree directory, or change a review's size.

## Cost, models and permissions

**Tokens.** Crucible spends tokens to save your attention: by the
maintainer's impression, about 5–10× a plain session in the typical case,
and 1.5–2× superpowers (§ How it compares). A large new spec's first
review round seats four or five reviewers.

**Subscriptions,** in the maintainer's experience: Codex is effectively
unusable below ChatGPT's Pro plan, between its low overall limit and its
five-hour window. Claude's Pro plan works with one session at a time;
several sessions at once need Max.

**Models.** Nearly every agent crucible starts runs on your host's default
role, a strong model, and the session running the workflow should be on a
strong model too. Each host's models are named in its host map's Model
roles entry (`skills/using-crucible/references/claude-code.md`,
`skills/using-crucible/references/codex.md`).

**Permissions.** Crucible assumes agents can work without you approving
each step, such as in Claude Code's auto mode. Any other permission setup
is yours to manage.

## Crucible and your host's own features

- **Plan mode:** crucible's plans are documents committed beside the spec,
  so they persist and every agent can read them. Crucible does not use
  the host's plan mode for them; asking for plan mode sends the session
  through brainstorming first.
- **Built-in code review:** not used; crucible's own branch review takes
  its place.
- **Worktree tools:** used where the host offers them.

## Codex

Experimental. On the Codex CLI crucible failed two checks: one fresh
session in three acted before reading the router, and the checklist tool
crucible uses is off by default and, turned on, has only been seen to
accept a call. The desktop app and the IDE extension are untested.
`docs/codex.md` covers installing it, the two config settings it needs,
checking that it is the only router and that sessions reach it, and
rolling back.

## Updates and versions

A release is tagged `v<version>` and published as a GitHub release with a
few lines of notes. The repository's default branch, `stable`, holds the
latest release, so a plain install gets it, and the maintainer's own
install tracks it too. A behaviour change bumps the minor version; a fix
bumps the patch version.

To update on Claude Code, run `claude plugin update crucible@crucible`,
then start a new session. To stay on a version, or go back to one,
install from its tag: `claude plugin marketplace add
PrimeSeeker/crucible#v<version>` on Claude Code, `--ref v<version>` on
Codex. Note your installed version before updating: it is the one you
would go back to. `claude plugin list` and `codex plugin list` show it.
`docs/dual-runtime.md` § Upgrades and rollback has the full commands for
both hosts.

## Glossary

- **Operator** — you, the person steering.
- **Router** — the skill that decides, at the start of a session, which
  workflow applies.
- **Seat** — one fresh agent given one job: a reviewer, an implementer, a
  verifier.
- **Spec** — the design document: intent, decisions, constraints,
  acceptance.
- **Plan** — who does what, in what order, and how each part is checked.
- **Campaign** — the spec's review: rounds of reviewer panels until it
  converges.
- **Round** — one review pass by a panel.
- **Wave** — one batch of fixes plus its check.
- **Terminal pass** — the last check of a review, including whether what
  you were told matched the findings.
- **Decision ask** — a question for you, in plain language, with options
  and a recommendation.
- **Route** — standard, folded or very small (§ How it works).
- **Feature folder** — the committed folder with a feature's spec and plan.
- **Umbrella** — the committed document holding an effort of several
  features: what they share, what each delivers, and which have landed.
- **Workspace** — the untracked folder with a feature's process records,
  deleted at finish.
- **Host map** — the file that maps crucible's operations to one host's
  tools and models.

## Contributing

Reports and suggestions are welcome as GitHub issues. Pull requests are
not accepted yet. An accepted report becomes an item in `docs/backlog/`
that links the issue. `AGENTS.md` holds the rules for changing crucible
itself, and `docs/decisions/` why things are as they are.

## License and credits

MIT; see `LICENSE`. Much of crucible's skill text, prompts and scripts is
ported from [superpowers](https://github.com/obra/superpowers) by Jesse
Vincent, used under the MIT license; `LICENSE` carries the attribution.
The plan format merges a proposal from
[superpowers issue #895](https://github.com/obra/superpowers/issues/895)
with the plan skill of Compound Engineering's
[plugin](https://github.com/EveryInc/compound-engineering-plugin),
`ce-plan`.
