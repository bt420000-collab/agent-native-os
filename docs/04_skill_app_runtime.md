# Skill App Runtime

A Skill App is an installable capability package for agents.

It is not just a prompt.

A Skill App declares:

- what it does
- what it needs
- what it can read
- what it can write
- what it must not touch
- what it outputs
- whether it needs audit
- how it reports uncertainty
- what other skills it depends on

## Standard package

```txt
skill-app/
  manifest.yaml
  instructions.md
  input_contract.md
  output_contract.md
  permissions.yaml
  source_policy.md
  examples/
  tests/
  changelog.md
```

## Runtime actions

The Skill App Runtime should support:

- install
- inspect
- enable
- disable
- run
- compose
- audit
- remove
- lock version

## Skill registry

The registry records installed skills:

```txt
.agent-os/
  registry/
    installed_skills.yaml
    skill_lock.yaml
    permissions.lock
```

## Philosophy

Developers should not rebuild agent workflows from scratch.

They should install Skill Apps into an agent-native OS and compose governed workflows.
