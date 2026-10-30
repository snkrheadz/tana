---
name: lock-in-lessons
description: Find the mistakes that keep recurring in this repo and make each one impossible to repeat. Use for /tana:lock-in-lessons or "stop making the same mistake", "why do we keep fixing this".
disable-model-invocation: true
---

# Lock in lessons

Some mistakes come back every few sessions. A note in `CLAUDE.md` does not stop them. A
change to the repo does. Read `../mode/pillars/log-the-catch.md` for where a lesson
belongs and how to move a rule into a check. This skill finds the lessons worth moving.

Assume the next contributor has only the files it opened, copies the nearest example,
and stops when the code compiles.

## 1. Collect

1. Read `git log` for reverts and "fix" commits, closed PR review comments, and
   `tasks/lessons.md` if it exists.
2. Grep for comments that explain a workaround and for rules in `CLAUDE.md` that start
   with "never" or "always".
3. Optionally scan recent session JSONL under `~/.claude/projects/<project>/` for
   user messages that correct the agent. Use `Explore` with `model: "haiku"`.

Group the findings into classes. A class counts after two occurrences. A single
incident is a fix, not a lesson.

## 2. Pick the strongest home

For each class, try these in order and stop at the first that works.

1. Remove the possibility: one owner for the state, one supported way to do the task,
   an internal module that cannot be imported from outside, a list generated from one
   source. Delete the old path an agent would copy.
2. Make the type reject it, or add a lint or CI check whose error names the thing to
   use instead.
3. Write a test on the behavior. Delete tests that pass when the behavior breaks.
4. Add a hook if the rule is about what the agent may do.
5. Write prose only for judgment calls, and give the reason.

Measure first, as `../mode/pillars/sounding.md` says. Run the proposed check over the
whole repo and look at what it flags before you enforce it.

## 3. Prove it

1. Reproduce a real past mistake from the history. Show the new check fails on it.
2. Land one class per commit, so each can be reverted alone.
3. Run the same command locally and in CI.
4. Mark exceptions on the offending line with the reason.

## 4. Keep a rule table

In `CLAUDE.md`, keep one table: rule, then what enforces it. When a rule has no
enforcer and is broken again, move it up a level in the same change. Delete a rule once
its mistake cannot happen.

## Report

For each class: the evidence, the home you chose, and why a stronger home did not fit.
