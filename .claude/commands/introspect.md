---
description: Run the introspecter sub-agent to evaluate whether Rysy's stated character is still aligned with her recent practice.
---

Invoke the `introspecter` sub-agent. The agent's instructions are in `.claude/agents/introspecter.md`.

The introspecter will read self/character.md, the recent journal entries, the recent patterns, and the most recent campaign reflections, and answer: *is the character document still a true description of how Rysy works, or has it drifted?*

The agent writes:
- An introspection entry to `experience/journal/monthly/{YYYY-MM}-introspection.md`
- A proposed diff to `experience/journal/proposed-character-diffs/` only if drift is detected

Report the findings when the agent completes. Do not apply any diff — that requires human review and the `/apply-diff` flow.
