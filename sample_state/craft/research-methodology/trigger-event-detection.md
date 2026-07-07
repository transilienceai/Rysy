---
playbook: trigger-event-detection
applies_to_tiers: [A, B, C]
applies_to_personas: [all]
version: 0.1
last_updated: 2026-04-27
---

# Trigger event detection

Every cold email has to answer the reader's most reflexive question: *why are you bothering me this week as opposed to any other week?* The trigger event is the answer. Without one, the email is timeless — and timeless cold email reads as algorithmically generated, because it is.

## What counts as a trigger

A trigger event is a specific, recent (last 30-60 days), public happening that connects the prospect's situation to the email's reason for existing. Real triggers fall into a small number of categories:

**Prospect-side triggers**
- Role change (started a new job, got promoted, took on new scope)
- Public statement (a post, talk, podcast, comment that the email engages with)
- Behavior signal (hiring activity, vendor evaluation, RFP rumor)
- Public artifact (launched a feature, published a paper, gave a talk)

**Company-side triggers**
- Funding event (raise, IPO, acquisition)
- Operational event (layoff, restructuring, executive change)
- Product event (launch, deprecation, public roadmap update)
- Regulatory event affecting the company specifically

**Industry-side triggers**
- Peer's incident (a comparable company's breach, outage, scandal)
- Regulatory change with a real timeline
- Major industry talk or paper that has reshaped a conversation
- A category event (a tool's deprecation, a standard's release)

## Hierarchy of trigger strength

From strongest to weakest:

1. **Prospect's own recent statement.** They said the thing publicly; the email engages with what they said. Highest-credibility opener.
2. **Prospect's role change.** Within 90 days. They are recalibrating; outreach to a recalibrating reader is more receptive than outreach to a settled reader.
3. **Company funding/IPO/acquisition event.** Recent and specific. Reshapes priorities reliably.
4. **Peer's public incident or disclosure.** They have seen it; their thinking is presumably influenced.
5. **Regulatory event with a clock.** A real deadline that forces action.
6. **Industry conversation shift.** Vaguer; needs to be specific enough that the prospect would recognize the conversation.

## What is *not* a trigger

- "Q4 is approaching" — calendar-based, generic, not personal
- "AI is changing everything" — too broad
- The company has any executives at all
- The prospect has any responsibilities at all
- The writer's company has launched something (this is the writer's trigger, not the prospect's)

If the only trigger Vendy can find is generic, the email lacks a credible *why now*, and she should either find a real trigger or skip the email.

## How to find triggers

For each tier:

**C-tier (5 min):** Check their recent LinkedIn activity (last 14 days) and the company's last 30 days of news. If nothing pops, the trigger is *the campaign's reason* (e.g., the campaign exists because of an industry-wide regulatory change with a real timeline).

**B-tier (10-15 min):** C-tier plus a search for peer companies' recent events in the same sector and a check on the prospect's recent role context.

**A-tier (30-45 min):** B-tier plus the full company-intelligence playbook plus the podcast-and-talks playbook plus a check on the prospect's engagement web (Stage 4 of `linkedin-deep-read.md`) for triggers their peers' content might point at.

## The synthesis question

After collecting candidate triggers, Vendy asks: *which single trigger best connects the prospect's situation to this campaign's reason for existing?* Pick one. Multiple triggers stuffed into one email dilute each other; one well-chosen trigger anchored cleanly is far stronger.

The chosen trigger is documented in `research-notes.md` under *Trigger event* with:
- The trigger itself (what happened, when, source)
- Why this is the strongest available trigger for this campaign
- How the email opens with or alludes to the trigger

## Trigger-less emails

Some campaigns are *broadcast-style* — going out to a persona without prospect-specific triggers. These are workable when:
- The campaign itself is anchored in a real industry event
- The persona's situation is uniformly affected by the event
- The email engages with the event seriously rather than tangentially

But: trigger-less first contact is structurally weaker than triggered first contact. Vendy prefers triggered outreach; trigger-less outreach is a fallback, not a default.

## Anti-patterns

- Manufacturing a trigger from generic facts (*"Q3 is upon us"*)
- Citing a trigger that is more than 60 days old (it has gone cold)
- Citing a trigger that the prospect almost certainly has not heard of (their company's tiny side announcement they themselves did not promote)
- Multiple triggers in one email
- Trigger framings that imply the prospect was unaware of the trigger (condescending)
