# Fork and own

## Decision

Crucible is its own project, forked from superpowers at v6.2.0 and owned
outright: project-agnostic, versioned separately, not a git fork, and
merging nothing from upstream. It replaces superpowers completely, every
upstream skill kept, rewritten, folded or dropped, and carries upstream's
MIT license with a repository-level attribution and credits
(`README.md` § License and credits). Restored upstream text counts
against the prose budget like any other
(`docs/decisions/authoring-crucible.md`).

**One router.** No session runs crucible's router beside another; how a
user turns the other one off is that user's migration (`README.md`
§ Coming from superpowers).

**The upstream map.** `docs/upstream.md` holds the fork base and the last
fully reviewed upstream version, the later upstream pieces taken without
a full review, the upstream skills renamed or folded and where they went,
each drop with a one-line reason, and the drops not yet decided, marked
pending with their backlog item. Each upstream release is reviewed as a
diff from the last fully reviewed version; a completed review advances
that version, and rows change only where a disposition does.

## Why

### A fork, owned

Crucible diverges from upstream in its premise. Upstream's plans are
written "assuming the engineer has zero context for our codebase and
questionable taste" and document everything, code included
(`superpowers/skills/writing-plans/SKILL.md` at v6.2.0); crucible's plans
are written for strong implementers, point at the spec instead of
copying it, and lean on adversarial agent review
(`docs/decisions/the-spec.md`). Changes of that kind do not merge back,
and upstream asks forks not to open pull requests that sync a fork or
carry fork-specific changes (its `CLAUDE.md`, under "Fork-specific
changes", at v6.2.0). (Basis: the maintainer's preference, 2026-08-06:
crucible will not merge upstream; external, for upstream's text.)

No existing framework fitted either (§ Rejected).

### A complete replacement, one router

Upstream's SessionStart hook injects its router skill when a session
starts, is cleared or is compacted (`superpowers/hooks/session-start` and
`superpowers/hooks/hooks.json` at v6.2.0), as crucible's hook does
on Claude Code; two routers in one session fight over which workflow it
follows. Crucible therefore replaces superpowers rather than sitting
beside it, and every upstream skill needed a disposition. (Basis: the
maintainer's preference, 2026-08-06; external, for upstream's hook.)

Whether the other router is disabled or uninstalled was once written
into crucible's own process, first as an uninstall and later as a
disable-in-place cutover. The maintainer ruled both out of the decision
on 2026-10-17: "we don't care much for a disable/uninstall (this was a
process bleedthrough), only for not running two routers at once".
(Basis: the maintainer's preference, quoted.) The Codex steps are in
`docs/codex.md` § One router at a time.

### The license

`LICENSE` lines 1 to 3 and 5 to 22 are upstream's `LICENSE` at v6.2.0
byte for byte; line 4 adds crucible's own copyright line, and the
attribution after the license text covers every ported file once.
(Basis: external, compared against upstream's file.)

### The upstream map and its upkeep

An audit of crucible against upstream v6.2.0 (2026-10-17) found upstream
files dropped with no recorded reason, and decisions the tree carries with
no record of why. The map gives each drop its reason in one place, and a
drop not yet decided says so, with the backlog item that decides it. The
reasons are the ones recorded with the drops and the ones the maintainer
confirmed on 2026-10-20, row by row, from an agent's draft; a reason not
confirmed is marked pending. (Basis: measured, for the audit; judgment
accepted by the maintainer, for the reasons.)

Reviewing each release as a diff from the last fully reviewed version
keeps one point at which every disposition was checked; a piece taken
from a later release on its own is listed separately because the rest of
that release was not reviewed, and a file that maps one to one needs no
row. The first such review, to v7.0.1, ran on 2026-10-27
(`docs/crucible/2026-10-27-upstream-review/dispositions.md`).
(Basis: judgment, accepted by the maintainer on 2026-10-20.)

## Rejected

- **An off-the-shelf spec-driven framework** (Spec Kit, Kiro, BMAD,
  OpenSpec, Tessl). A survey of their published documentation on
  2026-08-05 found each one written for an implementer that needs
  everything spelled out, gated on human approvals between phases, or
  both; none treated adversarial agent review of specs and plans as a
  first-class step, and none had a contract for an implementer departing
  from the plan with a logged reason. (Basis: external, as surveyed on
  that date.)
- **Running beside superpowers**, or as a git fork that tracks upstream:
  two routers fight over a session, and there is nothing to merge
  (§ Why).
- **Prescribing disable versus uninstall**: not a decision (§ Why).

## Changes

- 2026-10-27: the upstream map reviewed to v7.0.1; the record points at
  that review's dispositions in place of the backlog item it closed.
- 2026-10-20: the upstream map, maintained, in place of a frozen
  manifest of the v6.2.0 port; each release reviewed as a diff from the
  last fully reviewed version.
- 2026-10-19: a fork owned outright and a complete replacement for
  superpowers, its license and credits carried in `LICENSE` and the
  README.
- 2026-10-17: one router: no session runs two; how the other one is
  turned off is the user's migration.
- 2026-08-05: no off-the-shelf spec-driven framework adopted.
