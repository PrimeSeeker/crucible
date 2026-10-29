# Fully ephemeral records: spec and plan never committed

## Observation

Crucible commits few process records: the feature workspace is
untracked and deleted at SDD's Finish. What a feature commits is its
spec and plan, in the feature folder, its commit messages, and, unless
the project's instructions name another home, an `open-items.md` in the
feature folder listing the work it left open; an umbrella's folder can
hold one too, written at its landing or after its closing review. The spec and plan
ride in the feature branch's commits; finishing's pull-request option
can remove them only in a final commit, which keeps them out of the
merged tree but not out of the pull request's commits.

The maintainer asked for a mode in which the spec and plan are never
committed on the feature branch.

## Follow-up

Design that mode. It has to answer what replaces commit-based pins (the
plan header's `spec @ <rev>`, which every seat reads) and how worktree
agents read the artifacts; a local-only `.git/info/exclude` entry for
`docs/crucible/` is one starting point. It also has to say where open
items go: a mode that commits no feature-folder files leaves the
default `open-items.md` without a home, so the mode names one, an
in-repository file or an outside tracker, as a project's instructions
may.
