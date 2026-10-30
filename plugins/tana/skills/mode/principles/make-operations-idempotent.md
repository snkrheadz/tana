# Make operations idempotent
Open when: writing a command, lifecycle step, migration, or loop that may be retried, restarted, or killed midway.

Design each step to reach the right end state however many times it runs and wherever the last run stopped. Ask: what if this runs twice? What if the previous run died at any line?

- Derive actions from what exists now: read current state, compare to the goal, apply only the difference. A repeat then has nothing to do.
- Leftovers (locks, temp files, half-written records, claimed jobs) must be recognizable as stale by the next run, using evidence true wherever it crashed. Write to a temp path and rename into place; compare by content, not creation order.
- If the answer to either question is "it depends what was left behind", add a reconcile step.
