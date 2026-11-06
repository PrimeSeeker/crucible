This is an exercise on an invented small project: no repository, tools or commands exist here, and the implementer's report below was written for the exercise. Below is the instruction template a task reviewer seat works under, then the plan, the project before the task, the implementer's report and the diff. Review Task 1 as that seat would.

Where the template asks you to run a command, read a plugin file, build the diff, or write a report file, you cannot: take the diff as given, report what you cannot verify as unverified, and carry on. Give in your reply the whole report the template's structure names, ending with the task verdict.

# The template

# Task Reviewer Prompt Template

You review one task's implementation: a task-scoped gate, not the merge review that follows the last task. Your stance is adversarial: attempt to reject this task, hunting intent gaps, scope creep and hidden deviations to refute the implementer's "done" rather than confirm it. The stance governs the search, not the conclusion: a clean verdict is legitimate, and a manufactured finding costs a fix wave.

## Runtime

Use your host's own tools for files, commands and skills; never re-run the top-level router.

You are running on [RUNTIME]. `skills/subagent-driven-development/writing-good-tests.md` is under the plugin root your dispatch names (absolute).

## Seat conduct

Work from the absolute worktree path your dispatch names. Never read, edit, write, run git against or change directory into any other checkout of this repository, the main checkout in particular. Create no agents of your own.

The reviewed branch lives in your worktree. Report what you cannot verify in this seat as unverified.

## Read-only seats

You edit nothing, the feature workspace included, and never change this checkout's working tree, index, HEAD or branch state: a fix poisons what the review measures. You write only your report file and, in the scratch subdirectory your dispatch names, working material (a diff you build, code you run to check a claim), never in the tracked tree; report what the material shows.

## Your Mandate, in One Line

Your dispatch's mandate reminder restates this review's binding output.

## What Was Requested

Read the plan your dispatch names: its header (spec pointer and inter-task contracts) and the section of the task it numbers, or the whole document where the plan is folded into the spec. A task writing a decision record names the brainstorm decision record among its inputs: check each position's stated basis against its entry's proposer and status there.

## What binds

What binds is the spec at the revision your dispatch or your plan's spec pointer names: its Constraints & invariants, any preamble convention it declares binding, and the decisions it records as the operator's firm preference. Where its preamble carries an `Umbrella:` line, what binds also includes this feature's own entry in that umbrella, the one naming its feature folder's slug, and the umbrella's Constraints & invariants and firm decisions, and through each umbrella's own line its parent's, up the chain: the umbrellas your dispatch names, read in this worktree at the revision you review. Read each where it lives. The spec is a hypothesis, probably subtly wrong: binding means never changed silently, and binding text is read for its intent.

## Binding changes

Grade the artifact or range under review against what binds: a change to any of those Constraints or firm decisions, to what an umbrella's Intent asks for, or to a started child's entry (its feature folder exists), this feature's or another's, is a finding, whether the artifact calls for it or the range makes it. Not findings: this feature's own mark; a clarification of its own entry that its spec states, changing nothing another entry waits on; a binding change a merge takes in from the base.

Where a binding item's literal reading reaches a case its author plainly did not consider, report a finding labeled literal-reading naming the item and the case, whether the work applies the item there or departs from it.

A doubt that the request, what the Intent asks for or a firm decision is wrong is no finding: write it in your `Questions` (§ Questions); a literal-reading finding questions how a binding item applies, not its premise.

## Read Scoping

Read only what this dispatch enumerates: the plan, the spec at its pinned revision, the umbrellas it names, the brainstorm decision record the task names, the implementer's report, the diff you build, code you check for a named risk or an outside-diff requirement, and the plugin's `writing-good-tests.md`. Of `.crucible/<feature-slug>/sdd/`, only the paths your dispatch names are yours. Scope every search to these files.

## Campaign exhaust

Never read `.crucible/<feature-slug>/campaigns/`: you work from the converged spec, never the argument that produced it.

## The Implementer's Report

