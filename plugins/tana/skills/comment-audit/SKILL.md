---
name: comment-audit
description: Audit code comments in a diff and delete the ones that narrate, apologize, or hide a workaround, then fix what they were hiding. Use for /tana:comment-audit or "clean up comments".
disable-model-invocation: true
---

# Comment audit

A comment that explains surprising code in your own repo is a bug report. Fix the
code so the comment is not needed. Keep a comment only when it is about something you
cannot change.

## Scope

Use the files or diff the user gave. Otherwise use the diff against `main`, working
tree included.

## Steps

1. Spawn the `comment-auditor` agent with the scope. Do not restate its rules.
2. Read its report and the diff. Reject any edit that touches application code, leaves
   the scope, deletes a comment under an exception, or gives a wrong reason. Restore
   a deleted comment only with the exact exception and proof that it holds today.
3. Check for lint and type suppressions it missed. Suppressions that hide a correctness
   or safety rule are findings.
4. For a vague warning such as "do not remove", read the code it points at. Find out
   whether the claim is true on a live path. If you cannot show it, delete the comment.
5. Fix the trivial findings: delete dead code, drop an unused parameter, call the real
   API. For anything that needs a new shape, use `/tana:sketch-design` once for the
   whole set, then implement.
6. Make the smallest fix for the root cause inside the scope. If the cause is outside,
   fix what is in scope and list the rest as open. Follow `../mode/pillars/light-tackle.md`.
7. A comment that says "do not change this" about something outside your control stays.
   Offer the cheapest check that would enforce it (a type, a test, a lint). With
   approval, add the check, then delete the comment.
8. If the auditor's output is bad twice, stop and report it.

## Report

Deleted count, restored comments, fixes made, checks offered or added, constraints
still unenforced, and other open work.
