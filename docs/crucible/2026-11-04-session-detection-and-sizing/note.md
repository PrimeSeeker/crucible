Lane: very-small (operator-confirmed 2026-11-04)

## Intent

1. A session that loaded another process router at its start stops
   before acting and asks the operator to turn one off. Crucible can't
   turn another plugin off, but its router can notice one.
2. On Claude Code, some sessions are marked unattended by the host: the
   hook's environment has `CLAUDE_CODE_SESSION_ATTENDED=0`. It was seen
   on Claude Code 2.1.317 in a `claude -p` session, and the variable is
   not on the host's environment-variable page. Such a session gets a
   short note in place of the router. The note says crucible is
   installed, routes nothing where nobody can answer, and still runs a
   skill the prompt names. Any other value, or none, loads the router as
   before. The README says so, and tells Codex users, whose sessions get
   no hook, to turn crucible off for headless runs.
3. Planning's advisory sizing calibration measures a task by the number
   and size of the files it edits, beside its neighbours', instead of by
   page length. A task far above its neighbours is split, or the plan
   says why not. The decision record says the saving is unmeasured.
4. The third test justification reads "the deletion or loosening fulfils
   a requirement or review finding".
5. On the very-small lane, the controller's own fix reports name the
   justification for each deleted test, case or assertion and each
   loosened test, as an implementer's do.

## Change list

Advisory.

- The router (`skills/using-crucible/SKILL.md`): the second-router line.
- The hook (`hooks/session-start`): an unattended branch inside the
  Claude Code arm.
  - The test runner (`tests/hook_runner.py`) pins the variable, so the
    suite's result doesn't depend on which session runs it.
  - A hook test covers the variable at 0, 1 and unset.
  - A scanner allowlist entry (`tests/claudeism-allowlist.txt`), if
    needed.
- Docs: `hooks/README.md` § SessionStart injection; `README.md`'s install
  step 3, plus a headless note with the Codex line; and the line in
  `docs/dual-runtime.md` saying the hook inlines the router.
- Skills:
  - the writing-plans sizing sentence (`skills/writing-plans/SKILL.md`
    § Task sizing);
  - the seat rule's third justification
    (`skills/subagent-driven-development/references/seat-rules.md`
    § Tests in review), with the templates regenerated
    (`python tools/instrument_agents.py write`);
  - the very-small lane's inline fix-report sentence
    (`skills/subagent-driven-development/references/very-small-lane.md`).
- Records, each with a 2026-11-04 Changes line:
  `docs/decisions/session-start-hook.md`, `docs/decisions/fork-and-own.md`
  § One router, `docs/decisions/plans.md`, `docs/decisions/test-rules.md`.
- Deletions: the backlog items `docs/backlog/session-environment-detection.md`,
  `docs/backlog/task-sizing-by-implementer-load.md` and
  `docs/backlog/test-justification-followups.md`.
- The prose budget (`tests/prose-budget.txt`) for using-crucible,
  writing-plans and subagent-driven-development.

## Acceptance

- `python -m pytest tests/` passes on two runs, one started with
  `CLAUDE_CODE_SESSION_ATTENDED=0` set and one without it.
- A standing hook test checks both outputs:
  - with the variable at 0, the context is the note and carries none of
    the router's text;
  - at 1 or unset, it is the router and the host map.
- `grep -rl "the change fulfils" skills agents docs/decisions` finds
  nothing (10 files before this lane).
- `grep -c "around a page" skills/writing-plans/SKILL.md` prints 0 (1
  before this lane).
- The three backlog files named in the change list are gone (all
  present before this lane).
- Review-judged: the router line, the note, the README text, the sizing
  sentence, the lane pointer and the records do what the Intent says,
  and nothing more.

## Out of scope

- Any Codex hook or per-run Codex switch.
- Detecting a second router by reading plugin settings.
- A plan-review check of task load.
- Measuring the sizing saving.
- The verifier-repair follow-ups (`docs/backlog/verifier-repair-gaps.md`).
- The other three open rulings: records retention, the visual companion
  and the second-runtime seat.
