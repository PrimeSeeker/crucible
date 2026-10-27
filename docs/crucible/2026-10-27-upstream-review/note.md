Lane: very-small (operator-confirmed 2026-10-27)

# Upstream review to v7.0.1, and the defects it found

## Intent

Record the review of superpowers v6.2.0 → v7.0.1 and the maintainer's
rulings on it, and fix the defects it found that crucible still carries:

- `find-polluter.sh` cannot run as documented: it is stored without the
  executable bit, and `./find-polluter.sh` resolves against the user's
  project, not the skill;
- `root-cause-tracing.md` contradicts itself on a trace that dead-ends
  ("Fix at symptom point" in one diagram, "NEVER fix just the symptom" in
  the other);
- the session-start hook runs `cat` from `PATH`: with an empty `PATH` the
  router does not load, and a `cat` in the working directory runs at
  session start;
- the Claude Code host map says the host reads only `CLAUDE.md`; since
  v2.1.277 it reads `AGENTS.md` where no `CLAUDE.md` exists;
- `codex-dispatch.md` states, unmeasured, that a full-history fork
  inherits model and effort; upstream's source reading says the opposite,
  and crucible never forks with history;
- the review seats check that each end of their range is a commit, not
  that the base is an ancestor of the head.

## Change list

- The feature folder holds `dispositions.md`: the merged table, one row
  per upstream change with its disposition and reason, and the
  maintainer's rulings of 2026-10-27.
- `docs/upstream.md`: last fully reviewed version v7.0.1; upstream paths
  at v7.0.1, a row whose file upstream removed saying so; new
  not-carried rows for the declines that concern files (executing-plans'
  scripts, `claude-code-tools.md`'s nested controller, diagnosing-superpowers,
  `builder-check-prompt.md`); the pending rows for the verification table,
  the shell lint (reframed: upstream's pre-commit config lints no shell)
  and the debugging tests moved to Not carried with their reasons.
- `docs/backlog/upstream-sync-review.md` deleted. New items: Codex wait
  cadence (measure on a Codex run first), an audit of `[LOAD-BEARING]`
  marks (how often one forced a stop or a supersede), nested
  orchestration on Claude Code (cost of a controller one layer down).
  `docs/backlog/skill-size-after-compaction.md` gains upstream's form
  (always-run sections into references, a 20,000-character `SKILL.md`
  ceiling) and the authoring rule it would reopen;
  `docs/backlog/skill-text-rewrite.md` gains SDD's two meanings of
  "load-bearing".
- `skills/systematic-debugging/root-cause-tracing.md`: the script run as
  `bash` with its path from the plugin root, the Windows note reworded;
  both dead-end edges lead to instrumenting and tracing on, then to
  `SKILL.md`'s "No Root Cause" section. `find-polluter.sh` gets mode
  100755. `docs/decisions/upstream-skills-kept-close.md` lists both
  departures, with a Changes line.
- `hooks/session-start`: `read_text` uses a builtin read, so the hook
  runs no external command; `tests/test_hook_script.py` gains an
  empty-`PATH` case; `hooks/README.md` states that the registration
  resolves `bash` from `PATH`.
- `skills/using-crucible/references/claude-code.md`: Instruction files
  adds `AGENTS.md` where no `CLAUDE.md` exists.
- `skills/using-crucible/references/codex-dispatch.md`: the full-history
  parenthetical removed.
- The diff step of `task-reviewer-prompt.md`, `re-review-prompt.md`,
  `code-reviewer.md` and SDD's adjudicator: the base must be an ancestor
  of the head (`git merge-base --is-ancestor`), else it is reported, never
  reviewed. `agents/` regenerated; `tests/prose-budget.txt` raised.

## Acceptance

1. `git ls-files -s skills/systematic-debugging/find-polluter.sh` shows
   mode 100755 (100644 before); `grep -n '^\./find-polluter'
   skills/systematic-debugging/root-cause-tracing.md` finds nothing (1
   before).
2. `grep -c "Fix at symptom point"
   skills/systematic-debugging/root-cause-tracing.md` prints 0 (2 before).
3. `grep -nw cat hooks/session-start` finds nothing (1 before); the
   suite's empty-`PATH` case passes.
4. `grep -n AGENTS.md skills/using-crucible/references/claude-code.md`
   finds the clause (nothing before).
5. `grep -rn "full-history" skills` finds nothing (1 before).
6. `grep -rln "is-ancestor" skills` lists the four sites (nothing before).
7. `docs/upstream.md` names v7.0.1 as the last fully reviewed version, and
   every `superpowers/` path in it exists at v7.0.1 or its row says
   upstream removed it (a one-time check against an upstream clone).
8. `docs/backlog/upstream-sync-review.md` does not exist.
9. `python -m pytest tests/` passes.

## Out of scope

- The improvements the review adopted (review grading on spec silence,
  implied inputs in plans, the implementer's failure report, the close
  readout's rulings, the unstated-defaults clause, the scratch-probe
  clause, and the three smaller ones): the next lane.
- The compaction split and the `SKILL.md` size test (the rewrite).
- Changing the hook registration's `bash`; Codex wait guidance; nested
  orchestration; extending inline execution.
- Reporting the root-cause contradiction upstream (the maintainer's call).
- The release.
