# Output format — current.md and run reports

## current.md

```yaml
---
timestamp: <ISO-8601>
sources_consulted: [<list of source names>]
trends_surviving_filter: <integer>
candidates_dropped: <integer>
status: active
next_refresh_due: <date 14 days out>
---
```

Body:

```markdown
# Current trends

## {Trend 1 title}

**What it is**: [4-5 sentences]

**Why it's hot now**: [the trigger that made it surface]

**Evidence**:
- [link 1 with one-line context]
- [link 2 with one-line context]
- [link 3 with one-line context]

**Personas affected**: [comma-separated tags]

**Conversational hook**: *[one suggested phrasing]*

## {Trend 2 title}

[same structure]
```

## Run report

`craft/trends/runs/{timestamp}.md` documents the audit:

```yaml
---
run_at: <ISO-8601>
sources_consulted: [<list>]
candidates_considered: <integer>
trends_surviving: <integer>
candidates_dropped: <integer>
---
```

Body:

```markdown
# Trends refresh run — {timestamp}

## Summary

[2-3 sentences on what changed since last refresh]

## Trends surviving filter

- {trend slug 1}
- {trend slug 2}
...

## Candidates dropped

| Topic | Failed criterion | Evidence |
|-------|-----------------|----------|
| {topic} | {one of 4} | {one-line} |
...

## Notable absence

[Any topics that were prominent in the previous current.md but are no longer surfacing — these are themselves signals]
```
