# Task Card

## Metadata

- Task ID: TASK-001
- Title: Create documentation brief
- Role: Researcher
- Skill App: documentation-brief
- Source Mount: MOUNT-001
- Output Contract: CONTRACT-TASK-001
- Created By: Host
- Status: open

## Goal

Read the mounted sources and produce a concise documentation brief for the internal knowledge base project.

## Readable Sources

- .agent-os/sources/current_requirements.md
- .agent-os/sources/project_notes.md

## Forbidden

Do not read or use:

- archive/
- registry/
- private editions
- unmounted sources

Do not modify:

- .agent-os/sources/
- .agent-os/tasks/
- .agent-os/mounts/
- .agent-os/contracts/
- skills/

## Required Outputs

| Name | Type | Path |
|---|---|---|
| documentation_brief | markdown | .agent-os/outputs/TASK-001/documentation_brief.md |
| handoff_report | markdown | .agent-os/handoffs/HANDOFF-TASK-001.md |

## Required Sections

The documentation brief must include:

- Summary
- Key Findings
- Unknowns
- Risks
- Next Steps

The handoff report must include:

- Metadata
- Sources Used
- Outputs Created
- Decisions Made
- Uncertainties
- Risks
- Next Steps
- Audit Status

## Rules

- Use only mounted sources.
- Mark unknowns explicitly as `UNKNOWN`.
- Do not invent facts.
- Do not modify forbidden paths.
- Prepare for Host audit.

## Audit Requirement

- Required: yes
- Auditor Role: Host

## Recovery Requirement

- Required: no

## Handoff Requirement

- Required: yes
