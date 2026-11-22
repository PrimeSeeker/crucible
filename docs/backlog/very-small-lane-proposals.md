# The very-small lane and the last full read: three proposals

Each came from a controller's process notes on two prose-only features
built back to back on the very-small lane. The maintainer has seen them
and not ruled.

## Observation

- What the last full-scope pass finds at MINOR can only be filed, or fixed
  on the maintainer's word, the one cleanup wave being spent or the fix
  not worth a wave and a further pass. On those two features and the one
  before them, four of six findings left that way were statements in a
  decision record that were false or misattributed; such records instruct
  no agent. The other two were a sentence of skill text and a backlog
  item. Dropping the pass after a minors-only wave, and skipping it
  for a wave that changes no rule, were both rejected on evidence
  (`docs/decisions/branch-review.md`).
- A lane note is "shown with the lane proposal" and written "as the
  operator approved it" (`skills/brainstorming/references/lane-note.md`),
  while its binding parts bind the branch reviewer and the maintainer
  reads it as the reviewer's document. On both features the controller
  showed the design in a few numbered items and wrote the note fuller,
  recording the difference as its own call. The reviewer's goal check
  already holds the note against the operator's recorded messages.
- A lane note's Acceptance must be runnable checks that fail on the old
  tree. For prose that produced searches for exact wording: on one
  feature two of six checks searched for sentences the branch reviewer
  then improved, and since Acceptance binds, each rewording took the
  maintainer's decision and a re-pin of the note. The searches passed on
  every run of both features.

## Follow-up

Put each to the maintainer; each is a sentence or two of skill text.

- Let the controller correct a false or misattributed statement in a
  decision record after the last full-scope pass, with no wave and no
  further pass, naming the correction in the close readout. The cost:
  nobody reviews the correction.
- Have the operator approve the design and the lane, the controller write
  the note, and the reviewer's goal check hold it against the request.
  The cost: the operator no longer approves the note's exact exclusions.
- For a change that is prose only, have Acceptance take the suite and
  structural checks (a file exists or is gone, generated files match
  their sources) and no search for wording, the rule the repository
  already applies to its tests (`AGENTS.md`, Authoring rules).
