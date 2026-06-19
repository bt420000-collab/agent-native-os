# Agent-Native OS

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

A context-native operating system architecture for long-running AI agents and installable Skill Apps.

![Spec](https://img.shields.io/badge/spec-v0.2-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Status](https://img.shields.io/badge/status-draft-orange)

## What is this?

Most AI agents today are being trained to use human computers: screens, buttons, browsers, terminals, APIs, and GUI workflows.

Agent-Native OS asks a different question:

> What kind of operating system does an agent need for its own work?

Human operating systems are built around applications, windows, files, and devices.

Agent-native systems should be built around context, source hierarchy, task isolation, role runtime, output contracts, audit gates, handoff protocols, archives, and recovery points.

## Core idea

In a human OS, the first-class citizen is the application.

In an Agent OS, the first-class citizen is the context.

Agent-Native OS is an open architecture for installing and running Skill Apps inside governed, context-aware agent workspaces.

Informally, it can be understood as the "Windows layer for AI agents": a native workspace where agents can install Skill Apps, manage context, enforce permissions, audit outputs, and preserve long-running project state.

## Five principles

Agent-Native OS is built on five principles:

1. Context is the first-class resource.
2. Contracted natural language is source code.
3. Context Kernel is the runtime.
4. Structured output is the Context ABI.
5. Skill Apps are installable applications.

## What this project defines

This repository defines the open architecture for:

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

## What it is not

Agent-Native OS is not:

- a prompt pack
- a GUI automation tool
- a single-agent script
- a simple workflow template
- a vendor-specific agent framework
- a domain-specific private edition

Instead:

- LLM frameworks call models.
- Agent frameworks call tools.
- Workflow engines arrange steps.
- Agent-Native OS governs long-running agent work.

## Try the demo

Run:

```bash
python scripts/run_docs_brief_demo.py
```

Then open:

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

Copy the prompt into your coding agent or LLM and let it produce the governed outputs.

Validate the workspace:

```bash
python scripts/validate_workspace.py examples/docs-brief-demo
```

The demo shows the minimal governed loop:

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

## Minimal viable kernel

The MVP is intentionally small:

1. Skill App Manifest
2. Source Mount
3. Task Card
4. Output Contract
5. Handoff Report

Recommended extensions:

6. Audit Gate
7. Recovery Point
8. Role Runtime
9. Skill Registry
10. Source Policy

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

Open the architecture. Keep private editions private.

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
