# craft/patterns/

Patterns are observations promoted to durable belief, with explicit evidence.

## Promotion criteria

A note is promotable to a pattern when:

1. **At least three corroborating notes** exist in `craft/notes/` that point at the same belief
2. **The corroborating notes span at least two distinct campaigns** (avoiding pattern-promotion based on a single context)
3. **The promoting note has an explicit evidence section** that references the source notes by ID
4. **No unrebutted counter-evidence** exists — if a note explicitly contradicts the pattern, it is acknowledged in the pattern file's *Anti-cases* section, with a reasoning note

The `promote-pattern` skill enforces these mechanically. Patterns that do not meet the criteria cannot be promoted.

## Format

Filename: `{slug}.md`

```yaml
---
promoted: <date>
confidence: tentative | provisional | established
evidence_notes: [<list of note IDs>]
campaigns_covered: [<list of campaign IDs>]
last_reaffirmed: <date>
last_challenged: <date or null>
status: active | retired
---
```

Body:

```markdown
# {Pattern title}

## The belief

[2-3 sentences stating the pattern explicitly. Specific.]

## Evidence

- {note-id-1}: [one-line summary] — [link]
- {note-id-2}: [one-line summary] — [link]
- {note-id-3}: [one-line summary] — [link]

## Implications

[How Rysy uses this pattern when drafting. Concrete moves, not abstract principles.]

## Re-test

[How she will know if this stops being true. The signals that would prompt re-evaluation.]

## Anti-cases

[Notes that did not fit the pattern, with brief reasoning for why the exception does not invalidate the pattern.]
```

## Confidence levels

- **`tentative`** — minimum criteria met (3+ corroborating notes, 2+ campaigns); the pattern is provisionally believed but should be re-tested. Default at promotion time.
- **`provisional`** — pattern has been re-affirmed by additional evidence after promotion; held with more weight.
- **`established`** — pattern has been re-affirmed across many campaigns over time; held strongly. The pattern's anti-cases have been considered and explicitly fail to invalidate it.

Confidence escalates only with continued evidence. It can also descend — if counter-evidence accumulates, a previously established pattern can drop to provisional or be retired.

## Pattern retirement

A pattern is retired when:
- New evidence contradicts the pattern in 3+ recent notes
- The conditions that produced the pattern have changed (e.g., a market shift, a regulation, a platform change)
- The pattern has not been reaffirmed in 6+ months and recent practice no longer follows it

Retirement is *not* deletion. The pattern file remains with `status: retired` and an explanation of why. Past evidence is preserved.

## Why patterns are autonomous

Rysy promotes patterns without human approval. This is deliberate: the smriti layer must grow freely, by evidence, or the learning loop dies. Human approval is reserved for changes to `self/` (the constitution).

The safeguard against rotten patterns is not human approval — it is the promotion criteria themselves (3 notes, 2 campaigns, evidence section), the anti-cases requirement, and the periodic introspection cycle that re-evaluates patterns against current behavior.

## INDEX.md

`craft/patterns/INDEX.md` is rebuilt by the `reindex-memory` skill. It maintains a list of patterns with date, confidence, status, and last-reaffirmed timestamp.
