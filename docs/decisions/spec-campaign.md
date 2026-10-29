# Spec campaign

## Decision

**Scope.** Redteaming reviews specs and plans and nothing else: a spec,
or a folded spec+plan document, gets the spec campaign, and a plan gets
the plan phase (`docs/decisions/plans.md`). Open-ended, project-wide
issue-mining is out of its scope, and whole-branch review of
implemented code belongs to `crucible:requesting-code-review`
(`crucible:redteaming § Overview`).

**Round 0.** Before any panel on an artifact with a code baseline, one
standalone agent, the campaign's one controller-composed dispatch,
builds a claim table (every claim about the code, TRUE or FALSE with
evidence), checks liveness (every declared mechanism has a producer and
a consumer within the artifact) and runs the artifact's regex and CLI
claims rather than reading them. Its fixes land before round 1 with no
verifier of their own. A greenfield artifact gets no round-0 agent: one
round-1 seat takes the claim table and the liveness check as its
ordered-first hunt. Round 0 consumes no round of the cap
(`crucible:redteaming § Round 0 — mechanical pre-pass`).

**Panels.** Panel size tracks the artifact's maturity and size, never a
fixed number; the calibration is advisory: 4–5 seats for a fresh large
artifact's round 1, one seat carrying several lenses for a small
artifact, 1–2 for a round reading the result of a wave that added,
removed or re-shaped a major mechanism. Every seat reads the whole
artifact, its lens only ordering the search, and no seat sees another's
report. The roster is correctness, evidence-and-inference, general,
contract-fidelity where interfaces are dense, right-sizing, and
abstraction-level for specs; lenses rotate across rounds and mix per
artifact, and the controller may add a lens for what the artifact makes
load-bearing, with a one-line description in the seat's lens slot
(`crucible:redteaming § Panels`). Nothing tallies lenses to demote one;
the roster changes when the skill does. In a spec campaign's round 1
with two or more seats on this host, the one the controller judges most
architecture-heavy runs on the alternate role
(`docs/decisions/model-roles-and-effort.md`).

**The general lens.** Every multi-seat round has at least one general
seat, with no box, and a one-seat round is general by default.

**Right-sizing.** The right-sizing seat's product is scope-cut
decisions, and it is judged by them. It sits in round 1 and is
re-seated mid-campaign or when the artifact has grown, a soft judgment
on the net of the line counts the round records' trace holds (git's
lines added minus lines removed between the round's base and head), a
reflow's noise tolerated. It carries the over-subtraction guard: what it
attests as right-sized is cut only by a logged ruling. A fix that
removes machinery outranks one that adds it, all else equal.

**Quorum and degraded rounds.** Every lost or crashed seat is recorded,
and a round that lost one is topped back up or recorded degraded. A
top-up starts only when the host confirms the lost seat terminal or
absent, or that it acknowledged an interrupt; ambiguous liveness is
BLOCKED and goes to the operator, and the replacement writes a fresh
report under a fresh seat id. A degraded round never counts toward
convergence or against the cap, a one-seat round that loses its seat is
degraded, and two consecutive degraded rounds go to the operator as an
infrastructure escalation (`crucible:redteaming § Panels`).

