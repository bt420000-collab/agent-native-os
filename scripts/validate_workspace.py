#!/usr/bin/env python3
"""Validate an Agent-Native OS v0.3.0 clean workspace skeleton.

Usage:
    python ano/scripts/validate_workspace.py
    python scripts/validate_workspace.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

VERSION = "0.3.0"
ROOT_ALLOWED = {"README.md", "USER_LOG.md", "ano", "user", "apps", "res", "out"}
LEGACY_ROOTS = {".agent-os", "skills"}
FORBIDDEN_ROOT_DIRS = {"ano-workspace", "my-workspace"}

REQUIRED_DIRS = [
    "ano/kernel",
    "ano/registry/apps",
    "ano/registry/mounts",
    "ano/registry/context_objects",
    "ano/runtime/apps",
    "ano/runtime/sessions",
    "ano/runtime/locks",
    "ano/runtime/bridges",
    "ano/runtime/context_vm/working_sets",
    "ano/runtime/context_vm/cold_refs",
    "ano/runtime/context_vm/snapshots",
    "ano/scripts",
    "ano/logs",
    "user/profile",
    "user/preferences",
    "user/memory",
    "user/apps",
    "user/projects",
    "user/imports/_unsorted",
    "apps/_inbox/official",
    "apps/_inbox/community",
    "apps/_inbox/installed",
    "res",
    "out",
]

REQUIRED_FILES = [
    "README.md",
    "USER_LOG.md",
    "ano/VERSION",
    "ano/kernel/HOST.md",
    "ano/kernel/FILESYSTEM_STANDARD.md",
    "ano/kernel/APP_PACKAGE_INBOX.md",
    "ano/kernel/OS_AGENT_COMMAND_GATE.md",
    "ano/kernel/CONTEXT_PERMISSION_MODEL.md",
    "ano/kernel/CONTEXT_VIRTUAL_MEMORY.md",
    "ano/kernel/SCHEDULER.md",
    "ano/registry/installed_apps.json",
    "ano/runtime/process_table.json",
    "ano/runtime/context_allocations.json",
    "ano/runtime/context_vm/catalog.json",
    "ano/runtime/context_vm/leases.json",
    "ano/runtime/context_vm/page_table.json",
    "ano/runtime/context_vm/page_faults.jsonl",
    "ano/runtime/context_vm/events.jsonl",
    "ano/runtime/events.jsonl",
    "ano/scripts/list_app_packages.py",
    "ano/scripts/install_app_package.py",
    "ano/scripts/validate_workspace.py",
    "ano/scripts/ano_host.py",
    "ano/scripts/context_vm.py",
    "user/profile/global_profile.yaml",
]

JSON_FILES = [
    "ano/registry/installed_apps.json",
    "ano/runtime/process_table.json",
    "ano/runtime/context_allocations.json",
    "ano/runtime/context_vm/catalog.json",
    "ano/runtime/context_vm/leases.json",
    "ano/runtime/context_vm/page_table.json",
]

RESERVED_APP_DIRS = {"_inbox"}


def validate_json(path: Path, errors: list[str]) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid JSON: {path} ({exc})")


def validate_workspace(workspace: Path) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not workspace.exists():
        errors.append(f"Workspace does not exist: {workspace}")
        return False, errors, warnings

    if workspace.name in FORBIDDEN_ROOT_DIRS:
        errors.append(
            f"Forbidden workspace root name: {workspace.name}. "
            "Install ANO into the current authorized root."
        )

    for legacy in LEGACY_ROOTS:
        if (workspace / legacy).exists():
            errors.append(f"Legacy root directory is forbidden: {legacy}")

    root_entries = {path.name for path in workspace.iterdir()}
    unknown = sorted(root_entries - ROOT_ALLOWED)
    if unknown:
        errors.append("Unexpected root entries found: " + ", ".join(unknown))

    for forbidden in FORBIDDEN_ROOT_DIRS:
        if (workspace / forbidden).exists():
            errors.append(f"Nested workspace directory is forbidden: {forbidden}")

    for dirname in REQUIRED_DIRS:
        path = workspace / dirname
        if not path.is_dir():
            errors.append(f"Missing required directory: {dirname}")

    for filename in REQUIRED_FILES:
        path = workspace / filename
        if not path.is_file():
            errors.append(f"Missing required file: {filename}")

    for filename in JSON_FILES:
        path = workspace / filename
        if path.exists():
            validate_json(path, errors)

    version_file = workspace / "ano/VERSION"
    if version_file.exists():
        actual = version_file.read_text(encoding="utf-8").strip()
        if actual != VERSION:
            errors.append(f"Workspace version mismatch: expected {VERSION}, found {actual}")

    process_table = workspace / "ano/runtime/process_table.json"
    if process_table.exists():
        try:
            table = json.loads(process_table.read_text(encoding="utf-8"))
            host = table.get("host", {})
            if host.get("id") != "ano.host":
                warnings.append("process_table.json host.id should be ano.host")
            if not host.get("persistent"):
                warnings.append("process_table.json host.persistent should be true")
        except Exception:
            pass

    pending = (
        list((workspace / "apps/_inbox/official").glob("*.zip"))
        + list((workspace / "apps/_inbox/community").glob("*.zip"))
    )
    if pending:
        warnings.append(
            f"Pending Skill App packages detected: {len(pending)}. "
            "They remain uninstalled until user approval."
        )

    apps_root = workspace / "apps"
    installed_dirs = []
    if apps_root.exists():
        installed_dirs = [
            path
            for path in apps_root.iterdir()
            if path.is_dir() and path.name not in RESERVED_APP_DIRS
        ]

    registry_root = workspace / "ano/registry/apps"
    registry_records = list(registry_root.glob("*.json")) if registry_root.exists() else []
    if not registry_records:
        warnings.append("No installed App registry records found yet. This is normal before installation.")
    if not installed_dirs:
        warnings.append("No Skill Apps installed yet. This is normal before optional installation.")

    return not errors, errors, warnings


def main(argv: list[str]) -> int:
    workspace = (Path(argv[1]) if len(argv) > 1 else Path.cwd()).resolve()
    ok, errors, warnings = validate_workspace(workspace)

    print(f"Agent-Native OS v{VERSION} Workspace Validator")
    print("=" * 50)
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
