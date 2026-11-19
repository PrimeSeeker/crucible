# Process gaps a folded-lane run showed: rulings between round close and campaign close, the record of an ask, a status-only question

## Observation

One feature on another project (Python, a Claude-family controller on 0.33.1,
folded lane: round 0, a four-seat round 1 with one seat on another host, a
terminal pass and a second read, then three tasks) showed these. Counts are
from that one run.

- **An operator ruling that lands after a round closes and before the
  terminal pass has no defined vehicle.** Round 1's readout carried two
  decision asks. The answers changed the artifact (a decision replaced, a
  failure path added). `round-readout.md` sends such a ruling to the round's
  `## Rulings and corrections`; `flip-paths.md` governs only from the
  campaign's close on; `fix-application.md` says rulings "ride" a fix list,
  but the round's list was applied and verified already. The controller
  improvised a second wave inside the closed round, with its own fix list, a
  verifier report under a file name `round-record.md` does not list, and its
  own judgment that the wave did not re-shape a major mechanism. The
  terminal pass accepted that; nothing told the controller to do it.
- **The recorded readout is not the delivered readout.** The controller
  wrote a compact readout into the record and sent the operator a fuller
  message. The terminal pass audits the record, so it reported omissions the
  delivered asks did not have, and the second read noted it could not check
  the delivered text. `round-readout.md` says "deliver the readout to the
  operator as recorded"; the controller did not, and no step makes the
  delivered text the record.
- **Asks may go out before the round's verifier returns.** The controller
  delivered the round's decision asks while the blind verifier ran, to save
  the operator's waiting time, then recorded the readout afterwards. The
  state line has no place for it.
- **A carried question whose only effect was a status label.** Round 0's
  agent asked whether a decision the spec recorded as the operator's firm
  preference was firm for this feature too. The design kept the rule either
  way. `merge-and-finding-hygiene.md` requires carrying a question that
  doubts a firm decision, quoted verbatim with its ids, so the operator was
  asked a question that changed nothing built, in words that needed
  translating.
- **Record corrections dominated the close.** The terminal pass found
  nothing in the artifact and three record corrections; the second read
  found four more, all in the close readout the controller had just
  written, one of them a bias line stated backwards. Two default-role runs
  went on the controller's prose for a filter of about a hundred lines. The
  corrections were real; the cost sits oddly against the artifact's size.
- **Baseline in a fresh worktree.** `setup.md` wants the project's suite run
  in the worktree before any task. The controller reused a full green run
  from the same commit in another checkout, made hours earlier, and recorded
  that in the ledger. The rule has no words for a baseline already shown on
  the same commit.
- **Host, not crucible:** a dispatch sent in the same response as another
  tool call was several times refused by the host's permission checker and
  had to be sent again alone.

## Follow-up

- Say where a ruling on a round's ask is applied when it arrives before the
  terminal pass: its fix list, its verification, and who judges whether it
  re-opens the stop rule.
- Make the delivered readout and asks the record, verbatim, or have the
  terminal pass read the delivered text.
- Decide whether asks may be delivered before the verifier returns, and give
  the state line a way to show it.
- Let the controller answer a question that changes only a status label,
  recording the answer as its own, or batch it into the close.
- Consider a lighter record check for a small artifact: one pass, or the
  second read only where a correction is flagged.
- State whether a baseline shown on the same commit elsewhere counts.
