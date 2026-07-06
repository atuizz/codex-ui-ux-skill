# Release Checklist

Use this checklist before tagging or publishing a version.

## Required

- [ ] `python -S quick_validate.py` passes.
- [ ] `ui-ux/SKILL.md` frontmatter has correct `name` and a specific
      `description`.
- [ ] `ui-ux/SKILL.md` remains under 500 lines.
- [ ] New or changed behavior is covered by `ui-ux/evals/evals.json`.
- [ ] Trigger changes are covered by `ui-ux/evals/trigger-evals.json`.
- [ ] No `__pycache__`, `.pyc`, local benchmark outputs, or private files are
      included.
- [ ] Changelog is updated.
- [ ] Install instructions are still accurate.
- [ ] `python -S scripts/package_skill.py` creates `dist/ui-ux-<version>.skill`.

## Recommended

- [ ] Run with-skill vs baseline benchmark.
- [ ] Review at least one output from each functional eval category.
- [ ] Verify installation into a clean Codex skills directory.
- [ ] Confirm templates install cleanly into a temporary project.

## Manual install smoke test

```powershell
cd D:\UI-UX
python -S quick_validate.py
python -S scripts/package_skill.py
Copy-Item -Recurse -Force "D:\UI-UX\ui-ux" "C:\Users\Administrator\.codex\skills\ui-ux"
```
