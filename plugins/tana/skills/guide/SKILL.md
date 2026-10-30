---
name: guide
description: Point to the tana skill, playbook, or principle that fits a task, or answer a question about how tana works. Use for /tana:guide or "which tana skill should I use".
disable-model-invocation: true
---

# Guide

Answer with one recommendation first, then at most two alternatives and why they lose.
If the task needs no tana piece at all, say so.

## Working style

`/tana:mode` turns on the style for the rest of the session: find the check before the
change, write less, keep one loop, turn repeated lessons into structure, keep reversible
work moving. It routes each task to a playbook in `../mode/playbooks/`. Check these first;
a playbook usually fits better than a skill for everyday work:

| Situation | Playbook (through `/tana:mode`) |
| :- | :- |
| A check is red on a PR or branch, including a test you did not touch | `red-check` |
| Something is broken | `bug-fix` |
| New or changed behavior | `feature` |
| Review findings to act on | `review-loop` |
| Opening a PR or writing its description | `opening-a-pr` |
| A question to answer with no code change | `investigation` |

## By task

| You want to | Use |
| :- | :- |
| Understand how some code works or where a change belongs | `/tana:explain-code` |
| Know why the code is the way it is, or what caused a regression | `/tana:trace-why` |
| Have a body of work explained so a person understands it | `/tana:teach` |
| Hear the last answer again in plain words | `/tana:plain-words` |
| Check that the agent understood the goal | `/tana:restate-goal` |
| Get caught up on what happened while you were away | `/tana:catch-up` |
| Rebuild the agent's own working context after a break | `/tana:rebuild-context` |
| Make a task deeper before starting it | `/tana:sharpen` |
| Sketch types and module shape before writing code | `/tana:sketch-design` |
| Try several implementations and keep the best parts | `/tana:compete` |
| Cover a lot of ground in parallel and get one report | `/tana:fan-out` |
| Challenge a design or diff from several angles | `/tana:stress-review` |
| Find what a change could break beyond the diff | `/tana:blast-radius` |
| Plan a large or ambiguous change someone will audit later | `/tana:plan-big-change` |
| Start a fix or feature from a failing test | `/tana:failing-test-first` |
| Trust a performance number before acting on it | `/tana:vet-measurement` |
| Give a project a skill that drives its app like a user | `/tana:create-verify-skill`, then `/tana:maintain-verify-skill` |
| Add formal checks where bugs cost most | `/tana:create-formal-check`, then `/tana:maintain-formal-check` |
| Model a state machine and draw it | `/tana:statechart` |
| Stop agents repeating the same mistake in this repo | `/tana:lock-in-lessons` |
| Learn from the session that just ended | `/tana:retro` |
| Keep a decision trail during long or unattended work | `/tana:decision-log` |
| Turn your own preferences into a reusable skill | `/tana:capture-my-style` |
| Remove comments that restate code | `/tana:comment-audit` |
| Cut machine-sounding phrasing from prose | `/tana:cut-ai-tells` |
| Write docs, PR text, or instructions clearly | `/tana:tech-writing` |
| Audit a Claude Code setup and keep only what earns its place | `/tana:retie` |
| Make REVIEW.md and the CI review match what `/code-review` reads | `/tana:review-fit` |

TypeScript conventions load on their own when `.ts` or `.tsx` files are read or edited.

## Principles

Short design rules live in `../mode/principles/`; `../mode/principles/INDEX.md` lists
each with when to open it.
