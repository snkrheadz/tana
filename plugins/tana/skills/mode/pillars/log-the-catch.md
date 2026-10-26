# Log the catch

An angler who writes down depth, bait, and time catches more next season. A lesson
that lives only in this conversation is lost when the conversation ends. A lesson
written as prose is paid for in tokens on every future run and still gets ignored
sometimes. Put each lesson where it is enforced most cheaply.

## Where a lesson goes, strongest first

| Home | Use when |
| :- | :- |
| A test | The lesson is about behavior the code must keep |
| A type or a lint rule | The mistake has a recognizable shape in the code |
| A hook in `settings.json` | The rule is about what the agent may do (a command, a file, an order of steps) and must never be skipped |
| A script or `make` target | The right procedure has several steps that are easy to get wrong |
| A skill | The procedure needs judgment and is used often enough to be worth loading |
| `CLAUDE.md` | None of the above can carry it. Write the rule and the reason behind it |
| Auto-memory | A personal preference of this user, not a rule of the codebase |

When you move a rule into a stronger home, delete the prose version in the same
change.

## When the user corrects you

1. Fix the thing.
2. Ask whether the same mistake could happen again. If yes, put the lesson in the
   strongest home that fits, with the pattern and the reason.
3. If the project keeps a lessons file (for example `tasks/lessons.md`), add a short
   entry there too.

## Measure changes to prompts, skills, and config

A change to a prompt, a skill, a hook, or `CLAUDE.md` is a change to behavior, and
behavior is noisy. Treat it like an experiment.

1. **Have cases first.** A handful of realistic tasks is enough to start, each with a
   check on the outcome and, where it matters, a check on the steps taken.
2. **Change one thing.** Two changes at once tell you nothing about either.
3. **Run each case more than once,** with and without the change. A regression can
   show up in one run of two.
4. **Read the cases that flipped,** not only the average. A better total can hide a
   case that broke.
5. **Keep what holds up.** If the change does not move the result, remove it. Its cost
   in context is real even when its benefit is not.

`claude plugin eval` runs cases with and without a plugin. For a single rule, a
headless run with `--setting-sources` and `--append-system-prompt-file` compares the
rule against its absence without touching the live config.

Rules written for an older model often stop paying off with a newer one. When the
model changes, retest the rules that were added to work around its weaknesses.

## Long runs leave a trail

For work the user will review later (an overnight run, a long migration), keep a
short decision log as you go: what you chose, what you rejected, and why. Keep it in
the scratchpad, and commit it only when the stakes call for an audit trail.
