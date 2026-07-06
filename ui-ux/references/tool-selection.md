# Tool and Component Selection

## Principle

Do not assemble a random tool buffet. Choose tools based on project stage, surface type, product temperament, team needs, and existing code. When a project already has a stack, default to extending it rather than replacing it.

## UI foundation categories

### Source-owned component systems

Project-owned; AI-readable and easily customizable.

- **shadcn/ui registry**: strong default for React + Tailwind projects. Treat it as a baseline — mature into project-specific components and tokens. Do not leave the default shadcn look as the final product.
- **Origin UI and similar shadcn-compatible resources**: useful for additional patterns; review before adopting.

### Headless / primitive behavior

Accessible interaction behavior without inheriting any visual style.

- Radix UI
- Base UI
- React Aria Components
- Ark UI
- Headless UI

Best for: dialogs, popovers, selects, tabs, menus, tooltips, focus management, keyboard interaction.

### Full visual component libraries

Use when speed, coverage, or established conventions matter more than unique brand expression.

- **Ant Design**: strong for Chinese or enterprise admin surfaces; data-entry patterns are mature; visually opinionated.
- **MUI**: broad coverage, Material ecosystem; visually opinionated.
- **Mantine / Chakra / HeroUI**: productive and polished; bring a default face.
- **DaisyUI / Flowbite**: fast Tailwind components; risk of template feel.

Use deliberately — these bring a visual identity you will need to either accept or override.

### Data and admin engines

- **TanStack Table**: recommended for serious data tables with column state, sorting, filtering, row selection. Style separately.
- **TanStack Query**: server-state management.
- **Refine**: headless admin framework for CRUD / auth / data-provider work; not a design system.
- **React Admin**: fast CRUD admin; can constrain product feel.

### Visualization and dashboard

- **Tremor**: useful for analytics / dashboard components and inspiration.
- **Recharts / Visx / ECharts / D3**: choose by customization need and complexity.

### Verification and governance

- **Storybook**: component state documentation and isolated review.
- **Playwright**: user flows, screenshots, responsive checks, visual regression.
- **Accessibility**: axe / playwright-axe where required.

### Design exploration

- **OpenDesign, design galleries, and curated UI inspiration libraries**: useful for exploration and references. Not a final authority for dense tools or admin surfaces.

---

## Recommendations by surface

### API console / developer tool

Prefer:
- React + Vite or Next.js depending on routing / deployment needs.
- shadcn / project-owned components.
- Radix / Base UI / React Aria for interactions.
- Code inspectors, JSON viewers, request history, copy-as-cURL affordances.
- Playwright screenshots.

Avoid landing-page hero treatment.

### Ops / admin console

Prefer:
- Next.js or Vite + React.
- shadcn / project registry, or Ant Design if enterprise conventions dominate.
- TanStack Table.
- TanStack Query.
- Storybook for shared components.
- Playwright for critical flows.

### Novel AI-native product

Prefer:
- Flexible framework + custom design direction.
- Headless primitives for behavior.
- Project-specific tokens.
- Expressive but restrained motion.
- Prototype previews before final implementation.

Avoid old enterprise admin feel unless the product is genuinely an internal console.

### Docs / marketing

Prefer:
- Astro / Next.js / MDX depending on content model.
- Stronger art direction.
- Reference packs from Stripe, Vercel, or Linear-style products where appropriate.

### Half-built project

Prefer preserving the existing stack unless it directly blocks correct product modeling. Refactor by layers before restarting.

---

## Decision output

```text
Recommended stack:
Recommended UI foundation:
Why it fits this product:
Alternatives:
What not to use now:
Upgrade path:
Verification plan:
```
