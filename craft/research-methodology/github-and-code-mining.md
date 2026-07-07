---
playbook: github-and-code-mining
applies_to_tiers: [A, B]
applies_to_personas: [CTO, VP-Engineering, Head-of-Product-Security, technical-CISO]
version: 0.1
last_updated: 2026-04-27
---

# GitHub and code mining

For technical prospects, public code activity is some of the highest-signal research material available. A GitHub commit graph reveals what someone *actually does*, not what they *say* they do. This playbook covers the protocol for finding and reading their code-side public footprint.

## When to run this playbook

- The prospect's role is technical (CTO, VP Eng, Head of ProdSec, security engineering leadership)
- Their LinkedIn or other public bio links to GitHub or GitLab
- The prospect has, in the past five years, plausibly done hands-on technical work
- Tier A (always) or Tier B (if a GitHub link is on hand)

If the prospect is purely operational and has not done hands-on work in years, this playbook is low-yield; skip.

## Stage 1 — Find their account

Search patterns:
- `site:github.com "{name}"`
- `"{name}" "github"` (catches profile mentions)
- LinkedIn "Featured" section often links GitHub
- Their personal website (if found in `web-discovery`) usually links it

Multiple accounts: senior technical leaders sometimes have a *named* account and a *throwaway/personal* account. The named account is usually quiet; the personal account is more revealing.

## Stage 2 — Read their profile

On their account:
- Pinned repositories (what they want to be associated with)
- Recent commits (last 6 months — what they are actually doing)
- Repository they own vs. contribute to
- Stars (what they think is interesting)
- Following list (who they pay attention to)

Write findings into the *External trail* section under a sub-heading *GitHub*.

## Stage 3 — Recent activity reading

Open the contribution graph. Note:
- Frequency (daily? weekly? sporadic?)
- Concentrated areas (a recent burst of activity in one repo suggests current focus)
- Languages and frameworks (their technical taste)

If they have written commits in the last 90 days, sample a few. Read the commit messages — these reveal whether they write thoughtful code or rush. Sample the actual diffs of one or two — what kind of work are they doing?

## Stage 4 — The starred and contributed repositories

The starred list is signal about what they think is interesting; the contributed-to list is signal about what they think is worth their time. For each notable starred or contributed repo:
- What does the repo do?
- Why might this prospect care about it?
- Does this connect to anything they have publicly written about?

This stage is often where the strongest opener material comes from — a prospect's recent contribution to a tool the writer also uses, with a specific observation about the contribution.

## Stage 5 — Cross-reference

Compare the GitHub picture with the LinkedIn picture:
- Is the technical depth on GitHub consistent with how they describe themselves on LinkedIn?
- Are they an architect (lots of design discussions) or an implementer (lots of code)?
- Does their GitHub focus align with their LinkedIn role description, or has their day-job drifted from where their interests are?

The drift cases are particularly interesting. A VP of Engineering whose GitHub is full of low-level systems work is mentally still a senior engineer; their cold-email response will be different from a VP whose GitHub is silent.

## What to capture

In `research-notes.md` *External trail* > *GitHub*:

- Account URL
- Activity level (daily/weekly/sporadic/dormant)
- Pinned repos (with one-line summary each)
- Recent contributions (last 90 days, by repo)
- Notable starred repos (5-10 max)
- Cross-reference observation (alignment vs. drift with their stated role)

## Sample observations this enables

- *"Their last three commits in the past month are all to their personal SOAR tool — they are still building, not just buying."*
- *"They starred {tool} two weeks before posting publicly about evaluating it; the public post was not the first signal."*
- *"They contribute regularly to {open-source project}, which puts them in close contact with {peer name}, who is on the project's core team."*

## Anti-patterns

- Reading code purely for technical evaluation rather than for prospect insight (this is research, not code review)
- Cherry-picking trivial activity to fake depth
- Confusing organizational accounts with personal accounts (a prospect's company GitHub presence is not the same as their individual technical activity)
- Investing more than 30 minutes per prospect on this playbook (the diminishing returns curve is steep)

## Privacy line

The prospect chose to make this public. Reading public commits is fair. Inferring personal information from non-public-facing repos (forks they own that are private, draft PRs marked WIP) crosses the line — Vendy does not investigate private content even if technically accessible.
