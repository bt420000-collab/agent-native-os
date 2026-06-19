#!/usr/bin/env python3
"""
Check the Docs Brief Demo workspace and print next steps.

Usage:
  python scripts/run_docs_brief_demo.py
"""

from pathlib import Path
import sys


REQUIRED_FILES = [
    "README.md",
    "README.zh-CN.md",
    "PROMPT_FOR_AGENT.md",
    "EXPECTED_OUTPUT_SAMPLE.md",
    ".agent-os/sources/project_notes.md",
    ".agent-os/sources/current_requirements.md",
    ".agent-os/tasks/TASK-001.md",
    ".agent-os/mounts/MOUNT-001.yaml",
    ".agent-os/contracts/CONTRACT-TASK-001.yaml",
    ".agent-os/outputs/TASK-001/.gitkeep",
    ".agent-os/handoffs/.gitkeep",
    ".agent-os/reviews/.gitkeep",
    "skills/documentation-brief/manifest.yaml",
    "skills/documentation-brief/instructions.md",
    "skills/documentation-brief/output_contract.md",
    "skills/documentation-brief/permissions.yaml",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    root = repo_root()
    demo = root / "examples" / "docs-brief-demo"

    print("Docs Brief Demo check")
    print(f"Workspace: {demo.relative_to(root)}")

    missing = [path for path in REQUIRED_FILES if not (demo / path).exists()]

    if missing:
        print("\nFAIL: missing required files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("\nPASS: demo workspace exists and required files are present.")
    print("\nNext steps:")
    print("1. Open examples/docs-brief-demo/PROMPT_FOR_AGENT.md")
    print("2. Copy the prompt into Codex, ChatGPT, Claude, or another agent.")
    print("3. Ask the agent to create:")
    print("   - examples/docs-brief-demo/.agent-os/outputs/TASK-001/documentation_brief.md")
    print("   - examples/docs-brief-demo/.agent-os/handoffs/HANDOFF-TASK-001.md")
    print("4. Review the result against examples/docs-brief-demo/EXPECTED_OUTPUT_SAMPLE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
