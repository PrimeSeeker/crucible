# Records and workspace

## Decision

**The feature folder.** A feature commits its spec and, on the standard
route, its plan in one feature folder, `docs/crucible/<YYYY-MM-DD>-<slug>/`
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
anyway: by the close readout where it recommends
a pull request, otherwise by finishing. An umbrella's own pull request
leaves `umbrella.md` off that list, so it stays in the merged tree
(`crucible:finishing-a-development-branch § Step 5: Execute Choice`).

**The workspace.** A feature's process records (the quoted request, round
records, seat reports, the execution ledger, scratch) live in
`.crucible/<slug>/` at the root of the checkout the controller works in. It ignores itself through a
`.crucible/.gitignore` holding `*`, written by a prose provisioning step
and confirmed with `git check-ignore` on a file path
(`skills/redteaming/references/formats.md` § Feature workspace root and
layout); no host `.gitignore` is edited. Nothing in it is committed or
archived, and `.crucible/` holds workspaces only. SDD Setup looks for the
workspace before its worktree and provisioning steps, and continues in
the checkout that holds it. A workspace's life has three ends, SDD
Finish, an umbrella's landing and the feature's abandonment, and each
deletes it, at the first two only once the work left open has gone to
its home or been dropped, a discard aside; an umbrella's closing review
keeps a workspace of its own under the umbrella's slug, deleted on the
same condition (`skills/redteaming/references/formats.md` § Feature
workspace root and layout, § Open items). A workspace lost mid-feature
restarts the in-flight phase from the committed spec or plan and
`git log`.

**What is committed.** A feature's committed record is its spec, its
plan and its commit messages, and its open items where the project's
home for them is in the repository. Nothing summarizes a campaign or a
feature into the repository, and nothing parses records to assemble
one: open items list work left open, each with its source, not what the
feature did. The records' process rules
still bind, and their layout is guidance. The session transcripts hold
the raw records for as long as the host keeps them (`README.md` § What
it writes into your repository).

**Work left open.** What a phase leaves open travels to Finish in the
ledger: at the close that seeds it (the plan phase's, the folded
campaign's, or SDD Setup on the very-small lane), the controller also
seeds under `## Questions` what the brainstorm, the spec campaign and
the plan phase left open, each as `<phase>: <item> — carried`, apart
from `deferred-minor` entries, which go under `## Deferred minors` for
the branch review's triage (`docs/decisions/branch-review.md`;
`skills/redteaming/references/plan-phase.md`); SDD's Setup seeds any
such item, entry or open premise ask that the ledger lacks. Crucible
keeps no store of its own for open items. At Finish, after the operator's answer
to the close readout, the work left open (minors, leads, questions,
declined improvements, unruled asks, parked BLOCKER or MAJOR findings
with their rulings, and what earlier phases carried) goes, each item
with its source, to the home the project's instructions name for open
items: an in-repository home written and committed on the branch, or an
outside tracker as the instructions say, those being the operator's word
for it. Where they name none, the close readout asks the operator where
the items go or whether to drop them, and offers to record the answer
in an instruction file the operator picks, committed in the project or
private and uncommitted, so that the question does not recur; the
workspace is not deleted before that answer, so a session that ends
unanswered returns to the question. Items the answer drops go nowhere,
the readout having named them; where nothing was left open, nothing is
asked or written. No item takes a ruling of its own. An umbrella, which
has no ledger, sends what its brainstorm and campaign left open the same
way at its landing, its campaign's `deferred-minor` entries and the
decision asks still unruled there, premise asks aside, among them, the
landing ask carrying the question, and its
closing review sends the findings kept the same way
(`docs/decisions/umbrellas.md`). A deferral counts as done only once it
is in the home or dropped; no item is left only in the workspace
(`skills/redteaming/references/formats.md` § Open items;
`crucible:subagent-driven-development § Finish`). Brainstorming's
context gathering reads the home for open items touching the area,
which is what makes them found again (`crucible:brainstorming § Context
gathering (before any question)`). This repository's
`AGENTS.md` names `docs/backlog/` as its home, and has the controller
check open items against its no-local-context rule before committing
them.

**Finish.** SDD Finish runs in a fixed order. Record checks come first,
then the close readout to the operator, the decision point: it lists
the work left open, each item with the controller's proposal to keep or
drop it, and ends with a recommendation, one of the options finishing
offers on that branch or more work, with its reason; recommending a
pull request, it also asks the feature folder's files question. The
controller waits for the answer. An answer that asks for more work, or
a ruling that opens a wave, reopens the loop first, and Finish restarts
at the record checks. Where the readout asked where open items go,
nothing below runs until the answer says or drops them. An answer that
chooses an integration option, or that leaves the work in place and
chooses none, runs in order: the open items and the feature's mark in
its umbrella, where an umbrella names it, those in the repository
committed on the branch; the full suite or the
project's declared merge gate on that HEAD; deletion of
`.crucible/<slug>/` and nothing else; then finishing, which carries out
the answer without presenting its menu again and asks only what the
answer left open, or, where the answer chose no option, presents its
options with the recommendation. An answer that discards the work skips
the open items, which go with it, and the suite; finishing's typed `discard` confirmation comes
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
slug, deleted once its findings have gone to their home or been
dropped (`docs/decisions/umbrellas.md`). (Basis: judgment, accepted by the
maintainer.)

