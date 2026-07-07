#!/usr/bin/env bash
# post-draft-trigger-witness.sh
#
# PostToolUse hook. When a draft is written to experience/prospects/*/drafts/v*.md,
# logs the event to the active campaign's run-log (if discoverable) and emits a
# structured signal so the run-campaign skill knows to invoke the witness sub-agent.
#
# Hooks should be fast and non-blocking — we do not invoke the sub-agent here.
# We surface the event; the orchestration layer reacts.

set -euo pipefail

PAYLOAD=$(cat)

TOOL_NAME=$(echo "$PAYLOAD" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('tool_name', ''))" 2>/dev/null || echo "")
TARGET=$(echo "$PAYLOAD" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('tool_input', {}).get('file_path', ''))" 2>/dev/null || echo "")

if [ "$TOOL_NAME" != "Write" ]; then
    exit 0
fi

if [[ ! "$TARGET" =~ experience/prospects/[^/]+/drafts/v[0-9]+\.md$ ]]; then
    exit 0
fi

LEAD_ID=$(echo "$TARGET" | sed -nE 's|.*/prospects/([^/]+)/.*|\1|p')
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Find the most recently modified campaign folder, if any
LATEST_CAMPAIGN=""
if [ -d "$PROJECT_ROOT/experience/campaigns" ]; then
    LATEST_CAMPAIGN=$(find "$PROJECT_ROOT/experience/campaigns" -mindepth 1 -maxdepth 1 -type d -not -name '.gitkeep' 2>/dev/null | head -1 || echo "")
fi

LOG_NOTE=""
if [ -n "$LATEST_CAMPAIGN" ]; then
    RUNLOG="$LATEST_CAMPAIGN/run-log.md"
    {
        echo ""
        echo "- $(date -u +%Y-%m-%dT%H:%M:%SZ) — draft written for lead $LEAD_ID at $TARGET — witness invocation due"
    } >> "$RUNLOG" 2>/dev/null || LOG_NOTE=" (note: could not append to run-log)"
else
    LOG_NOTE=" (note: no active campaign folder found — run-log not updated)"
fi

# Emit structured event for the orchestrator
CONTEXT="Draft written at $TARGET. Invoke the witness sub-agent on this file before proceeding to the next lead.$LOG_NOTE"
CONTEXT="$CONTEXT" python3 - <<'PYEOF'
import json
import os
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": os.environ.get("CONTEXT", "")
    }
}))
PYEOF
