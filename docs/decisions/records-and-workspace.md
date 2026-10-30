# Records and workspace

## Decision

**The feature folder.** A feature commits its spec, on the standard
route its plan, and at its finish its `open-items.md` (below), in one
feature folder, `docs/crucible/<YYYY-MM-DD>-<slug>/`
by default, a root the project's instruction files name overriding the
default. The spec is the agents' coordination artifact: its audience is
the agent fleet, and it says what binds and what is advice
(`docs/decisions/the-spec.md`). All are committed on the feature branch,
where agents in other checkouts can read them. Brainstorming creates the
folder by a birth step that refuses a slug some folder already carries;
every later consumer finds it by a resolve step that creates nothing and
reports none or several (`skills/redteaming/references/formats.md`
§ Feature folder). A shipped spec is never silently edited: it stays as
the forensic record, and a route that replaces it writes a successor
beside it. The exception is an umbrella's `umbrella.md`, edited in place
after it lands until it closes (`docs/decisions/umbrellas.md`). In a pull
request, the operator is asked whether the files the branch adds to its
feature folder go in, told first that the branch's commits carry them
anyway and that leaving `open-items.md` out leaves the work left open
only in the branch's history: by the close readout where it recommends
a pull request, otherwise by finishing. An umbrella's own pull request
leaves `umbrella.md` off that list, so it stays in the merged tree
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
deletes it, the work left open written out first at the first two, a
discard aside; an umbrella's closing review keeps a workspace of its own
under the umbrella's slug, deleted once its findings are written
(`skills/redteaming/references/formats.md` § Feature workspace root and
layout). A workspace lost mid-feature restarts the in-flight phase from
the committed spec or plan and `git log`.

**What is committed.** A feature's committed record is its spec, its
plan, its open-items file and its commit messages. Nothing summarizes a
campaign or a feature into the repository, and nothing parses records
to assemble one: the open-items file lists work left open, each item
with its source, not what the feature did. The records' process rules
still bind, and their layout is guidance. The session transcripts hold
the raw records for as long as the host keeps them (`README.md` § What
it writes into your repository).

**Work left open.** What a phase leaves open travels to Finish in the
ledger: at the close that seeds it (the plan phase's, the folded
campaign's, or SDD Setup on the very-small lane), the controller also
seeds under `## Questions` what the brainstorm, the spec campaign and
the plan phase left open, each as `<phase>: <item> — carried`
(`skills/redteaming/references/plan-phase.md`). At Finish, after the
operator's answer to the close readout, the work left open (minors,
leads, questions, declined improvements, unruled asks, parked BLOCKER or
MAJOR findings with their rulings, and what earlier phases carried) is
written to `<feature-folder>/open-items.md`, each item with its source,
those the readout proposed to drop and the answer did not keep named
dropped, and committed on the branch; where nothing was left open, no
file is written. No item takes a ruling of its own. Where the project's
instructions name where open items go, they go there instead: an
in-repository home on the branch, or an outside tracker as the
instructions say, those being the operator's word for it; a mode that
commits no feature-folder files is such a case
(`docs/backlog/records-retention-config.md`). An umbrella, which has no
ledger, writes what its brainstorm and campaign left open to an
`open-items.md` in its folder at its landing, and its closing review
appends to it (`docs/decisions/umbrellas.md`). A deferral counts as
done only once it is in an open-items file or the home the instructions
name, or is named dropped; no item is left only in the workspace. In
this repository `AGENTS.md` keeps the default, an open item becoming a
backlog item on the operator's word, and has the controller check the
file against its no-local-context rule before committing it
(`crucible:subagent-driven-development § Finish`).

**Finish.** SDD Finish runs in a fixed order. Record checks come first,
then the close readout to the operator, the decision point: it lists
the work left open, each item with the controller's proposal to keep or
drop it, and ends with a recommendation, one of the options finishing
offers on that branch or more work, with its reason; recommending a
pull request, it also asks the feature folder's files question. The
controller waits for the answer. An answer that asks for more work, or
a ruling that opens a wave, reopens the loop first, and Finish restarts
at the record checks. An answer that chooses an integration option, or
that leaves the work in place and chooses none, runs in order: the
open-items file and the feature's mark in its umbrella, where an
umbrella names it, committed on the branch; the full suite or the
project's declared merge gate on that HEAD; deletion of
`.crucible/<slug>/` and nothing else; then finishing, which carries out
the answer without presenting its menu again and asks only what the
answer left open, or, where the answer chose no option, presents its
options with the recommendation. An answer that discards the work skips
the file and the suite; finishing's typed `discard` confirmation comes
before the workspace's deletion, and an answer whose discard is left
unconfirmed counts as one that chose no option. After loop activity
that follows an answer, a red suite's included, the next readout says
what changed, and the earlier answer stands only where nothing new was
left open. A red run is a BLOCKER for the branch-review loop, never
classified away; one the adjudicator dismissed is shown to the operator,
and an answer that accepts it lets finishing proceed past its suite
check (`crucible:subagent-driven-development § Finish`). Where no close
readout precedes finishing, as at an umbrella's landing or after a
standalone review, finishing presents its options with a recommendation.
Finishing accepts a full run on exactly the HEAD being integrated whose
output it can still show, and otherwise re-runs; it removes any
feature-folder files the answer leaves out of a pull request in a final
commit and re-runs the suite. In a pull request the repository's
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
feature's. (Basis: judgment, accepted by the maintainer.) An umbrella's
closing review, added on 2026-10-30, runs after that workspace and every
child's are gone, so it provisions one of its own under the umbrella's
slug, deleted once its findings are written
(`docs/decisions/umbrellas.md`). (Basis: judgment, accepted by the
maintainer.)

