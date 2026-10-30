---
name: failing-test-first
description: Pin a bug with a test that fails before the fix and passes after. Use for /tana:failing-test-first, "write a regression test first", or when a bug has a cheap local test target.
disable-model-invocation: true
---

# Failing test first

A test you have only seen pass proves nothing. Write it, watch it fail for the right reason, then fix. The reasoning is in `../mode/pillars/sounding.md`; the full loop is in `../mode/playbooks/bug-fix.md`.

## When to use it

Use it when the repo has a test file near the broken code and the bug can be stated as input and expected output. Skip it, and say so, when the test would need heavy mocks, slow end-to-end setup, production-only data, or a pile of new fixtures. A weak test is worse than none. Use the closest cheap check instead: a script, a `curl`, a snapshot diff, a log assertion.

## Steps

1. State the bug in one line: what should happen, what happens, on which input.
2. Find the nearest existing test for that code. Match its style and helpers.
3. Write the smallest test that expresses the correct behavior. It must describe what the code should do, not copy what it does now.
4. Run only that test. Read the failure. It must fail because of the bug in the report. If it passes, or fails on a typo or a missing import, fix the test and rerun. Do not touch product code yet.
5. Make the smallest fix. See `../mode/pillars/light-tackle.md`.
6. Run the test again, then the tests next to it.

## Rules

- Never edit a test just to fit a wrong result.
- Never loosen an existing assertion unless the intended behavior really changed, and then say why.
- If the bug is flaky, make the test deterministic first (fixed clock, fixed seed), or the pass means nothing.
- If the bug points to a whole class of failures, land the one regression test first. Add sibling cases after.

## Report

- The test or check you used, and the exact failure it gave before the fix.
- The run after the fix, plus the neighbours you ran.
- If you could not see it fail first, say why and name the substitute check.
