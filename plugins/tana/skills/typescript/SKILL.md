---
name: typescript
description: TypeScript rules for types, narrowing, validation, and tests. Applies when reading or editing .ts or .tsx files.
---

# TypeScript

Make illegal states impossible to build, and check data once where it enters. Examples
for each row are in `references/patterns.md`.

| Rule | In short |
| :- | :- |
| Tagged unions | Model variants with a literal `kind` field. No object with optional fields that can contradict each other. |
| Branded types | Brand ids and units with `& { readonly __brand: "X" }`. Create them in one parsing function with a type guard, never with `as`. |
| Build legal values | Make the type unable to hold the bad value: `[T, ...T[]]` for non-empty, start plus length for a range. Do not rely on a runtime check at each caller. |
| Loosest total type | Keep `T[]` while every operation works on empty input. Tighten only where code needs `!`, a cast, or an impossible throw. |
| `unknown`, not `any` | Input from outside is `unknown` until validated. |
| Schema first | Before writing a guard by hand, use the repo's schema library and infer the type from it. |
| No `as` | A cast skips the compiler. Cast only after validation, and prefer `satisfies`. |
| Narrowing order | Switch on tag, then `in`, then `typeof` or `instanceof`, then a custom guard, and `as` last. |
| Honest guards | A guard must check what its name claims. A guard that lies is worse than a cast. |
| Exhaustive switches | End with `const _never: never = x;` so a new variant fails the build. |
| Parse at the edge | Turn raw input into a named domain type once. Inside, trust the types. |
| Derive types | Use `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, `typeof` before writing a new interface. |
| Options object | Pass an object once a function has several arguments of the same type. Not in hot loops. |
| Real tests | Run the real thing where you can. Mock only what cannot run locally. |
| Logging | Use the project's structured logger with ids. No `console.log` in shipped code. |

Follow the repo's existing conventions where they differ from this table, and check with
`tsc` after the change. See `../mode/pillars/light-tackle.md` before refactoring types
that already work.
