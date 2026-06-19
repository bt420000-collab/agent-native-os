# Context Kernel

The Context Kernel is the runtime layer that decides what an agent can know, do, change, and hand off.

## Responsibilities

- Load the Task Card.
- Mount approved sources.
- Apply source priority.
- Enforce role permissions.
- Select the Skill App.
- Check the Output Contract.
- Trigger the Audit Gate.
- Create a Handoff Report.
- Write Recovery Points when required.
- Archive completed or stale artifacts.

## Context states

Recommended states:

```txt
hot       current task must-read context
warm      searchable support materials
cold      archived materials, not loaded by default
forbidden explicitly blocked materials
```

## Source authority

The kernel must distinguish between:

```txt
confirmed source
current design
working output
review feedback
old version
brainstorm
deprecated material
```

## Failure prevented

The Context Kernel prevents:

- context overflow
- source pollution
- unauthorized mutation
- role bleeding
- handoff amnesia
- archive haunting
