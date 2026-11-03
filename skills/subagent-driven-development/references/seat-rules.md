# Seat rules

The rules the seat templates share. Each section reaches the seats that
follow it inside their templates, each template taking the sections its
seat follows, so no templated seat reads this file. A dispatch a
controller composes with no template carries, copied into its prompt,
the sections the skill composing it names.

Redteam seats, the terminal pass, the branch reviewer, an umbrella's closing-review seats and implementers raise premise findings; a task reviewer raises none.

## Seat conduct

Work from the worktree path your dispatch names (absolute). Never read,
edit, write or run git against any other checkout of this repository —
the main checkout in particular — and never change directory into one.
Create no agents of your own: delegation is not part of your
assignment. Read only what this template's read scoping enumerates, and
keep every search you run within the bounds it sets.

## Read-only seats

You edit nothing: not the artifact or the code under review, not the
rest of the codebase, not the feature workspace, and on this checkout
never the working tree, the index, HEAD or branch state. A seat that
fixes what it finds poisons what the review measures. You write two
things: your report file, and working material in your scratch
subdirectory — any diff you build, the code you run to check a claim —
never in the tracked tree. That subdirectory is your report's path
within the feature workspace less `.md`, in the workspace's `scratch/`
directory; what its material shows goes in your report.

## Review evidence

The report you verify quotes the test runs its author made for exactly
this code: do not re-run the suite to confirm it. Run a test only when
reading the code raises a specific doubt no existing run answers.
Evidence that looks truncated, or a result the report claims that you
cannot find, re-read at its stated path before reporting it missing;
what is then still missing or garbled is a gap you report, never a
reason to re-run the suite.

## Report file

Write your report to the report file your dispatch names, a write this
dispatch authorizes, in the structure this template gives: the file is
the deliverable. If the host refuses the write, say so and put the full
report in your final reply instead.

## What binds

What binds is the spec at its pinned revision, as your dispatch or your plan's spec pointer names it (a thin plan carries no constraints section of its own): its Constraints & invariants, any preamble convention it declares binding, and the decisions it records as the operator's firm preference. Where its preamble carries an `Umbrella:` line, what binds also includes this feature's own entry in that umbrella and the umbrella's Constraints & invariants and firm decisions, and through each umbrella's own line its parent's, up the chain: the umbrellas your dispatch names, read in this worktree at the revision you review. Read each where it lives. The spec is a hypothesis, probably subtly wrong: binding means never changed silently, and binding text is read for its intent.

## Binding changes

Grade the artifact or range under review against what binds: a change to any of those Constraints or firm decisions, to what an umbrella's Intent asks for, or to the entry of a started child, this feature's or another's, is a finding, whether the artifact calls for it or the range makes it; a child has started once its feature folder is born. This feature's own mark, and a clarification of its own entry that its spec states, changing nothing another entry waits on, are none, and neither is a binding change taken in from the base by a merge.

## Premise findings

A premise finding claims, with evidence, that one of three things is wrong: the request, what the Intent asks for, or a firm decision. The request is the request file your dispatch names, if any; the Intent is a section of the document, and a firm decision says so in its rationale. For a child of an umbrella, the umbrella's Intent is protected as the child's own is. Mark a premise finding with the label `premise` after the finding's severity, in the place this template's report format gives it, and stake that severity as for any finding: it is for the operator's weighing.

Every other decision, whoever proposed it, is lightly held: a finding against it is an ordinary one, structural or not, and so is a correction of an Intent's wording or facts, the umbrella's included, that leaves what it asks for unchanged. Any other binding item shown wrong, such as a Constraint, is no premise finding: it keeps the route this template gives it.

## Binding items and unrecorded choices

Two findings a reviewer raises beyond a defect in the work:

- **A binding item that is itself wrong** is a legitimate finding,
  naming the item and the evidence that shows it wrong; changing the
  item is never yours to do. A firm decision shown wrong is a premise
  finding instead (§ Premise findings).
- **A consequential choice the artifact you review takes for granted**
  with no decision recording it (the platform, the language, the form
  of the deliverable) is a finding.

## The goal check

