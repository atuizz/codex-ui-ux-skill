# Workflow: Cognition → Recommend → Preview → Choose → Polish → Optimize → Judge → Codify → Unify

## 0. Project cognition comes first

Never start from "make it modern." Start from product reality:

- What is the project in ordinary human words?
- Who uses this surface?
- What is the primary task?
- What journey brought the user here, and what is the first decision?
- What counts as success, and how does the user recover from failure?
- What are the core business objects?
- Is this page a tool, admin, workbench, docs, marketing, onboarding, detail, table, wizard, or mobile task?
- What existing code, components, and design norms already exist?

If these are unknown, inspect docs, routes, components, screenshots, data models, and current UI before writing a line of code.

## 1. Recommend

For new or uncertain projects, recommend rather than waiting for the user to specify every technology.

Recommend:

- framework and routing;
- UI foundation;
- table / form / data / chart strategy;
- design reference pack;
- verification plan;
- first prototype pages.
- first journey map and recovery-state plan.

Format:

```text
Recommended: ...
Why: ...
Alternative: ...
Not recommended: ...
Upgrade path: ...
```

## 2. Preview

If product style is uncertain, do not lock a design from words alone. Describe or prototype 2–3 directions:

- conservative / safe baseline;
- product-specific polished direction;
- more expressive direction if product temperament supports it.

Previews clarify differences. They are not final code sprawl.

## 3. Choose

Record what the project wants to become:

- chosen direction;
- what to keep;
- what to avoid;
- where creative freedom is allowed;
- where operational clarity wins over aesthetics.

## 4. Polish

Polish the selected direction:

- task flow and first-decision clarity;
- visual hierarchy;
- spacing and density;
- typography scale;
- status badges;
- table scanning;
- action priority;
- empty / error / loading copy;
- recovery paths and completion feedback;
- mobile task layout;
- motion restraint;
- project-specific identity.

## 5. Optimize

Optimize implementation quality:

- component reuse;
- state coverage (loading / empty / error / long text);
- accessibility and keyboard / focus;
- responsive behavior and mobile task reordering;
- performance;
- code boundaries;
- Storybook stories;
- Playwright screenshots.

## 6. Judge

Use judgment, not only build success.

Ask:

- Does this page solve the user task?
- Is the journey clear from entry to completion?
- Does the user have a recovery path when something goes wrong?
- Is the product temperament right?
- Are important states and next actions clear?
- Is the UI in human language?
- Is there GPT/Codex flavor?
- Does mobile need task reordering rather than mechanical stacking?
- Are screenshots acceptable?

## 7. Codify

After good outcomes, update project memory:

- `DESIGN.md`;
- `FRONTEND_CONTRACT.md`;
- component docs;
- anti-pattern examples;
- Storybook stories;
- Playwright screenshot tests;
- review checklist.

Do not codify premature guesses as hard law.

## 8. Unify

Unify within the project:

- tokens;
- components;
- page shells;
- state language;
- table behavior;
- action patterns;
- copy voice;
- responsive rules.

Do not force unrelated projects into the same visual style.

---

## Lightweight gates

Use the smallest gate that fits the task.

### Tiny change

```text
Page / surface:
Impact:
Task / state affected:
Risk to avoid:
```

### New page

```text
Surface type:
Primary task:
Entry / journey:
First decision:
Information hierarchy:
User vocabulary:
Recovery path:
Mobile primary action:
Layout choice:
States required:
Verification:
```

### New project

```text
Project stage:
Product temperament:
User type:
Stack recommendation:
UI foundation:
Reference systems:
Prototype plan:
Governance plan:
```

### Half-built refactor

```text
Current UI level:
Should refactor?    no / local page / component-layer / page-IA restart
Keep:
Replace:
Smallest safe step:
```

### Rescue (AI output degraded)

```text
Failure modes present:    [list from anti-patterns.md]
UX failures present:      [list from ux-evaluation.md]
Root cause:
Fix depth:    cosmetic / page-level / component-layer / restart
First step:
```
