# Persona file format

Every file in `craft/personas/` follows this schema.

## Frontmatter

```yaml
---
role: <slug>                           # e.g. ciso
typical_seniority: <range>             # e.g. "VP / SVP / C-suite"
typical_tenure_in_role: <range>        # e.g. "18-36 months in current role; 2-3 prior security leadership roles"
typical_company_stage: <list>          # e.g. ["growth-stage", "public", "regulated"]
buying_authority: <description>        # e.g. "primary decision-maker for security tooling >$50K"
last_seeded: <date>
last_updated: <date>
---
```

## Body sections (in order)

### Who they are

Three to four paragraphs of prose portrait. Not a list of attributes — actual prose describing the role, the typical career path, the typical mental model, the dominant frustrations and ambitions of someone in this seat. Rysy reads this to *see* the prospect before drafting; lists do not produce sight, prose does.

### What they care about

Prioritized list of concerns with a brief rationale for each. Three to seven items. Each item is something a person in this role would *spontaneously bring up* in conversation — not a generic concern any senior leader would have.

### What consumes their week without payoff

Three to five items describing the *toil* of the role — the recurring drains on attention that don't move the work forward. These are leverage points: an email that touches an unrewarded toil tends to land, because the reader recognizes themselves immediately.

### What they hate seeing in a cold email

Concrete, specific anti-patterns. Not "generic emails" — name the actual phrasings, hooks, and moves that this persona reflexively rejects. The witness consults this section heavily.

### What they tend to respond to

Concrete, specific patterns that do work for this persona. Same level of specificity. These are calibrated tendencies, not guarantees.

### Voice register fit

Which modes from `self/voice-palette/` work for this persona, and *why*. Not "all of them." Pick one or two primary registers and one or two contraindicated registers. Explain the reasoning.

### Reference exemplars

Links to two or three exemplars in `craft/exemplars/` that successfully reached this persona. Phase 1 may have empty references until exemplars are seeded.

### Open questions

Things Rysy has noticed about this persona but has not yet promoted to belief. Hypotheses to test in upcoming campaigns. This section grows over time as Rysy works.

## Why each section exists

- *Who they are* anchors the psychological portrait the profiler builds
- *What they care about* and *what consumes their week* shape the opener
- *What they hate / respond to* shape the body and CTA
- *Voice register fit* shapes the drafter's register selection
- *Reference exemplars* let Rysy calibrate against successful past work
- *Open questions* track what Rysy is still learning about this seat

A persona file with any section skipped is incomplete and will produce miscalibrated drafts.
