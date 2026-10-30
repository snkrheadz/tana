---
type: llm
---

PASS if the reply says the failure is not flaky because the re-run failed the same way, and does not recommend re-running CI again as the fix.
FAIL if the reply treats it as a possible flake to retry, or does not address the repeated failure.
