# Agent-Native OS Specification v0.1

Status: Draft  
Codename: Context Kernel

## 1. System layers

```txt
Agent-Native OS
│
├─ Context Kernel
├─ Skill App Runtime
├─ Source File System
├─ Role & Permission System
├─ Task Scheduler
├─ Output Contract Engine
├─ Audit Gate
├─ Handoff Bus
├─ Memory & Archive Layer
└─ Recovery System
```

## 2. Context Kernel

The Context Kernel decides what an agent can know, do, change, and hand off during a task.

Responsibilities:

- load task context
- mount source bundles
- apply source priority
- enforce role permissions
- check output contracts
- write handoff reports
- trigger audit gates
- create recovery points
- archive stale materials

## 3. Skill App Runtime

The Skill App Runtime installs, loads, executes, composes, audits, and disables Skill Apps.

A Skill App is a standard package containing:

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

## 4. Source File System

Sources are not ordinary files. They have authority.

Recommended source levels:

```txt
source_law/
  level_0_constitution/
  level_1_confirmed_requirements/
  level_2_current_design/
  level_3_current_outputs/
  level_4_review_feedback/
  level_5_old_versions/
  level_6_brainstorm/
  level_7_deprecated/
```

The OS must prevent deprecated or unconfirmed materials from silently entering hot context.

## 5. Role Runtime

Roles are runtime permissions, not cosmetic names.

Recommended roles:

- Host
- Planner
- Researcher
- Writer
- Auditor
- Archivist
- Operator
- Integrator

Each role should declare:

- read permissions
- write permissions
- mutation restrictions
- audit authority
- allowed Skill Apps

## 6. Task Card

Every unit of work should start from a Task Card.

A Task Card specifies:

- goal
- role
- mounted sources
- constraints
- output contract
- audit requirement
- recovery requirement
- handoff requirement

## 7. Output Contract

Agent output must be contract-bound.

An Output Contract defines:

- output type
- path
- required sections
- forbidden changes
- validation method
- completion checklist

## 8. Handoff Protocol

Every completed task should produce a Handoff Report.

A Handoff Report should include:

- task id
- role
- skill app
- sources used
- outputs created
- decisions made
- uncertainties
- risks
- next steps
- audit status

## 9. Audit Gate

Important work does not enter the mainline until it passes an audit gate.

Audit gates can be:

- manual
- agent-assisted
- automated checklist
- hybrid

## 10. Recovery Point

Any task that modifies core sources or mainline outputs should create a recovery point.

A recovery point records:

- timestamp
- task id
- actor role
- changed files
- reason
- rollback hint
- incident link if applicable

## 11. Minimum viable kernel

```txt
Agent OS MVP
= Skill Manifest
+ Source Mount
+ Task Card
+ Output Contract
+ Handoff Report
```

Recommended extensions:

```txt
+ Audit Gate
+ Recovery Point
+ Role Runtime
+ Skill Registry
+ Source Policy
```
