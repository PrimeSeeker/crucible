## Round readout

At every round close the readout carries these items and nothing else:

- key findings, naming every rejected, parked or partly-applied BLOCKER/MAJOR in words the operator can act on, with its ruling;
- technical calls made autonomously;
- the round's `deferred-to-implementation` count;
- the questions carried to readout, each stated in plain words, then quoted as written with its id — omitted where none is;
- in every numbered spec-campaign round, whether overturning a major mechanism after code is still reasonably expected, and why, answering each seat forecast of an expected overturn by the mechanism it names — omitted elsewhere;
- in the plan record and a folded campaign's terminal-pass record, the tasks the plan marks `Review: branch only`, each with its reason, as information, not an ask — omitted elsewhere and where no task carries the mark;
- a seat on another host that ended with no report, and what happened — omitted where none did;
- each fresh look since the last readout, with what you did with it — omitted where none ran;
- in a spec campaign, the terminal pass's wait (`crucible:redteaming` § Stop rule and terminal pass) — omitted where nothing holds it;
- in a spec campaign's close, each ruling whose change waits for it (below) — omitted where none does;
- design judgments, as decision asks — omitted where none is.

An item is omitted only where its line says; an omitted item is dropped, not narrated as absent.

Beyond the quoted questions, the delivered readout carries no internal id (merged-list, seat-finding or question); what other readers need from the ids goes in its **trace**, the record-only part after it (`round-record.md` § Round record format, field 8).

Readout coverage is yours: beyond the terminal pass's check of carried questions, nothing checks it after you. Before recording, check the readout against the merged list and `## Question dispositions`. Then record the readout and its trace in the round record's `## Round readout`, write `state: readout`, and deliver the recorded readout word for word, less its trace; delivery closes the round.

Write an operator ruling or record correction that arrives after a round closed, dated, into that round's `## Rulings and corrections`; a ruling also enters `brainstorm-decisions.md` (status: `crucible:brainstorming` § Workspace provisioning). In a spec campaign, a ruling's change rides the next numbered round's fix list to freeze. After the last numbered round's has frozen, once that round has closed and the terminal pass's wait has ended, the rulings in hand ride one more fix list of that round, its rulings list (`round-record.md`), applied and verified as that round's own fix wave; an ask it raises goes to the operator at once, a repair's holding no pass. Otherwise, a ruling arriving after that list froze or the pass's dispatch waits for the close, its entry saying so; before the handoff, make it as `flip-paths.md` has a change after the close where that applies, the ruling confirming a scoped amendment.
