# Rationale template

One page. Replace each hint with real content.

1. **Problem.** What you are building and what makes the shape unclear. List the constraints found while grounding: types to match, callers you cannot break, invariants.
2. **Usage.** Written first. The quickstart and two or three call sites in the caller's own code. The sketch below must match it.
3. **Shape.** Core data structures, then how data moves through the signatures. Say which invariants live in types, where input is validated, and what the design refuses to do. State what the public surface hides and why it is no larger.
4. **Choice record.** Which candidate was the base, what was taken from the others, what was dropped. Leave out if there was only one.
5. **Tradeoffs.** One line each: "we accept X to get Y." Include anything a reader might mistake for a slip.
6. **Alternatives.** At least one real alternative shape, with the reason it lost, judged on what it exposes versus hides. If the constraints left one shape, say so.
7. **Open questions.** Phrase as questions the user can answer.
8. **Next step.** The first thing to build, in one sentence.
