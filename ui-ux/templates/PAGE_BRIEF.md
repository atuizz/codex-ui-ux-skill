# PAGE_BRIEF.md

> Per-page design memory. Fill in before building or refactoring a page.
> One file per distinct page or surface. Store alongside the component or route.

---

## Page name

[Name]

## Surface type

[marketing / docs / API console / admin / ops workbench / CRUD list / object detail / setup wizard / mobile task / other]

## User

[Who uses this page and what context they arrive in]

## Primary task

[The single most important thing the user wants to accomplish on this page]

## Entry and journey

- **Entry point / previous step:** [Where the user comes from and what they already know]
- **First decision:** [The first meaningful choice the page asks from the user]
- **Success criterion:** [What proves the task is complete]
- **Next step after success:** [Where the user should continue]

## Secondary tasks

- [Task]
- [Task]

---

## Information priority

What should be most visible, in order:

1. [Most important — conclusion, state, or action]
2. [Second]
3. [Third]

## What must NOT appear on this page

- [Background information that would clutter the task]
- [Internal terms that should be translated or hidden]
- [Data that belongs in a detail surface, not here]

---

## Layout decision

[Why this page uses table / workbench / detail panel / wizard / cards / split pane / etc. Link to the user task.]

## UX risks and recovery

| Risk / state | User impact | Recovery / next step |
|---|---|---|
| [Error / empty / permission / destructive action / long task] | [Impact] | [Retry / undo / request access / change input / details] |

## Mobile priority

[What appears first on narrow screens, what is collapsed, and where the primary action lives]

---

## Components

| Component | Purpose | Existing or new |
|---|---|---|
| [Component] | [What it does here] | [existing: path/to/component | new: justify] |

---

## Required states

- [ ] Loading
- [ ] Empty
- [ ] Error (with reason, impact, and next step)
- [ ] Permission denied
- [ ] Long text / overflow
- [ ] Dense data
- [ ] Mobile / narrow

---

## Copy notes

User-facing words to use:

- [word]

Primary language for labels, states, and actions:

- [language / locale]

Internal terms to translate:

| Internal term | User-facing label |
|---|---|
| [term] | [translation] |

Agent-only context not to show as primary UI copy:

- [implementation detail / design intent / protocol explanation]

---

## Anti-pattern risks

- [Most likely failure mode for this specific page]
- [Journey / friction / recovery risk]

---

## Verification

- [ ] Desktop screenshot
- [ ] Mobile screenshot
- [ ] State screenshots (empty / error / loading)
- [ ] Interaction check
