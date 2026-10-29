# Premise findings and questions

What a seat may raise beyond an ordinary finding, and the form it takes.
Your template names the sections that apply to you.

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
