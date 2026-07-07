# Voice palette file format

Every file in `voice-palette/modes/` follows this schema. Consistency matters because the drafter selects registers by reading these files; inconsistent formats break the selection logic.

## Frontmatter

```yaml
---
register: <slug>                    # e.g. dry-precise
seniority_fit: [<list>]              # which seniorities this register naturally fits
persona_fit: [<list>]                # which personas this register naturally fits
length_default: <range>              # e.g. "3-4 sentences"
default_when: <one-line trigger>     # quick decision aid
---
```

## Body sections (in order)

### Description

Two paragraphs of prose describing the register from the inside — what it sounds like, what it feels like to read, what its center of gravity is. Not a checklist. Vendy reads this to *enter* the register, not to verify a draft against it.

### When to use

Concrete prospect-shape signals that suggest this register fits. Examples:
- Prospect is X (e.g., a battle-hardened CISO with a thin LinkedIn footprint)
- Trigger event is Y
- Their own writing reads as Z

Three to six bullet points. Specific, not generic.

### When *not* to use

The inverse: prospect-shapes where this register will misfire. Equally important — the register's failure mode usually shows up here.

### Sample openers

Two or three opening lines in this register, each ~1-2 sentences. These are not templates to copy; they are tuning forks. Reading them should put Vendy in the right rhythm.

### Anti-patterns

Specific tells that mean the register has slipped. The line "if your draft has X, you're not in this register, you're in a degraded version of it."

### Notes

Free-form. Anything Vendy has learned about this register that doesn't fit the sections above.

## Why this format

Each section answers a different question Vendy asks herself during drafting:
- *What does this sound like?* → Description
- *Should I use it for this prospect?* → When to use / When not to use
- *What rhythm am I in?* → Sample openers
- *Have I drifted out of it?* → Anti-patterns

Without all four, the register is unusable.
