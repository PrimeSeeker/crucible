# Decision records

## Decision

Crucible's design decisions are recorded in `docs/decisions/`, one file
per family of related decisions, named by its slug alone, with no index
file. A record states the decision as it stands and is edited in place
when the decision changes; git history is the log, and there is no status
line or supersede chain. A reversal worth remembering becomes a line
under Rejected. A retired decision's record is deleted; where the retired
option could plausibly return, a related record's Rejected part says so.

A record's sections, in order:

- `## Decision`: the current positions, each in a sentence or two, with a
  pointer (`docs/authoring.md` § Reference convention) to the skill
  heading that holds the procedure rather than a restatement of it. What
  no skill holds stays here. A position not yet cut to this shape takes
  it when an edit rewrites that position; a clause-sized edit leaves it,
  and the record's other positions stay as they are.
- `## Why`: the reasoning and evidence, restated in the record, each with
  its basis inline: **measured** (what, how often, on what),
  **external** (a host's documentation, an upstream file, another cited
  source), **the maintainer's preference** (quoted where it helps),
  **judgment** (an agent's proposal the maintainer accepted, attributed
  as such, or "judgment, an agent's call the maintainer has not ruled
  on", naming the call) or **a single incident**.
- `## Rejected`: only where an alternative would plausibly be proposed
  again: what, and why not.
- `## What a project may change`: only where a project's instruction
  files can override the decision.
- `## Changes`: one line per change to a decision or its reasoning, newest
  first, `<YYYY-MM-DD>: <what changed, and why>`.

A record states a position as held firmly only where the maintainer
said so: "the maintainer's preference" names a position's origin, not
its strength, and no existing record is re-read as firm. A plan task
that writes or edits a record names the feature's brainstorm decision
record among its inputs, and each position's basis is attributed from
its entry's proposer and status, the maintainer's preference where the
operator proposed it and judgment, accepted by the maintainer, where the
controller did (`crucible:writing-plans § Per-task structure`). An
entry recorded `accepted — delegated to the
controller` is judgment, accepted by the maintainer, its text saying
that the maintainer left the call to the agent, never stating it as the
maintainer's ruling or choice.

A section carries content or is absent; none says "N/A". An edit that
changes a decision or its reasoning adds its Changes line in the same
commit; an edit that changes neither, such as a citation, wording or a cut
of restated text, adds none, and its commit says what it did. Existing
lines stay. At the port, a record got one Changes line per position it
states, ported or added beside the ported ones, dated by the day that
position took its current form.

A change that makes a record untrue edits it in the same change. Records
cite crucible's files by path and heading (`docs/authoring.md`
§ Reference convention) and each other by path; nothing crucible ships
cites a record. `AGENTS.md` sends how a rule was learned (incidents,
measurements, accepted trade-offs) here.

## Why

### Living records

