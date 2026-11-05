# Operator steering

## Decision

**Collaborative design, autonomous execution.** The operator's judgment
enters while the design is made, in brainstorming and through the spec
campaign's decision asks. From the plan on, work runs without check-ins
and stops only for a BLOCKED status it cannot resolve, a stop-and-ask
trigger, a decision ask that needs the operator, or completion
(`skills/subagent-driven-development/SKILL.md`, its continuous-execution
rule).

**The analyst stance.** No step requires the operator to read a spec,
plan, code or a diff, none is withheld, and a decision ask may quote the
few lines it turns on. The controller makes technical calls itself and
reports them; design judgments reach the operator as plain-language
decision asks with a recommendation and the strongest case against it,
and a message carrying anything
else puts them last, in a block of their own (`crucible:using-crucible
§ Decision asks`), which every controller reads. The README states the stance to newcomers (`README.md` § Who
it is for). There is no profile switch: the router's precedence line is
the override.

**The campaign gate approves the launch.** At brainstorming's campaign
gate the operator reviews the decision record's decisions, its open asks
and the campaign shape: seats, lenses, models and expected rounds, all
presented inline. Approving the design approves that shape, which the
decision record keeps; the campaign then starts with an announcement
naming any departure, not a pause. The gate shows no token figure
(`crucible:brainstorming § Campaign gate`).

## Why

### Autonomous execution

The design philosophy the maintainer confirmed on 2026-08-06: "A human
checkpoint between tasks is a design defect; safety comes from gates and
review, not attendance." The maintainer's own amendment to that text
records that the plan phase's asks were answered "proceed" more than 95%
of the time in practice (no count is recorded). Upstream's
subagent-driven development already ran tasks without check-ins
(`superpowers/skills/subagent-driven-development/SKILL.md` at v6.2.0);
crucible keeps that and extends it to the plan, which announces its
shape and proceeds (`skills/redteaming/references/plan-phase.md`).
(Basis: judgment, accepted by the maintainer, for the principle; the
maintainer's preference, for the amendment; external, for upstream.)

### Never required, never withheld

The stance began as the maintainer's own way of working: reading agents'
output, not code or diffs. Because human code review is not the
backstop, review has to hold without it, which is why crucible's review
is agentic and evidence-grounded (`docs/decisions/evidence-and-findings.md`).
(Basis: the maintainer's preference, for the way of working; judgment,
accepted by the maintainer, for what review owes it; 2026-08-06.)

On 2026-10-07 the stance became crucible's stated default, as "never
required", not "never shown": that already removes what hurts a reader
who wants to see more, a second mode would double every later route's
paths, and nobody had asked for one. Per-site "overridable" marks went
the same way, since the precedence line already ranks instruction files
and the operator's requests above the skills. (Basis: judgment, accepted
by the maintainer.)

Each decision ask lists every option the findings behind it propose and
states what its change withdraws from an earlier operator approval. That
rule comes from one ask in crucible's own review of its redteaming
rewrite: the ask left out the seats' middle option and did not say that
its fix withdrew relief the operator had approved. The terminal pass
caught it; re-asked, the operator chose the middle option. (Basis: a
single incident, 2026-10-08.)

### One gate for design and launch

