#!/usr/bin/env python3
"""
pre-write-tell-detector.py

PreToolUse hook. Scans Write/Edit operations targeting draft files and
final.md files for known AI tells (from .claude/lib/ai_tells.py).

Smart-quote normalization: Curly apostrophes and quotes are folded to
their straight ASCII equivalents before matching, so phrases like
"I'll follow up" are caught regardless of which apostrophe is used.
"""

import json
import sys
import os
import re


# Curly-to-straight normalization for matching
SMART_QUOTE_MAP = {
    "‘": "'",  # left single quote
    "’": "'",  # right single quote / apostrophe
    "“": '"',  # left double quote
    "”": '"',  # right double quote
    "–": "-",  # en dash
    "—": "-",  # em dash (also normalize — for matching)
}


def normalize(text):
    out = text
    for src, dst in SMART_QUOTE_MAP.items():
        out = out.replace(src, dst)
    return out.lower()


def find_tells(text, hard_blocks):
    text_n = normalize(text)
    hits = []
    for phrase in hard_blocks:
        phrase_n = normalize(phrase)
        pos = text_n.find(phrase_n)
        if pos != -1:
            hits.append((phrase, pos))
    return hits


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = payload.get("tool_name", "")
    tool_input = payload.get("tool_input", {})

    if tool_name not in ("Write", "Edit", "MultiEdit"):
        sys.exit(0)

    target = tool_input.get("file_path", "")

    is_draft = bool(re.search(r"experience/prospects/[^/]+/drafts/v\d+\.md$", target))
    is_final = bool(re.search(r"experience/prospects/[^/]+/final\.md$", target))

    if not (is_draft or is_final):
        sys.exit(0)

    if tool_name == "Write":
        content = tool_input.get("content", "")
    elif tool_name == "Edit":
        content = tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        content = "\n".join(e.get("new_string", "") for e in edits)
    else:
        content = ""

    project_root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    lib_dir = os.path.join(project_root, ".claude", "lib")
    sys.path.insert(0, lib_dir)
    try:
        from ai_tells import HARD_BLOCKS  # type: ignore
    except Exception as e:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"tell-detector: could not load ai_tells.py ({e})"
            }
        }))
        return

    hits = find_tells(content, HARD_BLOCKS)

    if not hits:
        sys.exit(0)

    hits_summary = ", ".join(f'"{phrase}"' for phrase, _ in hits[:5])
    if len(hits) > 5:
        hits_summary += f", and {len(hits) - 5} more"

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"AI-tell detector blocked this write. Found hard-blocked phrase(s): "
                f"{hits_summary}. These are documented in "
                f"craft/cold-email/ai-tells-graveyard.md. Rewrite without them."
            )
        }
    }))


if __name__ == "__main__":
    main()
