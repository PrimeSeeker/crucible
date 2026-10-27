# Authoring crucible

Rules for writing crucible's own files: the skills, their references and
templates, the hooks and these docs. A controller or seat running a skill
never needs them.

## Anchor stability

These headings are cited by other skills and scripts as interfaces, so
renaming one is an interface change, not an edit:

- the `##` headings of `skills/redteaming/references/formats.md`;
- `Hook registration per runtime` in `hooks/README.md`;
- the `##` headings of this file, which `hooks/README.md` cites;
- one heading outside those files, `Operating stance — baseline error rate`
  in `skills/redteaming/SKILL.md`, cited cross-skill as
  `crucible:redteaming § Operating stance — baseline error rate`. That names
  one target; it does not freeze `###` headings generally.

## Reference convention

The positive format every crucible author follows. Its classes are what
crucible's reference scanner (`tests/test_references.py`) validates against,
in the skills, the hooks, the decision records (`docs/decisions/`) and the
upstream map (`docs/upstream.md`).

### 1. Skill invocations

Always namespaced: `crucible:<skill-name>`, where `<skill-name>` is one of
the shipped roster:

`using-crucible`, `brainstorming`, `writing-plans`,
`subagent-driven-development`, `redteaming`, `requesting-code-review`,
`receiving-review`, `dispatching-parallel-agents`, `systematic-debugging`,
`using-git-worktrees`,
`finishing-a-development-branch`, `writing-skills`.

Example: invoke `crucible:redteaming`. Negative space (scanner-enforced): no
invocation may use the retired upstream namespace (any namespace-qualified
form of the upstream plugin's name), and no invocation-shaped reference may
name a dropped skill (the names test-driven-development,
verification-before-completion, executing-plans, receiving-code-review and
using-superpowers no longer exist as skills — their content was folded or
dropped). Bare prose mentions of those names as *provenance* ("the folded
TDD content") are legitimate and never match the scanner's patterns; an
invocation-shaped or link-shaped use is dangling by definition.

### 2. Sibling-file and cross-skill file references

Plugin-root-anchored paths: the path starts at the plugin root with
`skills/`, `hooks/`, `tests/` or `docs/`, and must resolve to a file that
exists in the repo (the scanner's dangling-reference check). Examples:

- `skills/redteaming/references/formats.md`
- `skills/subagent-driven-development/writing-good-tests.md`
- `hooks/README.md`

Never dirname-relative hops (`../other-skill/…`) for cross-skill references;
within-skill sibling files may additionally be named bare (superpowers'
structural convention), but the plugin-root-anchored form is always valid and
is the citable one. A script invocation carries the script's
plugin-root-anchored path behind the `<plugin-root>` placeholder, never a
dirname-relative path:

```
python <plugin-root>/skills/redteaming/scripts/conserve.py <feature-slug> <phase> <round>
```

### 3. Anchor citations

Citations into `skills/redteaming/references/formats.md`, `hooks/README.md`
and this file use the exact `##` heading text (e.g.
"see `formats.md` § Feature folder"). These headings are
frozen interfaces (§ Anchor stability). Cross-skill anchor citations take
the form `crucible:<skill> § <exact full heading text>` and are sanctioned
for the headings named as frozen citation targets in § Anchor stability;
that naming is the scope — the form is not opened to `###` headings
generally.

### 4. Decision records and the upstream map

The records and the map follow classes 1–3, with these differences:

- They cite a skill heading as `crucible:<skill> § <exact heading text>`,
  any heading, frozen or not. The scanner checks every citation: it fails
  one whose text after `§` does not begin with a heading of the cited
  file. The form marks no end to the heading, so the check cannot catch
  words appended to a real heading. They cite each other as
  `docs/decisions/<slug>.md`.
- In them a bare `README.md § <heading>` cites the root `README.md`; in
  `skills/` and `hooks/` it cites `hooks/README.md`.
- An upstream path carries the prefix `superpowers/`, as
  `superpowers/skills/executing-plans/`. The scanner's dropped-skill and
  anchor checks skip a prefixed path, and its dropped-skill check skips
  URLs, so an upstream skill crucible dropped can be named where upstream
  has it. The upstream namespace form (the upstream name followed by a
  colon) is never written: the retired-namespace check fails it here too.