The operator's request joined the workspace on 2026-11-01, as
`request.md`, after quoting it in committed feature folders published the
operator's messages: the workspace is uncommitted, reaches seats by path
and lives past the branch review, the last seat that reads the request
(`docs/decisions/the-spec.md`). (Basis: judgment, accepted by the
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

From 2026-10-30 to 2026-11-01 a feature also committed an open-items
file in its feature folder; since then it commits its open items only
where the project's home for them is in the repository. Either way they
are a list the controller writes from the ledger as the operator's
answer left it, not a summary parsed from records, so the parser's cost
does not return (§ Work left open). (Basis: judgment, accepted by the
maintainer, the list's final form a call the maintainer left to the
agent.)

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
accepted tentatively by the maintainer, for the file, its final form a
call the maintainer left to the agent.) At the close readout of the
feature that set this default (2026-10-30), the maintainer said of
the file: "In retrospect, open items stored like this are
definitely going to be lost. Backlog, please, we'll find a better
location later." The maintainer sent that feature's work left open to
the backlog and left the default to be changed later. (Basis: the
maintainer's preference.)

The maintainer's brainstorm of 2026-11-01 settled it. A discoverable
default was sought first: an in-repository backlog is this repository's
own feature, which other projects may not want in their tree, and the
maintainer proposed the host's memory but doubted that it fits Codex,
whose memory is per user rather than per project. The maintainer then
proposed no default at all: keep the items in the workspace and ask the
operator, insistently, before its deletion where no home is configured.
A session that ends
unanswered leaves the workspace, so the question returns on its own; a
workspace deleted by a request outside the flow is not worth covering.
This repository names `docs/backlog/` as its home, as the maintainer had
asked for at the earlier close readout. (Basis: the maintainer's
preference.) The offer to record the answer in an instruction file, so
the question does not recur, and brainstorming reading the configured
home, so the items are found again, were the controller's proposals,
which the maintainer agreed to. (Basis: judgment, accepted by the
maintainer.)

Sending the items after the operator's answer lets the readout propose
keeping or dropping each item without a ruling per item. Items the
answer drops are not written: a project's home holds work still to do,
and the readout has named each one. (Basis: judgment, accepted by the
maintainer at that feature's close readout: the implementer's call, in
the feature that removed the default file, reading the Intent that open
items end in the project's home or the operator's drop.) Items in an in-repository home
are committed before the suite, as the umbrella mark is, so the suite
runs on the tree that lands. No review reads them unless the loop
reopens, so the readout lists every item, and this repository has the
controller check them against the no-local-context rule. The commit
adds a little work to every feature, which word counts do not show.
(Basis: judgment, accepted by the maintainer: writing after the answer,
the order and the commit before the suite, a call the maintainer left
to the agent.)

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
that chose no option, so Finish resumes at the open items and the
suite. (Basis: judgment, an agent's call the maintainer has not ruled
on: a controller's ruling within that feature, on a conflict its task
review found.)

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
  rarely read, and costly to keep parsing open input (§ Why). Open items
  are no such summary.
- **The close readout as the only hand-over of work left open**, with
  filing left to the operator or the repository's conventions: work
  handed over only in chat was lost (§ Why).
- **A default home for work left open that crucible picks**: a
  project's own, such as an in-repository backlog, which not every
  project has or wants; an `open-items.md` in the feature folder, which
  the maintainer judged would be lost; or the host's memory, which on
  Codex is per user rather than per project (§ Why).
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
  instructions say. With none named, the operator is asked each time
  open items leave a workspace.

## Changes

- 2026-11-02: an umbrella's landing sends its campaign's
  `deferred-minor` entries and its decision asks still unruled, premise
  asks aside, with the work left open, since it has no ledger or branch
  review to take them (`docs/decisions/umbrellas.md`).
- 2026-11-02: what earlier phases left open no longer includes
  `deferred-minor` entries, which the close that seeds the ledger seeds
  under `## Deferred minors` for the branch review's triage; because
  that triage judges each against the code
  (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-01: the workspace holds the quoted request, `request.md`,
  written at brainstorm exit and deleted with the workspace; because
  quoting it in committed feature folders published the operator's
  messages.
- 2026-11-01: crucible keeps no store of its own for open items. They
  go to the home the project's instructions name or, with none named,
  where the operator's answer sends them, the readout offering to
  record that answer in an instruction file and the workspace kept until
  it comes; items the answer drops are not written; brainstorming reads
  the home; this repository names `docs/backlog/`. The maintainer's
  brainstorm resolved the 2026-10-30 view that the feature folder's
  `open-items.md` would be lost, and that default file is retired. At
  its close readout the maintainer accepted that dropped items are not
  written, and a home recorded in a user-level file counts as named.
- 2026-11-01: § Work left open names the maintainer's 2026-10-30 view
  that open items kept in the feature folder's file will be lost, and
  points to the backlog item that held the question; the file's basis
  reads accepted tentatively. The record had given the default as
  accepted without the maintainer's later doubt.
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
  hypothesis-specs umbrella found work handed over in chat lost. SDD's
  Setup seeds a carried item or open premise ask the ledger lacks; the
  file's order and pre-suite commit are attributed to the delegated
  final form, and the discard ruling's basis is labelled an agent's
  call the maintainer has not ruled on.
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
