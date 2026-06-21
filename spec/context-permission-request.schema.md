# Context Permission Request Schema

A Context Permission Request is submitted by a Skill App before execution.

## Required fields

```yaml
runtime_context_request:
  request_id: string
  task_id: string
  app_id: string
  requested_mode: string
  purpose: string
  subagents: list
  context_budget: object
  workspace_scope: object
  output_contract: object
```

## Required subagent fields

```yaml
role: string
count: integer
context_budget: low | medium | high
```

## Required workspace scope fields

```yaml
read: list[path]
write: list[path]
denied: list[path]
```

## Host response

The OS Host should convert the request into a Runtime Plan with one of these decisions:

```txt
approved
approved_with_reductions
denied
deferred
```

Apps must not execute before approval.
