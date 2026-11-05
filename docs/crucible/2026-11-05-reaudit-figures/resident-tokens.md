# Re-audit figures: tokens loaded per route and carried per seat

Counted by `resident_tokens_reaudit.py` (its docstring states the method), tokenizer `claude-opus-5-5`.
A route's total reads **every run** (with every conditional file added).

## Controller loads, compaction-fit manifest, with the two omitted reads

### standard

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 22,147 (+4,522) | 22,205 (+4,606) | 22,228 (+4,606) |
| spec campaign | 17,827 (+6,012) | 15,983 (+5,859) | 16,212 (+5,859) |
| plan | 6,578 | 5,933 | 5,933 |
| execution | 18,734 | 15,743 | 12,163 (+2,186) |
| branch review and finish | 11,401 | 9,802 | 11,719 |
| **total** | **79,145** (89,679) | **72,172** (82,637) | **70,761** (83,412) |

### folded

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 26,907 (+4,522) | 25,928 (+4,606) | 25,951 (+4,606) |
| spec campaign | 21,579 (+6,012) | 19,563 (+5,859) | 19,792 (+5,859) |
| execution | 18,734 | 15,743 | 12,163 (+2,186) |
| branch review and finish | 11,401 | 9,802 | 11,719 |
| **total** | **81,079** (91,613) | **73,542** (84,007) | **72,131** (84,782) |

### very-small

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 22,803 (+4,522) | 22,813 (+4,606) | 22,836 (+4,606) |
| execution | 21,222 (+10,152) | 18,486 (+10,731) | 12,133 (+12,566) |
| branch review and finish | 12,560 | 10,903 | 12,820 |
| **total** | **59,043** (73,717) | **54,708** (70,045) | **50,295** (67,467) |

### umbrella campaign

| Phase | `a3db87f` | `d78398c` | `4026f6b` |
|---|---|---|---|
| session start | 2,458 | 2,506 | 2,506 |
| brainstorm | 26,669 | 26,811 | 26,834 |
| spec campaign | 17,827 (+6,012) | 15,983 (+5,859) | 16,212 (+5,859) |
| landing | 6,471 | 6,616 | 6,616 |
| **total** | **53,425** (59,437) | **51,916** (57,775) | **52,168** (58,027) |

## Controller loads, prose-compaction manifest, with the two omitted reads

### standard

| Phase | `0deefcf` | `56e8475` | `5546425` |
|---|---|---|---|
| session start | 2,506 | 2,271 | 2,369 |
| brainstorm | 22,228 (+4,606) | 10,318 (+2,945) | 10,562 (+3,014) |
| spec campaign | 16,212 (+5,859) | 15,691 (+2,220) | 16,909 (+2,220) |
| plan | 5,933 | 4,182 | 4,186 |
| execution | 12,163 (+2,186) | 9,386 (+1,787) | 10,126 (+1,862) |
| branch review and finish | 11,719 | 8,933 | 9,104 |
| **total** | **70,761** (83,412) | **50,781** (57,733) | **53,256** (60,352) |

### folded

| Phase | `0deefcf` | `56e8475` | `5546425` |
|---|---|---|---|
| session start | 2,506 | 2,271 | 2,369 |
| brainstorm | 25,951 (+4,606) | 13,458 (+2,945) | 13,759 (+3,014) |
| spec campaign | 19,792 (+5,859) | 16,083 (+2,220) | 17,301 (+2,220) |
| execution | 12,163 (+2,186) | 9,386 (+1,787) | 10,126 (+1,862) |
| branch review and finish | 11,719 | 8,933 | 9,104 |
| **total** | **72,131** (84,782) | **50,131** (57,083) | **52,659** (59,755) |

### very-small

| Phase | `0deefcf` | `56e8475` | `5546425` |
|---|---|---|---|
| session start | 2,506 | 2,271 | 2,369 |
| brainstorm | 22,836 (+4,606) | 10,831 (+2,945) | 11,088 (+3,014) |
| execution | 12,133 (+12,566) | 9,372 (+9,154) | 10,286 (+9,348) |
| branch review and finish | 12,820 | 9,774 | 9,995 |
| **total** | **50,295** (67,467) | **32,248** (44,347) | **33,738** (46,100) |

### umbrella campaign

| Phase | `0deefcf` | `56e8475` | `5546425` |
|---|---|---|---|
| session start | 2,506 | 2,271 | 2,369 |
| brainstorm | 26,834 | 15,085 (+621) | 15,467 (+690) |
| spec campaign | 16,212 (+5,859) | 15,691 (+2,220) | 16,909 (+2,220) |
| landing | 6,616 | 3,859 | 3,859 |
| **total** | **52,168** (58,027) | **36,906** (39,747) | **38,604** (41,514) |

## Head references and cards in no route's manifest

- `skills/subagent-driven-development/references/seat-rules.md`
- `skills/using-crucible/references/claude-code.md`
- `skills/using-crucible/references/codex-dispatch.md`
- `skills/using-crucible/references/codex.md`

## Seat text per dispatch: tokens (words)

| Seat | `a3db87f` | `d78398c` | `4026f6b` | `0deefcf` | `56e8475` | `5546425` |
|---|---|---|---|---|---|---|
| redteam-seat | 5,991 (2,904) | 5,461 (2,688) | 5,461 (2,688) | 5,461 (2,688) | 3,622 (1,847) | 3,520 (1,779) |
| blind-verifier | 1,691 (821) | 1,656 (812) | 1,656 (812) | 1,656 (812) | 1,145 (600) | 1,145 (600) |
| terminal-pass | 6,691 (3,317) | 5,914 (2,912) | 5,914 (2,912) | 5,914 (2,912) | 4,402 (2,203) | 4,428 (2,217) |
| implementer | 7,181 (3,503) | 6,094 (2,951) | 6,094 (2,951) | 6,094 (2,951) | 4,691 (2,297) | 4,831 (2,354) |
| task-reviewer | 7,237 (3,523) | 6,022 (2,892) | 6,022 (2,892) | 6,022 (2,892) | 4,660 (2,265) | 4,740 (2,300) |
| re-reviewer | 3,360 (1,567) | 3,886 (1,864) | 3,886 (1,864) | 3,886 (1,864) | 3,285 (1,591) | 3,312 (1,607) |
| branch-reviewer | 8,273 (4,037) | 7,638 (3,752) | 7,626 (3,760) | 7,626 (3,760) | 5,183 (2,527) | 5,364 (2,622) |
| **one of each** | **40,424** (19,672) | **36,671** (17,871) | **36,659** (17,879) | **36,659** (17,879) | **26,988** (13,330) | **27,340** (13,479) |