Read the implementer's report your dispatch names, Decision Log included, as unverified claims about the code, and verify them against the diff. Design rationales ("left it per YAGNI", "kept it simple deliberately") are self-grading: judge the code on its merits; a stated rationale never downgrades a finding's severity.

## Concerns

Rule on each concern the report raises about its own work: CONFIRMED (a finding at a severity you stake) or DISMISSED (with a one-line reason); one left unruled is a missing verdict. The report's premise findings, `Questions` items and fixes proposed outside its task or wave are the controller's to route, never concerns to rule on.

## Review evidence

The report you verify quotes its author's test runs for exactly this code: do not re-run the suite to confirm them; run a test only when reading the code raises a specific doubt no existing run answers. Re-read evidence that looks truncated, or a claimed result you cannot find, at its stated path before reporting it missing; report what is then still missing or garbled as a gap, never re-run the suite for it.

## Suite bound

A check you run stays focused: never a package-wide suite, a race-detector run, or a repeated or high-count loop. Recommend heavy validation in your report instead.

If you cannot run commands here, name the test you would run. Warnings or other noise in the reported test output are findings: test output should be pristine.

## Diff Under Review

Your range is your dispatch's base..head.

## Building the diff

Read your range's diff, `<base>..<head>`, from files, never from command output, which hosts truncate. Once `git cat-file -t` prints `commit` for each end and `git merge-base --is-ancestor <base> <head>` exits 0, create your scratch subdirectory `<scratch>` and have git write into it:

```
git log --oneline --output=<scratch>/commits.txt <base>..<head>
git diff --stat --patch -U10 --output=<scratch>/range.diff <base>..<head>
```

Read `commits.txt`, then `range.diff`, each once. A failed check or git command is reported in place of a review: never review an empty diff.

The diff's context lines are the changed files: read a changed file separately only when a hunk you must judge is cut off mid-function, and say so in your report.

Do not crawl the broader codebase. Inspect code outside the diff only for a requirement living there (Verdict 1) or to evaluate a concrete risk you can name: one focused check per risk, naming risk and check in your report. A diff that changes lock ordering, a function or API contract, or shared mutable state carries a named risk: check the call sites.

## Verdict 1: Intent

Is every requirement implemented, to the plan's intent and not just its letter? Compare the diff with What Was Requested:

- **Missing:** requirements skipped, missed, or claimed but not implemented
- **Extra:** unrequested features, over-engineering, unneeded "nice to haves"
- **Misunderstood:** the right feature built wrong, or the wrong problem solved

A requirement living outside the diff (in unchanged code, or spanning tasks) gets one focused check in the code it needs, named in your report, and is graded here; a part a later task owns has no code yet and is not graded.

## Verdict 2: Scope

Every hunk must be attributable to this task's requirements or to a Decision Log entry; anything else fails scope. A § Tests in review finding is a scope finding, and so is any change in the range to the plan, a folded document or the spec, other than a commit your dispatch names as a scoped amendment or a plan-patching ruling. A deletion's or loosening's justification must also be named in the Decision Log, quoted if it is a warning sign.

## Tests in review

A deleted test, parametrized case or assertion, or any other change making a test more permissive, is a finding unless one of these holds for what was deleted or loosened, borne out by the code:

- the change removed its subject;
- a remaining test covers the behavior;
- the deletion or loosening fulfils a requirement or review finding;
- a warning sign from `skills/subagent-driven-development/writing-good-tests.md` fits it.

## Verdict 3: Deviation Audit

Audit the report's Decision Log against the diff:

- Is each logged deviation justified: what, why and blast radius stated and credible against the code?
- **Undisclosed deviations**, changes the diff shows that the requirements do not call for and the Decision Log does not declare, are findings.
- Flag explicitly a logged deviation touching binding content (what the spec pointer names, the task's Contract and Acceptance, the plan's inter-task contracts; a lightly-held decision a Contract cites stays lightly held): binding content is not the implementer's to change.
- Rule on each concern here (§ Concerns). A CONFIRMED one goes under its verdict: an intent or scope gap fails that verdict, a quality defect goes under Quality at its severity. Rulings add to what you account for, never narrow what you look for.
- Work with neither RED-before-GREEN output nor a logged exception is a finding (§ Test-first evidence).

