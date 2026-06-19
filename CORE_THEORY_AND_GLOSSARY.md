# Core Theory and Glossary for Agent-Native OS

This document defines the core theory, standard terminology, and glossary for the `agent-native-os` project.

Status: vocabulary authority and theory primer.

It is intended for new readers, contributors, Codex, and any repository-maintenance agent that initializes, edits, translates, or extends the public GitHub repository.

## 0. Document purpose

This file is the vocabulary authority for the public project.

When future documentation, specs, examples, schemas, CLI commands, or Skill App templates introduce related concepts, they should align with this document.

Core rule:

```txt
Do not turn Agent-Native OS into a generic prompt pack, workflow template, or GUI automation tool.
```

Agent-Native OS is an operating system architecture for agent-native work.

---

# 1. Core thesis

## 1.1 Old human software stack

In the traditional human software stack:

```txt
Natural language describes intent.
Programming languages become executable code.
Machines execute code.
Outputs and interfaces are designed for humans.
```

Short form:

```txt
Old stack:
Code for machines.
UI and output for humans.
```

Chinese:

```txt
旧架构：
代码是给机器执行的。
界面和输出是给人理解的。
```

## 1.2 New agent-native stack

In the agent-native stack:

```txt
Contracted natural language becomes executable context.
Context Kernel runs the agent workspace.
Structured output becomes the interface for the next agent, tool, audit gate, or human reviewer.
```

Short form:

```txt
Agent-native stack:
Language as source code.
Context as runtime.
Structured output as ABI.
```

Chinese:

```txt
Agent 原生架构：
自然语言即源代码。
上下文即运行时。
结构化输出即接口协议。
```

## 1.3 Main architecture shift

The key shift is not that agents can read prompts.

The key shift is that scoped, versioned, permissioned, and contract-bound natural language can behave like source code for agents.

Canonical principle:

```txt
In Agent-Native OS, natural language becomes source code when it is scoped, versioned, permissioned, and contract-bound.
```

Chinese:

```txt
在 Agent-Native OS 里，自然语言一旦具备作用域、版本、权限和输出契约，它就不再只是说明文字，而是源代码。
```

---

# 2. Five core principles

These principles should appear consistently across the project.

## Principle 1: Context is the first-class resource

```txt
In a human OS, the first-class citizen is the application.
In an Agent OS, the first-class citizen is the context.
```

Chinese:

```txt
在人类 OS 里，应用是第一公民。
在 Agent OS 里，上下文是第一公民。
```

Agent systems fail when context becomes bloated, stale, polluted, unauthorized, contradictory, or ungoverned.

## Principle 2: Contracted natural language is source code

Loose natural language is intention.

Contracted natural language is code.

```txt
Loose natural language = intention.
Contracted natural language = source code.
```

Chinese:

```txt
松散自然语言是意图。
契约化自然语言才是源代码。
```

A sentence like "help me organize this project" is not code.

A Task Card with role, source mount, permissions, forbidden paths, output contract, and audit gate is executable agent source.

## Principle 3: Context Kernel is the runtime

The Context Kernel decides what an agent can know, do, change, and hand off.

It is the runtime layer of the agent workspace.

## Principle 4: Structured output is the Context ABI

Agent output is no longer only a human-facing document.

It becomes structured state for the next agent, tool, audit gate, script, or human reviewer.

```txt
JSON is not the user interface.
JSON is the handoff interface.
```

Chinese:

```txt
JSON 不是用户界面。
JSON 是交接界面。
```

## Principle 5: Skill Apps are installable applications

Skill Apps are to Agent-Native OS what applications are to human operating systems.

A Skill App is not just a prompt.

It is an installable, permissioned, contract-bound, auditable capability package.

---

# 3. Stack comparison

## 3.1 Traditional software stack

```txt
Human intent
  ↓
Natural language requirements
  ↓
Programming language
  ↓
Compiler / interpreter
  ↓
Machine execution
  ↓
Human-facing UI / output
```

## 3.2 Agent-native software stack

```txt
Human intent
  ↓
Contracted natural language
  ↓
Context Kernel
  ↓
Agent execution
  ↓
Structured output / Context ABI
  ↓
Next Agent / Tool / Audit Gate / Human Review
```

## 3.3 Short comparison

```txt
Old world:
Natural language describes the program.
Code runs the program.

Agent-native world:
Natural language becomes the program.
Context runs the work.
Structured state carries the work forward.
```

Chinese:

```txt
旧世界：
自然语言描述程序，代码运行程序。

Agent 原生世界：
自然语言成为程序，上下文运行工作，结构化状态接力工作。
```

