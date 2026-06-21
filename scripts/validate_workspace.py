#!/usr/bin/env python3
"""Validate an Agent-Native OS v0.2.8 clean workspace skeleton.

Usage:
    python ano/scripts/validate_workspace.py
    python scripts/validate_workspace.py
"""

from __future__ import annotations

from pathlib import Path
import json
import sys

VERSION = "0.2.8"
ROOT_ALLOWED = {"README.md", "USER_LOG.md", "ano", "user", "apps", "res", "out"}
LEGACY_ROOTS = {".agent-os", "skills"}
FORBIDDEN_ROOT_DIRS = {"ano-workspace", "my-workspace"}

REQUIRED_DIRS = [
    "ano/kernel",
    "ano/registry/apps",
    "ano/registry/mounts",
    "ano/runtime/apps",
    "ano/runtime/sessions",
    "ano/runtime/locks",
    "ano/runtime/bridges",
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
    "ano/kernel/CONTEXT_PERMISSION_MODEL.md",
    "ano/kernel/SCHEDULER.md",
    "ano/registry/installed_apps.json",
    "ano/runtime/process_table.json",
    "ano/runtime/context_allocations.json",
    "ano/runtime/events.jsonl",
    "ano/scripts/list_app_packages.py",
    "ano/scripts/install_app_package.py",
    "ano/scripts/validate_workspace.py",
    "user/profile/global_profile.yaml",
]

JSON_FILES = [
    "ano/registry/installed_apps.json",
    "ano/runtime/process_table.json",
    "ano/runtime/context_allocations.json",
]

RESERVED_APP_DIRS = {"_inbox"}


def validate_json(path: Path, errors: list[str]) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Invalid JSON: {path} ({exc})")


def validate_workspace(workspace: Path) -> tuple[bool, list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not workspace.exists():
        errors.append(f"Workspace does not exist: {workspace}")
        return False, errors, warnings

    if workspace.name in FORBIDDEN_ROOT_DIRS:
        errors.append(f"Forbidden workspace root name: {workspace.name}. Install ANO into the current authorized root, not a child workspace folder.")

    for legacy in LEGACY_ROOTS:
        if (workspace / legacy).exists():
            errors.append(f"Legacy root directory is forbidden in v0.2.2+ clean workspace: {legacy}")

    root_entries = {p.name for p in workspace.iterdir()}
    unknown = sorted(root_entries - ROOT_ALLOWED)
    if unknown:
        errors.append("Unexpected root entries found: " + ", ".join(unknown))

    for forbidden in FORBIDDEN_ROOT_DIRS:
        if (workspace / forbidden).exists():
            errors.append(f"Nested workspace directory is forbidden: {forbidden}")

    for dirname in REQUIRED_DIRS:
        path = workspace / dirname
        if not path.exists() or not path.is_dir():
            errors.append(f"Missing required directory: {dirname}")

    for filename in REQUIRED_FILES:
        path = workspace / filename
        if not path.exists() or not path.is_file():
            errors.append(f"Missing required file: {filename}")

    for filename in JSON_FILES:
        path = workspace / filename
        if path.exists():
            validate_json(path, errors)

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

    pending = list((workspace / "apps/_inbox/official").glob("*.zip")) + list((workspace / "apps/_inbox/community").glob("*.zip"))
    if pending:
        warnings.append(f"Pending Skill App packages detected: {len(pending)}. They are not installed until user approval.")

    installed_dirs = []
    apps_root = workspace / "apps"
    if apps_root.exists():
        installed_dirs = [p for p in apps_root.iterdir() if p.is_dir() and p.name not in RESERVED_APP_DIRS]

    registry_records = list((workspace / "ano/registry/apps").glob("*.json")) if (workspace / "ano/registry/apps").exists() else []
    if not registry_records:
        warnings.append("No installed app registry records found yet. This is normal before optional app installation.")
    if not installed_dirs:
        warnings.append("No Skill Apps installed yet. This is normal before optional app installation.")

    return not errors, errors, warnings


def main(argv: list[str]) -> int:
    workspace = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    workspace = workspace.resolve()

    ok, errors, warnings = validate_workspace(workspace)

    print("Agent-Native OS v0.2.8 Workspace Validator")
    print("=" * 48)
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
