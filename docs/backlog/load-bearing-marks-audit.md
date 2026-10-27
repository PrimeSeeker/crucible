# How much crucible's specs mark load-bearing

## Observation

- A `[LOAD-BEARING]` mark binds the sentence it annotates: changing it
  takes a supersede or a scoped amendment, an operator decision. A spec's
  Constraints & invariants section binds as a whole.
- Counting marks in the specs and folded documents of crucible's own
  features: the first two carried 27 and 15 (August 2026); the ones
  since October carry 0 to 7, most 2 or 3. The Constraints sections are
  not in that count.
- The maintainer, on 2026-10-27: "we're probably marking too many points
  as load-bearing". Upstream, by v7.0.1, went the other way from crucible:
  its controller rules on a load-bearing finding at the fix loop's cap
  and carries on, where crucible's stops and asks the operator.
- How often a mark actually changed a run (a STOP, a supersede, a
  decision ask raised by a ruling that touched one) is not counted.

## Follow-up

Count, across past features' records, each mark and Constraints
item that triggered a stop, a supersede, a scoped amendment or a decision
ask, against those that never did. If most marks never bind anything, tighten
brainstorming's guidance on what earns a mark.
