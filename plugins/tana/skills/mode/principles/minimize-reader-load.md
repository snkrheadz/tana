# Minimize reader load
Open when: code is hard to trace, or you are about to add a layer or a piece of state.

Judge code by what a reader must do to follow it, on two separate axes: layers between a question and its answer, and hidden mutable state they must remember. A flat file of many globals can be as bad as a deep adapter stack.

The layer rules (inline single-caller wrappers, delete pass-through) live in `../pillars/light-tackle.md`. Beyond that:

- Prefer interfaces that hide real decisions; a wide interface hiding little forces readers to learn both sides.
- Shrink state scope: returns over mutation, locals over fields, fields over module state, module state over globals. Derive values rather than syncing them.
- State an invariant once at the boundary, not in every consumer.
- Test: can a newcomer say where X comes from and what can change it within half a minute?
