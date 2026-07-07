---
description: Run a cold-outreach campaign end-to-end. Reads input JSON, processes each lead through research → profile → draft → witness, writes output JSON.
argument-hint: <path-to-input.json>
---

Run the `run-campaign` skill on the input JSON at the path I'm about to give you.

Path: $ARGUMENTS

Process the campaign per the workflow in `.claude/skills/run-campaign/SKILL.md`. Iterate every lead. Use the researcher → profiler → witness sub-agents around drafting in your main thread. Write the output JSON to `experience/campaigns/{campaign-id}/output.json` and report results when done.

If anything is malformed or missing, surface it before processing — do not proceed with broken input.
