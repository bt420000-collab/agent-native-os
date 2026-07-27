#!/usr/bin/env python3
"""
Initialize Agent-Native OS v0.3.0 in the current authorized workspace root.

Hard rule:
  ANO installs into the current working directory only.
  It must not create a child workspace folder such as ano-workspace/ or my-workspace/.

Usage:
  python scripts/init_workspace.py
  python path/to/agent-native-os-main/scripts/init_workspace.py
  python scripts/init_workspace.py --no-bundled-apps
"""
from __future__ import annotations

import argparse
import datetime
import json
import shutil
import sys
from pathlib import Path

VERSION = "0.3.0"
ROOT_ALLOWED = {"README.md", "USER_LOG.md", "ano", "user", "apps", "res", "out"}
LEGACY_ROOTS = {".agent-os", "skills"}
FORBIDDEN_WORKSPACE_NAMES = {"ano-workspace", "my-workspace"}

SKELETON_DIRS = [
    "ano/kernel",
    "ano/registry/apps",
    "ano/registry/mounts",
    "ano/registry/context_objects",
    "ano/runtime/apps",
    "ano/runtime/sessions",
    "ano/runtime/locks",
    "ano/runtime/bridges",
    "ano/runtime/tmp",
    "ano/runtime/context_vm/working_sets",
    "ano/runtime/context_vm/cold_refs",
    "ano/runtime/context_vm/snapshots",
    "ano/logs",
    "ano/scripts",
    "ano/templates",
    "ano/spec",
    "user/profile",
    "user/preferences",
    "user/memory",
    "user/apps",
    "user/projects",
    "user/imports/_unsorted",
    "apps/_inbox/official",
    "apps/_inbox/community",
    "apps/_inbox/installed",
    "res/icons",
    "res/schemas",
    "res/shared_assets",
    "out/reports",
    "out/exports",
]

RUNTIME_SCRIPTS = [
    "list_app_packages.py",
    "install_app_package.py",
    "validate_workspace.py",
    "ano_host.py",
    "context_vm.py",
]


def iso_now() -> str:
    return (
        datetime.datetime.now(datetime.UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text.rstrip() + "\n")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def assert_current_root(target_arg: str | None) -> Path:
    cwd = Path.cwd().resolve()
    if target_arg is None:
        target = cwd
    else:
        target = Path(target_arg).resolve()
        if target != cwd:
            raise SystemExit(
                f"ANO v{VERSION} installs into the current authorized workspace root only.\n"
                f"Current directory: {cwd}\n"
                f"Rejected target:   {target}\n"
                "cd into the user-authorized directory, then run:\n"
                "  python scripts/init_workspace.py"
            )

    if target.name in FORBIDDEN_WORKSPACE_NAMES:
        raise SystemExit(
            f"Refusing to install into deprecated workspace folder name: {target.name}\n"
            "Use the user-authorized project root itself."
        )
    return target


def copy_runtime_scripts(target: Path) -> list[str]:
    copied: list[str] = []
    scripts_src = repo_root() / "scripts"
    for name in RUNTIME_SCRIPTS:
        src = scripts_src / name
        if not src.exists():
            continue
        dst = target / "ano" / "scripts" / name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(name)
    return copied


def copy_static_templates_and_specs(target: Path) -> tuple[list[str], list[str]]:
    copied_templates: list[str] = []
    copied_specs: list[str] = []
    mappings = [
        ("templates", "ano/templates", copied_templates),
        ("spec", "ano/spec", copied_specs),
    ]
    for source_name, target_name, output in mappings:
        src_dir = repo_root() / source_name
        dst_dir = target / target_name
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.glob("*")):
            if src.is_file():
                shutil.copy2(src, dst_dir / src.name)
                output.append(src.name)
    return copied_templates, copied_specs


def stage_bundled_app_packages(target: Path, include: bool = True) -> list[str]:
    """Stage official ZIP packages without installing them."""
    staged: list[str] = []
    if not include:
        return staged

    src_dir = repo_root() / "app_packages" / "official"
    dst_dir = target / "apps" / "_inbox" / "official"
    if not src_dir.exists():
        return staged

    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.glob("*.zip")):
        shutil.copy2(src, dst_dir / src.name)
        staged.append(src.name)
    return staged


def cleanup_root(target: Path, now: str) -> list[str]:
    """Move non-standard root entries into user imports after installation."""
    moved: list[str] = []
    staging = target / "user" / "imports" / "_unsorted" / now.replace(":", "").replace("-", "")
    for entry in list(target.iterdir()):
        if entry.name in ROOT_ALLOWED:
            continue
        staging.mkdir(parents=True, exist_ok=True)
        destination = staging / entry.name
        suffix = 1
        while destination.exists():
            destination = staging / f"{entry.name}.{suffix}"
            suffix += 1
        shutil.move(str(entry), str(destination))
        moved.append(entry.name)
    return moved


