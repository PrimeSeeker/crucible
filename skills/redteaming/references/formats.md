# Crucible formats reference

What a controller or seat writes and reads, defined once so writers and readers are built against one text: the feature workspace and the feature folder. Provisioning the workspace and finding the feature folder are steps stated here.

Field lists are binding where their section does not say otherwise, and file
and directory names are fixed: consumers depend on them. Content marked *advisory* may be refined by its implementer
with a logged decision.

## Feature workspace root and layout

**Root convention:** one workspace per feature at

```
<repo>/.crucible/<feature-slug>/
```

where `<repo>` is the root of the checkout the controller session works in
(typically the feature worktree) and `<feature-slug>` matches
`[a-z0-9]+(-[a-z0-9]+)*`; the slug also names the feature folder (§ Feature
folder).

**Self-ignition:** whoever creates `.crucible/` first also writes
`.crucible/.gitignore` containing exactly `*`. No host
`.gitignore` is ever edited: host gitignores are operator-owned.

**Provisioning (binding):** the step that creates a feature's workspace.
Re-running it on an existing workspace changes nothing.

1. Create `.crucible/<feature-slug>/` at the root of the checkout
   (`git rev-parse --show-toplevel`).
2. If `.crucible/.gitignore` is absent, write it holding the single line
   `*`, as UTF-8, with your file-writing tool and never a shell redirect:
   Windows PowerShell 5.1's `>` writes UTF-16LE, which git does not read.
   An existing one is never overwritten, whatever it holds.
3. From the checkout's root, run
   `git check-ignore -q .crucible/<feature-slug>/probe` (the path need
   not exist). Exit 0 confirms the workspace is ignored; report any other
   result to the operator. Check a file path, never the directory: against
   a UTF-16LE `.gitignore` the directory form, `.crucible/<feature-slug>/`,
   still exits 0.

Gitignored files do not propagate across worktrees, so the workspace lives in
one checkout: dispatch prompts pass its absolute path, and anything agents in
*other* checkouts must read — the spec, the plan — is committed to the repo,
never workspace-only. Nothing in the workspace is committed by any step of
crucible's flow.

**Layout** (the spec campaign, the plan phase and SDD share one
workspace):

```
<repo>/.crucible/
  .gitignore                  # exactly "*" — self-ignition
  <feature-slug>/             # the feature workspace
    brainstorm-decisions.md   # brainstorm decision record, the gate entry
                              #   included (crucible:brainstorming)
    request.md                # the request, quoted (crucible:brainstorming);
                              #   the goal check reads it
    tree-check.txt            # HEAD and status output at the latest window,
                              #   overwritten at each; the status check reads
                              #   it (subagent-driven-development's
                              #   dispatch-composition.md
                              #   § Shared-tree rules)
    campaigns/
      spec/                   # the spec campaign
        round-00/             # round 0 mechanical pre-pass (consumes no cap round)
        round-01/ ... round-NN/
        terminal-pass/        # terminal pass (consumes no cap round)
      plan/                   # the plan phase: round-01 only, no round-00 and
                              #   no terminal-pass/ — its pass reports into round-01/
    sdd/                      # SDD execution records (internal shape advisory)
      ledger.md
      reports/
      branch-review/          # pass-<k>.md per full-scope pass, pass-<k>-r<R>.md
                              #   for a replacement seat's
    sdd-lane/                 # a very-small lane's sdd/, moved aside at its
                              #   upgrade hatch
    scratch/                  # what read-only agents build or run to check
                              #   claims, one subdirectory per report;
                              #   deleted with the workspace
```

What a round directory under `campaigns/` holds and its record's shape: `skills/redteaming/references/round-record.md`.

The other report names under `sdd/` — review, re-review, fix and adjudication
reports — are fixed in `crucible:subagent-driven-development` § Finish.

**Later operator rulings enter the decision record (binding).** Every
operator ruling on a decision ask after the brainstorm — in a campaign, the
plan phase or execution — is also entered in `brainstorm-decisions.md`, in
that record's entry form (`crucible:brainstorming` § Workspace provisioning)
and with its status, beside wherever its own phase
records it.

**Later changes to the ask enter `request.md` (binding).** While the
workspace lives, the controller appends to it, quoted verbatim, each
operator message after brainstorm exit that changes what was asked.

**A report the controller saved carries a mark (binding).** Every report
file an instrument or seat owes — a round's `seat-<id>.md`, `verifier.md`,
`terminal-pass.md`, `pass.md` and `second-read.md`, and the reports SDD's
seats write under `sdd/` — is written by its author. The controller writes
one itself in two cases only: the host refused the write and the seat
returned the report as text; or the seat returned it as text without writing
it or reporting a refusal, and one resume left no file. It then writes the
returned text unchanged under a first line saying the controller saved it
and why, so whoever reads the workspace can tell the seat's text from text
the controller transcribed. The `sdd/` files the controller writes by rule —
the very-small lane's `wave-<n>-fix.md`, inline mode's report — are its own
and carry no mark.

