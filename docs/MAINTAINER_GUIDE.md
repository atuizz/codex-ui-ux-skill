# Maintainer Guide

## Project boundaries

This repository has two layers:

1. `ui-ux/` — the installable Codex skill bundle.
2. root and `docs/` — open-source project documentation, validation, and
   maintainer workflow.

Do not copy root-level project docs into `C:\Users\Administrator\.codex\skills`.
Only copy the `ui-ux/` directory when installing the skill.

## Common changes

### Change trigger behavior

1. Edit the `description` in `ui-ux/SKILL.md`.
2. Update `ui-ux/evals/trigger-evals.json`.
3. Run `python -S quick_validate.py`.
4. If possible, run a trigger optimization or manual trigger review.

### Change task behavior

1. Update the relevant section of `ui-ux/SKILL.md` or `ui-ux/references/`.
2. Update `ui-ux/evals/evals.json`.
3. Run `python -S quick_validate.py`.

### Change governance templates

1. Edit files under `ui-ux/templates/`.
2. Update `quick_validate.py` if the change introduces a new required maturity
   marker.
3. Smoke test template installation:

   ```bash
   python -S ui-ux/scripts/init_frontend_quality.py --project /tmp/example --update-agents
   ```

## Release checklist

See `docs/RELEASE_CHECKLIST.md`.

## Packaging

Create a local `.skill` archive with:

```bash
python -S quick_validate.py
python -S scripts/package_skill.py
```

The package script writes `dist/ui-ux-<version>.skill` and includes only the
installable `ui-ux/` directory.