def write_kernel_documents(target: Path) -> None:
    write(
        target / "ano/kernel/HOST.md",
        """
# OS Host

Agent-Native OS has exactly one persistent Host.

The Host belongs to the mother system. Apps may define coordinators, but Apps are not Hosts.
""",
    )
    write(
        target / "ano/kernel/FILESYSTEM_STANDARD.md",
        """
# Workspace Filesystem Standard

Installed Agent-Native OS workspaces use the current authorized directory as the root.

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

Rules:

1. Do not create a nested workspace folder.
2. `ano/` stores system internals.
3. `user/` stores user data, preferences, memory, projects, and imports.
4. `apps/` stores installed Apps and the pending App Package Inbox.
5. `res/` stores shared resources.
6. `out/` stores final user-facing outputs.
7. Apps and subagents must not write arbitrary files to the workspace root.
8. Legacy `.agent-os/` and `skills/` roots are forbidden.
""",
    )
    write(
        target / "ano/kernel/APP_PACKAGE_INBOX.md",
        """
# App Package Inbox

Pending Skill App ZIP packages live under:

```txt
apps/_inbox/official/
apps/_inbox/community/
apps/_inbox/installed/
```

Packages in `official/` and `community/` are install candidates only. They require explicit user approval.
After OS initialization, the Host must stop and return control to the user.
""",
    )
    write(
        target / "ano/kernel/OS_AGENT_COMMAND_GATE.md",
        """
# OS Agent Command Gate

Every user instruction is mediated by the ANO Host/Admin Agent after installation.

The Host checks App installation state, displays the install or runtime approval card,
and stops for user approval before an App can run. Do not bypass the Host by directly
executing files under `apps/<app>/runtime/`.
""",
    )
    write(
        target / "ano/kernel/CONTEXT_PERMISSION_MODEL.md",
        """
# Context Permission Model

Apps do not own context. Apps request context.

Every App run begins with a Context Permission Request approved by the OS Host.
""",
    )
    write(
        target / "ano/kernel/CONTEXT_VIRTUAL_MEMORY.md",
        """
# Context Virtual Memory

ANO Host owns the Context Catalog, revocable task leases, Agent working sets,
Page Fault resolution, eviction, and recovery snapshots.

Apps request context. They do not mount sources, widen leases, or approve their
own Page Fault Requests.
""",
    )
    write(
        target / "ano/kernel/SCHEDULER.md",
        """
# Scheduler

The OS Host owns subagent lifecycle control, process state, context allocation, and Cross-App Bridge approval.
""",
    )


def write_workspace_support_files(target: Path, now: str, staged_packages: list[str], copied_scripts: list[str]) -> None:
    write(target / "user/profile/global_profile.yaml", "profile_id: global\nuser_defined_agent_topology: {}\npreferences: {}")
    write(target / "user/imports/README.md", "# Imports\n\nPut source materials or raw user files here.")
    write(target / "user/projects/README.md", "# Projects\n\nUser projects live here.")
    write(target / "out/README.md", "# Output\n\nFinal user-facing outputs live here.")
    write(target / "res/README.md", "# Resources\n\nShared static resources live here.")
    write(
        target / "apps/README.md",
        """
# Apps

Installed Skill Apps live under `apps/<package_name>/`.

Pending packages live under `apps/_inbox/official/` and `apps/_inbox/community/`.
A package in `_inbox` is not installed.

```bash
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
python ano/scripts/validate_workspace.py
python ano/scripts/context_vm.py status
python ano/scripts/context_vm.py validate
```
""",
    )
    write(
        target / "apps/_inbox/README.md",
        """
# Skill App Package Inbox

- `official/`: bundled official reference packages
- `community/`: user-added or third-party packages
- `installed/`: archived packages that were installed through OS approval
""",
    )
    write(target / "apps/_inbox/official/README.md", "# Official App Packages\n\nOfficial reference packages staged for optional installation.")
    write(target / "apps/_inbox/community/README.md", "# Community App Packages\n\nPlace third-party Skill App ZIP packages here before installation.")
    write(target / "apps/_inbox/installed/README.md", "# Installed App Package Archive\n\nPackages are moved here after successful installation.")

    if staged_packages:
        package_text = "\n".join(f"- `apps/_inbox/official/{name}`" for name in staged_packages)
    else:
        package_text = "- No bundled App packages were staged."

    script_text = ", ".join(f"`{name}`" for name in copied_scripts) or "none"
    write(
        target / "README.md",
        f"""
# Agent-Native OS Workspace

Initialized: {now}  
Version: {VERSION}  
Filesystem: current root clean v1  
App package inbox: enabled

This workspace follows the Agent-Native OS v{VERSION} filesystem and Host-gate contract.

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

## Installation is complete

ANO initialization stops here. Do not auto-install or auto-start a Skill App.

## OS Host command gate

```bash
python ano/scripts/ano_host.py "列出应用"
python ano/scripts/ano_host.py "打开 ANO 小说工坊"
```

The Host checks installation state and displays the required approval card before continuing.

## Pending Skill App packages

{package_text}

## App installation

```bash
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
```

The command without `--yes` is preview-only.

## Validation

```bash
python ano/scripts/validate_workspace.py
```

Runtime scripts copied into this workspace: {script_text}
""",
    )

    log_lines = [
        "# User Log",
        "",
        f"- {now}: Initialized Agent-Native OS workspace v{VERSION} in the current directory.",
        f"- {now}: App Package Inbox enabled at `apps/_inbox/`.",
        f"- {now}: OS initialization completed and stopped. No App was auto-installed.",
    ]
    log_lines.extend(
        f"- {now}: Detected pending official Skill App package `{name}`. User approval required before installation."
        for name in staged_packages
    )
    write(target / "USER_LOG.md", "\n".join(log_lines))


