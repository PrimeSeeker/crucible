# Premise findings and questions

What a seat may raise beyond an ordinary finding, and the form it takes;
and the arrangement questions, which seats apply, as do the controllers
that propose a feature's arrangement, stop a spec campaign, mark a
plan's tasks or work a task inline. Your template or skill names
the sections that apply to you.

## Premise findings

A premise finding claims, with evidence, that something the operator
asked for or decided is wrong: the request itself, what the Intent asks
for, or a decision the operator made or holds firm, the chosen approach
included where the operator chose it. Mark it with the label `premise`
after the finding's severity, as in `FINDING s2-3 [MAJOR] premise`, and
stake that severity as for any finding: it is for the operator's
weighing.

What separates it from an ordinary finding is who stands behind what you
challenge, as the document records each decision's basis. A decision the
operator only accepted from the controller's proposal is lightly held: a
finding against it is an ordinary one, structural or not, and so is a
correction of the Intent's wording or facts that leaves what it asks for
unchanged. A firm decision or a lane note's Intent shown wrong is a
premise finding; any other binding item shown wrong stays the finding
your template already names for it. A `literal-reading` finding keeps its
own label: it questions how a binding item applies to a case, not the
premise behind it.

Redteam seats, the branch reviewer and implementers raise premise
findings. A task reviewer that doubts a premise writes the doubt in its
`Questions` (§ Questions).

## The goal check

Before you read the Intent, restate in one sentence the goal that the
`## Request` section asks for: the section of the document whose Intent
you grade against, which quotes the messages that asked for the work.
Then compare your sentence with the Intent. A mismatch you can stand
behind is a premise finding; a vaguer one is a question. The request is
evidence of what was asked, not the standard: you may find the request
itself wrong.

Reviewing a plan, restate the goal from the `## Request` section of the
spec its header names, and compare it with that spec's Intent and with
the plan's Goal.

Where no `## Request` section exists, as in a document written before
the section was required or a standalone branch review, restate the goal
from the Intent and say that the request was unavailable.

Write the sentence and what the comparison found where your template's
report format places them.

## Questions

Your report's `Questions` section holds anything material you could not
stake as a finding: a question, a doubt, a misgiving with nothing
specific to point to, or an improvement you would suggest. Improvements
and style preferences are never findings; an improvement worth making
goes here. Keep to a few items at most; for doubts and misgivings, none
is the normal case. An item carries no severity. Write each in the form
your template gives.

## Location

Every finding carries its evidence and a location: `file:line`, or, for
a premise finding, the passage of the spec, plan or request it
contradicts.

## The arrangement questions

Each site that applies one of these says what its answer decides there.

**The overturn question.** Once the work is coded, is overturning one of
its major mechanisms plausible? A major mechanism is a part of the
design other parts build on: a component, a rule others key on, a file
role, a data flow, an interface between parts. Overturning one replaces,
removes or re-shapes it; an addition, or a correction that leaves its shape
standing, does not count. Before code the answer is a forecast from the
design and its records; after code it is read from the code as well.

Before any review, the answer is no in two cases only:

- the work has no major mechanism: it adds to, corrects or removes
  within mechanisms that stay as they are;
- its decisions are overdetermined.

For an umbrella's campaign, the code is its children's: the question
asks whether implementing the children could plausibly overturn a
major mechanism the umbrella fixes, such as its split into children, an
interface between them or a constraint they share.

**Overdetermined.** Work, a whole design or a single task, is
overdetermined when every decision in it is forced by what is already
fixed (the codebase, binding items, decisions taken earlier) so firmly
that no alternative survives them: a careful independent reader would
make the same choices, so neither review before code nor a fresh
reader's pass has one left to change.

**The mark's criterion.** A plan task may take the branch review as its
first review, with no task review of its own, where it is low in
mechanism and nothing outside it depends on its details: it builds no
major mechanism and leaves little of how it works for its implementer
to decide, and later tasks, contracts and readers build on what it
delivers, never on how it does it. The branch review runs only after
every later task, too late for a detail something else builds on.