---

# 4. Agent-Native OS definition

## 4.1 Formal definition

```txt
Agent-Native OS is a context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

Expanded definition:

```txt
Agent-Native OS is an open architecture for installing and running Skill Apps inside governed, context-aware agent workspaces.
```

Chinese:

```txt
Agent-Native OS 是一种开放架构，用于在可治理、上下文感知的 Agent 工作空间中安装和运行 Skill App。
```

## 4.2 What it is not

Agent-Native OS is not:

```txt
a prompt pack
a chatbot framework
a GUI automation tool
a simple workflow template
a single-agent script
a vendor-specific agent platform
a domain-specific private edition
```

## 4.3 What it governs

Agent-Native OS governs:

```txt
context
sources
roles
permissions
tasks
Skill Apps
outputs
audits
handoffs
archives
recovery points
long-running project state
```

---

# 5. Core architecture

```txt
Agent-Native OS
│
├─ Context Kernel
├─ Skill App Runtime
├─ Source File System
├─ Role & Permission System
├─ Task Scheduler
├─ Output Contract Engine
├─ Audit Gate
├─ Handoff Bus
├─ Memory & Archive Layer
└─ Recovery System
```

## 5.1 Context Kernel

The runtime layer that decides what an agent can know, do, change, and hand off.

Responsibilities:

```txt
load task context
mount approved sources
apply source priority
enforce role permissions
select Skill App
check output contract
trigger audit gate
create handoff report
write recovery point
archive stale materials
```

## 5.2 Skill App Runtime

The runtime that installs, loads, executes, composes, audits, disables, and removes Skill Apps.

A Skill App should include:

```txt
manifest.yaml
instructions.md
input_contract.md
output_contract.md
permissions.yaml
source_policy.md
examples/
tests/
changelog.md
```

## 5.3 Source File System

A source system that treats files as authority-bearing materials, not ordinary documents.

Source states:

```txt
hot       loaded into current task context
warm      available for lookup
cold      archived, not loaded by default
forbidden explicitly blocked
```

## 5.4 Role & Permission System

Roles are runtime permissions, not cosmetic names.

A role declares:

```txt
read permissions
write permissions
forbidden paths
allowed Skill Apps
audit authority
mutation policy
```

## 5.5 Task Scheduler

The scheduler turns broad goals into isolated, contract-bound task runs.

## 5.6 Output Contract Engine

The output contract engine ensures agent output has a required type, path, structure, validation rule, and completion checklist.

## 5.7 Audit Gate

The audit gate prevents unaudited work from entering the mainline.

## 5.8 Handoff Bus

The handoff bus makes task results portable across agents, sessions, tools, and audits.

## 5.9 Memory & Archive Layer

The memory layer distinguishes current truth, working memory, reference material, old versions, and deprecated sources.

## 5.10 Recovery System

The recovery system records what changed, why, by whom, under which task, and how to roll back or repair.

---

# 6. Natural language as source code

## 6.1 Non-code natural language

This is intention:

```txt
Help me organize this project.
```

This is too loose for reliable agent execution.

## 6.2 Contracted natural language

This is source code for agent work:

```txt
Role:
Researcher

Task:
Read mounted sources and produce a structured project brief.

Readable Sources:
- mounted_sources/current_requirements.md
- mounted_sources/design_notes.md

Forbidden:
- archive/deprecated/
- source_law/

Output Contract:
- Summary
- Key Findings
- Unknowns
- Risks
- Next Steps

Audit:
Required by Host before mainline merge.
```

## 6.3 Required properties of contracted natural language

Natural language becomes agent source code when it has:

```txt
scope
role
task goal
source mount
permission boundary
forbidden materials
output contract
audit gate
handoff requirement
version or task identity
```

## 6.4 Recommended term

Use:

```txt
Contracted Natural Language
```

Chinese:

```txt
契约化自然语言
```

Do not reduce this concept to "prompt".

Prompt engineering writes instructions.

Agent OS writes executable context.

Chinese:

```txt
提示词工程写指令。
Agent OS 编写可执行上下文。
```

---

# 7. Structured output as Context ABI

## 7.1 Definition

```txt
Context ABI is the contract that defines how Skill Apps receive context, produce outputs, declare uncertainty, request permissions, and hand off state.
```

Chinese:

```txt
Context ABI 是 Skill App 接收上下文、产出结果、声明不确定性、请求权限和交接状态的接口契约。
```

## 7.2 Why "ABI"

In traditional software, ABI defines a low-level interface for binary compatibility.

In Agent-Native OS, Context ABI defines compatibility between agent tasks, Skill Apps, tools, audits, scripts, and future sessions.

It defines how work survives beyond one conversation.

## 7.3 Context ABI should cover

```txt
inputs
outputs
permissions
source policy
uncertainty policy
mutation policy
audit policy
handoff fields
status values
error format
recovery hints
```

## 7.4 Supported interface formats

Context ABI can be expressed through:

```txt
JSON
YAML
Markdown frontmatter
Typed Markdown
Contract Markdown
CSV
NDJSON
SQLite
other structured formats
```

The project should not lock the theory to JSON only.

Preferred default for documents:

```txt
Typed Markdown with machine-readable frontmatter.
```

## 7.5 Typed Markdown example

```md
---
artifact_type: audit_report
task_id: TASK-003
status: needs_revision
approved_for_mainline: false
severity: high
---

