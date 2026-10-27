# Routes

## Decision

A feature takes one of three routes, recommended at brainstorming's
present-the-design step, confirmed or vetoed by the operator there, and
recorded in the brainstorm decision record. The controller never
declares a small route, and no feature enters one mid-flight. An
umbrella, the document holding an effort of several features, takes
none of the three: it is campaigned or approved by what it carries, and
each of its children takes a route of its own
(`docs/decisions/umbrellas.md`).

- **Standard:** spec, spec campaign, plan, the plan's verification round,
  execution with per-task review, branch review.
- **Folded**, for a small change that carries a design decision worth
  reviewing before code: spec and plan in one document, `folded.md`, no
  plan phase, and every review instrument unchanged
  (`skills/redteaming/references/folded-lane.md`).
- **Very small**, for a small change with none: a frozen lane note
  (intent, change list, acceptance as runnable checks, out of scope),
  inline implementation, the repository's own gates and the branch
  review, with no spec campaign, plan, digest or per-task review
  (`skills/subagent-driven-development/references/very-small-lane.md`).

Both small routes qualify by judgment, not by file or line counts: no
new mechanism, no blast radius across subsystems, no change to
[LOAD-BEARING] content.

**The trivial-edit waiver.** For a change it judges trivial, the agent
may offer in one line to make it without crucible's process, with no
lane and no artifact; the operator's yes covers that edit only, and the
project's own rules still apply (`skills/using-crucible/SKILL.md`).

## Why

### One process for review, lighter documents

The process started uniform: small edits have surprising blast radius,
and in the maintainer's experience no spec had come through its first
review round without a major finding, small ones included (2026-08-07).
That still holds for the review instruments, which is why the folded
lane drops none of them. What was disproportionate on a small change was
the plan phase and oversized panels: in one run the maintainer described,
a change of four file deletions took about 15 agent dispatches, while
its terminal pass caught a real major defect. Findings scale with the
artifact's surface, not the change's, so the fold removes an artifact,
not a check (2026-08-21). Undoing a fold is an operator decision ask on
the supersede path, and the route is known from `folded.md` and the
decision record's entry, with no folded-lane marker written anywhere.
(Basis: the maintainer's preference, for the uniform review; judgment,
accepted by the maintainer, for the fold; a single incident, for the
run.)

### The very-small lane

Measured on crucible's runs on one project (2026-09-27), in
input-equivalent tokens (input 1×, cache write 1.25×, cache read 0.1×,
output 5×): a small mechanical change on the full route, a 700-line spec
with its campaign, per-task review and branch review, cost about 36
million, 23% of it implementation; a direct-fix session with no spec and
an iterated branch review landed five fixes for about 10.6 million, and
its first scoped re-review caught a major defect the first fix had left
open. So for a change with nothing to decide before code, the diff is
the review object and the branch-review loop iterates on it to its
severity floor. The comparison offers no counterfactual for what a spec
round would have caught. (Basis: measured.)

The note binds through its intent, acceptance and out of scope; a
departure from its change list is logged, and a reviewer's statement
that the change outgrew the lane is an operator decision ask: stay, or
move to the standard route, never to the folded one, whose entry comes
before any artifact is written. The note and the lane's ledger carry a
`Lane: very-small` line. (Basis: judgment, accepted by the maintainer.)

The note and the lane proposal share one gate (2026-10-07): a separate
gate re-presented decisions just made and never showed the note whose
acceptance binds the reviewer. (Basis: judgment, accepted by the
maintainer.)

### The waiver

A trivial change is a typo, a comment or wording the operator dictated;
if the work turns out larger, the agent stops and returns to the
operator. The maintainer's ruling of 2026-10-07 chose an offered waiver
over two alternatives: no route for trivial edits at all, which keeps
the overhead, and an agent-declared route, which hands the agent the
judgment the router exists to check. On 2026-10-12 brainstorming's hard
gate was left as written: the waiver is offered before brainstorming
loads, and the router's precedence line ranks the operator's yes above
any skill. The waiver is unmeasured. (Basis: the maintainer's preference,
for the ruling; judgment, accepted by the maintainer, for the hard
gate.)

## Rejected

- **One uniform process for every change**: on a small change the plan
  document, not the review, was the disproportionate part, and a change
  with nothing to decide before code is best reviewed as its diff
  (§ Why).
- **Qualifying a small route by file or line counts**: the question is
  design risk (new mechanism, blast radius, binding content), which a
  count does not measure.
- **A separate gate for the lane note** (§ Why).
- **No route for trivial edits, or an agent-declared one** (§ Why).

## What a project may change

The waiver never skips the project's own rules, worktrees and tests
included. The operator's instruction files and direct requests outrank
the skills (the router's precedence line), so a project can rule out a
small route or the waiver for its work.

## Changes

- 2026-10-28: an umbrella takes none of the three routes, since it has
  no plan or code of its own; its review follows what it carries, and
  its children take routes of their own.
- 2026-10-13: the folded lane: spec and plan in one document, every
  review instrument unchanged, the route known from `folded.md` and the
  decision record.
- 2026-10-12: the very-small lane: a frozen lane note, review moved to
  the diff, the repository's own gates.
- 2026-10-12: the trivial-edit waiver, offered by the router before
  brainstorming loads.
