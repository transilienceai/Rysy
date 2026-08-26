---
name: refresh-trends
description: Refresh craft/trends/current.md by pulling current security and engineering narratives from configured sources, filtering noise from real trends, and writing a fresh trends file. Use when the user invokes /refresh-trends, when run-campaign detects the trends file is older than 14 days, or when Rysy notices the trends file is stale relative to a major recent event.
---

# refresh-trends

Updates Rysy's rolling market context. Goes out, reads, filters, synthesizes, archives, writes.

## When to invoke

- Manually via `/refresh-trends`
- Autonomously when `craft/trends/current.md` is older than 14 days OR has `status: placeholder`
- When a major recent event (a regulation passing, a public breach, a category-shifting talk) has plausibly outdated the existing trends file

## Sources

The skill reads `sources.yaml` (in this skill's directory) for the configured source list. Sources are organized by type — newsletters, Reddit, Hacker News, GitHub trending, conferences, CVE feeds, SEC filings, practitioner voices. The list is editable; add or remove sources without modifying skill logic.

## Happy path

Five phases — collection, topic clustering, filter, synthesis, write & archive. Phases 1-2 are mechanical. Phase 3 (the noise/trend filter) is the load-bearing judgment step.

## The filter — what makes a trend survive

A topic survives only if it meets ALL of these:
1. **Independent sources** — appears across at least 3 unaffiliated sources
2. **Behavioral signal** — evidence of *behavior* (hiring, building, presenting, complying), not just opinion
3. **Time depth** — has been heating for at least 2 weeks
4. **Practitioner voice** — at least one practitioner (CISO/CTO/VP-level operator) has engaged substantively

Topics that fail any of these are dropped, with the failure reason logged. The full filter rationale and edge cases are in `references/filter-criteria.md`.

## Detailed workflow

The full five-phase workflow with output schemas is in `references/workflow.md`. The shape of the resulting `current.md` and the run report is in `references/output-format.md`.

## When the result is "no real change"

If the filter eliminates almost everything and the surviving trends are nearly identical to the previous version, write the new file with timestamp updated but say so honestly: *"This refresh found minimal change from the previous version. The macro environment is stable."* Do not invent change to justify the refresh's existence.
