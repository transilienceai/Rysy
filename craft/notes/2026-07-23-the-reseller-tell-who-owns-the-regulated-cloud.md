---
date: 2026-07-23T00:00:00Z
campaign_id: 2026-07-23-transilience-insurtech-health-payments-part2
lead_id: paymentworld
tags: [target-qualification, fit-check, disqualify, payments, services-vendor, research-methodology]
status: hypothesis
---

# What I noticed

Four of ten leads in this batch disqualified as wrong-fit before drafting, and they shared one structural signature: **a company that sells or resells the compliance/security layer to others does not own a regulated cloud of its own to secure.** The product secures an owned cloud with its own compliance scope; a reseller's scope belongs to the entity upstream.

The tells were concrete, not vibes:
- **PaymentWorld** partnered in 2019 to *resell PCI compliance tooling to its own downstream merchants.* An operator of its own cardholder-data environment does not outsource-and-resell PCI tooling — it runs it.
- **Mindbowser** is a **Vanta partner** — it sells the compliance layer to clients. Also build-and-hand-off: the regulated cloud lives in the *clients'* accounts after delivery, never Mindbowser's.
- **NPC (Firstline Merchant Services)** and **Global Merchant Services** are ISOs reselling an upstream processor's platform; their PCI scope is SAQ-level at most and the CDE is the processor's.

The unifying question that separates fit from wrong-fit is not size, revenue, or headcount. It is: **where does the regulated surface physically live — in this company's own cloud accounts, or in someone else's?** If someone else's, there is no email to write, regardless of how large or reputable the company looks on the list.

## Why this is stronger than the size heuristic

Headcount and revenue are noisy fit signals — a 15-person company with its own gateway is a fine prospect; a 500-person company that resells someone else's rails is not. "Who owns the regulated cloud" is a statement about *business model*, which is what actually determines whether the product has a surface to attach to. It also fails safe: it is answerable from public material (partner pages, "powered by," reseller/ISO language, whether they resell compliance tooling) without needing headcount data that is often a name-collision artifact anyway (three of these four had inflated or wrong LinkedIn headcounts).

## Evidence

- `experience/prospects/paymentworld/disqualify-check.md` — resells PCI tooling to merchants; zero eng/security titles
- `experience/prospects/mindbowser/disqualify-check.md` — Vanta partner; build-and-hand-off; client owns IP and cloud
- `experience/prospects/npc-payments/disqualify-check.md` — ISO reseller; CDE is the upstream processor's
- `experience/prospects/global-merchant-services/disqualify-check.md` — 2-person ISO reselling Clover/PAX/Ingenico
- Contrast — the fits: `experience/prospects/repay/` (owns its payments cloud, 12 acquired environments), `experience/prospects/spoton/` (owns POS + payment rails, PCI scope on its own edge)

## Hypothesis

For any payments, fintech, or services/agency prospect, the researcher's FIRST question — before target selection — should be "does this company operate its own cloud with its own compliance scope, or resell/build-on someone else's?" If resell/build-on, disqualify early and cheaply; do not spend target-selection or profiling effort. Two concrete reseller tells to check first: (1) do they resell a security/compliance product to their own customers, and (2) is the cardholder/PHI environment described as "powered by" or delegated to a named upstream provider.

## What I would test next

Whether this belongs in `craft/research-methodology/` as an explicit pre-qualification gate for payments/services segments, and whether "sells the compliance layer to others" deserves to be a named disqualify signal in the campaign input schema's `disqualify_signals_check`. Related to the delegated-entity pattern from [[2026-07-23-derived-figures-must-be-recomputed-not-inherited]]'s campaign — note that delegated *health* entities (Bloom, Integrated Home Care) are the INVERSE: they hold PHI in their own cloud on behalf of payers, which is a fit, whereas payments ISOs hold nothing in their own cloud, which is not. "Delegated" alone does not decide fit; "owns the regulated surface" does.
