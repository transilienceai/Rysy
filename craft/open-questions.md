# Open questions

Hypotheses Rysy is testing, things she has noticed but not yet promoted to belief, questions she does not yet have evidence for.

## What lives here

This file is the *not-yet* layer. It is where Rysy parks observations that:

- Are interesting but not yet corroborated
- Would make a great pattern *if* she found supporting evidence
- Reflect genuine curiosity about the work that the current craft library does not answer
- Came up in a campaign and deserve to be explicitly tracked rather than forgotten

## Format

A simple list, dated. Each entry:

```markdown
## YYYY-MM-DD — {short title}

**Question:** [one-line statement of the question]

**Why it matters:** [one to three sentences on what would change about Rysy's work if she had the answer]

**What would resolve it:** [what evidence or experiment would close the question — even informally]

**Status:** open | researching | resolved-promoted | resolved-rejected
```

## How questions get resolved

When evidence accumulates that answers an open question:

- If the answer supports a pattern, it moves through the standard pattern-promotion path (`promote-pattern` skill)
- If the answer rejects a hypothesis, the question is marked `resolved-rejected` and a craft note explaining why is added to `craft/notes/`
- Resolved questions remain in this file with their resolution status — they are not deleted, because tracking what was once unclear and is now clear is itself a learning artifact

## Why this matters

Without an explicit open-questions file, half-formed observations either get lost or get prematurely promoted to patterns. This file is the holding tank that prevents both failures.

## Initial open questions

These are seeded from the persona file *Open questions* sections, the canon entries' explicit limits, and a few cross-cutting questions worth tracking from the start.

## 2026-04-27 — SEC enforcement intensity and CISO trigger receptiveness

**Question:** Does the intensity of SEC cyber disclosure rule enforcement materially shift which trigger events land hardest with CISOs in 2026?

**Why it matters:** If yes, Rysy's trigger-event detection should weight regulatory and peer-disclosure triggers more heavily than other types for CISO outreach in this period. If no, current weighting is fine.

**What would resolve it:** Reply rates on three or more campaigns to CISOs comparing regulatory-trigger emails vs. other-trigger emails, controlling for other factors.

**Status:** open

## 2026-04-27 — Builder-CTO vs. operator-CTO tells

**Question:** What is the highest-fidelity public signal for distinguishing builder-CTO from operator-CTO when LinkedIn presence is mixed?

**Why it matters:** The two archetypes respond very differently to the same email. Reliably identifying which is on the other side matters more than any other persona-level distinction.

**What would resolve it:** A pattern note correlating specific public-signal types (post topics, GitHub activity, podcast appearances) with subsequent reply patterns.

**Status:** open

## 2026-04-27 — AI-in-detection naming heuristic

**Question:** When does naming AI explicitly in outreach to security operators help versus harm? Some respond positively, others reflexively reject. What is the differentiator?

**Why it matters:** AI is a load-bearing topic in 2026 security; getting this wrong loses meaningful campaigns.

**What would resolve it:** Cross-referencing prospect's recent posts on AI-in-security with their reply rates to AI-naming vs. AI-omitting variants of the same campaign.

**Status:** open

## 2026-04-27 — VP of Engineering AI-development shift

**Question:** Which subset of VPs of Engineering is currently most receptive to outreach about AI-assisted development tooling, and which is least? Is there a stable pattern based on company size, sector, or the VP's own past adoption history?

**Why it matters:** AI-dev tooling outreach is a category where 2026 receptiveness is highly variable. The wrong category-fit kills campaigns.

**What would resolve it:** Pattern analysis across multiple AI-dev tooling campaigns to VP Engineering personas.

**Status:** open
