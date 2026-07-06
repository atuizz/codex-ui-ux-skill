# Codex / GPT Frontend Anti-Patterns

Use this as a diagnostic list, not a rigid ban list. Some patterns can be valid on the right surface; the problem is mismatch, overuse, or absence of task value.

---

## 1. README on screen

**Symptoms:** Project definition, architecture, future roadmap, protocol explanation, or internal capabilities pasted into operational UI. Page feels like README + console + docs combined.

**Fix:**
- Keep UI copy short and task-specific.
- Move background content to docs / help / tooltips / expandable details.
- Translate internal language into user language.

---

## 2. Tool page as landing page

**Symptoms:** API console or admin tool gets a giant hero, decorative background, atmospheric copy, serif display title, or marketing language. The actual task flow is secondary to style.

**Fix:**
- Prioritize request / result / error diagnosis.
- Make raw data secondary to human conclusion.
- Keep branding subtle unless the surface is explicitly marketing.

---

## 3. Card wall

**Symptoms:** Every idea becomes a card. All cards have similar visual weight. No primary task or clear next action.

**Fix:**
- Group by task and severity.
- Use issue queues, state summaries, and action bars.
- Reduce card count or introduce hierarchy.

---

## 4. No journey, only screen

**Symptoms:** The screen looks organized, but it is unclear how the user arrived, what decision comes first, what happens after action, or how failure is recovered.

**Fix:**
- Map entry → decision → action → feedback → recovery → completion.
- Make the first decision and primary action obvious.
- Add feedback and recovery states before visual polish.

---

## 5. Everything visible at once

**Symptoms:** Summaries, forms, settings, logs, diagnostics, and actions are all exposed at the same time. The page feels complete but creates decision fatigue.

**Fix:**
- Separate browse / inspect / edit / commit.
- Use progressive disclosure for optional or advanced configuration.
- Demote diagnostics and raw detail behind panels, tabs, drawers, or expanders.

---

## 6. Business-object soup

**Symptoms:** Multiple distinct objects (project / customer / license / server / instance / user) share one flat table or workbench. Global pages perform context-specific actions without surfacing the active object.

**Fix:**
- Identify core objects and ownership boundaries.
- Move actions into the correct object context.
- Use detail pages, workbenches, or timelines per object.

---

## 7. All-in-one form / premature complexity

**Symptoms:** Multi-step flows expose every field upfront. Later configuration appears before source or goal is established.

**Fix:**
- Progressive disclosure.
- Step flows with conditional rendering.
- Previews before commitment.

---

## 8. Table stuffed with configuration

**Symptoms:** Inputs, toggles, badges, long IDs, actions, and nested state all inside table cells. Browsing and editing are mixed.

**Fix:**
- Table for scanning and selecting only.
- Details / drawer / modal for editing.
- Inline edit only for high-frequency, low-risk fields.

---

## 9. Technical status as user copy

**Symptoms:** `needs_recovery`, `persisting`, `retryable=false`, `GROUP_MESSAGE_CREATE`, `source_path`, `mount_id` shown as primary UI copy.

**Fix:**
- Translate every user-visible state.
- Show raw codes in diagnostic / detail sections.
- Include impact and next step in the primary message.

---

## 10. No recovery path

**Symptoms:** Error, empty, permission denied, timeout, or destructive action states only say what happened. They do not tell the user how to continue, retry, undo, request access, or inspect details.

**Fix:**
- Add reason, impact, and next step.
- Provide retry, undo, request-access, change-input, or view-details paths where appropriate.
- Keep raw diagnostics secondary.

---

## 11. Fake-premium styling

**Symptoms:** Large gradients, glass effects, giant type, soft shadows, decorative code panels, or premium fonts applied to a task-oriented surface. Style does not help the user decide or act.

**Fix:**
- Ask what the style does for the task.
- Align style to product temperament.
- Reserve expressive styling for surfaces where it is earned.

---

## 12. Mechanical mobile stacking

**Symptoms:** Desktop cards and tables simply stack vertically on mobile. The user must scroll past everything to reach the primary action.

**Fix:**
- Reorder layout by the mobile task, not by desktop layout order.
- Collapse or hide secondary sections.
- Replace complex tables with task-oriented cards or lists.
- Keep the primary action near the top.

---

## 13. Default component-library face as final product

**Symptoms:** Page is clean but indistinguishable from the shadcn / Ant Design / MUI example gallery. No project-specific language, state handling, or visual hierarchy.

**Fix:**
- Treat the library as a baseline, not the destination.
- Add project tokens, page patterns, state language, and business-specific components.
- Mature the UI toward product identity through the codify step.

---

## Diagnosis format

When reviewing an existing UI for anti-patterns, use:

```text
Anti-patterns present:
  - [pattern]: [where / how it appears]
Root cause:
Fix depth:    cosmetic / page-level / component-layer / restart
Recommended first step:
```
