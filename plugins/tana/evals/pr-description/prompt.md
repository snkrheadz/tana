---
description: PR loop. A branch mixes a feature with an unrelated rename. The agent should write a short briefing (why, scope, what it could break, how it was verified by a run) and point out that the branch should be two PRs.
max_turns: 30
timeout_seconds: 600
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. Write the title and description for a pull request of this branch against `main`, into `PR.md`. Do not open the PR.
