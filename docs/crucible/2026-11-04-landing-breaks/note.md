# Landing breaks: a landing that breaks the base says so first

Lane: very-small (operator-confirmed 2026-11-04)

## Intent

A landing, under an umbrella or not, can break the base until later work lands, and nothing surfaces that, so the operator can only plan around it if already aware. A break is a landing leaving the base unable to do something it did before, or leaving a path someone can reach that fails; unfinished work nobody can reach is not one. A break must be stated up front, accepted by the operator, checked by an independent reviewer and repeated before landing. Landing on the base stays the default.

## Change list

1. Spec contract and lane note: where a landing would break something, the Intent says what and until when.
2. Branch reviewer: a break the spec or note doesn't state is a finding.
3. Close readout: list any stated break before the landing ask, so runs and releases can be timed around it.
4. `skills/brainstorming/references/umbrellas.md`: an umbrella's proposal says whether its children can land without a break; what one leaves unfinished goes in the entry of the child that owes it.
5. Decision records: record the rule and why, and record a changed landing default and a dedicated effort-branch path as rejected.
6. `docs/backlog/umbrella-followups.md`: remove the question this settles.

## Acceptance

1. `python -m pytest tests/` passes, including the generated-template and word-budget checks.
2. The rule's wording appears at the sites in items 1 to 4; a search for similar wording finds none on the pre-change tree.
3. The backlog question is gone.

## Out of scope

- The other items in `docs/backlog/umbrella-followups.md`.
- Any run or check of the product itself.
- Existing features.
