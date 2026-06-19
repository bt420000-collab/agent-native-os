# Agent-Native OS

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

A context-native operating system architecture for long-running AI agents.

Most AI agents today are being trained to use human computers: screens, buttons, browsers, terminals, APIs, and GUI workflows.

Agent-Native OS asks a different question:

> What kind of operating system does an agent need for its own work?

Human operating systems are built around apps, windows, files, and devices. Agent-native systems should be built around context, source hierarchy, task isolation, role runtime, output contracts, audit gates, handoff protocols, archives, and recovery points.

## Start here

If you are new to the project, start with `CORE_THEORY_AND_GLOSSARY.md`.

It defines the core theory, standard vocabulary, and normative language for Agent-Native OS. In short:

```txt
Agent-Native OS turns natural-language instructions into executable context
and turns agent outputs into structured state for reliable continuation.
```

The project is built on five principles:

1. Context is the first-class resource.
2. Contracted natural language is source code.
3. Context Kernel is the runtime.
4. Structured output is the Context ABI.
5. Skill Apps are installable applications.

## Core idea

In a human OS, the first-class citizen is the application.

In an Agent OS, the first-class citizen is the context.

Agent-Native OS is an open architecture for installing and running Skill Apps inside governed, context-aware agent workspaces.

## What this project defines

This repository is a specification and project seed for building an "Agent Windows" layer:

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

Agent-Native OS is not another chatbot prompt pack.

It is not a GUI automation tool.

It is not a replacement for model frameworks, tool frameworks, or workflow engines.

Instead:

- LLM frameworks call models.
- Agent frameworks call tools.
- Workflow engines arrange steps.
- Agent-Native OS governs long-running agent work.

## Why now

Tools are multiplying: browsers, terminals, APIs, MCP servers, file editors, vector databases, and GUI control. More tools make agents more powerful, but also more chaotic.

Without an OS layer, agents suffer from:

- context overflow
- role bleeding
- source pollution
- handoff amnesia
- output drift
- unauthorized mutation
- review collapse
- archive haunting
- user override loss
- long-run degradation

Agent-Native OS turns agent work into a governable environment.

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

## Repository map

```txt
agent-native-os/
  README.md
  README.zh-CN.md
  AUTHORS.md
  BILINGUAL_POLICY.md
  CORE_THEORY_AND_GLOSSARY.md
  MANIFESTO.md
  NAMING_STRATEGY.md
  SPEC.md
  ROADMAP.md
  CODEX_HANDOFF.md
  docs/
  spec/
  templates/
  examples/
    docs-brief-demo/
  scripts/
```

## Public core, private editions

This repository defines the open architecture.

Domain-specific private editions can be built on top of it. Private editions may contain domain craft, business logic, specialized scoring systems, or proprietary workflows, and are intentionally not included.

## Contributing

This is a specification-first project. Contributions that clarify the architecture, improve templates, add neutral examples, or strengthen security and governance are welcome.

See `CONTRIBUTING.md`, `GOVERNANCE.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and `BILINGUAL_POLICY.md`.

## Author and contact

Maintainer: [bt420000-collab](https://github.com/bt420000-collab)

- Email: bt420@126.com
- WeChat: iMelodyJust

## Slogan

> Stop teaching agents only to use human desktops. Give them a native workspace.

Or, more directly:

> We are building the Windows layer for agents: a context-native OS where developers can install Skill Apps and compose reliable workflows.

## License

Apache-2.0. See `LICENSE`.
