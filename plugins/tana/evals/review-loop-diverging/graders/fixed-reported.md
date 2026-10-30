---
type: llm
focus: trace
---

PASS if, after the change, both confirmed bypasses are blocked or can no longer delete anything (`rm --recursive --force build/` and `r\m -rf build/`), the existing cases are still blocked, `ls -la` still runs, AND the agent showed this by running the guard or tests that cover those inputs.
FAIL if either confirmed bypass still gets through, if safe commands are now blocked, or if nothing was run to show it.
