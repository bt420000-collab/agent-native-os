# Source Mount Schema

A Source Mount defines which materials are available to a task.

## Required sections

```yaml
task_id: string
mount_id: string
hot_sources: list
warm_sources: list
cold_sources: list
forbidden_sources: list
source_priority: list
notes: string
```

## Example

```yaml
task_id: TASK-001
mount_id: MOUNT-001

hot_sources:
  - path: .agent-os/sources/current_requirements.md
    reason: user-confirmed requirements
  - path: .agent-os/tasks/TASK-001.md
    reason: active task card

warm_sources:
  - path: .agent-os/sources/background_notes.md
    reason: reference only

cold_sources:
  - path: .agent-os/archive/old_design.md
    reason: old version, do not load unless asked

forbidden_sources:
  - path: .agent-os/archive/deprecated/
    reason: deprecated material

source_priority:
  - user_latest_instruction
  - confirmed_requirements
  - current_design
  - current_outputs
  - review_feedback
  - old_versions
  - brainstorm
  - deprecated
```
