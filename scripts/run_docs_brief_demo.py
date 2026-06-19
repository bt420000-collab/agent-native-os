#!/usr/bin/env python3
"""Check that the Docs Brief Demo workspace is present and ready.

This script does not call any model or external API. It verifies the demo
structure and prints the next steps for a human or coding agent.
"""

from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_PATHS = [
    "examples/docs-brief-demo/README.md",
    "examples/docs-brief-demo/README.zh-CN.md",
    "examples/docs-brief-demo/PROMPT_FOR_AGENT.md",
    "examples/docs-brief-demo/EXPECTED_OUTPUT_SAMPLE.md",
    "examples/docs-brief-demo/.agent-os/sources/project_notes.md",
    "examples/docs-brief-demo/.agent-os/sources/current_requirements.md",
    "examples/docs-brief-demo/.agent-os/tasks/TASK-001.md",
    "examples/docs-brief-demo/.agent-os/mounts/MOUNT-001.yaml",
    "examples/docs-brief-demo/.agent-os/contracts/CONTRACT-TASK-001.yaml",
    "examples/docs-brief-demo/.agent-os/outputs/TASK-001/.gitkeep",
    "examples/docs-brief-demo/.agent-os/handoffs/.gitkeep",
    "examples/docs-brief-demo/.agent-os/reviews/.gitkeep",
    "examples/docs-brief-demo/skills/documentation-brief/manifest.yaml",
    "examples/docs-brief-demo/skills/documentation-brief/instructions.md",
    "examples/docs-brief-demo/skills/documentation-brief/output_contract.md",
    "examples/docs-brief-demo/skills/documentation-brief/permissions.yaml",
]


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "README.md").exists() and (candidate / "examples").exists():
            return candidate
    return start.resolve()


def main() -> int:
    repo_root = find_repo_root(Path.cwd())
    missing: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (repo_root / rel).exists():
            missing.append(rel)

    print("Agent-Native OS Docs Brief Demo Check")
    print("=" * 44)
    print(f"Repository root: {repo_root}")

    if missing:
        print("\nFAIL: Missing required demo files:")
        for rel in missing:
            print(f"  - {rel}")
        return 1

    print("\nPASS: Docs Brief Demo is ready.")
    print("\nNext steps:")
    print("1. Open examples/docs-brief-demo/PROMPT_FOR_AGENT.md")
    print("2. Copy the prompt into Codex, ChatGPT, Claude, or another agent")
    print("3. Let the agent create:")
    print("   - examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md")
    print("   - examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md")
    print("4. Validate the workspace:")
    print("   python scripts/validate_workspace.py examples/docs-brief-demo")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
