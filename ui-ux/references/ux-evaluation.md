# UX Evaluation

Use this when reviewing, rescuing, or designing a product surface where success depends on user flow, decision clarity, information architecture, recovery, or mobile behavior. It captures recurring user feedback and observed GPT/Codex frontend weaknesses.

---

## Project lessons to preserve

These are recurring lessons from real project feedback:

- A page can be visually neat and still fail UX if the user cannot tell what to do first.
- Admin and ops products need state, issue severity, and next action before decoration.
- Tool surfaces should not become landing pages; product atmosphere must not bury the workbench.
- Project docs, architecture, and internal concepts are agent context, not normal UI copy.
- Business objects need clear boundaries; global dashboards should not become object soup.
- Tables are for scanning and selection; complex editing belongs in details, drawers, or guided flows.
- Mobile UX needs task reordering, not only responsive stacking.
- Good UI work should leave reusable rules behind in project docs when the lesson will repeat.
- `AGENTS.md` is for short handoff pointers; detailed frontend rules belong in frontend governance docs.

---

## Why GPT frontend fails at UX

GPT/Codex often produces acceptable-looking screens while missing the product experience:

- It optimizes the screenshot, not the user's task.
- It confuses product explanation with interface design.
- It narrates its own implementation reasoning on the page instead of separating agent context from user action copy.
- It creates equal-weight cards instead of decisions and priorities.
- It exposes internal objects, README language, routes, statuses, and architecture terms.
- It treats shadcn / Ant / MUI defaults as the finished product.
- It makes generic SaaS dashboards instead of project-specific work surfaces.
- It mixes business objects on one flat surface because the data model is visible in code.
- It handles mobile by stacking desktop UI, not by reordering the mobile task.
- It forgets loading, empty, error, permission, destructive-action, long-text, and recovery states.
- It over-polishes with gradients, glass, badges, and cards without improving comprehension.

## UX-first questions

Before judging visual polish, answer:

```text
Who arrives here?
What happened immediately before this screen?
What is the user trying to decide or do?
What is the first decision the screen asks from them?
What is the success criterion?
What can go wrong?
How does the user recover?
What must be available on mobile first?
```

If these answers are unclear, the UI is not ready for visual polish.

## Journey map

Map the surface as:

```text
Entry → orientation → decision → action → feedback → recovery → completion
```

Check each step:

| Step | User goal | UI support | Friction | Fix |
|---|---|---|---|---|
| Entry | Know where they are | [breadcrumb/title/state] | [gap] | [change] |
| Decision | Choose next action | [primary action/summary] | [gap] | [change] |
| Action | Complete task safely | [form/table/drawer] | [gap] | [change] |
| Feedback | Understand result | [toast/state/result] | [gap] | [change] |
| Recovery | Fix failure | [copy/retry/undo] | [gap] | [change] |

## Information architecture checks

- Name the core business objects in human language.
- Keep object ownership clear; do not flatten customer / server / license / user / task / log into one surface.
- Place actions inside the correct object context.
- Separate browse, inspect, edit, and commit flows.
- Keep raw JSON, IDs, logs, and diagnostics secondary unless the surface is explicitly developer-focused.
- Prefer progressive disclosure when a task has prerequisites or optional configuration.

## Friction audit

Look for friction that a clean screenshot can hide:

- User must read paragraphs before acting.
- User must infer state from raw codes or badge colors.
- Primary and secondary actions look equal.
- Critical action is below a wall of cards or table columns.
- Error explains what failed but not what to do next.
- Empty state is decorative but not actionable.
- Permission denial has no request/access path.
- Long text, IDs, or paths destroy scanning.
- Mobile requires scrolling past secondary content before the main action.

## Microcopy and recovery

Primary UI copy should answer:

```text
What happened?
Why does it matter?
What can I do next?
```

Primary UI copy should not answer:

```text
Why did the agent design this panel?
What implementation contract does this component follow?
Which protocol concept is the agent trying to prove it understands?
```

Those belong in docs, tooltips, diagnostics, or raw details.

For every important state, include:

- loading: what is being prepared;
- empty: what this means and how to create or import data;
- error: reason, impact, next step;
- permission denied: who can grant access or where to request it;
- destructive action: scope, consequence, confirmation/undo;
- success: what changed and where to continue.

## Mobile UX

Mobile is not desktop stacked vertically.

- Put the primary task and current state near the top.
- Collapse or defer secondary summaries, filters, diagnostics, and raw details.
- Replace complex tables with task-oriented list rows or detail-first cards.
- Keep primary actions reachable without scrolling through context.
- Test dense data, long labels, modals/drawers, keyboard focus, and touch targets.

## Accessibility as UX

Accessibility is not only compliance:

- Keyboard path should match the task flow.
- Focus order should not jump through hidden or secondary content first.
- Error messages should be tied to the relevant field or action.
- Color should not be the only status signal.
- Dialogs, drawers, menus, and command palettes need clear labels and escape paths.

## Review output format

Use this for UX reviews:

```text
UX judgment:
Task success:
Journey gaps:
Information architecture issues:
Friction:
Missing states:
Recovery gaps:
Mobile risk:
Accessibility risk:
GPT/Codex weakness detected:
Recommended fix depth: cosmetic / page-level / component-layer / restart
First fix:
```
