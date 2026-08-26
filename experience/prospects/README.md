# experience/prospects/

Per-prospect working memory. One folder per researched lead.

## Privacy

This directory contains personal data about real prospects. It is gitignored at the project root. Treat its contents with the privacy posture you would treat any folder of personal data.

## Folder shape per prospect

Each prospect's folder lives at `prospects/{lead-id}/` and contains:

- **`brief.md`** — distilled lead context: name, company, role, campaign assignment, priority tier, any pre-attached intel
- **`research-notes.md`** — output of the `researcher` sub-agent, structured per the schema in `craft/research-methodology/linkedin-deep-read.md`
- **`psychological-portrait.md`** — output of the `profiler` sub-agent: a 3-5 paragraph portrait of the prospect's actual operational reality and what they would respond to
- **`drafts/`** — iterative drafts:
  - `v1.md` — first draft
  - `v2.md` — rewrite if the witness rejected v1
  - (rare) `v1-alternative.md` — for A-tier prospects where Rysy ships an alt version with rationale
- **`witness-feedback.md`** — the witness sub-agent's verdict: ship / rewrite / flag, plus prose explanation
- **`final.md`** — the final draft after witness approval (or the v2 if the second witness pass approved)
- **`disqualify-check.md`** — present only if a disqualify signal was detected; documents the signal and why outreach was declined

## INDEX.md

`prospects/INDEX.md` is rebuilt by `reindex-memory` and contains a searchable table of all prospects: lead-id, persona, industry, campaign, register used, witness verdict, outcome (when known), date.

This index lets Rysy answer questions like *have I emailed anyone in this persona+sector before?* without loading every prospect folder.

## Lifecycle

Prospect folders are created by `run-campaign` at the start of processing a lead. They are not automatically deleted; the audit trail matters. Long-term retention strategy will be revisited in Phase 2 alongside the broader memory architecture.

## Naming conventions

`lead-id` is supplied in the input JSON. If the input does not provide one, `run-campaign` generates one as `{slug-of-name}-{slug-of-company}-{short-hash}` to avoid collisions.
