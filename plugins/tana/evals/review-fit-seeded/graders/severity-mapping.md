---
type: llm
---

PASS if the reply points out that `/code-review` does not output blocking / major / minor severities (its findings carry a verdict such as CONFIRMED or PLAUSIBLE and a category), so the approve rule in REVIEW.md section 4 needs a mapping done by the CI step (for example a JSON schema or a script over the findings) or a rule restated in terms of verdict.
FAIL if the reply treats blocking / major / minor as something `/code-review` already emits, or ignores section 4.
