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
few lines it turns on. An ask, approval or consent a skill prescribes
reaches the operator as that skill states; any other choice the
router's test sends to them reaches them as a plain-language decision
ask with a recommendation and the strongest case against it; the
controller makes the rest of its calls itself and
states each in its next message to the operator. A message carrying
anything else puts the asks last, in a block of their own (`crucible:using-crucible
§ Decision asks`), which every controller reads. The README states the stance to newcomers (`README.md` § Who
it is for). There is no profile switch: the router's precedence line is
the override.

**The design's approval carries the launch.** As the design
presentation closes, the controller states the preset and the campaign
shape (seats, lenses, models and expected rounds) as its calls, which
the operator may veto; approving the design carries both, and the
decision record keeps them. Brainstorming's campaign gate presents the
record's decisions, its open asks and the shape inline, with what
changed in the spec since the operator's approval or last answer, and
waits only where that message carries a decision ask; otherwise the
campaign starts with an announcement naming any departure. The gate
shows no token figure (`crucible:brainstorming § Campaign gate`).

**Process notes, offered in a line.** A controller always notes what is
off in the process, with its cause, as it happens, and every seat says in
its final reply what was off in its own instructions or tools. When the
work ends the controller gives the operator one line offering the rest,
which in a feature's close readout says so where no notes were made; the
operator's instructions set what more they see, or that they see none
(`skills/using-crucible/SKILL.md`, its Process notes paragraph;
`skills/using-crucible/references/process-notes.md`;
`skills/subagent-driven-development/references/seat-rules.md` § Report
file; `skills/subagent-driven-development/references/dispatch-composition.md`,
item 5). Notes nobody takes are deleted with the workspace.

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

On 2026-11-19 that stop became conditional. A read of sixteen sessions
of one code project, twelve days of work, counted about 400 decisions
put to the operator: the largest housekeeping group, 56, was the route,
the campaign's shape and whether to run another round, and none drew a
departure from the recommendation, which is also the rate a stop kept
for a rare pivot would show. The gate keeps its stop for a pivot the
controller can see, a spec changed since the approval or a decision
still open, and gives it up for one only the operator could see, who
is still told and may interrupt the round. A further round was already
the stop rule's call, and the terminal pass's stop check still sends a
wrong stop to the operator. The conditional stop was the controller's
proposal, from a redteam seat's suggestion; the maintainer chose it
over no stop and over the stop as it stood. (Basis: measured, by
reader seats over the session transcripts, which this repository does
not hold, for the count; the maintainer's preference, over two
alternatives, for the conditional stop.)

### Decision asks apart

The audit behind that umbrella found decision asks buried in readout
bodies among the structural failures it fixes, so every readout now
puts them in a block after its body. (Basis: judgment, accepted by the
maintainer.)

### Which choices reach the operator

In the same read of about 400 decisions, 217 were about what the
product does or about scope, and the operator departed from the
recommendation or raised something new on 45 of them; 121 were
housekeeping, and the operator did so on 4, three of which ruled on the
process itself. About 18 of the product decisions were internal choices
nothing outside the code could observe. So since 2026-11-19 a choice
no skill prescribes reaches the operator only where the router's test
sends it there: an observable change to what the product does or
outputs, money spent outside the session, an act that cannot be undone
or faces outward, a change of scope, a reversed operator ruling, or a
change to a standing rule or a step a skill requires, the last being
the housekeeping where the operator's input fell. Every ask, approval
or consent a skill prescribes keeps its own route. A call the
controller makes is stated in its next message, which needs no record
to carry it and leaves the operator a prompt veto. Whether the test
withholds a choice the operator needed is unmeasured. The controller's
proposal, its last clause and the narrowing to observable changes added
after the count and shown before the design's approval. (Basis:
measured, by reader seats, for the counts; judgment, accepted by the
maintainer, for the test.)

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

### Process notes

The maintainer wanted feedback on the process, including what they cannot
observe at all and what they do not in practice; until 2026-11-21 it came
only when they asked, which spent their attention and reached no other
user. A keyword search of 18 sessions over two weeks, 17 of them on one
code project, found one such request; its answer listed nine things, three
of which led to a later feature. Whether any had been volunteered earlier
was not measured. (Basis: the maintainer's preference, for the feedback;
measured, by a keyword search over session transcripts this repository
does not hold, for the counts.)

A note's causes follow the maintainer's own split, crucible and the
project's or the operator's instructions, alone or with crucible, with the
host and the agent added in the approved note. The maintainer's third
cause, the operator themselves, is met by remarks on the operator's
steering, which wait for an invitation (below). (Basis: the maintainer's
preference, for the split; judgment, accepted by the maintainer, for the
additions.)

The maintainer's first outline left the report to the agent's discretion,
since some users should not be shown unfiltered feedback. The controller
argued that a controller's own account leans toward "it went fine" and
that the agent cannot tell which user it has, so notes are always made,
the operator's instruction files set how much of them they see, and the
agent judges only the kind of item: its own preferences and remarks on
the operator's steering wait for an invitation. (Basis: judgment, accepted
by the maintainer.)

