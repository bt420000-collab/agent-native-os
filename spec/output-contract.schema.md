# Output Contract Schema

An Output Contract specifies what a Skill App must produce.

## Required fields

```yaml
contract_id: string
task_id: string
outputs: list
required_sections: list
forbidden_changes: list
validation: object
completion_checklist: list
```

## Example

```yaml
contract_id: CONTRACT-001
task_id: TASK-001

outputs:
  - name: research_brief
    type: markdown
    path: out/TASK-001/research_brief.md
  - name: handoff_report
    type: markdown
    path: out/handoffs/HANDOFF-TASK-001.md

required_sections:
  - Summary
  - Key Findings
  - Unknowns
  - Risks
  - Next Steps

forbidden_changes:
  - user/imports/
  - ano/registry/

validation:
  method: checklist
  validator_role: host

completion_checklist:
  - Output files exist.
  - Required sections are present.
  - Unknowns are marked.
  - No forbidden paths changed.
```