### What is committed

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

From 2026-10-30 a feature also commits its open-items file, which
reverses the position that its committed record was its spec, its plan
and its commit messages alone. The file is a list the controller writes
from the ledger as the operator's answer left it, not a summary parsed
from records, so the parser's cost does not return (§ Work left open).
(Basis: judgment, accepted by the maintainer.)

### Work left open

Until 2026-10-30 the close readout was the only hand-over of work left
open, and filing it was left to the operator or the repository's
conventions. The audit of the hypothesis-specs umbrella found what that
cost: in 4 of its 10 clusters of lost or unseen findings, findings
arrived after a batched landing approval, were handed over only in
chat, and were lost when Finish deleted the ledger
(`docs/decisions/evidence-and-findings.md` § The audit of the
hypothesis-specs umbrella). What earlier phases left open, such as work
a disposition sent to a follow-up outside the feature or a parked entry
the operator had not ruled on, had no carrier to Finish: the plan
phase's close seeded the ledger with routed items, contained amendments
and open premise asks only. (Basis: measured, for the audit, and by
reading the plan phase's close as it then stood, for the seeding.)

Where the work goes was settled in steps. The maintainer ruled out an
in-repository backlog as the default, "in-repo backlog is not a
universal pattern", and work left open was to be filed into the
project's own home for deferred work. That home was unknown to
crucible, and each spec round found holes in the rules for when filing
it was authorized and how long it was kept. The controller proposed a
file in the feature folder, which every project crucible runs in has;
the maintainer answered tentatively, "Possibly this by default,
overridable by instructions?", and after two further re-shapings left
the final form to the controller, which kept a default file overridable
only by instructions that name where open items go. (Basis: measured,
for the rounds' findings; the maintainer's preference, for no
project-specific home and, tentatively, for the override; judgment,
accepted by the maintainer, for the file, its final form a call the
maintainer left to the agent.)

Writing the file after the operator's answer lets the readout propose
keeping or dropping each item without a ruling per item, and lets the
file record the answer. The file is committed before the suite, as the
umbrella mark is, so the suite runs on the tree that lands. No review
reads it unless the loop reopens, so the readout lists every item, and
this repository has the controller check it against the
no-local-context rule. The commit adds a little work to every feature,
which word counts do not show. (Basis: judgment, accepted by the
maintainer.)

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
to 39 minutes in that day's lane runs. (Basis: external, for upstream;
judgment, accepted by the maintainer; measured, by the maintainer's
report, for the run times.)

The umbrella mark, added on 2026-10-27, comes before the suite so that
the suite runs on the tree that lands, mark included; a mark committed
after it would land untested. (Basis: judgment, accepted by the
maintainer.)

Until 2026-10-30 Finish ran the suite before the close readout and
deleted the workspace after it, and finishing then presented its menu
"exactly as written". The maintainer found that the flow "railroads
towards the merge very hard", while the close readout was already the
decision point in practice. It now comes before the suite, carries the controller's
recommendation, and waits for the answer; an answer asking for more
work reopens the loop before anything is written, deleted or run, and
finishing carries out the answer instead of asking again. Integration
stays the operator's decision: nothing lands, pushes, opens a pull
request or discards work without that answer. (Basis: the maintainer's
preference, for loosening the flow; judgment, accepted by the
maintainer, for its order.)

The order was written for answers that integrate. On a discard, it
would have deleted the workspace before finishing's typed `discard`
confirmation, and a discard never confirmed would have left the work
left open nowhere durable. A task review in the feature that wrote the
order found this; the controller ruled that the confirmation comes
before the deletion and that an unconfirmed discard counts as an answer
that chose no option, so Finish resumes at the open-items file and the
suite. (Basis: judgment, a controller's ruling within that feature, on
a conflict its task review found.)

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
  rarely read, and costly to keep parsing open input (§ Why). The
  open-items file is no such summary.
- **The close readout as the only hand-over of work left open**, with
  filing left to the operator or the repository's conventions: work
  handed over only in chat was lost (§ Why).
- **Filing work left open into a project's own home by default**, such
  as an in-repository backlog: not every project has one, and its rules
  for authorizing and keeping a filing never held up in review (§ Why).
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
- Where open items go, named in its instruction files: an
  in-repository home on the branch, or an outside tracker as the
  instructions say; a mode committing no feature-folder files is such a
  case.

## Changes

- 2026-10-30: the close readout is Finish's decision point, before the
  suite: it lists the work left open with a keep-or-drop proposal for
  each item and recommends one of finishing's options or more work; the
  answer's integration runs the open-items file and the umbrella mark,
  the suite, deletion and finishing, which carries the answer out
  instead of presenting a fixed menu; a discard takes finishing's typed
  confirmation before deletion, an unconfirmed one counting as no
  option chosen. Work left open is written to the feature folder's
  `open-items.md` unless the project's instructions name another home,
  and what earlier phases left open reaches Finish through the ledger;
  this reverses the close readout as the only hand-over, filing left to
  the operator, and a committed record of spec, plan and commits alone.
  An umbrella's closing review keeps a workspace of its own. The
  maintainer found finish too rigid, and the audit of the
  hypothesis-specs umbrella found work handed over in chat lost.
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
