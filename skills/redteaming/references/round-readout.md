## Round readout

At every round close the readout carries these items and nothing else:

- key findings, naming every rejected, parked or partly-applied BLOCKER/MAJOR in words the operator can act on, with its ruling;
- technical calls made autonomously;
- the round's `deferred-to-implementation` count;
- the questions carried to readout, each quoted as written, ids included — omitted where none is;
- in every numbered spec-campaign round, whether overturning a major mechanism after code is still reasonably expected, and why, answering each seat forecast of an expected overturn by the mechanism it names — omitted elsewhere;
- in the plan record and a folded campaign's terminal-pass record, the tasks the plan marks `Review: branch only`, each with its reason, as information, not an ask — omitted elsewhere and where no task carries the mark;
- a seat on another host that ended with no report, and what happened — omitted where none did;
- design judgments, as decision asks — omitted where none is.

An item is omitted only where its line says; an omitted item is dropped, not narrated as absent.

Beyond the quoted questions, the delivered readout carries no internal id (merged-list, seat-finding or question); what other readers need from the ids goes in its **trace**, the record-only part after it (`round-record.md` § Round record format, field 8).

Readout coverage is yours: beyond the terminal pass's check of carried questions, nothing checks it after you. Before recording, check the readout against the merged list and `## Question dispositions`. Then record the readout and its trace in the round record's `## Round readout`, write `state: readout`, and deliver the readout to the operator as recorded, less its trace; delivery closes the round.

Write an operator ruling or record correction that arrives after a round closed, dated, into that round's `## Rulings and corrections`; a ruling also enters `brainstorm-decisions.md` (status: `crucible:brainstorming` § Workspace provisioning).