def init_workspace(target: Path, no_bundled_apps: bool = False) -> dict:
    target.mkdir(parents=True, exist_ok=True)
    now = iso_now()

    for dirname in SKELETON_DIRS:
        (target / dirname).mkdir(parents=True, exist_ok=True)

    copied_scripts = copy_runtime_scripts(target)
    copied_templates, copied_specs = copy_static_templates_and_specs(target)
    staged_packages = stage_bundled_app_packages(target, include=not no_bundled_apps)

    write(target / "ano/VERSION", VERSION)
    write_kernel_documents(target)
    write_json(target / "ano/registry/installed_apps.json", {"installed_apps": []})
    write_json(
        target / "ano/runtime/process_table.json",
        {
            "host": {
                "id": "ano.host",
                "type": "system_host",
                "status": "running",
                "persistent": True,
                "created_at": now,
            },
            "processes": [],
        },
    )
    write_json(target / "ano/runtime/context_allocations.json", {"allocations": []})
    write_json(target / "ano/runtime/context_vm/catalog.json", {"schema_version": VERSION, "objects": []})
    write_json(target / "ano/runtime/context_vm/leases.json", {"schema_version": VERSION, "leases": []})
    write_json(target / "ano/runtime/context_vm/page_table.json", {"schema_version": VERSION, "mounts": []})
    write(target / "ano/runtime/context_vm/page_faults.jsonl", "")
    write(target / "ano/runtime/context_vm/events.jsonl", "")
    write(
        target / "ano/runtime/events.jsonl",
        json.dumps(
            {
                "event": "workspace.initialized",
                "version": VERSION,
                "filesystem": "current_root_clean_v1",
                "app_package_inbox": True,
                "context_virtual_memory": True,
                "staged_packages": staged_packages,
                "time": now,
            },
            ensure_ascii=False,
        ),
    )
    write_workspace_support_files(target, now, staged_packages, copied_scripts)

    moved = cleanup_root(target, now)
    if moved:
        moved_text = ", ".join(f"`{name}`" for name in moved)
        append(target / "README.md", f"\nRoot cleanup moved these entries to `user/imports/_unsorted/`: {moved_text}")
        append(target / "USER_LOG.md", f"- {now}: Root cleanup moved entries into `user/imports/_unsorted/`: {moved_text}.")

    return {
        "version": VERSION,
        "workspace": str(target),
        "staged_packages": staged_packages,
        "copied_scripts": copied_scripts,
        "copied_templates": copied_templates,
        "copied_specs": copied_specs,
        "moved_root_entries": moved,
    }


def print_final_notice(result: dict) -> None:
    print(f"Initialized Agent-Native OS v{VERSION} in current workspace root: {result['workspace']}")
    print("\nWorkspace root layout:")
    print("  README.md  USER_LOG.md  ano/  user/  apps/  res/  out/")
    print("\nPending official App packages staged:")
    staged = result.get("staged_packages", [])
    if staged:
        for name in staged:
            print(f"  - apps/_inbox/official/{name}")
    else:
        print("  - none")
    print("\nSTOP: OS initialization is complete.")
    print("Do not auto-install Skill Apps. Return control to the user.")
    print("\nNext commands:")
    print('  python ano/scripts/ano_host.py "列出应用"')
    print("  python ano/scripts/validate_workspace.py")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "workspace_path",
        nargs="?",
        default=None,
        help="Must be omitted or '.'; ANO installs into the current directory only.",
    )
    parser.add_argument(
        "--no-bundled-apps",
        action="store_true",
        help="Do not stage bundled official App packages.",
    )
    args = parser.parse_args(argv)
    target = assert_current_root(args.workspace_path)
    result = init_workspace(target, no_bundled_apps=args.no_bundled_apps)
    print_final_notice(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
