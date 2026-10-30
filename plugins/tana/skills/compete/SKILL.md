---
name: compete
description: Run N independent attempts at the same task in separate worktrees, pick the best as a base, and graft the best parts of the rest into it. Use for /tana:compete or "compete this", "try it several ways", when one attempt would lock in the wrong shape.
disable-model-invocation: true
---

# Compete

Use this when the artifact is costly to get wrong and the right shape is unclear. For routine work, one attempt is cheaper. Read `../mode/pillars/one-rod.md` first: this is the "parallel pieces" and "fresh eyes" case, and you must name that reason in each spawn.

## 1. Frame

All candidates get one identical prompt, so the prompt is the contract.

1. Say what artifact each candidate makes.
2. Write a rubric of 3 to 6 checks that can be graded on this task. Keep it to yourself and the judge. Candidates see only the task.
3. Pick N. Two is the floor, three is usual. Use more only for several distinct design directions.
4. Give each candidate its own place to write: a worktree via `isolation: "worktree"` on the `Agent` call, so no two share files. Use `subagent_type: "general-purpose"`.
5. Use `model: "opus"` when the work needs judgment. Use `sonnet` when it is generation from a clear spec. Same model N times is fine for the latter. For the former, vary the brief's angle ("minimize API", "minimize moving parts") so candidates differ.

## 2. Fan out

Send all N `Agent` calls in one message with `run_in_background: true`. Each brief holds the task, paths to shared notes, and the shape of the result: the artifact plus a short note on options considered and rejected.

If one candidate returns nothing, go on with N-1 and say so.

## 3. Judge

Wait until all candidates finish. Then spawn one more `Agent`, read-only, `model: "opus"`. It must not have written any candidate. It gets the rubric and the candidate paths, scores each check, and names a base with reasons. Do this while you read the candidates yourself.

## 4. Pick the base

Read every candidate through before choosing. Score by rubric item, not by feel. Compare with the judge's verdict. If you agree, the pick stands. If not, read both reasonings before you decide; either the rubric was vague or someone is biased.

Take the base that is easiest to extend without breaking its invariants. On a tie, take the smaller interface.

## 5. Graft

Reread each loser for the one or two ideas worth moving. Fold them in by hand so the result still has one coherent design (`../mode/pillars/light-tackle.md`). Do not merge mechanically.

If all candidates landed on the same shape, that is strong agreement. Ship it, no graft. If they scatter wildly, the frame was too loose. Tighten it and rerun instead of averaging.

## 6. Verify

Check the result as you would any output: find the check, run it, paste the observation (`../mode/pillars/sounding.md`). A fault the competition missed means either the frame was wrong (rerun) or a loser had the fix and you skipped it (go back to 5).

Remove the candidate worktrees when done.

## Output

The one artifact, and a short note: the base and why, the judge's verdict (or that no judge ran), each graft and its source, what was rejected, dropouts, and the verification result.
