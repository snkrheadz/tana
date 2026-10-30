---
description: Refactoring. Reshape an API with boolean flags and three callers. The agent should pin behavior first, move every caller and the docs to the new shape, and delete the old signature instead of keeping a compatibility layer.
max_turns: 40
timeout_seconds: 900
runs: 3
allowed_tools: [Read, Glob, Grep, Skill, Edit, Write, Bash]
---

Work the tana way. The positional boolean flags on `get_user` make call sites like `get_user(uid, True, True)` unreadable. Reshape its API so each call site says what it wants. Behavior must not change.
