# Docs Brief Demo

Languages: [English](README.md) | [简体中文](README.zh-CN.md)

This demo shows the minimal Agent-Native OS loop:

```txt
Source -> Task -> Mount -> Output Contract -> Agent Prompt -> Handoff -> Audit
```

The goal is to turn messy project notes into a governed documentation brief.

This demo does not call any API and does not require any external package. It is designed to be copied into Codex, ChatGPT, Claude, or another agent.

## What this demo proves

This is not "ask an AI to summarize notes."

This is a governed agent workspace where:

- sources are mounted
- a task is scoped
- a Skill App is declared
- forbidden paths are defined
- outputs are contract-bound
- unknowns must be marked
- handoff is required
- audit is expected

## Demo files

```txt
examples/docs-brief-demo/
  README.md
  README.zh-CN.md
  PROMPT_FOR_AGENT.md
  EXPECTED_OUTPUT_SAMPLE.md

  .agent-os/
    sources/
      project_notes.md
      current_requirements.md
    tasks/
      TASK-001.md
    mounts/
      MOUNT-001.yaml
    contracts/
      CONTRACT-TASK-001.yaml
    outputs/
      TASK-001/
    handoffs/
    reviews/

  skills/
    documentation-brief/
      manifest.yaml
      instructions.md
      output_contract.md
      permissions.yaml
```

## Run the check

From the repository root:

```bash
python scripts/run_docs_brief_demo.py
python scripts/validate_workspace.py examples/docs-brief-demo
```

## Run the agent task

Open:

```txt
examples/docs-brief-demo/PROMPT_FOR_AGENT.md
```

Copy the prompt into your agent.

The agent should create:

```txt
examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md
examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md
```

Then a Host or Auditor can create:

```txt
examples/docs-brief-demo/.agent-os/reviews/AUDIT-TASK-001.md
```

## Expected output

See:

```txt
examples/docs-brief-demo/EXPECTED_OUTPUT_SAMPLE.md
```
