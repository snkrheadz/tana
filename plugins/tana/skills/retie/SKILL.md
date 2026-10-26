---
name: retie
description: Audit a Claude Code setup by removing each config item, rerunning real tasks, and keeping only what changes behavior. Use for "retie", "config retest", or a periodic config review.
---

# Retie

Anglers retie before a season, not because the knot looks bad but because a knot that
has held for months is the one that fails without warning. Claude Code config ages the
same way. A rule written for an older model, a hook that guards against a habit the
model no longer has, a skill nobody triggers: each still costs context on every run.
This skill finds out which items still earn their place, by measuring.

Read `../mode/pillars/log-the-catch.md` first. This skill is that pillar applied to
the config itself.

## 1. Inventory

List every item and what it claims to change. One row each.

| Kind | Where to look |
| :- | :- |
| CLAUDE.md sections | `~/.claude/CLAUDE.md`, the project's `CLAUDE.md`, `.claude/rules/` |
| Hooks | `hooks` in `~/.claude/settings.json` and `.claude/settings.json`, plus each enabled plugin's hooks |
| Skills and agents | `~/.claude/skills/`, `.claude/skills/`, `.claude/agents/`, plugin skills |
| Plugins | `enabledPlugins`. `claude plugin details <plugin>` gives each one's always-on token cost |

For each row write the behavior it should cause, phrased so a run can show it or not
("opens a PR only after a review", "routes search subagents to haiku").

Mark rows the repository or the system prompt already supplies (a convention visible
in the tree, a rule the harness states) as **derivable**. They are candidates to cut
without a run.

## 2. Pick the tasks

Choose two to five real tasks from this project's history (`git log`, closed PRs,
past sessions) that would exercise the rows you are least sure about. A task that
never triggers a row tells you nothing about it. If a row only fires on delegation,
pick a task large enough to tempt delegation.

Write each task as the prompt a user would type, with no hint about what is being
measured.

## 3. Run with and without

Never edit the live config during a run. Work in a git worktree or the scratchpad.

- **A CLAUDE.md section:** run headless with `--setting-sources project,local` so the
  user `CLAUDE.md` is not loaded, and pass the variant with
  `--append-system-prompt-file`. One arm gets the full text, the other the text
  minus the section.
- **A plugin, or a skill inside one:** `claude plugin eval` runs cases with and
  without the plugin.
- **A hook:** pass a `--settings` file that leaves the hook out, against one that
  keeps it.

Mechanics that bite:

- Feed `claude -p` its prompt as an argument and redirect stdin from `/dev/null`.
  A loop that reads tasks from stdin will otherwise hand the rest of the file to the
  first run.
- Capture `--output-format stream-json --verbose` and read the tool calls from the
  stream. The final text says what the agent believes it did, the tool calls show
  what it did.
- Pass `--allowedTools` one comma-joined argument (`"Read,Edit,Bash(git *)"`) and
  smoke-test it with one cheap run: confirm from the stream that a Bash call
  succeeded before launching the paid runs. A denied tool silently changes the task.
- Run each task at least twice per arm. Budget each run with `--max-budget-usd`.
- Before paying for runs, read what usage history already shows: transcripts
  under `~/.claude/projects/` record every tool call, skill invocation, and model.
  An item with zero use in two months, or one that is followed 99% of the time,
  may need no run at all. Count from `tool_use` blocks, not from tool names
  anywhere in the file, which also match tool listings.
- Say the cost before starting. A full pass is several sessions.

## 4. Verdict per row

| Verdict | When |
| :- | :- |
| **Keep** | Removing it changed behavior in a way you want, or it states something no run can derive |
| **Cut** | Both arms behaved the same on tasks that exercised it, or it is derivable |
| **Open** | No task exercised it. Say what task would, and leave it in place |
| **Move** | It changed behavior, but a test, lint, hook, or script could enforce it more cheaply than prose |

Compare per task, not by totals. One task that flipped matters more than an average
that did not move.

## 5. Land it

- Make the cuts and moves in one change, with the evidence table in the PR or commit
  message: row, tasks, result per arm, verdict.
- Delete the prose version of anything moved into a hook or test in the same change.
- Record the date and the next one (about six months out) where this setup keeps its
  notes, so the next retie starts from this one.
