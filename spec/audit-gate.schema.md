# Audit Gate Schema

An Audit Gate blocks important work from entering the mainline until reviewed.

## Required fields

```yaml
audit_id: string
task_id: string
target_outputs: list
auditor_role: string
status: pending|passed|failed|needs_revision
criteria: list
findings: list
required_fixes: list
```

## Example

```yaml
audit_id: AUDIT-001
task_id: TASK-001

target_outputs:
  - out/TASK-001/research_brief.md

auditor_role: host
status: pending

criteria:
  - Uses only mounted sources.
  - Has required sections.
  - Marks uncertainty.
  - Does not mutate forbidden files.

findings: []
required_fixes: []
```
