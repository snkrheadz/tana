# Layout of the explanation

Write for an engineer who knows the language but not this area. Use real names
("`OrderService` calls `PriceClient.fetch()`"), not "the service delegates to the client".

1. **Overview.** One or two short paragraphs: what it is, what it is for. A reader should
   be able to stop here.
2. **Key concepts.** The few types or ideas needed to follow the rest. One line each.
3. **How it works.** The longest part. Follow one request or event from trigger to result.
   Name the files and functions. Use a Mermaid or ASCII diagram only when several parts pass
   data between them and prose would blur it. Skip code blocks unless one snippet carries
   the point.
4. **Where things live.** A short map of the directories and files someone would open first.
5. **Gotchas.** Behavior that surprises, and traps. Leave the section out if there are none.

When something is complicated, say why it is. When it is simple, do not pad it. List open
questions from the subagents instead of hiding them.
