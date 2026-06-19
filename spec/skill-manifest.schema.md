# Skill Manifest Schema

A Skill Manifest declares an installable Skill App.

## Required fields

```yaml
name: string
version: semver
type: skill-app
description: string
runtime:
  agent_role: string
  requires_audit: boolean
inputs: list
outputs: list
permissions: object
policies: object
audit: object
```

## Example

```yaml
name: research-summary
version: 0.1.0
type: skill-app

description: >
  Summarize mounted source materials into a structured research brief.

runtime:
  agent_role: researcher
  requires_audit: true

inputs:
  - name: source_bundle
    type: mounted_sources
    required: true
  - name: task_card
    type: task_contract
    required: true

outputs:
  - name: research_brief
    type: markdown
    path: outputs/research_brief.md
  - name: handoff_report
    type: markdown
    path: handoffs/research_handoff.md

permissions:
  read:
    - mounted_sources
    - task_card
  write:
    - outputs/
    - handoffs/
  forbidden:
    - source_law/
    - system_kernel/
    - archive/cold/

policies:
  source_priority: strict
  hallucination_policy: cite_or_mark_unknown
  mutation_policy: no_core_source_mutation

audit:
  required_by:
    - host
```