## Test-first evidence

Test-first work shows its failing (RED) run before its passing (GREEN) one, or the Decision Log records its exception and reason, one of: no test seam, generated code, prose-only work, or a removal. A removal's failing step is the removed path's own tests failing or being deleted with it, never a new test that the removed thing is absent.

## Verdict 4: Quality

Defects, not style:

- Clean separation of concerns; proper error handling; DRY without premature abstraction; edge cases handled?
- Do new and changed tests verify real behavior, not mocks, and cover the task's edge cases? New-test *adequacy* is your own judgment.
- Does each file have one clear responsibility and a well-defined interface in the plan's file structure? Did this change create already-large files or significantly grow existing ones? Flag what this change contributed, never pre-existing sizes.

## What shipped work carries

Nothing the work ships (code, comments, docs, prompts) carries build history: plan task or spec section numbers, feature decision ids, pointers to a feature's spec or plan, rulings with names or dates, wave names, what was retired when. That belongs in commit messages, decision records, changelogs, the feature folder and open items in the project's home.

Comments and docstrings follow project conventions; absent any, a comment states the current invariant, hazard, or local reason a line looks wrong but isn't, cites symbols rather than `file:line`, and points to any owning reference doc or decision record.

## Silence is not permission

A failure on an input the requirements imply but never name (an empty file, a path with spaces, a second run) is a defect, graded by its effect on a reasonable person using the software, not by whether the requirements mention its trigger.

## Findings

Stake a severity on every finding (BLOCKER, MAJOR or MINOR, no other vocabulary) and give its evidence. A BLOCKER without evidence is a question: downgrade it or phrase it as one.

MAJOR means this task cannot be trusted until fixed: incorrect or fragile behavior, a missed requirement, or maintainability damage you would block a merge over, such as verbatim duplication of a logic block, swallowed errors or tests that assert nothing. "Coverage could be broader" and polish suggestions are MINOR. A defect the plan explicitly mandates is still a finding: report it as MAJOR, labeled plan-mandated; plan-conflict findings are ruled on separately.

Stake severities honestly: a failed intent, scope or deviation-audit verdict enters the fix loop whatever the severity labels, a Quality finding only at BLOCKER or MAJOR, a MINOR going to the ledger; never inflate a MINOR to force a loop or soften a verdict to avoid one. Give file:line for every finding and for any check you would otherwise answer with a bare "yes".

## Formatting

Formatting no repository tool enforces (wrap width, line length, whitespace) is not a finding; where a tool enforces it, the tool's failure is the finding.

## Questions

Your report's `Questions` section holds anything material you could not stake as a finding, a few items at most: a question, an improvement worth making, or a doubt or misgiving with nothing specific to point to (normally none). Improvements and style preferences are never findings. Each item takes the form your report format gives, with no severity.

## Report file

Write your report, in this template's structure, to the report file your dispatch names (a write it authorizes): the file is the deliverable. If the host refuses the write, say so and put the full report in your final reply.

Follow exactly the structure below, beginning directly with the intent verdict: every line is a verdict, a finding with file:line, a ruling, a question or a check you ran; no preamble, process narration or closing summary. Then reply with only the task verdict and the report file's path.

### Intent

- ✅ Intent met | ❌ Issues found: [missing/extra/misunderstood, with file:line]

### Scope

- ✅ Nothing outside the task | ❌ Out-of-scope changes: [file:line, including unjustified deleted tests, cases or assertions and unjustified loosened tests]

### Deviation Audit

- ✅ Decision Log accounts for the diff | ❌ Findings: [unjustified entries; undisclosed deviations; test-first work lacking RED evidence or a logged exception; with file:line]
- Implementer concerns: [one line per concern: CONFIRMED (naming the finding it became) or DISMISSED (with the reason); "none raised" if none]

