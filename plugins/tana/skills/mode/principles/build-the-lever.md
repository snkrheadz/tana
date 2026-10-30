# Build the lever
Open when: the work is more than a couple of obvious edits, or someone must be able to re-check what you did.

Write the small tool that does the job or proves it: a codemod, a generator, a query over dumped data, a rerunnable check. A script behaves the same each run, and a reviewer can run it instead of trusting you.

1. Do one unit by hand to learn the recipe.
2. Turn the recipe into a script, rerun it on that unit, and diff against your hand result.
3. Make it safe to run twice, then run it over everything yourself. A script that covers every unit beats spawning agents to hand-edit (see `../pillars/one-rod.md`).
4. If agents must do judgment work, put the recipe, the check, and the off-limits list in one file outside their write scope.

The bar is "not trivial", not "repeated". Keep it as small as the job needs, never a framework. Commit it if the work outlives the session. If you cite this and the diff holds no script, you did not apply it.
