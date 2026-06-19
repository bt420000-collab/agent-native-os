# Roadmap

## v0.1: Specification Seed

Status: complete.

Goals:

- Define Agent-Native OS theory.
- Define Context Kernel.
- Define Skill App Runtime.
- Provide templates.
- Provide specification documents.
- Provide sample workspaces.
- Provide Codex handoff guidance.

## v0.2: Runnable Demo and Validator

Status: current.

Goals:

- Add a runnable Docs Brief Demo.
- Add a neutral documentation Skill App example.
- Add a Task Card, Source Mount, Output Contract, Handoff, and Audit flow.
- Add `scripts/run_docs_brief_demo.py`.
- Add `scripts/validate_workspace.py`.
- Update README and README.zh-CN with a "Try the demo" section.
- Keep the demo domain-neutral and free of private edition content.

Validation commands:

```bash
python scripts/run_docs_brief_demo.py
python scripts/validate_workspace.py examples/docs-brief-demo
```

## v0.2.1: Machine-Checkable Schemas

Potential files:

```txt
schemas/task-card.schema.json
schemas/source-mount.schema.json
schemas/output-contract.schema.json
schemas/skill-manifest.schema.json
schemas/handoff-report.schema.json
schemas/audit-report.schema.json
```

Goals:

- Convert core templates into machine-checkable schemas.
- Validate YAML frontmatter and JSON artifacts.
- Add schema tests for the Docs Brief Demo.

## v0.3: CLI Prototype

Potential commands:

```bash
agent-os init
agent-os skill install ./skills/research-summary
agent-os skill list
agent-os task create
agent-os mount check TASK-001
agent-os contract check TASK-001
agent-os handoff validate HANDOFF-001
agent-os audit create TASK-001
agent-os recover list
```

Goals:

- Provide a small Python CLI.
- Keep dependencies minimal.
- Focus on workspace setup and validation before automation.

## v0.4: Skill Registry

Goals:

- Add local registry.
- Add Skill lock file.
- Add permission lock file.
- Add Skill dependency graph.
- Add compatibility checks.

## v0.5: Multi-Agent Runtime Adapters

Potential adapters:

- Generic adapter spec
- Codex adapter
- ChatGPT adapter
- Claude adapter
- Local model adapter
- MCP/tool driver notes

Goal:

- Allow different agents to operate inside the same Agent-Native OS workspace.

## v1.0: Stable Open Architecture

Goals:

- Stable manifest schema.
- Stable task, handoff, audit, and recovery schemas.
- Reference implementation.
- Example editions.
- Documentation site.
