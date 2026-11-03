# Fix verification and merge

## Decision

**Merge from the indexes.** Every seat report opens with `## Index`, one
line per finding: id, severity, a one-sentence claim, an evidence
pointer. The controller merges from the indexes and opens a finding's
body only to author its fix, to rule on a contested finding or a
collision between seats, or where the line is not enough; questions are
read in full. Every raw seat finding is merged into an entry or closed
as a duplicate of one, and each merged entry names the per-seat finding
ids it absorbs in an `origins:` element, which the terminal pass reads
to find the findings behind each decision ask
(`skills/redteaming/references/round-record.md` § Round record format).
Every seat question takes a disposition. Nothing mechanical checks the
merge. Seat ids are never reused within a feature, the plan phase's
pre-pass id `p0` excepted, so the stop check traces each seat's forecast
across rounds by its id (`crucible:redteaming § Panels`).

**Dispositions and rulings.** Each merged entry takes one disposition:
applied, partly-applied, parked, rejected, deferred-to-implementation or
deferred-minor. Every partly-applied, parked or rejected entry carries a
ruling, a partly-applied one naming the part not acted on; nothing is
silently discarded. When the controller opens a finding's body to author
its fix, it checks each sub-point against the fix item, for a BLOCKER or
MAJOR the body of every origin. An entry whose fix reverses an earlier
round's applied fix names that round and entry.

**The controller applies the fixes.** It writes the fix list into the
round record and applies it to the spec or plan itself; no agent applies
a fix wave (`crucible:redteaming § Fix application and blind
verification`).

