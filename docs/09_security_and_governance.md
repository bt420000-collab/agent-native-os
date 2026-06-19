# Security and Governance

Agent-Native OS treats Skill Apps as permissioned applications.

## Permission categories

Recommended permission categories:

```txt
read_sources
write_outputs
write_handoffs
modify_core_sources
modify_registry
run_tools
access_secrets
network_access
delete_files
```

## Default-deny principle

A Skill App should not access or mutate anything unless declared.

## Mutation classes

```txt
none       cannot write
output     can write outputs only
handoff    can write handoff reports
review     can write review reports
source     can propose source changes
core       can modify core sources after approval
```

## Secrets

Secrets should never be mounted as normal context.

They must be accessed through controlled tool drivers or environment-specific secret stores.

## Auditing

High-risk actions should require audit:

- core source mutation
- registry modification
- deletion
- external publishing
- irreversible tool actions
- large batch edits

## Principle

A strong agent without a permission model is just a faster creature in a messier room.
