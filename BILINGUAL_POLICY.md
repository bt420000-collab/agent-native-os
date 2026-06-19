# Bilingual Policy for Agent-Native OS

This document defines the bilingual documentation strategy for the public `agent-native-os` GitHub repository.

It is intended for Codex or any repository-maintenance agent that initializes, updates, or refactors the documentation.

## Final policy

Use a bilingual documentation strategy:

```txt
Primary public language: English
Full companion language: Simplified Chinese
Repository identity: English-first, bilingual-friendly
Internal concept origin: Chinese-friendly, not Chinese-only
```

In short:

```txt
English for global developers.
Chinese for original expression, local circulation, and concept precision.
```

## Why bilingual

Agent-Native OS is a technical architecture project. It should be understandable to global AI agent developers, open-source contributors, and researchers.

English is important for:

- GitHub search
- international developer adoption
- citations and references
- AI/agent ecosystem visibility
- technical terminology consistency

Chinese is also important because many of the core ideas were first expressed clearly in Chinese:

- 不是让 AI 接管电脑，是给 AI 装一台自己的电脑。
- 在人类 OS 里，应用是第一公民。在 Agent OS 里，上下文是第一公民。
- 模型框架管脑子，工具框架管手脚，工作流管步骤，Agent OS 管秩序。
- Agent 不缺更多按钮，Agent 缺一个工作场所。

The English version should be precise and professional.

The Chinese version should preserve the conceptual sharpness and original flavor.

## Required bilingual files

These files should exist in both English and Simplified Chinese:

```txt
README.md
README.zh-CN.md

MANIFESTO.md
MANIFESTO.zh-CN.md

SPEC.md
SPEC.zh-CN.md
```

For v0.1, if time is limited, the minimum required bilingual pair is:

```txt
README.md
README.zh-CN.md
```

Recommended v0.1 bilingual set:

```txt
README.md
README.zh-CN.md
MANIFESTO.md
MANIFESTO.zh-CN.md
NAMING_STRATEGY.md
BILINGUAL_POLICY.md
```

## English-first repository rule

The repository root should remain English-first for international readability.

Default files should use English names:

```txt
README.md
MANIFESTO.md
SPEC.md
ROADMAP.md
CODEX_HANDOFF.md
CONTRIBUTING.md
NAMING_STRATEGY.md
BILINGUAL_POLICY.md
```

Chinese versions should use `.zh-CN.md` suffix:

```txt
README.zh-CN.md
MANIFESTO.zh-CN.md
SPEC.zh-CN.md
ROADMAP.zh-CN.md
CONTRIBUTING.zh-CN.md
```

Do not create random mixed-language filenames for core docs.

Good:

```txt
README.zh-CN.md
SPEC.zh-CN.md
docs/zh-CN/context-kernel.md
```

Avoid:

```txt
说明书.md
Agent操作系统规范.md
中文版SPEC.md
readme中文.md
```

## Language navigation

Every major document should link to its companion language version near the top.

In `README.md`, add:

```md
Languages: [English](README.md) | [简体中文](README.zh-CN.md)
```

In `README.zh-CN.md`, add:

```md
语言：[English](README.md) | [简体中文](README.zh-CN.md)
```

In `MANIFESTO.md`, add:

```md
Languages: [English](MANIFESTO.md) | [简体中文](MANIFESTO.zh-CN.md)
```

In `MANIFESTO.zh-CN.md`, add:

```md
语言：[English](MANIFESTO.md) | [简体中文](MANIFESTO.zh-CN.md)
```

## Documentation directory layout

Recommended future layout:

```txt
docs/
  en/
    why-agent-os.md
    computer-use-vs-agent-native.md
    context-kernel.md
    skill-app-runtime.md
    context-abi.md
    failure-modes.md
  zh-CN/
    why-agent-os.md
    computer-use-vs-agent-native.md
    context-kernel.md
    skill-app-runtime.md
    context-abi.md
    failure-modes.md
```

For v0.1, it is acceptable to keep `docs/` English-only if the root README is bilingual.

## Translation style

Do not mechanically translate.

English should sound like a technical open-source project.

Chinese should sound clear, sharp, and natural.

### English style

Use:

```txt
context-native
agent-native
governed workspace
long-running agents
Skill Apps
Context Kernel
Context ABI
Output Contract
Audit Gate
Handoff Report
Recovery Point
```

Tone:

```txt
precise
technical
calm
credible
developer-friendly
```

Avoid:

```txt
hype-only language
vague AI marketing
overclaiming
vendor-specific assumptions
```

