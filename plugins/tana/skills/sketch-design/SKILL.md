---
name: sketch-design
description: Sketch types, signatures, and module boundaries before any real code, then fill them in against the chosen sketch. Use for /tana:sketch-design or "sketch the design", "design this first", or work where coding straight away would fix the wrong shape.
disable-model-invocation: true
---

# Sketch design

Write the shape of the code first: types, signatures, module map, with bodies that throw `not implemented`. Pick the shape. Then fill it in.

Keep it light. A small change gets one file of types. Only a large change gets a module map.

## 1. Ground

Read the code the new work touches until you can explain how it fits together, using `/tana:explain-code`. If the design moves ownership or layering, run `/tana:trace-why` on the current shape so its reasons become constraints. Skip this step only for greenfield work with nothing to join.

## 2. Sketch twice

Never settle on the first shape. Produce at least two structurally different candidates. Different layouts, not tweaks of one.

- Small task: draft both yourself.
- Hard or one-way decision: run `/tana:compete` with `references/candidate-brief.md` as the brief each candidate gets. That is a fresh-eyes use of subagents, so see `../mode/pillars/one-rod.md` for tiers. Design work runs on `opus`.

Write the caller's usage first: the quickstart a user would read and two or three real call sites. Derive the types from that. If they disagree, change the types.

Screen each candidate against `references/design-red-flags.md`. Assume the next contributor sees only the files they opened and copies the nearest example. Prefer the shape where a change that looks right in one file is right everywhere.

Compare on interface depth: more hidden behind a smaller surface wins.

## 3. Decide

By default, go on to implement with the chosen sketch. Stop for sign-off only when the user asked for a checkpoint. Reversible work keeps moving (`../mode/pillars/keep-moving.md`).

For adversarial pressure on the sketch before building, run `/tana:stress-review` on it.

If the user pushes back on the shape, treat that as new evidence. Go back to step 1.

## 4. Implement against the sketch

Replace the stubs with logic. The sketch is the contract. When a function needs something the sketch lacked, say which it is: the sketch was wrong, a requirement was missed, or you are reaching too far. Do not absorb it quietly.

Commit the sketch on its own if the diff is large. Planned breakage while stubs fill in is fine.

## 5. Scrap it when the shape is wrong

Look for a pattern, not one snag:

- the same workaround in unrelated places;
- special-case branches for many unrelated edge cases;
- types that only compile with `any`, casts, or fields that are always set;
- a sudden need for a lock when the sketch said state was not shared;
- callers who must know the internals to use it;
- two or more deviations of the same kind.

A few awkward cases do not condemn a design. Complex data is not a complex design.

To scrap: re-explain what was built, redesign as if the new facts were known on day one, make the new sketch smaller than the old one (`../mode/pillars/light-tackle.md`), and return to step 2.

## Output

- The sketch: one file, or a module map plus types.
- A one-page rationale shaped by `references/rationale-template.md`.
