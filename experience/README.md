# experience/

Vendy's record of doing the work. Episodic memory. The third memory layer alongside `self/` (constitution) and `craft/` (accumulated knowledge).

## Epistemic contract

Files in this directory are **writable by Vendy**. This is where her direct lived experience is recorded — every prospect she has researched, every campaign she has run, every reflection she has written, every diff she has proposed to her own constitution.

## Privacy and PII

`experience/prospects/` contains personal data about real prospects. It is gitignored at the project root. Do not commit or back up this directory through standard project channels. If long-term retention is needed, use a separate, access-controlled backup mechanism with appropriate retention policy.

`experience/journal/`, `experience/campaigns/` (excluding any prospect-identifying inputs), and the structure-only README files in `experience/prospects/` are git-tracked.

## Structure

- **`journal/`** — her introspective record
  - `monthly/` — periodic introspection entries
  - `adhoc/` — triggered reflections after specific sessions
  - `proposed-character-diffs/` — pending changes to `self/character.md` awaiting human approval
  - `applied-character-diffs/` — archived diffs after they have been approved and applied

- **`prospects/`** — per-prospect working memory (gitignored)
  - One folder per researched lead, named by `lead-id`
  - See `prospects/README.md` for the canonical folder shape per prospect

- **`campaigns/`** — per-campaign records
  - One folder per campaign, named by `campaign-id`
  - See `campaigns/README.md` for the canonical folder shape per campaign

## How experience connects to the other layers

When experience accumulates evidence of a generalizable pattern, the pattern can be promoted to `craft/patterns/` via the `promote-pattern` skill. When experience suggests Vendy's constitution should shift, the proposal goes through `journal/proposed-character-diffs/` and the `apply-approved-diff` skill (only after human approval).

The flow of learning is `experience/` → `craft/` for autonomous accumulation, and `experience/` → `self/` only via human-approved proposed diff. The two paths reflect the different epistemic statuses of those layers.
