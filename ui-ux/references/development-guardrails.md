# Development Guardrails

These guardrails become enforceable during implementation. Tailor them per project — do not copy as universal law.

## Rule layers

### Hard red lines

Non-negotiable on all projects:

- Secret / token / private URL leakage by default.
- Dangerous operation without confirmation, undo, or safety mechanism.
- Core async surface with no loading, empty, or error state.
- Technical state shown as primary UI copy with no human translation.
- Agent implementation context or design intent shown as primary UI copy.
- Long text, IDs, paths, JSON, or table cells breaking layout.
- Mobile view unusable for its primary task.
- Raw JSON as the main interface for non-developer tasks.
- README / architecture / product manifesto pasted into normal operational UI.

### Project contract

Defined per project in `FRONTEND_CONTRACT.md`:

- Product in human words.
- Target users.
- Product temperament.
- Reference systems.
- Allowed UI foundations.
- Business-object boundaries.
- User-facing vocabulary.
- Status translation table.
- Page patterns.
- Screenshots to maintain.

### Default recommendations

Apply unless there is a clear, stated reason to deviate:

- Tool pages: compact, task-first, no hero or atmosphere.
- Ops pages: state-first; issues and next actions before decoration.
- Marketing surfaces: more visual freedom is acceptable.
- Tables: browse and select; not for complex workflows or inline configuration.
- Complex configuration: progressive disclosure; not exposed all at once.
- Copy: concise; deep explanation belongs in docs, tooltips, or expandable details.

### Creative freedom

Allowed where product temperament supports it. The agent must:
1. Explain why the style fits the product.
2. Confirm that usability is preserved.

---

## Before coding

Produce the Frontend Thinking Gate (see `SKILL.md`). Do not start writing code until project cognition is established.

## During coding

Active checks:

- Reuse existing project components before creating new ones.
- If creating a component, explain why existing components are insufficient.
- Keep all page copy in user language.
- Keep agent-only context out of primary UI. If the text explains why a panel exists, how the UI is architected, or what the agent is trying to prove, move it to docs, tooltip, diagnostic detail, or code comments.
- Translate every user-visible status and error.
- Provide loading, empty, error, and long-text behavior for every async surface.
- Protect destructive actions with confirmation or undo.
- Do not let tables become configuration or editing surfaces.
- Consider mobile task reordering — not just vertical stacking.
- Prefer deterministic visual verification for important pages.

## After coding

Run appropriate checks:

- Typecheck / build / lint.
- Component tests if available.
- Storybook if component states changed.
- Playwright screenshots for core pages.
- Desktop / mobile / error / empty / long-content variants where relevant.

Then report:

```text
Project understanding used:
Design decisions:
Guardrails applied:
Verification:
Remaining risks:
What should be codified:
```

---

## Suggested project docs

- `DESIGN.md` — product temperament, references, tokens, UI direction.
- `FRONTEND_CONTRACT.md` — hard lines, page patterns, vocabulary, status translation.
- `PAGE_BRIEF.md` — page-specific task and layout decision.
- `FRONTEND_REVIEW.md` — review checklist and screenshot notes.

## Suggested component governance

When project patterns stabilize, add Storybook stories for:

- default state;
- loading;
- empty;
- error;
- long text;
- permission denied;
- dangerous action;
- dense data;
- mobile / narrow.

## Suggested visual QA

For each core page, capture:

- desktop;
- mobile;
- empty;
- error;
- long text;
- modal / drawer open;
- dense data.
