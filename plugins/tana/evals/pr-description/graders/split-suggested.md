---
type: llm
focus: trace
---

PASS if the agent noticed that the branch mixes two unrelated changes (the invoice CSV export and the `_fmt` to `format_money` rename) and recommended splitting them into separate PRs, or wrote the description for the feature and flagged the rename as belonging in its own PR.
FAIL if the description presents both as one change without suggesting a split.
