# Resident tokens per route

Counted on 2026-11-03 at three revisions: `a3db87f`, before the skill text
rewrite; `d78398c`, before the compaction fit; `4026f6b`, the compaction
fit's head with its skill changes in place.

- **What is counted.** For each route, `resident-tokens.json` lists every
  file a Claude Code controller loads, by phase, each once, under the phase
  that first loads it; its `about` list states the conventions (load forms,
  renamed files, what is left out). Compaction and re-reads are not
  modelled. The manifests are Claude Code's and say nothing about Codex,
  whose host files and tokenizer differ.
- **How.** `resident_tokens.py` sends each file's text, as the controller
  loads it, alone to Anthropic's token-counting endpoint (model
  `claude-opus-5-5`) and subtracts a one-word message's count. The run:
  `python resident_tokens.py a3db87f d78398c 4026f6b --out <file>`, 69
  counting calls, one-word base 9 tokens.
- **Reading the tables.** Each cell is the every-run total; the figure in
  brackets adds the files loaded only when their condition arises (a
  dispute, drift found after the fact, inline work, a flip path or premise
  ask, a child of an umbrella). A file marked absent did not exist at that
  revision: before `4026f6b` the step bodies now in references were part of
  their `SKILL.md`, and are counted there.

## Totals by route and phase

### standard

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 22,147 (+4,522) | 22,205 (+4,606) | 22,228 (+4,606) |
| spec campaign | 17,827 (+3,786) | 15,983 (+3,605) | 16,212 (+3,605) |
| plan | 6,578 | 5,933 | 5,933 |
| execution | 18,734 | 15,743 | 12,163 (+2,186) |
| branch review and finish | 11,401 | 9,802 | 11,719 |
| **total** | **79,145** (+8,308) | **72,172** (+8,211) | **70,761** (+10,397) |

### folded

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 26,907 (+4,522) | 25,928 (+4,606) | 25,951 (+4,606) |
| spec campaign | 21,579 (+3,786) | 19,563 (+3,605) | 19,792 (+3,605) |
| execution | 18,734 | 15,743 | 12,163 (+2,186) |
| branch review and finish | 11,401 | 9,802 | 11,719 |
| **total** | **81,079** (+8,308) | **73,542** (+8,211) | **72,131** (+10,397) |

### very-small

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 22,803 (+4,522) | 22,813 (+4,606) | 22,836 (+4,606) |
| execution | 21,222 (+4,946) | 18,486 (+4,672) | 12,133 (+6,507) |
| branch review and finish | 12,560 | 10,903 | 12,820 |
| **total** | **59,043** (+9,468) | **54,708** (+9,278) | **50,295** (+11,113) |

### umbrella campaign

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 26,669 | 26,811 | 26,834 |
| spec campaign | 17,827 (+3,786) | 15,983 (+3,605) | 16,212 (+3,605) |
| landing | 6,471 | 6,616 | 6,616 |
| **total** | **53,425** (+3,786) | **51,916** (+3,605) | **52,168** (+3,605) |

## Per file

| File | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| `hooks/session-start` | 2,458 | 2,506 | 2,506 |
| `skills/brainstorming/SKILL.md` | 7,776 | 6,913 | 5,612 |
| `skills/brainstorming/references/proposing-the-arrangement.md` | absent | absent | 1,324 |
| `skills/subagent-driven-development/references/seat-rules.md` (`skills/subagent-driven-development/references/premise-and-questions.md` at `a3db87f`) | 1,938 | 4,716 | 4,716 |
| `skills/redteaming/references/formats.md` | 8,762 | 7,675 | 7,675 |
| `skills/using-git-worktrees/SKILL.md` | 3,671 | 2,901 | 2,901 |
| `skills/brainstorming/references/umbrellas.md` | 4,522 | 4,606 | 4,606 |
| `skills/redteaming/SKILL.md` | 13,162 | 10,971 | 5,507 |
| `skills/subagent-driven-development/references/dispatch-composition.md` | 1,707 | 2,287 | 2,287 |
| `skills/using-crucible/references/claude-code-dispatch.md` | 618 | 607 | 607 |
| `skills/redteaming/references/panels.md` | absent | absent | 1,500 |
| `skills/redteaming/references/merge-and-finding-hygiene.md` | absent | absent | 1,786 |
| `skills/redteaming/references/fix-application.md` | absent | absent | 1,485 |
| `skills/redteaming/references/round-readout.md` | absent | absent | 922 |
| `skills/redteaming/seat-prompt.slots.md` | 1,041 | 882 | 882 |
| `skills/redteaming/verifier-prompt.slots.md` | 475 | 439 | 439 |
| `skills/redteaming/terminal-pass-prompt.slots.md` | 824 | 797 | 797 |
| `skills/redteaming/references/flip-paths.md` | 3,786 | 3,605 | 3,605 |
| `skills/writing-plans/SKILL.md` | 4,098 | 3,220 | 3,220 |
| `skills/redteaming/references/plan-phase.md` | 2,480 | 2,713 | 2,713 |
| `skills/subagent-driven-development/SKILL.md` | 15,673 | 12,860 | 5,191 |
| `skills/subagent-driven-development/references/setup.md` | absent | absent | 478 |
| `skills/subagent-driven-development/references/task-loop.md` | absent | absent | 3,124 |
| `skills/subagent-driven-development/references/what-a-report-voices.md` | absent | absent | 487 |
| `skills/subagent-driven-development/implementer-prompt.slots.md` | 1,160 | 1,067 | 1,067 |
| `skills/subagent-driven-development/task-reviewer-prompt.slots.md` | 742 | 715 | 715 |
| `skills/subagent-driven-development/re-review-prompt.slots.md` | 1,159 | 1,101 | 1,101 |
| `skills/subagent-driven-development/references/disputes-and-adjudication.md` | absent | absent | 1,328 |
| `skills/subagent-driven-development/references/drift.md` | absent | absent | 507 |
| `skills/subagent-driven-development/references/inline-mode.md` | absent | absent | 351 |
| `skills/requesting-code-review/SKILL.md` | 6,292 | 4,772 | 4,772 |
| `skills/requesting-code-review/code-reviewer.slots.md` | 1,118 | 1,127 | 1,137 |
| `skills/subagent-driven-development/references/finish.md` | absent | absent | 1,907 |
| `skills/finishing-a-development-branch/SKILL.md` | 3,991 | 3,903 | 3,903 |
| `skills/brainstorming/references/folded-lane-document.md` | 662 | 503 | 503 |
| `skills/redteaming/references/folded-lane.md` | 1,272 | 867 | 867 |
| `skills/brainstorming/references/lane-note.md` | 656 | 608 | 608 |
| `skills/subagent-driven-development/references/very-small-lane.md` | 3,224 | 2,732 | 2,732 |
