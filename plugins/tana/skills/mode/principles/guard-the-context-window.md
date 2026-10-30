# Guard the context window
Open when: output is large, files are long, you are rereading things, or planning a wide sweep.

A full context makes reasoning worse and eventually stops the work. Keep raw bulk out of the main thread and keep conclusions in it.

- Send sweeps, long logs, and crawls to a subagent that returns a short result (`../pillars/one-rod.md`).
- Read the lines you need (offsets, grep) rather than whole files; do not reread what you already hold.
- Plan in phases with a bounded number of files each, and count what orchestration itself costs.
- Write intermediate findings to a scratch file so a long task can resume without replaying it.
