# Cross-App Bridge

A Cross-App Bridge is an OS-approved data channel between two Skill Apps.

Apps must not directly read each other's private workspaces.

## Example

```txt
ano.skill.novel/outbox/adaptation_packet/
  ↓ bridge approved by ANO Host
ano.skill.comic/inbox/adaptation_packet/
```

## Bridge properties

A bridge is:

- scoped to a task
- scoped to exact paths
- revocable by the OS Host
- visible in the event bus
- recorded in `ano/runtime/bridges/`

## Why it exists

Multi-app workflows need cooperation without filesystem chaos.

Example workflows:

```txt
novel app + comic app      -> novel-to-comic adaptation
research app + writing app -> report generation
code app + audit app       -> software review pipeline
```

The Host schedules the workflow and controls the bridge.
