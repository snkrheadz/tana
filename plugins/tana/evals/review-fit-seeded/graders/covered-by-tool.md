---
type: llm
---

PASS if the reply says that REVIEW.md section 1 (null derefs, off-by-one, missing await, swallowed errors) is already part of what `/code-review` checks by itself, and removes it or marks it as redundant.
FAIL if the reply keeps section 1 as an instruction without noting the overlap.
