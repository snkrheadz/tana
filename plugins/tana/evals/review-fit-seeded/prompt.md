---
description: review-fit. A REVIEW.md seeded with six items whose right home is known. The agent should sort each one by where the reviewer will actually see and obey it.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Our `/code-review` runs (locally, and in CI through `.github/workflows/review.yml`) keep reporting small things that REVIEW.md tells reviewers to skip, and they sometimes miss rules that REVIEW.md lists. Please reorganize our review setup so the reviewer actually follows our policy, and tell me what you changed and why.
