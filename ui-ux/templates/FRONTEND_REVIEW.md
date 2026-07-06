# FRONTEND_REVIEW.md

> Per-review record. Fill in when reviewing a page or component.
> Attach screenshots where possible.

---

## Context

- **Project:**
- **Page / surface:**
- **Build / screenshot reviewed:**
- **Reviewer:**
- **Date:**

---

## Judgment summary

```text
Verdict:          pass / pass with notes / needs polish / needs refactor / needs restart
Biggest strength:
Biggest risk:
Recommended action:    keep / polish / local refactor / component refactor / page restart
```

---

## Project cognition

- [ ] Page matches the project's human definition
- [ ] User and primary task are clear from the layout
- [ ] Business objects are not incorrectly mixed
- [ ] Page type matches layout and style choice

---

## UX flow

- [ ] Entry point and page orientation are clear
- [ ] First decision and primary action are obvious
- [ ] Information appears in task order, not data-model order
- [ ] Browse / inspect / edit / commit responsibilities are separated
- [ ] User receives clear success / completion feedback after action
- [ ] Error, empty, permission denied, and destructive-action states provide recovery
- [ ] Mobile layout reorders around the primary task instead of only stacking

---

## Human-language copy

- [ ] UI does not paste README or architecture copy
- [ ] UI does not narrate agent reasoning, implementation contracts, or panel purpose as primary copy
- [ ] Review treats examples as context/hierarchy failures, not a string blacklist
- [ ] Technical states are translated to user language
- [ ] Error copy includes reason, impact, and next step
- [ ] Raw IDs / JSON are secondary or hidden unless developer-focused
- [ ] Primary UI language is consistent; protocol/API terms are secondary unless required

---

## Visual and product fit

- [ ] Product temperament is appropriate for this surface
- [ ] Style supports the task rather than decorating it
- [ ] Visual hierarchy is clear
- [ ] UI is not merely a default component-library template
- [ ] Page has product identity without fake-premium decoration

---

## Interaction and states

- [ ] Loading state
- [ ] Empty state
- [ ] Error state
- [ ] Permission denied state with access/request path
- [ ] Success / completion feedback with next step
- [ ] Long-text handling
- [ ] Dangerous action protection (confirmation / undo)
- [ ] Responsive / mobile task layout

---

## Component and system quality

- [ ] Existing components reused where appropriate
- [ ] New components justified (existing components insufficient because…)
- [ ] Table / form / detail responsibilities separated
- [ ] Repeated patterns identified for codification

---

## Findings

| Priority | Finding | Evidence | Suggested fix |
|---|---|---|---|
| P1 | [Blocker] | [Screenshot / code ref] | [Fix] |
| P2 | [Should fix] | | |
| P3 | [Nice to have] | | |

---

## What to codify

After this review, update:

- [ ] `DESIGN.md` — [what changed]
- [ ] `FRONTEND_CONTRACT.md` — [rule added or updated]
- [ ] Storybook story — [component / state]
- [ ] Playwright screenshot — [page / state]
- [ ] Component extraction — [what and where]
