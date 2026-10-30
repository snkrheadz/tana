# Explain the number
Open when: you are about to measure something, or about to trust or report a speedup, regression, latency, throughput, or eval score.

A number is not a finding until you can say what bounds it and what else it might be measuring. Basics (repeat runs, spread) are in `../pillars/sounding.md`. The extra steps:

1. Before running, write which result would change a decision and how large the noise is. If run-to-run spread exceeds the effect, stop and fix the setup.
2. Ask why it is not twice as good. Name the limiter (a core, a lock, disk, network, the load generator) from a profile or counters taken during the run, not from reading code.
3. Rule out look-alikes with evidence: errors, cached or skipped work, code that never ran, one side left untuned, a piece too small to matter end to end.
4. Store run count, spread, and limiter next to the figure.

For evals, ask whether every trial really attempted the task and whether the gap holds across trials.
