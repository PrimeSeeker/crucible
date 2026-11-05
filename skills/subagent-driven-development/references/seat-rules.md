# Seat rules

Redteam seats, the terminal pass, the branch reviewer, an umbrella's closing-review seats and implementers raise premise findings; a task reviewer raises none.

## Selected passages

A passage from a line `[[when <selector> = <value>]]` to a line `[[end]]` applies only where your dispatch sets that selector to that value; any other is inert: never perform, attest or mention it.

## Runtime

Use your host's own tools for files, commands and skills; never re-run the top-level router.

## Seat conduct

Work from the absolute worktree path your dispatch names. Never read, edit, write, run git against or change directory into any other checkout of this repository, the main checkout in particular. Create no agents of your own.

## Read-only seats

You edit nothing, the feature workspace included, and never change this checkout's working tree, index, HEAD or branch state: a fix poisons what the review measures. You write only your report file and, in the scratch subdirectory your dispatch names, working material (a diff you build, code you run to check a claim), never in the tracked tree; report what the material shows.

## Campaign exhaust

Never read `.crucible/<feature-slug>/campaigns/`: you work from the converged spec, never the argument that produced it.

## Review evidence

The report you verify quotes its author's test runs for exactly this code: do not re-run the suite to confirm them; run a test only when reading the code raises a specific doubt no existing run answers. Re-read evidence that looks truncated, or a claimed result you cannot find, at its stated path before reporting it missing; report what is then still missing or garbled as a gap, never re-run the suite for it.

## Report file

Write your report, in this template's structure, to the report file your dispatch names (a write it authorizes): the file is the deliverable. If the host refuses the write, say so and put the full report in your final reply.

## Report file required

Write the report file even where your host advises returning findings as text.

## What binds

What binds is the spec at the revision your dispatch or your plan's spec pointer names: its Constraints & invariants, any preamble convention it declares binding, and the decisions it records as the operator's firm preference. Where its preamble carries an `Umbrella:` line, what binds also includes this feature's own entry in that umbrella, the one naming its feature folder's slug, and the umbrella's Constraints & invariants and firm decisions, and through each umbrella's own line its parent's, up the chain: the umbrellas your dispatch names, read in this worktree at the revision you review. Read each where it lives. The spec is a hypothesis, probably subtly wrong: binding means never changed silently, and binding text is read for its intent.

## Binding changes

Grade the artifact or range under review against what binds: a change to any of those Constraints or firm decisions, to what an umbrella's Intent asks for, or to a started child's entry (its feature folder exists), this feature's or another's, is a finding, whether the artifact calls for it or the range makes it. Not findings: this feature's own mark; a clarification of its own entry that its spec states, changing nothing another entry waits on; a binding change a merge takes in from the base.

## Premise findings

A premise finding claims, with evidence, that one of these is wrong: the request (the request file your dispatch names, if any), what the Intent asks for, or a firm decision (one its rationale calls firm). For a child of an umbrella, the umbrella's Intent is protected as the child's own is. Label the finding `premise` after its severity, where your report format puts it, and stake that severity as for any finding, for the operator to weigh.

Every other decision, whoever proposed it, is lightly held: a finding against it is ordinary, structural or not, as is a correction of an Intent's wording or facts, the umbrella's included, that leaves what it asks for unchanged. Any other binding item shown wrong, such as a Constraint, is no premise finding: it keeps the route this template gives it.

## Binding items and unrecorded choices

Beyond defects in the work, these are findings:

- a binding item that is itself wrong, naming it and the evidence; changing it is never yours to do. A firm decision shown wrong is a premise finding instead.
- a consequential choice the reviewed artifact takes for granted with no decision recording it (the platform, the language, the form of the deliverable).

## The goal check

Before you read the Intent, restate in one sentence the goal asked for in the request file your dispatch names (`request.md`, quoting the messages that asked). Compare your sentence with the Intent: a mismatch you can stand behind is a premise finding, a vaguer one a question. The request is evidence of what was asked, not the standard; you may find it wrong.

For an umbrella's child, the request holds only what was asked from the child's own brainstorm on; compare your sentence with both Intents and the child's entry in the umbrella's Children list.

If your dispatch names no request file or the file is missing, restate the goal from the Intent and say the request was unavailable.

## Findings

Stake a severity on every finding (BLOCKER, MAJOR or MINOR, no other vocabulary) and give its evidence. A BLOCKER without evidence is a question: downgrade it or phrase it as one.

## Location

Every finding carries its evidence and a location: `file:line`, or, for a premise finding, the passage of the spec, plan or request it contradicts.

## Formatting

Formatting no repository tool enforces (wrap width, line length, whitespace) is not a finding; where a tool enforces it, the tool's failure is the finding.

## Questions

Your report's `Questions` section holds anything material you could not stake as a finding, a few items at most: a question, an improvement worth making, or a doubt or misgiving with nothing specific to point to (normally none). Improvements and style preferences are never findings. Each item takes the form your report format gives, with no severity.

## What shipped work carries

Nothing the work ships (code, comments, docs, prompts) carries build history: plan task or spec section numbers, feature decision ids, pointers to a feature's spec or plan, rulings with names or dates, wave names, what was retired when. That belongs in commit messages, decision records, changelogs, the feature folder and open items in the project's home.

Comments and docstrings follow project conventions; absent any, a comment states the current invariant, hazard, or local reason a line looks wrong but isn't, cites symbols rather than `file:line`, and points to any owning reference doc or decision record.

## Silence is not permission

A failure on an input the requirements imply but never name (an empty file, a path with spaces, a second run) is a defect, graded by its effect on a reasonable person using the software, not by whether the requirements mention its trigger.

## Tests in review

A deleted test, parametrized case or assertion, or any other change making a test more permissive, is a finding unless one of these holds for what was deleted or loosened, borne out by the code:

- the change removed its subject;
- a remaining test covers the behavior;
- the deletion or loosening fulfils a requirement or review finding;
- a warning sign from `skills/subagent-driven-development/writing-good-tests.md` fits it.

## Test-first evidence

Test-first work shows its failing (RED) run before its passing (GREEN) one, or the Decision Log records its exception and reason, one of: no test seam, generated code, prose-only work, or a removal. A removal's failing step is the removed path's own tests failing or being deleted with it, never a new test that the removed thing is absent.

## Building the diff

Read your range's diff, `<base>..<head>`, from files, never from command output, which hosts truncate. Once `git cat-file -t` prints `commit` for each end and `git merge-base --is-ancestor <base> <head>` exits 0, create your scratch subdirectory `<scratch>` and have git write into it:

```
git log --oneline --output=<scratch>/commits.txt <base>..<head>
git diff --stat --patch -U10 --output=<scratch>/range.diff <base>..<head>
```

Read `commits.txt`, then `range.diff`, each once. A failed check or git command is reported in place of a review: never review an empty diff.

## Concerns

Rule on each concern the report raises about its own work: CONFIRMED (a finding at a severity you stake) or DISMISSED (with a one-line reason); one left unruled is a missing verdict. The report's premise findings, `Questions` items and fixes proposed outside its task or wave are the controller's to route, never concerns to rule on.
