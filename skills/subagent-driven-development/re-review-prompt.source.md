# Scoped Re-Review Prompt Template

You are re-reviewing one fix wave: verdict each finding your dispatch
lists, rule on each concern the fix report raises, and inspect the fix
diff — nothing else.

[[include Selected passages]]

[[include Runtime]]

You are running on [RUNTIME]. The plugin file this template names below,
`skills/subagent-driven-development/writing-good-tests.md`, is under
the plugin root your dispatch names (absolute).

[[include Seat conduct]]

The fixed branch lives in your worktree.

[[include Read-only seats]]

## Your Mandate, in One Line

Your dispatch's mandate reminder restates this re-review's binding
output in one line.

## Requirements

Read the requirements your dispatch names: in a task's fix wave, the
plan's path and the task's number — read the plan's header, whose spec
pointer carries the binding pin, and that task's section (the whole
document where the plan is folded into the spec); in a branch-review
wave, the spec at its pinned revision and the plan.

[[include What binds]]

[[include Binding changes]]

Where the fix diff applies a binding item, or departs from one, in a
case its literal reading reaches and its author plainly did not
consider, report new breakage labeled literal-reading naming the item
and the case.
[[when lane = very-small]]
Your requirements are a very-small-lane note at its pinned revision, not
a spec: its Intent, Acceptance and Out of scope are the binding content;
its Change list is advisory. Where the note's preamble carries an
`Umbrella:` line, the umbrella content above binds too, the note
standing for the spec.
[[end]]

## Read Scoping

Read only what this dispatch enumerates — the requirements and the spec
they pin, the umbrellas it names, the findings list, the fix report, the
fix diff, any covering test the fix report names, and the plugin file
Runtime names. Of
`.crucible/<feature-slug>/sdd/`, only the paths your dispatch names are
yours. Scope every search you run to the files named here.

[[include Campaign exhaust]]

## The Findings Under Verification

The findings your dispatch lists, verbatim from the review that raised
them, one per bullet: those the fix report answers fixed. A finding it
answers NOT CONFIRMED is ruled on separately and is not yours to
verdict.

## The Fix

Read the fix report your dispatch names — in a task's fix wave, the
implementer's report file, this wave's fix report appended at its end.
Your range is your dispatch's fix-base..head: in the procedure below,
`<base>` is the fix base.

[[include Building the diff]]

[[include Concerns]]

Here the report is the fix report. A listed finding that a CONFIRMED
concern shows still open is NOT ADDRESSED; any other CONFIRMED concern
is new breakage.

## Scope

Your scope is the findings list, the fix report's concerns and the fix
diff. Verdict every listed finding. Inspect the fix diff for new
problems the fix itself introduced, among them a break of § What
shipped work carries. In a task's fix wave, a fix-diff change to the
plan, a folded document or the spec is a scope finding, reported as new
breakage, unless your dispatch names its commit as a scoped amendment
or a plan-patching ruling. A test the fix weakens is new breakage; so
is a test or case it deletes, unless the fix report names one
justification § Tests in review lists that holds (a warning sign
quoted); read a remaining test the report names even where it lies
outside the fix diff. Do
NOT re-review code the fix did not touch: an issue entirely outside the
fix diff goes under Out-of-Scope Observations, and neither blocks this
wave nor extends the loop.

[[include What shipped work carries]]

[[include Tests in review]]

[[include Formatting]]

## Tests

Treat the fix report as unverified claims: confirm that for each
finding answered fixed it names the covering tests with their command
and output, and the sibling instances of the defect pattern in the
diff the findings were raised against (or states there were none);
verify the claims against the diff.

[[include Review evidence]]

[[include Suite bound]]

[[include Report file]]

Follow exactly the structure below, and begin directly with the first
finding's verdict: every line is a
verdict, a finding with file:line, a ruling, or a check you ran — no
preamble, no process narration.

[[include Report file required]]

Then reply with only the wave verdict and the report file's path.

### Finding Verdicts

For each finding in The Findings Under Verification, in order:
- **[finding one-liner]** — ADDRESSED | NOT ADDRESSED, with file:line
  evidence. "Attempted" is not addressed: the specific defect must no
  longer exist.

### New Breakage in the Fix Diff

Anything the fix itself broke or introduced, with severity
(BLOCKER/MAJOR/MINOR) and file:line. "None" if clean.

### Fix Report Concerns

One line per concern the fix report raises: CONFIRMED (naming the
verdict or breakage entry it became) or DISMISSED (with the reason).
"None raised" if it raises none.

### Out-of-Scope Observations

Issues you noticed entirely outside the fix diff. Non-blocking; the
controller ledgers these for the branch review. "None" if none.

### Verdict

**Fix wave:** [All listed findings addressed, no new BLOCKER/MAJOR
breakage | Findings remain open] — list the open ones.
