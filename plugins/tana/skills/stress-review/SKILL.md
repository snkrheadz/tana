---
name: stress-review
description: Attack a design or a diff from several independent angles and keep only the findings a run proves. Use for /tana:stress-review or "stress test this", "tear this apart", "find blind spots", "challenge this design".
disable-model-invocation: true
---

# Stress review

The built-in `/code-review` reads a diff for line-level bugs. This skill goes further. Its attackers question the premise and the design too: wrong problem, wrong boundary, a case the plan forgot. Each attack must be proven by running something. Report findings. Do not fix them.

Use it for a risky change, a design before you build it, or a diff you do not trust. For an ordinary diff, `/code-review` is enough.

## 1. Frame

The scope is what the user names. Otherwise it is the branch diff from its merge base to the working tree. State the intent in your own words (`/tana:restate-goal`), drawn from the request, commits, and PR text. If you cannot tell the intent, ask.

## 2. Pick the angles

Choose three or four that fit. For example:

- **Input**: the odd, empty, huge, or hostile input.
- **Order and time**: retries, partial failure, two runs at once, teardown.
- **Premise**: is the assumption the design stands on true? Probe it.
- **Neighbors**: callers, data formats, other readers of the same state (run `/tana:blast-radius` thinking).
- **Rollback**: can this be undone cleanly?

## 3. Spawn attackers

This is a fresh-eyes case from `../mode/pillars/one-rod.md`: the reviewers must not be the author. Spawn one `Agent` per angle in a single message, `run_in_background: true`, `model: "opus"`, `isolation: "worktree"`. Copy uncommitted changes into each worktree first. Brief:

> Your job is to make this fail. Scope and intent are below, and your angle is X. A finding counts only if you demonstrated it on the real code: a test that fails, a script that reproduces it, or terminal output with the wrong result. If the target is a design or plan, write a throwaway probe or exercise the current tree. Do your experiments inside your own worktree. For every finding return a title, the command, what it printed, and what the intent says should have printed. Skip anything you did not execute: style, naming, structure, and risks that only appear after some later change. Finding nothing is an acceptable result.

## 4. Verify

Run every reported command again yourself. A finding stays if the rerun reproduces the failure and that failure contradicts the intent; anything else goes. Fold findings that trace to one cause into one. There is no winning attacker: all verified findings stay.

## Output

- **Intent**, as you restated it.
- **Findings**, each with its command, its output, the way it defeats the intent, and the angles that hit it. Say "no verified findings" if none held.
- **Dropped**: a count per attacker and the reason.
