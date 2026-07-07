# Detailed workflow — run-campaign

The happy path is in `SKILL.md`. This file documents every step with edge cases, error handling, and the exact files to read/write at each stage.

## 1. Validate and set up

- Read input JSON; validate against `references/input-schema.md`
- If validation fails, write error report to `experience/campaigns/_errors/{timestamp}.md` and stop
- Generate `campaign-id` from `campaign.id` if present, otherwise `{date}-{slug-of-campaign-name}`
- Create `experience/campaigns/{campaign-id}/`
- Copy input JSON to `experience/campaigns/{campaign-id}/input.json`
- Write human-readable `brief.md` distilling the campaign + sender blocks
- Initialize an empty `output.json` skeleton, an empty `run-log.md`, and an empty `results-summary.md` placeholder

## 2. Trends freshness check

- Read frontmatter of `craft/trends/current.md`
- If timestamp is older than 14 days OR `status: placeholder`:
  - Invoke `refresh-trends` skill
  - Note in run-log: "trends were stale; refreshed before campaign"
- Otherwise note in run-log: "trends were fresh; proceeding"

## 3. Per-lead loop

For each lead in `leads[]`, in order:

### 3a. Set up lead workspace
- Generate or use `lead-id` from input
- Create `experience/prospects/{lead-id}/` if not exists
- Write `brief.md` for the lead with input fields and pre-attached intel

### 3b. Disqualify pre-check
- Check `context.disqualify_signals_check` for any pre-flagged signals from the input
- If a signal is set, mark lead as skipped with reason; append to run-log; continue

### 3c. Research
- Invoke `researcher` sub-agent with the lead brief
- Researcher loads the relevant playbooks from `craft/research-methodology/` based on tier and persona
- Researcher writes `research-notes.md`
- If researcher detects a disqualify signal during work, it writes `disqualify-check.md` and signals skip
- If skip: mark lead skipped; append to run-log; continue

### 3d. Profile
- Invoke `profiler` sub-agent
- Profiler reads research-notes.md, brief.md, and the relevant `craft/personas/{role}.md`
- Profiler writes `psychological-portrait.md`

### 3e. Draft (main thread)
- Read the portrait, the brief, the campaign block, the active trends, the relevant persona file
- Consult `self/voice-palette/` and pick the register
- Optionally read 1-2 exemplars from `craft/exemplars/` matching the persona and rhetorical move
- Optionally consult `craft/cold-email/` for specific architecture cues
- Draft into `drafts/v1.md`

The `pre-write-tell-detector.py` hook fires on this write. If it blocks, rewrite (up to 2 deterministic-block rewrites). If still blocking after 2 attempts, mark as flag for human review.

### 3f. Witness
- After draft is written, the `post-draft-trigger-witness.sh` hook records the event in run-log.md and surfaces a cue
- **Vendy's main thread then explicitly invokes the witness sub-agent on the draft**
- Witness writes `witness-feedback.md` with verdict (ship | rewrite | flag) plus prose
- If verdict = `ship`: copy v1 to `final.md`; proceed to 3g
- If verdict = `rewrite`: read witness's specific direction; produce `drafts/v2.md`; witness re-runs on v2
  - If second verdict = `ship`: copy v2 to `final.md`
  - If second verdict = `rewrite` or `flag`: mark lead as flag (human review required)
- If verdict = `flag`: mark lead as flag (human review required)

### 3g. Note-taking
- After each lead, reflect briefly: did anything in this run change Vendy's understanding?
- If yes, invoke `take-craft-note` with the observation
- If no, no note

### 3h. Append to output
- Append the lead's result to `output.json` (the schema is in `references/output-schema.md`)
- Append timestamped event to `run-log.md`

## 4. Campaign close

- Write `output.json` finalized with all leads
- Write `results-summary.md` with counts (drafted/skipped/flagged) and brief notes on each skip and flag
- Write `what-i-learned.md` reflecting on the campaign's themes
- Invoke `reindex-memory` to refresh INDEX files
- If `craft/notes/` accumulated above threshold (default: 5+ new notes from this campaign), surface a suggestion: *"Worth running /promote-patterns to evaluate them for promotion."*

## Failure modes

- **Input JSON malformed**: stop with error report; no leads processed
- **Researcher times out or returns empty research-notes**: mark lead as flag with reason "research insufficient"
- **Disqualify signal during research**: mark lead as skipped with reason; do not draft
- **Witness consistently rejects across rewrite cycle**: mark as flag; do not loop further
- **Tell-detector blocks repeatedly (2+ times)**: mark as flag; do not loop further
- **Profiler returns thin portrait honestly labelled as thin**: proceed to draft anyway, but witness's bar shifts toward extra scrutiny
- **A sub-agent crashes or returns malformed output**: log to run-log, mark lead as flag, continue with next lead

The skill never silently swallows errors. Every failure is recorded and surfaces as either a flag or a skip in the output.
