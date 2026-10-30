---
name: plan-big-change
description: Design a reviewable playbook for work no existing playbook fits, such as a large migration or a multi-part change a human reads after stepping away. Use for /tana:plan-big-change or "figure out how to do this big thing".
disable-model-invocation: true
---

# Plan a big change

When no playbook in `../mode/playbooks/` fits, the first deliverable is the plan itself: phases sized to the risk, a loop that tests hypotheses, and a trail a person can audit later.

Start by rereading `../mode/SKILL.md` and its pillars.

## 1. Frame

Ground first, then commit. Do not begin until you can state:

- Done, as a predicate that could be false (`../mode/pillars/sounding.md`).
- Scope in rough units and effort, plus blockers you found while grounding.
- Rigor level, leaning high. One-way doors and wide blast radius get gates and artifacts. Reversible small steps get less. Rigor means gates, not trying harder.

Show the framing and its tradeoffs. Reversible work goes ahead (`../mode/pillars/keep-moving.md`), but a run of hours earns one check-in.

## 2. Design the plan

1. Split into units that can land alone. Do the riskiest unknown first.
2. Build the check before the work. Capture a baseline from the untouched tree, so the result reads "old value, new value".
3. For a one-way design choice, use `/tana:sketch-design` (which may call `/tana:compete`). Skip it when the shape is already settled; a second contest over a settled design is waste.
4. Decide what fans out. Only across real seams, each worker in its own worktree. Do not over-split (`/tana:fan-out`, `../mode/pillars/one-rod.md`).
5. Write the phase list in a file. That list is what the human reviews.

Then add its steps to your task list and run them.

## 3. Run each unit as an experiment

State the hypothesis. Make the smallest change (`../mode/pillars/light-tackle.md`). Measure against the done predicate on the real artifact. Keep it if it moved forward; revert it if not. Check each unit before the next one starts.

- Inspect the artifact, not a worker's claim. If something passes too easily, doubt your measuring first.
- If a delegated worker games the check, reset and tighten the contract. If the check is wrong, fix it in its own change.
- Verdicts are VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass.

## 4. Keep a trail

Record a row as each step lands, using `/tana:decision-log`. For work this large, commit the trail so the reviewer sees it in the PR.

## 5. Verify and hand back

Check the whole against the done predicate on the real product, not only the harness. Turn any repeated correction into a check, lint rule, or script (`../mode/pillars/log-the-catch.md`).

Reply with the plan, the rigor level and why, the trail path, what is verified against the predicate, and what is open.
