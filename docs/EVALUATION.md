# Evaluation Guide

This project keeps two eval sets:

- `ui-ux/evals/evals.json` — functional task behavior.
- `ui-ux/evals/trigger-evals.json` — trigger / skip boundaries.

## Functional eval coverage

The functional evals cover:

- new project stack and governance recommendation;
- half-built admin refactor;
- rescue of GPT/Codex-looking UI;
- frontend governance installation;
- tiny UI-sensitive copy change;
- backend-only skip near-miss;
- finished product UX polish.

Each eval has human-readable expectations. These are intended to support both
manual review and future benchmark automation.

## Trigger eval coverage

The trigger evals include 10 should-trigger and 10 should-not-trigger examples.
Negative cases are near misses such as backend-only changes, dependency chores,
documentation-only work, CI fixes, and non-web artifacts.

## Recommended benchmark loop

For release candidates, run:

1. with-skill execution for each functional eval;
2. baseline execution without the skill;
3. grading against `expectations`;
4. aggregate benchmark report;
5. human review of qualitative outputs.

The benchmark should answer:

- Does the skill improve project cognition?
- Does it avoid unnecessary UI ceremony for skip cases?
- Does it improve UX flow, recovery, state, and mobile coverage?
- Does it add unacceptable token or time overhead?

Use `docs/BENCHMARK_TEMPLATE.md` when recording release benchmark results.

## Release bar

A release should not regress:

- trigger precision on near-miss negative cases;
- governance-doc installation behavior;
- template maturity markers;
- `python -S quick_validate.py`.
