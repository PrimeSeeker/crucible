# Brainstorming first

## Decision

**Brainstorming first.** Feature work, behaviour changes and the host's
planning mode start in `crucible:brainstorming`, whose hard gate holds
implementation until the design is approved, the spec (or lane note) is
written and the handoff has run, "regardless of perceived simplicity".
The one way around it is the trivial-edit waiver
(`docs/decisions/routes.md`).

**Probes.** A throwaway probe in the host's temporary directory that
answers a question is context gathering, not implementation, and is
never committed (`crucible:brainstorming § Context gathering (before
any question)`). Upstream's spike, a throwaway build on the person's
yes, was not taken.

**A document from outside is its input.** A requirements document, an
issue or a plan crucible did not write goes to brainstorming, which keeps
what it settles and asks only about the rest; the result gets its
route's review (`crucible:brainstorming § Context gathering (before any
question)`). `crucible:writing-plans` takes only a spec that has closed
its campaign, and no route runs a foreign plan as written.

**Questions** come one per message, multiple choice where it fits and
open-ended otherwise (`crucible:brainstorming § The dialogue`).

**No visual companion.** Upstream's is not carried; a lighter, opt-in
form is open (`docs/backlog/visual-companion.md`).

## Why

### Brainstorm first

Spec-driven development fails when the author is too confused to write
the spec, a criticism that recurred in the developer discussions surveyed
on 2026-08-05. Exploring before specifying is the part of upstream's flow
that this criticism supports, and it was kept. (Basis: external, as
surveyed on that date; judgment, accepted by the maintainer.)

### Incoming documents

Turning a foreign document straight into a spec would rebuild
brainstorming's output without its review (2026-10-07). The maintainer
called incoming documents "explicitly an improvisation territory (and
probably any such doc is worth redteaming)" (2026-10-11), and on
2026-10-12 dropped the route that would have run a foreign plan as
written: an operator who wants to skip the process says so, and the
router's precedence line makes that request outrank the skill. A foreign
plan takes the route that fits it; on the standard route writing-plans
reads it beside the spec for tasks to reuse, and
`crucible:subagent-driven-development` sends one it is handed to
brainstorming before its Setup creates anything. (Basis: the
maintainer's preference, quoted; judgment, accepted by the maintainer,
for the first point.)

### Questions

Upstream's "prefer multiple choice" was restored on 2026-10-07. The port
had replaced it with a rule against menus, which was one person's
preference: a preference of that kind belongs in that person's
instruction files, not in a skill every user runs. (Basis: judgment,
accepted by the maintainer.)

### The visual companion

The port dropped it because the maintainer did not use it. Upstream's
form is a Node server (`superpowers/skills/brainstorming/scripts/server.cjs`
at v6.2.0) whose page loads its logo from Prime Radiant's site with the
plugin version in the request unless a telemetry opt-out variable is
set: a usage ping crucible would have to strip. A builder tool does
want visual questions, so a lighter, host-neutral form stays open rather
than refused. (Basis: the maintainer's preference, for the
original drop; external, for upstream's server; judgment, accepted by
the maintainer, for keeping it open.)

## Rejected

- **A route that runs a foreign plan as written**: it skips the review
  crucible's own plans get; an operator who wants that asks for it
  (§ Why).
- **writing-plans taking a requirements document or issue directly**:
  it would rebuild brainstorming's output without its review (§ Why).
- **A rule against multiple-choice questions in the skill**: one
  person's preference (§ Why).
- **Upstream's companion as it is**: a Node server with a usage ping
  (§ Why).

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line): an operator may
ask for a foreign plan to run as written, or set how questions are asked.

## Changes

- 2026-10-27: a throwaway probe answering a question is context
  gathering, never committed, narrower than upstream's spike (v7.0.1
  review): it lets a question the repo can answer by running something
  be answered without a design.
- 2026-10-12: brainstorming first, with a document from outside, a
  foreign plan included, as its input; no run-as-written route.
- 2026-10-07: the visual companion stays dropped, now with a reason.
