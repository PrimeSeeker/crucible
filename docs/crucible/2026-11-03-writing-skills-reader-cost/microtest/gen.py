"""Build the fix-recipe micro-test prompts: two real review findings x four guidance arms.

Arms: control (writing-skills SKILL.md at the pre-change commit), recipe and recipe2 (control plus one
sentence each), rewrite (SKILL.md at the commit --rewrite-at names; the arm is left out without it). Each prompt asks a fresh agent to
apply the finding to the file as it stood before the fix, writing its edits as JSON to out/.

    python gen.py [--repo <repository root>] [--prompts <dir>] [--rewrite-at <commit>]

Runs write their JSON where --out names (a new temporary directory by default; the committed runs are in out/, beside this file), and the prompts go where --prompts names (likewise temporary by default).
"""
import argparse, pathlib, subprocess, tempfile

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--repo", default=str(HERE.parents[3]))
ap.add_argument("--prompts", default=None, help="where prompts go; a new temporary directory by default")
ap.add_argument("--out", default=None, help="where runs write their JSON; a new temporary directory by default")
ap.add_argument("--rewrite-at", default=None, help="the commit whose skills/writing-skills/SKILL.md the rewrite arm uses")
args = ap.parse_args()
REPO = pathlib.Path(args.repo)
OUT = pathlib.Path(args.out or tempfile.mkdtemp(prefix="microtest-out-"))
PROMPTS = pathlib.Path(args.prompts or tempfile.mkdtemp(prefix="microtest-"))
PROMPTS.mkdir(parents=True, exist_ok=True)
OUT.mkdir(exist_ok=True)

PRE_CHANGE = "a3eb3ca"  # writing-skills as it stood before this lane
CASES_AT = "56e8475^"  # the files as they stood before the prose-compaction review fixes


def git_show(spec):
    return subprocess.run(["git", "-C", str(REPO), "show", spec], capture_output=True, check=True).stdout.decode("utf-8")


ws = git_show(f"{PRE_CHANGE}:skills/writing-skills/SKILL.md")
anchor = "State each rule once, where its reader acts on it, and point to it from elsewhere."
assert ws.count(anchor) == 1
recipe = anchor + " A fix to existing text rewrites the sentence that owns the case so that it states the corrected rule; where no sentence owns the case, the fix is one sentence beside the rule it extends."
recipe2 = anchor + " A fix revises the sentence that owns the case; its added words are the rule's new condition or action, stated as the sentence states its others, while the finding's reasons, its failure scenario and what a pointer already defines stay out of the text."
arms = {
    "control": ws,
    "recipe": ws.replace(anchor, recipe),
    "recipe2": ws.replace(anchor, recipe2),
}
if args.rewrite_at:
    arms["rewrite"] = git_show(f"{args.rewrite_at}:skills/writing-skills/SKILL.md")

cases = {
    "setup": {
        "path": "skills/subagent-driven-development/references/setup.md",
        "finding": (
            "MINOR (loss) - setup.md, the ledger-seeding list. Premise asks left open in the brainstorm "
            "decision record (`.crucible/<feature-slug>/brainstorm-decisions.md`) are never seeded into the "
            "ledger. Under an umbrella, a child inherits the umbrella's open premise asks through its brainstorm "
            "decision record, not through the plan record or the spec campaign's close, so the seeding list misses "
            "them. Failure: a child feature's controller starts execution with an inherited premise ask absent "
            "from `## Adjudication rulings`; the branch review and the close readout, which read the ledger, never "
            "surface it to the operator."
        ),
    },
    "umbrella": {
        "path": "skills/brainstorming/references/umbrella-children.md",
        "finding": (
            "MINOR (loss) - umbrella-children.md, the binding-change paragraph. Before the split into this file, "
            "the rules on a binding change to an umbrella said that the operator's ruling also decides whether the "
            "change takes a campaign (an umbrella's review is a spec campaign or the operator's approval, "
            "`skills/brainstorming/references/umbrellas.md` § Review). The paragraph now goes from the decision "
            "ask straight to landing. Failure: a controller lands an operator-approved binding change without "
            "asking whether it needs a campaign, so a change that should have been redteamed reaches every child "
            "in flight unreviewed."
        ),
    },
}

PREFACE = """Apply a review finding to a file in the repository of a process plugin whose skills instruct coding agents.

The project's guidance for writing text that instructs agents is below, under "Guidance"; read it before changing the file. Then apply the finding, under "Finding", to the file, under "File" (path `{path}`, shown whole).

Use only the text in this prompt: read no other file, search nothing, run no command. Your only tool call is one Write.

Output: write a JSON file to `{outdir}/{case}-{arm}-<RUN>.json` (the run number is in your dispatch message), holding one object: `{{"edits": [{{"old_string": "...", "new_string": "..."}}], "note": "<one line: what you changed>"}}`. Each `old_string` must occur exactly once in the file, as an exact-match edit tool requires. Then reply with the single word `done`.

# Guidance

{guidance}

# Finding

{finding}

# File

{file}
"""

for cname, c in cases.items():
    text = git_show(f"{CASES_AT}:{c['path']}")
    with (PROMPTS / f"{cname}-original.md").open("w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    for aname, g in arms.items():
        p = PREFACE.format(path=c["path"], outdir=OUT.as_posix(), case=cname, arm=aname, guidance=g, finding=c["finding"], file=text)
        with (PROMPTS / f"prompt-{cname}-{aname}.md").open("w", encoding="utf-8", newline="\n") as f:
            f.write(p)
print("prompts in", PROMPTS)
print("runs write to", OUT)