### Chinese style

Use:

```txt
上下文原生
Agent 原生
可治理工作空间
长任务 Agent
Skill App / 技能应用
上下文内核
Context ABI / 上下文接口契约
输出契约
审查门禁
交接报告
恢复点
```

Tone:

```txt
锋利
清楚
有技术骨架
保留原始思想表达
```

Avoid:

```txt
生硬机翻
纯营销腔
过度玄学化
把 Agent OS 写成普通提示词工程
```

## Key bilingual terminology

| English | Simplified Chinese |
|---|---|
| Agent-Native OS | Agent 原生操作系统 |
| Context-Native OS | 上下文原生操作系统 |
| Context Kernel | 上下文内核 |
| Skill App | Skill App / 技能应用 |
| Skill App Runtime | 技能应用运行时 |
| Context ABI | Context ABI / 上下文接口契约 |
| Governed Workspace | 可治理工作空间 |
| Source File System | 法源文件系统 |
| Source Law | 法源层级 |
| Source Mount | 资料挂载 |
| Task Card | 任务卡 |
| Output Contract | 输出契约 |
| Audit Gate | 审查门禁 |
| Handoff Report | 交接报告 |
| Recovery Point | 恢复点 |
| Cold Archive | 冷归档 |
| Role Runtime | 角色运行时 |
| Permission System | 权限系统 |
| Failure Modes | 失效模式 / 系统病 |
| Context Overflow | 上下文爆炸 |
| Role Bleeding | 角色串线 |
| Source Pollution | 法源污染 |
| Handoff Amnesia | 交接失忆 |
| Output Drift | 输出漂移 |
| Archive Haunting | 旧档闹鬼 |
| Governable Automation | 可治理自动化 |

## README language priority

The main `README.md` should be English.

Reason:

```txt
GitHub global discovery should work without translation.
```

The Chinese README should be a complete companion, not a short summary.

Reason:

```txt
The Chinese version preserves the concept's original force and helps local developers understand the system without losing nuance.
```

## Do not mix languages randomly

Avoid paragraphs like:

```txt
Agent-Native OS 是一个 context-native operating system for long-running agents，可以 install Skill Apps.
```

Better Chinese:

```txt
Agent-Native OS 是一种面向长任务 AI Agent 的上下文原生操作系统架构，开发者可以在其中安装 Skill App，并组合出可治理的工作流。
```

Better English:

```txt
Agent-Native OS is a context-native operating system architecture for long-running AI agents, where developers can install Skill Apps and compose governed workflows.
```

Technical terms such as `Skill App`, `Context Kernel`, and `Context ABI` may remain in English when useful.

## Version synchronization rule

When updating a major English document, check whether a Chinese companion exists.

If yes, update both or add a note:

```md
> Translation status: This document is pending zh-CN synchronization.
```

When updating a Chinese document first, update the English companion or add:

```md
> Translation status: This document is pending English synchronization.
```

## Codex instruction

When maintaining the repository:

1. Keep `README.md` as the primary English README.
2. Keep `README.zh-CN.md` as the full Simplified Chinese companion.
3. Add language navigation links near the top of bilingual documents.
4. Use `.zh-CN.md` suffix for Simplified Chinese companion files.
5. Do not rename the project into Chinese.
6. Do not make the repository Chinese-only.
7. Do not make the repository English-only if a Chinese companion already exists.
8. Preserve the terminology table above.
9. Use English for GitHub metadata, repository description, topics, and release titles.
10. Use Chinese companion docs for concept depth and local communication.
11. Keep the public repository domain-neutral.
12. Do not add private domain edition content while translating.

## Suggested GitHub repository description

Use English:

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

Optional Chinese description inside README.zh-CN.md:

```txt
面向长任务 AI Agent 与可安装 Skill App 的上下文原生操作系统架构。
```

## First bilingual tasks for Codex

Recommended initial tasks:

1. Ensure `README.md` links to `README.zh-CN.md`.
2. Ensure `README.zh-CN.md` links back to `README.md`.
3. Create `MANIFESTO.zh-CN.md` from `MANIFESTO.md`.
4. Create `SPEC.zh-CN.md` from `SPEC.md` when time allows.
5. Preserve `NAMING_STRATEGY.md` in English, but optionally create `NAMING_STRATEGY.zh-CN.md`.
6. Keep `BILINGUAL_POLICY.md` in English because it is an instruction file for repository automation agents.

## Final rule

The project should be:

```txt
English-first for global open source.
Chinese-complete for original thought and local adoption.
```

Do not choose one language at the cost of the other.
