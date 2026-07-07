---
description: Scan recent craft notes for clusters that meet pattern-promotion criteria, and promote them to craft/patterns/.
---

Invoke the `promote-pattern` skill. The skill's instructions are in `.claude/skills/promote-pattern/SKILL.md`.

The skill scans `craft/notes/` for the last 30 days, clusters notes by tag overlap, applies promotion criteria (≥3 corroborating notes, ≥2 distinct campaigns, no unrebutted counter-evidence), and promotes surviving clusters to `craft/patterns/` with explicit evidence pointers.

Report:
- How many candidate clusters were considered
- How many were promoted
- How many were rejected, and why

Do not modify `self/` — pattern promotion is a craft-layer operation.
