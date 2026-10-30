# What `/code-review` reads and returns

Measured on 2026-10-30 with Claude Code 2.1.314, headless
(`claude -p "/code-review high <base>...HEAD"`). The command is part of Claude Code and
changes with it. If `claude --version` is not 2.1.314, run `probe.sh` and trust its
numbers over this file.

## What it reads as project rules

- Its conventions check is told to look for CLAUDE.md files: the user's
  `~/.claude/CLAUDE.md`, the repo root `CLAUDE.md`, and `CLAUDE.md` / `CLAUDE.local.md`
  in directories above the changed files. It flags a rule only when it can quote the rule
  and the line that breaks it.
- Placement probe (one rule seeded in one place, a repo of 45 files with a 58 KB
  REVIEW.md, 3 runs each). Runs that cited the rule:

  | Where the rule lived | Cited |
  | :- | :- |
  | `CLAUDE.md` at the repo root | 3/3 |
  | `.claude/CLAUDE.md` | 3/3 |
  | `.claude/rules/*.md` with `paths:` matching the change | 3/3 |
  | Only inside REVIEW.md | 2/3 (1/3 in an earlier, flawed set) |

  In a 4-file repo every placement was cited, because the reviewer printed every file.
  Headless runs reviewed in one context and did not fan out to subagents; the interactive
  fan-out was not measured. The REVIEW.md in this probe was a real 58 KB review document;
  `probe.sh` uses synthetic filler where the rule stands out more, so it scores higher.
- So a rule the reviewer must enforce goes in a CLAUDE.md or a path-scoped rule file.
  REVIEW.md is read only when the reviewer happens to explore it.

## How it searches

- `high` runs eight finder angles: three for correctness, three for cleanup (reuse,
  simplification, efficiency), one for root-cause depth, one for conventions.
- `high`, `xhigh` and `max` favor recall: a candidate with a nameable failure scenario is
  kept even when it is only half believed. `medium` favors precision.
- Caps on reported findings: low 4, medium 8, high 10, xhigh and max 15.
  `--max-findings <n|all>` changes it.
- Consequence: any real diff yields cleanup candidates. A 7-line diff drew 3 to 9 findings
  in the probe, more in the larger repo with more rules. Zero findings is not a
  target `high` is built to reach.

## What it returns

- Each finding has a file, line, summary, failure scenario, category (a bug angle,
  `reuse`, `simplification`, `efficiency`, `altitude`, `conventions`, or a narrower
  slug), a verdict (`CONFIRMED` or `PLAUSIBLE`) when a verify pass ran, and an outcome
  after `--fix`. There is no severity field. Text output is a list ranked most severe
  first.
- A gate written as blocking / major / minor needs your own mapping: a `--json-schema`
  on the CI call, or a script over the findings.

## What steers it

- Flags: the level (`low` to `max`, or `ultra` in the cloud; with no level it reuses the
  last one typed), `--max-findings`, `--fix`, `--comment`.
- Prose cannot reliably override the level's stance. One repo told its CI reviewer to
  report only confirmed minor findings; unconfirmed ones kept appearing, and the repo
  ended up filtering them in code.
