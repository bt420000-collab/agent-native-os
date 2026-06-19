# Roadmap

## v0.1: Specification seed

- Define Agent-Native OS theory
- Define Context Kernel
- Define Skill App Runtime
- Provide templates
- Provide sample workspaces
- Provide Codex handoff guide

## v0.2: Validation package

- Runnable Docs Brief Demo
- Workspace validator
- Demo runner
- First Skill App example
- Add JSON/YAML schemas
- Add validation scripts
- Add more sample Skill Apps
- Add `agent-os doctor` concept
- Add source mount linting
- Add handoff validation

## v0.3: CLI prototype

Potential commands:

```bash
agent-os init
agent-os install ./skills/research-summary
agent-os task new
agent-os mount sources
agent-os run task TASK-001
agent-os audit TASK-001
agent-os archive
agent-os recover
```

## v0.4: Skill registry

- Local registry
- Skill lock file
- Permission lock file
- Skill dependency graph
- Compatibility checks

## v0.5: Multi-agent runtime adapters

- Generic adapter spec
- Codex adapter
- ChatGPT adapter
- Claude adapter
- Local model adapter
- MCP/tool driver notes

## v1.0: Stable open architecture

- Stable manifest schema
- Stable task/handoff/audit schema
- Reference implementation
- Example editions
- Documentation site
