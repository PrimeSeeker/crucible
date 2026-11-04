# Crucible formats reference

File and directory names here are fixed: consumers depend on them. Content marked *advisory* (the `sdd/` internal shape) may be refined by its implementer, logging the decision.

## Feature workspace root and layout

One workspace per feature, at `<repo>/.crucible/<feature-slug>/`, where `<repo>` is the root of the checkout the controller session works in (typically the feature worktree) and `<feature-slug>` matches `[a-z0-9]+(-[a-z0-9]+)*`; the slug also names the feature folder (§ Feature folder). The spec campaign, the plan phase and SDD share it.

**Provisioning (binding)** creates a feature's workspace; re-running it changes nothing.

1. Create `.crucible/<feature-slug>/` at the checkout root (`git rev-parse --show-toplevel`).
2. If `.crucible/.gitignore` is absent, write it holding the single line `*`, as UTF-8, with your file-writing tool, never a shell redirect: Windows PowerShell 5.1's `>` writes UTF-16LE, which git does not read. Never overwrite an existing one, whatever it holds.
3. From the checkout root, run `git check-ignore -q .crucible/<feature-slug>/probe` (the path need not exist). Exit 0 confirms the workspace is ignored; report any other result to the operator. Check a file path, never the directory: against a UTF-16LE `.gitignore` the directory form still exits 0.

No host `.gitignore` is ever edited: the operator owns those.

Gitignored files do not propagate across worktrees, so the workspace lives in one checkout: dispatch prompts pass its absolute path, and anything agents in other checkouts must read (the spec, the plan) is committed, never workspace-only. No step of crucible's flow commits anything in the workspace.

**Layout:**

```
<repo>/.crucible/
  .gitignore
  <feature-slug>/
    brainstorm-decisions.md
    request.md
    tree-check.txt
    campaigns/
      spec/
        round-00/
        round-01/ ... round-NN/
        terminal-pass/
      plan/
        round-01/
    sdd/
      ledger.md
      reports/
      branch-review/
        pass-<k>.md
        pass-<k>-r<R>.md
    sdd-lane/
    scratch/
```

A round directory's contents and record: `skills/redteaming/references/round-record.md`. The other `sdd/` report names are fixed in `crucible:subagent-driven-development` § Finish.

**Later operator rulings enter the decision record (binding).** Every operator ruling on a decision ask after the brainstorm is also entered in `brainstorm-decisions.md`, in that record's entry form (`crucible:brainstorming` § Workspace provisioning) and with its status, besides wherever its own phase records it.

**Later changes to the ask enter `request.md` (binding).** While the workspace lives, the controller appends to it, quoted verbatim, each operator message after brainstorm exit that changes what was asked.

**A report the controller saved carries a mark (binding):** it is the returned text unchanged, under a first line saying the controller saved it and why; saved to an appended report it is appended, the mark opening its section. The `sdd/` files the controller writes by rule (the very-small lane's `wave-<n>-fix.md`, inline mode's report) are its own and carry none.

**Lifecycle (binding):** provisioned at brainstorm exit; lives until SDD Finish, an umbrella's landing, or abandonment, the operator's call (a late split's included) on a readout listing what the records hold open. At each end the controller deletes `.crucible/<feature-slug>/` and nothing else, and reports what it could not delete. An umbrella's closing review has its own workspace, under the umbrella's slug, deleted once its findings have left (§ Open items). No orphan workspaces. Workspace lost mid-feature: the in-flight phase restarts from the committed spec or plan and `git log`.

## Feature folder

**Feature folder (binding):** each feature's committed documents, its spec and plan, live together in one tracked directory of the target repo, `<root>/<YYYY-MM-DD>-<feature-slug>/`. `<root>` is `docs/crucible` unless the project's instruction files name another. The date is the day brainstorming first writes the spec, before provisioning; the slug is the workspace slug.

**Files named by role (binding)**, the folder carrying slug and date:

- Exactly one *current* spec, named by its kind: `design.md` (standard route), `folded.md` (folded spec+plan), `note.md` (very-small lane) or `umbrella.md` (umbrella).
- `plan.md`, on the standard route only.
- A route that replaces a spec keeps the predecessor in place as the forensic record and writes the successor into the same folder: a supersede successor takes a numeric suffix (`design-2.md`, `plan-2.md`, …); an unfold leaves `folded.md` beside its `design.md` and `plan.md` successors, and the very-small lane's upgrade hatch leaves `note.md` beside them.
- Other feature-scoped documents may live there, under descriptive names.

**Birth and resolve; a slug names one feature (binding):** two steps find a feature's folder, and both match a directory under `<root>` named exactly `YYYY-MM-DD-<feature-slug>`: a date of that shape, then the whole slug. A `*-<feature-slug>` glob is not that match: `*-diet` also matches `2026-09-27-cost-diet`.

- **Birth** (brainstorming, on first writing the spec): list `<root>`; if no directory matches, create `<root>/<today>-<feature-slug>/` (local date). If one does, refuse and tell the operator: a new feature never resolves into a finished feature's folder, and takes a new slug.
- **Resolve** (every other consumer: a resumed brainstorm, the plan, a successor spec, dispatches): find the one matching directory, creating nothing; report none or several to the operator.
- Nothing but the birth creates a feature folder.

## Open items

This section binds. Crucible keeps no store of its own for open items, the work left open. They leave the workspace at SDD's Finish, an umbrella's landing and an umbrella's closing review, each with its source; an item the operator's answer drops goes nowhere, the readout having named it. Where nothing was left open, nothing is asked or written.

- **The project's instructions name a home** (a user-level file's line naming the project counts): items go there, an in-repository home's items committed on the branch the step names, an outside tracker used as the instructions say.
- **They name none:** the readout listing the items asks the operator where they go or whether to drop them, and offers to record the answer in an instruction file the operator picks (committed in the project or private and uncommitted; your runtime reference names them), so the question does not recur; a line in a user-level file names its project. The answer's home is then used as a named one; a line recorded in a committed file is committed with the items.

**Deletion waits (binding).** A workspace holding open items is not deleted until they have gone to their home or been dropped; discarding the work drops them. A session that ends before the answer leaves the workspace in place, and the next returns to the question.
