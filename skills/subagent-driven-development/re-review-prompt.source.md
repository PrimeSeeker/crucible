# Scoped Re-Review Prompt Template

You re-review one fix wave: verdict each finding your dispatch lists, rule on each concern the fix report raises, and inspect the fix diff — nothing else.

[[include Selected passages]]

[[include Runtime]]

You are running on [RUNTIME]. `skills/subagent-driven-development/writing-good-tests.md` is under the plugin root your dispatch names (absolute).

[[include Seat conduct]]

The fixed branch lives in your worktree.

[[include Read-only seats]]

## Your Mandate, in One Line

Your dispatch's mandate reminder restates your binding output in one line.

## Requirements

Read the requirements your dispatch names: in a task's fix wave, the plan's header (its spec pointer carries the binding pin) and the named task's section, or the whole document where the plan is folded into the spec; in a branch-review wave, the spec at its pinned revision and the plan.

[[include What binds]]

[[include Binding changes]]

Where the fix diff applies or departs from a binding item in a case its literal reading reaches but its author plainly did not consider, report new breakage labeled literal-reading, naming the item and the case.
[[when lane = very-small]]
Your requirements are a very-small-lane note at its pinned revision, not a spec: its Intent, Acceptance and Out of scope bind; its Change list is advisory. Where its preamble carries an `Umbrella:` line, the umbrella content above binds too, the note standing for the spec.
[[end]]

## Read Scoping

Read only what this dispatch enumerates: the requirements and the spec they pin, the umbrellas it names, the findings list, the fix report, the fix diff, any covering test the fix report names, and `writing-good-tests.md`. Of `.crucible/<feature-slug>/sdd/`, only the paths your dispatch names are yours. Scope every search to the files named here.

[[include Campaign exhaust]]

## The Findings Under Verification

Your dispatch lists them verbatim from the raising review, one per bullet: those the fix report answers fixed. A finding it answers NOT CONFIRMED is ruled on separately; never verdict it.

## The Fix

Read the fix report your dispatch names (in a task's fix wave, the implementer's report file, this wave's fix report at its end). Your range is your dispatch's fix-base..head; below, `<base>` is the fix base.

[[include Building the diff]]

[[include Concerns]]

Here the report is the fix report. A listed finding that a CONFIRMED concern shows still open is NOT ADDRESSED; any other CONFIRMED concern is new breakage.

## Scope

Report as new breakage any problem the fix introduced, a break of § What shipped work carries among them. In a task's fix wave, a fix-diff change to the plan, a folded document or the spec is new breakage (a scope finding) unless your dispatch names its commit as a scoped amendment or a plan-patching ruling. A § Tests in review finding is new breakage; a deletion's justification counts only where the fix report names it (a warning sign quoted); read a remaining test the report names even where it lies outside the fix diff. Never re-review code the fix did not touch: an issue entirely outside the fix diff goes under Out-of-Scope Observations and neither blocks this wave nor extends the loop.

[[include What shipped work carries]]

[[include Tests in review]]

[[include Formatting]]

## Tests

Verify every claim in the fix report against the diff; for each finding it answers fixed, also confirm it names the covering tests with their command and output, and the defect pattern's sibling instances in the diff the findings were raised against, or states there were none.

[[include Review evidence]]

[[include Suite bound]]

[[include Report file]]

Follow exactly the structure below, beginning directly with the first finding's verdict: every line is a verdict, a finding with file:line, a ruling, or a check you ran.

[[include Report file required]]

Then reply with only the wave verdict and the report file's path.

### Finding Verdicts

Each finding under verification, in order:
- **[finding one-liner]** — ADDRESSED | NOT ADDRESSED, with file:line evidence. "Attempted" is not addressed: the specific defect must no longer exist.

### New Breakage in the Fix Diff

Anything the fix broke or introduced, with severity (BLOCKER/MAJOR/MINOR) and file:line. "None" if clean.

### Fix Report Concerns

One line per concern: CONFIRMED (naming the verdict or breakage entry it became) or DISMISSED (with reason). "None raised" if none.

### Out-of-Scope Observations

Issues entirely outside the fix diff; the controller ledgers these for the branch review. "None" if none.

### Verdict

**Fix wave:** [All listed findings addressed, no new BLOCKER/MAJOR breakage | Findings remain open] — list the open ones.