# Audit Report

## Findings

1. Source pollution detected.

## Required Fixes

- Remove deprecated source reference.
- Regenerate using mounted sources only.

## Next Step

Return to Writer role for revision.
```

This format has three advantages:

```txt
human-readable
agent-readable
script-parseable
```

## 7.6 JSON example

```json
{
  "artifact_type": "audit_report",
  "task_id": "TASK-003",
  "status": "needs_revision",
  "approved_for_mainline": false,
  "findings": [
    {
      "severity": "high",
      "type": "source_pollution",
      "message": "Output references deprecated source material.",
      "required_fix": "Remove deprecated reference and regenerate from mounted sources only."
    }
  ],
  "next_step": "Return to Writer role for revision."
}
```

---

# 8. Standard glossary

This glossary is the authoritative terminology table for the project.

## 8.1 Project identity terms

| Term | Chinese | Definition |
|---|---|---|
| Agent-Native OS | Agent 原生操作系统 | A context-native operating system architecture for long-running AI agents and installable Skill Apps. |
| Context-Native OS | 上下文原生操作系统 | The theory that agent systems should be built around context rather than human UI metaphors. |
| Agent Windows | Agent 的 Windows 层 | Informal metaphor for a Windows-like system layer where agents can install Skill Apps and compose governed workflows. Use as metaphor only, not formal project name. |
| Agent Workspace | Agent 工作空间 | A project environment governed by Agent-Native OS. |
| Governed Workspace | 可治理工作空间 | A workspace with context, permissions, contracts, audits, handoffs, and recovery. |

## 8.2 Core architecture terms

| Term | Chinese | Definition |
|---|---|---|
| Context Kernel | 上下文内核 | Runtime layer deciding what an agent can know, do, change, and hand off. |
| Skill App Runtime | 技能应用运行时 | System for installing, loading, running, composing, auditing, and disabling Skill Apps. |
| Source File System | 法源文件系统 | File system that treats source materials as authority-bearing context. |
| Role Runtime | 角色运行时 | Runtime permission model for agent roles. |
| Permission System | 权限系统 | Rules controlling read, write, mutation, tool, and audit authority. |
| Task Scheduler | 任务调度器 | System that creates, isolates, and dispatches task runs. |
| Output Contract Engine | 输出契约引擎 | System that enforces output structure, path, type, and validation rules. |
| Audit Gate | 审查门禁 | Checkpoint that blocks work from entering mainline until reviewed. |
| Handoff Bus | 交接总线 | Mechanism that transfers structured task state across agents and sessions. |
| Memory & Archive Layer | 记忆与归档层 | Layer separating hot context, warm reference, cold archive, and forbidden material. |
| Recovery System | 事故恢复系统 | System for recording changes, incidents, rollback hints, and repair paths. |

## 8.3 Source and context terms

| Term | Chinese | Definition |
|---|---|---|
| Context | 上下文 | The active cognitive environment an agent uses to perform work. |
| Context Budget | 上下文预算 | Limit and policy controlling how much and which context enters a task. |
| Hot Context | 热上下文 | Materials loaded directly into current task context. |
| Warm Context | 温资料 | Searchable or reference material not loaded by default. |
| Cold Archive | 冷归档 | Preserved material excluded from default context. |
| Forbidden Source | 禁用资料 | Material explicitly blocked from a task. |
| Source Law | 法源层级 | Authority hierarchy of source materials. |
| Source Mount | 资料挂载 | The act of making selected sources available to a task. |
| Source Policy | 法源策略 | Rules for source priority, conflict resolution, and access. |
| Source Pollution | 法源污染 | Failure mode where old, deprecated, or unconfirmed material contaminates active work. |
| Archive Haunting | 旧档闹鬼 | Failure mode where cold or deprecated material repeatedly contaminates current work. |

## 8.4 Task and contract terms

| Term | Chinese | Definition |
|---|---|---|
| Task Card | 任务卡 | Contract-bound unit of work for an agent. |
| Output Contract | 输出契约 | Specification of what the agent must produce, where, and in what structure. |
| Input Contract | 输入契约 | Specification of what the Skill App or task expects to receive. |
| Handoff Report | 交接报告 | Structured continuation state produced after a task. |
| Audit Report | 审查报告 | Structured review output from an audit gate. |
| Incident Report | 事故报告 | Record of failure, cause, impact, and prevention rule. |
| Recovery Point | 恢复点 | Record enabling change tracing, rollback, or repair. |
| Mainline | 主线 | Approved current project state. |
| Mutation Policy | 修改策略 | Rule defining what a role or Skill App may modify. |

## 8.5 Skill App terms

| Term | Chinese | Definition |
|---|---|---|
| Skill App | Skill App / 技能应用 | Installable, permissioned, contract-bound agent capability package. |
| Skill Manifest | 技能声明文件 | Manifest defining a Skill App's metadata, inputs, outputs, permissions, and policies. |
| Skill Registry | 技能注册表 | Registry of installed Skill Apps, versions, permissions, and dependencies. |
| Skill Lock | 技能锁文件 | Lock file recording exact installed Skill App versions. |
| Skill Permission | 技能权限 | Declared read, write, tool, mutation, and audit permissions. |
| Skill Dependency | 技能依赖 | Another Skill App or runtime capability required by a Skill App. |
| Skill Composition | 技能组合 | Chaining or combining multiple Skill Apps into a governed workflow. |

## 8.6 Interface terms

| Term | Chinese | Definition |
|---|---|---|
| Context ABI | Context ABI / 上下文接口契约 | Interface contract defining how Skill Apps receive context, output state, declare uncertainty, request permissions, and hand off work. |
| Typed Markdown | 类型化 Markdown | Markdown document with machine-readable metadata, usually frontmatter. |
| Contract Markdown | 契约化 Markdown | Markdown format where structure and metadata are part of an output contract. |
| Structured Output | 结构化输出 | Output designed for agent, tool, script, or audit continuation. |
| Artifact | 产物 | Any output generated by a task or Skill App. |
| Artifact Metadata | 产物元数据 | Machine-readable metadata describing artifact type, status, task id, role, and audit state. |
| Handoff Interface | 交接接口 | Structured form through which work passes to the next actor. |

## 8.7 Failure mode terms

| Term | Chinese | Definition |
|---|---|---|
| Context Overflow | 上下文爆炸 | Too much context enters the task and priority collapses. |
| Role Bleeding | 角色串线 | A role exceeds or confuses its runtime responsibility. |
| Handoff Amnesia | 交接失忆 | A task ends without usable continuation state. |
| Output Drift | 输出漂移 | Output gradually deviates from required format, goal, or style. |
| Unauthorized Mutation | 越权修改 | Agent modifies files, sources, or state without permission. |
| Review Collapse | 审查失效 | Important work enters mainline without audit. |
| User Override Loss | 用户意见丢失 | Latest user instruction fails to enter the proper authority level. |
| Long-Run Degradation | 长程退化 | Project coherence decays across many tasks or sessions. |
| Semantic Drift | 语义漂移 | Meaning, intent, or project direction gradually shifts without explicit decision. |

## 8.8 Programming model terms

| Term | Chinese | Definition |
|---|---|---|
| Contracted Natural Language | 契约化自然语言 | Natural language with scope, role, source mount, permissions, output contract, and audit requirements. |
| Executable Context | 可执行上下文 | Context package that can guide an agent task as source code guides a machine. |
| Context Program | 上下文程序 | A task or workflow expressed as contracted natural language plus structured contracts. |
| Agent Source Code | Agent 源代码 | Contracted natural language and structured policies that drive agent behavior. |
| Context Runtime | 上下文运行时 | Runtime environment formed by Context Kernel, mounted sources, role, permissions, and contracts. |
| Governable Automation | 可治理自动化 | Automation that is traceable, auditable, permissioned, recoverable, and composable. |

---

# 9. Recommended normative language

Use these phrases consistently.

## 9.1 English phrases

```txt
Agent-Native OS is not a prompt pack.
It is a context-native operating system architecture for long-running agents.

