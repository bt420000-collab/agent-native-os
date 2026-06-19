# Prompt for Agent: TASK-001

You are operating inside an Agent-Native OS workspace.

You are the `Researcher` role.

Your Skill App is:

```txt
documentation-brief
```

Your task is:

```txt
TASK-001
```

## Read first

Read only these mounted sources:

```txt
examples/docs-brief-demo/.agent-os/sources/current_requirements.md
examples/docs-brief-demo/.agent-os/sources/project_notes.md
examples/docs-brief-demo/.agent-os/tasks/TASK-001.md
examples/docs-brief-demo/.agent-os/mounts/MOUNT-001.yaml
examples/docs-brief-demo/.agent-os/contracts/CONTRACT-TASK-001.yaml
examples/docs-brief-demo/skills/documentation-brief/instructions.md
```

## Forbidden

Do not read or use:

```txt
archive/
registry/
private editions
unmounted sources
```

Do not modify:

```txt
examples/docs-brief-demo/.agent-os/sources/
examples/docs-brief-demo/.agent-os/tasks/
examples/docs-brief-demo/.agent-os/mounts/
examples/docs-brief-demo/.agent-os/contracts/
examples/docs-brief-demo/skills/
```

## Required outputs

Create these files:

```txt
examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md
examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md
```

## Required sections for documentation_brief.md

```txt
Summary
Key Findings
Unknowns
Risks
Next Steps
```

## Required sections for HANDOFF-TASK-001.md

```txt
Metadata
Sources Used
Outputs Created
Decisions Made
Uncertainties
Risks
Next Steps
Audit Status
```

## Rules

- Use only mounted sources.
- Do not invent facts.
- Mark unknowns explicitly as `UNKNOWN`.
- Preserve the difference between source facts and your interpretation.
- Do not modify forbidden paths.
- Prepare the output for Host audit.

## Final response

After creating the files, respond with:

```txt
TASK-001 completed.
Outputs created:
- .agent-os/outputs/TASK-001/documentation_brief.md
- .agent-os/handoffs/HANDOFF-TASK-001.md

Audit required by Host.
```
