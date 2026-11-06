# Wording test

The test behind `docs/decisions/fix-verification-and-merge.md` § Repeat hits. One
fresh agent per sample on the default role, each reading one prompt file and
writing one fix-list item. The rule tested is the wording in `prompts/p2.md`,
`p3.md` and `p6.md`; what shipped differs, as the record states.

| Prompt | Passage | Reference |
|---|---|---|
| `p1` | The open-items rule, from one campaign's spec at its round 1 | Today's |
| `p2` | The same | With the rule |
| `p4` | The finding rule, from another campaign's spec at its terminal pass | Today's |
| `p3` | The same | With the rule |
| `p6` | A search in an acceptance item, a small correction | With the rule; no control was run |

Each finding was reconstructed from what the next revision changed; `p6`'s is
invented. `samples.md` holds every reply, unedited.

## How each reply was read

By eye, by one reader; `samples.md` lets another check it.

| Prompt | Samples 1 to 5 |
|---|---|
| `p1` | Hold on integration, hold, hold, new fallback in the pull request description, hold; all keep the cases apart |
| `p2` | Always commit on the branch, close to the maintainer's ruling; then hold, hold, hold, hold, each rewritten from its purpose |
| `p4` | One general rule, one, one, added exceptions, split kept with a pointer to the general rule |
| `p3` | One general rule in all five |
| `p6` | A wider search: phrases folded and hyphens matched, kept phrases and hyphens matched, then folded, folded, folded |

## Length

Words in the returned passage, its acceptance text aside.

| Passage | Before | Today's reference, median | With the rule, median |
|---|---|---|---|
| Open-items rule | 235 | 259 (251 to 275) | 291 (285 to 311) |
| Finding rule | 152 | 146 (143 to 170) | 158 (152 to 163) |
| Small correction | 62 | not run | 68 (64 to 77) |
