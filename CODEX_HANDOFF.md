# Codex Handoff: Create GitHub Repository

This package is intended to be given to Codex or another coding agent to initialize the public repository.

## Project name

Recommended repository name:

```txt
agent-native-os
```

Alternative names:

```txt
context-native-os
agent-os-spec
agent-work-os
```

## Public positioning

Use this as the repository description:

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

## Required actions

1. Create a GitHub repository named `agent-native-os`.
2. Copy all files from this package into the repository root.
3. Ensure no private/domain-specific edition files are included.
4. Commit with message:

```txt
Initial Agent-Native OS specification v0.1
```

5. Add recommended topics:

```txt
ai-agents
agent-os
context-engineering
multi-agent
skill-apps
workflow-automation
agent-framework
ai-native
```

6. Enable Issues and Discussions if possible.
7. Create initial issues from `ROADMAP.md`.

## Important boundary

This public repository must contain only the open architecture.

Do not add private domain editions, proprietary prompt craft, business-specific scoring systems, or internal production workflows.

## Suggested first GitHub issues

- Define formal JSON Schema for Skill Manifest.
- Build `agent-os init` CLI prototype.
- Build source mount validator.
- Build handoff report validator.
- Add example Skill App: research-summary.
- Add example Skill App: product-doc-review.
- Add security model for Skill App permissions.
- Add docs site with diagrams.

## Suggested README badges

Add later after repo exists:

```md
![Spec](https://img.shields.io/badge/spec-v0.1-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
```

## Suggested branch strategy

- `main`: stable spec
- `dev`: working drafts
- `examples`: optional branch for experiments if desired

## Codex behavior instructions

When extending this project, preserve the distinction between:

- Agent-Native OS: open architecture
- Domain Editions: optional private or external packages

Do not assume any specific domain such as fiction, legal, medicine, finance, or software development in the core spec.
