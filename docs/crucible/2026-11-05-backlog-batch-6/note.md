Lane: very-small (operator-confirmed 2026-11-05)

# Backlog batch 6

## Intent

Clear the backlog points whose fix is stated and needs no evidence from a real run:

- from `skill-text-rewrite`: the wording points, the undefined "phase's final check", the wrong ground of a retired trigger, the report form of an umbrella's closing-review seats, and the terminal pass's read scope;
- `writing-skills-followups`, `repo-conventions-at-setup`, `declared-worktree-directory-residuals`;
- the own-entry clause missing from `review-terms.md`, and `record-wording-slips`.

The minors policy the operator accepted applies: fix a minor only if it could lose a record or sits on a path that has actually run; file the rest.

No break: a not-ignored worktree directory is now excluded locally where a commit went through, and nothing the base does stops working.

## Change list

1. `skills/using-crucible/SKILL.md` § Decision asks: where a message to the operator carries other content, its decision asks come last, in a block of their own. The restatement in `skills/redteaming/references/round-readout.md` and the pointers to it in `skills/brainstorming/SKILL.md` and `skills/brainstorming/references/umbrellas.md` go.
2. `skills/subagent-driven-development/references/finish.md` step 2: the recommendation is the final block's last item, resolving "final block" against "last".
3. No change for "proposing no preset": `very-small-lane.md` § The upgrade hatch states it where the controller acts, and its route entry says the operator chose to move.
4. `skills/redteaming/references/round-record.md`: "the phase's final check" goes, at both sites, since nothing defines it.
5. `docs/decisions/authoring-crucible.md`: the trigger's retirement no longer says growth is held word by word by the prose budget, which records growth and refuses none; a Changes line.
6. `skills/brainstorming/references/umbrellas.md` § Closing review: the seats' prompts carry a report form.
7. `skills/redteaming/terminal-pass-prompt.source.md`: read scoping admits the files a claim the pass checks cites; templates regenerated.
8. `skills/writing-skills/compacting.md` step 4: the loop ends only when no addition that adds or changes a rule stands.
9. `skills/writing-skills/SKILL.md`: a micro-test's sample on a realistic task needs no announcement; the no-guidance run on Codex is the same task where the skill is not installed.
10. `skills/using-git-worktrees/SKILL.md`: before the feature's first commit, on any path through the skill, read what the repository says shapes a commit. `docs/decisions/records-and-workspace.md` follows.
11. `skills/using-git-worktrees/references/git-fallback.md`: a not-ignored directory is reported from any checkout, and nothing is committed. `skills/finishing-a-development-branch/SKILL.md` Step 6 also removes a worktree under the declared directory. `docs/decisions/worktrees.md` follows.
12. `skills/subagent-driven-development/references/review-terms.md` § What binds in a spec takes the own-entry clause; `docs/decisions/evidence-and-findings.md` names where a closing-review seat's questions go; `docs/decisions/umbrellas.md`'s Changes line says "conflicts".
13. Backlog: delete `writing-skills-followups.md`, `repo-conventions-at-setup.md`, `declared-worktree-directory-residuals.md` and `record-wording-slips.md`; remove the done points from `skill-text-rewrite.md` and `umbrella-followups.md`.

## Acceptance

- `python -m pytest tests/` passes; `python tools/instrument_agents.py check` exits 0.
- A one-time text check confirms each change above at its site, having failed on the tree before the change.

## Out of scope

The other points of `skill-text-rewrite.md` (separability, tension-closing, umbrella landings, the plugin-root exception) and of `umbrella-followups.md`; `small-wave-full-pass`, which comes next as its own feature.
