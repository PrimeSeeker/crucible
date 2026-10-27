# Scoped Re-Review Prompt Template

You are re-reviewing one fix wave: verdict each finding your dispatch
lists and inspect the fix diff — nothing else.

**Selected passages:** a passage opened by a line
`[[when <selector> = <value>]]` and closed by a line `[[end]]` applies
only where your dispatch's slot card sets that selector to that value.
Any other such passage is inert: do not perform it, attest it or mention
it.

## Runtime

You are running on [RUNTIME]. Use this host's own tools for editing
files, running commands and loading a skill; do not re-run the
top-level router. The plugin file this template names below,
`skills/subagent-driven-development/writing-good-tests.md`, is under
the plugin root your dispatch names (absolute).

## Where You Work

Work from the worktree path your dispatch names (absolute); the fixed
branch lives there. Binding:
- Read only in that worktree and the plugin file Runtime names. Never
  edit, write, or run git against any other checkout of this repo — the
  main checkout in particular — and never change directory into one.
- Your review is read-only on this checkout: never mutate the working
  tree, the index, HEAD, or branch state. Your only writes are your
  report file and, in your scratch subdirectory, the diff you build and
  the code you run to check a claim. That subdirectory is your report's
  path within the feature workspace less `.md`, in the workspace's
  `scratch/` directory — from the worktree root,
  `.crucible/<feature-slug>/scratch/sdd/reports/task-3-re-review-w1/`
  for `sdd/reports/task-3-re-review-w1.md` — never in the tracked tree;
  what that code shows goes in your review.
- Create no agents of your own.

## Your Mandate, in One Line

Your dispatch's mandate reminder restates this re-review's binding
output in one line.

## Requirements

Read the requirements your dispatch names: in a task's fix wave, the
plan's path and the task's number — read the plan's header, whose spec
pointer carries the binding pin, and that task's section (the whole
document where the plan is folded into the spec); in a branch-review
wave, the spec at its pinned revision and the plan. What binds is the
spec at that revision: its Constraints & invariants, its [LOAD-BEARING]
marks, and any preamble convention it declares binding. Where the spec's
preamble carries an `Umbrella:` line, what binds also includes this
feature's own entry in that umbrella and the umbrella's Constraints &
invariants and [LOAD-BEARING] marks, and through each umbrella's own
line its parent's, up the chain: the umbrellas your dispatch names, read
in this worktree at the revision you review. Within the range you
review, a change to those Constraints or marks is a finding, and so is a
change to the entry other than the feature's own mark or a clarification
its spec states that changes nothing another entry waits on; a binding
change taken in from the base by a merge is not. Read each there; none
is copied into this prompt.
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
Runtime names. Never read `.crucible/<feature-slug>/campaigns/`: that
exhaust of the spec campaign and plan phase is not evidence about
whether these findings were addressed. Of
`.crucible/<feature-slug>/sdd/`, only the paths your dispatch names are
yours. Scope every search you run to the files named here.

## The Findings Under Verification

The findings your dispatch lists, verbatim from the review that raised
them, one per bullet: those the fix report answers fixed. A finding it
answers NOT CONFIRMED goes to an adjudicator and is not yours to
verdict.

## The Fix

Read the fix report your dispatch names — in a task's fix wave, the
implementer's report file, this wave's fix report appended at its end.
Build the diff of your dispatch's fix-base..head range as files and
read it there, never from command output, which hosts cap below a
diff's size. Once `git cat-file -t` prints `commit` for each end and
`git merge-base --is-ancestor <fix-base> <head>` exits 0, have git
write into your scratch subdirectory, `<scratch>` (create it first):

```
git log --oneline --output=<scratch>/commits.txt <fix-base>..<head>
git diff --stat --patch -U10 --output=<scratch>/range.diff <fix-base>..<head>
```

Read each once — the fix commits, then a stat summary and the fix
diff with surrounding context. An end that is not a commit, a fix base
that is not an ancestor of the head, or a failing git command, goes to
the controller in place of a re-review: never verdict against an empty
diff.

## Scope

Your scope is the findings list and the fix diff. Verdict every
listed finding. Inspect the fix diff for new problems the fix itself
introduced — among them build history in anything the fix ships (plan
task numbers, spec section numbers, feature decision ids, pointers to
a feature's spec or plan, rulings carrying names or dates, wave names,
what was retired when; decision records and changelogs exempt) and,
absent project comment conventions, a `file:line` citation in a
comment. Formatting no repo tool enforces (wrap width, line length,
whitespace) is not a finding; where a tool enforces it, the tool's
failure is. In a task's fix wave, a fix-diff change to the plan, a
folded document or the spec is a scope finding, reported as new
breakage, unless your dispatch names its commit as a scoped amendment
or a plan-patching ruling. A test the fix weakens (made more
permissive, an assertion removed) is new breakage; so is a test or
case it deletes, unless the fix report names one justification that
holds: the subject the change removed; the remaining test covering the
behavior, which you read where it lies outside the fix diff; the
requirement or review finding the deletion fulfils; or a warning sign
from `skills/subagent-driven-development/writing-good-tests.md`, quoted,
that fits the test. Do NOT re-review code the fix did not touch: an issue entirely outside the fix diff goes under Out-of-Scope
Observations, and neither blocks this wave nor extends the loop.

## Tests

Treat the fix report as unverified claims: confirm that for each
finding answered fixed it names the covering tests with their command
and output, and the sibling instances of the defect pattern in the
diff the findings were raised against (or states there were none);
verify the claims against the diff. Evidence that looks truncated, or
results it claims that you cannot find, re-read at its stated path
before reporting it missing. Do not re-run the suite to confirm the
report. Run a test only when reading the code raises a specific
doubt no existing run answers — a focused test, never a package-wide
suite.

## Report

Write your report to the report file your dispatch names, in exactly
the structure below. Begin directly with the first finding's verdict:
every line is a verdict, a finding with file:line, or a check you ran
— no preamble, no process narration. The file is required even where
your host advises returning findings as text. Then reply with only the
wave verdict and the report file's path. If the host refuses the write,
say so and put the full report in that reply instead.

### Finding Verdicts

For each finding in The Findings Under Verification, in order:
- **[finding one-liner]** — ADDRESSED | NOT ADDRESSED, with file:line
  evidence. "Attempted" is not addressed: the specific defect must no
  longer exist.

### New Breakage in the Fix Diff

Anything the fix itself broke or introduced, with severity
(BLOCKER/MAJOR/MINOR) and file:line. "None" if clean.

### Out-of-Scope Observations

Issues you noticed entirely outside the fix diff. Non-blocking; the
controller ledgers these for the branch review. "None" if none.

### Verdict

**Fix wave:** [All listed findings addressed, no new BLOCKER/MAJOR
breakage | Findings remain open] — list the open ones.
