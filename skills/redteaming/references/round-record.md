# Round record reference

Each round has a directory under the feature workspace's `campaigns/`. Field lists are binding unless their section says otherwise; file and directory names are fixed: consumers depend on them.

Per-round directory contents:

```
round-NN/ # NN zero-padded, sequential; round 0 is round-00
  record.md # the round record
  seat-<id>.md # one per seat report, raw, workspace-only
  verifier.md # the blind verifier's report
  terminal-pass.md # plan phase only
  second-read.md # plan phase, if one runs
terminal-pass/ # the spec campaign's terminal pass
  record.md
  pass.md # the pass's report
  second-read.md # if a second read runs
```

## Round record format

Stop-rule inputs, cap arithmetic, parked and deferred minors and quorum status are all computed from the round records. A record's field layout and section titles are guidance; the process rules its fields state bind. Fields 1–2 are the preamble, before the first `##` heading; each later field is a `##` section under its title. Any record may add `## Rulings and corrections`: dated operator rulings on its decision asks and corrections to the record, entered after the round closed.

Fields, in order:

**1. Header**: phase (`spec` | `plan`), round number, feature slug, date, and the artifact reviewed as `<path> @ <rev>` (`<rev>` a commit hash or stated revision marker; backticks optional on either part): the one revision every seat in the round reads.

**2. State line** (binding): the single line `state: <value>`, `<value>` exactly one token of:

`dispatched → returned → merged → fix-applied → verified → readout`

The plan record alone appends `confirmed`. States advance strictly in order, each written only after its phase's outputs are on disk. Numbered rounds (`round-01..NN`) skip none; a special record (below) skips the states of steps it does not run.
- `dispatched`: seats launched, roster recorded.
- `returned`: every dispatched seat's report on disk, or its loss recorded and resolved (field 3).
- `merged`: the merged finding list, with dispositions, written.
- `fix-applied`: the recorded fix list landed in the artifact.
- `verified`: the blind verifier's report on disk, each item or claim found failing repaired or put to the operator as a decision ask.
- `readout`: the round readout recorded; the round closes once it is delivered.
- `confirmed`: the terminal pass's report, and any second read, on disk, and the phase's final check done.

**3. `## Quorum block`**: seats dispatched, seats returned, and every lost or crashed seat by id, with what happened and its resolution: `topped-up` (re-dispatched, report present), `not replaced` (a seat on another host, `panels.md`) or the round marked degraded. Its one binding line, `degraded: yes | no`, feeds cap arithmetic: a round that lost any dispatched seat but a seat on another host and did not top it back up is `degraded: yes`.

**4. `## Panel roster`**: per seat, its id, model, assigned lens and `seat-<id>.md` file.

**5. `## Merged finding list`** (merge rules: `crucible:redteaming` § Merge and finding hygiene): entries only, one list item per finding opening `- <id> <SEVERITY>` (BLOCKER, MAJOR or MINOR, the only vocabulary), continuation lines indented. Each entry carries its originating seat(s), an `origins:` element, a one-line substance, the `UNVERIFIED` tag where staked without evidence with its verification outcome, one `disposition:` element (`applied` | `partly-applied` | `parked` | `rejected` | `deferred-to-implementation` | `deferred-minor`), and the ruling a partly-applied, parked or rejected entry owes. An entry merged from a premise finding carries `premise` after its severity: `- F4 MAJOR premise`. Elements may share the opening line, em-dash separated: `- F3 MAJOR (seat-s2, seat-s3) — origins: s2-4, s3-1 — … — disposition: applied`.

**Origins** (binding): `origins: <seat-id>-<n>, <seat-id>-<n>`, one id per raw seat finding the entry absorbs, merged into it or closed against it as a duplicate; the terminal pass finds seat findings through it. A seat finding's id is the one its report's finding header carries: `<seat-id>` is the seat's `seat-<id>.md` identity (`p0` for the plan phase's pre-pass), and `<n>` numbers its findings from 1.

**`## Question dispositions`**, after the merged list, part of field 5: every question a seat report raises, by its id `<seat-id>-q<n>`, is answered (with the answer), carried to readout (the question quoted verbatim in this round's readout), rejected (with a ruling) or adopted (an improvement riding this round's fix wave, with the fix item carrying it).

**6. `## Fix list`** (what it takes, the propagation sweep and the trace: `crucible:redteaming` § Fix application and blind verification): enumerated items, each naming the finding id(s) it resolves or the question id of the adopted improvement it carries. It is the blind verifier's sole mandate input: fix list + diff, never rationale. **Restating sites** (binding): each item also names every other artifact site its sweep and any trace find.

**7. `## Verifier block`**: a pointer to `verifier.md`; a landed/not-landed verdict per fix item; the nothing-outside-the-list-moved verdict; a verdict per delta claim, TRUE or FALSE with evidence, or not checked with the reason; for each claim not checked, your own check and its outcome; and each repair, with its re-check's verdict or the decision ask it became.

**8. `## Round readout`**: the readout as delivered to the operator, compact, with the items and form of `crucible:redteaming` § Round readout. After it, a line `Trace:` opens the trace, the bookkeeping other readers need, record-only and never delivered:
- in a numbered round record and the plan record, each decision ask's merged-list ids, the entries it turns on (the terminal pass reads them).

**Special records:**

- **Round 0** (`round-00/record.md`): fields 1, 2, 6 and 8 plus `## Claim table` (claim → TRUE/FALSE with evidence). Its fix list holds its findings and the fixes applied before round 1; each finding the list does not take is named after the items, with its disposition. It runs no blind verifier, and with no merge has no question dispositions: its agent's questions are answered in its readout.
- **Terminal pass** (`terminal-pass/record.md`): fields 1, 2, 6 and 8, a pointer to `pass.md` in its preamble, and `## Deferred minors`, the pass's `deferred-minor` findings (a second read's included), each with its disposition. Field 6 appears only when the pass's findings trigger the at-most-one further fix wave. Field 8, the close, is recorded before any second read and delivered after it, its corrections added. Here `verified` means `second-read.md` is on disk.
- **Plan phase** (`campaigns/plan/round-01/record.md`), the phase's only record: no `round-00`, no `terminal-pass/`; its terminal pass's reports go in `round-01/`, beside the pre-pass's `seat-p0.md`, a seat report for every purpose. Fields 1–8 plus `## Terminal pass`: the pass's `Record corrections: <N>` outcome, any repair of the pass's findings, the close delivered after the pass, any second read, the pass's `deferred-minor` findings and the final check before `confirmed`. The quorum block is kept for lost seats; no cap arithmetic applies. That repair re-advances the record through `fix-applied` → `verified`; `confirmed` is written last. A flagged correction is a decision ask to the operator.
