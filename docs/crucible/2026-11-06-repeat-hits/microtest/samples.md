# Replies

## p1: open-items rule, today's reference

### Sample 1

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER or MAJOR findings with
  their rulings, the deferrals D23 brings) becomes one grouped entry per
  feature in the project's home for deferred work, each item in it, and
  those the controller judges not worth keeping named dropped there; no
  item takes a ruling of its own, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before
  the suite, so the suite runs once on the tree that lands; no review
  reads it on a first pass through Finish, so the close readout names the
  entry, and where the loop reopens, the branch reviewer takes that
  commit as in scope, as it takes the umbrella mark. Outside the
  repository (an issue tracker): the readout proposes the entry, filed
  only on the operator's word. No home known: the readout proposes one.
  Unruled asks are not filed; the readout asks them. A later answer
  revises the entry when Finish restarts. The operator's integration
  decision is carried out, and the workspace deleted, only once every
  item is filed or named dropped: an unanswered filing proposal is not a
  drop, a declined one is, and while one stands unanswered the controller
  says so and integrates nothing. Acceptance: with a tracker or no known
  home, an operator who leaves the proposal unanswered and chooses a pull
  request gets no pull request yet, the proposal asked again and the
  workspace kept. This reverses the recorded position that filing open
  work is left to the operator or the repository's conventions: the
  filing is the controller's step, made where the convention says.

Moves the existing hold from workspace deletion to the integration decision too, replacing that sentence and adding no store or fallback; a declined proposal counts as a drop, so the hold cannot deadlock.
Adds parked BLOCKER or MAJOR findings with their rulings to the parenthesis, and an acceptance item from the finding's reproducer.
Limit: the hold does not reach a pull request the operator opens outside the session, where the items stay only in the workspace.

### Sample 2

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER and MAJOR findings with
  their rulings, the deferrals D23 brings) becomes one grouped entry per
  feature in the project's home for deferred work, each item in it, and
  those the controller judges not worth keeping named dropped there; no
  item takes a ruling of its own, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before the
  suite, so the suite runs once on the tree that lands; no review reads it
  on a first pass through Finish, so the close readout names the entry,
  and where the loop reopens, the branch reviewer takes that commit as in
  scope, as it takes the umbrella mark. Outside the repository (an issue
  tracker): the readout proposes the entry. No home known: the readout
  proposes one. Either proposal goes with the integration ask, and the
  integration decision is not carried out until the operator has answered
  it: the entry filed, or its items named dropped. Unruled asks are not
  filed; the readout asks them. A later answer revises the entry when
  Finish restarts. The workspace is deleted only once every item is filed
  or named dropped. This reverses the recorded position that filing open
  work is left to the operator or the repository's conventions: the filing
  is the controller's step, made where the convention says. Acceptance:
  with an outside tracker or no known home, an operator who chooses a pull
  request and leaves the proposal unanswered gets no pull request and is
  asked the proposal again; a parked MAJOR finding appears in the entry
  with its ruling.

Adds parked BLOCKER and MAJOR findings with their rulings to the items the entry takes, and adds the acceptance item.
Replaces the unanswered-proposal state with a gate on the integration decision, deleting "an unanswered filing proposal is not a drop" and "the workspace stays", which that state alone needed.
Residual: the gate binds only integration the controller carries out; a merge the operator runs outside Finish is out of its reach.

### Sample 3

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER or MAJOR findings with
  their rulings, the deferrals D23 brings) becomes one grouped entry per
  feature in the project's home for deferred work, each item in it, and
  those the controller judges not worth keeping named dropped there; no
  item takes a ruling of its own, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before the
  suite, so the suite runs once on the tree that lands; no review reads it
  on a first pass through Finish, so the close readout names the entry,
  and where the loop reopens, the branch reviewer takes that commit as in
  scope, as it takes the umbrella mark. Outside the repository (an issue
  tracker): the readout proposes the entry, filed only on the operator's
  word. No home known: the readout proposes one. Unruled asks are not
  filed; the readout asks them. A later answer revises the entry when
  Finish restarts. A filing proposal is answered before integration: while
  it stands unanswered, which is not a drop, the controller carries out no
  integration decision, a pull request included, and says that integration
  waits and the workspace stays. The workspace is deleted only once every
  item is filed or named dropped. This reverses the recorded position that
  filing open work is left to the operator or the repository's
  conventions: the filing is the controller's step, made where the
  convention says. Acceptance: with no known home or with an outside
  tracker, an operator who chooses a pull request and leaves the proposal
  unanswered gets no pull request, a readout saying integration waits on
  the proposal, and the workspace with its items intact.

