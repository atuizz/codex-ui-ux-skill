# DESIGN.md

> Project-level frontend design memory for AI agents and humans.
> Update after previews, direction choices, reviews, and repeated implementation lessons.
> Do not paste this document into normal UI — it is internal agent context.

---

## 1. Project in human words

[One or two sentences a normal user could understand. No architecture, no internal terms.]

---

## 2. Core users

- [User group and what they need from this product]
- [User group and what they need from this product]

---

## 3. Core business objects

| Object | What it means to the user | Should appear where | Must not be mixed with |
|---|---|---|---|
| [Object] | [Human meaning] | [Pages / surfaces] | [Boundaries] |

---

## 4. Core journeys

| Journey | Entry point | First decision | Success criterion | Recovery path |
|---|---|---|---|---|
| [Journey] | [Where users arrive from] | [First choice] | [Done means…] | [How users recover] |

---

## 5. Product temperament

Choose one or combine deliberately:

- [ ] Developer Precision
- [ ] AI Native Future
- [ ] Enterprise Ops
- [ ] Commerce Trust
- [ ] Content Ops
- [ ] Public Marketing / Consumer Delight

**Why:** [Reason this temperament fits the product and users]

---

## 6. Reference systems

| Reference | Borrow | Avoid |
|---|---|---|
| [GitHub Primer / Stripe / Carbon / etc.] | [Patterns and principles to adopt] | [What not to clone] |

---

## 7. UI foundation

| Decision | Choice | Notes |
|---|---|---|
| Framework | | |
| Component foundation | | |
| Table / data strategy | | |
| Form strategy | | |
| Storybook | enabled / deferred | |
| Playwright / visual QA | enabled / deferred | |

---

## 8. Visual direction

| Dimension | Decision |
|---|---|
| Density | compact / balanced / spacious |
| Typography | |
| Color tone | |
| Radius / shadow | |
| Motion | restrained / purposeful / none |
| Icon style | |
| Mobile approach | task-reorder / responsive / dedicated |

---

## 9. Vocabulary

### User-facing words (use in UI)

- [word]
- [word]

### Internal terms to keep secondary (translate or hide)

| Internal term | Human translation | Where to surface |
|---|---|---|
| [term] | [translation] | detail / tooltip / diagnostic / never |

---

## 10. Page patterns

| Page / surface | Preferred pattern | Hard lines |
|---|---|---|
| [e.g. API console] | [e.g. Request workbench + result + raw details] | [e.g. No hero] |
| [e.g. Admin list] | [e.g. Filter + table + detail drawer] | [e.g. No inline config] |

---

## 11. UX principles for this project

Record project-level UX decisions here so future agents do not re-derive them
from scratch on every page.

### Primary task before background explanation

- [What the user must do first on core pages]
- [What context may be shown only after the task/action is clear]
- [Background, architecture, or docs content that must stay out of primary UI]

### Default recovery paths

| State / risk | Default recovery | Notes |
|---|---|---|
| Empty | [Create / import / connect / request access] | |
| Error | [Retry / change input / view details / contact owner] | |
| Permission denied | [Request access / switch account / contact admin] | |
| Destructive action | [Confirm scope / undo / restore] | |
| Long-running action | [Progress / safe cancel / resume / notification] | |

### Mobile task priority

- [What appears first on narrow screens]
- [What collapses or moves below the primary action]
- [Which desktop table/detail pattern becomes a mobile list, drawer, or step flow]

---

## 12. Anti-patterns to watch for this project

- [Most likely failure mode for this product]
- [Second most likely]

---

## 13. Screenshot / QA requirements

Core pages must capture:

- [ ] Desktop
- [ ] Mobile
- [ ] Loading state
- [ ] Empty state
- [ ] Error state
- [ ] Long-text / dense-data state

---

## 14. Change log

| Date | Change | Reason |
|---|---|---|
| [date] | [what changed] | [why] |
