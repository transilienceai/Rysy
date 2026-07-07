# craft/trends/

Vendy's rolling market context. The macro narratives currently shaping the world her prospects live in.

## What lives here

- `current.md` — the active trends file, refreshed by the `refresh-trends` skill
- `archive/` — past versions, archived on each refresh
- `runs/` — the run reports from each `refresh-trends` invocation, including which sources were consulted and what was filtered out

## How `current.md` is structured

Frontmatter declares the timestamp, sources consulted, number of trends surviving the filter, and number of candidate topics dropped (with reasons summarized).

Body has one section per surviving trend, each with:
- A one-line title
- A 4-5 sentence summary of what it is and why it is hot now
- A list of the strongest evidence pieces (with links)
- The personas it most affects
- A *conversational hook* — one suggested phrasing for how Vendy might mention this in an email if it matched the prospect's context

## How `current.md` is consulted

The `session-start-load-self.sh` hook injects `current.md` into Vendy's session context at the start of every session, so she always begins with awareness of the macro environment. When drafting, she checks whether any of the active trends connect to the prospect's situation; if yes, the trend may be the trigger event or the body's anchor.

## When to refresh

Vendy invokes `refresh-trends` autonomously when `current.md` is older than 14 days (configurable). She also responds to a manual `/refresh-trends` invocation from the human.

The *signal/noise filter* the skill applies is documented in detail at `.claude/skills/refresh-trends/SKILL.md`. The short version: a topic survives only if it appears across at least 3 independent sources, has behavioral signal (not just opinion), has at least 2 weeks of time depth, and has at least one practitioner voice (not just analysts and vendors).

## Initial state

`current.md` is initially a placeholder. Run `refresh-trends` (or `/refresh-trends`) before the first campaign to populate it with current macro context.