Adds parked BLOCKER or MAJOR findings with their rulings to the entry's list.
Makes an unanswered filing proposal hold integration, replacing "the controller says the workspace stays", and adds the reproducer as an acceptance item; one site, D22.
Limit: a pull request the operator opens by hand outside Finish is not stopped; the workspace stays and the controller has said so, since no crucible-owned store exists to hold the items.

### Sample 4

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER or MAJOR findings with
  their rulings, the deferrals D23 brings) becomes one grouped entry per
  feature in the project's home for deferred work, each item in it, and
  those the controller judges not worth keeping named dropped there; no
  item takes a new ruling, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before
  the suite, so the suite runs once on the tree that lands; no review
  reads it on a first pass through Finish, so the close readout names the
  entry, and where the loop reopens, the branch reviewer takes that commit
  as in scope, as it takes the umbrella mark. Outside the repository (an
  issue tracker): the readout proposes the entry, which reaches the
  tracker only on the operator's word. No home known: the readout proposes
  one. Where such a proposal is still unanswered when the branch is
  integrated, the pull request's description, or a local merge's commit
  message, carries the entry, and that files it. Unruled asks are not
  filed; the readout asks them. A later answer revises the entry when
  Finish restarts. The workspace is deleted only once every item is filed
  or named dropped: until then an unanswered filing proposal is not a
  drop, and the controller says the workspace stays. This reverses the
  recorded position that filing open work is left to the operator or the
  repository's conventions: the filing is the controller's step, made
  where the convention says.

  Acceptance: with an outside tracker or no known home, the operator
  leaves the filing proposal unanswered and integrates through a pull
  request: the pull request's description holds the entry, every item in
  it, and the controller deletes the workspace. A parked MAJOR with its
  ruling at Finish: the entry holds it with that ruling.

Changes: an unanswered proposal at integration now files the entry in the pull request's description or local merge's commit message, so no tree change or suite re-run follows and the workspace can go in the same session.
Adds parked BLOCKER and MAJOR findings with their rulings to the entry; "no item takes a new ruling" replaces "a ruling of its own", which those would contradict.
Adds the acceptance item the finding's reproducer requires; the local merge is included because it strands items the same way.

### Sample 5

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER or MAJOR findings with
  their rulings, the deferrals D23 brings) becomes one grouped entry per
  feature in the project's home for deferred work, each item in it, and
  those the controller judges not worth keeping named dropped there; no
  item takes a ruling of its own, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before the
  suite, so the suite runs once on the tree that lands; no review reads it
  on a first pass through Finish, so the close readout names the entry,
  and where the loop reopens, the branch reviewer takes that commit as in
  scope, as it takes the umbrella mark. Outside the repository (an issue
  tracker): the readout proposes the entry, filed only on the operator's
  word. No home known: the readout proposes one. Integration waits on
  either proposal: the operator's answer files the entry or names its
  items dropped, and an unanswered proposal is not a drop. Unruled asks
  are not filed; the readout asks them. A later answer revises the entry,
  or commits it to the home named, when Finish restarts. The workspace is
  deleted only once every item is filed or named dropped. This reverses
  the recorded position that filing open work is left to the operator or
  the repository's conventions: the filing is the controller's step, made
  where the convention says. Acceptance: no home known or an outside
  tracker, the proposal unanswered, the operator asks for a pull request:
  no pull request opens, the controller repeats the proposal, and the
  workspace stays.

Integration now waits on an outside-tracker or no-home proposal, so silence can't strand items; this replaces "the controller says the workspace stays" and adds the reproducer's acceptance item.
Parked BLOCKER or MAJOR findings with their rulings join the entry's parenthesis; an answer naming a home in the repository commits on Finish's restart, so the suite still runs on the tree that lands.
No new store or fallback is added; an operator who merges by hand outside the session stays uncovered.

## p2: open-items rule, with the rule

### Sample 1

