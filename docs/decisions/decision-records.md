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

- `## Decision`: the current position, in a few lines.
- `## Why`: the reasoning and evidence, restated in the record, each with
  its basis inline: **measured** (what, how often, on what),
  **external** (a host's documentation, an upstream file, another cited
  source), **the maintainer's preference** (quoted where it helps),
  **judgment** (an agent's proposal the maintainer accepted, attributed
  as such) or **a single incident**.
- `## Rejected`: only where an alternative would plausibly be proposed
  again: what, and why not.
- `## What a project may change`: only where a project's instruction
  files can override the decision.
- `## Changes`: one line per change, newest first,
  `<YYYY-MM-DD>: <what changed, and why>`.

A record states a position as held firmly only where the maintainer
said so: "the maintainer's preference" names a position's origin, not
its strength, and no existing record is re-read as firm. A plan task
that writes or edits a record names the feature's brainstorm decision
record among its inputs, and each position's basis is attributed from
its entry's proposer and status, the maintainer's preference where the
operator proposed it and judgment, accepted by the maintainer, where the
controller did (`crucible:writing-plans § Per-task structure — four
fields, all required`).

A section carries content or is absent; none says "N/A". Every edit adds
its Changes line in the same commit. At the port, a record got one
Changes line per position it states, ported or added beside the ported
ones, dated by the day that position took its current form.

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

## Rejected

- **An append-only log** whose entries supersede earlier ones by naming
  them: the form these records replace (§ Why).
- **Immutable records with a status line**, superseded by successor
  records: replaced before the first record was written (§ Why).
- **Dated names, and an index file** (§ Why).
- **Placeholder sections** ("N/A", "none") (§ Why).

## Changes

- 2026-10-28: a position is stated as firmly held only on the
  maintainer's word, the maintainer's preference naming its origin, not
  its strength; a task writing a record attributes each basis from the
  brainstorm decision record's proposer and status.
- 2026-10-20: records by family, edited in place with git history as the
  log, in place of the append-only log and the planned immutable records.
- 2026-10-20: slug-only names and no index file.
- 2026-10-20: the record shape, with the basis stated inline and a Changes
  line added by every edit.
