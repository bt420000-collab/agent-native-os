# Agent-Native OS

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

A context-native operating system architecture for long-running AI agents and installable Skill Apps.

![Spec](https://img.shields.io/badge/spec-v0.2-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

<p align="center">
  <img src="docs/assets/homepage/poster-not-human-desktop.png" alt="Not letting AI take over human computers, but giving AI its own computer" width="88%" />
</p>

<p align="center">
  <img src="docs/assets/homepage/poster-token-effective-work.png" alt="Spend tokens on effective work" width="43%" />
  <img src="docs/assets/homepage/poster-robot-os-standard.png" alt="Build operating system standards for the next generation of intelligent robots" width="43%" />
</p>

> **Not teaching AI to use human desktops.**  
> **Giving AI a computer of its own.**

Agent-Native OS is not an operating system for humans.
It is a native operating layer for large-model agents: a governed workspace where agents can install Skill Apps, manage context, isolate tasks, enforce permissions, hand off state, and keep long-running work coherent.

Informally, you can think of it as **the Windows layer for AI agents**.

## Why this project exists

Most AI tooling today is focused on making agents better at using human computers: browsers, terminals, GUIs, APIs, and app workflows.

Agent-Native OS asks a deeper systems question:

> **What kind of operating system does an agent need for its own work?**

This project exists because agent work has its own failure modes:

- context overflow
- source pollution
- role bleeding
- broken handoffs
- unaudited outputs
- long-run degradation
- massive token waste across messy workflows

Agent-Native OS is designed to reduce that waste and make every token more likely to contribute to effective work.

## What it means

In a human OS, the first-class citizen is the application.

In an Agent OS, the first-class citizen is the context.

Agent-Native OS is an open architecture for:

- Context Kernel
- Skill App Runtime
- Source File System
- Role & Permission System
- Task Scheduler
- Output Contract Engine
- Audit Gate
- Handoff Bus
- Memory & Archive Layer
- Recovery System

## Five principles

1. **Context is the first-class resource.**
2. **Contracted natural language is source code.**
3. **Context Kernel is the runtime.**
4. **Structured output is the Context ABI.**
5. **Skill Apps are installable applications.**

## Why it matters beyond software

Agent-Native OS is not only about documentation or coding agents.
It points toward a broader infrastructure layer for the next generation of intelligent systems.

Potential impact areas:

- more efficient AI work pipelines
- lower token waste through governed context use
- more reliable multi-agent collaboration
- clearer standards for permissions, audits, and recovery
- foundational norms for future embodied or robotic operating systems

## Visual overview

### 1) From code-for-machines to context-for-agents

<p align="center">
  <img src="docs/assets/homepage/diagram-from-code-to-agents.png" alt="From code for machines to context for agents" width="82%" />
</p>

### 2) System architecture and operating loop

<p align="center">
  <img src="docs/assets/homepage/diagram-core-architecture.png" alt="Core architecture" width="46%" />
  <img src="docs/assets/homepage/diagram-operating-loop.png" alt="Operating loop" width="46%" />
</p>

### 3) Agent-native system and workspace layout

<p align="center">
  <img src="docs/assets/homepage/diagram-agent-native-system.png" alt="Agent-native system" width="46%" />
  <img src="docs/assets/homepage/diagram-workspace-layout.png" alt="Workspace layout" width="46%" />
</p>

## Try the demo

Run:

```bash
python scripts/run_docs_brief_demo.py
```

Then open:

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

Copy the prompt into your coding agent or LLM and let it produce governed outputs.

Validate the workspace:

```bash
python scripts/validate_workspace.py examples/docs-brief-demo
```

The demo shows the minimal operating loop:

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

## Repository map

```txt
agent-native-os/
  README.md
  README.zh-CN.md
  MANIFESTO.md
  SPEC.md
  ROADMAP.md
  CORE_THEORY_AND_GLOSSARY.md
  NAMING_STRATEGY.md
  BILINGUAL_POLICY.md
  docs/
  spec/
  templates/
  examples/
  scripts/
```

## Public core, private editions

This repository defines the open architecture.

Domain-specific private editions can be built on top of it. Private editions may contain domain craft, business logic, specialized scoring systems, or proprietary workflows, and are intentionally not included.

**Open the architecture. Keep private editions private.**

## Suggested GitHub description

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

## Suggested topics

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

## License

Apache-2.0. See `LICENSE`.
