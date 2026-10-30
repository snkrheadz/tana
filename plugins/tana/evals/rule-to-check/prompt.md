---
description: Pillar 4. Turn a repeated review rule into a check in a repo that already breaks it. The agent should measure false positives, baseline the existing violations in a ledger that can only shrink, and update every copy of the prose.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. The reviewer has flagged `print()` in `src/` on two PRs already (see the git log). Turn that rule into a check that makes `python3 -m unittest` fail when someone adds a new one. Do not remove the existing calls in this change; that cleanup is separate.
