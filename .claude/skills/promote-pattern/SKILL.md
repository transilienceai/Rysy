---
name: promote-pattern
description: Scan recent craft notes for clusters that meet promotion criteria, and promote them to craft/patterns/ with explicit evidence pointers. Use when the user invokes /promote-patterns, when session-end-reflect surfaces a pattern-promotion suggestion (notes have accumulated above threshold), or after a campaign that produced notable observations across multiple leads. Do NOT invoke after every campaign — premature promotion produces unreliable patterns.
---

# promote-pattern

The mechanism by which Vendy's observations become beliefs.

## When to invoke

- Manually via `/promote-patterns`
- Auto-suggested by `session-end-reflect.sh` when ≥5 new notes accumulated since last reindex
- After a campaign that produced ≥3 notable observations across multiple leads

## Promotion criteria

A note cluster is promotable to a pattern only when ALL of these hold:

1. **At least 3 corroborating notes** point at the same belief
2. **Notes span at least 2 distinct campaigns** (avoiding patterns based on a single context)
3. **No unrebutted counter-evidence** in the broader notes set
4. **The pattern can be stated explicitly** in 2-3 sentences

These criteria are mechanical — the skill enforces them. The clustering and convergence-judgment algorithm is in `references/clustering.md`.

## Happy path

Read recent notes (last 30 days). Cluster by tag overlap. For each cluster, judge convergence. Apply the four criteria. Draft pattern files for surviving clusters. Update notes index and patterns index. Surface results.

## Output

For each promoted cluster, a pattern file at `craft/patterns/{slug}.md` per the schema in `craft/patterns/README.md`. Initial confidence is always `tentative`.

## What this skill does NOT do

- Modify `self/character.md` (use `apply-approved-diff` for that)
- Delete or merge existing patterns (pattern lifecycle is a separate workflow)
- Promote based on counter-evidence alone (the bar is positive evidence)
- Skip the *Anti-cases* section (write "none observed yet" rather than skipping)

## Detailed workflow

The full clustering algorithm, the convergence-judgment criteria, the exact promotion logic, and the pattern file template are in `references/clustering.md` and `references/pattern-template.md`.
