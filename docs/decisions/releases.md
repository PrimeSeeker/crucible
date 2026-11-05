# Releases

## Decision

**A release is a promotion to `stable`.** Features land on `master`. A
release bumps the version in the three manifests that carry one, lands
that bump on `master` like any change, tags the commit `v<version>`,
fast-forwards `stable` to it and publishes a GitHub release with a few
lines of notes. A behaviour change bumps the minor version, fixes the
patch version. `stable` is the default branch and holds only releases,
so a plain install from GitHub gets the latest one, and the maintainer's
own install tracks it (`AGENTS.md`, Git; `docs/dual-runtime.md`
§ Release metadata). The suite checks that the three versions are equal.
None of upstream's release tooling is carried (`docs/upstream.md`).

**Installing from a tag.** Every release keeps its tag. Holding a
version, or rolling back to one, reinstalls from that version's tag; no
archive is kept (`docs/dual-runtime.md` § Upgrades and rollback).

**Pre-releases.** To try a change before its release, `master`'s version
is bumped to a pre-release one (`0.3.0-rc.1`), that commit tagged, and an
install pinned to the tag; `stable` does not move. Reinstalling a release
tag goes back (`docs/dual-runtime.md` § Release metadata, § Upgrades and
rollback). The maintainer holds this position tentatively (§ Why).

**Promotion only between features.** An install moves to a new process
version only when no feature is between its brainstorm and its finish
(`AGENTS.md`, You are editing the process you run under). The rule
covers `stable` and any other install a feature runs under.

## Why

### Releases as promotions

The maintainer's choice, on 2026-10-19: one manual step in place of
upstream's release tooling, with the suite already enforcing equal
versions. That the default branch holds only releases the maintainer
ruled while that design was under review, so a plain install gets a
release, never work in progress. (Basis: the maintainer's preference.)

Claude Code's `claude plugin tag` creates `{name}--v{version}` tags (its
help, Claude Code 2.1.304), the form that other plugins' dependency
version ranges resolve against ("Plugin dependencies", Claude Code's
documentation, read 2026-10-20). No plugin depends on crucible, so it
tags `v<version>`. (Basis: external; judgment, accepted by the
maintainer.)

The first release, 0.2.0 (2026-10-27), ran the install and the pin to a
tag from GitHub on both hosts; the second, 0.3.0 (2026-10-27), ran the
update from 0.2.0 on both, and each host fetched the new copy. (Basis:
measured.)

Codex does not hold a copy by its version. On 2026-11-05 (codex-cli
0.164.0, a throwaway `CODEX_HOME`), an install from the `v0.27.0` tag kept
its copy through re-adding the marketplace at `master`, at the same
version, and `codex plugin marketplace upgrade` then replaced it; from
`v0.26.0` the same steps moved it to 0.27.0, with no `plugin` command in
either run. No ref moved under a marketplace that stayed in place: each
run re-added it. (Basis: measured.)

The version stays in both `.claude-plugin/plugin.json` and the
marketplace entry, though Claude Code's documentation advises against
stating it twice: the suite fails on any mismatch, so the two cannot
drift apart. Record formats carry no version marker, since no reader
refuses an older record's shape, so none would act on one. An agent's
proposal, which the maintainer accepted. (Basis: judgment, accepted by
the maintainer.)

### Installing from a tag

The rule dates from the dual-runtime design of 2026-08-09: install every
upgrade from a tagged revision whose predecessor stays installable, so
that a rollback is defined without an archive. On 2026-10-19 it took its
current form: every release keeps its tag, and holding or rolling back a
version pins it. (Basis: judgment, accepted by the maintainer.)

### Pre-releases

The maintainer asked for "something like an experimental branch" to try
a change on real work; an agent proposed pre-release tags on `master`,
since a host fetches a new copy when the version changes. The maintainer
agreed tentatively ("OK, tentatively agree", 2026-10-27), and the
position was held until both hosts were seen to accept a pre-release
version. Before the first release, both did: an install pinned to a
`0.2.1-rc.1` tag loaded that version, in a newly fetched copy, and moving
back to `v0.2.0` loaded 0.2.0, on Claude Code and on Codex. (Basis:
judgment, accepted tentatively by the maintainer; measured.)

### Promotion between features

A skill change can change the rules under a feature in flight: when the
record parser began reading round records by their exact headings
(2026-10-09), a record written under the older, looser headings would
have printed misses midway through its campaign. Promoting only when no
feature is between its brainstorm and its finish means no feature runs
part of its life under each version (2026-10-10). The maintainer has
promoted that way since, for instance before a brainstorm ("OK, please
promote", 2026-10-13). (Basis: judgment, accepted by the maintainer.)

## Rejected

- **Upstream's release tooling** (a version-bump config and script, a
  release-notes file): one manual step suffices (`docs/upstream.md`).
- **Claude Code's `{name}--v{version}` tag form**: it serves plugin
  dependencies, and none exists (§ Why).
- **A rollback archive**: the predecessor's tag is the rollback.
- **The version in one Claude Code manifest only**: the suite already
  keeps the two equal (§ Why).
- **A version marker in record formats**: nothing would read it (§ Why).

## Changes

- 2026-11-05: the version stays in both Claude Code manifests and record formats take no version marker, each weighed and kept as it is; Codex's refresh of a copy under an unchanged version is measured.
- 2026-10-27: 0.3.0 ran the update from 0.2.0 on both hosts; the
  statement that the update was still to run is replaced by that result.
- 2026-10-27: pre-releases: `master` bumped to a pre-release version and
  tagged, an install pinned to the tag; adopted tentatively once both
  hosts were seen to accept one.
- 2026-10-27: the first release ran the install and pin commands from
  GitHub; the statement that none had run is replaced by that result.
- 2026-10-19: a release bumps the three manifests on `master`, tags
  `v<version>`, fast-forwards `stable`, the default branch holding only
  releases, and publishes notes; minor for behaviour, patch for fixes.
- 2026-10-19: every release keeps its tag; holding or rolling back a
  version reinstalls from its tag, with no archive.
- 2026-10-10: an install is promoted only when no feature is between its
  brainstorm and its finish.
