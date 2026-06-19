# Codex Homepage Art Update Instructions

This overlay updates the public homepage presentation of the `agent-native-os` repository.

## Goal

Upgrade the repository homepage so it feels like a serious large-scale project rather than a small script collection.

The design priority is:

1. Put the **Chinese artistic propaganda posters first** for maximum impact.
2. Keep the repository **English-first in structure** by preserving `README.md` as the primary root document.
3. Follow the posters with the more technical diagrams and demo instructions.

## Copy target

Expected repository directory:

```txt
./agent-native-os/
```

## Copy action

Copy all files from this overlay into the repository root, preserving paths.

Key files:

- `README.md`
- `README.zh-CN.md`
- `docs/assets/homepage/*`

## After copying

1. Check that all image paths in both README files resolve.
2. Verify the GitHub README renders the posters and diagrams correctly.
3. Optionally update GitHub About settings:

Description:

```txt
A context-native operating system architecture for long-running AI agents and installable Skill Apps.
```

Topics:

```txt
ai-agents
agent-os
agent-native
context-engineering
context-native
multi-agent
skill-apps
workflow-automation
agent-framework
ai-native
```

## Do not change

- project name
- core theory terminology
- public/private boundary
- demo scripts
- existing domain-neutral policy

## Completion

After applying the overlay, create or update:

```txt
CODEX_COMPLETION_REPORT.md
```

Include:

- files copied
- README render check
- any broken links or path issues
- whether GitHub About fields were updated
