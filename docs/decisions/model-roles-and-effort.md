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
bounded task may drop to the bounded role. Task reviewers and
re-reviewers run on the bounded role or better. The adjudicator, the
redteam panel seats and passes, and the branch reviewer run on the
default role, never lowered to save cost; the blind verifier runs on the
bounded role, never lower; the snapshot-blessing agent runs on the
bounded role or better (`crucible:subagent-driven-development
§ Models`; `crucible:redteaming § Panels`;
`crucible:requesting-code-review § Dispatch the branch reviewer`).

**The alternate role has exactly three triggers:** round 1's swap, where
in a spec campaign's round 1 with two or more seats on the host the seat
the controller judges most architecture-heavy runs on it, named in the
campaign shape at the digest gate, with no swap in a one-seat round 1 or
the plan phase; work of a kind the host map lists as a weak spot of its
default role, at an implementer, reviewer or redteam seat, never the
blind verifier; and the operator's request, at any seat. A host map
naming no alternate skips all three.

**Escalation is the tier bump alone.** SDD's fix waves 4–5 go to a fresh
implementer a tier up where one exists, and at the default role to fresh
eyes at the same tier; a BLOCKED reasoning problem at the default role
goes to the operator, who may name the alternate role. Where a host gives
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
§ Install). There are no per-role levels. What a Claude Code seat runs at
with effort unset is unmeasured (`docs/backlog/escalation-and-effort.md`).

A change to the roles, the seats' assignments or the alternate role's
triggers edits this record. A model release that keeps them edits a host
map's Model roles entry, and on Claude Code perhaps the generator's alias
(`docs/dual-runtime.md` § Model floor and effort policy).

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

### The alternate role

Round 1's swap is the maintainer's: "probably we need an R1 replacement
for the highest-level redteam seat"; of three readings an agent offered,
the maintainer chose the seat the controller judges most
architecture-heavy ("IDK, I'd go after c?"). It is held lightly. The
weak-spot and operator triggers were an agent's proposal the maintainer
did not object to. (Basis: the maintainer's preference, for the swap;
judgment, accepted by the maintainer, for the other two.)

On 2026-10-07 an operator exception naming a model above the default was
deleted as "overly strong"; on 2026-10-13 that model returned as Claude
Code's alternate role, reached by the three triggers rather than by the
operator's authorization alone, with that history shown to the
maintainer. Nothing escalates a stuck seat to it. The maintainer: "Late
waves are generally not stuck, just slowly mining the residual issues.
We'll probably introduce a stuck trigger later." The question is open in
`docs/backlog/escalation-and-effort.md`, with whether SDD's fresh
implementer at waves 4–5 keeps its reason. (Basis: the maintainer's
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
request. A Claude Code seat
with effort unset may run below a session set higher, which is
unmeasured. (Basis: external.)

## Rejected

- **Model names in the skills**: every model release would touch every
  skill that names a seat's model.
- **A stuck trigger for the alternate role**: late waves mine residual
  issues rather than stall; open in the backlog (§ Why).
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

## What a project may change

The operator's instruction files and direct requests outrank the skills
(`skills/using-crucible/SKILL.md`, the precedence line). They may name a
model, the alternate role's included, or an effort level for any seat;
the operator's request is one of the alternate role's triggers and the
one way a dispatch gets an effort. On Codex the seats' effort is the
operator's config key.

## Changes

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
