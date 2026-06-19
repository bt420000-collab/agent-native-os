# Handoff Report Schema

A Handoff Report is the continuation state after a task.

## Required fields

```yaml
handoff_id: string
task_id: string
role: string
skill_app: string
sources_used: list
outputs_created: list
decisions: list
uncertainties: list
risks: list
next_steps: list
audit_status: string
```

## Markdown template

```md
# Handoff Report

## Metadata

- Handoff ID:
- Task ID:
- Role:
- Skill App:
- Date:

## Sources Used

## Outputs Created

## Decisions Made

## Uncertainties

## Risks

## Next Steps

## Audit Status
```
