Lane: very-small (operator-confirmed 2026-11-24)

# Seats without the artifact tools

## Intent

Twice a review seat on Claude Code called the host's artifact tool, its
publish call with edits, to change its own report file: on 2026-10-18 the
call published a branch reviewer's report; on 2026-11-23 a generated
branch-reviewer seat made the same call and the host's permission check
refused it. Asked afterwards, that seat said it wanted to batch several
replacements, that the tool's description presents the call as file
editing, and that an instruction in its context forbidding subagents to
publish was not in mind when it chose. A prose ban had not stopped the
call; taking the tools away does.

The generated instrument agents (`agents/*.md`) therefore deny the host's
four artifact tools through their frontmatter. No allow-list is added:
every other tool stays, the seat's own report-writing tools included, so
the reason the instruments record gives for leaving seats unrestricted
still holds.

Premise: the two incidents and the seat's account are observed. That a
deny list naming tools absent from a session does not stop an agent
launching is measured (Claude Code 2.1.330, headless, a project agent).
That the host honours the list for a plugin's agents and for these tools
is not measured: it shows only in a session after an install update.

Break: a crucible seat on Claude Code dispatched as an instrument agent can
no longer call the artifact tools; nothing in crucible asks a seat to.
Permanent. Nothing changes on Codex, whose seats read the templates, which
this change leaves alone.

## Change list

- `tools/instrument_agents.py`: each rendered agent's frontmatter gains a
  `disallowedTools` line naming Artifact, ArtifactComments, ArtifactData
  and ArtifactCheck; the module's account of the frontmatter says so.
- `agents/*.md`: regenerated with `python tools/instrument_agents.py write`.
- `tests/test_instrument_agents.py`: the frontmatter test admits that key,
  and checks its value is the generator's list.
- `docs/decisions/instruments.md`: the position that instrument agents
  carry no tool restriction becomes one naming the deny list, with the
  incidents, the seat's account and what is unverified; a dated line in
  `## Changes`.
- A backlog item: the seats the list does not reach (template-path and
  controller-composed seats), and the check that the host honours the
  list, due at the first session after an install update.

## Acceptance

1. `python -m pytest tests/` passes, the generator's check mode included.
2. Each of the seven `agents/*.md` files carries exactly one line
   `disallowedTools: Artifact, ArtifactComments, ArtifactData, ArtifactCheck`
   in its frontmatter, and none carries a `tools` key:
   `grep -c "^disallowedTools: Artifact, ArtifactComments, ArtifactData, ArtifactCheck$" agents/*.md`
   prints 1 for each file, and `grep -l "^tools:" agents/*.md` prints
   nothing.
3. `git diff master...HEAD -- docs/decisions/instruments.md` adds a
   `- 2026-11-24:` line.

## Out of scope

- Template-path seats (Codex, and Claude Code's fallback) and seats the
  controller composes: they keep the tools.
- Skill text, seat rules and dispatch cards.
- An install update or trial, and the check that the host honours the
  list.
