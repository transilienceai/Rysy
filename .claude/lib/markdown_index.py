"""
markdown_index.py

Utilities for building INDEX.md files across the library. Used by the
reindex-memory skill.

Markdown-only indexing — no embeddings, no vector search. Fast, transparent,
debuggable.

Index builders implemented:
- craft/INDEX.md (top-level navigation + recent activity)
- craft/notes/INDEX.md
- craft/patterns/INDEX.md
- craft/canon/INDEX.md
- craft/exemplars/INDEX.md
- craft/anti-canon/INDEX.md
- experience/prospects/INDEX.md
- experience/campaigns/INDEX.md
"""

import os
import re
from pathlib import Path
from datetime import datetime


# ===== Frontmatter parsing =====

def parse_frontmatter(path: Path) -> dict:
    """Parse YAML-style frontmatter from a markdown file. Lightweight."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return {}
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    raw = parts[1]
    out = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1]
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            if inner:
                value = [x.strip().strip('"\'') for x in inner.split(",")]
            else:
                value = []
        out[key] = value
    return out


def first_paragraph(path: Path) -> str:
    """Return the first non-frontmatter paragraph from a markdown file."""
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return ""
    if text.startswith("---"):
        parts = text.split("---", 2)
        text = parts[2] if len(parts) >= 3 else text
    text = text.strip()
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    for p in paras:
        if not p.startswith("#"):
            return p.split("\n")[0][:200]
    return ""


def _normalize_date(value):
    """Return YYYY-MM-DD if value is ISO-8601 with time; else passthrough string."""
    if isinstance(value, str) and "T" in value:
        return value.split("T")[0]
    return value or ""


def _stringify(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value or "")


def _md_files(directory: Path):
    """Return non-INDEX, non-README markdown files in a directory."""
    return sorted(
        p for p in directory.glob("*.md")
        if p.name not in ("README.md", "INDEX.md", "format.md")
    )


# ===== Index builders =====

def build_notes_index(notes_dir: Path) -> str:
    rows = []
    for p in _md_files(notes_dir):
        fm = parse_frontmatter(p)
        rows.append("| {date} | {slug} | {tags} | {status} | {promoted} |".format(
            date=_normalize_date(fm.get("date", "")),
            slug=p.stem,
            tags=_stringify(fm.get("tags", [])),
            status=fm.get("status", ""),
            promoted=fm.get("promoted_to", "—"),
        ))

    out = [
        "# Notes index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill. Do not edit by hand.",
        "",
        "| Date | Slug | Tags | Status | Promoted to |",
        "|------|------|------|--------|-------------|",
    ]
    out.extend(rows or ["| *(empty — no notes yet)* | | | | |"])
    return "\n".join(out) + "\n"


def build_patterns_index(patterns_dir: Path) -> str:
    rows = []
    for p in _md_files(patterns_dir):
        fm = parse_frontmatter(p)
        rows.append("| {slug} | {promoted} | {confidence} | {status} | {reaffirmed} |".format(
            slug=p.stem,
            promoted=_normalize_date(fm.get("promoted", "")),
            confidence=fm.get("confidence", ""),
            status=fm.get("status", ""),
            reaffirmed=_normalize_date(fm.get("last_reaffirmed", "")),
        ))

    out = [
        "# Patterns index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill.",
        "",
        "| Slug | Promoted | Confidence | Status | Last Reaffirmed |",
        "|------|----------|------------|--------|-----------------|",
    ]
    out.extend(rows or ["| *(empty — no patterns yet)* | | | | |"])
    return "\n".join(out) + "\n"


def build_canon_index(canon_dir: Path) -> str:
    rows = []
    for p in _md_files(canon_dir):
        para = first_paragraph(p)
        rows.append(f"| {p.stem} | {para[:140]}... |")

    out = [
        "# Canon index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill.",
        "",
        "| Slug | Description |",
        "|------|-------------|",
    ]
    out.extend(rows or ["| *(empty)* | |"])
    return "\n".join(out) + "\n"


def build_exemplars_index(exemplars_dir: Path) -> str:
    """Used by the drafter to query exemplars by persona + rhetorical move."""
    rows = []
    for p in _md_files(exemplars_dir):
        fm = parse_frontmatter(p)
        rows.append("| {slug} | {persona} | {move} | {register} | {source} |".format(
            slug=p.stem,
            persona=fm.get("persona_targeted", ""),
            move=fm.get("rhetorical_move", ""),
            register=fm.get("register_fit", ""),
            source=fm.get("source", ""),
        ))

    out = [
        "# Exemplars index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill. Used by the drafter to query exemplars by persona + rhetorical move.",
        "",
        "| Slug | Persona | Rhetorical move | Register | Source |",
        "|------|---------|-----------------|----------|--------|",
    ]
    out.extend(rows or ["| *(empty — seed exemplars from team wins or curated public corpus)* | | | | |"])
    return "\n".join(out) + "\n"


def build_anti_canon_index(anti_canon_dir: Path) -> str:
    """Used by the witness for anti-canon lookups when a draft is borderline."""
    rows = []
    for p in _md_files(anti_canon_dir):
        fm = parse_frontmatter(p)
        rows.append("| {slug} | {failure} | {persona} | {source} |".format(
            slug=p.stem,
            failure=fm.get("primary_failure", ""),
            persona=fm.get("persona_targeted", ""),
            source=fm.get("source", ""),
        ))

    out = [
        "# Anti-canon index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill. Used by the witness for anti-canon lookups.",
        "",
        "| Slug | Primary failure | Persona targeted | Source |",
        "|------|-----------------|------------------|--------|",
    ]
    out.extend(rows or ["| *(empty — seed from real bad cold emails with dissection)* | | | |"])
    return "\n".join(out) + "\n"


def _read_witness_verdict(prospect_dir: Path) -> str:
    """Read just the verdict line from witness-feedback.md if present."""
    f = prospect_dir / "witness-feedback.md"
    if not f.exists():
        return ""
    try:
        text = f.read_text(encoding="utf-8")
    except Exception:
        return ""
    m = re.search(r"\*\*Verdict\*\*:\s*(\w+)", text, re.IGNORECASE)
    return m.group(1).lower() if m else ""


def build_prospects_index(prospects_dir: Path) -> str:
    """Searchable index across all per-prospect folders."""
    rows = []
    for prospect_dir in sorted(p for p in prospects_dir.iterdir() if p.is_dir()):
        brief_path = prospect_dir / "brief.md"
        fm = parse_frontmatter(brief_path) if brief_path.exists() else {}
        verdict = _read_witness_verdict(prospect_dir)
        rows.append("| {lead_id} | {persona} | {industry} | {campaign} | {verdict} | {date} |".format(
            lead_id=prospect_dir.name,
            persona=fm.get("persona", fm.get("role", "")),
            industry=fm.get("industry", ""),
            campaign=fm.get("campaign_id", ""),
            verdict=verdict or "—",
            date=_normalize_date(fm.get("date", fm.get("created", ""))),
        ))

    out = [
        "# Prospects index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill. Lets Rysy answer 'have I emailed anyone like this before' without loading every folder.",
        "",
        "| Lead ID | Persona | Industry | Campaign | Witness verdict | Date |",
        "|---------|---------|----------|----------|-----------------|------|",
    ]
    out.extend(rows or ["| *(empty — no prospects researched yet)* | | | | | |"])
    return "\n".join(out) + "\n"


def _read_campaign_summary(campaign_dir: Path) -> dict:
    """Extract summary stats from output.json or results-summary.md if present."""
    summary = {"drafted": "—", "skipped": "—", "flagged": "—", "total": "—"}
    output_json = campaign_dir / "output.json"
    if output_json.exists():
        try:
            import json
            data = json.loads(output_json.read_text(encoding="utf-8"))
            s = data.get("summary", {})
            summary["drafted"] = str(s.get("drafted", "—"))
            summary["skipped"] = str(s.get("skipped", "—"))
            summary["flagged"] = str(s.get("flagged", "—"))
            summary["total"] = str(s.get("total_leads", "—"))
        except Exception:
            pass
    return summary


def build_campaigns_index(campaigns_dir: Path) -> str:
    rows = []
    for campaign_dir in sorted(p for p in campaigns_dir.iterdir() if p.is_dir()):
        brief_path = campaign_dir / "brief.md"
        fm = parse_frontmatter(brief_path) if brief_path.exists() else {}
        summary = _read_campaign_summary(campaign_dir)
        rows.append("| {cid} | {date} | {sender} | {service} | {total} | {drafted} | {skipped} | {flagged} |".format(
            cid=campaign_dir.name,
            date=_normalize_date(fm.get("date", "")),
            sender=fm.get("sender", ""),
            service=fm.get("service_line", ""),
            total=summary["total"],
            drafted=summary["drafted"],
            skipped=summary["skipped"],
            flagged=summary["flagged"],
        ))

    out = [
        "# Campaigns index",
        "",
        "Auto-rebuilt by the `reindex-memory` skill.",
        "",
        "| Campaign ID | Date | Sender | Service line | Total | Drafted | Skipped | Flagged |",
        "|-------------|------|--------|--------------|-------|---------|---------|---------|",
    ]
    out.extend(rows or ["| *(empty — no campaigns run yet)* | | | | | | | |"])
    return "\n".join(out) + "\n"


def build_craft_top_index(project_root: Path) -> str:
    """Top-level navigation across the library plus recent-activity summary."""
    notes_dir = project_root / "craft" / "notes"
    patterns_dir = project_root / "craft" / "patterns"
    trends_current = project_root / "craft" / "trends" / "current.md"

    notes_count = len(_md_files(notes_dir)) if notes_dir.exists() else 0
    patterns_count = len(_md_files(patterns_dir)) if patterns_dir.exists() else 0

    trends_status = "never"
    if trends_current.exists():
        fm = parse_frontmatter(trends_current)
        ts = fm.get("timestamp", "")
        status = fm.get("status", "")
        if status == "placeholder":
            trends_status = "placeholder (run `/refresh-trends`)"
        elif ts:
            trends_status = _normalize_date(ts)

    today = datetime.utcnow().strftime("%Y-%m-%d")

    body = f"""# craft/ INDEX

