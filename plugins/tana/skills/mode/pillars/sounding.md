# Sound the depth

Before the first edit, answer one question: **what will I observe that proves this
worked?** Then make sure you can observe it now, while it still shows the old behavior.
A check you have only seen pass cannot tell you it measures the right thing.

## Find the check, cheapest first

1. **The repository already has it.** A verify script named in `CLAUDE.md`, a test that
   covers the code path, a `make` or `npm run` target. Run the narrowest one that
   touches the change.
2. **Run the real thing.** Start the server, the CLI, or the app and look at what it
   does. In Claude Code:
   - a server or watcher: start it with `run_in_background`, wait for its ready line
     with an `until` loop, then hit it with `curl` or a client;
   - a web UI: drive it through the browser tools, or the built-in `/run` skill;
   - a CLI: run it with the inputs the user will give it and read the output.
3. **Script the comparison.** When no ready-made check exists, write a short script
   that prints the value you care about, before and after. Keep it in the scratchpad.
   Commit it only when the repository already keeps tests of that kind.
4. **Change to a prompt, skill, hook, or `CLAUDE.md`.** The artifact is the agent's
   behavior. Run it headless (`claude -p ... --output-format stream-json --verbose`) or with
   `claude plugin eval`, and read what the agent did, not what it said it did.

## Take the reading before the change

- **Bug:** the check fails, and fails for the reason in the report. If you cannot make
  it fail, you have not found the bug yet. Keep looking before you edit.
- **Feature:** the check shows the behavior is absent, or shows the old behavior.
- **Refactor:** the check passes before and must still pass after, with the same
  output.

## Proxies that do not count

Exit code 0. "It compiles." A file's modification time. A test suite that passes but
never runs the changed lines. A subagent's report that it finished. Each of these can
be true while the work is wrong. Read the real value: the response body, the rendered
page, the row in the database, the diff on disk.

When a check disagrees with what you expected, suspect the check first. Confirm it
can see the thing (right process, right port, right file, not a cached copy) before
you change the code to satisfy it.

## Numbers

A measured number (latency, a speedup, a pass rate, a token count) is not evidence
until you know its spread. Run it more than once under the same conditions. Say what
limits it and what else could have moved it. An agent eval that ran each case once
can hide a regression that shows up one run in two.

## When you cannot build the check

Say so in the reply, plainly, with the reason. Give the user the smallest check they
can run themselves, as a command they can paste. Do not describe unverified work as
done.

Long or unattended work (a loop, an overnight run) needs a check that stops the run
when it fails. Without one, do not start the run. Build the check first.
