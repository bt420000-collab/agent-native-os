#!/usr/bin/env python3
"""
Initialize a minimal Agent-Native OS workspace.

Usage:
  python scripts/init_workspace.py my-workspace
"""

from pathlib import Path
import sys
import datetime

SKELETON_DIRS = [
    ".agent-os/registry",
    ".agent-os/sources",
    ".agent-os/tasks",
    ".agent-os/outputs",
    ".agent-os/handoffs",
    ".agent-os/reviews",
    ".agent-os/archive/hot",
    ".agent-os/archive/warm",
    ".agent-os/archive/cold",
    ".agent-os/recovery",
    "skills",
]

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")

def init_workspace(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for d in SKELETON_DIRS:
        (target / d).mkdir(parents=True, exist_ok=True)

    write(target / ".agent-os/registry/installed_skills.yaml", "installed_skills: []")
    write(target / ".agent-os/sources/README.md", "# Sources\n\nPut source materials here.")
    write(target / ".agent-os/tasks/README.md", "# Tasks\n\nPut task cards here.")
    write(target / ".agent-os/handoffs/README.md", "# Handoffs\n\nPut handoff reports here.")
    write(target / ".agent-os/reviews/README.md", "# Reviews\n\nPut audit reports here.")
    write(target / ".agent-os/recovery/README.md", "# Recovery\n\nPut recovery points here.")
    write(target / "README.md", f"""# Agent OS Workspace

Initialized: {datetime.datetime.utcnow().isoformat()}Z

This workspace follows the Agent-Native OS v0.1 structure.
""")

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/init_workspace.py <workspace-path>")
        return 1
    init_workspace(Path(sys.argv[1]))
    print(f"Initialized Agent OS workspace at: {sys.argv[1]}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
