# Records and workspace

## Decision

**The feature folder.** A feature commits its spec and, on the standard
route, its plan, in one feature folder, `docs/crucible/<YYYY-MM-DD>-<slug>/`
by default, a root the project's instruction files name overriding the
default. The spec is the agents' coordination artifact: its audience is
the agent fleet, and it says what binds and what is advice
(`docs/decisions/the-spec.md`). Both are committed on the feature branch,
where agents in other checkouts can read them. Brainstorming creates the
folder by a birth step that refuses a slug some folder already carries;
every later consumer finds it by a resolve step that creates nothing and
reports none or several (`skills/redteaming/references/formats.md`
§ Feature folder). A shipped spec is never silently edited: it stays as
the forensic record, and a route that replaces it writes a successor
beside it. The exception is an umbrella's `umbrella.md`, edited in place
after it lands until it closes (`docs/decisions/umbrellas.md`). In a pull
request, finishing lists the files the branch adds to its feature folder
and asks the operator whether they go in, saying first that the branch's
commits carry them anyway; an umbrella's own pull request leaves
`umbrella.md` off that list, so it stays in the merged tree
(`crucible:finishing-a-development-branch § Step 5: Execute Choice`).

**The workspace.** A feature's process records (round records, seat
reports, the execution ledger, scratch) live in `.crucible/<slug>/` at the
root of the checkout the controller works in. It ignores itself through a
`.crucible/.gitignore` holding `*`, written by a prose provisioning step
and confirmed with `git check-ignore` on a file path
(`skills/redteaming/references/formats.md` § Feature workspace root and
layout); no host `.gitignore` is edited. Nothing in it is committed or
archived, and `.crucible/` holds workspaces only. SDD Setup looks for the
workspace before its worktree and provisioning steps, and continues in
the checkout that holds it. A workspace's life has three ends, SDD
Finish, an umbrella's landing and the feature's abandonment, and each
deletes it (`skills/redteaming/references/formats.md` § Feature
workspace root and layout). A workspace lost mid-feature restarts the
in-flight phase from the committed spec or plan and `git log`.

**No committed summary.** A feature's committed record is its spec, its
plan and its commit messages. Nothing summarizes a campaign or a feature
into the repository, and nothing parses records to assemble one; the
records' process rules still bind, and their layout is guidance. The
session transcripts hold the raw records for as long as the host keeps
them (`README.md` § What it writes into your repository).

**Finish.** SDD Finish runs in a fixed order: record checks, the
feature's mark in its umbrella where an umbrella names it, the full
suite or the project's declared merge gate on HEAD, a close readout to
the operator, deletion of `.crucible/<slug>/` and nothing else, then
finishing; any loop activity restarts it at the record checks. A red run
is a BLOCKER for the branch-review loop, never classified away; the close
readout, assembled from the ledger, is the only hand-over of work left
open (`crucible:subagent-driven-development § Finish`). Finishing accepts
a full run on exactly the HEAD being integrated whose output it can still
show, and otherwise re-runs. In a pull request the repository's
conventions come first, and changing commits already made to meet one is
the operator's decision; PR feedback is handled in the kept worktree
under `crucible:receiving-review`
(`crucible:finishing-a-development-branch § Step 5: Execute Choice`).

## Why

### The feature folder

The spec exists to align implementers, reviewers and redteamers in fresh
contexts; once the feature ships that coordination has ended, so the spec
stays as it was, a record of what was built against, and durable
knowledge goes to documentation instead (the design philosophy of
2026-08-06). (Basis: judgment, accepted by the maintainer.)

