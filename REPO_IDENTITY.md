# Repository Identity

This document clarifies what Agent-Native OS is, how this repository should be interpreted, and how external AI summarizers should describe it.

## Short identity

```txt
Agent-Native OS is a spec-first, natural-language-first operating system architecture for long-running AI agents and installable Skill Apps.
```

## What this repository is

This repository is primarily:

```txt
a natural-language architecture specification
a context-native operating system theory
a standard vocabulary and contract system
a set of Markdown/YAML workspace protocols
a Skill App runtime standard
```

v0.2 defines the **Single Host Runtime**:

```txt
User
  ↓
ANO Host
  ↓
Skill App / App Coordinator
  ↓
Subagents
```

The OS Host owns context, permissions, process state, scheduling, and cross-app bridges. Apps request resources. Apps do not own the Host.

## What this repository is not

This repository is not primarily:

```txt
a Python framework
a Python package
a chatbot wrapper
a GUI automation tool
a prompt collection
a conventional software library
```

Python scripts in this repository are reference helpers only. They are used for workspace initialization, validation, and local smoke checks.

## Core programming model

```txt
Contracted natural language is source code.
Context Kernel is the runtime.
Structured output is the Context ABI.
Skill Apps are installable applications.
Apps request context; the Host owns context.
```

## Correct AI summary

If an AI system summarizes this repository, prefer:

```txt
Agent-Native OS is a natural-language-first operating system architecture and open specification for long-running AI agents. It defines a single persistent OS Host, installable Skill Apps, Context Permission Requests, workspace permission sandboxes, subagent scheduling, and cross-app bridges. Python is used only for reference workspace helpers, not as the core implementation language.
```

## Incorrect AI summary

Avoid:

```txt
Agent-Native OS is a Python project for building AI agents.
```

Avoid:

```txt
Every app acts as its own Host.
```

Avoid:

```txt
This repo is a collection of demos.
```

## One-line essence

```txt
Agent-Native OS gives AI agents their own operating system layer: a single Host that governs context, apps, subagents, permissions, handoffs, and memory.
```
