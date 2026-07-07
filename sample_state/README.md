# sample_state/ — a populated snapshot of a running Vendy

This directory is a **frozen snapshot of a real, evolving Vendy instance's memory**, kept
as a reference for what the project looks like after it has actually processed campaigns.

The repo root is a **clean, ready-to-use Vendy**: the full framework and craft library,
but with the `experience/` output directories reset to empty scaffolding. Open the root
in Claude Code and run `/run-campaign` to start fresh.

`sample_state/` is the opposite — the accumulated memory of an instance mid-life:

- `experience/campaigns/` — completed campaign records (input, output, run-logs, reflections)
- `experience/prospects/` — per-lead working memory (research notes, portraits, drafts, witness feedback)
- `experience/journal/` — introspective entries and proposed character diffs
- `craft/` — the library (notes, patterns, exemplars, personas, …) as it stood at snapshot time
- `self/` — the constitution and voice palette at snapshot time

It intentionally does **not** copy the runnable framework (`.claude/`, `CLAUDE.md`,
`tests/`, build scripts). Those live once, in the root. Duplicating `.claude/` here would
also make Claude Code register a second, conflicting set of skills — so this snapshot is
memory only, not a second executable instance.

## ⚠️ Contains real personal data

The prospect and campaign records here hold **real names, work email addresses,
LinkedIn URLs, and psychological profiles of real people**. This is why the repository
is kept **private**. Do not make this repo public, and do not redistribute the contents
of this folder without scrubbing the PII first.

The root instance's `experience/prospects/` is gitignored precisely to avoid committing
this class of data; `sample_state/` is the one deliberate, contained exception, retained
for demonstration inside a private repo.
