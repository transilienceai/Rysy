---
date: 2026-07-23T00:00:00Z
campaign_id: 2026-07-23-transilience-insurtech-health-payments
lead_id: zipari-mpulse
tags: [research-handoff, factual-integrity, witness, elapsed-time, first-sentence]
status: hypothesis
---

# What I noticed

The researcher's notes carried both a hard date (acquisition closed September 2024) and a derived figure computed from it ("approximately 10 months into integration"). The two contradicted each other — from a September 2024 close, July 2026 is twenty-two months. I put the derived figure into the first sentence of the draft without recomputing it. The witness caught it.

The structure of the error is what makes it worth recording. I checked the *sourcing* of the research (was the acquisition date verified? yes, press release) and treated everything downstream of a verified fact as inherited. But an elapsed-time figure is not a fact — it is arithmetic performed at the moment the note was written, and it decays. A researcher writing "10 months" may have been working from a stale draft, a different close date, or simple error; the note's own verified dates were sufficient to catch it and I did not do the subtraction.

Two things compound the cost. First, elapsed-time figures gravitate to the opener, because "N months after X" is a natural way to establish that the sender understands the reader's situation — so the error lands in the sentence with the least tolerance for it. Second, the reader is by definition the person who lived through the interval. Brian Higgins would not have needed to check twenty-two versus ten; he would have felt it wrong before finishing the line, and every subsequent claim would inherit that doubt.

The corrected figure was also the *better* figure. Environments still separate at ten months are mid-integration; environments still separate at twenty-two months are separate for structural reasons. The error was not just wrong, it was weaker.

## Evidence

- Research notes: `experience/prospects/zipari-mpulse/research-notes.md` (September 2024 close, verified; "~10 months into integration", derived and wrong)
- Draft v1: `experience/prospects/zipari-mpulse/drafts/v1.md` — "Ten months after a close" in sentence one
- Witness rejection: `experience/prospects/zipari-mpulse/witness-feedback.md`
- Corrected: `experience/prospects/zipari-mpulse/drafts/v2.md`, witness verdict `ship`
- Near-miss on the same campaign: `experience/prospects/bloom/` — research notes dated the CMS audit report July 15, 2025 while calling it eight days old. Caught before drafting; the email ships with no date at all and a flag for human verification.

## Hypothesis

Any figure in a research note that was *computed* rather than *observed* — months elapsed, tenure length, company age, headcount growth, time since funding — should be recomputed from the underlying dates before it enters a draft, and preferentially replaced with the underlying date or a coarser phrase ("nearly two years past the close") that degrades gracefully if slightly off.

The sharper version of the hypothesis: a research note should be read as two documents. The observations carry the researcher's verification. The inferences and arithmetic carry only the researcher's attention at the time of writing, which is not the same thing, and the doer is the last line of defense on them. Related: [[witness-must-check-implication-not-factuality]] — the witness caught this one, but it caught it as a factual error, which the note there argues is not primarily the witness's job. Two of two campaigns have now produced a factual defect that reached the witness. That is the doer's failure both times.

## What I would test next

Whether a standing pre-draft pass — recompute every number in the research notes, name the ones that cannot be recomputed from stated sources — costs less than the rewrite cycle it prevents. Two data points from this campaign say it would have caught both instances before either reached a draft.
