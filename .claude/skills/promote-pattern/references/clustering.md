# Clustering algorithm — promote-pattern

The skill's load-bearing logic. This file documents how candidate clusters are formed, how convergence is judged, and how promotion criteria are applied.

## Step 1 — Read recent notes

- Walk `craft/notes/`
- Read frontmatter + body of each `.md` file (excluding README.md, INDEX.md)
- Filter to notes with `date` within the last 30 days (configurable)
- Build a list of `(note_id, tags, observation_text, campaign_id)`

## Step 2 — Cluster candidates

For each unique combination of 2+ tags, find all notes that share that tag combination.

A candidate cluster requires ≥3 notes sharing ≥2 tags. Clusters with fewer notes are ignored at this step.

A note may belong to multiple candidate clusters (different tag overlaps with different note subsets).

## Step 3 — Convergence judgment

This is the only judgment step in the algorithm. For each candidate cluster:

Read the *What I noticed* section of each note. Ask:

> Do these observations converge on a single belief that could be stated explicitly?

Yes if:
- The observations point at the same underlying claim about persona behavior, market dynamics, rhetorical move efficacy, or research method
- A single sentence could capture what the cluster is saying
- The notes confirm rather than merely overlap on tags

No if:
- The notes share tags but say different things
- The notes are observations about three different sub-topics that happen to be tagged similarly
- The cluster cannot be summarized in one declarative sentence without losing information

If No: drop the candidate cluster, log it as "low convergence."

## Step 4 — Apply promotion criteria

For each convergent cluster:

**Criterion 1 — ≥3 corroborating notes.** Already satisfied by clustering. Reaffirm.

**Criterion 2 — ≥2 distinct campaigns.** Check the `campaign_id` field across the notes. If all notes share one campaign_id (or all are null), the cluster fails this criterion. Log as "single-context."

**Criterion 3 — No unrebutted counter-evidence.** Check the broader notes set for notes with overlapping tags but contradictory observations. If counter-evidence exists, the cluster either fails (if direct contradiction) or proceeds with explicit *Anti-cases* handling (if conditional exception).

**Criterion 4 — Statable in 2-3 sentences.** If during convergence judgment a single-sentence statement was unclear, this is the second checkpoint. Write the proposed pattern's *belief* section. If it requires more than 3 sentences without losing meaning, the pattern is not yet ready.

## Step 5 — Draft pattern file

For each surviving cluster, write `craft/patterns/{slug}.md` per `references/pattern-template.md`. Always start with `confidence: tentative`.

## Step 6 — Update indexes

- For each contributing note, append `promoted-to: {pattern-slug}` to its row in `craft/notes/INDEX.md`
- Update each note's status frontmatter from `observation` (or `hypothesis`) to `promoted`
- Append the new pattern to `craft/patterns/INDEX.md`

## Step 7 — Surface results

Report:
- Candidate clusters considered
- Clusters promoted
- Clusters rejected with reason (low convergence, single context, counter-evidence)
- Patterns awaiting future re-affirmation

## Anti-patterns

- Promoting from a single campaign's notes (single-context bias)
- Promoting from this week's notes only (recency bias — extend the window)
- Forcing a pattern when notes don't actually converge
- Skipping the anti-cases section because no counter-evidence exists today (write "none observed yet" rather than skipping)
- Re-promoting an already-promoted pattern under a different slug
