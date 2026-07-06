#!/usr/bin/env python3
"""Package the installable ui-ux skill bundle as a .skill archive.

The archive intentionally contains only the `ui-ux/` skill directory, not the
repository-level open-source docs.

Usage:
    python -S scripts/package_skill.py
    python -S scripts/package_skill.py --output-dir /tmp/release
"""
from __future__ import annotations

import argparse
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SKILL = ROOT / "ui-ux"
DEFAULT_VERSION_FILE = ROOT / "VERSION"
FIXED_ZIP_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def read_version(version_file: Path) -> str:
    version = version_file.read_text(encoding="utf-8").strip()
    if not version:
        raise ValueError(f"Version file is empty: {version_file}")
    return version


def should_include(path: Path) -> bool:
    if path.name == "__pycache__":
        return False
    if path.suffix in {".pyc", ".pyo"}:
        return False
    return True


def add_file(zipf: zipfile.ZipFile, source: Path, arcname: str) -> None:
    info = zipfile.ZipInfo(arcname.replace("\\", "/"))
    info.date_time = FIXED_ZIP_TIMESTAMP
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    zipf.writestr(info, source.read_bytes())


def package_skill(skill_dir: Path, output_dir: Path, name: str, version: str) -> Path:
    if not skill_dir.is_dir():
        raise FileNotFoundError(f"Skill directory not found: {skill_dir}")
    if not (skill_dir / "SKILL.md").is_file():
        raise FileNotFoundError(f"Skill directory is missing SKILL.md: {skill_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    archive = output_dir / f"{name}-{version}.skill"

    with zipfile.ZipFile(archive, "w") as zipf:
        for path in sorted(skill_dir.rglob("*")):
            if not should_include(path):
                continue
            if path.is_file():
                rel = path.relative_to(skill_dir.parent).as_posix()
                add_file(zipf, path, rel)

    return archive


def main() -> int:
    parser = argparse.ArgumentParser(description="Package the ui-ux Codex skill.")
    parser.add_argument("--skill-dir", default=str(DEFAULT_SKILL), help="Path to the installable skill directory")
    parser.add_argument("--output-dir", default=str(ROOT / "dist"), help="Directory for the .skill archive")
    parser.add_argument("--name", default="ui-ux", help="Archive base name")
    parser.add_argument("--version", default=None, help="Version string; defaults to VERSION file")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    version = args.version or read_version(DEFAULT_VERSION_FILE)

    archive = package_skill(skill_dir=skill_dir, output_dir=output_dir, name=args.name, version=version)
    print(f"Created: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
