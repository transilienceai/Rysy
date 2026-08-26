---
name: take-craft-note
description: Writes a dated atomic observation to craft/notes/ with consistent frontmatter. Invoke when Rysy notices something worth recording during or after prospect engagement.
---

# take-craft-note

Rysy's note-taking primitive. Writes one atomic observation per file in `craft/notes/` with a consistent format, then updates the index.

## When to invoke

After a prospect engagement (research run, draft, witness verdict), ask: *did anything in this run change my understanding?* If yes, invoke this skill. If no, do not invoke. Note-taking for its own sake produces low-quality smriti.

Specific triggers worth a note:

- The witness flagged something that may be a generalizable pattern, not a one-off
- A move that worked unusually well or unusually badly
- A signal in research that turned out to be misleading
- A reader response (when known) that reframed how Rysy thinks about a persona
- A subject line, opener, or CTA that landed (or didn't) in a notable way
- A research method that surfaced something the standard playbook missed

## Inputs

When invoking, supply:
- `observation` — the 2-3 sentence observation, specific not abstract
- `evidence_link` — link or path to the artifact that triggered the note
- `tags` — 2-5 tag slugs (persona, sector, move, phenomenon — see `craft/notes/README.md`)
- `campaign_id` (optional) — if note arose from a specific campaign
- `lead_id` (optional) — if note arose from a specific prospect
- `hypothesis` (optional) — one-line generalization candidate
- `test_next_time` (optional) — what would confirm or refute this in upcoming campaigns

## Workflow

1. Build filename: `{YYYY-MM-DD}-{slug-of-observation}.md` (slug derived from first few words of observation)
2. If filename already exists today, append `-2`, `-3`, etc.
3. Write file to `craft/notes/{filename}` with the schema in `craft/notes/README.md`
4. Append a row to `craft/notes/INDEX.md` with date, slug, tags, status
5. Status defaults to `observation` unless `hypothesis` is supplied (then `hypothesis`) or test_next_time + 2+ corroborating prior notes are tagged (then `tentative-pattern`)

## Schema enforced

Frontmatter:
```yaml
---
date: <ISO-8601>
campaign_id: <id or null>
lead_id: <id or null>
tags: [<list>]
status: observation | hypothesis | tentative-pattern
---
```

Body sections:
1. `# What I noticed` — the observation, 2-3 sentences
2. `## Evidence` — bullet list of evidence links
3. `## Hypothesis` (only if supplied)
4. `## Test next time` (only if supplied)

## Anti-patterns

- Notes that try to capture more than one observation. Split into multiple notes.
- Notes without evidence pointers. Always cite the artifact that triggered the note.
- Notes that describe the prospect rather than the observation. Prospect-specific facts go in `experience/prospects/{lead-id}/`. Notes are about *what was learned*, not *who was researched*.
- Notes that are speculation without an evidence section. Speculation goes in `craft/open-questions.md`.

## What this skill does *not* do

- It does not promote notes to patterns. That is `promote-pattern`'s explicit work.
- It does not reorganize the notes directory. That is `reindex-memory`'s work.
- It does not delete or modify existing notes. Notes are append-only.
