# Separate before serializing shared state
Open when: concurrent actors (agents, workers, jobs, branches) may write the same thing.

First ask whether they need the same object. Usually they do not.

1. List shared mutable things: files both read and write, branches both push to, APIs one defines and another consumes.
2. Default to giving each actor its own file, key, branch, or directory, and merge only when reading or reporting. Two workers each writing a field into one state file still share; two separate state files do not.
3. If one shared target is a genuine invariant, enforce order structurally: lockfile, sequential phases, a single writer, or compare-and-swap. A rule in a prompt is not concurrency control.

Treat "we need a lock" as a design smell to examine. For agents this means worktrees or disjoint files (`../pillars/one-rod.md`). Races are intermittent and expensive to debug, so remove them by design.