Committing on the feature branch is what makes the documents reachable:
the workspace is gitignored, and gitignored files do not reach a
worktree another agent works in. The maintainer ruled on 2026-08-07 that
retention beyond that is the project's business: committing every spec
forever had been an inherited habit, and review commits could outnumber
the code's. Upstream commits its specs to a default folder of its own
and lets a user's preference move them
(`superpowers/skills/brainstorming/SKILL.md`); crucible fixed its root for
a while and made it a default again on 2026-10-12, restoring that
override. (Basis: the maintainer's preference; external, for upstream.)

The birth and resolve steps match a folder name exactly, a date then the
whole slug: a `*-<slug>` pattern would also match
`2026-10-11-bar-<slug>`, and a new feature would resolve into a finished
one's folder. (Basis: judgment, accepted by the maintainer, 2026-10-11.)

The pull-request ask came on 2026-10-08. A branch's commits carry its
spec and plan, so removing them before a push keeps them out of the
merged tree only; the maintainer judged the real fix to lie at the start
of the work, since the plan's pins need commits, and a mode in which they
are never committed is `docs/backlog/records-retention-config.md`.
(Basis: the maintainer's preference.)

An umbrella is the exception to that ask, since its children read it,
their marks included, on the base they branch from and land on: removed
from the merged tree, it would be gone for every child after it. The
trade-off is that a project keeping feature folders out of its merged
tree still keeps each `umbrella.md`; a child's own folder is asked about
like any feature's. (Basis: judgment, accepted by the maintainer,
2026-10-27.)

### The workspace

Upstream's SDD keeps a per-plan workspace,
`.superpowers/sdd/<plan-basename>/`, made by a script that writes a
self-ignoring `.gitignore`, and deletes it after the final review
(`superpowers/skills/subagent-driven-development/scripts/sdd-workspace`).
Crucible widened it to one workspace per feature, shared by the spec
campaign, the plan phase and execution. Archiving it was rejected on
2026-08-07: the maintainer judged that full archives would accumulate
heavily even on a small project. (Basis: external; the maintainer's
preference.)

Provisioning became a prose step on 2026-10-11, when the script that did
it was retired. Its two cautions are host facts, checked again on
2026-10-20 with git 2.56.0 on Windows: Windows PowerShell 5.1's `>`
writes UTF-16LE, and against a UTF-16LE `.gitignore` holding `*`,
`git check-ignore` exits 0 for the workspace directory and 1 for a file
inside it, so only the file-path form shows that git does not read the
file. (Basis: measured.)

A lost workspace costs at most the in-flight phase, since everything an
earlier phase settled is committed. A configuration file under
`.crucible/` was dropped on 2026-10-12: its history was empty in
crucible's own repository and in the one other project crucible had run
on, and a project states its wishes in its own instruction files, which
outrank skills. (Basis: measured; judgment, accepted by the maintainer.)

An umbrella's landing became the third end on 2026-10-27. An umbrella
takes no plan and no execution, so it never reaches SDD Finish, and its
workspace would otherwise outlive it; it is deleted before the landing,
after the campaign records are checked, as SDD Finish deletes a
feature's. (Basis: judgment, accepted by the maintainer.)

### No committed summary

Until 2026-10-10 a script parsed the agents' records into a committed
feature summary. The records are open input, and the parser grew a case
each time a review found a shape it misread: 720 lines on 2026-08-07,
3,014 by 2026-10-09, eighteen commits in that month's first nine days.
Measured on 2026-10-10 over the maintainer's session transcripts since
2026-08-01: the summaries were read 198 times, mostly by the session that
wrote them or by other production work, and two or three times to learn
what an earlier feature did. The record checks built into the summary
step, shipped on 2026-10-07, never fired in the 125 runs after.
(Basis: measured.)

### Finish

The suite runs before the workspace is deleted, because a failure found
afterwards has no ledger to land in (2026-10-07). A red run is handed to
the branch-review loop like any other BLOCKER: classifying it as not the
branch's own is a dispute the adjudicator rules on
(`docs/decisions/adjudication.md`). Upstream's finishing runs the full
suite at its Step 1 every time
(`superpowers/skills/finishing-a-development-branch/SKILL.md`).
Crucible keeps upstream's point, that a run proves only the tree it ran
on, and relaxes the rule: a run on exactly the HEAD being integrated,
whose output can still be shown, counts, so finishing does not repeat
SDD Finish's run; the maintainer reported crucible's own suite taking 7
to 39 minutes in that day's lane runs. The close readout replaced the
committed summary as the hand-over of open work; filing that work is
left to the operator or the repository's conventions. (Basis: external,
for upstream; judgment, accepted by the maintainer; measured, by the
maintainer's report, for the run times.)

The umbrella mark, added on 2026-10-27, comes before the suite so that
the suite runs on the tree that lands, mark included; a mark committed
after it would land untested. (Basis: judgment, accepted by the
maintainer.)

Repository conventions come first in a pull request (2026-10-08), with no
attempt to detect who owns the repository; a convention that rewrites
commits already made, such as sign-offs, is a history rewrite and the
operator's call. Reading those conventions at worktree setup instead is
`docs/backlog/repo-conventions-at-setup.md`. PR feedback is handled
where the PR's reviewers and thread already form the loop, in the kept
worktree. (Basis: judgment, accepted by the maintainer.)

## Rejected

- **A committed feature or campaign summary**, per-round summary
  commits, and the parser, index and record checks that served them:
  rarely read, and costly to keep parsing open input (§ Why).
- **Archiving the workspace**: archives would pile up even on a small
  project (§ Why).
- **Living specs** kept true after the feature ships: a shipped spec is a
  forensic record, and durable knowledge goes to documentation (§ Why).
  The rejection covers a feature's spec once its feature ships. An
  umbrella is edited in place after it lands, because it holds an open
  effort's current state, and is frozen once it closes
  (`docs/decisions/umbrellas.md`).
- **A configuration file under `.crucible/`**: no repository crucible
  ran on ever used one, and instruction files already outrank skills
  (§ Why).

## What a project may change

- The feature folder's root, named in its instruction files.
- Its pull-request conventions (template, commit-message rules, sign-off,
  hooks), which override crucible's defaults.
- Its merge gate, which SDD Finish and finishing run in place of the full
  suite.

## Changes

- 2026-10-28: umbrellas (`docs/decisions/umbrellas.md`): an umbrella's
  landing as the workspace's third end, since an umbrella never reaches
  SDD Finish; the umbrella mark in SDD Finish before the suite, so the
  suite runs on the tree that lands; `umbrella.md` kept off the
  pull-request ask, since children read it from the merged tree; and the
  living-specs rejection scoped to a feature's spec after it ships, since
  an umbrella stays open after it lands.
- 2026-10-12: the feature folder: spec and plan committed on the feature
  branch under a default root a project may override, found by an exact
  birth and resolve match, a shipped spec never silently edited, and the
  pull-request ask about the folder's files.
- 2026-10-11: the workspace: `.crucible/<slug>/`, self-ignoring through a
  prose provisioning step checked on a file path, nothing committed or
  archived, found first by SDD Setup, a lost one restarting the
  in-flight phase.
- 2026-10-11: SDD Finish: record checks, the suite on HEAD, the close
  readout, deletion of the workspace alone, then finishing; finishing's
  reuse of a run on the exact HEAD, repository conventions first in a
  pull request, and PR feedback in the kept worktree.
- 2026-10-10: no committed feature summary and none of its record
  machinery; the spec, the plan and the commit messages are the
  committed record.
