# Spec campaign

## Decision

**Scope.** Redteaming reviews specs and plans and nothing else: a spec,
or a folded spec+plan document, gets the spec campaign, and a plan gets
the plan phase (`docs/decisions/plans.md`). Open-ended, project-wide
issue-mining is out of its scope, and whole-branch review of
implemented code belongs to `crucible:requesting-code-review`
(`crucible:redteaming § Overview`).

**Round 0.** Before any panel on every spec campaign, one standalone
agent, the campaign's one controller-composed dispatch, builds a claim
table (every claim about the code, or with no code baseline every claim
about the artifact's inputs, TRUE or FALSE with evidence), checks
liveness (every declared mechanism has a producer and a consumer within
the artifact) and runs the artifact's regex and CLI claims rather than
reading them. Its prompt has it stake each finding's severity, and its
fix list, which takes what any fix list takes
(`docs/decisions/fix-verification-and-merge.md`), lands before round 1
with no verifier of its own. Round 0 consumes no round of the cap
(`crucible:redteaming § Round 0 — mechanical pre-pass`).

**Panels.** Panel size tracks the artifact's maturity and size, never a
fixed number; the calibration is advisory: 4–5 seats for a fresh large
artifact's round 1, one seat carrying several lenses for a small
artifact, 1–2 for a round reading the result of a wave that added,
removed or re-shaped a major mechanism. Every seat reads the whole
artifact, its lens only ordering the search, and no seat sees another's
report. The roster is correctness, evidence-and-inference, general,
contract-fidelity where interfaces are dense, right-sizing,
abstraction-level for specs, and outside-the-frame, which asks whether
the design solves the problem the request poses (for a child, with its
umbrella's Intent and its entry) and whether another framing, or no
change, would serve it better, carried by one seat of a spec campaign's
round 1 and no other; lenses rotate across rounds and mix per
artifact, and the controller may add a lens for what the artifact makes
load-bearing, with a one-line description in the seat's lens slot
(`crucible:redteaming § Panels`). Nothing tallies lenses to demote one;
the roster changes when the skill does. In a spec campaign's round 1
with two or more seats on this host, the one the controller judges most
architecture-heavy runs on the alternate role
(`docs/decisions/model-roles-and-effort.md`).

**A seat on another host.** It runs only where the operator's
instructions or request ask for one, never on crucible's proposal: an
extra seat, read-only, beside the round's seats on this host, which stay
complete without it, required lenses included. Its loss costs the round
nothing, though the round readout names it, and its findings are each
checked against the files before they merge (`skills/redteaming/references/panels.md`;
`skills/redteaming/references/merge-and-finding-hygiene.md`).

**The general lens.** Every multi-seat round has at least one general
seat, with no box, and a one-seat round is general by default; a
one-seat round 1 carries outside-the-frame beside general.

**Right-sizing.** The right-sizing seat's product is scope-cut
decisions, and it is judged by them. It sits in round 1 and is
re-seated mid-campaign or when the controller judges the artifact has
grown far enough to need it. It carries the over-subtraction guard, as lens text the controller fills into its lens slot (`skills/redteaming/references/panels.md`): what it
attests as right-sized is cut only by a logged ruling. A fix that
removes machinery outranks one that adds it, all else equal.

**Quorum and degraded rounds.** Every lost or crashed seat is recorded,
and a round that lost one, a seat on another host aside, is topped
back up or recorded degraded. A
top-up starts only when the host confirms the lost seat has stopped; a
seat whose state the host cannot confirm is a stop-and-ask, and the
replacement writes a fresh report under a fresh seat id. A degraded round never counts toward
convergence or against the cap, a one-seat round that loses its seat is
degraded, and two consecutive degraded rounds go to the operator as an
infrastructure escalation (`crucible:redteaming § Panels`).

**Stop rule and cap.** The campaign stops after the first numbered
panel round once overturning a major mechanism after code is no longer
reasonably expected: the overturn question, defined in
`skills/subagent-driven-development/references/review-terms.md`
§ The arrangement questions, its reading for an umbrella's campaign in
§ An umbrella's overturn question. The call is the controller's judgment, not
put to the operator to confirm, over the round's records, the seats'
forecasts included, never conversation memory; finding counts and
finding provenance are not signals, and severity is not the trigger: a
BLOCKER that would overturn a mechanism
keeps the campaign going by the question itself. A round whose own fix
wave adds, removes or re-shapes a major mechanism is never the stop
round, since no seat has read the result, and once a campaign is chosen
at least one numbered panel round runs. The stop round's open findings
that a fix list takes, premise findings aside, get one fix wave and blind
verification, and the terminal pass always follows and checks the stop's
basis (`docs/decisions/terminal-pass.md`). In a spec campaign every
panel seat's verdict carries a line forecasting the answer, naming the
mechanism where it forecasts an overturn
(`skills/redteaming/seat-prompt.md`), and every numbered
round's readout, the folded lane's and an umbrella's included, states
whether an overturn is still reasonably expected and why, answering
each forecast that one is by the mechanism it names. The cap is 4
rounds, degraded rounds excluded, counted from the records, the
campaign's guarantee that it ends; it bounds rounds, not spend. An
overturn still reasonably expected at the cap, or a cap round whose own
wave adds, removes or re-shapes a major
mechanism, goes to the operator as a decision ask: another round, a
supersede, or acceptance with parked rulings; so does any BLOCKER or
MAJOR still open at the cap
(`crucible:redteaming § Stop rule and terminal pass`). A premise finding
(`docs/decisions/evidence-and-findings.md`) is merged `parked` as a
decision ask to the operator and is never an open finding here: it
opens no fix wave, holds no cap and joins neither cap ask, and at the
cap it is put to the operator alone. A pending one holds no stop; a
ruling that upholds it after the stop takes the flip paths. One still
open at the campaign's close is carried in its close readout, and
seeded into the ledger as open at SDD's Setup; an umbrella's goes to the
operator with the landing ask (`docs/decisions/umbrellas.md`;
`skills/redteaming/references/premise-asks.md` § Premise findings).

**Focused checks.** Panel seats, the round-0 pre-pass, the blind
verifier and the terminal pass run a focused check where a claim needs
one, never a package-wide suite, and recommend heavier validation in
their reports. The task reviewer and re-reviewer are held to focused
checks as well; the implementer is the one seat its template sends to
the full suite (`skills/subagent-driven-development/implementer-prompt.md`
§ Tests: Test-First, Evidence Before Done).

**Operating stance.** Redteaming assumes a baseline error rate in
controller-authored text and budgets blind verification and the
terminal pass for it; errors, the
controller's own included, are reported in the flat register of any
other finding. It makes shading a record, not erring in it, the only
reportable failure of the reporting duty, and forbids citing the stance
to skip, soften or summarize any reporting duty
(`crucible:redteaming § Operating stance`).

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

Until 2026-11-02 an artifact with no code baseline got no round-0 agent,
one round-1 seat checking its claims against its inputs first, and the
folded lane gave a code baseline as its reason for always running round
0. The skill text rewrite made round 0 one rule for every spec
campaign: its audit counted round 0 among the reads that catch real
defects, an artifact with no code baseline is rare, and one rule
replaces two. Its prompt stakes severities since then too, because
severity now decides whether a fix list takes a finding. (Basis:
judgment, accepted by the maintainer, for the rule; judgment, an agent's
call the maintainer has not ruled on: round 0 stakes severities.)

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

The outside-the-frame lens came on 2026-11-02 with the skill text
rewrite, beside premise findings kept without their holds. The
rewrite's audit of recorded runs found real catches coming from first
reads of a design, the first panel round among them, and the lens sits
in round 1 alone. (Basis: measured, for where catches come from;
judgment, an agent's proposal accepted by the maintainer, for the lens
and its seat.)

Unless the operator asks otherwise, every panel runs on one host's
model family. A model judging outputs
can favour its own: "Self-Preference Bias in LLM-as-a-Judge" found a
significant degree of it in GPT-4 (https://arxiv.org/abs/2410.21819).
In "Replacing Judges with Juries", a panel of smaller judges from
disjoint model families outperformed a single large judge, with less
intra-model bias, at over seven times lower cost
(https://arxiv.org/abs/2404.18796). That self-preference risk was
accepted on 2026-08-07, to be revisited once a second runtime worked.
(Basis: external; judgment, accepted by the maintainer, for accepting
the risk.)

The revisit came on 2026-11-04: a seat on another host runs only where
the operator asks, and the risk stays accepted for a panel with none.
The recorded yield is thin and nobody has counted it: one BLOCKER, a
fatal flaw in the option Claude had picked; one MAJOR another seat also
raised, backed by an executed probe; one clean return after a short
read; one audit with nothing the others missed and about half its
claims holding only partly, mostly on attribution; one large review
with nothing beyond the losses already accepted; and the run on the
lane that added it, with no findings where that lane's branch review
found a binding line left uncorrected. That does not justify
proposing the seat to everyone, and the audit is why each finding is
checked before it merges. It is an extra seat so that a usage limit, an
expected trade-off on the other host, costs the round nothing. Its
sandbox enforces read-only where a prompt cannot, at the price of
probes that write files. The readout names a lost seat so that a broken
setup cannot silently turn the operator's instruction into nothing.
The README's recommendation is the maintainer's own and is labelled
anecdotal. (Basis: measured, on thin data, for the yield; judgment, an
agent's proposal accepted by the maintainer, for the form; the
maintainer's preference, for the recommendation.)

The run on that lane, from Claude Code with crucible enabled on Codex,
took about 2 minutes and 101k tokens. Its session recorded the
operator's `model_reasoning_effort` value, and its commands read its
template first and no router, the whole basis for the README's "needs
no switch". A run still going after 30 minutes counts as lost: the
figure is a judgment, generous beside that run, and the one hung run on
record was under a fresh Codex home on Windows. (Basis: measured, one
run; judgment, an agent's call, for the figure.)

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
judgment, accepted by the maintainer.) On 2026-11-02 the skill text
rewrite retired the counts, among the campaign mechanisms its audit
found catching little or never running, and the re-seat became the
controller's judgment on how far the artifact has grown. (Basis:
judgment, an agent's proposal accepted by the maintainer.)

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
(Basis: judgment, accepted by the maintainer.) The skill text rewrite
reduced it to one line on 2026-11-02, the ambiguous-liveness BLOCKED
entry in the quorum block going (`docs/decisions/shared-tree.md`).

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

A sentence written when the stop keyed on open BLOCKERs exempted a
pending premise ask from the stop judgment altogether, so a campaign
could stop while an ask whose upholding would re-shape a mechanism
waited on the operator (the audit, `docs/decisions/evidence-and-findings.md`).
From 2026-10-30 such an ask held the stop: the campaign paused at the
round's close until the operator ruled. On 2026-11-02 the hold went,
among the campaign mechanisms the skill text rewrite retired: a pending
ask's failure is loud, since it still reaches the operator and a ruling
that upholds it after the stop takes the flip paths. The label and its
routes stayed, since without the label each place a doubt arises would
need a rule of its own, as that feature's campaign found. (Basis:
measured, for the finding; judgment, an agent's proposal accepted by the
maintainer, for the hold and for its retirement; judgment, accepted by
the maintainer, for keeping the label, a call the maintainer left to the
agent.)

The arrangements spec, as approved at its digest gate, made the stop a
downshift for the operator to confirm, never the controller's alone;
that feature's round-0 fixes made the stop the controller's judgment,
and the change was never put to the maintainer. The audit found it, and
the maintainer then confirmed the stop as the controller's call
("Agreed with the recommendations"); only this record changed. An
agent's proposal, which the maintainer accepted. (Basis: judgment,
accepted by the maintainer.)

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
stays cheap; the clause on disclosure keeps it from being read as a
licence to soften records, and the terminal pass's bias line is the
instrument that detects shading (`docs/decisions/terminal-pass.md`).
On 2026-10-13 the block lost four
sentences on the recommendation of the controller, its reader, keeping
that paragraph unchanged; on 2026-10-28 the paragraph lost its
[LOAD-BEARING] mark, its wording kept, when marks became a spec
convention (`docs/decisions/the-spec.md`); on 2026-11-02 the block lost
its sentence pointing to the directional-bias statement, which folded
into the bias line; on 2026-11-03 it became one sentence, the disclosure
paragraph a clause of it. (Basis: a single incident, for
the motive; judgment, accepted by the maintainer, for the stance and the
trim.)

## Rejected

- **Offering a seat on another host at the campaign gate**: it adds
  detection, and a question for people who never asked (§ Why).
- **Finding counts as a stop signal**: they stay flat deep into long
  campaigns (§ Why).
- **Severity and the structural judgment as the stop trigger**, alone
  or beside the overturn question: a round repairing its predecessor's
  drift kept the campaign going (§ Why).
- **The stop as a downshift the operator confirms**: the form the
  arrangements spec was approved with, replaced in its round 0 and the
  replacement confirmed by the maintainer afterwards (§ Why).
- **A verifier for round 0's fixes**: the next dispatch is a full-scope
  panel (§ Why).
- **A round-1 seat in place of round 0 where there is no code
  baseline**: two rules where one serves (§ Why).
- **A mechanical growth gate**, a token counter or a hard cap on
  growth: the re-seat stays the controller's judgment on growth
  (§ Why).
- **A package-wide suite run from a campaign seat** (§ Why).

## Changes

- 2026-11-04: the round readout names a lost seat on another host, a run counts as lost after 30 minutes, and the record keeps what the one measured run showed, which would otherwise leave with its workspace.
- 2026-11-04: the quorum rule excepts a seat on another host and required lenses stay on this host's seats, so losing it costs the round nothing; the yield gains that lane's own run.
- 2026-11-04: a seat on another host, opt-in and written down, settling the single-family revisit: the maintainer's ruling on a thin recorded yield, and the risk stays accepted for a panel with none.
- 2026-11-03: the operating stance is recorded as the one sentence the compaction made it, its disclosure paragraph now a clause.
- 2026-11-03: the over-subtraction guard reaches the right-sizing seat as lens text from `skills/redteaming/references/panels.md`, and the seat card's `right-sizing` selector goes; because every redteam seat's agent carried the guard for the one seat that takes it (`docs/decisions/instruments.md`).
- 2026-11-03: the premise-finding route is cited at `skills/redteaming/references/premise-asks.md`, where flip-paths' § Premise findings moved, so a controller handling a premise finding no longer loads the flip paths (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: a premise ask open at the campaign's close is seeded into the ledger at SDD's Setup, the ledger's only seeding writer, not at the plan phase's or the folded campaign's close (`docs/decisions/records-and-workspace.md`).
- 2026-11-03: the overturn question's reading for an umbrella's campaign is cited at its own section, split from § The arrangement questions so the seats that never review an umbrella's campaign stop receiving it.
- 2026-11-03: the arrangement questions' citation follows their move from the shared seat reference to `skills/subagent-driven-development/references/review-terms.md`, a reference of their own, so a controller that applies them no longer loads the seat rules.
- 2026-11-02: the shared seat reference's citations follow its rename
  to `seat-rules.md`.
- 2026-11-02: the top-up gate is the one-line replacement rule: the
  host's confirmation that the lost seat has stopped, an unconfirmable
  seat a stop-and-ask; the ambiguous-liveness BLOCKED entry in the
  quorum block removed, because the skill text rewrite reduced seat
  replacement to its line (`docs/decisions/shared-tree.md`).
- 2026-11-02: the right-sizing re-seat is the controller's judgment on
  how far the artifact has grown, and the round record's trace loses its
  line for the wave's line counts; because the skill text rewrite
  retired the counts among the campaign mechanisms its audit found
  catching little or never running
  (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-02: round 0 runs on every spec campaign, with no code
  baseline checking the artifact's claims against its inputs and
  liveness, and its prompt stakes each finding's severity; the seat
  `worksheet` selector's `ordered-first` value and its round-1 hunt are
  removed, `pre-pass` kept; the folded lane's stated reason for round 0
  (a code baseline) goes; because one rule replaces two and the skill
  text rewrite's audit counted round 0 among the reads that catch real
  defects, and round 0 stakes severities because severity now decides
  whether a fix list takes a finding.
- 2026-11-02: a premise ask open at the campaign's close is carried in
  the close readout alone, the design digest and its `## Open judgments`
  being retired, and the round readout drops its digest-update item
  (`docs/decisions/operator-steering.md`).
- 2026-11-02: the operating stance drops its sentence pointing to the
  terminal pass's directional-bias statement, which became the report's
  one bias line (`docs/decisions/terminal-pass.md`); the heading stays,
  since another skill cites it.
- 2026-11-02: round 0's and the stop round's fix lists take only what
  any fix list takes, BLOCKER, MAJOR and binding-text MINOR findings,
  the stop round's no longer every open finding of any severity; the
  other MINORs take `deferred-minor` or an earlier disposition; because
  the skill text rewrite's audit found fix waves the main source of
  process-introduced defects
  (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-02: the operating stance no longer budgets the conservation
  check, retired with `conserve.py` because the skill text rewrite's
  audit found about one trivial catch in about 73 runs
  (`docs/decisions/fix-verification-and-merge.md`).
- 2026-11-02: the hold a pending premise ask put on the stop is
  retired, the `premise` label and its routes kept; the lens roster
  adds `outside-the-frame`, one seat of a spec campaign's round 1 only,
  beside general in a one-seat round 1; because the skill text rewrite
  retired the holds, whose failure is loud, and added the round-1 lens.
- 2026-10-30: the stop trigger asks whether an overturn is still
  reasonably expected, the maintainer's words; a pending premise ask
  whose upholding would re-shape a major mechanism holds the stop until
  ruled, replacing the exemption of premise asks from the stop
  judgment; the stop as the controller's call, made in the arrangements
  campaign's round 0 without an ask, recorded as confirmed by the
  maintainer; after an audit of the hypothesis-specs umbrella.
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
