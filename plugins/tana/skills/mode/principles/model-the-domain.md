# Model the domain
Open when: writing stateful logic, or the same if/else or shape assumption is spreading across files.

Put the real domain into a structure so invalid states cannot be written and branches disappear. Doing it while writing is cheap; recovering it later is a refactor that gets postponed.

- Several booleans or phase checks: a state machine.
- Loose parameters: a typed record. Branching across files: a table, registry, or tagged union.
- Scattered mutations: a reducer or event model.
- Organize modules by domain knowledge, not by step order (load, validate, transform, save).

Do not force it. If the code is already clear and local, boring wins; an abstraction that removes no branch, duplicate rule, or bad state is just indirection. A warning sign: a feature adds one more branch to a chain, or a second flag that must track the first. Short form: `../pillars/light-tackle.md`.
