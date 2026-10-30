---
type: llm
---

PASS if the reply says that the "only report verified minor issues / no performance nitpicks" text cannot reliably override `/code-review high`, because the high level is built to favor recall (surface uncertain findings), AND it proposes a mechanism instead of prose: a lower level such as `medium` (precision), `--max-findings`, or filtering the output by verdict or category in the CI step.
FAIL if the reply keeps or rewrites that instruction as prose and expects the reviewer to obey it, or does not address it.
