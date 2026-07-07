---
date: 2026-04-27T00:00:00Z
campaign_id: 2026-04-27-transilience-gdpr-billtrust
lead_id: ankit-taneja-billtrust
tags: [witness, methodology, trigger-event, regulatory-pitch]
status: hypothesis
---

# What I noticed

The witness on v1 verified that the trigger facts were real and recent — Belgium e-invoicing mandate, Deloitte Belgium partnership, both true — and shipped the draft. A post-ship reviewer caught immediately that the trigger did not logically support the pitch's claim (the e-invoicing mandate is a VAT regime, not a GDPR Article 33 expansion). Factuality and implication are different checks. The witness performed the first; the email needed both.

## Evidence

- Witness verdict: `experience/prospects/ankit-taneja-billtrust/witness-feedback.md` (verdict: ship)
- Reviewer critique (post-ship) identified the logical gap in seconds
- v1 draft: `experience/prospects/ankit-taneja-billtrust/drafts/v1.md`

## Hypothesis

The witness's checklist for trigger-anchored emails should include an explicit implication step: given this hook, does the body's central claim follow without the reader manufacturing a step? If the implication chain has a missing link, the email reads as borrowing recency it has not earned, regardless of factuality.

## Test next time

Update witness invocations on regulatory or trigger-anchored drafts to ask three questions in order: (1) is the hook factually accurate? (2) is the hook logically connected to what the body claims? (3) would a domain expert read the connection as obvious or as stretched? Watch for cases where (1) passes but (2) or (3) fails. If the witness sub-agent's prompt needs to change, propose a diff to its definition.
