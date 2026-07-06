# Benchmark Report Template

Use this template after running with-skill vs baseline evals.

## Metadata

- **Skill:** ui-ux
- **Version:**
- **Date:**
- **Executor model:**
- **Runs per configuration:**
- **Eval set:** `ui-ux/evals/evals.json`

## Summary

| Configuration | Pass rate | Avg time | Avg tokens | Notes |
|---|---:|---:|---:|---|
| with_skill | | | | |
| without_skill | | | | |
| delta | | | | |

## Per-eval results

| Eval | with_skill | without_skill | Key difference |
|---|---:|---:|---|
| new-project-stack-and-governance | | | |
| half-built-admin-refactor | | | |
| rescue-gpt-looking-ui | | | |
| install-frontend-governance-docs | | | |
| tiny-ui-sensitive-tweak | | | |
| backend-only-skip-near-miss | | | |
| finished-product-polish | | | |

## Qualitative observations

- Where the skill improved project cognition:
- Where the skill added unnecessary ceremony:
- Which assertions failed in both configurations:
- Which evals were flaky or ambiguous:

## Release decision

- [ ] Ready to release
- [ ] Needs skill instruction changes
- [ ] Needs eval changes
- [ ] Needs trigger description changes

## Follow-up

- [Action]
