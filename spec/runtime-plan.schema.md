# Runtime Plan Schema

A Runtime Plan is the OS-approved executable form of a Context Permission Request.

## Required fields

```yaml
runtime_plan:
  plan_id: string
  source_request_id: string
  task_id: string
  app_id: string
  approved_by: ano.host
  decision: approved | approved_with_reductions | denied | deferred
  final_agent_roster: list
  final_context_budget: object
  final_workspace_scope: object
  bridge_grants: list
  user_customizations_applied: list
  event_log_path: string
```

## Rule

Only a Runtime Plan approved by `ano.host` is executable.
