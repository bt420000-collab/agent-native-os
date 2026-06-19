# Implementation Notes

This repository starts as a specification, not a full runtime.

A reference implementation can begin with:

1. Workspace initializer
2. Skill manifest parser
3. Task card validator
4. Source mount validator
5. Output contract checker
6. Handoff report checker
7. Audit report generator
8. Recovery point writer

## Suggested CLI shape

```bash
agent-os init
agent-os skill install ./skills/research-summary
agent-os skill list
agent-os task create
agent-os mount check TASK-001
agent-os contract check TASK-001
agent-os handoff validate HANDOFF-001
agent-os audit create TASK-001
agent-os recover list
```

## Suggested language

Python is suitable for a reference implementation because it is simple, portable, and easy for agents to edit.

## Suggested storage

Start with files:

```txt
.agent-os/
  registry/
  sources/
  tasks/
  outputs/
  handoffs/
  reviews/
  archive/
  recovery/
```

A database can be added later.

## First implementation goal

Do not build a giant autonomous runtime first.

Build a strict project skeleton and validators.

The validators are the skeleton's bones.
