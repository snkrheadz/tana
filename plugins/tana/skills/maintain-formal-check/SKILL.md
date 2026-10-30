---
name: maintain-formal-check
description: Bring a project's formal check back in line with the code after changes, then say whether each failure is drift in the model or a bug in the code. Use for /tana:maintain-formal-check, or "is the model still true to the code".
disable-model-invocation: true
---

# Maintain a formal check

A check proves something about what it describes. If the code moved on and the model did not, a green run is a false proof. This pass catches changes that skipped the check skill. Pair it with `/tana:create-formal-check`.

## Outcome per check

- **in sync:** nothing relevant changed, it passes.
- **updated:** code changed, model now matches, it passes.
- **bug:** model matches current code and the property fails. This is a finding.
- **blocked:** could not update or run. Say why.

## Scope

Edit only models, harnesses, property files, and the check skill. Never edit product code unless asked. Never weaken a property to get green.

## Steps

1. **Find the checks.** Look for project skills that run a model checker, prover, or verifier. For each, note property, covered code, bounds, command, sync commit. None found: stop and suggest `/tana:create-formal-check`. No sync commit recorded: use the last commit touching the check files, and say so.
2. **Run as is.** Record the result. A pass only means the old description still holds.
3. **Read the changes.** `git diff <sync>..HEAD` on covered files, plus the log messages. Follow moved, renamed, or split functions, and new code that writes the guarded state. Sort each change:
   - no effect on the model (check against the model, not the commit message);
   - model no longer matches (a step split, a branch added, a new path in);
   - promise changed on purpose (cite the doc, test, or changelog);
   - promise maybe broken (a failure now is a bug candidate).
4. **Update from the code.** Write model changes from the code before rerunning. Change a property only for an intended promise change, and record old wording, new wording, evidence. Keep bounds unless they became wrong; report any cut.
5. **Rerun and judge.**
   - Pass: break the new code the way the property guards against and confirm the check fails, then undo.
   - Fail: replay the counterexample on the real code. A step that cannot happen means the model is wrong, so fix it. All steps possible means a bug. Name the introducing commit, give the steps in the code's words, one sentence of harm.
6. **Update the check skill.** Covered code, commands, bounds, assumptions, sync commit (the commit you checked; leave it for blocked checks). Run the check skill once as a newcomer would.

## Report

Per check: outcome and commits read; what changed and why; rerun result and the break you used; bugs in plain words; gaps in coverage. Say which failures were drift and which were bugs. If a check passed before and fails after your update, the old pass was on a stale model. Keep model updates in their own commit, apart from any product fix.
