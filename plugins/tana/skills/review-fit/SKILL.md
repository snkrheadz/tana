---
name: review-fit
description: Fit a repository's review setup (REVIEW.md, review rules in CLAUDE.md, the CI review step) to what `/code-review` actually reads and returns, so the reviewer enforces the project's rules and its findings settle. Use when `/code-review` keeps reporting what the policy says to skip, misses project rules, never gets to zero findings, when the same findings keep coming back across PRs, or when asked to tidy REVIEW.md or the review setup.
---

# Review fit

Bait the fish is not feeding on stays on the hook all day. A review policy written where
the reviewer does not look, or phrased against how it searches, gets the same result:
the rules are missed and the noise stays.

Read `contract.md` first. It records what `/code-review` reads, how it searches, and what
it returns, measured on one Claude Code version. If `claude --version` differs, run
`probe.sh` (a few dollars) and go by its numbers.

## 1. List every instruction that steers review

REVIEW.md, review rules in any CLAUDE.md or `.claude/rules/`, the CI step that runs the
reviewer (its prompt, level, schema, and any filtering after it), and PR template
checklists. One row per instruction, with what it asks for.

## 2. Give each row one home

| Home | The row is | Do |
| :- | :- | :- |
| Nowhere: the reviewer already does it | A restatement of a built-in angle: null and off-by-one bugs, missing `await`, reuse, simplification, efficiency, root-cause depth | Delete it. A copy costs context and adds findings |
| A CLAUDE.md or a path-scoped `.claude/rules/` file | A project rule the reviewer should enforce, sayable in one quotable sentence with its reason | Move it. Prefer a path-scoped file when it covers one area |
| A test, a type, or a lint rule | A rule with a recognizable shape in code (unused export, forbidden import, naming table) | Build the check (`../mode/pillars/log-the-catch.md`), then delete the prose. A check that only comments does not stop anything |
| A flag or code in the review step | A wish about which findings appear: only confirmed ones, no nitpicks, severities, when to approve | Use the level or `--max-findings`, or filter and map by verdict and category in the CI step. Prose loses to the level's stance |
| A document for humans | Dependabot, release, who may approve | Keep it, outside what the reviewer is fed |

## 3. Make local and CI judge the same way

- One command reproduces the CI verdict locally: same level, same inputs, same mapping.
  Without it the author cannot run the check that will judge the work before pushing it.
- Record the Claude Code version CI pins. Re-run `probe.sh` when it moves.

## 4. Close the loop across PRs

- **Record every run** where it outlives the PR and a new session can read it without
  cloud credentials, such as an append-only file on a side branch. A sticky comment that
  is overwritten or an artifact that expires loses the first occurrence.
- **Signal a repeat where it cannot be missed**: a SessionStart hook that prints it
  before work starts, or a required check that fails until the rule has a guard. Issues
  and labels go unread.
- **Pick one number and take its baseline now**, from the history you already have:
  review rounds per PR, or the share of findings on lines the previous push changed.

## 5. Measure before you keep it

A change to review config is a change to behavior. Pick three to five merged PRs with
known real findings (bugs fixed after review) and known noise (findings closed without a
change). Run `/code-review` on each `base...head` with the old setup and the new one, at
least twice each. Keep the change if the real findings are still found and the rest
drops. Read the PRs whose result flipped. A `high` run on a mid-sized PR cost $0.6 to
$2.9 in one repo, so state the estimate before running.

## 6. Ship it as its own change

The review setup is team policy and often the merge gate. Put it in its own PR, apart
from feature work, with the before and after numbers. A person merges it.
