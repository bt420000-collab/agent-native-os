# Naming Strategy for Agent-Native OS

This document defines the recommended naming structure for the public open-source project.

It is intended for Codex or any repository-maintenance agent that initializes or updates the GitHub repository.

## Final recommendation

Use this as the public repository identity:

```txt
Repository name: agent-native-os
Formal project name: Agent-Native OS
Theory subtitle: Context-Native Operating System for AI Agents
Informal metaphor: Agent Windows
Product category: Skill App Runtime for governed agent workspaces
```

Recommended GitHub repository description:

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

Recommended README opening:

```md
# Agent-Native OS

A context-native operating system architecture for long-running AI agents and installable Skill Apps.

Informally, Agent-Native OS can be understood as the "Windows layer for AI agents": a native workspace where agents can install Skill Apps, manage context, enforce permissions, audit outputs, and preserve long-running project state.
```

## Name hierarchy

| Layer | Name | Usage |
|---|---|---|
| GitHub repository | `agent-native-os` | Stable, searchable, neutral open-source repo name |
| Formal project name | `Agent-Native OS` | README title, documentation, releases |
| Theory name | `Context-Native OS` | Architecture papers, manifesto, design docs |
| Informal metaphor | `Agent Windows` | Talks, social posts, explanations, punchy positioning |
| Core module | `Context Kernel` | Internal architecture component |
| App ecosystem | `Skill App Runtime` | Developer-facing extension model |
| Interface concept | `Context ABI` | Skill App interoperability contract |

## Why `agent-native-os` should be the repository name

`agent-native-os` is the strongest public repository name because it is:

1. Accurate  
   It directly describes an OS architecture designed for AI agents, not humans.

2. Neutral  
   It does not depend on any vendor, platform, model, or GUI metaphor.

3. Searchable  
   It uses clear technical words that developers already understand.

4. Expandable  
   It can support future editions, runtimes, Skill Apps, registries, validators, and adapters.

5. Safer  
   It avoids overusing brand-sensitive names such as Windows in the formal project identity.

## Why not use `Agent Windows` as the repository name

`Agent Windows` is powerful as a metaphor, but it should not be the formal GitHub repository name.

Reasons:

- It may create unnecessary brand or trademark ambiguity.
- It may be misunderstood as an agent that operates Microsoft Windows.
- It may narrow the architecture to a desktop metaphor.
- It is better used as an explanatory phrase, not the legal or technical identity.

Recommended usage:

```txt
Good:
Agent-Native OS is the Windows layer for AI agents.

Avoid:
This project is named Agent Windows.
```

## Why not use `AI OS`

`AI OS` is too broad.

It can be confused with:

- AI desktop environments
- AI PC operating systems
- AI assistants built into existing operating systems
- AI-generated operating systems
- general marketing language

This project is more specific:

```txt
Agent-Native OS is not an OS made by AI.
It is an OS architecture made for AI agents.
```

## Why not use only `Context-Native OS`

`Context-Native OS` is technically precise, but it is colder as a public project name.

It works best as the theory label:

```txt
Agent-Native OS is the project.
Context-Native OS is the architecture philosophy.
```

## Recommended slogans

Primary slogan:

```txt
Stop teaching agents only to use human desktops.
Give them a native workspace.
```

Short slogan:

```txt
The Windows layer for AI agents.
```

Technical slogan:

```txt
A context-native operating system architecture for long-running AI agents.
```

Developer slogan:

```txt
Install Skill Apps. Govern context. Compose reliable agent workflows.
```

Chinese slogan:

```txt
别只教 Agent 使用人类桌面。
给它们一个原生工作空间。
```

Short Chinese slogan:

```txt
Agent-Native OS 是 AI Agent 的 Windows 层。
```

## Positioning sentence

Use this sentence when describing the project:

```txt
Agent-Native OS is an open architecture for installing and running Skill Apps inside governed, context-aware agent workspaces.
```

Chinese version:

```txt
Agent-Native OS 是一种开放架构，用于在可治理、上下文感知的 Agent 工作空间中安装和运行 Skill App。
```

## Repository topics

Suggested GitHub topics:

```txt
ai-agents
agent-os
agent-native
context-engineering
context-native
multi-agent
skill-apps
workflow-automation
agent-framework
ai-native
```

## README naming block

Add this near the top of the README if needed:

```md
## Naming

This project is formally named **Agent-Native OS**.

Its core architecture is a **Context-Native Operating System for AI Agents**.

Informally, it can be described as **Agent Windows**, meaning a Windows-like system layer for agents where developers can install Skill Apps and compose governed workflows.

The repository name is `agent-native-os`.
```

## Domain edition naming rule

The public open-source repository should remain domain-neutral.

Correct:

```txt
Agent-Native OS
Agent-Native OS: Docs Edition
Agent-Native OS: Research Edition
Agent-Native OS: Product Docs Edition
```

Avoid exposing private domain editions in the public repository.

Use this rule:

```txt
Open the architecture.
Keep private editions private.
```

## Codex instruction

When initializing or updating the GitHub repository:

1. Use `agent-native-os` as the repository name.
2. Use `Agent-Native OS` as the project title.
3. Use `Context-Native OS` as the theory subtitle.
4. Use `Agent Windows` only as an informal metaphor.
5. Do not rename the project to `Agent Windows`, `AI OS`, or `AgentOS`.
6. Do not add private domain edition materials to the public repository.
7. Keep the project description focused on long-running AI agents, context governance, Skill Apps, and reliable workflows.

## Final naming decision

```txt
Repository: agent-native-os
Project: Agent-Native OS
Theory: Context-Native OS
Metaphor: Agent Windows
Ecosystem: Skill Apps
Kernel: Context Kernel
Interface: Context ABI
```
