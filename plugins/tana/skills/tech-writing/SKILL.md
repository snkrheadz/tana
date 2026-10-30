---
name: tech-writing
description: Write or review docs, READMEs, RFCs, PR descriptions, and commit messages so a tired engineer gets them on one read. Use for /tana:tech-writing or "tighten these docs".
disable-model-invocation: true
---

# Tech writing

Four layers apply: pick one document type, write to the reader, make each statement
stand alone, and remove double meanings. Three rules sit over them.

1. Delete any word that does no work.
2. Use the short word. "Use", not "utilize".
3. If a rule makes the sentence worse, fix it another way. A sentence that obeys every
   rule and still sounds robotic has failed.

Use the real names from the codebase: the symbol, flag, file, or command. Do not invent
terms. Run `/tana:cut-ai-tells` on the result.

## Pick one type per document

Ask two questions. Does it help someone act or understand? Does the reader want to
learn or to get work done?

| Reader needs | Type | Rules |
| :- | :- | :- |
| To learn by doing | Tutorial | Say what they will build. Every step shows a result. Say what they should see. |
| To finish a task | How-to | Steps only. Name it by the task. Link out for background. |
| To look something up | Reference | Facts, no opinion. Mirror the structure of the thing. Generate from code if you can. |
| To understand why | Explanation | One topic. Give context, trade-offs, and your view. |

Do not mix types. Split and link.

## Sentences

- Address the reader as "you", in the present tense.
- Name the actor. "The compiler checks the types", not "types are checked".
- Imperative for steps. Put the condition first: "To delete the file, run `rm`".
- Common case first, exceptions after.
- Never write "simply", "just", "easy", or "please" in a procedure.
- Link text says where it goes. Never "click here".
- Headings state the point, in sentence case. Numbered lists for sequences, bullets for
  the rest. Keep list items parallel.

## One reading only

- One instruction per sentence. Split instructions past about 20 words and other
  sentences past about 25.
- Put a warning before the step it guards.
- Keep "the" and "a". Keep "that" where it shows structure.
- Use one word per action and one name per thing, throughout.
- Place "only" and "not" next to the word they modify.
- Break long noun chains: "the script that checks the import budget".
- Make every "it", "this", and "they" point at one noun. Repeat the noun if unsure.
- No slashes ("a/b"), no "(s)", no "etc.", no idioms, no semicolons.

## Rhythm

Vary sentence length: short for the point, longer for a fact with its condition. Take a
position in explanation. Be concrete: "a column rename fails the build", not "changes may
cause issues".

## Commits and PRs

A PR body is a briefing readable in a minute. State what changed, why, and how it was
checked. Link logs and metric tables. Make every count true at the commit that lands it.

## Example

Before: "Configuration of the import budget script is performed via budget.json. It is
important to note that --write should only be used when lowering."

After: "`budget.mjs` reads `budget.json` and counts the files that import protos. If the
count exceeds the budget, CI fails. Run `budget.mjs --write` only to lower the budget."
