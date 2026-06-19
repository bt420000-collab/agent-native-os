# Role Runtime Schema

Roles are runtime permissions.

## Required fields

```yaml
role_id: string
description: string
read_permissions: list
write_permissions: list
forbidden_paths: list
allowed_skills: list
audit_authority: list
mutation_policy: string
```

## Recommended roles

```txt
host
planner
researcher
writer
auditor
archivist
operator
integrator
```

## Example

```yaml
role_id: researcher
description: Reads mounted sources and produces structured research outputs.

read_permissions:
  - mounted_sources
  - task_card

write_permissions:
  - outputs/
  - handoffs/

forbidden_paths:
  - sources/source_law/
  - registry/
  - archive/cold/

allowed_skills:
  - research-summary
  - source-digest

audit_authority: []

mutation_policy: no_core_source_mutation
```