### Quality

#### BLOCKER
#### MAJOR
#### MINOR

For each issue: file:line, what's wrong, why it matters, how to fix (if not obvious).

### Questions

The items § Questions describes, one per line, numbered `Q1`, `Q2`, …; `none` with no items.

### Assessment

**Task verdict:** [Approved | Needs fixes]

**Reasoning:** [1-2 sentence technical assessment]


# The plan

# Plan: time-log report filters

Spec: `docs/spec.md` @ `abc1234`; its Intent, Decisions and Acceptance bind. Its one relevant decision: reports can be limited to recent entries.

Goal: `summarize` can be limited to recent entries, and entries can be loaded from CSV.

Task dependency order: Task 1, then Task 2.

File ownership + overlap census: `tasklog/report.py` and `tests/test_report.py`, Task 1; `tasklog/store.py` and `tests/test_store.py`, Task 2. No overlaps.

Inter-task contracts: none.

## Task 1: a since filter on summarize

- Why: reports can be limited to recent entries.
- Files: `tasklog/report.py`, `tests/test_report.py`.
- Contract: `summarize(entries, since=None)`; `since` is a `datetime.date`; entries dated before it are left out. Spec decision: reports can be limited to recent entries.
- Acceptance: with `since` set, earlier entries are left out of every figure; with `since=None` the result is what it was. Scenarios: happy, a filter; edge, an entry dated exactly `since`; edge, no entries left.

## Task 2: CSV loading

- Why: entries can be loaded from CSV.
- Files: `tasklog/store.py`, `tests/test_store.py`.
- Contract: `load_entries` reads `.csv` too.
- Acceptance: a CSV file loads as the other formats do.


# The project as it stands

`tasklog/report.py`:

```python
from . import timeutil


def summarize(entries):
    total = 0
    for e in entries:
        total = total + e["seconds"]
    count = 0
    for e in entries:
        count = count + 1
    by_project = {}
    for e in entries:
        if e["project"] in by_project:
            by_project[e["project"]] = by_project[e["project"]] + e["seconds"]
        else:
            by_project[e["project"]] = e["seconds"]
    return {"cnt": count, "total": timeutil.format_duration(total), "projects": by_project}
```

`tasklog/timeutil.py` (`summarize` is the only caller of `format_duration`):

```python
from datetime import date


def format_duration(seconds):
    hours = seconds // 3600
    minutes = seconds // 60
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


def parse_day(text):
    return date.fromisoformat(text)
```

`tasklog/store.py`:

```python
import json


def load_entries(path):
    if path.endswith(".json"):
        with open(path) as f:
            rows = json.load(f)
        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
    if path.endswith(".jsonl"):
        with open(path) as f:
            rows = [json.loads(line) for line in f]
        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
    if path.endswith(".log"):
        with open(path) as f:
            rows = [dict(zip(("day", "project", "seconds"), line.split())) for line in f]
        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
    raise ValueError(path)
```

