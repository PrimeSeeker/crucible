Lane: very-small (operator-confirmed 2026-11-03)

# writing-skills: reader cost

## Intent

writing-skills becomes the guidance for agent-read text that is reused: skills, instruction files, rules, prompts and dispatch templates, hook-injected text. It is organized around reader cost, tokens × reads for each reader. It carries what the prose-compaction effort (`docs/crucible/2026-11-03-prose-compaction/effort.md`) and this lane's micro-test learned about keeping that text small, and its own `SKILL.md` ends no larger in tokens than before.

## Change list

Advisory.

- `skills/writing-skills/SKILL.md`, re-derived from a rule inventory of the current file plus the rules below, by the lite procedure: inventory, one writer working from the inventory alone, blind check, repair, check after the last repair. The new content:
  - an opening that scopes the skill by reader and reuse, and a description that names those kinds of text rather than a catch-all;
  - a reader-cost section: measure per reader and per load; load each rule where its reader acts on it; a pointer pays only where the reader already loads its target; one file per set of readers; retire a rule whose reason has lapsed; a review of agent-read text counts excess as a finding; measure the written text, never estimate it;
  - the fix recipe, worded as tested: "A fix revises the sentence that owns the case; its added words are the rule's new condition or action, stated as the sentence states its others, while the finding's reasons, its failure scenario and what a pointer already defines stay out of the text.";
  - the current sections kept and regrouped: form versus failure, evaluation, the discipline toolkit, and the skill-specific parts (host tooling, descriptions and names, structure).
- A supporting file, read only when compacting: the lite procedure, the effort's cut patterns (`docs/crucible/2026-11-03-prose-compaction/style.md`) in general form, and the "stated elsewhere" ledger for passes over several files.
  - Deferred to implementation: the supporting file's name.
- Consumers: the router's Skill Index line, the implementer template's pointer to writing-skills (regenerated), `AGENTS.md` and `docs/decisions/authoring-crucible.md` where they cite the Size and placement bullet, `README.md`'s skill line, and any record that cites a moved section.
- `docs/decisions/authoring-crucible.md`: the writing-skills record takes the restructure and the micro-test's figures; the rejected entries "Removing writing-skills, or rewriting it whole" and "A total or reduction target" are amended, the cap scoped to this rewrite; Changes lines.
- The micro-test's scripts and outputs go in this folder, the repository path a parameter.
- `docs/backlog/prose-creep-containment.md` drops its writing-skills part and records the operator's objection that token costs are underestimated before implementation, which weighs against a design-time allowance.

## Acceptance

1. `python -m pytest tests/` passes.
2. `skills/writing-skills/SKILL.md` counts at most 3,366 tokens by Anthropic's token-counting endpoint, as the file counted on 2026-11-03.
3. The micro-test's umbrella case, run five times with the new `SKILL.md` as the guidance: median growth at most 22 words, and no run restates the definition behind the `umbrellas.md` § Review pointer (read by hand). The pre-change skill gave a median of 33, two of five runs restating it.
4. The blind check accounts for every item of the pre-change `SKILL.md`'s rule inventory: kept, moved to a named file, or retired by a ruling the record lists.
5. Every citation of a writing-skills section (on 2026-11-03: the Size and placement bullet in `AGENTS.md` and `docs/decisions/authoring-crucible.md`, and § Descriptions and names in the latter) names a section or bullet the new `SKILL.md` has.

## Out of scope

The crucible-side containment (a measured trigger, a design-time allowance, a review-terms line on excess, recasting the prose budget), which stays in `docs/backlog/prose-creep-containment.md`. Renaming the skill. Any other skill's text beyond the consumers above.
