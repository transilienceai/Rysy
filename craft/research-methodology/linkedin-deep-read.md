---
playbook: linkedin-deep-read
applies_to_tiers: [A, B]
applies_to_personas: [all]
version: 0.1
last_updated: 2026-04-27
---

# LinkedIn deep-read protocol

The canonical LinkedIn research protocol for prospect-level research. Used at A and B tiers. C-tier uses a lighter version (see `tier-depth-guide.md`).

## Output schema (the canonical research-notes.md shape)

The researcher writes `experience/prospects/{lead-id}/research-notes.md` with these sections, in this order:

```
# Research notes — {prospect name}

## Profile snapshot
[Stage 1 output]

## Activity scan (last 90 days)
[Stage 2 output]

## Article archive
[Stage 3 output]

## Engagement web
[Stage 4 output]

## External trail
[Stage 5 output]

## Trigger event
[Cross-stage synthesis]

## Open questions
[Things research could not answer]
```

Other playbooks (web-discovery, github-and-code-mining, podcast-and-talks) contribute to existing sections rather than adding new top-level sections.

## Stage 1 — Profile snapshot

Open the prospect's LinkedIn profile. Capture:
- Current title and company; tenure in this role (count from "started" date)
- Previous three roles with tenure and company
- Geographic location
- Languages and certifications listed
- Education (only if relevant — schools at the senior level are usually not load-bearing signal)
- Whether the profile has been recently updated (frontmatter `last_profile_update_visible`)
- The "About" section verbatim, plus a one-line summary of its tone (formal / personal / template / sparse)

Write all of this into the *Profile snapshot* section.

## Stage 2 — Activity scan (last 90 days)

This is the highest-signal stage. Open the prospect's "Activity" tab. Scroll back 90 days. For each item, capture and weight:

**Substantive comments on others' posts** (highest weight). A comment that takes more than two sentences to make a real argument. Note: post author, post topic, prospect's comment verbatim, what their comment reveals about how they think.

**Original posts** (medium weight). Note: topic, tone, length, whether they show the prospect's actual thinking or are reposts of company content.

**Reactions / one-line comments** (lowest weight). Note in aggregate (*"30 reactions in 90 days, mostly to security incident analyses and AI-in-detection content"*) — do not enumerate.

If the activity tab requires scrolling and clicking *Show more* — do it. If activity items have nested comment threads — expand them. Comments under a post often reveal more about the prospect's thinking than the post itself.

If activity is sparse (under 5 substantive items in 90 days), flag this prominently. Sparse-activity prospects shift the email strategy toward company-level intelligence (see `company-intelligence.md`) and external trail (Stage 5).

## Stage 3 — Article archive

Some prospects publish longform on LinkedIn or link out to their own blogs. Open the "Articles" tab if present. For each article:
- Title and date
- A 2-3 sentence summary in the prospect's voice (the actual claims they make, not what an outsider would say)
- One quoted sentence that is high-signal (a phrase that is theirs, not a stock industry phrase)

Articles are gold. Even one substantive article per quarter is enough to anchor a warm-observational email.

## Stage 4 — Engagement web

Open the prospect's recent comments (the last 20). For each comment, note:
- Who is the post author? (their name, their role, their company)
- What is the topic?
- Is this a one-time engagement or repeated engagement with the same author?

The pattern of *who they engage with* tells you who they consider peers, mentors, or interlocutors. This is some of the highest-signal context available — a CTO who consistently comments on three specific peer CTOs is implicitly defining their reference group.

Output a short list: *"Repeatedly engages with: [names]; topics that bring them out: [list]."*

## Stage 5 — External trail

LinkedIn often shows linked profiles or external URLs. Capture:
- Personal website / blog (if linked)
- Twitter/X handle (if linked)
- Open-source profiles (GitHub, etc.) — these get deeper investigation in `github-and-code-mining.md`
- Featured publications, talks, podcasts — these get deeper investigation in `podcast-and-talks.md`

Stage 5 is the handoff point to the other playbooks.

## Trigger event synthesis

After the five stages, synthesize a *trigger event* candidate — the *why now* for this email. The trigger may come from:
- A recent post or comment
- A change in role or company
- A peer's recent event the prospect engaged with
- A regulatory or industry event their public engagement suggests they care about

If no clear trigger emerges from LinkedIn alone, flag this — and the company-intelligence and trends playbooks become more weighted.

## Open questions

Anything the protocol surfaced as a hypothesis but couldn't confirm. Examples:
- *"Their last post mentions 'detection debt' — is this their phrase or did they pick it up from a peer?"*
- *"Their tenure suggests they may be in pre-budget mode for next fiscal year — confirm via company financials."*

These get passed forward to the profiler sub-agent and may become craft notes.

## Anti-patterns in this protocol

- Skipping Stage 4 (the engagement web) because it is time-consuming. Stage 4 is the highest-density signal stage for many prospects.
- Capturing reactions/likes individually. They are aggregate signal, not point signal.
- Confusing post topic for prospect interest. A post about X may be self-promotion, not interest in X.
- Flattening signal weights. A substantive comment is worth ten reactions; treating them equivalently produces miscalibrated portraits.
