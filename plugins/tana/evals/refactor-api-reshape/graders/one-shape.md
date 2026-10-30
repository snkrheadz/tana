---
type: llm
focus: trace
---

PASS if, at the end, all three callers (`api.py`, `report.py`, `admin.py`) use the new API, `docs/usage.md` describes the new API instead of the old flags, AND the old positional-boolean signature is gone rather than kept alive for compatibility (no wrapper, alias, deprecated path, or `*args` shim that still accepts `get_user(uid, True, True)`).
FAIL if any caller or the doc still uses the old form, or if the old signature still works through a compatibility layer.
