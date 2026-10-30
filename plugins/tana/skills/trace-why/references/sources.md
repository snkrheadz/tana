# Sources to search

Use whatever is connected. Tool names differ by server, so read each tool's description
and match by purpose. Each investigator searches one kind, writes nothing, and returns
quotes with links plus a list of what it searched.

## Source control (always available)

- `git blame -L a,b file` for the last touch of each line, then `git log --follow -p -- file`
  for history through renames.
- Pickaxe: `git log -S'literal' --oneline` and `git log -G'regex'` find when a string or
  pattern appeared or vanished.
- Commit bodies, PR descriptions, review comments (`gh pr view <n> --comments`,
  `gh api repos/{owner}/{repo}/pulls/<n>/comments`), linked issues, tests added with the change.
- Revert-then-reapply pairs and "hotfix" or "temporary" in messages are strong signals.
  Check whether the stated temporary condition still holds.

## Issue tracker

Search by ticket ID from the anchor, then by feature keywords, labels, and the date range
around the commit. Read the description, comments, and linked incidents. Best at the
product or customer reason behind the work.

## Long-form docs and wikis

Search for design docs, RFCs, ADRs, and meeting notes by the feature name and the
function or flag name. Check the doc's date against the commit date. Docs often describe a
plan that later changed, so say which.

## Team chat

Search channel history near the commit date for the symbol, ticket ID, and PR number.
Read whole threads, not single hits. Most useful when the paper trail is thin. Treat
chat as opinion until a decision is stated.

## Incident notes and postmortems

If the target is defensive (null guards, retries, timeouts, rate limits, flags, memory
limits), search incident channels, postmortem docs, and tickets labeled with incident or
severity terms near the date the code appeared.

## Observability and error trackers

Look for the signal the code reacts to: timeouts, retry rates, a specific exception, a
latency or error-rate change before the commit. Pull dates and counts, not impressions.
For a threshold, check whether the data supports the number or the number was round.
Treat what is live now as current state, not proof of what motivated the change then.

## Data warehouse and analytics

For flag-gated code, experiments, migrations, and "where does this number come from",
query read-only: when the flag rolled out, the metric it moved, the cohort size. Record
the query so the reader can rerun it, and see `../../mode/pillars/sounding.md` on
reading a number with its spread.
