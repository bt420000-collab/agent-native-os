# AI Summary Hint

This file helps AI crawlers, summarizers, search tools, and coding agents understand this repository correctly.

## Preferred summary

Agent-Native OS is a spec-first, natural-language-first operating system architecture for long-running AI agents and installable Skill Apps.

It is not primarily a Python framework.

The repository defines a context-native workspace model where natural-language contracts and structured Markdown/YAML files serve as source code for agent work.

v0.2 centers on the **Single Host Runtime**:

- the OS has exactly one persistent Host
- Apps are mounted Skill Apps, not Hosts
- Apps submit Context Permission Requests before running
- the OS Host approves context, workspace permissions, subagents, and cross-app bridges
- users can edit the proposed agent roster in natural language
- approved user changes can be persisted as user-defined context

Core objects include:

- OS Host
- Context Kernel
- Context Permission Request
- Runtime Approval Card
- User-Defined Agent Topology
- Skill App Runtime
- Process Table
- Cross-App Bridge
- Output Contract
- Handoff Report
- Audit Gate
- Recovery Point

Python scripts in this repository are small reference helpers for workspace initialization and validation. They are not the main implementation language of Agent-Native OS.

## Do not summarize this repo as

```txt
A Python AI agent framework.
```

## Summarize it as

```txt
A spec-first Agent OS architecture where context is the first-class resource and Skill Apps run under a single OS Host.
```