The append-only log these records replace made a reader rebuild a
position from a chain of entries, each superseding or amending the last
by naming the clause it changed: the rule on how much a spec may grow
during review took five entries between 2026-08-05 and 2026-10-10. An
audit of that log against the tree (2026-10-17) also found the discipline
leaking: entries that changed earlier ones without naming them, and a
shipped wording change in a skill that no entry recorded. A record edited
in the same change as its decision holds one current statement, and git
keeps the earlier ones. (Basis: measured, by reading the log and the
audit's claim checks.)

On 2026-10-15 the plan was immutable records, one per decision, each with
a status line (Accepted, or Superseded by another record) as the only
part ever changed: an agent's call, which the maintainer accepted. On
2026-10-20, before any record was written, the maintainer observed that
records grouped by family would need further edits anyway; an agent
proposed living records on that ground, and the maintainer accepted.
(Basis: judgment, accepted by the maintainer.)

A record that a later change contradicted without an edit would read as
live while the skills say otherwise. That nearly happened once: a
feature's controller ruled that it needed no log entry, and the branch
review overturned the call, because three live positions would otherwise
have been ported contradicting the shipped skills. (Basis: a single
incident, 2026-10-15.)

A change that leaves every recorded decision as it stands edits no
record: a model release that keeps the roles, the seats' assignments and
the triggers is one (`docs/dual-runtime.md` § Model floor and effort
policy).

### Names and shape

A date in a file name goes stale at the first in-place edit, and an index
file is a second list to keep true beside the directory. (Basis:
judgment, accepted by the maintainer on 2026-10-20.)

The basis labels come from the 2026-10-15 design, with **judgment** added
so that an agent's proposal the maintainer accepted is never recorded as
the maintainer's preference. Rejected and What a project may change appear
only where they say something: an agent flagged placeholder sections as
bureaucracy, and the maintainer agreed. (Basis: judgment, accepted by the
maintainer on 2026-10-20.)

A Changes part in every record is the maintainer's addition: living
records "would probably involve a local changelog as well". Its shape, a
dated line per change added by the edit's own commit, was an agent's
proposal the maintainer confirmed. (Basis: the maintainer's preference,
for the changelog; judgment, accepted by the maintainer, for its shape;
2026-10-20.)

Evidence is restated rather than cited because the records are read
without the history they came from; quoting the maintainer is fine.
(Basis: judgment, accepted by the maintainer on 2026-10-17; quoting is
the maintainer's own allowance.)

### When an edit takes a Changes line

Until 2026-11-04 every edit to a record added a Changes line. By then the
records held 395 lines totalling 15,946 words, 19% of the records' words.
About two dozen only followed a moved citation or a removed mark (a keyword
search, likely an undercount), and 171 were dated in the two days of the
2026-11 skill rewrite. A search of the repository outside the records found
the branch reviewer the only reader, checking that they exist. (Basis:
measured.)

A line now goes with an edit that changes a decision or its reasoning, and
the commit carries the rest: an agent's proposal, which the backlog item
had suggested. The maintainer's "OK" answered a recommendation whose
sentence did not separate this option from removing the sections
altogether; the controller said so and took this one, which loses nothing.
(Basis: judgment, accepted by the maintainer, 2026-11-04.)

### A Decision points at procedure

The reference scanner catches a renamed or removed heading a record cites,
but not changed content, so a Decision restating a skill could go untrue
with no test failing, and each skill edit forced a repeat edit. A one-off
screen, its script not kept, took each Decision sentence's content words and
the largest share of them in any one paragraph of the shipped skills: 48% of
the words were in sentences at 0.6 or above, 37% between 0.4 and 0.6 and 16%
below; it misses paraphrase and does not search `AGENTS.md` or `docs/`. Eight
records held 65% of the high-overlap words. (Basis: measured.) Those eight
were cut first, with no word target, and the other 22 were to follow when
their Decisions were next edited, since a citation fix should not carry a
whole cut: an agent's proposal, which the maintainer accepted. (Basis:
judgment, accepted by the maintainer, 2026-11-04.)

Read literally, that made a one-clause edit carry a cut of the whole record.
The next two lanes edited uncut Decisions and cut none; the second changed 24
diff lines in five of them, which held about 26 KB of Decision text in about
117 KB of record. (Basis: measured.) So a position takes the short shape when
an edit rewrites it, and the rest waits. Nothing now brings the remaining
records to that shape on any schedule, so their restated procedure can still
go untrue with no test failing: an agent's proposal, stating that cost and that
it withdrew the earlier rule, which the maintainer accepted. (Basis: judgment,
accepted by the maintainer, 2026-11-04.)

On 2026-11-05 one seat, on the default role, checked the 22 records' Decisions
against the shipped text: about 463 statements by its own split, 5 it graded
untrue, 11 true but missing a condition and 3 it could not test, for want of
upstream's text at the version cited, for 376k tokens. Read by hand, 13 of
the 16 held and 3 did not; two of the 13 were shared by a shipped sentence,
so the check also found skill text no test could. Those were fixed once, and
the goal of cutting the rest was retired: nothing crucible ships reads a
record, so a wrong one misleads only someone editing it, against about 78 KB
of Decision text to cut and review. Positions still take the short shape when
an edit rewrites them. Nothing repeats the check, so restatements can go out
of step again unseen. An agent's recommendation, stating that cost and that
it withdrew the earlier plan to cut them, which the maintainer accepted, after
asking for the check first. (Basis: measured, by one seat, a lower bound;
judgment, accepted by the maintainer, 2026-11-05.)

### Origin and strength

On crucible's umbrella-specs feature (2026-10-28), the task that wrote a
decision record could not see the brainstorm decision record, and tagged
every position "judgment, accepted by the maintainer", the maintainer's
own included. Naming that record among the task's inputs, for its
implementer and its task reviewer, was an agent's follow-up the
maintainer agreed to. (Basis: a single incident; judgment, accepted by
the maintainer.)

With approvals recorded `accepted` by default and `firm` only on the
operator's word (`docs/decisions/the-spec.md`), "the maintainer's
preference" could be read as firmness; the sentence keeping origin and
strength apart was an agent's proposal, the maintainer leaving the call
to it ("your call"). (Basis: judgment, accepted by the maintainer,
2026-10-28.)

The brainstorm decision record records a call left to the controller
as `accepted — delegated to the controller`, never as the operator's
ruling or choice (`docs/decisions/the-spec.md`). The attribution rule
named only the operator and the controller as proposers, so the
delegated form, which the paragraph above already used, became part of
it. An agent's proposal, which the maintainer accepted. (Basis:
judgment, accepted by the maintainer, 2026-10-29.)

