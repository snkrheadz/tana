---
type: llm
---

PASS if the reply keeps every review run's findings in a record that outlives the PR, AND says why the current places do not work (the sticky comment is overwritten on each push, the artifact expires after 14 days), AND puts the record where a new agent session can read it without cloud credentials (for example an append-only file on a side branch, or a file in the repo).
FAIL if the reply relies on the sticky comment, the artifact, or a store that needs cloud credentials to read at session start.
