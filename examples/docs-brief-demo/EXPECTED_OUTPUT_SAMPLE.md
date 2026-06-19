# Expected Output Sample

This sample is illustrative. It shows the shape of a successful run, not a mandatory generated result.

## Example `documentation_brief.md`

```md
# Documentation Brief

## Summary

The team is building an internal knowledge base for onboarding, project decisions, and operational references. The immediate documentation need is a concise starter brief that separates confirmed requirements from unresolved notes.

## Key Findings

- The current priority is an internal knowledge base, not a public docs site.
- The first audience is new team members and project contributors.
- Required initial sections are onboarding, decision log, source index, and maintenance rules.
- Existing notes contain useful ideas, but some details are unconfirmed and should not enter mainline without review.

## Unknowns

- The owner for long-term documentation maintenance is not confirmed.
- The publishing target is not decided.
- The update cadence is not confirmed.

## Risks

- Outdated meeting notes could contaminate the current brief if treated as authoritative.
- Without ownership, the knowledge base may become stale.
- Missing maintenance rules could cause source pollution over time.

## Next Steps

1. Ask the Host to confirm the documentation owner.
2. Decide whether the first version lives in a repository, wiki, or shared drive.
3. Create a source policy for confirmed requirements, working notes, and deprecated material.
4. Draft the first onboarding page from confirmed requirements only.
```

## Example `HANDOFF-TASK-001.md`

```md
---
artifact_type: handoff_report
task_id: TASK-001
role: Researcher
skill_app: documentation-brief
audit_status: pending_host_review
---

# Handoff Report

## Metadata

- Task ID: TASK-001
- Role: Researcher
- Skill App: documentation-brief
- Status: completed_for_audit

## Sources Used

- `.agent-os/sources/current_requirements.md`
- `.agent-os/sources/project_notes.md`

## Outputs Created

- `.agent-os/outputs/TASK-001/documentation_brief.md`

## Decisions Made

- Treated `current_requirements.md` as higher authority than `project_notes.md`.
- Marked ownership, publishing target, and update cadence as unknowns.

## Uncertainties

- Documentation owner remains unconfirmed.
- Publishing target remains unconfirmed.
- Maintenance cadence remains unconfirmed.

## Risks

- Source pollution if older notes are reused without review.
- Stale documentation if ownership is not assigned.

## Next Steps

- Host should audit the brief.
- If approved, Writer role can draft the first onboarding page.

## Audit Status

Pending Host audit.
```

## Example Audit Checklist

```md
# Audit Checklist for TASK-001

- [ ] Output uses only mounted sources.
- [ ] Required sections are present.
- [ ] Unknowns are marked explicitly.
- [ ] Source authority is respected.
- [ ] Forbidden paths were not read or modified.
- [ ] Handoff report includes continuation state.
- [ ] Output is ready to enter mainline or return for revision.
```
