---
date: 2026-08-13T00:00:00Z
campaign_id: 2026-07-23-transilience-insurtech-health-payments
lead_id: (set-level — all ten)
tags: [witness, set-review, template-convergence, ai-tells, humanize, product-sentence]
status: hypothesis
---

# What I noticed

The human reviewer rejected ten witness-shipped, tell-scan-clean finals as "AI slop." They were right, and the evidence was greppable: "holds live posture state" in 6/10 emails, "for a human/person to approve" in 7/10, "worth fifteen minutes" in 8/10, one identical five-beat skeleton in all ten. Every email passed alone; the set was a template. The per-email witness cannot see this by construction — it reads one draft at a time.

The deeper finding came from the fix. The first rewrite (v3) varied the *words* and kept the *structures*: a set-level witness found the three-verb tricolon product sentence still present in all ten (reads/keeps/holds/watches/tracks/maintains — six verbs, one architecture), every email at exactly six sentences, and the second rewrite (v4) then *introduced its own convergences* — "Transilience keeps" as clause-opener in 5/10, "[fix] arrives written/drafted" in 6/10, nine of ten with exactly one em-dash, all ten with exactly one semicolon. **Convergence is conserved under synonym rotation.** When you fix a repeated phrase without changing the sentence's architecture, the repetition reappears one level up.

What actually worked (v5): vary the architecture itself — product as two-beat, effect-first ("what you get is the correction, not a report about it"), appositive, standalone declarative ("Nothing touches that environment without a human's yes"); sentence counts spanning 4–6; CTA shapes all different; off-ramp closes cut from five to two; punctuation counts uneven on purpose. Final audit: all eight template phrases at 0–2 of 10.

One boundary the third-round set witness drew that I want to keep: **template versus voice.** One product's three functions appearing in every email is voice — that is what the product does. Domain vocabulary shared by same-sector emails is voice. Identical *constructions* are template. A signature move (the off-ramp) at 2-in-10 is a voice; at 5-in-10 it is a tic.

## Evidence

- Slop audit (before): main-thread grep, 2026-08-13 — counts above
- Set reviews: `experience/campaigns/2026-07-23-transilience-insurtech-health-payments/set-review-v3.md`, `set-review-v4.md`, `set-review-v5.md`
- Per-email trail: `experience/prospects/*/drafts/v3–v5.md` + `witness-feedback-v3/-v4/-v5.md`
- After: template phrases 3–8/10 → 0–2/10; sentence counts 4/5/6 = 2/4/4; em-dash 0/1/2 = 2/7/1

## Hypothesis

For any multi-lead campaign: (1) a set-level witness pass over all finals is mandatory before delivery — the per-email witness structurally cannot do this job; (2) rewrites driven by convergence findings must change sentence *architecture*, not vocabulary, or the convergence re-forms; (3) the reviewer of round N must re-derive its findings from scratch on round N+1, because fixes introduce new convergences exactly where the old ones were removed.

## What I would test next

Whether the set-level pass belongs in the run-campaign skill itself as a standing step between per-lead finalization and campaign close — and whether a cheap deterministic pre-pass (grep for 3+-word phrases in ≥3 finals, sentence-count histogram, punctuation histogram) catches enough that the set witness can start from evidence instead of discovery. Related, doer-side: [[2026-07-23-derived-figures-must-be-recomputed-not-inherited]] — both are cases of the doer inheriting structure (a figure, a skeleton) without re-deriving it.
