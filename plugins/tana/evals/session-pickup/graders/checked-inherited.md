---
type: llm
focus: trace
---

PASS if, before building on the note, the agent ran the existing tests (or an equivalent check) to confirm the "done and verified" claims, discovered that `weekly_csv` has no header row and its test fails, AND fixed `weekly_csv` (or clearly reported the broken claim and fixed it) rather than trusting the note.
FAIL if the agent took the note's "verified" claims at face value and never found the weekly failure.
