Lane: very-small (operator-confirmed 2026-11-23)

# Release channels: a testing branch between master and stable

## Intent

Until now every landed change was released the same day: 36 releases from
2026-10-27 to 2026-11-23, each cut within hours of its landing, because a
change can only be tried once it is installed and the maintainer's
installs followed `stable`. So `stable`, the default branch a plain
install gets, served as the test channel, and a rule released in one
version was up for narrowing two versions later. The route meant for
trying a change first, a pre-release tag with the install pinned to it,
was never used: pinning means removing and re-adding the marketplace for
each trial.

This change puts a branch between the two.

- **`master`**: features land as now, with no version change, tag or
  install update for a landing.
- **`testing`**: the maintainer's installs follow it. A trial moves it:
  one commit, landed on `master` as any change is, sets the version to
  the next pre-release (`0.38.0-rc.1`, `rc.2`, …), `testing`
  fast-forwards to it, and the installs update. No tag and no GitHub
  release.
- **`stable`**: stays the default branch and holds only releases. A
  release is cut from what `testing` has run: a commit on `testing`'s tip
  sets the final version, is tagged, and `testing` and `stable`
  fast-forward to it; it is merged into `master`; the GitHub release's
  notes can say what ran.
- `testing` and `stable` each move only on the maintainer's word, and an
  install moves only when no feature is between its brainstorm and its
  finish, as before. A release waits until what it holds has run on real
  work; that is a judgment, with no fixed cadence.
- Pre-release tags are retired as the way to try a change. Rolling back
  stays what it is: pin an install to a release tag.

Not in this change: a path for an urgent fix to `stable` while `testing`
holds untried work, which has not come up.

Premise. The counts are from this repository's tags. That both hosts
follow a branch was measured on 2026-11-23 in throwaway configurations
against a local git remote (Claude Code 2.1.330, codex-cli 0.170.0):
Claude Code accepted a branch as the marketplace's ref, kept its copy
through a new commit under an unchanged version, and fetched a new copy
at each version change, 0.37.0 to `0.38.0-rc.1`, to `rc.2`, to 0.38.0,
once `claude plugin marketplace update` had run before
`claude plugin update`; Codex followed the branch and its
`marketplace upgrade` replaced the copy under an unchanged version. Not
measured: the GitHub `owner/repo#testing` form, which the first trial on
the real repository measures.

Break: none for anyone installing from `stable`. The maintainer's own
installs are re-pointed once, after the landing.

## Change list

- `AGENTS.md`, Git: the release bullet becomes two, a trial and a
  release.
- `docs/dual-runtime.md` § Release metadata: the paragraphs on a release
  and a pre-release state the three branches, a trial and a release;
  § Upgrades and rollback: following `testing` in place of trying a
  pre-release, with the update commands as measured.
- `README.md` § Updates and versions: `testing` named, and how to follow
  it.
- `docs/decisions/releases.md`: the Decision, a § Why section with the
  counts, the maintainer's words and the probe, the rejected
  alternatives, and a `## Changes` line. `docs/decisions/git-steps.md`:
  the sentence on what `master` is for.
- After the landing, on the maintainer's go-ahead, outside the diff: the
  landing's own trial (a version commit to `0.38.0-rc.1`), `testing`
  created on the remote at it, and both installs re-pointed to `testing`.

## Acceptance

1. `python -m pytest tests/` passes.
2. `git grep -c "^- 2026-11-23:" -- docs/decisions/releases.md` prints a
   count.
3. After the landing and the go-ahead, run by the controller and
   reported at the close, not by the branch reviewer:
   `git ls-remote origin testing` prints the trial commit, and each
   host's plugin list shows `0.37.1-rc.1` from a marketplace whose
   recorded ref is `testing`.

On the tree before the change, check 1 passes and check 2 prints nothing;
`origin` has no `testing` branch. No check searches for wording: the
Intent states the outcome and the branch reviewer judges the documents
against it.

## Out of scope

- Skill text: none changes, so no prose budget moves.
- Any change to how a plain install from `stable` works, the tag form,
  or rollback by tag.
- A path for an urgent fix to `stable`.
- A cadence or a counter for releases.
- The suite: no test of branch names or version shape is added.
- The closing line of the process notes, a separate change that follows.
