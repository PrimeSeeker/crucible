# Task: write per-file compaction briefs

Workspace: `<workspace>/` (WS below). Repo root: the repository root.

A per-file pipeline will rewrite each skill file for density: several writers with different framings, blind inventory checks, a synthesizer, blind verification, behavioural QA. Each unit's writers read three things: the file, `WS/style.md` (cut patterns and "What not to cut") and that file's **brief**, which you write. The brief is the only place the writers learn the cross-file rulings that touch their file; anything a ruling asks for that is not in the brief will not happen, and anything you put in the brief that no ruling asks for may cause a loss.

## Read first

1. `WS/brief-common.md` (the goal and constraints).
2. `WS/decisions.md`: the controller's rulings. Rejected clusters must not appear in any brief as instructions (you may tell writers to keep what a rejected cluster would have cut).
3. `WS/decisions-draft.md`: every cluster C1–C49 (what, saving, loss, risk). The structural clusters (C1, C2, C4, C5, C6, C7(1)-(3), C9, C10–C15 splits/moves, C17, C18, C20, C21, C22, C43 part F, C33 part O, C35's move) are ALREADY DONE in the tree by commits on branch prose-compaction (`git log master..HEAD` from the repo root). What remains for the per-file pass: the line-edit parts of C14 and C15, C16, C19, C30–C46 (except the parts already done), C47(a), C48 (a writer rule), C49 (the target form for loop prose in C34/C45). Read each cluster's text and work out, per file, what it asks of that file in the tree as it stands now (line numbers in the draft are stale: the structural steps moved text; find the passage by content).
4. `WS/style.md` (so you don't repeat it in briefs).
5. `WS/structural-journal.json`: per step, the implementer's and fixer's `deviations` and `defects`, and the reviewers' findings. Some are addressed to "the per-file pass" or "the controller"; carry each such item into the brief of the file it concerns. Known ones: `skills/subagent-driven-development/references/setup.md` now carries a copy of using-git-worktrees' Step 2 setup table, so C43's table replacement must be applied identically in both files (name the pair in both briefs); `skills/redteaming/references/panels.md` and `plan-phase.md` still say "filled slot card" (pre-C5 wording: since C5 the seat gets the card's filled Slots and Selectors); `skills/subagent-driven-development/references/review-terms.md`'s preamble says templates take its sections by splice, loose since C4(b).
6. `docs/authoring.md` § Paired texts: for each file in a pair, the brief names the other side and says the paired statement must stay consistent with it (the pipeline rewrites files independently; tell writers to keep the paired statement's content and wording close to the original so the integration step can reconcile).

## Controller additions (put in the named briefs)

- C7(3) loss repair: at each site where a controller enters an operator's ruling in `brainstorm-decisions.md` (SDD `SKILL.md`, `references/very-small-lane.md`, requesting-code-review `SKILL.md`, and any other site you find with that wording), the brief asks to keep or add the pointer `(status: \`crucible:brainstorming\` § Workspace provisioning)` or an equally short equivalent, since the status rule ('firm' only on the operator's explicit word) is otherwise unreachable from there.
- The three files `skills/using-crucible/references/codex-dispatch.md`, `skills/using-crucible/references/claude-code-dispatch.md` and `skills/subagent-driven-development/references/dispatch-composition.md` are being edited right now by structural step C3 (Codex seats read their template by path). Write their briefs anyway, noting at the top: "C3 has changed how a Codex seat gets its template; keep the C3 wording's content."
- Pilot finals for `skills/finishing-a-development-branch/SKILL.md` and `skills/redteaming/references/panels.md` exist in `WS/units/` but predate the structural steps; ignore them.
- Rationalization tables (C16): name in the brief which rows to keep (destructive-action guards; rows with recorded evidence: `docs/decisions/worktrees.md`'s measured rows etc.) and which go (rows whose Reality restates a body rule and carry no recorded catch). Search docs/decisions for each row's evidence before marking it for deletion. The router's (using-crucible) Red Flags table is KEPT whole.

## What a brief holds

Format (see `WS/briefs/systematic-debugging__SKILL.md` for one written earlier):

```
# Unit brief

<one line: what this file is, who reads it and when (controller at which step / which seat / every session), from resident-tokens.json and the citers in corpus-map.json>

Rulings for this file:
- <each concrete instruction, citing its cluster id: what to cut, merge, move out or keep>

Keep (beyond style.md's list): <file-specific musts: text tests read, paired statements, headings cited elsewhere that the checker might not see, rules a ruling explicitly keeps>

Cross-file: <paired texts and the other side's path; text another file restates that this file should now only point at, or vice versa>

Write one paragraph or list item per line.
```

Keep briefs short (most 40–150 words; a heavily ruled file may need more). Name rulings, not wording. No rule a ruling does not ask for. Where no cluster touches a file, the brief says "No cross-file ruling touches this file; apply style.md." plus the who-reads-it line and any Keep items.

## Output

Write each brief to `WS/briefs/<slug>.md`, slug = the repo path without `skills/` and `.md`, with `/` replaced by `__` (e.g. `skills/redteaming/references/panels.md` → `redteaming__references__panels.md`). Overwrite the two pilot briefs for finishing and panels. Then write `WS/briefs-<your group>-notes.md` listing: each brief written; each cluster part you could not place in any file (with why); anything in the rulings you judge contradictory or risky.

## Constraints

Read-only on the repository: no edits outside `WS/briefs/` and your notes file, no git command that changes anything. Another agent is committing a structural step in the same worktree as you work; ignore its changes except for the three C3 files above. Run `git status --short` (repo root) at your start and end and report both outputs. Start no agents. Publish nothing. Call no model API.

Your final message: the list of briefs written, and your notes file's path.
