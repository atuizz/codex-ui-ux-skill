# ui-ux Codex Skill

`ui-ux` is a Codex skill for frontend UI/UX quality work. It helps agents avoid
generic AI-looking interfaces by establishing project cognition, user journeys,
business-object boundaries, recovery states, mobile priorities, and frontend
governance before implementation.

This is an unofficial community-maintained skill for Codex.

This repository is the clean working project for the skill. The actual skill
bundle lives in [`ui-ux/`](ui-ux/).

## What this skill is for

Use this skill when frontend work materially affects a web product surface:

- page creation, redesign, polish, rescue, or review;
- screenshot or UX critique;
- component-system or UI-foundation choices;
- shadcn/Tailwind/table/form patterns with user-visible impact;
- loading, empty, error, permission, success, long-text, mobile, or accessibility states;
- frontend governance docs such as `DESIGN.md`, `FRONTEND_CONTRACT.md`,
  `PAGE_BRIEF.md`, and `FRONTEND_REVIEW.md`.

Do not use it for pure backend/API/data/model work, dependency chores, mechanical
renames, or tests with no user-visible frontend impact.

## Repository layout

```text
.
├── ui-ux/                     # Skill bundle copied into CODEX_HOME/skills
│   ├── SKILL.md               # Main skill instructions
│   ├── references/            # Progressive-disclosure reference docs
│   ├── templates/             # Frontend governance templates
│   ├── scripts/               # Skill helper scripts
│   └── evals/                 # Functional and trigger eval sets
├── docs/                      # Maintainer docs for this open-source project
├── quick_validate.py          # Structural validator and smoke test
└── PROJECT.md                 # Local working notes
```

Keep the actual skill folder lean. Project-level documentation belongs at the
repository root or in `docs/`, not inside `ui-ux/`.

## Requirements

- Python 3.10+ recommended.
- No third-party Python packages are required for validation.

Use `python -S` for validation to avoid user-site Python startup issues:

```powershell
python -S quick_validate.py
```

## Install locally

Validate first:

```powershell
cd D:\UI-UX
python -S quick_validate.py
```

Then copy the skill into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force "D:\UI-UX\ui-ux" "C:\Users\Administrator\.codex\skills\ui-ux"
```

On macOS/Linux-style environments, adapt the destination to your `CODEX_HOME`:

```bash
cp -R ./ui-ux "$CODEX_HOME/skills/ui-ux"
```

## Validate before every change

```powershell
python -S quick_validate.py
```

The validator checks:

- skill metadata and progressive-disclosure structure;
- required references, templates, scripts, and evals;
- smoke behavior of `scripts/init_frontend_quality.py`;
- absence of cache/build artifacts in the skill bundle;
- open-source project hygiene files and CI workflow.

## Evaluation assets

- [`ui-ux/evals/evals.json`](ui-ux/evals/evals.json) covers functional behavior.
- [`ui-ux/evals/trigger-evals.json`](ui-ux/evals/trigger-evals.json) covers trigger
  and skip boundaries.

See [`docs/EVALUATION.md`](docs/EVALUATION.md) for how to run qualitative and
quantitative evaluations.

## Package a release artifact

Validate first, then create a `.skill` archive:

```powershell
python -S quick_validate.py
python -S scripts/package_skill.py
```

The archive is written to `dist/ui-ux-<version>.skill` and intentionally includes
only the installable `ui-ux/` skill bundle.

## Contributing

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md). In short:

1. Keep `ui-ux/SKILL.md` concise.
2. Add or update evals when changing behavior.
3. Run `python -S quick_validate.py`.
4. Do not put README/changelog/general project docs inside the skill bundle.

## Security

This repository contains instructions and helper scripts for a Codex skill. Do
not add secrets, private URLs, tokens, or organization-specific identifiers to
templates, references, evals, or examples. See [`SECURITY.md`](SECURITY.md).

## License

MIT. See [`LICENSE`](LICENSE).
