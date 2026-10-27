# Review the upstream delta since the fork base (v6.2.0 → v7.0.0)

## Observation

- Crucible forked superpowers at v6.2.0. Upstream has since tagged v6.3.0
  (2026-08-12), v6.4.1 (2026-09-19), v6.4.2 (2026-09-25) and v7.0.0
  (2026-10-09). The delta has not been reviewed against crucible's
  dispositions.
- Attribution is repository-level by design (`LICENSE`). Near-verbatim
  ports include `writing-good-tests.md`, `systematic-debugging/*`, and
  parts of finishing, worktrees and dispatching-parallel-agents;
  writing-skills' `SKILL.md` keeps three upstream sections (form to
  failure, micro-tests, the meta-question) and its
  `graphviz-conventions.dot` is upstream's verbatim.
- Upstream's behaviour tests and its drill harness
  (`superpowers/docs/testing.md`) are not carried, and no probe set
  replaces them.
- One piece of the delta is taken: v6.3.0's Codex spawn effort fix
  (#2060–#2062). Upstream pins `model` and `reasoning_effort` on every
  spawn, with `[agents] default_subagent_reasoning_effort` as a backstop;
  crucible takes the backstop as the mechanism instead: its dispatches
  leave effort unset, the user's Codex config sets it (`docs/codex.md`
  § Install), and the controller warns once when the key is absent. The
  rest of upstream's
  `superpowers/skills/using-superpowers/references/codex-tools.md`
  changes (waits, lifecycle, model allowlist) are unreviewed.
- v7.0.0's hooks no longer look up `dirname`, `cat` or `bash` on `PATH` (a
  startup `PATH` that cannot resolve them dropped the bootstrap), and its
  Windows launcher ignores a `bash` or `where` planted in the repository.
  Crucible's `hooks/hooks.json` runs `bash` from `PATH`, and
  `hooks/session-start` calls `cat`.
- Upstream's `root-cause-tracing.md` contradicts itself, in v6.4.1 and in
  crucible's copy: its first diagram sends a trace that dead-ends to "Fix
  at symptom point"; its second sends the same "no" to "NEVER fix just the
  symptom".
- Upstream files dropped with no decision yet (`docs/upstream.md`
  § Not carried, decision pending): `superpowers/.pre-commit-config.yaml`
  and `superpowers/scripts/lint-shell.sh` with
  `superpowers/tests/shell-lint/` (crucible's bash hook is unlinted), and
  `superpowers/tests/systematic-debugging/` (`find-polluter.sh` ships
  verbatim and untested).
- Upstream's verification-before-completion has a Common Failures table
  (a claim, what proves it, what does not) and a check on agent
  delegation. Crucible folded the skill into the router's evidence line,
  the implementer's quoted-run rule and SDD Finish's suite run; whether
  those cover the table has not been compared.

## Follow-up

- Review the v6.2.0 → v7.0.0 delta against crucible's dispositions,
  including the v7.0.0 hook `PATH` hardening and the rest of upstream's
  `superpowers/skills/using-superpowers/references/codex-tools.md`
  changes.
- Check v7.0.0's `root-cause-tracing.md` and pick one answer for a trace
  that dead-ends.
- Decide each dropped file above: adopt, or record why not.
- Compare verification-before-completion's Common Failures table and its
  delegation check against crucible's checks; adopt what is missing, or
  record why not.
