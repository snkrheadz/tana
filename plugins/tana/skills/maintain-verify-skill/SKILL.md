---
name: maintain-verify-skill
description: Audit a project's verify skill and feature map against the source and a live run, fixing drift in one small change. Use for /tana:maintain-verify-skill or "audit the verify skill".
disable-model-invocation: true
---

# Maintain a verify skill

Feature maps go stale as soon as the app changes. This is the upkeep pass for a skill made by `/tana:create-verify-skill`. Cover every feature file from source and drive each one live. Not every line needs proof.

## Pick an outcome and name it

- **clean:** every feature read and driven, nothing to fix. No branch.
- **changed:** one change with proven corrections.
- **blocked:** say what stopped you.

## Scope

Edit only the verify skill's own folder: `SKILL.md`, `features/`, its scripts. Never touch product code. If the map says something the app no longer does, decide: stale doc (fix the doc) or product regression (report it, leave the doc true to intent).

## Steps

1. **Find the target.** Look for `.claude/skills/verify-*/`. Several: ask which. None: stop and suggest `/tana:create-verify-skill`.
2. **Tidy the index.** Compare `features/README.md` to the files on disk. Fix missing, extra, or dead links.
3. **Read the source.** Spawn one `Explore` subagent per feature file, `model: "haiku"`, in one message so they run together (see `../mode/pillars/one-rod.md`). Each reads the code behind its feature and returns: summary, entry points, suspected drift with file and line, one live recipe. Subagents do not drive the app or edit.
4. **Reconcile.** Spot-check the cited drift. Look at recent commits for user-facing surfaces the map lacks, and require a real source path before adding one.
5. **Drive live.** Do this even if the source looks clean. You drive, serially, following the skill's own Launch section. Keep three habits: run doctor before the first drive and after any failed one; check that saved evidence still exists after each cleanup; clean up anything a failed drive left running. A feature you cannot reach is `unreachable` only with the prerequisite and the route you tried. Re-drive any harness fix before it ships.
6. **Sort findings.** Wrong description: fix the doc. Working behavior the harness cannot drive: fix the harness. Broken app behavior: report it, keep it out of the change.
7. **Ship or stop.** For changed, reread each edited file, then open one PR (`../mode/playbooks/opening-a-pr.md`). For clean or blocked, no PR; report coverage honestly.

Keep short run notes in the scratchpad. Do not commit them.
