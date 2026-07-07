---
description: Refresh craft/trends/current.md by pulling current security/eng narratives from configured sources and filtering noise from real trends.
---

Invoke the `refresh-trends` skill. The skill's instructions are in `.claude/skills/refresh-trends/SKILL.md`. Source list is in `.claude/skills/refresh-trends/sources.yaml`.

Run the five-phase workflow: collection → topic clustering → filter (≥3 independent sources, behavioral signal, ≥2 weeks time depth, ≥1 practitioner voice) → synthesis → write and archive.

Report:
- Sources consulted
- Topics surviving the filter (count)
- Topics dropped (count, with example reasons)
- Path to the new `craft/trends/current.md`
