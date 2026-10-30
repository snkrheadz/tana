---
name: decision-log
description: Keep a short TSV trail of decisions during long or unattended work so a reviewer can check it later. Use for /tana:decision-log, overnight runs, or multi-phase work someone reviews after you finish.
disable-model-invocation: true
---

# Decision log

When someone reviews your work after the fact, they need to see what you chose and why,
not just what changed. Keep one TSV file with a row per decision. See
`../mode/pillars/log-the-catch.md`, last section, for when a trail is worth keeping.

## Columns

`ts`, `phase`, `decision`, `why`, `evidence`, `result`. One line per cell. Evidence is a
pointer (commit, PR number, `file:line`, output path), never a paragraph.

## Write a row

Run `log.sh` from this skill's directory:

```bash
./log.sh decisions.tsv <phase> "<decision>" "<why>" "<evidence>" "<result>"
```

It adds the header on first use, stamps the time in UTC, flattens tabs and newlines, and
puts a quote before a cell that starts with `=`, `+`, `-`, or `@` so a spreadsheet does
not run it.

Write cells the way you would tell a teammate. Plain words, concrete actions.

Log forks, finished units with their check result, reverts with the trigger, blockers.
Do not log every command.

## Rules

1. Append only. A wrong call gets a later row that replaces it. Never edit old rows.
2. When a run resumes an existing log, its first row has phase `start`, and the evidence
   names the run. Use `start` for nothing else.
3. Keep the file in the work directory or the scratchpad, and out of git. Commit it
   only when the reviewer needs it to trust the result.

## Before you hand back

1. Read your own rows against the session's JSONL under
   `~/.claude/projects/<project>/`. Check that each row records something that happened
   and that its evidence resolves.
2. Add a row for any fork or abandoned approach that shaped the work and is missing.
3. Spawn one `opus` subagent that reads only the log and the transcript. Ask it for
   rows with weak evidence, checks claimed but not shown, risky choices, and gaps.
4. End your reply with an "Attention" section: the flags, each tied to a row, or
   "no flags".

To read the log in a terminal: `column -s$'\t' -t decisions.tsv`.
