---
name: statechart
description: Model a system that moves between states in TLA+, check it with TLC, and draw the state graph as a Mermaid stateDiagram. Use for /tana:statechart, or to show a bug as a path through states.
disable-model-invocation: true
---

# Statechart

Write a small TLA+ spec of the flow, let TLC check the rules, and draw what it explored. The reader of the chart decides whether the behavior is right, so label everything in their words. For why a model counts as a check, see `../mode/pillars/sounding.md`.

## Tools

- Work in a scratch folder outside the repo.
- Java must be on `PATH` (`java -version`).
- If `tla2tools.jar` is missing, download it from the official TLA+ releases: `curl -L -o tla2tools.jar https://github.com/tlaplus/tlaplus/releases/latest/download/tla2tools.jar`. Needs network. Pin the version in the hand-off.
- Converter: `python3 -I <skill dir>/dot_to_mermaid.py graph.dot > chart.mmd` (standard library only).

## Steps

1. Write `Spec.tla` and `Spec.cfg`. Each rule the reader agrees with is an `INVARIANT`. If the model has no variable for a rule, add one. Never weaken a rule to make it hold.
2. Write `Next` as a disjunction of named actions, such as `Pay \/ Cancel`, so TLC labels the edges with those names.
3. A correct end state has no step out and TLC reports deadlock. Either add an action that is true only there and changes nothing (`Done == phase = "paid" /\ UNCHANGED vars`) or pass `-deadlock`.
4. Keep constants small, or add a `CONSTRAINT`. A model without bounds can run forever.
5. Run it:
   ```sh
   java -XX:+UseParallelGC -jar tla2tools.jar -workers 1 -config Spec.cfg \
     -metadir states -dump dot,actionlabels graph.dot Spec.tla | tee tlc.out
   ```
   `-dump dot` writes the graph even when a rule breaks, so the chart also shows states after the bug.
6. Convert: `python3 -I dot_to_mermaid.py graph.dot > chart.mmd`.
7. Relabel for the reader. The script prints raw variable values and action names. Edit `chart.mmd` by hand: rename states to what the reader sees ("Paying", "Lease held, write pending"), rename arrows to what they do ("you press play"), and merge states that act the same.
8. Aim for about 20 arrows. Drop steps every state has, such as a reset, and say in the hand-off which you hid.

## Reading a violation

TLC prints the shortest trace to the first broken rule in `tlc.out`. Number its steps and write each in plain words. In the chart, mark the state where the rule breaks (`classDef breaks fill:#fdd` and `class s3 breaks`). Do not merge two states that break different rules.

For a large graph, TLC may print more states than a chart can show. Over about 500 states, draw only the path to each broken rule and report the state count.

## Hand off

Show `chart.mmd` as a `mermaid` code block. Per bug, give the rule, the reader's sentence for it, and the numbered path. Say what the model leaves out, and give the exact command and jar version that rebuild the files.

If the model describes real code, replay each bug path against the code as a test or a live run. If the bug does not happen there, suspect the model first.
