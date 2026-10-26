# Feature

1. **Learn the water.** Read the code the feature will touch and the callers that
   depend on it. If the area is large, send one read-only subagent to map it and
   return file paths and a short summary (pillar 3, the context-flood case).
2. **Name the data shape.** Write down the types, the states, and who owns each piece
   of state before writing logic. Many branches over the same flags usually want a
   table, a state machine, or a typed model instead.
3. **Sound the depth.** Read `pillars/sounding.md`. Decide what you will observe when
   the feature works, and take the before reading.
4. **Build in small steps.** Each step ends in a check that passes before the next
   step starts. Commit at each green step if the user works with commits.
5. **Check with the real thing.** Run the feature the way its user will. If the change
   is large or the design was a close call, ask a fresh-context subagent to review the
   diff against the request, and judge its findings yourself.
6. **Trim.** Read your own diff once more and remove what the feature does not need:
   speculative options, one-caller helpers, comments that restate the code.

Reply with what the user can now do, the design choices that were close calls and why
you chose as you did, what you observed, and any decision left open.
