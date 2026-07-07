# Exemplar file format

Every exemplar in `craft/exemplars/` follows this schema.

## Frontmatter

```yaml
---
slug: <slug>
source: <named source — team-win, josh-braun-newsletter, etc.>
source_attribution: <full attribution if from public corpus>
date: <when the email was originally sent or published>
persona_targeted: <ciso | cto | vp-eng | vp-security | head-of-prodsec | other>
service_pitched: <one-liner of what was being sold>
outcome: <what happened — replied, met, closed, etc.>
length_sentences: <integer>
rhetorical_move: <slug — observation, diagnostic, trigger-anchored, peer-recognition, etc.>
register_fit: <which voice-palette mode this most resembles>
tags: [<list>]
---
```

## Body sections

### The email

The full email text, verbatim. Anonymized where needed (names, company names changed; substantive content preserved).

```
Subject: <subject line>

<body>

— <signature>
```

### Why it works

A 4-6 paragraph dissection. Sentence-by-sentence where the structure rewards it. This is the load-bearing section — the dissection is what makes the file useful.

The dissection should answer:
- What does the opener do, and how does it earn the next sentence?
- What rhetorical move is the email executing?
- What does the writer's posture communicate?
- Where does the email take risks, and why do those risks pay off?
- What is the email *not* doing that a worse version would do?

### Anti-patterns it avoids

Concrete, named anti-patterns the email could have stumbled into but didn't. *"This email could have started with 'I came across your profile' but didn't"* — name what was avoided and why the avoidance matters.

### When to reach for this exemplar

Specific prospect-shapes or campaign contexts where this exemplar is calibrating. Examples:
- *"Reach for this when writing to a CISO with a thin LinkedIn footprint and an active regulatory trigger"*
- *"Reach for this when the diagnostic register fits but the prospect rewards lighter touch"*

## Why each section exists

The dissection is the lesson. The frontmatter is what makes the exemplar findable. The "when to reach for this" section is what calibrates Vendy's selection during drafting.

A file with the email but no dissection is just an email. A file with all four parts is an exemplar.