Auto-rebuilt by the `reindex-memory` skill. Top-level navigation across the library.

## Layers

- [`canon/`](./canon/) — the lineage; thinkers Rysy stands on
- [`exemplars/`](./exemplars/) — gold-standard cold emails with dissection
- [`anti-canon/`](./anti-canon/) — bad emails dissected; what she's avoiding
- [`personas/`](./personas/) — buyer archetypes she writes to
- [`psychology/`](./psychology/) — persuasion frameworks per persona
- [`research-methodology/`](./research-methodology/) — playbooks the researcher loads
- [`cold-email/`](./cold-email/) — internalized knowledge of the form
- [`notes/`](./notes/) — atomic dated observations
- [`patterns/`](./patterns/) — observations promoted to belief, with evidence
- [`trends/`](./trends/) — rolling market context
- [`open-questions.md`](./open-questions.md) — hypotheses she is testing

## Recent activity

- Notes total: {notes_count}
- Patterns total: {patterns_count}
- Last trends refresh: {trends_status}
- Last reindex: {today}
"""
    return body


# ===== Entry points =====

def write_index(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def reindex_all(project_root: Path) -> dict:
    """Run all index rebuilds. Returns counts per directory."""
    counts = {}
    skipped = []

    targets = [
        ("notes", project_root / "craft" / "notes", build_notes_index),
        ("patterns", project_root / "craft" / "patterns", build_patterns_index),
        ("canon", project_root / "craft" / "canon", build_canon_index),
        ("exemplars", project_root / "craft" / "exemplars", build_exemplars_index),
        ("anti-canon", project_root / "craft" / "anti-canon", build_anti_canon_index),
        ("prospects", project_root / "experience" / "prospects", build_prospects_index),
        ("campaigns", project_root / "experience" / "campaigns", build_campaigns_index),
    ]

    for name, directory, builder in targets:
        if not directory.exists():
            skipped.append(name)
            continue
        write_index(directory / "INDEX.md", builder(directory))
        counts[name] = len(_md_files(directory))

    # Top-level craft INDEX
    craft_dir = project_root / "craft"
    if craft_dir.exists():
        write_index(craft_dir / "INDEX.md", build_craft_top_index(project_root))
        counts["craft_top"] = 1

    return {"counts": counts, "skipped": skipped}


if __name__ == "__main__":
    import sys
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    result = reindex_all(root)
    print(f"Reindexed: {result['counts']}")
    if result['skipped']:
        print(f"Skipped (directory missing): {result['skipped']}")