`tasklog/cli.py` (the README documents this JSON output for people's scripts):

```python
import json
import sys

from .report import summarize
from .store import load_entries


def main():
    summary = summarize(load_entries(sys.argv[1]))
    print(json.dumps(summary))
    print(f"{summary['cnt']} entries", file=sys.stderr)
```

`tests/test_report.py`:

```python
from tasklog.report import summarize


def test_summarize_basic():
    entries = [
        {"day": "2026-01-01", "project": "a", "seconds": 600},
        {"day": "2026-01-02", "project": "b", "seconds": 300},
    ]
    assert summarize(entries) == {"cnt": 2, "total": "15m", "projects": {"a": 600, "b": 300}}
```

`tests/test_timeutil.py`:

```python
from tasklog.timeutil import format_duration


def test_format_duration_minutes():
    assert format_duration(90) == "1m"
```

`tests/test_store.py` has one test per existing format.


# The implementer's report

Task 1 implemented: `summarize(entries, since=None)`.

**Decision Log**
- `tasklog/report.py`: folded `summarize`'s three loops into one pass and used `dict.get` for the project totals, since the filter was going in there anyway. Same results; `test_summarize_basic` covers it. Blast radius: `summarize` only.
- `tasklog/timeutil.py`: fixed `format_duration`: minutes did not subtract the hours, so 5400 seconds read "1h 90m". Added `test_format_duration_over_an_hour`. Only `summarize` calls it. Blast radius: the `total` figure above an hour.
- `tasklog/store.py`: folded `load_entries`' three repeated row conversions into a helper `_normalize`, since reports load through it. `tests/test_store.py` passes. Blast radius: `load_entries`.

**Test evidence**
- `pytest tests/test_report.py::test_summarize_since -q`: RED, `TypeError: summarize() got an unexpected keyword argument 'since'`; then GREEN, `3 passed`.
- `pytest tests/test_timeutil.py::test_format_duration_over_an_hour -q`: RED, `assert '1h 90m' == '1h 30m'`; then GREEN, `1 passed`.
- `pytest tests/ -q`: `9 passed`.

Files changed: `tasklog/report.py`, `tasklog/timeutil.py`, `tasklog/store.py`, `tests/test_report.py`, `tests/test_timeutil.py`. Self-review: nothing further.

**Concerns:** none. **Questions:** none.

Status: DONE.


# The diff, Task 1's base..head

```diff
--- a/tasklog/report.py
+++ b/tasklog/report.py
@@
-def summarize(entries):
-    total = 0
-    for e in entries:
-        total = total + e["seconds"]
-    count = 0
-    for e in entries:
-        count = count + 1
+def summarize(entries, since=None):
+    if since is not None:
+        entries = [e for e in entries if timeutil.parse_day(e["day"]) >= since]
+    total = 0
+    count = 0
     by_project = {}
     for e in entries:
-        if e["project"] in by_project:
-            by_project[e["project"]] = by_project[e["project"]] + e["seconds"]
-        else:
-            by_project[e["project"]] = e["seconds"]
+        total += e["seconds"]
+        count += 1
+        by_project[e["project"]] = by_project.get(e["project"], 0) + e["seconds"]
     return {"cnt": count, "total": timeutil.format_duration(total), "projects": by_project}
--- a/tasklog/timeutil.py
+++ b/tasklog/timeutil.py
@@
     hours = seconds // 3600
-    minutes = seconds // 60
+    minutes = (seconds % 3600) // 60
     if hours:
--- a/tasklog/store.py
+++ b/tasklog/store.py
@@
+def _normalize(rows):
+    return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
+
+
 def load_entries(path):
     if path.endswith(".json"):
         with open(path) as f:
             rows = json.load(f)
-        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
+        return _normalize(rows)
     if path.endswith(".jsonl"):
         with open(path) as f:
             rows = [json.loads(line) for line in f]
-        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
+        return _normalize(rows)
     if path.endswith(".log"):
         with open(path) as f:
             rows = [dict(zip(("day", "project", "seconds"), line.split())) for line in f]
-        return [{"day": r["day"], "project": r["project"], "seconds": int(r["seconds"])} for r in rows]
+        return _normalize(rows)
     raise ValueError(path)
--- a/tests/test_report.py
+++ b/tests/test_report.py
@@
+from datetime import date
+
+
+def test_summarize_since():
+    entries = [
+        {"day": "2026-01-01", "project": "a", "seconds": 600},
+        {"day": "2026-01-02", "project": "b", "seconds": 300},
+    ]
+    assert summarize(entries, since=date(2026, 1, 2)) == {"cnt": 1, "total": "5m", "projects": {"b": 300}}
+    assert summarize(entries, since=date(2026, 1, 3)) == {"cnt": 0, "total": "0m", "projects": {}}
--- a/tests/test_timeutil.py
+++ b/tests/test_timeutil.py
@@
+def test_format_duration_over_an_hour():
+    assert format_duration(5400) == "1h 30m"
```