**Lifecycle** (binding): provisioned at brainstorm exit; lives until one of
three ends — SDD Finish, an umbrella's landing (an umbrella never reaches
SDD), or feature abandonment. At each, the controller deletes
`.crucible/<feature-slug>/` and nothing else, and reports to the operator
anything it could not delete. No item left open stays only in the
workspace: at Finish and at an umbrella's landing, the deletion waits
until the work left open has gone where § Open items sends it, in the
order `crucible:subagent-driven-development` § Finish or
`skills/brainstorming/references/umbrellas.md` § Landing gives; at
abandonment, the operator's call (a late split's included), the readout
asking for it lists what the records hold open. An umbrella's closing
review has a workspace of its own under the umbrella's slug, in the
checkout the session works in, deleted once its findings have gone where
§ Open items sends them (`skills/brainstorming/references/umbrellas.md`). No orphan workspaces. Workspace lost mid-feature: the in-flight phase restarts
from the committed spec or plan and `git log`; the session transcripts hold
the lost records if they are needed.

## Feature folder

This section is the binding definition of where a feature's committed
documents live — its spec and its plan.

**Feature folder (binding):** each feature's committed documents live
together in one tracked directory of the target repo, the feature's
*feature folder*:

```
<root>/<YYYY-MM-DD>-<feature-slug>/
```

`<root>` is `docs/crucible` by default; a root the project's instruction
files name overrides this default. The date is the day brainstorming first
writes the spec, before provisioning; `<feature-slug>` is the workspace slug
(§ Feature workspace root and layout).

**Files named by role (binding):** the folder carries the slug and the date,
so a filename carries only its role.

- Exactly one *current* spec, named by its kind: `design.md` (standard
  route), `folded.md` (the folded spec+plan), `note.md` (the very-small lane)
  or `umbrella.md` (an umbrella, `skills/brainstorming/references/umbrellas.md`).
- `plan.md`, on the standard route only.
- A route that replaces a spec keeps the predecessor in place as the
  forensic record and writes the successor into the same folder: a supersede
  successor takes a numeric suffix (`design-2.md`, `plan-2.md`, …); an
  unfold leaves `folded.md` beside its `design.md` and `plan.md` successors,
  and the very-small lane's upgrade hatch leaves `note.md` beside them.
- Other feature-scoped documents may live in the folder under descriptive
  names.

**Birth and resolve; a slug names one feature (binding):** two steps find
a feature's folder, and both match a directory under `<root>` named
exactly `YYYY-MM-DD-<feature-slug>`: a date of that shape, then the whole
slug, so slug `diet` never matches `2026-09-27-cost-diet`. A
`*-<feature-slug>` glob is not that match: it also matches
`2026-10-11-bar-<feature-slug>`.

- **Birth** — brainstorming, when it first writes the spec. List
  `<root>`. Where no directory there is named exactly
  `YYYY-MM-DD-<feature-slug>`, create `<root>/<today>-<feature-slug>/` (local
  date). Where one is, refuse and tell the operator: a new feature
  never resolves into a finished feature's folder, so it takes a new slug.
- **Resolve** — every other consumer: a resumed brainstorm, the plan, a
  successor spec, dispatches. Find the one directory under `<root>`
  named exactly `YYYY-MM-DD-<feature-slug>`, creating nothing. None, or more
  than one, is reported to the operator.
- Nothing but the birth creates a feature folder, so a feature never has a
  second home.

## Open items

The binding definition of where the work left open goes. Crucible keeps no store of its own for it. Open items leave
the workspace at SDD's Finish, an umbrella's landing and an umbrella's
closing review, each with its source; an item the
operator's answer drops goes nowhere, the readout having named it.
Where nothing was left open, nothing is asked or written.

- **The project's instructions name a home for open items** (here and
  wherever the skills name them, a user-level file's line naming the
  project counts): they go
  there, an in-repository home committed on the branch the step names,
  an outside tracker used as the instructions say.
- **They name none:** the readout listing the items asks the operator
  where they go, or whether to drop them, and offers to record the answer
  in an instruction file the operator picks (your runtime reference names
  them), committed in the project or private and uncommitted, so the
  question does not recur; a line in a user-level file names its
  project. The home the answer names is then used as a named one; a
  line recorded in a committed file is committed with the items.

**Deletion waits (binding).** A workspace holding open items is not
deleted until they have gone to their home or been dropped, a discard of
the work dropping them; a session
that ends before the answer leaves it, and the next returns to the
question.