**Stop rule and cap.** The campaign stops after the first numbered
panel round once overturning a major mechanism after code is no longer
plausible: the overturn question, defined with its reading for an
umbrella's campaign in
`skills/subagent-driven-development/references/premise-and-questions.md`
§ The arrangement questions. The call is the controller's judgment over
the round's records, the seats' forecasts included, never conversation
memory; finding counts and finding provenance are not signals, and
severity is not the trigger: a BLOCKER that would overturn a mechanism
keeps the campaign going by the question itself. A round whose own fix
wave adds, removes or re-shapes a major mechanism is never the stop
round, since no seat has read the result, and once a campaign is chosen
at least one numbered panel round runs. The stop round's open findings
of any severity, premise findings aside, get one fix wave and blind
verification, and the terminal pass always follows and checks the stop's
basis (`docs/decisions/terminal-pass.md`). In a spec campaign every
panel seat's verdict carries a line forecasting the answer, naming the
mechanism where it forecasts an overturn
(`skills/redteaming/seat-prompt.md`), and every numbered
round's readout, the folded lane's and an umbrella's included, states
whether an overturn is still plausible and why, answering each plausible
forecast by the mechanism it names. The cap is 4 rounds, degraded rounds
excluded, counted from the records, the campaign's guarantee that it
ends; it bounds rounds, not spend. An overturn still plausible at the
cap, or a cap round whose own wave adds, removes or re-shapes a major
mechanism, goes to the operator as a decision ask: another round, a
supersede, or acceptance with parked rulings; so does any BLOCKER or
MAJOR still open at the cap
(`crucible:redteaming § Stop rule and terminal pass`). A premise finding
(`docs/decisions/evidence-and-findings.md`) is merged `parked` as a
decision ask to the operator and is never an open finding here, and an
open one joins neither cap ask. One still
open at the campaign's close is carried in the digest's
`## Open judgments`, or in the close readout of a minor design, and
seeded into the ledger as open at the plan phase's close, or at the
campaign's own close on the folded lane; an umbrella's goes to the
operator with the landing ask (`docs/decisions/umbrellas.md`;
`skills/redteaming/references/flip-paths.md` § Premise findings).

**Focused checks.** Panel seats, the round-0 pre-pass, the blind
verifier and the terminal pass run a focused check where a claim needs
one, never a package-wide suite, and recommend heavier validation in
their reports. The task reviewer and re-reviewer are held to focused
checks as well; the implementer is the one seat its template sends to
the full suite (`skills/subagent-driven-development/implementer-prompt.md`
§ Tests: Test-First, Evidence Before Done).

**Operating stance.** Redteaming assumes a baseline error rate in
controller-authored text and budgets blind verification, the
conservation check and the terminal pass for it; errors, the
controller's own included, are reported in the flat register of any
other finding. Its paragraph on disclosure makes shading a record, not
erring in it, the only reportable failure of the reporting duty, and
forbids citing the stance to skip, soften or summarize any other
obligation (`crucible:redteaming § Operating stance — baseline error
rate`).

## Why

### Where the campaign comes from

Upstream reviews a spec through the author's inline self-review and the
user's read of the written file; a spec-document reviewer prompt ships
beside the skill, and no skill text at v6.2.0 dispatches it
(`superpowers/skills/brainstorming/SKILL.md`,
`superpowers/skills/brainstorming/spec-document-reviewer-prompt.md`).
Crucible's campaign grew instead from the maintainer's own redteaming
skill, rebuilt on two studies of how that skill had run on another
project (2026-08-05): one over its git history (474 campaigns, about
1,028 fix commits, February to August 2026), one over session
transcripts (10 multi-agent rounds, 37 seat reports, about 360 raw
findings). (Basis: external, for upstream; measured, for the studies.)

### Scope

The maintainer reported that the skill had been borrowed for
project-wide audits and that this use was never intended; such an audit
needs its own framing (2026-08-06). (Basis: the maintainer's
preference.)

### Round 0

