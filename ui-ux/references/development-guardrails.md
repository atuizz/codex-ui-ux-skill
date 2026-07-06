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

Creative freedom is not a waiver for baseline craft. Do not ban expressive visuals by default; instead preserve the craft floor that lets creativity feel intentional rather than accidental.

## Baseline craft floor

Apply these checks to every user-visible surface, regardless of style:

- **Alignment and rhythm:** sections, cards, controls, and panels align to an obvious grid or rhythm. Avoid stray half-width islands and leftover empty regions that make the page look unfinished.
- **Spacing consistency:** similar component groups use similar padding, gaps, radii, and density unless a product reason explains the difference.
- **Action hierarchy:** define primary, secondary, and utility actions before coloring buttons. Use one primary action per region when possible; keep utility actions such as copy/export visually quieter.
- **Action proximity:** place an action near the content it operates on. A copy button belongs with the copied content; a delete button belongs with the item or panel it affects.
- **Status vs controls:** read-only status indicators must not look like editable inputs. Navigation tabs and display-only step/status indicators must use distinct treatments.
- **Human label vs technical identifier:** user-facing labels are primary; endpoints, paths, IDs, status codes, JSON keys, hashes, filenames, and version strings are secondary, smaller, lower contrast, or monospace where helpful.
- **Technical string rendering:** render API endpoints, URLs, file paths, IDs, hashes, and version strings in a style that makes them recognizable as data, not prose; avoid giving them equal weight with task labels.
- **Numeric precision:** numeric values in the same column or list use consistent precision and alignment. Prefer user-facing labels like "匹配度 90%" when raw confidence is not needed.
- **Tag semantics:** tags with different meanings (source, author, type, status, environment) should not all look identical. Use grouping, prefix, tone, or shape to distinguish semantic categories.
- **Tag overflow:** list-row tags need max-width, truncation, wrapping rules, or tooltip. Long tags should not break row rhythm.
- **Selected state:** active/selected states use at least two visual signals, such as color + border, background + weight, icon + label, or position + emphasis. Do not rely on color alone.
- **Separator convention:** choose one separator convention per component type and apply it consistently. Avoid mixing `·`, `/`, badges, and loose spaces at the same interface layer.
- **Conditional copy:** instructional copy that references a state ("select an item", "after step X") appears only when that state is true. Loading, empty, error, and success states need their own copy.

---

## Before coding

Produce the Frontend Thinking Gate (see `SKILL.md`). Do not start writing code until project cognition is established.

## During coding

Active checks:

- Reuse existing project components before creating new ones.
- If creating a component, explain why existing components are insufficient.
- Keep all page copy in user language.
- Keep agent-only context out of primary UI. This is not a string blacklist: if the text helps the current user act, debug, or recover, it can remain in the right place. If it explains why a panel exists, how the UI is architected, or what the agent is trying to prove, move it to docs, tooltip, diagnostic detail, or code comments.
- Translate every user-visible status and error.
- Provide loading, empty, error, and long-text behavior for every async surface.
- Protect destructive actions with confirmation or undo.
- Do not let tables become configuration or editing surfaces.
- Consider mobile task reordering — not just vertical stacking.
- Preserve baseline craft: alignment, spacing, action hierarchy, status/control distinction, action proximity, technical identifier hierarchy, and intentional whitespace.
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
