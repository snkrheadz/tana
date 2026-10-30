---
name: vet-measurement
description: Vet a performance number before you report it or act on it. Use for /tana:vet-measurement, or when you ran a benchmark and are about to claim a speedup or a regression.
disable-model-invocation: true
---

# Vet a measurement

A number is a claim. Before you report it, run it through seven questions and answer each from a run, not from reading the code. `../mode/pillars/sounding.md` explains why spread matters.

A rough figure the user asked for can be one run. Say it is one run, and still answer questions 4 and 7. A choice between two options is never a rough figure.

## Before the first run

1. Write the sentence you hope to ship, for example "import is 30% faster at p50 on the 60k-row file".
2. Read the measuring script. Note what it times and what it leaves out.
3. Run `uptime`. If the machine is busy, find the cause. If you cannot stop it, alternate the sides so both see the same noise, and say so.

## Seven questions

1. **What limits it?** Find the bottleneck in a separate, unreported run, since profilers slow things down. Look at CPU per process, a language profiler (`py-spy`, `node --cpu-prof`, `perf`), I/O wait. Check the load generator too: it may be the thing you measured.
2. **Is each side tuned the way production is?** Same build mode, flags, pool sizes, cache state, data, versions. If a side runs on defaults, you compared settings, not code. Tune it and rerun.
3. **Does the arithmetic allow it?** Compare throughput with disk and network limits, and the time saved with the time that piece took. Cutting a 10% piece cannot give more than about 11%. Beyond a limit means you measured a cache or a no-op.
4. **Did anything fail?** Count errors and bad responses, and check outputs are right. Failures are often fast.
5. **Does it repeat?** Run each side at least five times, alternating A, B, A, B. Report median and range. A gap inside the range is no gap.
6. **Does it matter end to end?** Time the path a user waits on, with realistic size and concurrency. Say the micro result as a share of that.
7. **Did the work happen?** Confirm the rows were written, the bytes read, the result used. Lazy iterators, unawaited promises and timeouts give fast numbers for nothing.

## Report

- First word: faster, slower, no measurable difference, or inconclusive.
- Then the number with unit, run count, range, and the limiter. Example: "p50 41 ms to 33 ms, median of 7 per side, range 32 to 35 ms, bound by JSON parsing on one core."
- Call it inconclusive if you cannot name the limiter, a side was untuned, or questions 4 or 7 went unchecked. Name the gap.
- A PR body gets one number; see `../mode/playbooks/opening-a-pr.md`. Keep the runs in notes.
