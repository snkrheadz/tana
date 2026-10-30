# Confidence tiers

Put every claim in one tier. The tier decides where it goes and how it is worded.

| Tier | What backs it | Wording |
| :- | :- | :- |
| Direct | Someone wrote the reason: a PR body, ticket, comment, doc, or message | "This exists because X" with the citation next to it |
| Supported | Several indirect pieces point the same way, none says it | "The evidence points to X:" then list the pieces |
| Inferred | Your reading of the context, with no source for it | "Given A and B, C seems likely, because D" |
| Speculative | A thin guess that other causes fit equally | "One possibility is X; nothing confirms it" |
| Unknown | You looked and found nothing | "Searched A, B, C for these terms; no rationale found" |

Rules:

- Words like "because", "was designed to", "fixes", "the team decided" need a citation
  beside them. If you have none, hedge: "appears to", "is consistent with".
- Skip "obviously", "clearly", "just", and "I think".
- Do not invent a clean rationale for messy history. Copy-paste can look like intent.
- When two sources disagree (ticket says compliance, PR says cleanup), show both. They may
  both be true. Let the reader judge.
- A missing answer is a result. Say who might know: the author, the owner, the on-call.
- Before sending, check each claim: cited or moved down a tier, wording matches its tier,
  and a "Not known" section exists. If it has no gaps, look again.