The gate replaced the maintainer's habit of mining an intermediate spec
revision for its decisions, trade-offs and omitted but material details.
Upstream's brainstorming has the user review the written spec file
before planning (`superpowers/skills/brainstorming/SKILL.md` at v6.2.0,
its checklist's step 8); crucible's gate asks for decisions instead, and
shows any part of the spec the operator asks for. A separate pause to
approve the campaign launch had been, in the maintainer's words, only a
visibility checkpoint: "I basically never adjusted the shape". (Basis:
the maintainer's preference, 2026-08-06 and 2026-08-07.)

Launch approval moved into the gate, then called the digest gate, on
2026-10-07. The only cost data is the maintainer's runs on one project,
so a token range at the gate would be false precision. The shape has named each seat's model
since 2026-10-09. (Basis: judgment, accepted by the maintainer.) Round
1's alternate-role seat has been named in it since 2026-10-13, at the
maintainer's request for a round-1 replacement of the highest-level
seat (`crucible:redteaming § Panels`). (Basis: the maintainer's
preference.)

Until 2026-11-02 a design digest, a derived file collating a major
design's decisions, flipped positions and open asks from the decision
record and the readouts, was shown at the gate. The skill text rewrite
retired it on its audit's evidence
(`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`, D4). The gate stayed, short: the operator wanted a stop before the
campaign "in case of something coming up". (Basis: judgment, accepted
by the maintainer, for the retirement; the maintainer's preference, over
the controller's recommendation to fold the shape into the design's
approval, for the gate.)

### Decision asks apart

The audit behind that umbrella found decision asks buried in readout
bodies among the structural failures it fixes, so every readout now
puts them in a block after its body. (Basis: judgment, accepted by the
maintainer.)

### The case against a recommendation

A controller's readouts and asks lean toward a coherent account and toward
its own recommendations. On umbrella-specs (2026-10-28) a terminal pass's
second read found three asks framed one-sidedly toward the chosen option
and a plan-phase record calling a repair complete that had missed a site.
On audit-corrections (2026-10-30) the terminal passes and their second
reads found nine statements in the controller's records leaning toward
closure. On backlog batch 8 (2026-11-05), a very-small lane, the branch
review's questions caught three overstatements in the controller's account;
the router's wording had also
narrowed a rule beyond what the maintainer had been told, which the controller
itself said at the close readout. No search has looked for a decision that
went wrong because of any of these. A change
can also reach the records without reaching the maintainer: on arrangements
(2026-10-29) round-0 fixes made the campaign stop the controller's judgment
where the approved spec had made it the operator's to confirm, and the
change was never put to the maintainer, who has since confirmed it
(`docs/decisions/spec-campaign.md`). (Basis: measured, by the reviews'
reports, for the earlier features; the controller's own account for batch 8,
whose reports were not kept.)

The maintainer's view on 2026-10-28 was that the lean is known and expected
and so far not a problem, and that framing both sides is worth examining
but will not remove every bias and may cause decision fatigue. On
2026-11-05 the controller recommended closing all three candidates; the
maintainer chose this clause alone, "for now": a trial, with no review
date. It costs six words in text every session loads, and reaches the
very-small lane, which has no terminal pass to check its asks. It has no
wording test: the failure is on record and the clause is a trial, the
controller's call, which the maintainer accepted. (Basis: the maintainer's
preference, over the controller's recommendation, for the clause; judgment,
accepted by the maintainer, for skipping the test.)

## Rejected

- **An independent read of the controller's records before each round
  readout**: a dispatch per round, beside the terminal pass and its second
  read. The maintainer took the clause instead (§ Why).
- **A check that a readout reached the operator**: no design exists, and the
  maintainer took the clause instead (§ Why). The terminal pass's check still
  stops at the records (`docs/decisions/terminal-pass.md`).
- **A human checkpoint between tasks**: a design defect (§ Why).
- **An analyst profile switch**, or per-site "overridable" marks: the
  precedence line already does it (§ Why).
- **A separate approval pause before the campaign**: never used to
  change the shape (§ Why).
- **Folding the campaign shape into the design's approval**, with no
  gate: the operator kept a stop before the campaign (§ Why).
- **A token estimate at the gate**: false precision (§ Why). The README's
  comparisons carry token figures as the maintainer's labelled
  impressions; the gate does not (`docs/decisions/publication.md`).

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line), so an operator
who wants to read and approve every spec or plan says so, and crucible
shows them; nothing is ever withheld.

## Changes

- 2026-11-05: a decision ask also gives the strongest case against its recommendation, as a trial on the maintainer's choice; because the lean toward a controller's own recommendations recurred and independent reads do not reach every ask.
- 2026-11-05: decision asks coming last in a block of their own moved to the router's § Decision asks, reaching any message to the operator, and SDD's close readout keeps only "in a final block", since the campaign gate, the umbrella landing and the closing review reached the rule only through a redteaming reference.
- 2026-11-02: the design digest retired, with its `digest.md`, its
  format with its `## Decisions`, `## Positions flipped` and
  `## Open judgments` sections, the round readout's digest-update item
  and the major and minor design distinction; brainstorming's "Digest
  gate" section renamed "Campaign gate", showing the decision record's decisions and open asks inline; decision
  asks stand in a block of their own after every readout's body; on the
  umbrella audit's evidence and its structural fix for buried asks.
- 2026-10-19: the analyst stance stated openly in the README: reading is
  never required and nothing is withheld.
- 2026-10-13: the digest gate approves the campaign launch, its shape
  naming seats, lenses, models and expected rounds.
- 2026-08-06: collaborative design, autonomous execution.