In a classified sample of 141 findings from the git-history study, 14%
were the artifact claiming something false about existing code:
mechanically checkable, and concentrated in early rounds. The liveness
class, a mechanism something reads that nothing writes, surfaced as late
as round 16 in one campaign. A non-adversarial pass catches both before a
panel pays for them, and its fixes need no verifier because the next
dispatch is a full-scope panel (crucible's first design, 2026-08-06).
When templated seats became generated instruments (2026-09-30), the
pre-pass, one per campaign, stayed controller-composed. (Basis:
measured, for the classes; judgment, accepted by the maintainer, for the
pass.)

### Panels and lenses

From the transcript study: in a round, the third to fifth seats
typically added 2–6 unique BLOCKER or MAJOR findings each and none was
fully redundant, while yield fell with the round number, to 1–2 unique
substantive findings from a third seat in a late confirmation round.
About 60% of BLOCKER-class defects were found independently by two or
more seats, minors mostly by one: the full-scope mandate is what buys
that confirmation. Correctness seats had the highest substantive
density. The general seat varied most and produced the sample's
highest-value report, attacking measurement validity, which no named
lens owned; that is why
every multi-seat round keeps one and why evidence-and-inference became a
lens of its own. The 4–5 calibration is that sample's number, fixed on
2026-08-07; the data is thin, so it stays advisory. (Basis: measured;
judgment, accepted by the maintainer, for the roster and calibration.)

The abstraction-level lens counters mechanism creeping into a spec's
binding sections, which is how specs grow (`docs/decisions/the-spec.md`;
judgment, accepted by the maintainer, 2026-08-05). Rotation and custom
lenses were in the maintainer's earlier skill, were lost in crucible's
rewrite with no recorded reason, and returned on 2026-10-13. (Basis:
judgment, accepted by the maintainer.) Per-lens tallies were built to
inform demotion and retired when no decision ever used one
(`docs/decisions/rejected-machinery.md`); demotion was ruled the
maintainer's call, never the controller's, on 2026-08-07. (Basis:
judgment, accepted by the maintainer.)

Every panel runs on one host's model family. A model judging outputs
can favour its own: "Self-Preference Bias in LLM-as-a-Judge" found a
significant degree of it in GPT-4 (https://arxiv.org/abs/2410.21819).
In "Replacing Judges with Juries", a panel of smaller judges from
disjoint model families outperformed a single large judge, with less
intra-model bias, at over seven times lower cost
(https://arxiv.org/abs/2404.18796). That self-preference risk was
accepted on 2026-08-07, to be revisited once a second runtime worked.
The trigger is met on the mechanism side only: Codex is a supported
host, the skill states how a seat on another host would count in round
1's swap, and no workflow composes one; the opt-in seat is
`docs/backlog/second-runtime-seat.md`. (Basis: external; judgment,
accepted by the maintainer, for accepting the risk.)

### Right-sizing

From the git-history study: 77% of rounds grew the artifact, later
rounds grew it more, specs ended 1.4 to 3.4 times their drafted size,
and a simplification lens lost consistently; in the transcript study its
seats filed the round's correctness blockers instead, and the study
suggested folding it into another seat. The maintainer reframed the seat
on 2026-08-05: its product is cutting overdesign, not document size. On
2026-08-06 the maintainer made growth a soft signal, a design that
genuinely explodes being one to split anyway, and on 2026-08-07 kept the
seat against the folding suggestion, seated in round 1 and periodically
after. (Basis: measured; the maintainer's preference, for the seat and
the soft gate.) A mechanical token count once drove the re-seat; it ran
116 times, and one re-seat it tripped found three over-subtraction
MAJORs in an amendment just applied. It went on 2026-10-10 with the
script that parsed the records, and git's line counts took its place,
moving into the round record's trace on 2026-10-13. (Basis: measured;
judgment, accepted by the maintainer.)

### Quorum and degraded rounds

A crashed seat's silence is not a clean pass, and a round missing a seat
reads less than its panel was sized to, so it neither counts toward
convergence nor spends the cap; a quota or infrastructure stall pauses
the campaign rather than wedging it, and repeated loss is the
operator's to fix (crucible's first design, 2026-08-06). The top-up gate
is the seat-replacement rule execution uses
(`docs/decisions/shared-tree.md`), applied to campaign seats on
2026-08-16: a timeout or a missing reply does not prove the first seat
stopped, a replacement beside a live original makes two writers, and a
fresh report path keeps a late return from overwriting its successor.
(Basis: judgment, accepted by the maintainer.)

### Stop rule and cap

Finding counts do not decay: across 89 campaigns of the git-history study
with three or more parseable rounds, first rounds averaged 4.91 findings
and last rounds 5.18. Convergence is information exhaustion, never
validation. (Basis: measured; judgment, accepted by the maintainer,
2026-08-05.)

The share of findings introduced by earlier fix waves left the stop rule
on 2026-08-17, with the per-merge attribution that computed it, and the
structural conjunct then carried the rule: in the spec campaign for
crucible's Codex support, the zero-BLOCKER half held from round 2 while
structural findings ran on to round 4. The cap fell from 6 to 4,
calibrated on that feature's spec and plan campaigns, both of which ran
five rounds; the one round on record past the trigger, the plan
campaign's fifth, returned no BLOCKER, one MAJOR and five MINORs, a cost
the terminal pass's full-scope re-read mitigates. (Basis: measured, on
thin data; judgment, accepted by the maintainer.)

