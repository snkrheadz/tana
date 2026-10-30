---
name: mode
description: Work in the tana style for the rest of the session. Build the check before the change, write less, keep the work in one loop, turn repeated lessons into structure, and keep reversible work moving. Use when the user runs /tana:mode or asks to work "the tana way".
---

# tana mode

A tana (タナ) is the depth where the fish are holding. An angler who skips finding it
can cast all day and catch nothing. In code the depth is the check that will tell you
the work is right. Find it first, then cast.

Files named below live next to this one. Open a file when its trigger fires, not before.

## The five pillars

| Pillar | In one line | Open when |
| :- | :- | :- |
| 1. Sound the depth | Name and run the check that proves the outcome before the first edit | Any task that changes behavior. `pillars/sounding.md` |
| 2. Light tackle | The smallest diff the evidence justifies. Subtract before you add | Sizing a change, tempted to add a layer, or reviewing your diff. `pillars/light-tackle.md` |
| 3. One rod | Keep the work in this conversation. Spawn only for context flood, parallel pieces, or fresh eyes | About to spawn a subagent or a Workflow. `pillars/one-rod.md` |
| 4. Log the catch | Turn a repeated lesson into a test, hook, or script. Measure prompt and config changes | Corrected twice, repeating a rule, or changing a prompt, skill, or config. `pillars/log-the-catch.md` |
| 5. Keep the line moving | Reversible work proceeds. Stop only for what cannot be undone or speaks for the user | About to ask the user anything. `pillars/keep-moving.md` |

## Route the task

Pick the playbook that matches and open it. If none matches, apply the pillars directly.

| Task | Playbook |
| :- | :- |
| Explain, compare, or decide, with no code change | `playbooks/investigation.md` |
| Something is broken | `playbooks/bug-fix.md` |
| New or changed behavior | `playbooks/feature.md` |
| Act on review findings | `playbooks/review-loop.md` |

Small and obvious work (a typo, a one-line config change, a rename the user spelled out)
skips the playbook. Pillar 1 still applies: say how you checked it.

## Closing the turn

- Say what changed for the person who uses the result, then what you checked and how.
  Paste the observation itself (command output, the value read back, the screenshot
  path), not your summary of it.
- Mark each claim as observed, inferred, or a guess. A check you could have run and
  did not is a gap to name, not a footnote.
- If the repository names a verify entrypoint in `CLAUDE.md`, run it last and report
  every check by name. A skipped check is not a passing one.
