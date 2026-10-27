# Fix verification and merge

## Decision

**Merge from the indexes.** Every seat report opens with `## Index`, one
line per finding: id, severity, a one-sentence claim, an evidence
pointer. The controller merges from the indexes and opens a finding's
body only to author its fix, to rule on a contested finding or a
collision between seats, or where the line is not enough; questions are
read in full. Each merged entry names the per-seat finding ids it
absorbs in an `origins:` element
(`skills/redteaming/references/formats.md` § Round record format).

**Conservation by token presence.** At merge time in every numbered
panel round, the controller runs `conserve.py`: every finding and
question id the round's seat reports carry must occur in the round
record outside a recorded `unaccounted:` line. It reads no markdown
structure and refuses no layout; exit 2 means only a usage error or a
missing or unreadable input. The controller's own run is the only
conservation check, and where the script cannot run at all the
controller stops and tells the operator rather than reconciling by hand.
Seat ids are never reused within a feature, the plan phase's pre-pass id
`p0` excepted (`crucible:redteaming § Merge and finding hygiene`).

**Dispositions and rulings.** Each merged entry takes one disposition:
applied, partly-applied, parked, rejected or deferred-to-implementation.
Every partly-applied, parked or rejected entry carries a ruling, a
partly-applied one naming the part not acted on; nothing is silently
discarded. When the controller opens a finding's body to author its
fix, it checks each sub-point against the fix item, for a BLOCKER or
MAJOR the body of every origin. An entry whose fix reverses an earlier
round's applied fix names that round and entry.

**The controller applies the fixes.** It writes the fix list into the
round record and applies it to the spec or plan itself; no agent applies
a fix wave (`crucible:redteaming § Fix application and blind
verification`).

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
delivered readout carries no merged-list, seat-finding or question id
and no line counts. Those go in the record-only trace after it: each
decision ask's merged-list ids, which the terminal pass reads, and, in a
numbered spec-campaign round, the wave's line counts, which the
right-sizing re-seat reads. A readout delivered again after compaction
leaves its trace out (`crucible:redteaming § Round readout`).

## Why

### Merging from indexes

In a 2026-09-27 audit of crucible's token costs, the feature workspace's
records were 23% of the characters the controller read. An index line
lets the controller rule on most findings without opening their bodies
(2026-09-28). Nothing has held an index to its findings since the
conservation check stopped parsing reports (2026-10-10), an accepted
gap. (Basis: measured; judgment, accepted by the maintainer.)

### Conservation

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
costing a repair cycle. Checking token presence keeps the cheap part and
gives up the rest: a mistyped id, a mention counted as accounted and an
index that disagrees with its findings all go unchecked. An independent
re-run in the terminal pass was designed and grew, under review, into
contract changes across four files, so the controller's own run stays
the only one. (Basis: measured; judgment, accepted by the maintainer.)

The check moved to `conserve.py` under its own name on 2026-10-11. The
trade accepted there: a host with bash but no usable Python learns of
the missing interpreter only at the first `conserve.py` run, where the
controller stops and tells the operator. Unique seat ids keep a mention
of one round's id from accounting for another round's finding; the
plan phase's `p0` exception was the controller's call, delegated by the
maintainer (2026-10-10). (Basis: judgment, accepted by the maintainer.)

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
judgment, accepted by the maintainer, for the trace.)

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
- **An independent conservation re-run** in the terminal pass or at
  round close (§ Why).
- **Parsing seat reports and records** to refuse shapes, exact headings
  or index mismatches (§ Why).

## Changes

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