## Rejected

- **An append-only log** whose entries supersede earlier ones by naming
  them: the form these records replace (§ Why).
- **Immutable records with a status line**, superseded by successor
  records: replaced before the first record was written (§ Why).
- **Dated names, and an index file** (§ Why).
- **Placeholder sections** ("N/A", "none") (§ Why).
- **Cutting the remaining records in a lane of their own**: about 78 KB of
  Decision text and its reviews, against the few statements a full check
  found out of step (§ Why).
- **Removing the Changes sections**, for now: the changelog was the
  maintainer's own addition (§ Why), and the maintainer has not reversed it.

## Changes

- 2026-11-05: the goal of cutting the remaining 22 records is retired, with a one-off repair of what a check of them confirmed; because nothing shipped reads a record and the check found few statements out of step.
- 2026-11-04: a position not yet cut takes the short shape when an edit rewrites it, no longer a whole record at the next edit of its Decision; because a clause-sized edit would have carried a far larger cut, and the lanes making such edits did not follow it.
- 2026-11-04: a Changes line goes with an edit that changes a decision or its reasoning, no longer every edit, and a Decision points at the skill heading holding the procedure rather than restating it; because the lines were a fifth of the records' words with one reader, and restated procedure could go untrue with no test failing.
- 2026-11-03: the citation of writing-plans' per-task structure uses its shortened heading.
- 2026-10-30: an entry recorded `accepted — delegated to the
  controller` is attributed as judgment, accepted by the maintainer,
  saying the maintainer left the call to the agent, since the
  attribution rule named no form for it; and an agent's call the
  maintainer has not ruled on gets its own judgment form, since the
  plain label reads as the maintainer's acceptance.
- 2026-10-28: a position is stated as firmly held only on the
  maintainer's word, the maintainer's preference naming its origin, not
  its strength; a task writing a record attributes each basis from the
  brainstorm decision record's proposer and status.
- 2026-10-20: records by family, edited in place with git history as the
  log, in place of the append-only log and the planned immutable records.
- 2026-10-20: slug-only names and no index file.
- 2026-10-20: the record shape, with the basis stated inline and a Changes
  line added by every edit.
