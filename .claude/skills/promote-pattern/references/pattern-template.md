# Pattern file template

Every promoted pattern follows this exact format.

## Filename

`craft/patterns/{slug}.md` — slug is derived from the central observation, kebab-case, ~3-6 words.

## Frontmatter

```yaml
---
promoted: <ISO-8601 date>
confidence: tentative          # always tentative at promotion time
evidence_notes: [<note IDs>]
campaigns_covered: [<campaign IDs>]
last_reaffirmed: <same as promoted at first>
last_challenged: null
status: active
---
```

## Body

```markdown
# {Pattern title}

## The belief

[2-3 sentences stating the pattern explicitly. Specific, declarative, defensible.]

## Evidence

- {note-id-1}: [one-line summary] — [link to note]
- {note-id-2}: [one-line summary] — [link to note]
- {note-id-3}: [one-line summary] — [link to note]

## Implications

[How Vendy uses this pattern when drafting. Concrete moves, not abstract principles.]

## Re-test

[How she will know if this stops being true. Specific signals or campaign types that would prompt re-evaluation.]

## Anti-cases

[Notes that did not fit, with brief reasoning for why the exception does not invalidate the pattern. If no anti-cases observed yet, write "none observed yet" — do not skip this section.]
```

## Confidence escalation

A pattern's confidence escalates after promotion based on subsequent evidence:

- `tentative` → `provisional`: the pattern has been reaffirmed by at least 2 additional notes after promotion
- `provisional` → `established`: the pattern has been consistently reaffirmed across 6+ months and 5+ campaigns

Confidence escalation is NOT the work of `promote-pattern`. It is a separate cycle (Phase 2) tracked through note-taking and a future re-affirmation skill.
