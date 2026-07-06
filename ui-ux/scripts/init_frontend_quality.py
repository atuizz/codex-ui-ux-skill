#!/usr/bin/env python3
"""Scaffold frontend quality docs into a project.

Usage:
    python scripts/init_frontend_quality.py --project /path/to/repo
    python scripts/init_frontend_quality.py --project . --docs docs/frontend --force
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil

TEMPLATES = [
    "DESIGN.md",
    "FRONTEND_CONTRACT.md",
    "PAGE_BRIEF.md",
    "FRONTEND_REVIEW.md",
]
AGENTS_MARKER = "Frontend quality governance"


def update_agents_pointer(project: Path, docs_path: str) -> Path:
    agents_path = project / "AGENTS.md"
    normalized_docs = docs_path.replace("\\", "/").strip("/")
    pointer = f"""
## {AGENTS_MARKER}

Before broad frontend UI/UX changes, read:

- `{normalized_docs}/DESIGN.md`
- `{normalized_docs}/FRONTEND_CONTRACT.md`

For new or substantially refactored pages, create or update a `PAGE_BRIEF.md`
near the route/component or under `{normalized_docs}/pages/`. Keep detailed
frontend rules in the frontend docs; do not duplicate long checklists in
`AGENTS.md`.
"""
    existing = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    if AGENTS_MARKER in existing:
        return agents_path
    separator = "\n\n" if existing.strip() else ""
    agents_path.write_text(existing.rstrip() + separator + pointer.strip() + "\n", encoding="utf-8")
    return agents_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold AI frontend design/governance templates.")
    parser.add_argument("--project", required=True, help="Project root to receive docs")
    parser.add_argument("--docs", default="docs/frontend", help="Docs path relative to project root")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument(
        "--update-agents",
        action="store_true",
        help="Append a short frontend governance pointer to AGENTS.md if one is not already present",
    )
    args = parser.parse_args()

    skill_root = Path(__file__).resolve().parents[1]
    templates_dir = skill_root / "templates"
    project = Path(args.project).resolve()
    target = project / args.docs
    target.mkdir(parents=True, exist_ok=True)

    copied = []
    skipped = []
    for name in TEMPLATES:
        src = templates_dir / name
        dest = target / name
        if dest.exists() and not args.force:
            skipped.append(dest)
            continue
        shutil.copyfile(src, dest)
        copied.append(dest)

    print(f"Scaffolded frontend quality docs in: {target}")
    if copied:
        print("Copied:")
        for item in copied:
            print(f"  - {item}")
    if skipped:
        print("Skipped existing files (use --force to overwrite):")
        for item in skipped:
            print(f"  - {item}")
    if args.update_agents:
        agents_path = update_agents_pointer(project, args.docs)
        print(f"AGENTS.md pointer ensured: {agents_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
