---
name: create-formal-check
description: Find the code where a bug costs most and tests reach least, verify one property of it with a model checker or verifier, and leave a project-local check skill. Use for /tana:create-formal-check, "model-check this race", or "prove this invariant".
disable-model-invocation: true
---

# Create a formal check

A test covers the cases someone wrote. A model checker covers every ordering within a stated size. Use it where order, retries, or state decide whether users get hurt. The reasoning on checks is in `../mode/pillars/sounding.md`.

## 1. Choose the target from the code

Start with the user's area or bug if they named one. Otherwise find a promise the code makes, where breaking it harms users and tests rarely hit the breaking case: concurrency, retries, locks, state machines, parsers, unsafe code. Take the strongest target, not the easiest.

## 2. Let the question pick the tool

- Can events happen in a bad order? Model the design in TLA+ and run TLC. This works for any language.
- Does the code itself hold for all inputs (overflow, memory safety, a data-structure rule)? Use a verifier that reads the code, if one exists for the language.
- No verifier for the language? Say so, and test the real code with generated inputs instead of modeling a function by hand.
- Must it hold at every size? That may need a proof assistant.

Prefer tools the team can install. Tell the user why you chose it.

## 3. What a good check has

- **True to the code:** each part of the model points to code a reviewer can open. One indivisible step in the code is one step in the model.
- **Can fail:** break the guarded code on purpose (drop a check, swap two steps) and watch the check fail. A check never seen failing proves nothing.
- **Findings stay findings:** if the current code breaks the property, report the counterexample in the code's words. Do not weaken the property or edit product code.
- **Honest scope:** state what was checked, the bounds, the assumptions, and what is left out.
- **Plain words:** one sentence for the property, one for the harm.
- **Cheap to rerun:** one command, pinned tool version, short run.
- **Tracked:** record the files and functions covered and the commit where you last confirmed the model matches them.

## 4. Write the check skill

Project-local, with frontmatter naming the area. A reader with no context must be able to: tell if a change touches covered code, run the check, tell a real bug from a modeling slip, and update the model for an intended change. Put the coverage list and sync commit in it, and say to advance the commit only after confirming the model matches the new code. For TLA+ checks, point to `../statechart/SKILL.md` for reading results; do not copy its commands.

## 5. Prove it

Follow the new skill once on a scratch edit that breaks the property in the real code. It must catch it. Undo the edit and confirm the check is back to its starting result. If it misses, fix the check, not the edit.

## 6. Hand off

Report: what you checked, tool and reason, bounds, findings in plain words, how to run, what is not covered. Mention `/tana:maintain-formal-check` for later drift.
