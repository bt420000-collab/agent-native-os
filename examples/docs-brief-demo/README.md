# Docs Brief Demo

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

This demo shows the minimal Agent-Native OS operating loop:

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

## Purpose

Turn messy project notes into a governed documentation brief using Agent-Native OS primitives.

The scenario is intentionally neutral: a small team is building an internal knowledge base and needs a concise brief from scattered notes and current requirements.

## What This Demonstrates

- Sources are mounted explicitly.
- A Task Card defines role, goal, readable sources, forbidden areas, outputs, and audit.
- An Output Contract defines the required sections and paths.
- A Skill App declares its instructions, permissions, and output contract.
- A copyable prompt lets a human run the task with any capable coding agent or LLM.
- A handoff report preserves continuation state.
- An audit checklist shows how work is reviewed before entering mainline.

## Try It

From the repository root, run:

```bash
python scripts/run_docs_brief_demo.py
```

Then open:

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

Copy the prompt into your coding agent or LLM. The agent should create:

```txt
examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md
examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md
```

## Validate the Workspace

Run:

```bash
python scripts/validate_workspace.py examples/docs-brief-demo
```

The validator checks for a minimal Agent-Native OS workspace skeleton and at least one task file.
