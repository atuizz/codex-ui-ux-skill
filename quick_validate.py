#!/usr/bin/env python3
"""Validate the local Codex `ui-ux` skill before installing it globally.

Run from the repository root:

    python -S quick_validate.py

`-S` is intentional: it avoids user-site Python startup issues and keeps this
validator focused on the skill files themselves.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SKILL = ROOT / "ui-ux"
SKILL_MD = SKILL / "SKILL.md"

REQUIRED_REFERENCES = {
    "anti-patterns.md",
    "design-reference-packs.md",
    "development-guardrails.md",
    "project-cognition.md",
    "tool-selection.md",
    "ux-evaluation.md",
    "workflow.md",
}

REQUIRED_TEMPLATES = {
    "DESIGN.md",
    "FRONTEND_CONTRACT.md",
    "FRONTEND_REVIEW.md",
    "PAGE_BRIEF.md",
}

REQUIRED_PROJECT_FILES = {
    "README.md",
    "README.zh-CN.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    ".gitignore",
    ".editorconfig",
    ".gitattributes",
    "PROJECT.md",
    "VERSION",
}

REQUIRED_DOCS = {
    "BENCHMARK_TEMPLATE.md",
    "EVALUATION.md",
    "MAINTAINER_GUIDE.md",
    "RELEASE_CHECKLIST.md",
    "OPEN_SOURCE_MATURITY.md",
    "ROADMAP.md",
}

REQUIRED_GITHUB_FILES = {
    ".github/workflows/validate.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def ok(self, condition: bool, message: str) -> None:
        if not condition:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        if not condition:
            self.warnings.append(message)


def read_text(path: Path, report: Report) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        report.errors.append(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")
    except FileNotFoundError:
        report.errors.append(f"Missing file: {path.relative_to(ROOT)}")
    return ""


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        result[key.strip()] = value
    return result


def validate_structure(report: Report) -> None:
    report.ok(SKILL.is_dir(), "Missing skill directory: ui-ux/")
    report.ok(SKILL_MD.is_file(), "Missing ui-ux/SKILL.md")
    report.ok((SKILL / "references").is_dir(), "Missing ui-ux/references/")
    report.ok((SKILL / "templates").is_dir(), "Missing ui-ux/templates/")
    report.ok((SKILL / "scripts").is_dir(), "Missing ui-ux/scripts/")
    report.ok((SKILL / "evals").is_dir(), "Missing ui-ux/evals/")

    reference_names = {p.name for p in (SKILL / "references").glob("*.md")}
    template_names = {p.name for p in (SKILL / "templates").glob("*.md")}
    report.ok(REQUIRED_REFERENCES <= reference_names, f"Missing reference files: {sorted(REQUIRED_REFERENCES - reference_names)}")
    report.ok(REQUIRED_TEMPLATES <= template_names, f"Missing template files: {sorted(REQUIRED_TEMPLATES - template_names)}")
    report.ok((SKILL / "scripts" / "init_frontend_quality.py").is_file(), "Missing scripts/init_frontend_quality.py")

    junk = [
        p.relative_to(ROOT).as_posix()
        for p in SKILL.rglob("*")
        if p.name == "__pycache__" or p.suffix in {".pyc", ".pyo"}
    ]
    report.ok(not junk, f"Compiled/cache artifacts should not be committed inside the skill: {junk}")

    extra_docs = [
        p.relative_to(ROOT).as_posix()
        for p in SKILL.iterdir()
        if p.is_file() and p.name.lower() in {"readme.md", "changelog.md", "todo.md"}
    ]
    report.ok(not extra_docs, f"Keep skill root lean; move extra docs outside the skill: {extra_docs}")


def validate_open_source_hygiene(report: Report) -> None:
    for rel in sorted(REQUIRED_PROJECT_FILES):
        report.ok((ROOT / rel).is_file(), f"Missing root open-source project file: {rel}")

    for name in sorted(REQUIRED_DOCS):
        report.ok((ROOT / "docs" / name).is_file(), f"Missing maintainer doc: docs/{name}")

    for rel in sorted(REQUIRED_GITHUB_FILES):
        report.ok((ROOT / rel).is_file(), f"Missing GitHub community/CI file: {rel}")

    readme = read_text(ROOT / "README.md", report)
    for marker in [
        "## What this skill is for",
        "## Install locally",
        "## Validate before every change",
        "## Evaluation assets",
        "## Security",
        "## License",
    ]:
        report.ok(marker in readme, f"README.md missing section: {marker}")

    readme_zh = read_text(ROOT / "README.zh-CN.md", report)
    for marker in [
        "**语言：**",
        "## 为什么需要它",
        "## 适用场景",
        "## 本地安装",
        "## 每次修改前都要校验",
        "## 项目状态",
    ]:
        report.ok(marker in readme_zh, f"README.zh-CN.md missing section: {marker}")

    contributing = read_text(ROOT / "CONTRIBUTING.md", report)
    for marker in ["python -S quick_validate.py", "ui-ux/evals/evals.json", "ui-ux/evals/trigger-evals.json"]:
        report.ok(marker in contributing, f"CONTRIBUTING.md missing contributor instruction: {marker}")

    license_text = read_text(ROOT / "LICENSE", report)
    report.ok("MIT License" in license_text, "LICENSE should clearly identify the license")

    workflow = read_text(ROOT / ".github" / "workflows" / "validate.yml", report)
    for marker in ["actions/checkout@v4", "actions/setup-python@v5", "python -S quick_validate.py"]:
        report.ok(marker in workflow, f"validate.yml missing CI marker: {marker}")

    release = read_text(ROOT / "docs" / "RELEASE_CHECKLIST.md", report)
    report.ok("python -S quick_validate.py" in release, "Release checklist should require quick validation")

    maturity = read_text(ROOT / "docs" / "OPEN_SOURCE_MATURITY.md", report)
    for marker in ["Project hygiene", "Skill quality", "Remaining release-hardening work"]:
        report.ok(marker in maturity, f"OPEN_SOURCE_MATURITY.md missing marker: {marker}")

    version = read_text(ROOT / "VERSION", report).strip()
    report.ok(bool(re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version)), "VERSION should use semver, e.g. 0.1.0")

    readme_markers = ["python -S scripts/package_skill.py", "dist/ui-ux-<version>.skill"]
    for marker in readme_markers:
        report.ok(marker in readme, f"README.md missing packaging marker: {marker}")

    changelog = read_text(ROOT / "CHANGELOG.md", report)
    report.ok(f"## [{version}]" in changelog or "## [Unreleased]" in changelog, "CHANGELOG.md should mention the current version or Unreleased")


def validate_skill_md(report: Report) -> None:
    text = read_text(SKILL_MD, report)
    if not text:
        return
    frontmatter = parse_frontmatter(text)
    report.ok(frontmatter.get("name") == "ui-ux", "SKILL.md frontmatter name must be `ui-ux`")

    description = frontmatter.get("description", "")
    report.ok(bool(description), "SKILL.md frontmatter must include description")
    report.ok(250 <= len(description) <= 1300, "Description should be specific but not bloated (250-1300 chars)")
    for term in ["Use", "Skip", "frontend", "UI/UX", "governance"]:
        report.ok(term.lower() in description.lower(), f"Description should mention `{term}`")
    report.ok(len(text.splitlines()) <= 500, "SKILL.md should stay under 500 lines for progressive disclosure")

    required_sections = [
        "Trigger tiers",
        "Adjacent skill boundaries",
        "Frontend Thinking Gate",
        "Project-stage modes",
        "Reference files",
        "Delivery format",
    ]
    for heading in required_sections:
        report.ok(f"## {heading}" in text, f"SKILL.md missing section: {heading}")

    for marker in [
        "not a string blacklist",
        "not forbidden literal strings",
        "baseline craft floor",
        "freedom in style, discipline in structure",
    ]:
        report.ok(marker.lower() in text.lower(), f"SKILL.md missing context-based copy marker: {marker}")

    for match in re.finditer(r"`((?:references|templates|scripts)/[^`]+)`", text):
        rel = match.group(1)
        report.ok((SKILL / rel).exists(), f"SKILL.md references missing path: {rel}")


def validate_markdown_resources(report: Report) -> None:
    for path in list((SKILL / "references").glob("*.md")) + list((SKILL / "templates").glob("*.md")):
        text = read_text(path, report)
        if not text:
            continue
        rel = path.relative_to(ROOT).as_posix()
        report.ok(text.lstrip().startswith("# "), f"{rel} should start with a level-1 heading")
        lines = text.splitlines()
        if path.parent.name == "references":
            report.warn(len(lines) <= 300, f"{rel} is over 300 lines; add a table of contents if it grows further")

    required_template_markers = {
        "templates/DESIGN.md": [
            "## 11. UX principles for this project",
            "### Primary task before background explanation",
            "### Default recovery paths",
            "### Mobile task priority",
            "Agent-only context to keep out of primary UI",
            "not a blacklist of exact phrases",
            "## 8A. Baseline craft norms",
        ],
        "templates/FRONTEND_REVIEW.md": [
            "## UX flow",
            "permission denied",
            "Success / completion feedback",
            "Mobile layout reorders around the primary task",
            "does not narrate agent reasoning",
            "Primary UI language is consistent",
            "not a string blacklist",
            "## Baseline craft",
            "Empty space is intentional",
        ],
        "templates/FRONTEND_CONTRACT.md": [
            "Agent-only context",
            "Primary UI copy says what happened and what to do next",
            "protocol/API words are secondary",
            "not string blacklists",
            "## Baseline craft floor",
            "Actions must sit near the content they operate on",
        ],
        "templates/PAGE_BRIEF.md": [
            "Primary language for labels",
            "Agent-only context not to show as primary UI copy",
            "not a banned-phrase list",
            "## Baseline craft decision",
            "Empty-space policy",
        ],
    }
    for rel, markers in required_template_markers.items():
        text = read_text(SKILL / rel, report).lower()
        for marker in markers:
            report.ok(marker.lower() in text, f"{rel} missing UX maturity marker: {marker}")


def validate_scripts(report: Report) -> None:
    for script in (SKILL / "scripts").glob("*.py"):
        source = read_text(script, report)
        if source:
            try:
                compile(source, str(script), "exec")
            except SyntaxError as exc:
                report.errors.append(f"{script.relative_to(ROOT)} has a syntax error: {exc}")

    root_scripts = ROOT / "scripts"
    report.ok((root_scripts / "package_skill.py").is_file(), "Missing root release script: scripts/package_skill.py")
    for script in root_scripts.glob("*.py"):
        source = read_text(script, report)
        if source:
            try:
                compile(source, str(script), "exec")
            except SyntaxError as exc:
                report.errors.append(f"{script.relative_to(ROOT)} has a syntax error: {exc}")

    init_script = SKILL / "scripts" / "init_frontend_quality.py"
    if not init_script.exists():
        return

    with tempfile.TemporaryDirectory(prefix="uiux-skill-validate-") as tmp:
        project = Path(tmp) / "project"
        project.mkdir()
        # Intentionally force --update-agents in the smoke test: this proves the
        # governance-doc copy path and the AGENTS.md pointer/idempotency path.
        # Normal users should pass this flag only when they want repo-level
        # frontend governance installed, not for every page edit.
        cmd = [sys.executable, "-S", str(init_script), "--project", str(project), "--update-agents"]
        first = subprocess.run(cmd, cwd=str(SKILL), text=True, capture_output=True)
        report.ok(first.returncode == 0, f"init_frontend_quality.py smoke test failed: {first.stderr or first.stdout}")

        second = subprocess.run(cmd, cwd=str(SKILL), text=True, capture_output=True)
        report.ok(second.returncode == 0, f"init_frontend_quality.py idempotency run failed: {second.stderr or second.stdout}")

        docs = project / "docs" / "frontend"
        for name in REQUIRED_TEMPLATES:
            report.ok((docs / name).is_file(), f"Smoke test did not create docs/frontend/{name}")
        agents = project / "AGENTS.md"
        if agents.exists():
            marker_count = agents.read_text(encoding="utf-8").count("Frontend quality governance")
            report.ok(marker_count == 1, "AGENTS.md pointer should be idempotent and appear exactly once")
        else:
            report.errors.append("Smoke test did not create AGENTS.md with --update-agents")

    package_script = ROOT / "scripts" / "package_skill.py"
    if package_script.exists():
        package_source = read_text(package_script, report)
        for marker in ["VERSION_PATTERN", "Version file not found", "Create VERSION or pass --version"]:
            report.ok(marker in package_source, f"package_skill.py missing version-safety marker: {marker}")

        with tempfile.TemporaryDirectory(prefix="uiux-package-validate-") as tmp:
            cmd = [sys.executable, "-S", str(package_script), "--output-dir", tmp]
            result = subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)
            report.ok(result.returncode == 0, f"package_skill.py smoke test failed: {result.stderr or result.stdout}")
            version = read_text(ROOT / "VERSION", report).strip()
            archive = Path(tmp) / f"ui-ux-{version}.skill"
            report.ok(archive.is_file(), f"package_skill.py did not create expected archive: {archive.name}")
            if archive.is_file():
                try:
                    with zipfile.ZipFile(archive) as zipf:
                        names = set(zipf.namelist())
                        report.ok("ui-ux/SKILL.md" in names, "Packaged archive must include ui-ux/SKILL.md")
                        report.ok("README.md" not in names, "Packaged archive should not include root README.md")
                        report.ok(not any("__pycache__" in name or name.endswith((".pyc", ".pyo")) for name in names), "Packaged archive should exclude Python cache artifacts")
                except zipfile.BadZipFile as exc:
                    report.errors.append(f"Packaged .skill archive is not a valid zip file: {exc}")


def validate_evals(report: Report) -> None:
    evals_path = SKILL / "evals" / "evals.json"
    trigger_path = SKILL / "evals" / "trigger-evals.json"

    try:
        evals = json.loads(read_text(evals_path, report))
    except json.JSONDecodeError as exc:
        report.errors.append(f"evals/evals.json is invalid JSON: {exc}")
        evals = {}

    if isinstance(evals, dict):
        report.ok(evals.get("skill_name") == "ui-ux", "evals/evals.json skill_name must be ui-ux")
        cases = evals.get("evals", [])
        report.ok(isinstance(cases, list) and len(cases) >= 6, "evals/evals.json should include at least 6 realistic evals")
        ids: set[int] = set()
        has_skip_case = False
        for idx, case in enumerate(cases):
            prefix = f"evals[{idx}]"
            report.ok(isinstance(case.get("id"), int), f"{prefix}.id must be an integer")
            if isinstance(case.get("id"), int):
                report.ok(case["id"] not in ids, f"{prefix}.id is duplicated")
                ids.add(case["id"])
            for field in ["prompt", "expected_output"]:
                report.ok(isinstance(case.get(field), str) and len(case[field].strip()) >= 40, f"{prefix}.{field} should be a detailed string")
            report.ok(isinstance(case.get("files", []), list), f"{prefix}.files must be a list")
            expectations = case.get("expectations", [])
            report.ok(isinstance(expectations, list) and len(expectations) >= 3, f"{prefix}.expectations should include at least 3 checks")
            combined = (case.get("prompt", "") + " " + case.get("expected_output", "")).lower()
            has_skip_case = has_skip_case or "should not trigger" in combined or "skip" in combined
        report.ok(has_skip_case, "evals/evals.json should include at least one skip / should-not-trigger near-miss case")
    else:
        report.errors.append("evals/evals.json must be an object")

    try:
        trigger_evals = json.loads(read_text(trigger_path, report))
    except json.JSONDecodeError as exc:
        report.errors.append(f"evals/trigger-evals.json is invalid JSON: {exc}")
        trigger_evals = []

    if isinstance(trigger_evals, list):
        report.ok(len(trigger_evals) >= 18, "trigger-evals.json should include at least 18 trigger boundary queries")
        positives = 0
        negatives = 0
        for idx, item in enumerate(trigger_evals):
            report.ok(isinstance(item.get("query"), str) and len(item["query"].strip()) >= 30, f"trigger-evals[{idx}].query should be realistic")
            report.ok(isinstance(item.get("should_trigger"), bool), f"trigger-evals[{idx}].should_trigger must be boolean")
            if item.get("should_trigger") is True:
                positives += 1
            if item.get("should_trigger") is False:
                negatives += 1
        report.ok(positives >= 8 and negatives >= 8, "trigger-evals.json should include at least 8 positives and 8 negatives")
    else:
        report.errors.append("evals/trigger-evals.json must be a list")


def main() -> int:
    report = Report()
    validate_structure(report)
    validate_open_source_hygiene(report)
    validate_skill_md(report)
    validate_markdown_resources(report)
    validate_scripts(report)
    validate_evals(report)

    if report.warnings:
        print("Warnings:")
        for item in report.warnings:
            print(f"  - {item}")
    if report.errors:
        print("Validation failed:")
        for item in report.errors:
            print(f"  - {item}")
        return 1

    print("Validation passed: ui-ux skill is structurally ready for beta/global installation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
