# Publication

## Decision

**What the README claims.** It presents crucible as one person's
workflow, shared because frameworks for individual-scale autonomous
agentic development are scarce: not a product, with no support promise.
It states no effect of crucible as measured unless it was. Its three
comparisons, against the host with no process plugin, against
superpowers, and against superpowers with a generic iterative redteaming
skill, are labelled the maintainer's impressions, their token figures
(about 5–10× a plain session, 1.5–2× superpowers) guesses; the third
stands beside the outcome review's finding of no detectable difference.
Subscription advice is labelled the maintainer's experience. It claims
no measurement of skill triggering (`docs/decisions/crucible-suite.md`).
Its platforms name what was measured: the hook on Windows and Linux, not
on macOS (`docs/decisions/session-start-hook.md`), and Codex as
experimental, with the checks it failed
(`docs/decisions/runtime-adapters.md`). It states where crucible's
calibration comes from in aggregate figures (`README.md` § How it
compares).

**What may be published about another project.** Committed text carries
no local context, with one exception: about a project, aggregate figures
(its language, model family, sizes and duration, and measurements of
crucible's own runs on it, such as token costs, rates, ratios and counts)
and a description of what crucible itself did in a run on it may be
published, never the project's name, domain, content or implementation
details. The branch reviewer checks it (`AGENTS.md`, No local context in
committed text).

**The outcome review.** Evidence for the README's claims comes from a
retrospective outcome review whose method was fixed before its data was
read. How and when crucible's calibrations are re-derived is open in
`docs/backlog/outcome-evidence.md`.

**Contributions: issues only, for now.** Reports and suggestions go to
GitHub issues, and pull requests are not accepted yet. An accepted report
becomes a backlog item linking its issue. There is no code of conduct,
CONTRIBUTING file or `.github/` template; `AGENTS.md` holds the rules for
changing crucible (`README.md` § Contributing).

**The backlog's shape.** One file per item in `docs/backlog/`: a title,
the observation, the follow-up, and a link to its GitHub issue where one
exists. An item states the current state, with no progress log; a
resolved item is deleted, and a partly resolved one keeps only what
remains open (`AGENTS.md`, Where things are).

## Why

### The README's claims

From 2026-10-07 the README was to describe cost qualitatively, with no
token figure: the only cost data was one maintainer's work on one
project, so a range would have been false precision. On 2026-10-19 the
maintainer supplied figures for the README's comparisons, "comparisons
on vibes" in the maintainer's words, and they stand as labelled guesses;
the design digest still shows none
(`docs/decisions/operator-steering.md`). That no effect is stated as
measured unless it was is a rule of the same design. (Basis: the
maintainer's preference, for the figures; judgment, accepted by the
maintainer, for the rule.)

### Another project's figures

Crucible's numbers, how many seats a round has, how many rounds a review
may take, how large a plan gets, come from one project, and a reader
needs to know how far that project is from theirs. The maintainer ruled
on 2026-10-19 that its aggregate figures may be published, never its
name, domain or content; on 2026-10-20 the exception took in measurements
of crucible's own runs on it, which the backlog already published. On the
same day, for these decision records, an agent proposed that it also
take in a description of what crucible itself did in a run there, so
that a record can restate the runs its evidence comes from, and the
maintainer agreed: "OK, agree". (Basis: judgment, accepted by the maintainer.)

### The outcome review

The first design (2026-08-07) set an outcome review after crucible's
first cutover, three features or a month in, as the trigger to roll back
on a quality regression: every earlier acceptance criterion checked that
the process ran, none that it worked. It never ran. On 2026-10-17 the
maintainer wanted it anyway: "Seems like we need that outcome review,
then". Its rollback purpose gone, it became evidence for the README's
claims. (Basis: the maintainer's preference.)

It ran on 2026-10-17 over one project's history, comparing escaped
defects (later fixes and reverts touching a feature's files) in code
written with crucible and before it: no detectable difference. Per added
line the ratio favoured crucible when a repair had to come at least
three days after the code, and was unstable at seven; per commit, with uncertain items counted
against crucible, it reversed; classifiers called about the same share
of later edits repairs in both periods. Hence the third comparison's
caveat. (Basis: measured.)

### Issues only

The maintainer's choice, on 2026-10-19: nothing to maintain, and easy to
open later. It also disposes of upstream's contributor guidelines, code
of conduct and `.github/` (`docs/upstream.md`). (Basis: the maintainer's
preference.)

### The backlog's shape

An item is read by someone with none of the repository's history, so it
says where things stand now; the filed date, the source and the progress
log went on 2026-10-19, and git history keeps them. (Basis: judgment,
accepted by the maintainer.)

## Rejected

- **Measured-sounding claims without a measurement**: every comparison
  and cost figure carries its label (§ Why).
- **Naming another project**, or its domain, content or implementation
  details, in committed text (§ Why).
- **Pull requests, a code of conduct, a CONTRIBUTING file or issue
  templates**, for now (§ Why).
- **A progress log in a backlog item** (§ Why).

## Changes

- 2026-10-20: the exception also admits a description of what crucible
  itself did in a run on another project.
- 2026-10-20: aggregate figures about another project may be published,
  measurements of crucible's runs on it included; never its name,
  domain, content or implementation details.
- 2026-10-19: the README presents a personal workflow with no support
  promise, states nothing as measured that was not, and names the
  measured platforms.
- 2026-10-19: the README's comparisons are the maintainer's labelled
  impressions, with token figures as guesses.
- 2026-10-19: contributions as GitHub issues only, for now.
- 2026-10-19: backlog items state the current state: title, observation,
  follow-up, issue link; no progress log.
- 2026-10-17: a retrospective outcome review, its method fixed first, as
  evidence for the README's claims; it found no detectable difference.
