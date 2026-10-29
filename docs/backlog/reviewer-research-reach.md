# Reviewers' research reach and review methods

## Observation

- The maintainer observed that reviewers seemed more freeform in their
  research than the seats' read scopes suggest (2026-10-28), while ruling
  on how an umbrella reaches a child's reviewers. Not yet examined: which
  reviewers, which reads, and whether the reads went outside what each
  template admits.
- Which review methods catch what is unexamined too. An audit of the
  hypothesis-specs umbrella (2026-10-29) used methods none of the
  effort's reviews ran: a walkthrough of the routes, a trace from the
  request, a read for design smells. Of its 23 correctness findings, 12
  had never been seen during development.
- The same audit compared the effort's review seats by model, but the
  four that ran on the other host were all in first rounds, so stage and
  model are confounded:
  a difference between them could be the round's as much as the model's.

## Follow-up

- Sample review transcripts from recent runs, compare each seat's reads
  with its template's read scope and its dispatch's input list, and
  decide whether the scopes, the templates or nothing should change.
- Find which of the audit's methods would catch what the reviews missed,
  and at which stage, before adding any of them to a review.
- Compare seats by model with stage held fixed: seats on both hosts in
  the same round.
