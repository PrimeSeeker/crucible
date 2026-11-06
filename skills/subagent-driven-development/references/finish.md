## Finish

1. Record checks: inspect the feature workspace against the ledger and list every gap. Expect:
   - the campaign records where their phases ran (round records, readouts, fix lists), and the ledger's sections
   - in `sdd/reports/`: per task, `task-<N>-<kind>.md`, `<kind>` being `report`, `review` (none where the latest run completed branch review only), `re-review-w<W>` per wave, `adjudication-<b>` per dispute batch and `snapshot-<k>` per snapshot blessing; for a task run again, only its latest run's, in `-x<X>` form; `-r<R>` forms included; and `lane-report.md` where the lane dispatched an implementer
   - in `sdd/branch-review/`: each `pass-<k>.md`, `wave-<n>-fix.md`, `wave-<n>-re-review.md` and `adjudication-<b>.md`
2. Close readout to the operator: a message, not a file, its decision asks in a final block. Assemble it from the ledger's `## Adjudication rulings`, `## Deferred minors`, `## Questions`, `Task <N>: parked` lines and lane section, following its predecessor link where one exists. It lists:
   - dismissed BLOCKER/MAJOR findings and ruled premise findings, with their rulings
   - every ruling you made yourself, with its reason: disputes and plan conflicts, the plan patches they led to, contained amendments, the plan phase's included
   - every improvement you adopted, named as a lightly held change
   - each fresh look (`<workspace>/fresh-look-<k>.md`), with what you did with it
   - each ruling or requested change a fixer declined, as an ask
   - the lane's departures and the record-check gaps
   - after loop activity that followed an earlier answer, what changed since
   - then the work left open, each item with its source and your proposal to keep or drop it, and why: parked BLOCKER/MAJOR findings with their rulings, premise asks still unruled, `unstated break` asks still open, deferred minors and leads (a RECOMMENDED lead you did not adopt, with its verdict; where a cleanup wave ran, why it left each one), and, with your disposition, the `## Questions` items not listed above (declined improvements and what earlier phases carried among them)
   - where the project's instructions name no home for open items and something is left open, an ask where it goes or whether to drop it, offering to record the answer (`skills/redteaming/references/formats.md` § Open items)
   - where this feature's landing could complete its umbrella, what `skills/brainstorming/references/umbrellas.md` § Closing review has the readout say
   - each break the spec, folded document or lane note states (`crucible:brainstorming` § Spec contract) or an operator's ruling accepted, and until when, or an `unstated break` still open, so the operator can time runs and releases around it
   - your recommendation and why, the final block's last item: one of the options `crucible:finishing-a-development-branch` § Step 4: Present Options offers on this branch, or more work; recommending a pull request, also ask that skill's question whether the feature folder's files go into it
3. Wait for the answer; integration stays the operator's decision.
   - More work asked for, or a ruling that opens a wave: reopen the branch-review loop before any later step; Finish then restarts at step 1.
   - Loop activity after an answer, a red suite's included: Finish restarts at step 1; the earlier answer stands only where nothing new was left open; otherwise ask again.
   - An integration option: run steps 4–7 in order.
   - Where step 2 asked where open items go: steps 4–7 wait until the answer names a home or drops them; until then, ask again and leave the workspace in place.
   - Discard: skip steps 4 and 5, and take finishing's typed `discard` confirmation before step 6 deletes the feature workspace; unconfirmed, it counts as no option chosen.
   - No option chosen (the work left in place): run steps 4–7; at step 7 finishing presents its options with your recommendation.
4. Send the work left open, as the answer left it, where `formats.md` § Open items sends it, writing on this branch an in-repository home's items and any instruction-file line recording the answer, where that file is committed; dropped items go nowhere. No item takes a ruling of its own. With an `Umbrella:` line in the spec, folded document or lane note, mark this feature's entry in that umbrella `landed`; with none, an unmarked entry opening with the slug that `git grep -n "<feature-slug>" <base-branch> -- "*/umbrella.md"` finds may be this feature's. Both cases follow `skills/brainstorming/references/umbrella-children.md` § Marks. Commit what this step wrote, so the suite runs on the tree that lands; if the loop reopens, the next answer rewrites these items.
5. The suite: run the full suite, or the project's declared merge gate, on HEAD, and show the operator a green run's summary line. Do not classify a red run: it is a BLOCKER finding against the branch, handed to `crucible:requesting-code-review`'s loop and counted against its cap. That a failure is not the branch's (it fails on the merge base too, or is environmental) is an ordinary dispute, which you may raise before the wave opens. A failure ruled not the branch's, whoever ruled, is recorded with its ruling and not raised again while it fails the same way; show the operator the red run with that ruling: only an answer accepting it lets finishing pass its Step 1.
6. Delete `.crucible/<feature-slug>/` and nothing else; report to the operator anything you could not delete.
7. Use `crucible:finishing-a-development-branch`: it carries out the answer without presenting its menu again and asks only what the answer left open.
