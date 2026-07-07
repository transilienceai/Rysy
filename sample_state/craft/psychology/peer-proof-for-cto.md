# Peer proof for CTO

Peer proof is a refinement of Cialdini's social proof. The bare claim *other companies use this* triggers nothing. The specific claim *companies at your stage, in your sector, with your specific architectural pattern, are doing X* triggers genuine attention. The difference is *peer-ness* — and CTOs are unusually rigorous about it.

## Why CTOs care about peer-ness specifically

CTOs are professionally responsible for technical decisions that have multi-year consequences. They are aware that what works at one scale fails at another, that what works in one sector is illegal in another, and that what works for a team of 50 fails for a team of 500. They have seen vendor pitches that conflate stages and sectors, and they have learned to discount any claim where peer-ness is unclear.

This means: a generic logo list (*"used by Acme, Initech, and Globex"*) is worse than no social proof at all, because it signals the sender doesn't grasp peer-ness.

## What makes a peer reference actually peer

A peer reference earns its place when it shares with the reader's company:

- **Stage.** Same funding stage, same revenue band, same headcount range
- **Sector.** Same business model and regulatory environment
- **Architectural shape.** Similar stack, similar scale, similar constraints
- **Time horizon.** The peer made the decision recently enough to be relevant

Sharing all four is the gold standard. Sharing three is workable. Sharing two or fewer is not a peer reference; it is a logo.

## How peer proof actually appears in a working email

Compare:

**Bad (logo theatre):** *We work with Stripe, Datadog, and Coinbase.*

**Bad (vague peer claim):** *Companies at your scale are seeing X.*

**Good (real peer proof):** *Two of your peers in the post-Series-D fintech space made the same SOAR-vs-build call in Q1, and the consequences they are seeing six months in are unflattering for the build side. Worth sketching what they ran into if you're at a similar fork.*

The good version names the peer-ness criteria explicitly (stage, sector, decision context), references a specific decision (not a general accomplishment), and offers value (the lesson) before asking.

## The "already deciding this" move

The most powerful peer-proof move is when the writer can credibly say *peers like you are actively deciding this question this quarter*. This works because:

1. It tells the reader they are not alone in facing the decision
2. It implies the writer has visibility into peer behavior the reader does not
3. It anchors the email's reason-for-existing in real industry timing

This move requires real signal. Without real signal, it is a fabricated trend, and CTOs detect it.

## When peer proof backfires

- When the named peer is a competitor the reader resents (the peer reference is then anti-proof)
- When the named peer is so much larger or smaller that the comparison is obviously wrong
- When the *outcome* of the peer's decision is unknown and the writer is hand-waving
- When the writer cannot disclose the peer's name and uses vague stand-ins (*a Series C fintech*) for *every* claim — the vagueness compounds and the email loses credibility

## When *not* to use peer proof at all

Some CTOs — particularly technical co-founders at early-stage companies — actively dismiss peer proof. Their cognitive model is *we are doing it differently for a reason*. Peer-proof outreach to this archetype reads as if the writer is missing the point of their company.

For this archetype, the better moves are:
- First-principles framings (the trade-off itself, not what others are doing)
- Architectural observations (what's true of their stack, regardless of others)
- Direct technical engagement (what would you build to handle X?)

## What the witness checks

For drafts using peer proof, the witness asks:
- Is the peer reference specific enough that the reader recognizes the comparison as fair?
- Does the peer share at least three of {stage, sector, architecture, timing}?
- Is the peer's outcome named, or is it implicit?
- Could the reader reasonably resent the peer being named (competitor, lower-tier company, sworn enemy)?
- Would removing the peer reference and replacing it with a first-principles claim make the email stronger?

The last check is the most important. If the email survives the removal of the peer reference, the peer reference was decoration; if it weakens meaningfully, the peer reference was load-bearing.
