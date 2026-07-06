# Project Cognition and Human-Language Copy

## Why this matters

Many AI frontend failures are not CSS failures. They happen because the agent starts UI work before understanding the product. When project cognition is missing, the model falls back to generic SaaS dashboards, card walls, CRUD tables, landing heroes, and README-on-screen copy.

## Project cognition checklist

Before significant frontend work, answer:

- What does this project do in one sentence a normal user could understand?
- Who uses this page?
- What are the project's core business objects?
- What should the user decide or do on this screen?
- What step brought the user here, and what should happen after success?
- What can go wrong, and how should the user recover?
- What information is background context for the agent but should not be displayed?
- Which terms are user-facing and which are internal implementation terms?
- Which states require explanation and next actions?
- Which operations are risky?

## Human-language copy rule

Default UI copy uses user language. Technical terms belong in diagnostic areas, raw inspectors, developer mode, tooltips, or expandable details — unless the page is explicitly for developers.

Before writing page copy, split context into two buckets:

| Bucket | Belongs where | Example |
|---|---|---|
| Agent / implementation context | Code, docs, comments, tooltips, diagnostics, governance docs | "JSON is diagnostic only", "resource resolution uses search → resources → resolve" |
| User action context | Primary UI labels, states, empty/error/success copy | "搜索已完成，未找到匹配资源", "选择一个结果查看可下载资源" |

Do not paste the first bucket into the second. This is the most common source of GPT/Codex self-narrating UI.

Hierarchy:

```
Human conclusion → operational detail → technical diagnostics
```

Avoid:

```
internal_term=true → code → raw object → user must infer what happened
```

Also avoid:

```text
Design intent / implementation explanation → primary UI copy
```

## Status translation pattern

When a technical state surfaces in the UI, translate it:

| Technical state | User-facing label | Explanation / next step |
|---|---|---|
| `STATE_CODE` | Short human label | What happened and what to do |

Examples:

- `SOURCE_NOT_FOUND` → **书源不存在** — 当前选择的书源没有启用，请切换到自动或检查后台配置。
- `retryable=false` → **此错误无法通过重试解决。**
- `needs_recovery` → **需要恢复** — 上次操作未完成，点击恢复继续。
- `persisting` → **正在保存**
- `indexing` → **正在建立索引**
- `dispatch` → **已放行**
- `ignore` → **已拦截**

## Project vocabulary template

Fill this in for every project before implementation:

```text
Project in one sentence:

Core users:

Core business objects:
  - [Object]: what it means to the user, not to the code

Core journeys:
  - [Entry] → [first decision] → [primary action] → [feedback] → [recovery if needed] → [completion]

User-facing words (use these in UI):
  - [word]
  - [word]

Internal terms to keep secondary (translate or hide):
  - [term] → [human translation]
  - [term] → [human translation]

Agent-only context that should not appear as primary UI copy:
  - [implementation note / design intent] → [where it belongs: docs / tooltip / diagnostic / code comment]

States that need explanation and next-step copy:
  - [state]: [what it means] + [what user should do]

Risky operations (require confirmation or undo):
  - [operation]
```

## Illustration: applying the template

The following is one example of a filled-in vocabulary template. Use it to understand the format — do not copy its content into unrelated projects.

```text
Project in one sentence:
  A Telegram book-search bot that receives, stores, searches,
  and downloads books, and exposes library capabilities to other systems.

Core users:
  Bot operators and book library administrators.

Core business objects:
  - 书库: the library of books stored in Telegram
  - 书籍: a single book record
  - 导入任务: a pending or completed ingestion job

User-facing words:
  - 书库 / 找书 / 搜书 / 收录 / 上传 / 下载 / 书籍恢复 / 导入失败 / 可搜索 / 重试

Internal terms to keep secondary:
  - intake → 收录任务
  - replica → 备份副本
  - tg_file_id → Telegram 文件 ID（放在详情面板）
  - source_path → 原始路径（放在诊断区）
  - HMAC ticket → 访问凭证（不展示给非开发用户）

States needing translation:
  - needs_recovery → 需要恢复 — 上传未完成，点击恢复。
  - indexing → 正在建立索引 — 文件已上传，稍后可搜索。

Risky operations:
  - 删除书籍（批量）: 需要二次确认，说明影响范围。
```
