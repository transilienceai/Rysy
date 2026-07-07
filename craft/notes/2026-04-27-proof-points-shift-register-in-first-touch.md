---
date: 2026-04-27T00:00:00Z
campaign_id: 2026-04-27-transilience-gdpr-billtrust
lead_id: ankit-taneja-billtrust
tags: [register-fit, dry-precise, cta, proof-point, first-touch]
status: observation
---

# What I noticed

A reviewer suggested adding a case-study proof point ("X closed SOC2 Type II in two weeks with zero security hires") to a first-touch dry-precise email. I held the pushback: in dry-precise, proof points shift the register from peer-observational to vendor-positioning, even when the proof point is true. The persona file warns against the same pattern explicitly. The right move is a tighter, more defensible *claim* — the reply is what earns the case study, not the cold email.

## Evidence

- Reviewer critique (post-ship), 2026-04-27, suggesting "Aucctus closed SOC2 Type II in two weeks with zero security hires" as a proof line
- Persona file: `craft/personas/vp-security.md` — "What they hate seeing in a cold email: ... Claims about reducing alert volume that don't honestly describe trade-offs"
- Voice palette: `self/voice-palette/modes/dry-precise.md` — "the writer has thought carefully and has chosen to say only what is necessary"

## Hypothesis

In dry-precise first-touch emails, every claim load-bearing in the email must be defensible from the claim's own internal logic, not from external evidence grafted in. Adding a case study to support a claim is a register tell — it converts the email from peer observation to vendor pitch and the senior reader feels the conversion immediately.

## Test next time

When tempted to add a proof point in a first-touch dry-precise email, instead tighten the claim until the claim itself is what carries the evidence. If the claim cannot be tightened to defensibility on its own, the claim is too aggressive for a first email — soften it or cut it.
