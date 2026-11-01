> The brief the umbrella's audit (2026-11-01) gave its transcript readers, kept as the re-audit's method (`umbrella.md` D9). Local paths and project names removed.

# Evidence brief: what crucible's mechanisms caught

Shared brief for the evidence readers of a mechanism audit. Your dispatch names your slice and your report path; everything else is here.

## Purpose

Crucible is a process plugin: skill text that makes agents brainstorm, write specs, run review campaigns, plan, implement through dispatched seats and review branches. Its skill text has grown to about 66,000 words, and a rewrite is coming. The rewrite's main lever is retiring mechanisms that do not pay for themselves. The operator will rule on each retirement, and your report is part of the evidence they rule on. A mechanism inventory lists 147 mechanisms with stable IDs:

`inventory.md` (beside this brief)

Read its Method and per-skill tables first. Column "Observable signature" says what each mechanism leaves in a transcript. The per-mechanism sections below the tables give stated purpose and consumers; read those for the mechanisms your slice exercises.

## Your job

Read your slice of session transcripts and record, per mechanism ID, **what happened when it ran**. You record outcomes; you do not recommend keep or retire. Give "fired and changed nothing" the same care as "fired and caught something": both are evidence, and the report is worthless if it leans either way.

For each mechanism your slice exercises:

1. **Fires**: how many times it ran (count, or an estimate marked `~` with how you estimated).
2. **Catches**: fires that changed something real: the artifact, the code, a decision, or what the operator was told. For each catch, give a pointer (session id, subagent file or record path, and a quote of at most two lines), its severity as the record staked it, and **whether a later stage would plausibly have caught the same thing**: the per-task review, the branch review (which reads the whole diff on every route), the implementer's own tests, or the operator. Give the reason in one line. Where you cannot tell, say so.
3. **Null fires**: fires that changed nothing, or whose findings were all rejected, reverted or dropped.
4. **Cost signals**: churn the mechanism caused (fix waves that were later reverted, findings rejected, extra rounds, operator questions it generated), and anything that suggests its cost in time or tokens. Rough is fine.
5. **Misses**: cases where a mechanism should have fired by its own text and did not, or fired and let through something a later stage or the operator then caught.

Also record, outside the per-mechanism table:

- **Operator interventions**: places where the operator corrected the process, overrode a mechanism or complained about it. Quote briefly.
- **Behaviour not in the inventory**: something the agents did repeatedly that no listed mechanism asked for, or a mechanism you could not map to an ID.

## Version caveat

These runs used earlier crucible versions. A session whose transcript loads skills from a path outside the plugin cache ran a pre-2026-10-27 local install; a path under `plugins\cache\crucible\crucible\<version>` names the version. Mechanisms were renamed and added over time. Map an older name to the inventory ID it became where the match is clear, flag where it is not, and note which inventory mechanisms did not exist yet in your slice, so the merge doesn't read their absence as zero catches.

## How to read the transcripts

- Claude Code transcripts are JSONL, one event per line: `~/.claude/projects/<project-dir>/<session-id>.jsonl` for the controller, and `<session-id>/subagents/agent-*.jsonl` (with `.meta.json` beside each) for every dispatched agent.
- Files are very large (up to hundreds of MB). Never read one whole. Use Grep for signatures, and write small stdlib Python scripts into your scratch folder to extract what you need: for example, every `Write` or `Edit` tool call whose `file_path` contains `round-`, `verifier`, `pass.md`, `ledger`, `readout` or `record.md`; the final assistant message of each subagent transcript, which is its report; the controller's assistant text around readouts and asks; the `.meta.json` descriptions, which name each dispatch. Workspace records were deleted at each finish, but their content survives in these Write and Edit calls.
- Sample where you must, and say what you sampled and what you did not read.

## Hard constraints

- Read-only everywhere except your scratch folder the audit folder (the folder holding this brief). Edit nothing in the crucible checkout, the audited project's checkout or the host's configuration directory. Run no git command that changes state.
- Dispatch no agents. Publish nothing through any Artifact or claude-artifacts tool.
- The transcripts hold a private project's content. Your report stays private, but quote only what a pointer needs (at most two lines per quote), and describe project content generically ("a parser module", "the export feature").
- **Write your report early and keep it updated**: first a skeleton with the table, then fill in as you go, so a run cut short still leaves evidence. Use the Write tool, at the path your dispatch names.

## Report shape

1. **Preamble**: your slice, the versions it ran, what you read, sampled and skipped.
2. **Per-mechanism table**: ID | fires | catches (count) | null fires | later stage would have caught (yes / no / unclear, counts) | cost signals | confidence. Only mechanisms your slice exercised; list the rest in one line as "not exercised" or "did not exist yet".
3. **Catches**: one entry per catch, with its pointer, severity and later-stage line.
4. **Misses**, **Operator interventions**, **Behaviour not in the inventory**.
5. **What you could not determine**.

## Reply

When done, reply in under 250 words: the report path, the mechanisms with the most catches, those that fired most with no catch, and anything that surprised you. The file holds the detail.
