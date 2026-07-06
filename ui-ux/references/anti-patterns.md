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

## 1A. Self-narrating UI / interface self-narration

**Symptoms:** The interface explains its own design intent or implementation semantics instead of helping the user act. Examples include prominent subtitles about why a panel exists, labels that explain component contracts, or status text that describes the system's internal model rather than the user's current result.

This usually happens when the agent confuses:

```text
What the agent needs to know to implement the page
```

with:

```text
What the user needs to see to complete the task
```

This is not a ban on particular words. It is a context, hierarchy, and usefulness test:

- If copy helps this user decide, act, debug, or recover now, it can stay.
- If copy mainly proves the agent understands the protocol, component role, or implementation plan, it should move out of primary UI.
- Developer and diagnostic surfaces may show technical terms, raw JSON, protocol steps, and panel roles when that is the user's actual job; still avoid making implementation rationale the headline for a task flow.

**Fix:**
- Keep implementation reasoning in code, docs, comments, tooltips, diagnostics, or governance files.
- Primary UI copy should state what happened, why it matters, and what the user can do next.
- Replace self-explanatory copy with state/action copy.
- Use the user's primary language for labels, states, and actions. Put protocol/API names in secondary labels or raw diagnostics.

Pattern example, not a literal lint rule:

```text
Problematic as primary task copy:
  JSON 区只做诊断，不作为主操作入口。

Better when the user is trying to find a resource:
  搜索已完成，未找到匹配资源。换一个关键词，或切换书源后再试。

Acceptable when it is inside an advanced diagnostic help note:
  原始响应仅用于排查接口问题。
```

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
- If the primary UI is in Chinese, do not let English protocol words dominate labels and actions. Use forms such as `搜索（search）`, `资源列表（resources）`, or keep protocol words in diagnostic details.

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

## 14. Local consistency drift / weak craft floor

**Symptoms:** The page has a coherent visual idea, and individual components look acceptable, but the whole surface feels patched together. Common signs: misaligned panels, uneven leftover whitespace, read-only status cards that look like inputs, actions far from the content they operate on, technical identifiers at the same weight as human labels, mixed separators, inconsistent tag styles, mixed numeric precision, or selected states relying only on color.

This is not a creativity ban. Gradients, unusual layouts, dense consoles, expressive motion, and strong brand treatments can all be valid. The failure is when basic alignment, hierarchy, semantic grouping, and state clarity collapse under the style.

**Fix:**
- Establish a simple grid, spacing rhythm, and region hierarchy before polishing details.
- Define primary / secondary / utility action hierarchy per region.
- Keep status, controls, navigation, diagnostics, and raw data visually distinct.
- Put actions near their target content.
- Make human labels primary and technical identifiers secondary.
- Use consistent numeric precision, tag semantics, separators, active-state signals, and overflow rules.
- Remove or assign purpose to empty leftover space.

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
