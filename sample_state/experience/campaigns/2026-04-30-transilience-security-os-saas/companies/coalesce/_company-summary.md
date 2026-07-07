# Coalesce.io — campaign company summary

**ICP fit:** A — primary. 142 employees, Series B Snowflake-ecosystem data transformation SaaS, no CISO, security ownership distributed across founding team and infra leadership. Two recent acquisitions (CastorDoc March 2025, SYNQ March 2026) creating Transform/Catalog/Quality platform. SOC 2 Type 2 (since July 2022), ISO, GDPR, HIPAA already in place.

## Four routings, four distinct angles, four distinct vocabularies

The discipline at a 142-person company: do not send four variants of the same email. Beyond just *angles*, each draft must use distinct *vocabulary, syntactic structure, and CTA shape* — because a forwarded email inside the company exposes templating-with-personalization-wrapper.

| Lead | Role | Subject | Angle | Product-sentence shape | CTA shape |
|---|---|---|---|---|---|
| Satish Jayanthi | CTO & Co-Founder | Permission state vs declared intent | Intent-vs-effective-permission-state, narrow gap CSPM doesn't close | Inversion: "*[description]* is what Transilience operates on" | Yes/no architectural choice |
| Mike McCune | VP of Engineering | SOC 2 after two acquisitions | Compliance-as-capacity-tax (engineering-economics) | Subject-verb: "Transilience generates..." | Open how-question |
| Justin Stanford | Director, Infrastructure | Terraform-declared vs actual cloud state | Continuous diff between IaC declared and actual deployed state | Subject-verb-object: "Transilience surfaces this diff continuously..." | Binary technical choice |
| Cyrille David | Head of Eng — Catalog | Coalesce Catalog and the controls cadence | Policy-in-catalog vs control-in-cloud cadence asymmetry | No product sentence — let the substance speak | Conditional question |

## Why this took six rounds of rewrites

The first round shipped four drafts on isolated-witness verdicts. User review caught a campaign-level failure mode the per-lead witness could not see: **the same four-item product enumeration ("declared baseline, continuous drift detection, prioritized findings, remediation human-in-the-loop") appeared verbatim in three of four drafts.** Personalization was the wrapper; the product pitch was the constant. One forward inside the company exposes the template.

A second round (Satish v3, Mike v3, Justin v4) fixed the verbatim repetition but introduced new structural echoes: "Transilience runs" opening two product sentences, "additive to existing CSPM" appearing in two, "Curious" starting all three CTAs, "after" in three of four subjects. A third round (Satish v4, Mike v4, Justin v5) resolved most. A fourth (Justin v6) cut residual filler and the last "additive" echo.

**Total: 18 drafts written across 4 leads. 4 shipped. 14 rewrites.**

## Lessons captured (in feedback memory)

1. **Cross-email diff is the doer's job, not the witness sub-agent's.** Subagents read in isolation and can't see verbatim phrase repetition across emails to the same company.
2. **"Acceptable risk" on a witness flag is usually rationalization.** When the witness names a weakness, fix it.
3. **Cadence-asymmetry framings must survive practitioner scrutiny.** A CISO running CSPM sees through audit-cycle-vs-continuous strawmans. Name the *narrow* honest gap (intent vs effective state).
4. **Preempt the "we already have this" objection.** Without one phrase distinguishing from Wiz/Drata/Vanta/Lacework, the category-incumbent filter blocks the email.
5. **Subject lines that read like newsletter headlines fail.** "{Concept} and the {abstract layer}" is editorial-shaped. Cold from a founder should sound like internal slack.

## Sequencing guidance

These four emails should NOT be sent in the same week. Recommended: one lead per fortnight, bottom-up by seniority (Justin → Cyrille → Mike → Satish). Four touches into one 142-person org in seven days is a campaign push that any reply chain surfaces internally.

## Artifacts

Per-lead final emails: `experience/prospects/{lead-id}/final.md`
Per-lead deeper artifacts (research, portrait, all drafts, witness feedback): `experience/prospects/{lead-id}/`
Per-lead campaign JSONs (this directory): `{lead-id}.json`
Cross-draft witness review: `_witness-cross-draft-review.md`
