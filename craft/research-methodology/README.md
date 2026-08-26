# craft/research-methodology/

The playbooks the researcher sub-agent loads before each research run. These files are the operational doctrine for *how* Rysy researches. Without them, the researcher would improvise differently every time and the quality of research would drift.

## How playbooks are used

When the researcher sub-agent is invoked by the `run-campaign` skill, its system prompt instructs it to first load the relevant playbooks for the tier and persona of the current lead. The researcher then follows the protocols in those playbooks rather than relying on the agent's own judgment about what to do next. This makes research *consistent and reproducible*, two properties that matter when downstream profiling depends on the research's shape.

## The playbooks

- `linkedin-deep-read.md` — the canonical LinkedIn protocol for prospect research
- `web-discovery.md` — going beyond LinkedIn to find the prospect's broader public footprint
- `github-and-code-mining.md` — for technical buyers, finding their public repos and engagement
- `podcast-and-talks.md` — discovering and reading their talk and podcast appearances
- `company-intelligence.md` — the company-side research, not just the prospect-side
- `trigger-event-detection.md` — the cross-cutting "why now" methodology
- `tier-depth-guide.md` — what A/B/C-tier research scope actually means in practice

## How playbooks evolve

Each playbook's frontmatter declares the tier scopes it applies to and the version. As Rysy works, she takes craft notes about research moves that landed (or failed). When evidence accumulates that a playbook should change — a new search pattern that catches what others miss, a stage of LinkedIn research that has become unproductive — the playbook can be revised through the standard pattern-promotion path.

The research methodology is *not* part of the constitution; it is craft. It evolves as the platforms, personas, and prospect behaviors evolve. LinkedIn's UI changes, search engines change, what senior buyers post changes, and the playbooks should change with them.

## What the researcher returns

After running the playbooks for a lead, the researcher writes `experience/prospects/{lead-id}/research-notes.md` in a consistent format defined in `linkedin-deep-read.md` (which carries the canonical schema). Other playbooks contribute sections to this file but do not redefine its overall shape.