A recount of the campaign records (2026-10-12) supported neither raising
nor lowering the cap, nor changing the trigger: no fresh-panel round past
a valid trigger is on record, so stopping later is as untested as
stopping earlier. At least 7 of 75 stop calls were overturned, reopened
or flagged `CONCLUSION-CHANGING`, the structural half the contested one,
so from 2026-10-13 a BLOCKER-free round's readout stated its structural
basis for the operator. (Basis: measured; judgment, accepted by the
maintainer.)

Under that trigger, a round spent repairing the drift of the last
round's fixes kept the campaign going: on one project, 60–90% of the
findings of rounds 2 and later had been introduced by the previous
round's fix waves. The maintainer judged that reasoning about code is
easier than about a planned design, and proposed the criterion "do we
reasonably expect major mechanisms to be overturned further down the
line?", additions and smaller corrections not counting (2026-10-28).
(Basis: measured, for the drift share; the maintainer's preference, for
the criterion, approved as a hypothesis with no demonstrated accuracy.)
The hypothesis-specs effort applied it to its own campaigns before it
was written into the skills, stopping three times, after one, one and
two panel rounds; nothing found later overturned a major mechanism, and
the post-stop MAJORs that could be traced were drift from recent fixes
(`docs/decisions/routes.md` gives the figures and their limits). On
2026-10-29 the question became the trigger, replacing severity and the
structural judgment rather than joining them, and the cap stayed as the
termination guarantee, stated as a bound on rounds, not on spend. The
alternatives offered were the controller's judgment alone, with no
forecasts, and both tests together. (Basis: measured, for the stops;
judgment, accepted by the maintainer, for the rule's form.)

The seats' forecasts and the re-shape rule answer one weakness of the
probe: in each of those stops the controller made the call and wrote the
readout justifying it. A forecast line from every seat gives the stop a
record the controller did not write, and the terminal pass checks the
stated basis against it (`docs/decisions/terminal-pass.md`). In the
campaign that wrote these rules, piloting the forecast lines, its
terminal pass flagged `CONCLUSION-CHANGING` a round-2 stop resting on
the controller's reading of one seat's forecast, and the operator ran a
third round. (Basis: judgment, accepted by the
maintainer; a single incident, 2026-10-29.) Whether a multi-round
campaign is net-positive at all, and what would settle the cap, stay
open in `docs/backlog/campaign-early-stop-investigation.md`.

The hypothesis-specs umbrella asked that a seat be able to say the spec,
or the goal behind it, is wrong without costing a fix wave, so a premise
finding reaches the operator as a decision ask rather than as an open
BLOCKER or MAJOR that a gate would wait on. The readouts carry it until
it is ruled, and each close passes it to the next phase's record: an
agent's proposal, which the maintainer accepted. (Basis: judgment,
accepted by the maintainer, 2026-10-29.)

### Focused checks

