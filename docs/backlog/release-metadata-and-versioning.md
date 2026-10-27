# Release metadata: what the first release left open

## Observation

- 0.2.0 is the first public release (2026-10-27). The install, pin and
  pre-release commands in `README.md`, `docs/codex.md` and
  `docs/dual-runtime.md` § Upgrades and rollback ran from GitHub on both
  hosts (Claude Code 2.1.311, codex-cli 0.164.0): both resolve the
  marketplaces' repository-relative sources, and both fetch a new copy
  when an install moves to a tag with a different version.
- Not yet run: an update across a release (`claude plugin update`; on
  Codex, `codex plugin marketplace upgrade` then remove and add), which
  needs a second release; and whether either host skips the fetch when
  the content changes but the version does not. Claude Code's plugin
  manifest reference says it does; on Codex it is unverified.
- The version is stated both in `.claude-plugin/plugin.json` and in the
  marketplace entry, which Claude Code's documentation advises against;
  the suite requires the two to be equal.
- Record formats carry no version marker. No reader refuses an older
  record's shape today, so none would act on one.
- Atlassian's Crucible is a code-review product at end of life (new sales
  ended 2025-05-13, support ends 2028-05-15), so a name collision looks
  unlikely; no trademark check has been run.

## Follow-up

- At the next release, run the update on both hosts and state the result
  in `docs/dual-runtime.md` § Upgrades and rollback; check there whether
  Codex fetches a new copy only on a version change.
- Decide whether the version stays in both `plugin.json` and the
  marketplace entry or moves to one, changing the suite's equal-versions
  check to match.
- Decide whether record formats need a version marker for in-flight
  upgrades.
- Run a trademark check on the name.