- **D22 — Work left open outlasts the workspace: it lands on the branch at
  Finish, filed or named dropped.** At SDD's Finish, the work left open
  (minors, leads, questions, declined improvements, parked BLOCKER and
  MAJOR findings with their rulings, the deferrals D23 brings) becomes one
  grouped entry per feature, each item in it, and those the controller
  judges not worth keeping named dropped there; no item takes a ruling of
  its own, so "no ruling per minor" stands. The controller commits the
  entry on the branch beside the umbrella mark, before the suite, so the
  suite runs once on the tree that lands and every way of integrating the
  branch carries the entry, answered or not. It goes in the project's home
  for deferred work when that is in the repository, and otherwise at a path
  the readout names; no home known, the readout proposes that path as the
  home. No review reads the commit on a first pass through Finish, so the
  close readout names the entry, and where the loop reopens, the branch
  reviewer takes that commit as in scope, as it takes the umbrella mark. A
  home outside the repository (an issue tracker): the readout also proposes
  the entry there, filed only on the operator's word. Unruled asks are not
  filed; the readout asks them. A later answer moves or revises the entry
  when Finish restarts. The workspace is deleted only once the entry is
  committed; from then on it holds no item the branch lacks, so losing it
  loses no item. This reverses the recorded position that filing open work
  is left to the operator or the repository's conventions: the filing is
  the controller's step, made where the convention says.
  Acceptance: with the home outside the repository or none known, the
  proposal unanswered and the branch integrated through a pull request, the
  integrated tree holds the entry with every item in it or named dropped, a
  parked finding with its ruling among them, and removing the workspace
  loses no item.

Replaces D22 from its purpose (repeat hit): the entry is always committed on the branch before the suite, so no route depends on an answer; the workspace-stays and unanswered-proposal clauses go, no longer needed.
Adds parked BLOCKER and MAJOR findings with their rulings to the entry, and an acceptance item for the unanswered-proposal, pull-request case.
Trade-off: a project with an outside tracker or no home gets a committed entry unless the operator moves it; tracker filing still needs the operator's word.

### Sample 2

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped, before the branch is integrated.** The workspace
  holding that work is gitignored and nothing returns to it after
  integration. At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER and MAJOR findings
  with their rulings, the deferrals D23 brings) becomes one grouped entry
  per feature in the project's home for deferred work, each item in it,
  and those the controller judges not worth keeping named dropped there;
  no item takes a ruling of its own, so "no ruling per minor" stands. In
  the repository: committed on the branch beside the umbrella mark, before
  the suite, so the suite runs once on the tree that lands; no review
  reads it on a first pass through Finish, so the close readout names the
  entry, and where the loop reopens, the branch reviewer takes that commit
  as in scope, as it takes the umbrella mark. Outside the repository (an
  issue tracker): the readout proposes the entry, filed only on the
  operator's word. No home known: the readout proposes one, and the entry
  then takes that home's case. The operator may answer either proposal by
  naming the whole entry dropped. Unruled asks are not filed; the readout
  asks them. A later answer revises the entry when Finish restarts. Until
  every item is filed or named dropped, the controller carries out no
  integration decision and deletes no workspace, and the readout says so:
  an unanswered proposal is not a drop. This reverses the recorded
  position that filing open work is left to the operator or the
  repository's conventions: the filing is the controller's step, made
  where the convention says. Acceptance: with an outside tracker or no
  known home, the proposal unanswered and the operator choosing a pull
  request, no pull request is opened, and the readout repeats the proposal
  and says the workspace stays.

Replaces D22 (repeat hit) around its purpose: filing or a named drop now precedes integration, so an unanswered proposal holds the integration instead of stranding the items; no new store or fallback location.
Adds parked BLOCKER and MAJOR findings with their rulings to the entry, the operator's drop of a whole entry as the way out of the hold, and the reproducer as an acceptance item.
Limit: this binds the controller only, so a pull request the operator opens outside the session can still strand the items.

### Sample 3

