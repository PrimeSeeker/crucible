Lane: very-small (operator-confirmed 2026-10-27)

# Release follow-up

## Intent

Bring the docs and records in line with what the first release's install
checks showed: the first release is out, its install path from GitHub ran
on both hosts, and the pre-release channel passed its check.

## Change list

- `docs/backlog/release-metadata-and-versioning.md`: rewritten as what
  remains open. Drop the release steps and the answered questions
  (repository-relative sources resolve; a pin to a tag works; the Codex
  command forms ran on codex-cli 0.164.0). Keep: an update across a
  release (run at the next release), whether a host skips the fetch when
  content changes without a version change, the version in two places,
  record version markers, the trademark check.
- `docs/dual-runtime.md` § Release metadata and § Upgrades and rollback:
  the pre-release channel (bump master to `X.Y.Z-rc.N`, tag, install
  pinned to the tag; back by pinning a release tag or re-adding the
  marketplace without a ref); `v*` tags are protected from deletion, so a
  pre-release tag is kept; the "whether Codex does too is unverified"
  sentence replaced by what was measured (both hosts fetch a new copy on a
  version change; the "only" untested on Codex).
- `docs/decisions/releases.md`: the pre-release position (Why: the
  measurement, and the maintainer's tentative agreement); "None of the
  install… commands has yet run" replaced; 2026-10-27 Changes lines.
- `docs/codex.md` opening paragraph: the install and pin commands ran on
  codex-cli 0.164.0.

## Acceptance

1. `grep -niE "has yet run|At the cut|is cut|whether Codex does too"
   docs/backlog/release-metadata-and-versioning.md docs/decisions/releases.md
   docs/dual-runtime.md` finds nothing (4 lines before the change).
2. `grep -ni "pre-release"` finds the channel in both `docs/dual-runtime.md`
   and `docs/decisions/releases.md` (nothing before the change).
3. `docs/decisions/releases.md`'s newest Changes line is dated 2026-10-27.
4. `python -m pytest tests/` passes.
5. The cut tool's leak search over the worktree reports
   `0 unexplained hit(s)`.

## Out of scope

- README's "tested on" lines, which describe crucible's behaviour tests,
  not the installs.
- The backlog item's other open questions.
- Any skill text.
- A GitHub release page for pre-releases.
