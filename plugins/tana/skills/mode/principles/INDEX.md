# Principles

| File | Open when |
| :- | :- |
| [attack-the-premise.md](attack-the-premise.md) | two or more fixes built on the same belief have failed the same check. |
| [boundary-discipline.md](boundary-discipline.md) | adding validation, error handling, or glue between your logic and a framework or outside system. |
| [build-the-lever.md](build-the-lever.md) | the work is more than a couple of obvious edits, or someone must be able to re-check what you did. |
| [encode-lessons-in-structure.md](encode-lessons-in-structure.md) | you are about to write the same instruction twice, or a correction keeps coming back. |
| [exhaust-the-design-space.md](exhaust-the-design-space.md) | a UI interaction or architecture choice has no precedent in the codebase and the right answer depends on feel. |
| [experience-first.md](experience-first.md) | a product, UX, or scope trade-off pits convenience for the builder against value for the user. |
| [explain-the-number.md](explain-the-number.md) | you are about to measure something, or about to trust or report a speedup, regression, latency, throughput, or eval score. |
| [fix-root-causes.md](fix-root-causes.md) | debugging, and the obvious change would be a guard, retry, or catch near where it blew up. |
| [foundational-thinking.md](foundational-thinking.md) | choosing core types or data structures, ordering scaffold against feature work, or letting concurrent actors share something. |
| [guard-the-context-window.md](guard-the-context-window.md) | output is large, files are long, you are rereading things, or planning a wide sweep. |
| [laziness-protocol.md](laziness-protocol.md) | sizing a diff, or tempted to add an abstraction, layer, or extra parameter threading. |
| [make-operations-idempotent.md](make-operations-idempotent.md) | writing a command, lifecycle step, migration, or loop that may be retried, restarted, or killed midway. |
| [migrate-callers-then-delete-legacy-apis.md](migrate-callers-then-delete-legacy-apis.md) | you introduce a new internal API while the old one still has callers. |
| [minimize-reader-load.md](minimize-reader-load.md) | code is hard to trace, or you are about to add a layer or a piece of state. |
| [model-the-domain.md](model-the-domain.md) | writing stateful logic, or the same if/else or shape assumption is spreading across files. |
| [never-block-on-the-human.md](never-block-on-the-human.md) | you are about to ask "should I do X?" about work that can be undone. |
| [outcome-oriented-execution.md](outcome-oriented-execution.md) | carrying out a planned rewrite or migration with explicit phases. |
| [prove-it-works.md](prove-it-works.md) | you are about to say a task is done. |
| [redesign-from-first-principles.md](redesign-from-first-principles.md) | fitting a new requirement into an existing design. |
| [separate-before-serializing-shared-state.md](separate-before-serializing-shared-state.md) | concurrent actors (agents, workers, jobs, branches) may write the same thing. |
| [sequence-verifiable-units.md](sequence-verifiable-units.md) | doing a sweep, migration, or any run of similar edits, or deciding how to order commits. |
| [subtract-before-you-add.md](subtract-before-you-add.md) | starting a change in an area with dead code or unused options, or about to polish before the core works. |
| [test-behavior-not-implementation.md](test-behavior-not-implementation.md) | writing or reviewing a test, or a refactor broke tests that should not have broken. |
| [type-system-discipline.md](type-system-discipline.md) | defining types, handling outside data, or seeing impossible states and mixed-up primitives. |
