# Documentation Brief Skill Instructions

## Role

Act as the Researcher role.

## Goal

Turn mounted source material into a concise documentation brief that a Host can audit and a future Writer can continue.

## Source Rules

- Read only the mounted sources declared for the task.
- Treat `current_requirements.md` as higher authority than `project_notes.md`.
- Do not use forbidden paths.
- Do not modify source files.
- Mark unresolved information as unknown instead of guessing.

## Output Rules

Create:

- `.agent-os/outputs/TASK-001/documentation_brief.md`
- `.agent-os/handoffs/HANDOFF-TASK-001.md`

Follow `.agent-os/contracts/CONTRACT-TASK-001.yaml`.

## Audit Readiness

The output is not approved for mainline until the Host audits it.
