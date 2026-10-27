# Shared tree

## Decision

**Read windows.** While any seat, verifier or pass reads a spec or plan,
the artifact is frozen: fixes land between dispatches. While a dispatched
agent works in the worktree, the controller commits nothing there and
queues the commit until it returns. Every read-only dispatch window, in
the campaigns and in execution alike, runs one tree check: it starts with
no tracked or staged change, and the controller records `git rev-parse
HEAD` and `git status --porcelain --untracked-files=all` before and
after. A moved HEAD, any tracked or staged change, or an untracked path
that appeared or disappeared voids every report from the window until it
is re-run on a clean tree; untracked files present at the start are
tolerated, and an edit inside one of them goes unseen, an accepted
residual (`crucible:redteaming § Inputs and state`;
`crucible:subagent-driven-development § Shared-tree rules`). A
campaign seat's input paths are the artifact, its workspace paths, the
supporting inputs its card lists and, for the blind verifier, the
tracked files a delta claim names. Read-only seats run the code they
check claims with under the workspace's `scratch/`, one subdirectory per
report; a standalone branch review, which has no workspace, uses the
host's temporary directory.

**Replacing a seat is gated.** A replacement for a seat that already
holds work starts only when the host confirms the prior seat terminal or
absent, or confirms that it acknowledged an interrupt; that confirmation
revokes its right to write, and silence or a timeout does not. Where
liveness is ambiguous, the controller records the seat BLOCKED, escalates
to the operator, and never dispatches a replacement to find out. A
sanctioned replacement writes to a fresh report path, and the revoked
seat's file stays as the record. In execution the fresh path is the
card's path with `-r<R>` before `.md`
(`crucible:subagent-driven-development § Shared-tree rules`); the same
gate tops up a campaign round that lost a seat, where the replacement
takes a seat id no earlier seat of the feature used and writes that
seat's `seat-<id>.md` (`crucible:redteaming § Panels`;
`docs/decisions/spec-campaign.md`).

## Why

### Read windows

The freeze came from one campaign's terminal pass: the controller
committed a naming fix while the pass was reading, and the pass, which
could not see the conversation, attributed the change to a rogue agent
and objected. Nothing had forbidden editing an artifact under review.
(Basis: a single incident, 2026-08-07.)

The index is shared inside a worktree, so a bare commit, `git add -A` or
`git stash` takes another party's staged work along with it; three
incidents in crucible's runs, recorded on 2026-10-04, led to the
no-commit rule for controllers and the staging rule for implementers
(`docs/decisions/git-steps.md`). On 2026-10-05 the maintainer ruled that
only what the incidents support lands. (Basis: measured, from those
incidents; the maintainer's preference, for the trim.)

A read-only agent that runs code to check a claim has to put that code
somewhere, and in the worktree it changes the tree a sibling seat, or
the controller's next measurement, reads. Hence the tree check, which
makes a changed tree void the window's reports instead of passing
silently, and the workspace's `scratch/`, which ignores itself and so
leaves the check meaningful (2026-10-05). The maintainer chose the
workspace over the host's temporary directory so that scratch code goes
with the workspace instead of accumulating. (Basis: judgment, accepted
by the maintainer.)

The first tree check voided a window on any status line. In execution,
the files an implementer's own test runs leave behind voided reviews
that nothing had disturbed, so on 2026-10-07 execution moved to comparing
the before and after readings, and on 2026-10-09 the campaigns adopted
the same comparison, to keep one rule. A further narrowing, voiding only
for an untracked path among a seat's inputs, was declined on 2026-10-12:
no void it would have spared was on record, and it would have cost a
second rule; the maintainer reaffirmed one rule on a corrected
description. (Basis: judgment, accepted by the maintainer, for the
comparison; the maintainer's preference, for keeping one rule.)

### Replacing a seat

A timeout, a transport error or a missing reply does not show that a
seat stopped, and replacing a seat that is still alive puts two writers
on one tree. The design for
crucible's Codex support (2026-08-09) chose to refuse that state rather
than survive it: BLOCKED is the whole mechanism, and a fresh report path
keeps a late return from the revoked seat from overwriting its
successor's report. The gate landed in SDD's fix loop on 2026-08-16, was
applied to campaign seats the same day, and became a rule for every
seat on 2026-10-07. (Basis: judgment, accepted by the maintainer.)

## Rejected

- **A tree-status attestation in every read-only report**, with a check
  that it is there: the templates' read-only lines already bind, and
  the controller's own check costs one command instead of a section in
  every report (declined on 2026-10-05).
- **Voiding a window only for untracked paths among the seat's inputs**:
  no void it would spare is on record, and it costs a second rule
  (§ Why).
- **Fencing to survive two live writers** (write fences, quarantine
  ledgers): designed on an abandoned branch whose review rounds kept
  adding machinery, and left out; refusing the state costs one
  escalation (§ Why).

## Changes

- 2026-10-12: read windows: the artifact frozen while read, no controller
  commit while a seat works, one comparing tree check for every
  read-only window, a seat's input paths including its supporting
  inputs, and scratch under the workspace or, for a standalone review,
  the host's temporary directory.
- 2026-10-07: the seat-replacement gate, for every seat: a replacement
  only on the host's confirmation that the prior seat is terminal,
  absent or interrupted, ambiguous liveness BLOCKED and escalated, and a
  fresh report path, `-r<R>` in execution and a fresh seat id in a
  campaign.
