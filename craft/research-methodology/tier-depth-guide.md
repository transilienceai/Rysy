---
playbook: tier-depth-guide
applies_to_tiers: [A, B, C]
applies_to_personas: [all]
version: 0.1
last_updated: 2026-04-27
---

# Tier depth guide

The campaign input JSON includes a `priority` field for each lead: A, B, or C. This playbook defines what each tier means in terms of research scope, time budget, and which other playbooks run.

## Tier definitions

### A-tier — high-priority prospects

The prospect is a strategic target. The email needs to land. Research scope is full.

**Time budget**: 60-90 minutes per prospect

**Playbooks run**:
- `linkedin-deep-read.md` (full protocol, all 5 stages)
- `web-discovery.md` (full search patterns)
- `company-intelligence.md` (all 5 stages)
- `trigger-event-detection.md` (full)
- `github-and-code-mining.md` (if persona is technical and account exists)
- `podcast-and-talks.md` (if any talks/podcasts exist)

**Output expectations**:
- Research notes are comprehensive across all sections
- At least 3 verbatim quotes captured (from posts, talks, articles)
- Engagement web is mapped (Stage 4 of LinkedIn protocol)
- Trigger event is identified and synthesized
- The portrait will be detailed enough to support warm-observational or diagnostic-pattern register

**Drafts**: A-tier prospects can get an alternative draft as well, with rationale for both versions.

### B-tier — standard prospects

The prospect is a credible target. Research scope is focused.

**Time budget**: 25-40 minutes per prospect

**Playbooks run**:
- `linkedin-deep-read.md` (Stages 1-4; Stage 5 only if signals are thin)
- `web-discovery.md` (focused search; skip aggregators unless time allows)
- `company-intelligence.md` (Stages 1-3)
- `trigger-event-detection.md` (basic; skip the engagement-web inference)

**Skipped**:
- `github-and-code-mining.md` (unless link is on hand and persona is technical)
- `podcast-and-talks.md` (unless explicitly relevant)

**Output expectations**:
- Research notes are present in all sections, but External trail and Engagement web may be light
- At least 1 verbatim quote captured
- Trigger event is identified
- Portrait will be sufficient for dry-precise or diagnostic-pattern register

### C-tier — lighter prospects

The prospect is part of a broader campaign and the email is modest in ambition. Research is deliberately minimal.

**Time budget**: 5-10 minutes per prospect

**Playbooks run**:
- `linkedin-deep-read.md` (Stages 1 and 2 only — Profile snapshot and Activity scan)
- `company-intelligence.md` (Stages 1 and 2 only — Company snapshot and Recent events)
- `trigger-event-detection.md` (campaign-level trigger applied; minimal prospect-specific augmentation)

**Skipped**: Everything else.

**Output expectations**:
- Research notes are minimal but accurate
- No verbatim quotes required (often there will be none to capture)
- Campaign-level trigger may be the only trigger
- Portrait will be light; register is usually dry-precise (the register that requires the least prospect-specific signal)

## Why tiers exist

The purpose is *resource allocation*. Research time is the scarce resource. A-tier prospects deserve the full hour; C-tier prospects need a workable 5 minutes. Spending equal time on every prospect produces miscalibrated effort — too much on the unimportant, too little on the strategic.

## How tier affects the witness

The witness applies the same standards regardless of tier — but its tolerance for *thin signal* in the email shifts. For C-tier, the witness accepts that the email may rely on campaign-level signal rather than prospect-specific signal, as long as the campaign-level signal is credible. For A-tier, the witness expects prospect-specific signal in every key sentence.

## Disqualify checks at each tier

All tiers run disqualify-signal checks (recent layoff at company, prospect on PTO, prospect in active crisis). A disqualify hit at any tier results in `status: skipped` in the output, with the disqualify reason documented.

For A-tier prospects, the disqualify check is more thorough — Rysy actively looks for any reason the prospect should not be contacted right now.

## Tier escalation and de-escalation

The tier is set in the input JSON, but Rysy can flag a mismatch. If C-tier research surfaces material that suggests the prospect deserves A-tier treatment (a major recent role change, a hot trigger event), Rysy notes this in the output and the human reviewer can decide whether to upgrade.

Conversely, if A-tier research surfaces a reason the prospect is poorly fit (the disqualify check, or simply that the prospect is not as strategic as the input assumed), Rysy flags this too — and may downgrade or skip.
