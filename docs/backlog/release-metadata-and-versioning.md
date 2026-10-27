# The first public release and the install path from GitHub

## Observation

- The version is 0.2.0 in the three manifests, the first public version:
  tagged `v0.2.0` when the public repository is cut, with `stable`
  fast-forwarded to it (`docs/dual-runtime.md` § Release
  metadata).
- `stable` has to be the GitHub repository's default branch for a plain
  install to get the latest release, as `README.md`, `docs/codex.md` and
  `docs/dual-runtime.md` say it does.
- The install, update, pin and rollback commands in `README.md`,
  `docs/codex.md` and `docs/dual-runtime.md` § Upgrades and rollback have
  never been run: they were written before the repository existed. Open
  with them:
  - whether both hosts' installs from GitHub resolve the marketplaces'
    repository-relative sources (`"source": "./"` in
    `.claude-plugin/marketplace.json`, `{"source": "local", "path": "./"}`
    in `.agents/plugins/marketplace.json`);
  - whether Codex, like Claude Code, fetches a new copy only when the
    version changes (`docs/dual-runtime.md` marks it unverified);
  - whether the Codex command forms, taken from codex-cli 0.163.0, exist
    on 0.162.1, the version crucible was tested on.
- The version is stated both in `.claude-plugin/plugin.json` and in the
  marketplace entry, which Claude Code's documentation advises against;
  the suite requires the two to be equal.
- Record formats carry no version marker. No reader refuses an older
  record's shape today, so none would act on one.
- Atlassian's Crucible is a code-review product at end of life (new sales
  ended 2025-05-13, support ends 2028-05-15), so a name collision looks
  unlikely; no trademark check has been run.

## Follow-up

- At the cut: tag `v0.2.0`, fast-forward `stable`, make `stable` the
  default branch, publish the release.
- Then run, from GitHub on both hosts, the install, an update across a
  release, a pin to a tag and a rollback. Confirm the repository-relative
  sources resolve; confirm whether Codex fetches a new copy only on a
  version change, and state the answer in `docs/dual-runtime.md`; confirm the
  Codex command forms on the tested CLI version, or state the version they
  need.
- Decide whether the version stays in both `plugin.json` and the
  marketplace entry or moves to one, changing the suite's equal-versions
  check to match.
- Decide whether record formats need a version marker for in-flight
  upgrades.
- Run a trademark check on the name.