Before you read the Intent, restate in one sentence the goal that the
request asks for: the request file your dispatch names, the feature
workspace's `request.md`, which quotes the messages that asked for the
work. Then compare your sentence with the Intent. A mismatch you can
stand behind is a premise finding; a vaguer one is a question. The
request is evidence of what was asked, not the standard: you may find
the request itself wrong.

For a child of an umbrella, the request holds only what was asked in the
child's own brainstorm and after it: compare your sentence with the
child's Intent, the umbrella's Intent and the child's entry in the
umbrella's Children list.

Where your dispatch names no request file or the file is missing, as in
a standalone branch review, restate the goal from the Intent and say
that the request was unavailable.

Write the sentence and what the comparison found where this template's
report format places them.

## Findings

Stake a severity on every finding, BLOCKER, MAJOR or MINOR and no other
vocabulary, and give it its evidence. A BLOCKER without evidence is a
question, not a blocker: downgrade it, or phrase it as a question.

## Location

Every finding carries its evidence and a location: `file:line`, or, for
a premise finding, the passage of the spec, plan or request it
contradicts.

## Formatting

Formatting no repository tool enforces (wrap width, line length,
whitespace) is not a finding; where a tool enforces it, the tool's
failure is the finding.

## Questions

Your report's `Questions` section holds anything material you could not
stake as a finding: a question, a doubt, a misgiving with nothing
specific to point to, or an improvement you would suggest. Improvements
and style preferences are never findings; an improvement worth making
goes here. Keep to a few items at most; for doubts and misgivings, none
is the normal case. An item carries no severity. Write each in the form
this template gives.

## What shipped work carries

Nothing the work ships — code, comments, docs, prompts — carries build
history: plan task numbers, spec section numbers, feature decision ids,
pointers to a feature's spec or plan, rulings carrying names or dates,
wave names, what was retired when. Build history belongs in commit
messages, decision records, changelogs and the feature folder's files,
which exist to hold it.

Comments and docstrings follow the project's conventions. Absent any, a
comment states the current invariant, hazard, or local reason a line
looks wrong but isn't; cites symbols rather than `file:line`; and points
to the owning reference doc or decision record where the project has
one.

## Silence is not permission

The requirements' silence is not permission. A failure on an input they
imply but never name (an empty file, a path with spaces, a second run)
is a defect, graded by its effect on a reasonable person using the
software, not by whether the requirements mention its trigger.

## Tests in review

A weakened test, made more permissive or with an assertion removed, is
a finding whatever a log says about it. A deleted test, or a deleted
case of a parametrized one, is a finding unless one justification
holds, borne out by the code:

- the subject the change removed;
- the remaining test covering the behavior, which exists and covers it;
- the requirement or review finding the deletion fulfils;
- a warning sign from
  `skills/subagent-driven-development/writing-good-tests.md` that fits
  the test.

## Test-first evidence

Test-first work shows its failing (RED) run before its passing (GREEN)
run, or the Decision Log records its exception with the reason: work
with no test seam, generated code, prose-only work, or a removal. A
removal's failing step is the removed path's own tests failing or being
deleted with it, never a new test that the removed thing is absent.

## Building the diff

Build the diff of your range, `<base>..<head>`, as files and read it
there, never from command output, which hosts cap below a diff's size.
Once `git cat-file -t` prints `commit` for each end and
`git merge-base --is-ancestor <base> <head>` exits 0, have git write
into your scratch subdirectory, `<scratch>` (create it first):

```
git log --oneline --output=<scratch>/commits.txt <base>..<head>
git diff --stat --patch -U10 --output=<scratch>/range.diff <base>..<head>
```

Read each once: the commit list, then a stat summary and the full diff
with surrounding context. An end that is not a commit, a base that is
not an ancestor of the head, or a failing git command, is reported in
place of a review: never review an empty diff.

## Concerns

Rule on each concern the report raises about its own work: CONFIRMED,
a finding at the severity you stake, or DISMISSED, with a one-line
reason. A concern left unruled is a missing verdict. The report's
premise findings, `Questions` items and fixes proposed outside its task
or wave are the controller's to route: rule on none of them as a
concern.
