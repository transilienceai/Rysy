# craft/

Vendy's library — what she has learned about the work. The accumulating layer.

## Epistemic contract

Files in this directory are **writable by Vendy**. She extends the library as she works. This is the layer where her learning lives. Patterns get promoted from observation to belief here, autonomously, by evidence.

Promotion criteria — for any file moving from observation to a more durable belief — require explicit evidence pointers back to source notes. See `patterns/README.md` for the formal criteria.

## Structure

- **`canon/`** — the lineage. Seeded thinkers whose contributions Vendy stands on. Mostly read-only; she can extend it but rarely revises seeded entries.
- **`exemplars/`** — gold-standard cold emails with dissection. Real examples of the work done well.
- **`anti-canon/`** — bad cold emails with dissection. Real examples of the work done badly. What she is avoiding, made concrete.
- **`personas/`** — buyer archetypes she writes to. Seeded from the team's ABM doc; extended over time.
- **`psychology/`** — persuasion frameworks per persona. How Cialdini-style frames apply specifically to a CISO vs. a CTO.
- **`research-methodology/`** — playbooks the researcher sub-agent loads before each run. How she actually does LinkedIn deep-reads, web discovery, GitHub mining, podcast trails, company intelligence, trigger-event detection, and tier-depth scoping.
- **`cold-email/`** — her internalized knowledge of the form. Openers, subjects, CTAs, tells to avoid, opening architectures.
- **`notes/`** — atomic dated observations. Her zettelkasten. One observation per file.
- **`patterns/`** — observations promoted to belief, with evidence. The next layer up from notes.
- **`trends/`** — rolling market context. Refreshed periodically by the `refresh-trends` skill.
- **`open-questions.md`** — hypotheses she is testing, things she has noticed but not yet promoted.

## How she navigates

`INDEX.md` (auto-rebuilt by the `reindex-memory` skill) is the entry point. From there, Vendy reads what is relevant to the task at hand. She does not load the entire library every session — she reaches for what fits.

## What does *not* live here

Her constitution, voice palette, and the registers themselves live in `self/`. Specific prospect research, drafts, and campaign records live in `experience/`. Agent definitions, skills, hooks, and configuration live in `.claude/`.
