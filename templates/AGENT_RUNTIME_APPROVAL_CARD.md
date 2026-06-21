# Agent Runtime Approval Card

## App

- App ID: `ano.skill.example`
- Display Name: ANO Example Skill App
- Requested Mode: normal
- Task ID: TASK-001

## Planned Agent Roster

| Role | Count | Purpose | Context Budget |
|---|---:|---|---|
| example.coordinator | 1 | Coordinate the app workflow | low |
| example.worker | 1 | Produce the requested output | low |

## Workspace Permissions

### Read

```txt
ano/runtime/apps/ano.skill.example/inbox/
```

### Write

```txt
ano/runtime/apps/ano.skill.example/outbox/
```

### Denied

```txt
ano/kernel/
ano/runtime/apps/*/private/
```

## Cross-App Bridge

```txt
none requested
```

## User Customizations

```txt
none yet
```

## Commercial Notice

```txt
free / Apache-2.0 / no payment required
```

## Decision

User may answer:

```txt
approve
reject
approve but reduce to one worker
add a reviewer agent
add a troll simulator agent
```
