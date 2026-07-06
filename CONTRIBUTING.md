# Contributing

Thanks for improving the `ui-ux` Codex skill.

## Development principles

- Keep the skill useful across projects; avoid overfitting to one app or one
  user's vocabulary.
- Explain why instructions matter. Prefer durable judgment over long rule lists.
- Preserve progressive disclosure: keep `ui-ux/SKILL.md` concise and move
  detailed guidance into targeted files under `ui-ux/references/`.
- Keep the skill bundle lean. Repository docs belong at the root or in `docs/`,
  not inside `ui-ux/`.
- Do not include secrets, private URLs, customer data, internal identifiers, or
  organization-specific examples.

## Before opening a pull request

Run:

```bash
python -S quick_validate.py
```

Also check:

- If trigger behavior changed, update `ui-ux/evals/trigger-evals.json`.
- If task behavior changed, update `ui-ux/evals/evals.json`.
- If templates changed, ensure `quick_validate.py` still checks the important
  maturity markers.
- If helper scripts changed, add or keep smoke coverage in `quick_validate.py`.
- If release packaging changed, verify `python -S scripts/package_skill.py`.

## Skill authoring checklist

- [ ] Frontmatter has `name` and a specific `description`.
- [ ] `SKILL.md` stays under 500 lines.
- [ ] Reference files are linked from `SKILL.md` with clear read-when guidance.
- [ ] Templates are reusable and do not encode a private project.
- [ ] Eval cases include both positive and near-miss negative scenarios.
- [ ] Validator passes without relying on third-party packages.

## Commit style

Use concise, descriptive commit messages. Examples:

- `docs: add release checklist`
- `evals: cover billing cancellation polish`
- `skill: clarify adjacent frontend skill boundaries`
- `validator: check governance template markers`

## Pull request expectations

Explain:

1. What behavior changed.
2. Why the change improves the skill.
3. Which evals or validation checks cover it.
4. Any remaining risks or follow-up work.
