# A full-scope pass after a wave of a few sentences

## Observation

`crucible:requesting-code-review § The branch-review loop` runs a full-scope
pass after every wave, the cleanup wave included. Whatever the wave's size,
that pass costs what the branch's size costs. On a 2026-11-04 lane a cleanup
wave changed a few sentences in six files of text and passed its scoped
re-review; the further pass would have cost about 275k tokens, and the
maintainer left the call to the agent, which skipped it. On another lane the
same day, a wave of three minors ended the same way. Neither case shows
whether the skipped pass would have found anything. On a third lane that day
the pass ran after a wave of six findings, three of them MAJOR, on a branch of
text: about 155k tokens, no BLOCKER or MAJOR, two MINORs extending the wave's
own fix to two more sites.

On a fourth lane that day, the pass ran after a cleanup wave of six minors and
four small wording and rule changes, which its scoped re-review had passed.
At about 199k tokens it found a MAJOR in that wave's text: a new rule whose
review read one report over a range two runs wrote. The scoped re-review could
not see it, since it needed the reviewer's card, outside the fix diff. The next
full pass, after a one-clause wave, cost about 187k tokens and found three
MINORs. So a wave of a few sentences that adds a rule can need the full pass;
what is unsettled is a wave that adds none.

## Follow-up

Decide whether a small wave of prose needs more than its scoped re-review,
and if so what makes a wave small, without file, line or task counts. Whether
the wave adds or changes a rule, rather than its wording, is a candidate test.
