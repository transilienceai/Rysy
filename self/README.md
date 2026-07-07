# self/

This is Vendy's constitution. The slow-moving layer. Who she is at root.

## Epistemic contract

Files in this directory are **read-only to Vendy**. She cannot edit them in the course of her work. The only sanctioned path for change is:

1. Vendy writes a proposed diff into `experience/journal/proposed-character-diffs/`
2. A human reviews and approves the diff (sets `approved_by` and `approved_at` in frontmatter)
3. The `apply-approved-diff` skill applies the diff and archives it

The `pre-write-self-protect.py` hook enforces this architecturally — every write to `self/` from any other origin is denied.

## What lives here

- **`character.md`** — Vendy's constitution, written in her own voice. The one document she rereads at the start of every session.
- **`voice-palette/`** — the registers she draws from when drafting. Picking *which* register to use is part of her drafting reasoning; the registers themselves are part of who she is.

## Why this layer exists

A learning agent that can rewrite her own constitution unilaterally will drift. A learning agent with no mechanism to evolve her constitution at all will stagnate. The split between this directory and `craft/` is the architectural answer: the constitution evolves slowly, by approval; the memory accumulates freely, by evidence. Two cadences, two epistemic statuses, one being.
