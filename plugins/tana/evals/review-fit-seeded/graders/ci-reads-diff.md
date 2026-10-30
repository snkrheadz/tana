---
type: llm
---

PASS if the reply explains the CI runs with no findings by the reviewer failing to read the diff (for example a denied command under `--permission-mode dontAsk`, such as one using `$(...)`), AND proposes making the diff readable regardless (writing it to a file the reviewer reads first, or similar) or treating a run that never read the diff as a failure to re-run rather than a pass.
FAIL if the reply treats empty CI runs as clean reviews, or does not address them.
