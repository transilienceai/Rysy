#!/usr/bin/env bash
# subagent-stop-log.sh
#
# SubagentStop hook. Logs each sub-agent return to the active campaign's
# run-log (if one is discoverable). Surfaces a note in stderr if it cannot
# find a campaign to log against.

set -euo pipefail

PAYLOAD=$(cat)

AGENT_NAME=$(echo "$PAYLOAD" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('subagent_name', d.get('agent_name', 'unknown')))" 2>/dev/null || echo "unknown")
DURATION=$(echo "$PAYLOAD" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('duration_ms', 0))" 2>/dev/null || echo "0")
SUMMARY=$(echo "$PAYLOAD" | python3 -c "import sys, json; d=json.load(sys.stdin); s=d.get('summary', d.get('last_message', '')); print(s[:200].replace(chr(10), ' '))" 2>/dev/null || echo "")

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

LATEST_CAMPAIGN=""
if [ -d "$PROJECT_ROOT/experience/campaigns" ]; then
    LATEST_CAMPAIGN=$(find "$PROJECT_ROOT/experience/campaigns" -mindepth 1 -maxdepth 1 -type d -not -name '.gitkeep' 2>/dev/null | head -1 || echo "")
fi

if [ -n "$LATEST_CAMPAIGN" ]; then
    RUNLOG="$LATEST_CAMPAIGN/run-log.md"
    {
        echo ""
        echo "- $(date -u +%Y-%m-%dT%H:%M:%SZ) — sub-agent **$AGENT_NAME** returned (duration: ${DURATION}ms) — $SUMMARY"
    } >> "$RUNLOG" 2>/dev/null || echo "subagent-stop-log: could not append to $RUNLOG" >&2
else
    # No campaign in flight — sub-agent ran outside campaign context (e.g., manual /introspect)
    # This is fine; just don't log to a campaign that doesn't exist
    echo "subagent-stop-log: no active campaign — agent $AGENT_NAME completed in ${DURATION}ms" >&2
fi

exit 0
