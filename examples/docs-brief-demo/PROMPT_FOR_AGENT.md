# Prompt for Agent

Use this prompt with Codex, ChatGPT, Claude, or another capable agent.

```txt
You are acting inside an Agent-Native OS demo workspace.

Role:
Researcher

Skill App:
documentation-brief

Task:
Read the mounted sources and produce a governed documentation brief.

Workspace:
examples/docs-brief-demo

Task Card:
examples/docs-brief-demo/.agent-os/tasks/TASK-001.md

Source Mount:
examples/docs-brief-demo/.agent-os/mounts/MOUNT-001.yaml

Output Contract:
examples/docs-brief-demo/.agent-os/contracts/CONTRACT-TASK-001.yaml

Readable Sources:
- examples/docs-brief-demo/.agent-os/sources/current_requirements.md
- examples/docs-brief-demo/.agent-os/sources/project_notes.md

Forbidden:
- Do not read or modify archive/.
- Do not read or modify registry/.
- Do not modify source files.
- Do not create outputs outside the declared output and handoff paths.

Required Outputs:
1. Create:
   examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md

   Required sections:
   - Summary
   - Key Findings
   - Unknowns
   - Risks
   - Next Steps

2. Create:
   examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md

   Required sections:
   - Metadata
   - Sources Used
   - Outputs Created
   - Decisions Made
   - Uncertainties
   - Risks
   - Next Steps
   - Audit Status

Instructions:
- Read only the mounted sources listed above.
- Follow the output contract exactly.
- Mark unknowns explicitly instead of guessing.
- Preserve source authority: current_requirements.md has higher authority than project_notes.md.
- Prepare the outputs for Host audit.
- If you cannot create files, provide the exact contents for both required outputs.
```