The default for an operator who has said nothing, one line with the count,
the main note and an offer of the rest, was the controller's proposal; the
maintainer accepted it tentatively ("tentatively agree"). (Basis:
judgment, accepted by the maintainer, tentatively.)

With no notes made, a feature's close readout says so and other work says
nothing. A branch review asked what the line is then. The controller
proposed this answer, since at a close silence cannot be told from a
skipped step, while elsewhere the line would be process talk nobody asked
for. The statement is part of the one line, so an operator's instruction
asking for no process notes silences it too: as first written it stood
outside that exception, and a later full-scope pass, reading it literally,
found that such an operator would still see it. It is owed in the close
readout only: a feature dropped before execution, or an umbrella's
landing, says nothing. (Basis: judgment, accepted by the maintainer.)

Notes are made as things happen, one line each in a file in the feature
workspace, so from the workspace's provisioning on they survive compaction
and a change of session, which a question at the close alone would not; a
note made before that, during the brainstorm, is held in the controller's
context and written in once the file exists, and a compaction in between
loses it. They are reread at the close with what hindsight adds; the rule sits in the always-loaded router so it also
reaches work outside a feature. Asked
"what about subagents?", the controller added one sentence to the seats'
shared rules, since a seat is the only second observer of the controller;
the remark goes in the seat's reply rather than in a section of its
report, so the merge and readout rules stay as they were; where a reply
is saved as the report (a seat on another host, a refused write), the
line trails the report's last section. The seats a controller composes
itself, with no template (among them a spec campaign's mechanical
pre-pass, the adjudicator, the snapshot-blessing agent, a fresh look and
an umbrella closing review's seats), at first took no such sentence. Asked
at the build's close, the maintainer agreed that they should, and the duty
now sits in the return contract every dispatch carries, in place of a list
of exceptions. For a note crucible caused, the full list offers a draft
issue for crucible's maintainers, without the project's details, sent only
on the operator's word. The running notes, the seat sentence and the issue
offer were the controller's proposals. (Basis: judgment, accepted by the
maintainer.)

No store keeps notes beyond the workspace. The controller proposed none and
named the loss as a limit; the maintainer's view: "Losing ignored notes is
kind of a feature here, I think". (Basis: judgment, accepted by the
maintainer, for building no store; the maintainer's preference, for the
loss.)

The rule costs 121 words, 737 characters, in text every session loads. Whether
controllers make and offer notes shows only in later sessions
(`docs/backlog/skill-rewrite-reaudit.md`). (Basis: measured, for the words.)

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
- **No stop before the campaign**, the design's approval carrying the
  launch with no wait at the gate: the maintainer kept a stop where the
  gate's message carries a decision ask (§ Why).
- **An unconditional stop before the campaign**: 56 asks on the route,
  the shape or a further round drew no departure (§ Why).
- **No process report unless the operator asks**: the situation before
  process notes, which reaches no operator who does not think to ask
  (§ Why).
- **The full list of process notes by default**: an operator's instruction
  files can ask for it, and some operators should not be shown unfiltered
  feedback (§ Why).
- **An independent reader of a session's records or transcript as a
  standard step**: a strong-model run per feature; one can still be asked
  for.
- **A store for process notes** beyond the workspace: notes nobody takes
  are meant to go (§ Why).
- **Sending notes upstream automatically**: it would send session content
  outward without the operator's consent.
- **A token estimate at the gate**: false precision (§ Why). The README's
  comparisons carry token figures as the maintainer's labelled
  impressions; the gate does not (`docs/decisions/publication.md`).

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line), so an operator
who wants to read and approve every spec or plan says so, and crucible
shows them; nothing is ever withheld. Their instruction files can likewise
ask for the full list of process notes every time, or for none, and can
invite the agent's own preferences and remarks on their steering.

## Changes

- 2026-11-22: every seat says what was off in its instructions or tools, a seat the controller composes itself through the dispatch composition's return contract, the maintainer's answer to a question the build left open; and the statement that no notes were made is part of the one line, so an operator's instructions can silence it, owed in a feature's close readout only; because read literally an operator who asked for no process notes still saw it.
- 2026-11-22: with no process notes made, a feature's close says so and other work says nothing; because a branch review asked what the line is then, and at a close silence cannot be told from a skipped step.
- 2026-11-21: process notes: a controller always notes what is off in the process, with its cause, as it happens, a seat saying in its final reply what was off in its instructions or tools, and gives the operator one line when the work ends, the full list where they or their instructions ask; because the maintainer saw such things only when they asked, which spent their attention and reached no other user.
- 2026-11-19: the preset and the campaign's shape are the controller's calls, stated as the design presentation closes and carried by the design's approval, and the campaign gate waits only where its message carries a decision ask, one the record holds open or a change since the approval that the router's test sends to the operator; this narrows the unconditional stop before the campaign the maintainer kept on 2026-11-02, the conditional stop being the controller's proposal from a seat's suggestion, which the maintainer chose over no stop and over the stop as it stood. A choice no skill prescribes reaches the operator only where that test sends it, the controller stating its other calls in its next message. Because in a read of about 400 decisions over sixteen sessions of one code project the 56 on the route, the shape or a further round drew no departure, and the operator departed or raised something new on 45 of 217 product and scope decisions against 4 of 121 housekeeping ones.
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