A round-0 pre-pass once started a package-wide suite run of over 30
minutes beside other sessions' suites, on a tree that changed only
documentation. The implementer stays the exception: it is the seat whose
reported test output reviewers take as given
(`docs/decisions/evidence-and-findings.md`). (Basis: a single incident,
2026-10-09.)

### Operating stance

In one session's retrospective (2026-08-16), the controller's readouts
prosecuted its own error rate while its subagents' reports did not, and
the errors it disclosed leaned in the flattering direction, which shame
rewards. The stance makes a caught error the loop working, so disclosure
stays cheap; the paragraph on disclosure keeps it from being read as a
licence to soften records, and the terminal pass's directional-bias
statement is the instrument that detects shading
(`docs/decisions/terminal-pass.md`). On 2026-10-13 the block lost four
sentences on the recommendation of the controller, its reader, keeping
that paragraph unchanged; on 2026-10-28 the paragraph lost its
[LOAD-BEARING] mark, its wording kept, when marks became a spec
convention (`docs/decisions/the-spec.md`). (Basis: a single incident, for
the motive; judgment, accepted by the maintainer, for the stance and the
trim.)

## Rejected

- **Finding counts as a stop signal**: they stay flat deep into long
  campaigns (§ Why).
- **Severity and the structural judgment as the stop trigger**, alone
  or beside the overturn question: a round repairing its predecessor's
  drift kept the campaign going (§ Why).
- **A verifier for round 0's fixes**: the next dispatch is a full-scope
  panel (§ Why).
- **A mechanical growth gate**, a token counter or a hard cap on
  growth: the re-seat stays a soft judgment on git's line counts
  (§ Why).
- **A package-wide suite run from a campaign seat** (§ Why).

## Changes

- 2026-10-29: the stop trigger is the overturn question, replacing
  "zero BLOCKERs and no structural finding": every spec-campaign seat
  forecasts it, every numbered round's readout answers the forecasts,
  a round whose wave re-shapes a major mechanism is never the stop
  round, at least one panel round runs, and the stop round's open
  findings of any severity take its fix wave; the cap of 4 stays, a
  bound on rounds, not spend, and a cap round whose wave re-shapes a
  major mechanism takes the cap ask; the late-round panel calibration
  reads a re-shaping wave's result; after the maintainer's proposed criterion
  and this effort's own stops under it.
- 2026-10-29: a premise finding is a decision ask, outside the stop
  rule's count and the cap asks, carried across the campaign's close
  until ruled, so a seat can say the spec or its goal is wrong without
  costing a fix wave.
- 2026-10-28: the operating stance's paragraph on disclosure lost its
  [LOAD-BEARING] mark, its wording kept: marks are a spec convention.
- 2026-10-13: panels sized by the artifact's maturity and size, every
  seat full-scope with its lens only ordering the search, and lenses
  rotating, mixing per artifact and added with a one-line description.
- 2026-10-13: right-sizing judged by its scope cuts, guarded against
  over-subtraction, and re-seated by a soft judgment on git's line counts
  held in the round record's trace.
- 2026-10-13: the stop trigger and the cap of 4 kept after a recount; a
  BLOCKER-free round's readout states whether it drove structural change.
- 2026-10-13: the operating stance trimmed to the error-rate premise, the
  flat register, the [LOAD-BEARING] paragraph and the pointer to the
  directional-bias statement.
- 2026-10-09: campaign seats run focused checks, never a package-wide
  suite.
- 2026-09-30: round 0: a controller-composed pre-pass checking claims and
  liveness before any panel.
- 2026-08-16: quorum: a lost seat is topped up only on the host's
  confirmation that it is terminal, absent or interrupted, or the round
  is recorded degraded and spends no round of the cap.
- 2026-08-06: the general lens: an unscoped seat on every multi-seat
  round, and a one-seat round general by default.
- 2026-08-06: redteaming reviews specs and plans only, never project-wide
  audits.
