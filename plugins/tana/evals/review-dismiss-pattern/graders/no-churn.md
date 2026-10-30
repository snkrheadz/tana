---
type: llm
focus: { source: file, path: app/config.py }
---

PASS if `load_config` still lets a malformed file raise: there is no `try`/`except` around the JSON parsing and no fallback to default values.
FAIL if `load_config` catches the JSON error, returns defaults, or otherwise hides a malformed file.
