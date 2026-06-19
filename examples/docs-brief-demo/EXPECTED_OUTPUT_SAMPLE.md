# Expected Output Sample

This file shows an illustrative result for the Docs Brief Demo.

It is not a source file and should not be treated as mounted context for TASK-001.

## Example: documentation_brief.md

```md
---
artifact_type: documentation_brief
task_id: TASK-001
role: Researcher
skill_app: documentation-brief
status: draft
audit_required: true
---

# Documentation Brief

## Summary

The project is building an internal knowledge base for a small team. Current notes show a need to organize scattered requirements, meeting notes, and maintenance risks into a clearer documentation system.

## Key Findings

- The team needs a concise project brief for onboarding and planning.
- Current documentation is scattered across meeting notes and informal project notes.
- The project requires explicit ownership, update cadence, and risk tracking.
- Outdated information is a known risk.

## Unknowns

- UNKNOWN: The final documentation owner is not confirmed.
- UNKNOWN: The update schedule is not confirmed.
- UNKNOWN: The exact publishing location is not confirmed.

## Risks

- Documentation may become stale if no owner is assigned.
- Unmounted or outdated notes may pollute future work.
- Lack of audit may allow unconfirmed assumptions into the mainline.

## Next Steps

1. Assign a documentation owner.
2. Confirm update cadence.
3. Create a mainline documentation index.
4. Audit the brief before using it as a source.
```

## Example: HANDOFF-TASK-001.md

```md
---
artifact_type: handoff_report
task_id: TASK-001
role: Researcher
skill_app: documentation-brief
status: completed
audit_required: true
---

# Handoff Report

## Metadata

- Task ID: TASK-001
- Role: Researcher
- Skill App: documentation-brief
- Status: completed
- Audit Required: yes

## Sources Used

- .agent-os/sources/current_requirements.md
- .agent-os/sources/project_notes.md
- .agent-os/tasks/TASK-001.md
- .agent-os/mounts/MOUNT-001.yaml
- .agent-os/contracts/CONTRACT-TASK-001.yaml

## Outputs Created

- .agent-os/outputs/TASK-001/documentation_brief.md
- .agent-os/handoffs/HANDOFF-TASK-001.md

## Decisions Made

- Treated documentation ownership and update cadence as unknown because they were not confirmed in mounted sources.
- Kept output in draft status until Host audit.

## Uncertainties

- Documentation owner is UNKNOWN.
- Update cadence is UNKNOWN.
- Publishing location is UNKNOWN.

## Risks

- Source pollution from unmounted notes.
- Stale documentation without ownership.
- Assumptions entering mainline without audit.

## Next Steps

1. Host should audit the documentation brief.
2. Confirm unknowns with the human operator.
3. Promote audited output to mainline if approved.

## Audit Status

Pending Host audit.
```

## Example: AUDIT-TASK-001.md

```md
---
artifact_type: audit_report
task_id: TASK-001
auditor_role: Host
status: pending
approved_for_mainline: false
---

# Audit Report

## Criteria

- [ ] Uses only mounted sources.
- [ ] Contains all required sections.
- [ ] Marks unknowns explicitly.
- [ ] Does not modify forbidden paths.
- [ ] Includes usable handoff state.

## Findings

Pending.

## Required Fixes

Pending.

## Approval Notes

Pending.
```