- **D22 — Work left open outlasts the workspace: before the branch is
  integrated, it is filed where the project keeps deferred work, or named
  dropped.** The workspace is gitignored and may see no later session, so
  no item depends on it. At SDD's Finish, the work left open (minors,
  leads, questions, declined improvements, parked BLOCKER and MAJOR
  findings with their rulings, the deferrals D23 brings) becomes one
  grouped entry per feature in the project's home for deferred work, each
  item in it, and those the controller judges not worth keeping named
  dropped there; no item takes a ruling of its own, so "no ruling per
  minor" stands. In the repository: committed on the branch beside the
  umbrella mark, before the suite, so the suite runs once on the tree that
  lands; no review reads it on a first pass through Finish, so the close
  readout names the entry, and where the loop reopens, the branch reviewer
  takes that commit as in scope, as it takes the umbrella mark. Outside
  the repository (an issue tracker), or with no home known: the readout
  gives the entry in full and proposes where it goes, and it is filed only
  on the operator's word; a repository home so named takes the repository
  case and restarts Finish, and an entry the operator declines is named
  dropped in the readout. The controller carries out no integration
  decision, a pull request included, while that proposal stands
  unanswered: it repeats the proposal and says the branch and the
  workspace stay. Unruled asks are not filed; the readout asks them. A
  later answer revises the entry when Finish restarts. The workspace is
  deleted only after integration, every item by then filed or named
  dropped. The filing is the controller's step, made where the convention
  says, replacing the recorded position that leaves it to the operator or
  the repository's conventions. Acceptance: with an outside tracker or no
  known home, the proposal unanswered and the operator choosing a pull
  request, no pull request opens and the readout repeats the proposal with
  the entry in full; once the operator answers, it opens with every item
  filed or named dropped. A parked MAJOR with its ruling appears in the
  entry.

Replaces D22 (its one site, third round on this passage) from its purpose: an unanswered filing proposal now holds integration, so the stranded case cannot arise through the controller, and the "unanswered is not a drop" clause goes as redundant.
Adds parked BLOCKER and MAJOR findings with their rulings to the entry's contents, and an acceptance item for the finding's input.
Limit: an operator merging by hand, past the controller, is outside this hold; there the readout's full entry text is all that survives the workspace.

### Sample 4

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped, before the branch is integrated.** What a feature
  leaves open must outlast its workspace. At SDD's Finish, the work left
  open (minors, leads, questions, declined improvements, parked BLOCKER
  and MAJOR findings with their rulings, the deferrals D23 brings)
  becomes one grouped entry per feature in the project's home for
  deferred work, each item in it, and those the controller judges not
  worth keeping named dropped there; no item takes a ruling of its own,
  so "no ruling per minor" stands. In the repository: committed on the
  branch beside the umbrella mark, before the suite, so the suite runs
  once on the tree that lands; no review reads it on a first pass through
  Finish, so the close readout names the entry, and where the loop
  reopens, the branch reviewer takes that commit as in scope, as it takes
  the umbrella mark. Outside the repository (an issue tracker), or with
  no home known: the readout proposes the entry, and the home where none
  is known, as part of the ask for the integration decision. The
  operator's one answer files the entry or names its items dropped; an
  answer placing it in the repository takes the path above. An unanswered
  proposal is not a drop, and no integration, a pull request included, is
  carried out on it: the controller says the branch and the workspace
  stay, and asks again. Unruled asks are not filed; the readout asks
  them. A later answer revises the entry when Finish restarts. The
  workspace is deleted only once every item is filed or named dropped.
  This reverses the recorded position that filing open work is left to
  the operator or the repository's conventions: the filing is the
  controller's step, made where the convention says.
  Acceptance: with an issue tracker or no known home, the operator
  chooses a pull request and leaves the proposal unanswered: no pull
  request is opened, the proposal is asked again, and the branch and the
  workspace stay. A parked MAJOR with its ruling appears in the entry
  with that ruling.

Replaces D22 from its purpose, so filing or a named drop comes before integration in every kind of home, rather than adding a third clause to the workspace rule.
Adds parked BLOCKER and MAJOR findings with their rulings to the entry, and an acceptance item for the unanswered proposal and for a parked finding.
Adds no capability, since it only holds the controller's existing integration step; an operator who merges by hand outside Finish is not stopped, and the workspace then stays.

### Sample 5

