# Task Card Schema

A Task Card is the smallest contract-bound unit of agent work.

## Required fields

```yaml
task_id: string
title: string
goal: string
role: string
skill_app: string
source_mount: string
constraints: list
outputs: list
audit_required: boolean
handoff_required: boolean
recovery_required: boolean
```

## Example

```yaml
task_id: TASK-001
title: Create research brief
goal: >
  Read mounted sources and produce a concise research brief.

role: researcher
skill_app: research-summary
source_mount: MOUNT-001

constraints:
  - Do not modify core sources.
  - Mark unknown claims as unknown.
  - Use only mounted sources.

outputs:
  - path: .agent-os/outputs/TASK-001/research_brief.md
  - path: .agent-os/handoffs/HANDOFF-TASK-001.md

audit_required: true
handoff_required: true
recovery_required: false
```