Context is the first-class resource.

Contracted natural language is source code.

Context Kernel is the runtime.

Structured output is the Context ABI.

Skill Apps are installable applications.

Prompt engineering writes instructions.
Agent OS writes executable context.

Computer-use is a driver.
Agent OS is the governance layer.

LLM frameworks call models.
Agent frameworks call tools.
Workflow engines arrange steps.
Agent-Native OS governs long-running agent work.
```

## 9.2 Chinese phrases

```txt
Agent-Native OS 不是提示词包。
它是面向长任务 Agent 的上下文原生操作系统架构。

上下文是第一资源。

契约化自然语言是源代码。

上下文内核是运行时。

结构化输出是 Context ABI。

Skill App 是可安装应用。

提示词工程写指令。
Agent OS 编写可执行上下文。

Computer Use 是驱动层。
Agent OS 是治理层。

模型框架管模型调用。
Agent 框架管工具调用。
工作流引擎管步骤编排。
Agent-Native OS 管长期 Agent 工作的秩序。
```

---

# 10. Codex instructions

When Codex updates the repository, follow these rules.

## 10.1 Vocabulary rules

1. Use `Agent-Native OS` as the formal project name.
2. Use `agent-native-os` as the repository name.
3. Use `Context-Native OS` as the theory label.
4. Use `Agent Windows` only as an informal metaphor.
5. Use `Context Kernel`, not "prompt manager".
6. Use `Context ABI`, not "JSON output format" when describing inter-agent compatibility.
7. Use `Skill App`, not "prompt template" when referring to installable capabilities.
8. Use `Contracted Natural Language`, not "prompt" when the text has scope, permissions, and output contracts.
9. Use `Governed Workspace`, not "chat folder" or "workflow folder".
10. Use `Source Law` or `Source Policy`, not "reference docs" when authority matters.

## 10.2 Architecture rules

1. Keep the project domain-neutral.
2. Do not introduce private domain editions into the public repository.
3. Do not define Agent-Native OS as GUI automation.
4. Do not define Agent-Native OS as merely a workflow engine.
5. Do not lock Context ABI to JSON only.
6. Prefer Typed Markdown with frontmatter for human-readable artifacts.
7. Use JSON/YAML where machine validation is needed.
8. Keep English as primary public documentation language.
9. Keep Simplified Chinese as complete companion documentation.
10. Preserve terminology consistency across docs.

## 10.3 Documentation update rule

If adding a new concept, classify it under one of these categories:

```txt
project identity
core architecture
source and context
task and contract
Skill App
interface
failure mode
programming model
```

If it does not fit any category, reconsider whether it belongs in the core spec.

## 10.4 Do not dilute the theory

Avoid replacing precise concepts with generic words.

Bad:

```txt
This is a prompt workflow system.
```

Good:

```txt
This is a context-native operating system architecture for governed agent workspaces.
```

Bad:

```txt
The output should be JSON so AI can read it.
```

Good:

```txt
Structured output forms the Context ABI, allowing the next agent, tool, audit gate, or human reviewer to continue work reliably.
```

Bad:

```txt
The agent reads some files.
```

Good:

```txt
The Context Kernel mounts approved sources into hot, warm, cold, or forbidden context according to Source Policy.
```

---

# 11. Canonical summary

Use this as the short theoretical summary:

```txt
Agent-Native OS is built on five principles:

1. Context is the first-class resource.
2. Contracted natural language is source code.
3. Context Kernel is the runtime.
4. Structured output is the Context ABI.
5. Skill Apps are installable applications.

The old software stack used code to drive machines and UI to serve humans.

The agent-native stack uses contracted natural language to drive agents, context to run work, and structured output to hand off state across agents, tools, audits, and humans.
```

Chinese:

```txt
Agent-Native OS 建立在五个原则上：

1. 上下文是第一资源。
2. 契约化自然语言是源代码。
3. 上下文内核是运行时。
4. 结构化输出是 Context ABI。
5. Skill App 是可安装应用。

旧软件栈用代码驱动机器，用界面服务人类。

Agent 原生软件栈用契约化自然语言驱动 Agent，用上下文运行工作，用结构化输出在 Agent、工具、审查门禁和人类之间交接状态。
```

---

# 12. One-line essence

English:

```txt
Agent-Native OS turns natural-language instructions into executable context and turns agent outputs into structured state for reliable continuation.
```

Chinese:

```txt
Agent-Native OS 把自然语言指令变成可执行上下文，把 Agent 输出变成可可靠接力的结构化状态。
```
