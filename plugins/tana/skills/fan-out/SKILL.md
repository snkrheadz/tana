---
name: fan-out
description: Split work into parallel workers, collect their results, and return one merged report. Use for /tana:fan-out or "fan this out", for broad coverage, races between approaches, or sweeps over many pieces.
disable-model-invocation: true
---

# Fan out

Start with `../mode/pillars/one-rod.md`. Fan out only for a reason it lists, and put that reason in each worker's brief. Many sequential edits that depend on each other are not a fan-out.

## 1. Frame

1. Write the done condition and the report you need back.
2. Choose the shape:
   - **Slices**: split the work into independent parts, one worker each.
   - **Race**: several workers on the same brief. Decide now how to read the race: first pass wins, rank all, or best of.
   - **Mixed**: slices, each raced.
3. Pick the model per worker. Search and listing: `haiku`. Mechanical work or a clear spec: `sonnet`. Review and judgment: `opus`. For a race between models, name each worker's model before you start.
4. Workers that write get their own worktree (`isolation: "worktree"`) or distinct files. Two writers on one file is a collision.
5. If workers measure or verify commits, name the exact commit hashes and the method (sample count, what counts as one sample, order) in each brief. Workers record both in their reply.

## 2. Spawn

Send every `Agent` call in one message, `run_in_background: true`, `subagent_type: "general-purpose"` (or `Explore` for read-only search).

Each brief stands alone: goal, scope, the exact slice or race arm, how to check, and what to report. Ask for a verdict of `PASS`, `ISSUES`, or `BLOCKED`, with evidence. A worker that proves a defect lists every one it can prove.

Requests to one web host go one at a time. Do not give parallel workers the same host.

If a worker never returns, go on without it and note the gap.

For dozens of similar pieces, a `Workflow` script with a check per piece is better than hand-spawning. Offer it only if the user opted into multi-agent runs.

## 3. Merge

Read the results as they finish. Do not wait on polling; you are notified. Then:

- Reject a result that lacks the hashes or method its brief demanded. Respawn that worker once. After a second miss, record a gap. A gap is not a pass.
- For coverage, every slice needs a result.
- For a race, apply the rule you chose in step 1.
- Read the evidence yourself before you trust a verdict (`../mode/pillars/sounding.md`).

## 4. Report

Reply with one report: a table of slice or arm against verdict, one line per issue, gaps and dropouts, and the race rule if used. Never paste worker output wholesale.
