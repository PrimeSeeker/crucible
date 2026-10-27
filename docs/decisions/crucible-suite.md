# Crucible's test suite

## Decision

**The suite.** `python -m pytest tests/` from the repository root, on
Python 3.10 or newer with pytest and the standard library. The hook
tests need bash; without it they skip and print why, and a skip is not a
pass. The suite launches no model (`AGENTS.md`, Tests).

**Tests assert text only where code or the host reads it,** and name
that reader in a comment beside the assertion. Everything else is a
structural check (a file, heading or anchor exists, references resolve,
generated files match their source, slot cards, the generator and the
generated agents agree) or no test at all. There is no protected list of
safety sentences, no test pins a skill's description wording, and no test
pins the shape of a finished build.

**The claude-ism scanner.** `tests/claudeism_scanner.py` checks shipped
text for host-specific terms: every `.md` file under `skills/` and
`hooks/`, the root `README.md`, and `hooks/session-start` read as a
source, without running bash. Its terms are written in code, each with a
corpus case: one host's tool, mode and dispatch spellings, its home
paths and instruction file, and the Claude and Codex model names,
including any `gpt-` slug. Its allowlist, `tests/claudeism-allowlist.txt`,
admits a term at one named location, never a whole file, for the adapter
references, writing-skills' routing to each host's tooling, and the
README, `hooks/README.md` and the hook; it holds no verbatim witness
snippets and no rows for deleted files. A test checks that writing-skills
pairs its Claude Code home path with Codex's `$HOME/.agents/skills`,
never with Codex's built-in `.system/` directory.
`tests/test_acceptance_gate.py` runs the scanner over the live tree. The
rule it enforces is `docs/decisions/runtime-adapters.md`'s.

**No model-launching tests.** No eval harness, no triggering probe set or
runner, no model-running tests and no pressure fixtures. Whether skills
trigger is unmeasured, and so are the router's rewrite, the trigger-only
descriptions and the trivial-edit waiver's offer; use is their evidence.
The README claims no measurement of triggering. Before it claims one, a
one-off check runs on a newcomer's setup: no personal instruction files,
the default and bounded roles, about ten prompts, the results recorded
beside the claim, and no committed runner.

## Why

### Text only where code reads it

On 2026-10-06 about 75 tests asserted sentences no code read. Every
rewording became a test edit, and changes drifted toward appending text
rather than rewriting it. On 2026-10-06 the maintainer ruled the strict
rule, with no protected list: the passages such a list would guard are
rewritten on purpose, and those rewrites' reviews are the safeguard. What
was given up knowingly: no test guards the blind verifier's narrow
inputs, the read-scoping fences or the dispatch composition's wording.
(Basis: measured, for the count; judgment, accepted by the maintainer.)

On 2026-10-11 the tests written as the first build's acceptance gate
went: they pinned a finished build's shape, and the two worktree-adapter
files' 949 lines mostly exercised git's own behaviour and the shape of
the worktree skills' prose. (Basis: judgment, accepted by the
maintainer.)

### The scanner

Shared skills name no host's mechanics. A rule like that, stated only in
prose, kept being broken, so the vocabulary lives in code, with a corpus
of the cases that broke it (since 2026-08-16). The allowlist is per term
per location because the first positives sat in files that also carried
allowlisted model-policy text, which a whole-file entry would have
silenced. The scanner reads the hook script as a source because the
envelope's lead line lives only there, and reading it needs no bash
(2026-10-11). Codex model lines and slugs joined the terms when model
names moved into the host maps (2026-10-13;
`docs/decisions/model-roles-and-effort.md`). Codex reads a user's skills
from `$HOME/.agents/skills` ("Build skills", Codex's documentation, read
2026-10-20); `.system/` holds its built-in skills, so pairing with it
would be no Codex sibling at all (2026-10-14). (Basis: judgment, accepted
by the maintainer; external, for Codex's path.)

### No model-launching tests

The first design shipped no eval harness, the maintainer's ruling: "By
the nature of the exercise there are no good eval examples"
(2026-08-06). Triggering goes unmeasured because, as the maintainer
asked on 2026-10-14, "Practically speaking, skill triggering don't seem
to be a problem? Why a reusable probe?", and because automated live
tests are a maintenance burden and resource-heavy, with audits the
cheaper route to evidence (the maintainer's reason, 2026-10-12). (Basis:
the maintainer's preference.)

On 2026-10-14 an agent restated the first design's reason, which the
maintainer accepted: it holds for whether review finds what matters, not
for triggering, where cheap examples exist; and on Claude Code no missed
trigger was on record in crucible's repository between the router
rewrite (2026-10-07) and that day. (Basis: judgment, accepted by the
maintainer.)

That use is one environment, the maintainer's own: the default role and
the maintainer's instruction files. A newcomer's sessions may trigger
differently, hence the check before any README claim. An agent proposed
its shape, which the maintainer accepted. (Basis: judgment, accepted by
the maintainer.) Upstream's pressure fixtures invent stakes for the
tested agent, which crucible's evaluation rule forbids
(`docs/decisions/authoring-crucible.md`).

## Rejected

- **An eval harness, or a reusable triggering probe set** (§ Why).
- **Model-launching tests**, upstream's included: a maintenance burden
  and resource-heavy (§ Why).
- **Prose pins**, a protected list of safety sentences, or a test pinning
  description wording: they freeze wording, not behaviour.
- **Tests pinning a finished build's shape** (§ Why).
- **A whole-file allowlist entry** (§ Why).

## Changes

- 2026-10-14: no eval harness, probe set, model-launching tests or
  pressure fixtures; triggering unmeasured, with a newcomer check before
  any README claim of it.
- 2026-10-14: the claude-ism scanner over the skills, hooks, README and
  hook script, Claude and Codex model names included, allowlisted per
  term per location, Codex's home path paired.
- 2026-10-11: tests assert text only where code or the host reads it,
  naming the reader; structural checks otherwise; the first build's
  acceptance tests retired.
