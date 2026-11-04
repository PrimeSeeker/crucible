# The git fallback's local exclude: what stays open

## Observation

`skills/using-git-worktrees/references/git-fallback.md` adds a not-ignored
directory to the clone's `info/exclude`. Throwaway-repository probes show it
passing the ignore check in an ordinary repository, from a linked worktree
and in a submodule.

- **No outcome for a re-check that still fails.** The sentence runs on to
  telling the operator the exclusion holds. The re-check stays at exit 1
  where a `.gitignore` holds `!.worktrees/`, and for a declared directory
  given as an absolute path, whose pattern matches nothing.
- **A host may refuse the write.** A file tool's edit under `.git/` worked on
  Claude Code in a temporary directory. Other project locations and Codex's
  sandbox are unchecked; a sandbox refusing it may refuse the commit and
  `git worktree add` too, and the fallback's failure line covers only the
  latter.
- **A clone whose template has no `info/` directory.** The path is printed
  and its directory is absent, so an append creates it or fails visibly.

No run has reached this path: this repository's `.worktrees/` is ignored.

## Follow-up

Say that a re-check still exiting 1, or a refused write, is reported to the
operator and creation waits. Run the route once on each host.
