# Anti-canon file format

Mirrors `craft/exemplars/format.md` with these adjustments:

## Frontmatter

```yaml
---
slug: <slug>
source: <where the email came from>
source_attribution: <attribution if from public dissection>
date: <when the email was sent or published>
persona_targeted: <persona>
service_pitched: <one-liner>
outcome: <what failed — ignored, marked spam, replied-with-rejection, etc.>
length_sentences: <integer>
primary_failure: <single-phrase summary — e.g., "manufactured-urgency", "fake-personalization", "vague-cta">
secondary_failures: [<list>]
tags: [<list>]
---
```

## Body sections

### The email

The full email verbatim, anonymized.

```
Subject: <subject line>

<body>

— <signature>
```

### Why it fails

A 4-6 paragraph dissection. The mirror of the exemplar section. The dissection should answer:
- What does the opener fail to do?
- Where is the writer's posture wrong?
- What signal of effort was missing?
- What did the writer *not* know about the reader that the email reveals?
- What pattern of failure does this exemplify?

### What the writer probably thought they were doing

This section is unique to anti-canon. It captures the *intent* behind the failure — what the writer thought was good practice, where they got the misimpression, why this failure pattern is structurally common. Naming the intent is what makes anti-canon educational rather than just mocking.

### How a working version would have looked

A short paragraph: if the writer had real signal and a peer-posture, what would the email have looked like? Not a full rewrite — just the *shape* of the corrected version.

### Tags

Tag the failure type (manufactured-urgency, fake-personalization, vague-cta, vendor-posture, AI-tell-pattern, etc.) so anti-canon can be queried by failure mode.

## Why this format

The anti-canon entry teaches by negative example, but only if the failure is *named precisely* and the *correct alternative is sketched*. Anti-canon entries that just dump a bad email without dissection are unproductive — they mock without teaching.
