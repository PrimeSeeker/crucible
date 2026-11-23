# Releases

## Decision

**Three branches.** Features land on `master`, with no version change.
`testing` holds what is on trial, and the maintainer's installs follow
it. `stable` is the default branch and holds only releases, so a plain
install from GitHub gets the latest one. A trial moves `testing`, and a
release is cut from what `testing` has run; a behaviour change takes the
next minor version, fixes the next patch. Each of the two branches moves
only on the maintainer's word, and a release waits until what it holds
has run on real work, a judgment with no cadence. The steps of a trial
and a release: `docs/dual-runtime.md` § Release metadata; `AGENTS.md`,
Git. The suite checks that the three versions are equal. None of
upstream's release tooling is carried (`docs/upstream.md`).

**Installing from a tag.** Every release keeps its tag. Holding a
version, or rolling back to one, reinstalls from that version's tag; no
archive is kept (`docs/dual-runtime.md` § Upgrades and rollback).

**Promotion only between features.** An install moves to a new process
version only when no feature is between its brainstorm and its finish
(`AGENTS.md`, You are editing the process you run under). The rule
covers `testing`, `stable` and any other install a feature runs under.

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
either run. With a ref moving under a marketplace that stayed in place (a
local bare clone through a git URL rewrite), that command alone moved the
copy from 0.26.0 to 0.27.0, then replaced its content at 0.27.0. (Basis:
measured.)

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

### A testing branch

The maintainer asked for "something like an experimental branch" to try
a change on real work; an agent proposed pre-release tags on `master`,
since a host fetches a new copy when the version changes. The maintainer
agreed tentatively ("OK, tentatively agree", 2026-10-27). Before the
first release both hosts were seen to accept a pre-release version: an
install pinned to a `0.2.1-rc.1` tag loaded that version, in a newly
fetched copy, and moving back to `v0.2.0` loaded 0.2.0, on Claude Code
and on Codex. (Basis: judgment, accepted tentatively by the maintainer;
measured.)

No pre-release was cut after that. From 2026-10-27 to 2026-11-23 the
repository released 36 times after its first release, 0.2.0, which is its
first commit, each release commit made within three hours
of the commit before it (a median of a minute), and the notes of the last
four, 0.34.0 to 0.37.0, each said that nothing in them had run in a
session. A change
can only be tried once it is installed, the maintainer's installs
followed `stable`, and pinning an install to a tag means removing and
re-adding the marketplace, more work than a release. So `stable` served
as the test channel. The maintainer, when a rule released in 0.35.0 came
up for narrowing two releases later: "our versioning and publishing
scheme is off. If we're narrowing the rule immediately after seeing it in
action, then it should have been in testing (probably a separate branch
for personal plugin install?), and stable should have been more
conservative" (2026-11-23).

Since 2026-11-23 the maintainer's installs follow a `testing` branch. A
branch is followed once, where a tag is pinned anew for each trial; a
landing costs no version change, tag or install update; and a release is
cut from the point that ran, which `master` will usually have moved past.
That is why the release commit is made on `testing`'s tip and merged into
`master`, in place of landing on `master` first. A trial's pre-release
is of the version its release will take, and moves up from a patch to a
minor when a behaviour change lands, so that versions only rise: no host
was measured moving to a lower version.

Measured that day in throwaway configurations against a local git remote
(Claude Code 2.1.330, codex-cli 0.170.0). Claude Code accepted a branch
as the marketplace's ref; a new commit under an unchanged version left
its copy as it was; and it fetched a new copy at each version change,
0.37.0 to `0.38.0-rc.1`, to `0.38.0-rc.2`, to 0.38.0, once
`claude plugin marketplace update` had run before `claude plugin update`,
which alone reported the old version as the latest; with the GitHub form
following `stable`, that one command moved an install from 0.36.0 to
0.37.0 the same day. Codex followed the
branch, and `codex plugin marketplace upgrade` replaced its copy under an
unchanged version, as measured before. Not measured there: the GitHub
`owner/repo#testing` form, which the first trial on the repository
measures.

The costs accepted: sessions on the maintainer's other work run
`testing`, so real work stays the test bed, one step ahead of `stable`
where it used to be on it; when a batch has run enough to release is a
judgment; and no path is designed for an urgent fix to `stable` while
`testing` holds untried work, which has not come up. (Basis: measured,
for the counts and the hosts; the maintainer's observation and
suggestion of a branch; judgment, the controller's proposal, accepted by
the maintainer, for the scheme's form.)

### Promotion between features

A skill change can change the rules under a feature in flight: when the
record parser began reading round records by their exact headings
(2026-10-09), a record written under the older, looser headings would
have printed misses midway through its campaign. Promoting only when no
feature is between its brainstorm and its finish means no feature runs
part of its life under each version (2026-10-10). The maintainer has
promoted that way since, for instance before a brainstorm ("OK, please
promote", 2026-10-13). (Basis: judgment, accepted by the maintainer.)

An update also reaches a session already running. One that began on
0.34.0 kept loading that copy's skills through two updates, loaded the
0.36.0 copy's from its next invocations after a compaction, and kept
those through a third update, its router text staying as loaded at its
start (2026-11-22 and 2026-11-23). That fits the mechanism
`docs/dual-runtime.md` § Upgrades and rollback states, a new version
loading once the session has reloaded its plugins; whether the
compaction was that reload was not checked. So an install's moves are
kept few and chosen on any branch. (Basis: a single observation.)

## Rejected

- **Upstream's release tooling** (a version-bump config and script, a
  release-notes file): one manual step suffices (`docs/upstream.md`).
- **Claude Code's `{name}--v{version}` tag form**: it serves plugin
  dependencies, and none exists (§ Why).
- **A rollback archive**: the predecessor's tag is the rollback.
- **The version in one Claude Code manifest only**: the suite already
  keeps the two equal (§ Why).
- **A version marker in record formats**: nothing would read it (§ Why).
- **A release for every landing**, the practice until 2026-11-23: it made
  `stable` the test channel (§ A testing branch).
- **Pre-release tags as the way to try a change**, held tentatively from
  2026-10-27 and never used: each trial means re-pinning the install
  (§ A testing branch).
- **The maintainer's installs following `master`**: a release should be
  cut from the point that ran, and `master` moves with every landing.

## Changes

- 2026-11-23: three branches in place of two: features land on `master`
  with no version change, the maintainer's installs follow `testing`,
  which a trial moves to a pre-release version commit, and `stable` is
  released from what `testing` has run; pre-release tags are retired as
  the trial route; because 36 releases in 27 days, each cut within three
  hours of the work it released, had made `stable` the test channel, and
  both hosts were measured following a branch. An update reaching a
  running session joins the reasons an install's moves are kept few.

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
