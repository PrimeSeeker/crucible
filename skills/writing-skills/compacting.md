# Compacting agent-read text

## Procedure

1. Inventory: list the file's rules as atomic items, every obligation, condition, format, ordering, pointer, rationale and example, each rated core, edge or support. For a file over a few hundred words, a completeness critic reads the file against the inventory and adds what it missed. Before any writing, the text's owner rules which items retire, and the inventory marks them.
2. One writer: for accreted text (tutorial passages, anecdotes, layered patches), it re-derives the file from the inventory without reading the original; for dense rule text, it line-edits.
3. Blind check: a checker who does not open the original reads the rewrite against the inventory, marks each item present, weakened, missing or dropped, and lists what the rewrite adds. Dropped covers an item the inventory marks retired, a support item the rewrite does without, listed for the owner, and a rule the ledger below records as stated elsewhere; any other absence is missing.
4. Repair and check again until no core or edge item is missing or weakened; the check after the last repair is the one that counts, and its "added" list, never empty, never ends the loop.
5. Run the project's own checks after every write.
6. Optionally, scenario questions drawn from the original, answered under the rewrite and graded only on core and edge items; read the partial grades by hand.

For several files in one pass, keep a ledger of the rules each unit drops as "stated elsewhere", check it at integration, and read the whole set together at the end: two files can each drop a rule on the strength of the other.

## Cut patterns

Each tightens wording; none retires a rule.

- Three or more cases stacked in one sentence become a list or a table of condition and action.
- Cite in the shortest form that resolves.
- Point or state, never both.
- Never restate a section beside the line that includes it.
- No argument against a misreading no record shows.
- A dispatcher's own text never restates the template it sends.
- One definition per term; every other site names it.
- A rationalization row stays only where it adds to the body.
- State a rule over its whole class, naming only the exceptions.
- Bold only a defined term or a read trigger; no alignment padding; one paragraph or list item per line.
- One procedure, one example; no anecdotes.
- A passage that says one thing several ways keeps one.
- Text about the text (where a rule lives, why a file omits something) goes to the project's docs.
- State a rare-path variant once, where its rare event is handled; other sites name only the common path.
- A shared section holds only what every taker follows; one taker's variant goes in its own text.

## What not to cut

- Anything code or tests read: frontmatter, cited headings, read triggers, generated-include markers.
- Rules with recorded evidence, and rules the owner recorded as a preference.
- A reason the rule needs to be read right, in one clause.
- The spine of a `SKILL.md` that a host re-attaches after compaction: step triggers, resume rules, loop bounds, gates and rules binding beyond one step.
