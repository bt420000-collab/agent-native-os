#!/usr/bin/env python3
"""Validate a minimal Agent-Native OS workspace skeleton.

Usage:
    python scripts/validate_workspace.py [workspace-path]

The validator uses only the Python standard library.
"""

from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_AGENT_OS_DIRS = [
    "sources",
    "tasks",
    "outputs",
    "handoffs",
    "reviews",
]

OPTIONAL_AGENT_OS_DIRS = [
    "mounts",
    "contracts",
    "archive",
    "recovery",
    "registry",
]


def validate_workspace(workspace: Path) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not workspace.exists():
        errors.append(f"Workspace does not exist: {workspace}")
        return False, errors, warnings

    agent_os = workspace / ".agent-os"
    if not agent_os.exists():
        errors.append(f"Missing .agent-os directory: {agent_os}")
        return False, errors, warnings

    for dirname in REQUIRED_AGENT_OS_DIRS:
        path = agent_os / dirname
        if not path.exists() or not path.is_dir():
            errors.append(f"Missing required directory: .agent-os/{dirname}")

    for dirname in OPTIONAL_AGENT_OS_DIRS:
        path = agent_os / dirname
        if not path.exists():
            warnings.append(f"Optional directory not found: .agent-os/{dirname}")

    tasks_dir = agent_os / "tasks"
    if tasks_dir.exists():
        task_files = sorted(tasks_dir.glob("*.md"))
        if not task_files:
            errors.append("No task files found in .agent-os/tasks")
        else:
            for task_file in task_files:
                text = task_file.read_text(encoding="utf-8", errors="replace")
                if "Task ID" not in text and "task_id" not in text:
                    warnings.append(f"Task file may be missing Task ID: {task_file}")

    sources_dir = agent_os / "sources"
    if sources_dir.exists():
        source_files = [p for p in sources_dir.rglob("*") if p.is_file()]
        if not source_files:
            warnings.append("No source files found in .agent-os/sources")

    return not errors, errors, warnings


def main(argv: list[str]) -> int:
    workspace = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    workspace = workspace.resolve()

    ok, errors, warnings = validate_workspace(workspace)

    print("Agent-Native OS Workspace Validator")
    print("=" * 42)
    print(f"Workspace: {workspace}")

    if errors:
        print("\nFAIL:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("\nPASS: Workspace skeleton is valid.")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"  - {warning}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
