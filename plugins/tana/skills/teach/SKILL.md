---
name: teach
description: Explain a piece of work so the person really understands it: what it is, how it works, and why it is that way. Use for /tana:teach or "teach me this", "help me understand X", "explain this change to me".
disable-model-invocation: true
---

# Teach

The goal is that the person understands. You do not change anything. This builds on
`/tana:explain-code` (how it works) and `/tana:trace-why` (why it is that way). Read their
`SKILL.md` files and follow them, or invoke them with the `Skill` tool.

1. **Choose what they should leave knowing.** Read their reason for asking from the
   conversation: about to change it, reviewing it, debugging it, new to it. Do not quiz
   them. Skip what they plainly know and spend the words where the question is.
2. **Gather, do not redo.** Open the code yourself to get oriented. Run explain-code for
   the mechanism and trace-why for the reasons. Use one if it is a small change, both for
   a subsystem. Keep trace-why narrow by default: git, PRs, and one or two other sources.
   Widen it only when the reasons are the point. Keep its confidence wording as is; a
   hedge there is a finding.
3. **Open with a plain definition.** Say what the thing is in general terms, with its
   common name. Then tie it to this case ("here we use it to...") and build up: how it
   works, then the deeper reasons, then edge cases. For each part, give the problem it
   solves and the mechanism. Walking through what happens when a user does something is
   better than listing functions.
4. **Draw in steps.** For three or more moving parts, draw a short series. Each diagram
   redraws the last and adds one part. One finished diagram with everything is reference,
   not teaching. Open the diff or run the code when that lands faster than words.
5. **Stay in conversation.** Offer to go deeper and follow their lead. No quizzes, no
   "say it back", no labels like "the key insight" or "the tricky part". Just say it. If
   no one is live, deliver it cleanly and put the offer at the end.

Write in plain spoken English, using `../cut-ai-tells/SKILL.md` as the filter. Name the
real mechanism, not a metaphor or a preview. One name per concept, kept all the way
through. Short sentences, few commas.

Reply with the explanation itself, not a report of what you did. Lead with the main
point. End with the threads worth following up through explain-code or trace-why.