- **D22 — Work left open is filed where the project keeps deferred work,
  or named dropped.** At SDD's Finish, the work left open (minors, leads,
  questions, declined improvements, parked BLOCKER or MAJOR findings with
  their rulings, the deferrals D23 brings) moves out of the workspace
  before the branch is integrated, so that no item's only copy goes with
  the workspace. It becomes one grouped entry per feature in the
  project's home for deferred work, each item in it, and those the
  controller judges not worth keeping named dropped there; no item takes
  a ruling of its own, so "no ruling per minor" stands. In the
  repository: committed on the branch beside the umbrella mark, before
  the suite, so the suite runs once on the tree that lands; no review
  reads it on a first pass through Finish, so the close readout names the
  entry, and where the loop reopens, the branch reviewer takes that
  commit as in scope, as it takes the umbrella mark. Outside the
  repository (an issue tracker), or no home known: the readout gives the
  entry's text and proposes filing it there, or proposes a home for it,
  and the operator's one answer files the entry or names it dropped. The
  operator's integration decision, a pull request included, is carried
  out only once that answer is in; until then the readout repeats the
  proposal and says the workspace stays. Unruled asks are not filed; the
  readout asks them. A later answer revises the entry when Finish
  restarts. The workspace is deleted once the integration decision is
  carried out. This reverses the recorded position that filing open work
  is left to the operator or the repository's conventions: the filing is
  the controller's step, made where the convention says.
  Acceptance: with an issue tracker or no known home, the proposal
  unanswered and the operator choosing a pull request, no pull request is
  opened, and the readout repeats the proposal and says the workspace
  stays; once the operator answers, the entry is filed or named dropped,
  the pull request opens and the workspace is deleted.

Replaces D22 from its purpose: an unanswered proposal now holds the integration decision, so a controller-opened pull request can't strand items, and the workspace's stay rule reduces to deletion after integration.
Adds parked BLOCKER or MAJOR findings with their rulings to the items, has the readout carry the entry's text, and adds the acceptance item.
Limit: an operator integrating by hand outside the session can't be held; there the readout's text is the only copy outside the workspace, which is not a filing.

## p4: finding rule, today's reference

### Sample 1

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. Within the range it
  reviews, a change to the umbrella that D8 keeps off a child's branch is
  a finding when the branch itself makes it, and not when it came in by
  merging the base. A successor — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

Replaces the by-kind finding rule and its exception with one rule: the test is what D8 keeps off a child's branch, and who made the change, so D8's allowed edits (the `landed` mark, the stated clarification) and merged-in base changes raise nothing.
Adds acceptance item 1: a child's branch review whose range changes the umbrella only by the child's `landed` mark raises no finding on it.
Adds acceptance item 2: a review whose range holds a merge of the base carrying an operator-approved change to Constraints & invariants raises no finding on it.

### Sample 2

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. Within the range it
  reviews, a change to any of them is a finding unless D8 lets it ride
  the child's branch or it came in by merging the base as D8 directs. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

Replaces D7's split finding sentence with one rule: a change to that content in the reviewed range is a finding unless D8 lets it ride the child's branch or it came in by merging the base.
This clears the child's `landed` mark and the merged operator-approved change; the clarification exception now rests on D8's own conditions, no longer restated here.
Adds acceptance items: a branch review whose range holds the child's own `landed` mark raises no finding on it; one whose range holds an operator-approved binding change taken in by merging the base raises no finding on it.

### Sample 3

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. Within the range it
  reviews, a change the child's branch makes to the umbrella that D8
  does not allow there is a finding; a change it takes in by merging
  the base is not. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

Replaces the sentence split by kind of content, with its exception, by one rule that defers to D8: a branch's own umbrella change is a finding unless D8 allows it, and a merge of the base is not one.
The `landed` mark and the stated clarification now pass as D8-allowed with no list of exceptions; the rule also now catches other edits D8 bars, such as to a started sibling's entry.
Adds an acceptance item: with a child's `landed` mark, or an operator-approved binding change merged from the base under D8, in the reviewed range, the review raises no finding on it.

### Sample 4

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. Within the range it
  reviews, a change to the umbrella's Constraints & invariants or
  [LOAD-BEARING] marks is a finding, and a change to the child's own
  entry is one unless it is the clarification D8 allows and the child's
  spec states it, or the child's own mark (D9). What D8's merge takes in
  from the base unaltered is no finding. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

D7 only: excepts the child's own mark (D9) from the finding rule on its own entry, and excepts what D8's merge takes in from the base unaltered from the rule as a whole.
A merge that alters the base's text in binding content stays a finding.
Acceptance item: a branch review whose range holds only the child's own `landed` mark and an operator-approved binding change merged in from the base raises no finding on either.

### Sample 5

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. Within the range it
  reviews, a change to the umbrella's Constraints & invariants or
  [LOAD-BEARING] marks is a finding, and a change to the child's own
  entry is one unless D8 allows it on a child's branch. A change taken
  in by merging the base, as the base has it, is not a finding. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

The own-entry exception now points at D8's whole allowance, so it covers the child's mark and the clarification without restating either.
A new sentence clears a binding change taken in by a base merge; "as the base has it" keeps a merge that alters that change a finding.
Acceptance item: a branch review whose range holds the child's own `landed` mark, or a base merge carrying an operator-approved binding change, raises no finding on either.

