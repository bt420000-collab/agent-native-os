#!/usr/bin/env python3
"""
Validate a minimal Agent-Native OS workspace skeleton.

Usage:
  python scripts/validate_workspace.py [workspace-path]
"""

from pathlib import Path
import sys


REQUIRED_DIRS = [
    ".agent-os",
    ".agent-os/sources",
    ".agent-os/tasks",
    ".agent-os/outputs",
    ".agent-os/handoffs",
    ".agent-os/reviews",
]


def validate_workspace(workspace: Path) -> list[str]:
    failures: list[str] = []

    if not workspace.exists():
        return [f"workspace does not exist: {workspace}"]

    if not workspace.is_dir():
        return [f"workspace is not a directory: {workspace}"]

    for required in REQUIRED_DIRS:
        path = workspace / required
        if not path.is_dir():
            failures.append(f"missing directory: {required}")

    tasks_dir = workspace / ".agent-os" / "tasks"
    if tasks_dir.is_dir():
        task_files = sorted(
            path for path in tasks_dir.iterdir()
            if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json"}
        )
        if not task_files:
            failures.append("no task file found in .agent-os/tasks")

    return failures


def main(argv: list[str]) -> int:
    workspace = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    failures = validate_workspace(workspace)

    print("Agent-Native OS workspace validation")
    print(f"Workspace: {workspace}")

    if failures:
        print("\nFAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nPASS")
    print("- .agent-os skeleton exists")
    print("- required workspace directories exist")
    print("- at least one task file exists")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
