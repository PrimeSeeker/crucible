# Shared tree

## Decision

**Read windows.** While any seat, verifier or pass reads a spec or plan,
the artifact is frozen: fixes land between dispatches. While a dispatched
agent works in the worktree, the controller commits nothing there and
queues the commit until it returns. Every review seat in execution,
every dispatch window in the campaigns and an umbrella's closing-review
seats end in one status check. The
seat is dispatched with no tracked or staged change, the controller
first writing the output of `git rev-parse HEAD` and `git status
--porcelain --untracked-files=all` to `<workspace>/tree-check.txt`,
overwritten at each window; seats out at the same time are one window,
the file written before the first and checked after the last. When the
window's last seat returns, before the next commit, the controller runs
both commands again: output differing from the file's voids every report
from the window until it is re-run on a clean tree. Untracked files
present at dispatch are tolerated, and an edit inside one of them goes
unseen, an accepted residual. Nothing about the check is recorded; a
controller resumed after a compaction finds the dispatch-time state in
the file (`crucible:redteaming § Inputs and state`;
`skills/subagent-driven-development/references/dispatch-composition.md`
§ Shared-tree rules). A
campaign seat's input paths are the artifact, its workspace paths, the
supporting inputs its card lists and, for the blind verifier, the
tracked files a delta claim names. Read-only seats run the code they
check claims with under the workspace's `scratch/`, one subdirectory per
report; a standalone branch review, which has no workspace, uses the
host's temporary directory, for `tree-check.txt` too.

**Replacing a seat: one line.** A replacement for a seat never starts
until the host confirms the first has stopped; silence or a timeout is no
confirmation, and a seat whose state the host cannot confirm is a
stop-and-ask, as any unresolvable state is. The replacement writes to a
fresh report path, and the first seat's file stays as the record. In
execution and the branch review the fresh path is the first's with `-r<R>` before `.md`, stated once for every seat there, the slot cards naming only the common path
(`skills/subagent-driven-development/references/dispatch-composition.md` § Shared-tree rules); the same
gate tops up a campaign round that lost a seat, where the replacement
takes a fresh seat id and writes its own `seat-<id>.md`
(`crucible:redteaming § Panels`;
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

The skill text rewrite's audit of crucible's runs counted about 1 catch
for the tree check in more than 800
(`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`), its readings
taken and recorded around every window. On 2026-11-02 it became one status
check after each review seat, kept because reviewers have written into
the tree and an unseen write would land unreviewed, a silent failure:
the readings in the round record and their fields went, and the
dispatch-time HEAD and status output moved to a workspace file, which a
resumed controller reads. The comparison with the dispatch-time untracked
list stays, since a seat can delete an untracked file as well as add
one, and checking for a clean tree alone would again void reviews over
implementers' test leftovers. (Basis: measured, by the audit; judgment,
the controller's proposal accepted by the maintainer, for the shape.)

An umbrella's closing review runs after the last landing, in the session's
checkout, usually on the base, so another session landing there moves HEAD
and voids reports whose fixed range did not move. That stays, an accepted
residual: it costs a re-run of two or three seats, in a review that gates
nothing. An exception sparing a HEAD moved only by `merge` or `pull` entries
in `git reflog` was proposed and dropped, since no such void is on record and
it would cost a second rule. A checkout of the review's own would take a
worktree request, move the workspace and add cleanup, for a rare collision.
(Basis: judgment, accepted by the maintainer, who left the call to the agent,
2026-11-04.)

### One home for both phases

Until 2026-11-02 the shared-tree rules lived in
subagent-driven-development, and redteaming restated the no-commit rule
and the status check beside its pointer there: its controller acts on
both but never reads the other skill. They moved to the dispatch
composition, which every dispatching controller reads when its skill
starts and after compaction, and each skill keeps only its windows.
(Basis: judgment, accepted by the maintainer.)

### Replacing a seat

A timeout, a transport error or a missing reply does not show that a
seat stopped, and replacing a seat that is still alive puts two writers
on one tree. The design for
crucible's Codex support (2026-08-09) chose to refuse that state rather
than survive it: BLOCKED is the whole mechanism, and a fresh report path
keeps a late return from the revoked seat from overwriting its
successor's report. The gate landed in SDD's fix loop on 2026-08-16, was
applied to campaign seats the same day, and became a rule for every
seat on 2026-10-07. (Basis: judgment, accepted by the maintainer.) On
2026-11-02 the skill text rewrite reduced the gate to one line: the
host's confirmation and the fresh report path stay, since a replacement
started early fails silently, and the ambiguous-liveness BLOCKED line and
its escalation text went, a seat whose state the host cannot confirm
being a stop-and-ask like any other unresolvable state. (Basis:
judgment, the controller's proposal accepted by the maintainer, for the
line; keeping the gate rather than retiring it, the controller's call,
delegated by the maintainer.)

## Rejected

- **A tree-status attestation in every read-only report**, with a check
  that it is there: declined, with its reason, in
  `docs/decisions/rejected-machinery.md`.
- **Voiding a window only for untracked paths among the seat's inputs**:
  no void it would spare is on record, and it costs a second rule
  (§ Why).
- **Sparing a closing review's window from a HEAD moved by a landing**:
  the same two grounds (§ Why).
- **Fencing to survive two live writers** (write fences, quarantine
  ledgers): designed on an abandoned branch whose review rounds kept
  adding machinery, and left out; refusing the state costs one
  escalation (§ Why).

## Changes

- 2026-11-04: another session's landing voiding a closing review's window is stated as an accepted residual, and an exception for it declined; because no such void is on record and the exception would cost a second rule.
- 2026-11-04: an umbrella's closing-review seats take the status check, since a window with no named check left the guard off them.
- 2026-11-03: a campaign's replacement seat takes a fresh id, no longer one no earlier seat of the feature used, since the stop check matches forecasts by mechanism, not by seat id: a minor loss under the maintainer's compaction mandate (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-03: the replacement's `-r<R>` path in execution and the branch review is stated in the dispatch composition's § Shared-tree rules, and the slot cards, SDD's shared-tree paragraph and the adjudicator's report paths no longer restate it; because four cards and two SDD sites each carried a copy.
- 2026-11-02: the no-commit rule, the status check and the replacement
  line are stated once, in the dispatch composition's § Shared-tree
  rules, read by every dispatching controller; subagent-driven-development
  and redteaming keep their windows and replacement paths.
- 2026-11-02: `tree-check.txt` is overwritten at each window, not each
  dispatch, matching the window rule beside it; a standalone branch
  review keeps it in the host's temporary directory, having no
  workspace.
- 2026-11-02: the tree check became one status check after each review
  seat against the HEAD and status output written at dispatch to
  `<workspace>/tree-check.txt`, seats out together one window; the
  tree-check readings and their round-record fields removed. Seat
  replacement became one line, the ambiguous-liveness BLOCKED line
  (`Task <N>: BLOCKED — ambiguous seat liveness`) and its escalation
  removed, an unconfirmable seat a stop-and-ask; because the tree
  check caught about 1 in more than 800 and each guard needs only its
  check or its trigger, its function kept.
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
