---
name: capture-my-style
description: Turn the user's working preferences into a skill or CLAUDE.md lines, backed by evidence from past sessions. Use for /tana:capture-my-style or "capture my preferences", "write down how I work".
disable-model-invocation: true
---

# Capture my style

Agents keep relearning how this user likes to work. Write it down once, in the place
that is cheapest to keep enforced. Read `../mode/pillars/log-the-catch.md` first.

## 1. See what exists

Read `~/.claude/CLAUDE.md`, the project `CLAUDE.md`, and auto-memory. Do not repeat a
rule that is already there. If a personal skill exists, you are updating it: mine only
sessions since its last edit (`git log -1 --format=%cI <path>` if it is in git).

## 2. Mine the history

Session transcripts are JSONL under `~/.claude/projects/<project>/`. Use only the
current project's folder unless the user names another.

Spawn up to three `general-purpose` subagents with `model: "sonnet"`, one per slice of
recent weeks. Each returns patterns with pointers to the turn. Signals to look for:

- Corrections: "no, shorter", "don't ask, just do it".
- Reply shape: length, format, language.
- Delegation: when the user wants subagents and which models.
- Done means: tests, a live run, a reviewer.
- Git habits: worktrees, commit style, who opens PRs.

A pattern in two or more slices is solid. A pattern seen once is noise. Drop it.

## 3. Ask about gaps

History cannot show intent that has not come up. Use `AskUserQuestion` for one or two
rounds of short multiple-choice questions on the areas the user cares about, then one
open question. Do not ask twenty.

## 4. Choose a home for each rule

| If the rule is | Put it in |
| :- | :- |
| Something a tool can check or block | A hook, lint, or test. Offer to build it |
| A personal preference that applies everywhere | `~/.claude/CLAUDE.md`, one line with the reason |
| A preference for one repo | The project `CLAUDE.md` |
| A procedure with judgment, used often | A skill the user invokes by name |
| A fact about the user | Auto-memory |

Write a skill only when several rules form a procedure. Most output should be a few
`CLAUDE.md` lines.

## 5. Draft and cut

1. Write each rule as an imperative with its reason. Skip generic advice. "Write clean
   code" changes nothing.
2. Point at other skills by path. Do not paste them in.
3. Skip a section if the user has no non-default rule there.
4. Run `/tana:cut-ai-tells` over the draft.
5. Show it, take edits, cut again.

Work on a branch or worktree if the target is under version control. Do not push.
