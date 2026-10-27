# Fully ephemeral records: spec and plan never committed

## Observation

Crucible commits no process records: the feature workspace is untracked
and deleted at SDD's Finish. What a feature commits is its spec and plan,
in the feature folder, and its commit messages. The spec and plan ride in
the feature branch's commits; finishing's pull-request option can remove
them only in a final commit, which keeps them out of the merged tree but
not out of the pull request's commits.

The maintainer asked for a mode in which the spec and plan are never
committed on the feature branch.

## Follow-up

Design that mode. It has to answer what replaces commit-based pins (the
plan header's `spec @ <rev>`, which every seat reads) and how worktree
agents read the artifacts; a local-only `.git/info/exclude` entry for
`docs/crucible/` is one starting point.
