# Recovery Point Schema

A Recovery Point records changes and rollback hints.

## Required fields

```yaml
recovery_id: string
timestamp: string
task_id: string
actor_role: string
changed_files: list
reason: string
rollback_hint: string
incident_id: string|null
```

## Example

```yaml
recovery_id: REC-001
timestamp: 2026-06-19T00:00:00Z
task_id: TASK-001
actor_role: host

changed_files:
  - .agent-os/outputs/TASK-001/research_brief.md

reason: Initial output generation.
rollback_hint: Remove TASK-001 output directory.
incident_id: null
```
