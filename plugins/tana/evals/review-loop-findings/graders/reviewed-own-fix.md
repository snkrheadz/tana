---
type: llm
focus: trace
---

PASS if, after its last code edit and before calling the branch ready, the agent looked at its own changes as a reviewer would (for example ran `git diff` and read it, or re-read every changed function and its callers) and ran the tests.
FAIL if the agent declared the branch ready without re-reading its own final changes, or without running the tests after the last edit.