## p3: finding rule, with the rule

### Sample 1

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. A child's branch changes
  what binds the child only as D8 allows: within the range a seat
  reviews, any other change the branch itself makes to that content is a
  finding, and what the branch took in by merging the base under D8 is
  not its own change. A successor — by supersede, unfold or the
  very-small lane's upgrade hatch — carries its predecessor's line. A
  child that existed before its umbrella carries no line and is bound by
  nothing in it.

Replaces the finding rule, patched in two earlier rounds, with one sentence from its purpose: D8 alone says what a child's branch may change, so the `landed` mark and the clarification need no exceptions listed here.
Limits the finding to changes the branch itself makes, so an operator-approved change merged in from the base under D8 no longer reads as one; it adds no mechanism.
Adds an acceptance item: a child's branch review whose range holds the child's own `landed` mark, or a merge of the base carrying an operator-approved change to the umbrella's Constraints & invariants, raises no finding on either.

### Sample 2

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. What binds a child changes
  on its branch only as D8 allows: within the range a seat reviews, a
  change the branch itself makes beyond that is a finding, and a change
  merged in from the base is not the branch's own. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

Repeat hit: replaces D7's finding sentence and its by-kind split and exception with one rule stated from its purpose, a child's branch changing binding content only as D8 allows.
The `landed` mark and the stated clarification now pass because D8 allows them, and a change taken in by merging the base is not the branch's own; no new capability.
Acceptance item: a child's own `landed` mark, and an operator-approved change merged in from the base inside the range, each raise no finding; a change the branch itself makes to the umbrella's Constraints & invariants still does.

### Sample 3

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. A child's branch changes
  what binds it only as D8 allows: within the range a seat reviews, any
  other change the branch itself makes to that content is a finding, and
  one taken in by merging the base is not the branch's own. A successor
  — by supersede, unfold or the very-small lane's upgrade hatch — carries
  its predecessor's line. A child that existed before its umbrella
  carries no line and is bound by nothing in it.

Repeat hit: replaces D7's finding sentences with one rule stated from their purpose, a child's branch changes what binds it only as D8 allows, dropping the split by kind of content and the single exception.
D8's allowances now decide what passes, so the `landed` mark and a clarification stated in the spec pass, while an unstated clarification or a branch's own edit to Constraints & invariants or marks stays a finding; site: D7 only.
Acceptance item: a child's branch whose only entry change is its own `landed` mark, or whose range holds an operator-approved binding change taken in by merging the base, draws no finding on that change at branch review.

### Sample 4

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. What binds a child is not
  the child's branch to change: within the range a seat reviews, a change
  the branch itself makes to any of it is a finding, unless D8 lets a
  child's branch make it. A change taken in by merging the base under D8
  is not the branch's own. A successor — by supersede, unfold or the
  very-small lane's upgrade hatch — carries its predecessor's line. A
  child that existed before its umbrella carries no line and is bound by
  nothing in it.

Replaces the split finding rule, now stated from its purpose; D8's own list covers the clarification and the `landed` mark, and "any of it" also reaches parents' content, which D8 already keeps off a child's branch.
Acceptance item 1: a child's branch review whose range holds the child's own `landed` mark in its entry raises no finding on that mark.
Acceptance item 2: a range holding an operator-approved change to the umbrella's Constraints & invariants, taken in by merging the base under D8, raises no finding on that change.

### Sample 5

- **D7 — The umbrella line.** A child's spec, folded document, lane note
  or umbrella carries in its preamble a line ``Umbrella: `<path>` ``.
  What binds the child then includes its own entry, and the umbrella's
  Constraints & invariants and [LOAD-BEARING] marks, and, through the
  umbrella's own line, its parent's, up the chain. Every seat that
  receives binding content reads them there as binding, in the worktree
  it works in, at the commit its review reads. A child's branch changes
  what binds it only as D8 lets a change ride that branch: within the
  range a seat reviews, any other change the branch itself makes to that
  content is a finding, and what the base already holds, taken in by D8's
  merge, is not the branch's change. A successor
  — by
  supersede, unfold or the very-small lane's upgrade hatch — carries its
  predecessor's line. A child that existed before its umbrella carries no
  line and is bound by nothing in it.

