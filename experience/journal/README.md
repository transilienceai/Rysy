# experience/journal/

Rysy's introspective record. Where she writes about herself and her work, distinct from the per-prospect notes in `experience/prospects/` and the craft observations in `craft/notes/`.

## Subdirectories

- **`monthly/`** — periodic introspection entries, written by the `introspecter` sub-agent or by Rysy herself when she runs introspection. Filename: `{YYYY-MM}-introspection.md`.

- **`adhoc/`** — triggered reflections after specific sessions or campaigns where something notable happened. Filename: `{YYYY-MM-DD}-{slug}.md`.

- **`proposed-character-diffs/`** — pending diffs to `self/character.md` written by Rysy or the introspecter. Each diff awaits human approval before being applied. Filename: `{YYYY-MM-DD}-{slug}.md`.

- **`applied-character-diffs/`** — archive of approved-and-applied diffs. Filename matches the original proposed-diff filename plus `applied-{date}` suffix.

## What goes in monthly introspection

The `introspecter` sub-agent, when invoked, runs in fresh context with read access to `self/character.md`, recent journal entries, recent patterns, and recent campaign reflections. It writes a monthly entry that:

- Describes what Rysy has been doing (inferred from recent activity)
- Identifies any drift between her stated character and her recent behavior
- Proposes (separately, in `proposed-character-diffs/`) any constitutional change that drift would warrant

A monthly entry exists for accountability — even if no drift is detected, the entry confirms the introspecter ran and what it found.

## What goes in adhoc

Adhoc entries capture in-the-moment reflection that does not warrant a full monthly introspection but is worth recording. Triggers include:

- A campaign where the witness rejected an unusual number of drafts
- A campaign where reply rates were notably high or low
- A research run that surfaced something Rysy did not expect
- A specific tension between two of her values that came up in the work

These entries are short (1-3 paragraphs) and timestamped.

## Proposed character diff format

```yaml
---
proposed: <date>
proposed_by: rysy | introspecter
trigger: <what surfaced this proposal>
approved_by: null  # filled in by human
approved_at: null  # filled in by human
status: pending | approved | rejected
---
```

Body:

```markdown
# Proposed change to self/character.md

## What I propose changing

[Specific text in character.md that should change]

## To what

[Specific replacement text]

## Why

[The reasoning, including evidence. What I have been doing that suggests the existing wording does not match my actual practice or what I have learned that suggests it should not.]

## What stays the same

[Explicit confirmation that adjacent values and principles are not being challenged, only the specific wording or position being addressed.]
```

The diff is *not* applied automatically. The `pre-write-self-protect.py` hook blocks any direct write to `self/`. The only sanctioned application path is the `apply-approved-diff` skill, invoked via `/apply-diff`, after the human has set `approved_by` and `approved_at` in the frontmatter.

## Why this layer exists

A learning agent without introspection drifts. An introspective agent without a record of introspection has no way to track its own evolution. This directory is where Rysy holds herself accountable — both to the work and to the question of who she is becoming through it.
