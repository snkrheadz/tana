---
name: create-verify-skill
description: Write a project-local skill that launches the app and drives it like a user, plus a feature map. Use for /tana:create-verify-skill, or "make a verify skill for this repo".
disable-model-invocation: true
---

# Create a verify skill

Claude Code's built-in `/run` skill starts an app once. This skill leaves something durable: a skill in the repo, at `.claude/skills/verify-<app>/`, that a later session can read cold and use to prove a change works. The reasoning on checks is in `../mode/pillars/sounding.md`.

## 1. Read the repo first

Ask the user only what the code cannot tell you.

- **Surface:** web UI, CLI, TUI, API, desktop, library? Pick the main one.
- **Start:** the repo's own dev command (package scripts, Makefile, README). Ports, env vars, seed data, login.
- **Drive:** reuse what exists: Playwright specs, expect scripts, curl-able routes. Otherwise use the browser tools for web, `tmux` for TUIs, `curl` for services.
- **Evidence:** screenshots, transcripts, response bodies, logs, exit codes, stored rows.
- **Isolation:** can two copies run at once? If not, the skill must refuse to drive an instance it did not start.

If the checkout does not build, fix that or report it before writing anything.

## 2. Write the skill

`SKILL.md` needs frontmatter with `name: verify-<app>` and a description naming the app and when to use it. Then these sections, filled with this repo's real commands and handles, no placeholders:

- **Launch:** command, ready signal, teardown. Reach a usable state from an empty data dir. A port that answers is not yet ready.
- **Doctor:** one read-only check: right build, right port, process is ours.
- **Drive:** recipes using stable handles (roles, labels, route paths, prompt text), not coordinates.
- **Evidence:** what to save and where. Use the real user path. Capture the action and the result. Check side effects (files, rows) next to what shows on screen.
- **Cleanup:** stop only what the run started, never by process name. Keep the evidence.
- **Helpers:** any script is executable and its call is shown in the skill.

## 3. Seed the feature map

Add `features/README.md` and one file per user-facing feature, three to five to start. See `references/feature-map-example.md` for the shape. If a journey lacks a precondition, record it under Gotchas. Do not soften the journey.

## 4. Run it once

Follow the new skill end to end: launch, doctor, drive one feature, save evidence, clean up. Check the evidence is still there. Clean up after every failed try. A skill never run is a draft.

If you proved it somewhere else than the target, list the setup steps that place did for you.

## 5. Hand off

Point to `/tana:maintain-verify-skill` for upkeep.
