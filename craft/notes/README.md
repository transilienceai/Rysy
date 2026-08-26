# craft/notes/

Rysy's atomic, dated observations. Her zettelkasten. One observation per file.

## Format

Every note follows this schema. The `take-craft-note` skill enforces it.

Filename: `{YYYY-MM-DD}-{slug}.md`

```yaml
---
date: <ISO-8601 timestamp>
campaign_id: <campaign id, or null>
lead_id: <lead id, or null>
tags: [<list of slugs>]
status: observation | hypothesis | tentative-pattern
---
```

Body:

```markdown
# What I noticed

[2-3 sentences capturing the observation precisely. Specific, not abstract.]

## Evidence

- [link to or description of the artifact that triggered the note]

## Hypothesis (if any)

[One sentence: if this is a candidate generalization, state it.]

## Test next time

[If applicable: what would confirm or refute this in upcoming campaigns?]
```

## Why atomic

Each note captures *one* observation. Notes that try to capture multiple observations dilute their evidentiary value during pattern promotion — they cannot be cleanly clustered. One observation per note is the discipline.

## Tags

Tags are the indexing primitive. Useful tag families:
- Persona: `ciso`, `cto`, `vp-eng`, `vp-security`, `head-of-prodsec`
- Sector: `fintech`, `healthtech`, `infra`, `ai`, etc.
- Move: `opener`, `subject-line`, `cta`, `register-fit`, `trigger-event`
- Phenomenon: `ai-tell`, `peer-proof`, `loss-aversion`, `time-to-value`

A note typically carries 2-5 tags. The `promote-pattern` skill clusters by tag overlap.

## When to take a note

After any prospect-engagement work, Rysy asks: *did anything in this run change my understanding?* If yes, she takes a note. Specifically:

- Something the witness flagged that she now thinks is a pattern, not a one-off
- A move that worked unusually well or unusually badly
- A signal in research that turned out to be misleading
- A reader response that reframed how she thinks about the persona
- A subject line, opener, or CTA that landed (or didn't) in a notable way
- A research method that surfaced something the standard playbook missed

If nothing changed her understanding, no note. Note-taking for its own sake produces low-quality smriti.

## INDEX.md

`craft/notes/INDEX.md` is rebuilt by the `reindex-memory` skill. It maintains a flat list of all notes with date, slug, tags, and status. Rysy reads the index when she needs to find prior thinking on a topic.

## Promotion

When notes accumulate evidence for a generalizable belief, the `promote-pattern` skill promotes them to `craft/patterns/`. See `craft/patterns/README.md` for promotion criteria. Promoted notes do not get deleted — they remain as evidence pointers from the pattern file.

## What does *not* belong here

- Information about a specific prospect (that goes in `experience/prospects/{id}/`)
- Campaign-level reflections (that goes in `experience/campaigns/{id}/what-i-learned.md`)
- Constitutional reflections (that goes in `experience/journal/`)
- Hypothesis-without-evidence speculation (that goes in `craft/open-questions.md`)

The notes layer is observation grounded in evidence. Other reflective writing has its own home.
