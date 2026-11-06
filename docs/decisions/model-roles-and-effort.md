# Model roles and effort

## Decision

**Three roles, named in the skills; models named in the host maps.**
Skills and slot cards name a role, never a model
(`skills/subagent-driven-development/references/dispatch-composition.md`
§ Models and effort):

- **the default role**: the strong model almost every seat runs on, and
  the ceiling of the automatic escalation;
- **the bounded role**: for a clearly bounded task, one step below the
  default role, or the default role's model itself where the host has no
  qualifying tier between; no dispatch goes below it;
- **the alternate role**: the host's other strong model, which no
  escalation reaches.

Each host map's Model roles entry names that host's model for each role
and the floor (`skills/using-crucible/references/claude-code.md`,
`skills/using-crucible/references/codex.md`): never a weak, fast or mini
tier, nor an earlier generation by the host's own labels, and every
model the entry names qualifies. The one other site naming models is the
agent generator's alias map, `MODELS` in `tools/instrument_agents.py`;
the claude-ism scanner flags model names anywhere else in shipped text.
Every dispatch names its model.

**The seats.** The implementer runs on the default role, and a clearly
bounded task may drop to the bounded role. The task reviewer runs on the
default role, every task it reviews; re-reviewers run on the bounded role or
better. The adjudicator, the
redteam panel seats and passes, and the branch reviewer run on the
default role, never lowered to save cost; the blind verifier runs on the
bounded role, never lower; the snapshot-blessing agent runs on the
bounded role or better. The default role is stated once, in the dispatch composition's § Models and effort; an instrument's slot card names only its seat's departure from it, or the branch reviewer's floor, in its Model line, and SDD's Models section the seats SDD composes (`skills/subagent-driven-development/references/dispatch-composition.md` § Models and effort; the seven `*.slots.md` cards; `crucible:subagent-driven-development
§ Models`; `crucible:redteaming § Panels`;
`crucible:requesting-code-review § Dispatch the branch reviewer`).

**The alternate role has exactly three triggers:** round 1's swap, where
in a spec campaign's round 1 with two or more seats on the host the seat
the controller judges most architecture-heavy runs on it, named in the
campaign shape at the campaign gate, with no swap in a one-seat round 1 or
the plan phase, and a round 1 recorded degraded handing on a swap no
returned seat ran (`docs/decisions/spec-campaign.md`); work of a kind the host map lists as a weak spot of its
default role, at an implementer, reviewer or redteam seat, never the
blind verifier; and the operator's request, at any seat. A host map
naming no alternate skips all three.

**Escalation is the tier bump alone.** A BLOCKED reasoning problem goes
to an implementer a tier up where one exists, and at the default role to
the operator, who may name the alternate role; SDD's fix waves escalate
nothing, the operator deciding after the third. Where a host gives
the bounded role the default role's model, escalation from it has no tier
to bump to.

**Effort is the operator's.** No flow sets or raises a dispatch's
reasoning effort on either host; a dispatch sets one only on the
operator's request, `ultra` included. The rule is held lightly, so a
measurement can change it. On Codex a seat whose dispatch names its model
and omits effort runs at `default_subagent_reasoning_effort` in the
`[agents]` table of the operator's Codex config, else at its model's
default; before its first dispatch in a session the controller reads that
config in the Codex home holding the plugin and, if it cannot read it or
the key is absent, tells the operator which and recommends `high`
(`skills/using-crucible/references/codex-dispatch.md`; `docs/codex.md`
§ Install). A seat started from Claude Code through `codex exec` takes
`model_reasoning_effort` from that config instead
(`skills/using-crucible/references/claude-code-dispatch.md`). There are
no per-role levels. A Claude Code seat with effort unset was measured
running at the session's effort on the default role and at `medium` on the
bounded role (§ Why, Effort).

A change to the roles, the seats' assignments or the alternate role's
triggers edits this record. A model release that keeps them follows
`docs/dual-runtime.md` § Model floor and effort policy.

## Why

### Strong models, named by role

The floor dates from 2026-08-07: implementers on a strong default, never
a weak tier, because plans written for strong models must not be padded
down for weak ones: "we don't want to write for them". On 2026-10-13 the
maintainer kept implementers on the default role: "our implementers kind
of double as reviewers (superpowers basically assumes that specs/plans
are reliable, and we shouldn't), so we indeed want a powerful model for
implementers". (Basis: the maintainer's preference.)

The roles came on 2026-10-13 from the maintainer's account of practice,
one strong model for almost everything and another for exceptional
persistence, difficulty or judgement and for a less correlated second
opinion, and from the maintainer's requirement: "All of this would change
with effectively every model release, so we need ease of updates". An
agent proposed the three roles, named in the skills and mapped to models
only in the host maps and the generator, and the maintainer accepted. On
Codex the bounded role was at first the default role's model: that host
listed no model of the current generation between it and the fast class
(read on codex-cli 0.162.1), and the maintainer preferred the default model to a
fast one: "Luna in my experience tends to be very tasteless, so I'd
rather exclude them. Sol fallback is OK". Codex then listed a
current-generation middle tier, `gpt-6.1-terra` (read on codex-cli
0.164.0, 2026-10-27); an agent proposed moving the bounded role to it,
and the maintainer agreed ("Yes, please"). Its capability against the
default model is unmeasured. The floor is
judged by the host's own generation labels rather than by a list written
in crucible. (Basis: the maintainer's preference, for the requirement and
the exclusion; judgment, accepted by the maintainer, for the structure
and the move to the middle tier.)

### The seats

The blind verifier dropped to the bounded role on 2026-09-28, its mandate
unchanged: checking a fix list against a diff is a clearly bounded task,
and a token-cost audit had counted about 91% of verifier dispatches clean.
A recount of the campaign records on 2026-10-12 did not reproduce that
figure: 40% clean in the same window on the audit's own definition, 60
to 64% on the loosest reading. An agent then recommended moving the
verifier back to the default role, and withdrew the recommendation once
the miss count showed no detectable difference in missed defects between
the default role's model of the time and the bounded role's, on a small
sample and a boundary chosen after seeing the data. On 2026-10-13 the
maintainer kept the bounded role: "OK, let's keep Sonnet (5.5 was
probably an upgrade there as well, but the sample size is too small)".
The tier rests on that ruling, not on the audit's clean rate. The other
seats' rows were an agent's recommendation on 2026-10-13, which the
maintainer did not object to: the panel seats, the terminal pass, the
adjudicator and the branch reviewer stay on the default role, the
adjudicator because its dismissals close findings without further
review, and "the bounded role or better" for reviewers replaced "mid-tier
or better", which no host map defined, with no change of meaning.
The snapshot-blessing agent had no row until 2026-10-27, when an agent
proposed the bounded role or better, since like the blind verifier it
checks one stated claim, and the maintainer approved it.
(Basis: the maintainer's preference, for the verifier's tier; measured,
for the recount; judgment, accepted by the maintainer, for the other
rows.)

The task reviewer moved to the default role on 2026-10-29. Its row had
read "the bounded role or better" since the rename above, and before it
"mid-tier or better", from a proposal of 2026-08-07 that measured
nothing; no measurement in crucible's records supports either wording,
and controllers took the floor. A differential probe (2026-10-28)
re-read 10 past task reviews that had approved, 5 on crucible and 5 on
one other project, each by one fresh default-role seat with no rubric,
given a snapshot at the reviewed head, the diff and the plan task. Where
the original reviewer ran on the bounded role (3 crucible samples), the
seat found every defect a later branch review caught that the original
had missed. Where the original ran on the default role over code (4
samples), both saw the same defects, and where a later fix exists, the
original had staked it MINOR and the ledger carried it to the fix. Model
and rubric are confounded in the first group, and the samples are
small. An agent proposed the default role for every task, and the
maintainer agreed, wondering why the lower tier had been chosen in the
first place. The re-reviewer keeps its row, which the probe did not
look at: an agent's proposal, which the maintainer agreed to. (Basis:
measured, on 10 samples; judgment, accepted by the maintainer.)

On 2026-11-03 the seats' rows stopped repeating the default. Every card's Model line, SDD's rows for its three instruments and redteaming's sentence on the verifier restated the default role and the alternate role's triggers, which § Models and effort already holds for every dispatch; the default is now stated there once, each card keeps only its seat's departure (the verifier's bounded role, the re-reviewer's bounded role or better, the implementer's drop for a bounded task, the branch reviewer's floor), and SDD keeps the rows of the seats it composes, which have no card. An agent's proposal, on which the maintainer left the call to the agent. (Basis: judgment, accepted by the maintainer.)

Read from the transcripts on disk on 2026-11-06 (48 sessions, 2,476 seats,
about 3,890 million input-equivalent tokens at the weights of
`docs/decisions/routes.md`), implementers cost 1,298 million, a third of
the whole, and 426 of 457 ran on the default role. On Claude Code the
bounded role's model costs half the default role's (the platform's price
list, read 2026-11-06), so moving half the implementers would save about
8% at equal token use. That runs against the 2026-10-13 ruling above, on
which implementers double as reviewers, and whether quality would hold on
the bounded role is unmeasured; a clearly bounded task can already drop. An agent's
recommendation to record the figure and open no item, which the
maintainer accepted. (Basis: measured, for the cost; judgment, accepted
by the maintainer.)

### A controller one subagent down

Claude Code lets a subagent dispatch its own, and upstream (superpowers
v6.4.1) offers an opt-in: an orchestrator subagent on a mid-tier model
runs SDD end to end, the controller being the costliest seat. A crucible
controller puts decision asks to the operator mid-run, which a nested one
cannot do until it returns. The maintainer, 2026-10-27: "the barrier is
not insurmountable, but I doubt the size of the cost win".

The same transcripts bound the win on Claude Code. The controller is 33% of a run's cost at the record's weights and 29% at
current prices, cache read at 0.05× and every cache write at the 1-hour 2×
(crucible's own 41%, the other project's 31%, at the record's weights; 17
to 74% by session, median 42%, across the 36 sessions with 10 or more
agents). Only part of that could move: while executing, attributed by what
it last dispatched, it is 16% of a run, and a further 6% is unattributed.
At the bounded role's half price and equal token use, that is about 8%, or
about 11% if all the unattributed part moved too, before the outer
controller's overhead. Token use would not be equal, though: about 78% of the
controller's cost at the record's weights is re-read cache, and a nested
controller starting at execution would carry less context, a saving no
script measured. It comes out of the same shares, and seats' costs do not
change, so before overhead the win is about 8% of a run at equal token use
and under 22% however short the context, the top being arithmetic on those
shares, at the record's weights, not a measurement; the overhead is
unmeasured. No nesting or hand-back
protocol was designed, since the barrier to the operator stands either way. The Codex half was never measured and was
dropped with the item. An agent's recommendation, which the maintainer
accepted on a first statement of "at most about 8%" and again on this one.
(Basis: measured, on
tokens, not quality, the other project's runs ending 2026-10-23; external,
for upstream and the host; the maintainer's preference, for the doubt;
judgment, accepted by the maintainer, for closing it.)

### The alternate role

Round 1's swap is the maintainer's: "probably we need an R1 replacement
for the highest-level redteam seat"; of three readings an agent offered,
the maintainer chose the seat the controller judges most
architecture-heavy ("IDK, I'd go after c?"). It is held lightly. The
weak-spot and operator triggers were an agent's proposal the maintainer
did not object to. (Basis: the maintainer's preference, for the swap;
judgment, accepted by the maintainer, for the other two.)

Compared on 2026-11-06 with stage held fixed, in the 28 spec round 1s
holding seats on both models, the alternate role's seat staked 1.54
BLOCKERs and MAJORs against 2.26 per default-role seat; the default role's
was higher in 18, the alternate's in 6, and 4 tied. Across spec round 1s,
its median seat used 0.56 million input-equivalent tokens against 0.86,
at 2.5 times the base
price on Claude Code (the platform's price list, read 2026-11-06). The
seat is chosen as the most architecture-heavy, not at random, and these
are staked counts, not whether a finding held or only that seat raised
it, so the swap stands on the maintainer's ruling. (Basis: measured, on
thin data.)

On 2026-10-07 an operator exception naming a model above the default was
deleted as "overly strong"; on 2026-10-13 that model returned as Claude
Code's alternate role, reached by the three triggers rather than by the
operator's authorization alone, with that history shown to the
maintainer. Nothing escalates a stuck seat to it. The maintainer: "Late
waves are generally not stuck, just slowly mining the residual issues.
We'll probably introduce a stuck trigger later." A seat is stuck when the
same finding fails its re-review on successive fix attempts. Script
counts over the transcripts on disk (2026-11-06; about 120 features, on
this repository and one other project whose runs ended by 2026-10-23)
agree with the first sentence as far as they can see.
11 of 740 parsed re-review verdicts failed, and at most one feature
failed at two separate re-reviews. Text matching linked none of the 11 to
any later verdict, so it shows no repeat without ruling one out. Of 496
implementers, 6 reported BLOCKED in an explicit status line, none on a
fix-wave dispatch, though a status was readable on only 188; none ran on
the alternate role, so nothing shows that role would unstick a seat. Of
the 70 tasks whose fix-wave lines the script captured from the ledgers,
none reached a third wave. In campaigns, BLOCKER or MAJOR findings worded
as repeats were as common in round 1 (6.9%) as later (6.5%), and rounds
past the first kept raising about 2 to 4 such findings per campaign,
among those that reached them. None of this was read by eye, and little
of it is real code under the current rules, so the re-audit counts
repeats there (`docs/backlog/skill-rewrite-reaudit.md`). A task's third
wave already goes to the operator, who may name the alternate role, so
the trigger is declined, withdrawing the expectation of one later.
(Basis: measured, for the counts; judgment, accepted by the maintainer,
for the decline.) SDD's fresh implementer a tier
up at fix waves 4–5 went on 2026-11-02 with the five-wave loop
(`docs/decisions/task-loop.md`). (Basis: the maintainer's
preference; judgment, accepted by the maintainer, for the return.)

### Effort

The rule is the maintainer's, from the 2026-10-13 campaign: "if we want
effort escalation, then it needs to be relative to a controller. Probably
shouldn't automate it, though, sneaky Fable Max would be really draining.
I'd guess we'd better leave it out as a main flow and go with 'when
things aren't right, talk to the user'?" Asked at the close whether that
was final: "that was an expression of uncertainty". Hence the light
hold. (Basis: the maintainer's preference.)

On Codex the ruling's premise, that an unset effort follows the
controller, turned out false when the model is named. In the August and
September sessions, 52 of 52 spawns that named their model and omitted
effort ran at that model's default (codex-cli 0.146.1 to 0.153.4), and a
probe on 0.162.1 (2026-10-14), under a `medium` parent, gave the child
`low` without the config key and `high` with it. Asked whether effort
could be "properly user-configurable", an agent proposed the host's own
key, which the operator sets once and a plugin upgrade leaves alone, with
`high` recommended, and the maintainer agreed. The controller reads the
config from the Codex home found through the plugin root's path, because
a Windows sandbox maps `~` and `CODEX_HOME` to its own account (seen on
codex-cli 0.149.0). Codex has one key for every spawned agent, so
per-role levels are not available. (Basis: measured; the maintainer's
preference, for user configuration; judgment, accepted by the
maintainer, for the mechanism.)

Claude Code's agent-dispatch tool takes an effort setting (its schema,
read 2026-10-13 and again 2026-10-20), used only on the operator's
request. (Basis: external.)

What a seat runs at with it unset was read on 2026-11-05 from the host's own
records, the `effort` field in the transcripts of one session's 325 subagents,
none of its 327 dispatches setting one (Claude Code 2.1.316 to 2.1.318). Under
a session at `high`, 169 Opus and 5 Fable subagents ran at `high`; under
`xhigh`, 86 Opus ones ran at `xhigh`; all 65 Sonnet ones, 9 of them under
`xhigh`, ran at `medium`. So the default role's seats followed the session,
which the tool's description ("its usual effort") does not suggest, and the
bounded role's did not. The alternate role's ran at the one level seen, which
cannot tell following the session from a default of `high`. Only those two
session levels were seen, and why Sonnet stays at `medium` was not
established. Told this, the maintainer accepted an agent's recommendation to
leave the rule as it is: no defect from it has been noticed, though nothing
searched for one, and setting `high` on the re-reviewer and the verifier
would cost more with no evidence for it.
(Basis: measured; judgment, accepted by the maintainer.)

## Rejected

- **Model names in the skills**: every model release would touch every
  skill that names a seat's model.
- **A stuck trigger for the alternate role**: failed fixes are rare,
  nothing shows a repeat, and a task's third wave already reaches the
  operator (§ Why).
- **Automatic effort, or a flow choosing `ultra`**: the maintainer's
  ruling, held lightly; on Codex `ultra` also carries automatic task
  delegation (`docs/decisions/instruments.md`).
- **An operator exception naming a model above the default**: "overly
  strong"; the alternate role reaches that model by its triggers instead.
- **Per-role effort levels set on each Codex dispatch**, the maintainer's
  tentative first answer: one host key covers every seat and survives
  upgrades.
- **Reading the Codex controller's own effort from its rollout file**:
  the format is undocumented, sandbox access and freshness are untested,
  and seats would follow a controller set to `xhigh`.
- **A controller one subagent down on a cheaper model**: it cannot reach
  the operator mid-run, and the saving before an unmeasured overhead is
  about 8% of a run at equal token use and under 22% however short its
  context (§ A controller one subagent down).

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line). They may name a
model, the alternate role's included, or an effort level for any seat;
the operator's request is one of the alternate role's triggers and the
one way a dispatch gets an effort. On Codex the seats' effort is the
operator's config key.

## Changes

- 2026-11-06: a stuck trigger is declined, no longer open, on a read of late waves and rounds whose limits § Why states; because failed fixes were rare and a task's third wave already reaches the operator.
- 2026-11-06: a controller one subagent down is rejected, since it cannot reach the operator and its saving at equal token use is small, the shorter context's saving and the Codex half unmeasured; the implementers' cost share and a comparison of the alternate role's seats in the same round are recorded, and neither changes a row.
- 2026-11-05: what a Claude Code seat runs at with effort unset is measured from host records; the operator-only rule stays, since no defect from the difference on the bounded role has been noticed.
- 2026-11-04: a round 1 recorded degraded hands on a swap no returned seat ran to the next round (`docs/decisions/spec-campaign.md`).
- 2026-11-04: a seat started through `codex exec` names no effort either, and takes the key that run reads from the operator's Codex config, so effort stays the operator's on this route too.
- 2026-11-03: the default role is stated once, in the dispatch composition's § Models and effort; the slot cards' Model lines keep only a seat's departure from it, SDD's Models section drops the implementer's, task reviewer's and re-reviewer's rows, and redteaming drops its sentence on the verifier's role; because each restated what every dispatch already shares.
- 2026-11-02: SDD's escalation row for fix waves 4–5 and its fresh
  implementer a tier up retired with the five-wave loop; the tier bump
  stays for a BLOCKED reasoning problem (`docs/decisions/task-loop.md`).
- 2026-11-02: round 1's swap is named at the campaign gate, the digest
  gate's new name, the design digest being retired
  (`docs/decisions/operator-steering.md`).
- 2026-10-29: the task reviewer's row reads "every task it reviews", a
  plan's task marked branch review only having no task review
  (`docs/decisions/task-loop.md`).
- 2026-10-29: the task reviewer runs on the default role, every task,
  after a differential probe of past task reviews; the re-reviewer keeps
  the bounded role or better.
- 2026-10-27: no dispatch reference states the no-tier-bump case any
  more, since Codex's dropped it; the escalation paragraph states the
  case host-neutrally.
- 2026-10-27: on Codex the bounded role moves from the default role's
  model to `gpt-6.1-terra`, since that host now lists a
  current-generation middle tier.
- 2026-10-27: the snapshot-blessing agent gets a row, the bounded role
  or better, since it had none.
- 2026-10-14: effort the operator's on both hosts, set on a dispatch only
  on request and held lightly; on Codex the seats' effort from the
  operator's config key, checked before the first dispatch, `high`
  recommended; no per-role levels.
- 2026-10-13: three roles named in the skills, models only in the host
  maps and the generator's alias map; the floor by the host's own labels;
  the seats' rows; the alternate role's three triggers; escalation the
  tier bump alone.
