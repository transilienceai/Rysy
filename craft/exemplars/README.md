# craft/exemplars/

Gold-standard cold emails with dissection. Real examples of the work done well.

## What an exemplar is

An exemplar is a real cold email — anonymized where appropriate — that demonstrably worked, accompanied by a careful dissection of *why*. The dissection is what makes the file useful. The email itself is just the artifact; the dissection is the lesson.

## Where exemplars come from

Two sources:

**Your team's wins.** Past cold emails sent by your team that received replies from senior buyers. You provide these (with consent and anonymization where needed). The dissection captures what your team's collective taste recognizes as the strong moves.

**Public craft corpus.** Emails published on cold-email-craft sources — Josh Braun's *Bad Cold Email of the Day* dissections (the good ones), Becc Holland's breakdowns, threads on r/sales where exemplars are shared with consent, books that publish real examples (*The Cold Email Manifesto*, etc.). Provenance is always credited in the file's frontmatter.

Exemplars are *not* synthesized. Rysy does not write fake exemplars. They have to be real.

## How exemplars are used

Before drafting, Rysy queries `craft/exemplars/INDEX.md` for exemplars matching the persona and rhetorical move she is considering, reads two or three of them, and uses them as *tuning forks* — to calibrate her standards, not to copy phrases.

Exemplars are *not* templates. The discipline is to read them and absorb what is true about them, then write something different but held to the same standard.

## Format

Each exemplar lives at `craft/exemplars/{slug}.md` and follows the schema in `format.md`.

## What does *not* belong here

- Made-up emails Rysy thinks would work
- Aggregated patterns abstracted from multiple emails (those go in `craft/cold-email/`)
- Emails of unknown provenance (we need to know they actually worked, against whom, and why)

## Initial state

This directory is initially empty. The format is defined in `format.md`. Seed the directory by:

1. Curating 5-10 of your team's best past cold emails (or asking Rysy to write the dissection sections after you provide the raw emails)
2. Selecting 5-10 from public craft sources (with attribution)

Phase 1 can run with as few as 5 exemplars. Aim for 15-20 within the first month of operation.
