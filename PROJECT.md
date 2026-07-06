# ui-ux skill project

This folder is the clean working project for the Codex `ui-ux` skill.

- Source skill: `ui-ux/`
- Edit the skill here first.
- Validate with `python -S quick_validate.py` before installing.
- Keep `ui-ux/evals/evals.json` and `ui-ux/evals/trigger-evals.json`
  current when changing trigger behavior or workflow requirements.
- Root-level files such as `README.md`, `CONTRIBUTING.md`, `LICENSE`,
  `.github/`, and `docs/` are for open-source project governance. Do not copy
  them into the installed skill directory.
- Package release artifacts with `python -S scripts/package_skill.py` only after
  validation passes.
- Do not copy this into `C:\Users\Administrator\.codex\skills` until the user explicitly wants the skill globally enabled.
- Keep the actual skill folder lean: no README, changelog, or extra docs inside `ui-ux/` unless they are runtime references/templates/scripts used by the skill.

Current install target when approved:

```text
C:\Users\Administrator\.codex\skills\ui-ux
```