**Small fix lists.** Every fix list (round 0's, a numbered round's, the
plan phase's, the spec terminal pass's follow-up wave's) and a
plan-phase repair take, of the findings, BLOCKER and MAJOR ones and
MINORs against binding text, those whose fix changes the artifact's own
binding content (in a spec what
`skills/redteaming/references/flip-paths.md` states binds, in a plan its
inter-task contracts and a task's required fields and acceptance); a
child's fix list never changes umbrella content. Deferral markers,
adopted improvements, operator rulings and contained amendments ride it
as before. Any other MINOR the controller accepts lands in Interfaces &
boundaries where it names missing non-local mechanism, else takes
deferred-to-implementation where its resolution needs local mechanism,
else parked where it is a design judgment for the operator, else
deferred-minor: it is not fixed in the artifact, and SDD's Setup
seeds it into the ledger under `## Deferred minors` with source
`Spec` or `Plan`, for the branch reviewer's triage against the code
(`docs/decisions/branch-review.md`); an umbrella's campaign sends it to
its landing's open-items step. A repeat of one closes as its duplicate.
A MINOR the controller finds wrong or outside the finding scope stays
rejected (`crucible:redteaming § Merge and finding hygiene`).

**Blind verification after every wave.** After every apply, MINOR-only
waves included, the blind verifier receives the fix list and the diff,
never the rationale, the seat reports, the readout or the artifact's
binding content. It verdicts every item landed, not landed or partly
landed, traces every diff hunk to an item, and checks the wave's new
claims about code: TRUE or FALSE with evidence, running each claim's
check against the tracked files it names, or not checked with the
reason. The controller checks each claim reported not checked and
records the outcome. The verifier runs on the bounded role
(`skills/redteaming/verifier-prompt.md`;
`docs/decisions/model-roles-and-effort.md`). Neither phase states a
repair path for a delta claim found FALSE, nor the spec campaign one
for an item not landed (`docs/backlog/verifier-verdict-repair-path.md`).

**Readout coverage and the trace.** The delivered readout names every
rejected, parked or partly-applied BLOCKER or MAJOR with its ruling, in
words; the controller checks that coverage against the merged list
before recording the readout, and nothing checks it afterwards. The
delivered readout carries no merged-list, seat-finding or question id.
Those go in the record-only trace after it: in a numbered round record
and the plan record, each decision ask's merged-list ids, which the
terminal pass reads (`skills/redteaming/references/round-record.md` § Round
record format, field 8). A readout delivered again after compaction
leaves its trace out (`crucible:redteaming § Round readout`).

## Why

### Merging from indexes

In a 2026-09-27 audit of crucible's token costs, the feature workspace's
records were 23% of the characters the controller read. An index line
lets the controller rule on most findings without opening their bodies
(2026-09-28). Nothing has held an index to its findings since the
conservation check stopped parsing reports (2026-10-10), an accepted
gap. (Basis: measured; judgment, accepted by the maintainer.)

### Conservation, retired

Merge conservation began as a reconciliation the controller did by hand,
and it failed once, silently, costing a forced extra fix wave; on
2026-08-21 it became a check in the workspace script, which also
assembled a committed feature summary. Both parsed agent-written
markdown, and the script grew a case each time a review found a shape it
misread: from 720 lines on 2026-08-07, before the check joined it, to
3,014 by 2026-10-10. Measured on 2026-10-10 over 193 rounds in 66
features: the check exited 1 seven times, three or four of them parser
false positives, two bookkeeping misses whose substance had been merged
and one left unresolved, with at most one real catch of a dropped
finding; it exited 2 nine times, each a seat-report format problem
costing a repair cycle. Checking token presence kept the cheap part and
gave up the rest: a mistyped id, a mention counted as accounted and an
index that disagreed with its findings all went unchecked. An independent
re-run in the terminal pass was designed and grew, under review, into
contract changes across four files, so the controller's own run stayed
the only one. (Basis: measured; judgment, accepted by the maintainer.)

The check moved to `conserve.py` under its own name on 2026-10-11. The
trade accepted there: a host with bash but no usable Python learned of
the missing interpreter only at the first `conserve.py` run, where the
controller stopped and told the operator. Unique seat ids kept a mention
of one round's id from accounting for another round's finding; the
plan phase's `p0` exception was the controller's call, delegated by the
maintainer (2026-10-10). (Basis: judgment, accepted by the maintainer.)

On 2026-11-02 the skill text rewrite retired the check, `conserve.py`
and the round record's `conservation:` line. Its audit of recorded runs
(`docs/crucible/2026-11-01-skill-text-rewrite/umbrella.md`) counted
about one trivial catch in about 73 runs of the script. The merge
keeps its `origins:` elements and question dispositions, and seat ids
stay unique because the stop check reads each seat's forecast lines by
id across rounds. (Basis: measured, for the catches; judgment, an
agent's proposal accepted by the maintainer, for the retirement.)

### Dispositions and the sub-point check

Twice in one feature a fix narrower than its finding was recorded
`applied`, and both times only the terminal pass caught it; the
partly-applied disposition and the sub-point check were adopted on
2026-10-07. A recount of the campaign records (2026-10-12) found three
more recorded cases, and the check stayed: it is the one control, at
fix authoring, for a fix narrower than its finding, which the blind
verifier cannot see from its inputs. (Basis: measured; judgment,
accepted by the maintainer.)

### The controller applies the fixes

Measured on 2026-09-30 over 147 fix waves, priced by how long each
touched span stayed in the controller's context: a wave's spec and plan
edits, reads and shell touches cost the controller at most about 0.22
million input-equivalent tokens, about 0.10 million for the edits
alone. A blind verifier, a fresh agent that reads less than an applier
would, cost a median 0.37 to 0.55 million. An applier would cost
roughly 2 to 4 times what it removes, and an agent placing fixes without
seeing the findings risks extra rounds. The maintainer declined it on
2026-09-30. It would be reconsidered if the controller's model came to
be priced well above the model an applier would run on, or a measured
per-wave controller cost rose above a blind verifier's median. (Basis:
measured; judgment, accepted by the maintainer.)

### Small fix lists

The skill text rewrite's audit (2026-11-01) found fix waves the main
source of the defects the process itself introduces: late-round
findings often corrected earlier waves' text, at least six campaign
MAJORs in one set of runs and six of ten correctness clusters of one
after-the-fact audit in another. A MINOR fixed in a campaign buys
little and risks such a defect, so fix lists keep only what must be
right before code: BLOCKER and MAJOR findings, and MINORs against
binding text, which no later stage may edit silently. Other MINORs go
to the branch review, whose triage judges each against the code that
was built, rather than to the close readout, where nobody would check
them against code. (Basis: measured, for the audit; judgment, accepted
by the maintainer, for the rule and the destination, and for the
carve-out for binding text, a call the maintainer left to the agent.)

### Blind verification

A study of the maintainer's earlier redteaming on another project
(2026-08-05) found the dominant late-round failure to be partial or
drifting application of the previous round's fixes: in one campaign, 5
of a round's 8 new findings traced to the prior rounds' cleanup
wording, and 41 commits recorded a defect a prior round's fix had
caused. A check shown the draft tends to repeat the draft's errors: in
"Chain-of-Verification Reduces Hallucination in Large Language Models",
verification questions answered in prompts that leave out the draft
response (the factored variant) did better than the joint variant,
which answers them beside the draft, on every task the paper reports
(https://arxiv.org/abs/2309.11495). Newer models show the same pull
from a prior judgment: in "Anchoring Bias in LLM-as-a-Judge Systems",
judges shown a prior wrong label corrected about half as many errors as
judges shown none (11.3% against 21.6%) and moved a tenth of correct
judgments to the label shown; a warning to disregard the label reduced
those moves without removing them, and asking for step-by-step reasoning
did not help (https://arxiv.org/abs/2608.25869). Its anchor is a label
on a rating task, not a rationale beside a diff; as of 2026-10-26 no
study found compares a verifier given the rationale with one given the
diff alone. Hence the fix list and the diff, never the rationale.
(Basis: measured; external.)

Skipping the verifier on MINOR-only waves was rejected on 2026-09-28,
because the catches it made were real; the same day it moved to the
bounded role, checking a fix list against a diff being a bounded task. A
recount (2026-10-12) found no detectable difference in misses between
verifiers on the default role's model and on the bounded role's (Fisher
exact p = 1.0, on a boundary chosen after seeing the data and per-day
model mixes), and the maintainer kept the bounded role, judging the
sample too small to show a difference. The same recount found half the
later verifiers leaving delta claims unchecked while their read scoping
put everything else out of scope; running a claim's check against the
files it names came into scope on 2026-10-13. That the earlier wording
caused the abstentions is an inference. (Basis: measured; the
maintainer's preference, for keeping the role; judgment, accepted by the
maintainer, for the scope.)

### Readouts and the trace

The coverage check on readouts used to run in a script: the round checks
ran 125 times after they shipped and never found a missing readout
entry, and they went with the parser on 2026-10-10. The readout's reader
is the operator, who acts on words; the ids serve the terminal pass and
the line counts the right-sizing judgment, so on 2026-10-13 both moved
to a trace the operator is not sent. (Basis: measured, for the check;
judgment, accepted by the maintainer, for the trace.) The line counts
left the trace on 2026-11-02, when the re-seat they served became the
controller's judgment (`docs/decisions/spec-campaign.md`).

## Rejected

- **An agent applying fix waves** (§ Why), unless a re-open condition
  above is met.
- **Skipping blind verification on MINOR-only waves** (§ Why).
- **A wrong-direction input to the verifier**: a list of affirmed
  decisions it checked reversals against. It was used in four to six
  features, raised one flag, ruled an intended reversal, and was
  removed on 2026-10-13; an entry whose fix reverses an earlier applied
  fix names it instead. (Basis: measured; judgment, accepted by the
  maintainer.)
- **A mechanical merge check**, by hand or by script: retired on
  2026-11-02 after about one trivial catch in about 73 runs (§ Why).
- **Parsing seat reports and records** to refuse shapes, exact headings
  or index mismatches (§ Why).

## Changes

- 2026-11-03: a `deferred-minor` entry is seeded into the ledger by SDD's Setup, the ledger's only seeding writer, not by the close of the plan phase or the folded campaign (`docs/decisions/records-and-workspace.md`).
- 2026-11-03: the round record's citations point at `skills/redteaming/references/round-record.md`, where § Round record format moved from `formats.md` so that a step reading `formats.md` for the workspace or the feature folder stops loading the round record (`docs/decisions/authoring-crucible.md`).
- 2026-11-03: the trace's decision-ask ids scoped as `formats.md`
  scopes them, to the numbered round records and the plan record.
- 2026-11-02: the readout's trace loses its line for the wave's line
  counts, and the delivered readout its rule against carrying them,
  the right-sizing re-seat they served having become the controller's
  judgment (`docs/decisions/spec-campaign.md`).
- 2026-11-02: fix lists, a plan-phase repair included, take only
  BLOCKER, MAJOR and binding-text MINOR findings; the disposition
  `deferred-minor` is added for the other MINORs, after
  Interfaces & boundaries, deferred-to-implementation and parked in
  precedence, seeded into the ledger's `## Deferred minors` with source
  `Spec` or `Plan`; because the skill text rewrite's audit found fix
  waves the main source of process-introduced defects.
- 2026-11-02: merge conservation retired with `conserve.py`: the round
  record's `conservation:` line and its `unaccounted:` element go, and
  the merge keeps `origins:` and question dispositions; seat ids stay
  unique, now for the stop check; because the skill text rewrite's audit
  found about one trivial catch in about 73 runs.
- 2026-10-26: the blind-verification reason adds a 2026 study of
  anchoring in LLM judges beside the 2023 Chain-of-Verification result,
  whose models are two generations old; the position is unchanged.
- 2026-10-13: blind verification after every wave on the bounded role,
  given the fix list and the diff only, checking delta claims against the
  tracked files they name and handing claims it cannot check to the
  controller.
- 2026-10-13: a ruling for every partly-applied, parked or rejected
  entry, the sub-point check at fix authoring, readouts naming those
  findings in words, and ids and line counts in a record-only trace.
- 2026-10-11: merge from the seat reports' indexes, conservation by token
  presence run as `conserve.py`, the controller stopping where it cannot
  run, and seat ids never reused within a feature.
- 2026-09-30: fix waves applied by the controller; a delegated applier
  declined.