Repeat hit (round 4, terminal pass): replaces the finding rule with one stated from its purpose, the branch's own changes judged against D8, so the `landed` mark and the stated clarification pass through D8; the rule now also reaches the parent's content, which D8 already keeps off a child's branch.
Acceptance item: a range whose only change to the child's entry is its own `landed` mark draws no finding; a range holding a base merge that carries an operator-approved Constraints & invariants change draws none; the same change made by the branch's own commit, or by a merge result differing from the base, is a finding.
Sites: D7 only.

## p6: small correction, with the rule

### Sample 1

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time: a search of those paths and
  `docs/decisions/umbrellas.md` for the words that name them, "no new
  mechanism", "blast radius" and "worth reviewing", each matched with any run
  of whitespace or hyphens between its words, so no wrapped or hyphenated form
  escapes, quoted, run before (hits, `skills/brainstorming/SKILL.md`'s
  "cross-subsystem blast-radius" among them) and after (none in that sense).

Repeat hit, so this replaces the search rather than adding a fifth phrase: it now matches the naming words across any whitespace or hyphens, and the two "blast radius" variants collapse into one term.
Acceptance: the search must hit the hyphenated phrase in `skills/brainstorming/SKILL.md` before the change, and find none in that sense after it.
This search was not run in this exercise; the controller must run it and put the command and output under the item before recording it applied.

### Sample 2

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time, to show the wording is gone however it is written:
  a search treating spaces, line breaks and hyphens between words alike, for
  "no new mechanism", "blast radius across subsystems", "cross-subsystem
  blast radius" and "worth reviewing" over those paths and
  `docs/decisions/umbrellas.md`, quoted, run before (hits,
  `skills/brainstorming/SKILL.md`'s "cross-subsystem blast-radius" among them)
  and after (none in that sense).

Repeat hit (rounds 0-2), so this replaces A1's search sentence from its purpose, showing the wording is gone however written, instead of adding a fifth phrase.
The search now treats spaces, line breaks and hyphens between words alike; paths, phrases and the Changes exception are unchanged.
The finding's reproducer becomes acceptance: the hyphenated form in `skills/brainstorming/SKILL.md` must show among the before hits.

### Sample 3

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time: a search that finds their wording however it is
  wrapped or hyphenated, for "no new mechanism", "blast radius" and "worth
  reviewing" with any run of whitespace or hyphens between the words, over
  those paths and `docs/decisions/umbrellas.md`, quoted, run before (hits) and after (none in
  that sense).

Replaces the search's description (repeat hit) with what it is for: finding the wording in any wrapping or hyphenation, so "cross-subsystem blast-radius" now counts as a hit.
Cuts the two blast-radius variants to the "blast radius" they share, so no further variant needs listing; paths, the Changes set-aside and the before/after run are unchanged.
The search has not been run in this exercise; the item still needs its command and output before it is recorded applied.

### Sample 4

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time: a search for their wording in any form, treating
  whitespace and hyphens between words alike, for "no new mechanism",
  "blast radius" and "worth reviewing" over those paths and
  `docs/decisions/umbrellas.md`, quoted, run before (hits, among them
  "cross-subsystem blast-radius" in `skills/brainstorming/SKILL.md`) and
  after (none in that sense).

Repeat hit, so this replaces the search rather than adding a fourth patch: it now states its purpose, any written form of the wording, and treats whitespace and hyphens alike.
The two "blast radius" word orders collapse into one root phrase, so a new order or hyphenation needs no further phrase; paths and the before/after run stay as they were.
The finding's reproducer becomes the required before-run hit; the search itself has not been run here, so it must run on the tree, command and output under the item, before this is recorded applied.

### Sample 5

- **A1.** The shape test and the "worth reviewing" split are gone from
  `skills/`, `README.md` and `docs/decisions/routes.md`, its Changes
  section aside. One-time, to show no written form of them survives: a
  search ignoring case and treating whitespace and hyphens alike, for
  "no new mechanism", "blast radius" and "worth reviewing" over those
  paths and `docs/decisions/umbrellas.md`, quoted, run before (hits) and
  after (none in that sense).

Replaces A1's search, a repeat hit, with one stated from its purpose: separators and case no longer split a phrase, so the hyphenated form is found.
Folds the two blast-radius phrases into "blast radius"; the paths, the Changes exception and the before/after run stay as they were.
The search itself is not run here (no tree in view); the command and its output still go under the item, with the before run showing the hyphenated hit in `skills/brainstorming/SKILL.md`.
