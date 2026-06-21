#!/usr/bin/env python3
"""
Initialize Agent-Native OS v0.2.8 in the current authorized workspace root.

Hard rule:
  ANO installs into the current working directory only.
  It must not create a child workspace folder such as ano-workspace/ or my-workspace/.

Usage:
  python scripts/init_workspace.py
  python path/to/agent-native-os-main/scripts/init_workspace.py
  python scripts/init_workspace.py --no-bundled-apps
"""

from __future__ import annotations

from pathlib import Path
import argparse
import datetime
import json
import shutil
import sys

VERSION = "0.2.8"
ROOT_ALLOWED = {"README.md", "USER_LOG.md", "ano", "user", "apps", "res", "out"}
LEGACY_ROOTS = {".agent-os", "skills"}
FORBIDDEN_WORKSPACE_NAMES = {"ano-workspace", "my-workspace"}

SKELETON_DIRS = [
    "ano/kernel",
    "ano/registry/apps",
    "ano/registry/mounts",
    "ano/runtime/apps",
    "ano/runtime/sessions",
    "ano/runtime/locks",
    "ano/runtime/bridges",
    "ano/runtime/tmp",
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
]


def iso_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def append(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def assert_current_root(target_arg: str | None) -> Path:
    cwd = Path.cwd().resolve()
    if target_arg is None:
        return cwd
    target = Path(target_arg).resolve()
    if target != cwd:
        raise SystemExit(
            "ANO v0.2.8 installs into the current authorized workspace root only.\n"
            f"Current directory: {cwd}\n"
            f"Rejected target:   {target}\n"
            "Do not create a child workspace directory. cd into the directory that the user authorized, then run:\n"
            "  python scripts/init_workspace.py\n"
            "or from an extracted source folder:\n"
            "  python agent-native-os-main/scripts/init_workspace.py"
        )
    if cwd.name in FORBIDDEN_WORKSPACE_NAMES:
        raise SystemExit(
            f"Refusing to install into deprecated workspace folder name: {cwd.name}\n"
            "Use the user-authorized project root itself, not ano-workspace/ or my-workspace/."
        )
    return cwd


def copy_runtime_scripts(target: Path) -> list[str]:
    copied: list[str] = []
    scripts_src = repo_root() / "scripts"
    for name in RUNTIME_SCRIPTS:
        src = scripts_src / name
        if src.exists():
            dst = target / "ano" / "scripts" / name
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            copied.append(name)
    return copied


def copy_static_templates_and_specs(target: Path) -> tuple[list[str], list[str]]:
    copied_templates: list[str] = []
    copied_specs: list[str] = []
    for source_dir_name, target_dir_name, out_list in [
        ("templates", "ano/templates", copied_templates),
        ("spec", "ano/spec", copied_specs),
    ]:
        src_dir = repo_root() / source_dir_name
        dst_dir = target / target_dir_name
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for src in sorted(src_dir.glob("*")):
            if src.is_file():
                shutil.copy2(src, dst_dir / src.name)
                out_list.append(src.name)
    return copied_templates, copied_specs


def stage_bundled_app_packages(target: Path, include: bool = True) -> list[str]:
    """Copy bundled official app ZIP packages into apps/_inbox/official/.

    This does not install apps. ANO must stop after OS initialization and wait for
    the user's next instruction.
    """
    staged: list[str] = []
    if not include:
        return staged
    src_dir = repo_root() / "app_packages" / "official"
    dst_dir = target / "apps" / "_inbox" / "official"
    if not src_dir.exists():
        return staged
    dst_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.glob("*.zip")):
        dst = dst_dir / src.name
        shutil.copy2(src, dst)
        staged.append(src.name)
    return staged


def cleanup_root(target: Path, now: str) -> list[str]:
    """Move non-standard root entries into user/imports/_unsorted/<timestamp>/.

    This runs after runtime scripts and official app packages have been staged, so
    an extracted source folder can be safely moved out of the workspace root.
    """
    moved: list[str] = []
    target.mkdir(parents=True, exist_ok=True)
    staging = target / "user" / "imports" / "_unsorted" / now.replace(":", "").replace("-", "")
    for entry in list(target.iterdir()):
        if entry.name in ROOT_ALLOWED:
            continue
        staging.mkdir(parents=True, exist_ok=True)
        destination = staging / entry.name
        if destination.exists():
            suffix = 1
            while (staging / f"{entry.name}.{suffix}").exists():
                suffix += 1
            destination = staging / f"{entry.name}.{suffix}"
        shutil.move(str(entry), str(destination))
        moved.append(entry.name)
    return moved


def init_workspace(target: Path, no_bundled_apps: bool = False) -> dict:
    target.mkdir(parents=True, exist_ok=True)
    now = iso_now()

    for d in SKELETON_DIRS:
        (target / d).mkdir(parents=True, exist_ok=True)

    copied_scripts = copy_runtime_scripts(target)
    copied_templates, copied_specs = copy_static_templates_and_specs(target)
    staged_packages = stage_bundled_app_packages(target, include=not no_bundled_apps)

    write(target / "ano/VERSION", VERSION)
    write(target / "ano/kernel/HOST.md", """
# OS Host

Agent-Native OS has exactly one Host.

The Host belongs to the mother system. Apps may define coordinators, but apps are not Hosts.
""")

    write(target / "ano/kernel/FILESYSTEM_STANDARD.md", """
# Workspace Filesystem Standard

Installed Agent-Native OS workspaces use the current authorized directory as the root. The installer must not create child workspace folders.

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

1. The current directory is the workspace root. Do not create `ano-workspace/`, `my-workspace/`, or any other child workspace folder.
2. Root is for the user, not for system clutter.
3. `ano/` stores system internals: Host policy, runtime, registry, scheduler state, logs, templates, scripts, and specs.
4. `user/` stores user data, preferences, memory, projects, and imported materials.
5. `apps/` stores installed Skill Apps. `apps/_inbox/` stores pending app ZIP packages awaiting user approval.
6. `res/` stores shared resources.
7. `out/` stores final user-facing outputs.
8. Apps and subagents must not write arbitrary files to the workspace root.
9. Legacy `.agent-os/` and `skills/` directories are forbidden in v0.2.2+ clean workspaces.
10. Unknown root files are moved to `user/imports/_unsorted/` during installation or cleanup.
""")

    write(target / "ano/kernel/APP_PACKAGE_INBOX.md", """
# App Package Inbox

The mother system may stage Skill App packages in `apps/_inbox/` but must not auto-install them.

```txt
apps/_inbox/official/    Official free demo packages bundled with the OS release.
apps/_inbox/community/   User-added or community app packages.
apps/_inbox/installed/   Packages already installed through OS approval.
```

Packages in `_inbox` are install candidates. They become installed apps only after the user explicitly asks the OS to install them.

After OS installation, the agent must stop and return control to the user. It must not continue into app installation automatically.
""")

    write(target / "ano/kernel/OS_AGENT_COMMAND_GATE.md", """
# OS Agent Command Gate

Hard rule: after Agent-Native OS is installed, every user instruction is addressed to the ANO Host/Admin Agent first.

The user does not directly talk to or run app agents. A request such as `打开 ANO Tiandao Furnace Skill AppAgent` must be handled as:

1. ANO Host acknowledges it is the OS administrator handling the request.
2. ANO Host identifies the target app by user-facing name, for example `天道哈希炉 / ANO Tiandao Furnace Skill App`.
3. ANO Host checks whether the app is installed or only staged in `apps/_inbox/`.
4. If not installed, ANO Host shows the install card and stops for user approval.
5. If installed, ANO Host shows the Context Permission Request and Agent Runtime Approval Card.
6. ANO Host stops and waits for the user's next instruction.
7. App internal runtime commands may only run after OS-mediated approval.

Do not bypass the OS by `cd apps/<app>/` and running internal scripts directly unless ANO Host has already approved that exact step.

Command gate helper:

```bash
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
python ano/scripts/ano_host.py "列出应用"
```
""")

    write(target / "ano/kernel/CONTEXT_PERMISSION_MODEL.md", """
# Context Permission Model

Apps do not own context. Apps request context.

Every app run should begin with a Context Permission Request approved by the OS Host.
""")

    write(target / "ano/kernel/SCHEDULER.md", """
# Scheduler

The OS Host owns subagent lifecycle control, process state, context allocation, and cross-app bridge approval.
""")

    write_json(target / "ano/registry/installed_apps.json", {"installed_apps": []})
    write_json(target / "ano/runtime/process_table.json", {
        "host": {
            "id": "ano.host",
            "type": "system_host",
            "status": "running",
            "persistent": True,
            "created_at": now,
        },
        "processes": [],
    })
    write_json(target / "ano/runtime/context_allocations.json", {"allocations": []})
    write(target / "ano/runtime/events.jsonl", json.dumps({
        "event": "workspace.initialized",
        "version": VERSION,
        "filesystem": "current_root_clean_v1",
        "app_package_inbox": True,
        "staged_packages": staged_packages,
        "time": now,
    }, ensure_ascii=False))

    write(target / "user/profile/global_profile.yaml", """
profile_id: global
user_defined_agent_topology: {}
preferences: {}
""")

    write(target / "user/imports/README.md", "# Imports\n\nPut source materials or raw user files here.")
    write(target / "user/projects/README.md", "# Projects\n\nUser projects live here.")
    write(target / "out/README.md", "# Output\n\nFinal user-facing outputs live here.")
    write(target / "res/README.md", "# Resources\n\nShared static resources live here.")
    write(target / "apps/README.md", """
# Apps

Installed Skill Apps live directly under `apps/<package_name>/`.

Pending app packages live under:

```txt
apps/_inbox/official/
apps/_inbox/community/
```

A package in `_inbox` is not installed yet.

Basic commands:

```bash
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
python ano/scripts/validate_workspace.py
```

The installer command without `--yes` only previews the install card and exits. It does not prompt or block.
""")
    write(target / "apps/_inbox/README.md", """
# Skill App Package Inbox

This folder stores pending app ZIP packages awaiting user approval.

- `official/`: official free demo packages bundled with ANO.
- `community/`: packages added by the user or third-party developers.
- `installed/`: packages already installed through OS approval.

Packages in `official/` and `community/` are not installed apps. Installed packages are moved to `installed/` after success.
""")
    write(target / "apps/_inbox/official/README.md", "# Official App Packages\n\nOfficial demo app packages staged for optional installation.")
    write(target / "apps/_inbox/community/README.md", "# Community App Packages\n\nDrop third-party Skill App ZIP packages here before installation.")
    write(target / "apps/_inbox/installed/README.md", "# Installed App Package Archive\n\nPackages are moved here after successful installation so they no longer appear as pending.")

    package_text = "No bundled app packages were staged."
    if staged_packages:
        package_text = "Detected pending official Skill App packages:\n" + "\n".join(f"- `apps/_inbox/official/{name}`" for name in staged_packages)

    script_text = ""
    if copied_scripts:
        script_text = "Runtime scripts copied to `ano/scripts/`: " + ", ".join(f"`{x}`" for x in copied_scripts)

    write(target / "README.md", f"""
# Agent-Native OS Workspace

Initialized: {now}  
Version: {VERSION}  
Filesystem: current root clean v1  
App package inbox: enabled

This workspace follows the Agent-Native OS v0.2.8 filesystem standard.

```txt
README.md
USER_LOG.md
ano/
user/
apps/
res/
out/
```

Key rules:

```txt
Host is the OS. Apps are not Hosts.
The current directory is the workspace root.
Do not create ano-workspace/ or any child workspace folder.
Apps live in apps/. System internals live in ano/.
Pending app packages live in apps/_inbox/ and require user approval.
Final user-facing outputs live in out/.
```

## Installation is complete

ANO OS installation stops here. The agent must not automatically install any app package after this point. Wait for the user's next instruction.

## OS Host command gate

Hard rule: after installation, all user instructions are handled by the ANO Host/Admin Agent first. Do not jump into `apps/<app>/runtime/` directly.

Handle a user instruction through the OS Host:

```bash
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
```

The Host will check installation status, print the app runtime permission request, and stop for user approval.

## Pending Skill App packages

{package_text}

## App installation guide

List staged packages:

```bash
python ano/scripts/list_app_packages.py
```

Preview one package's install card without installing:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
```

Install only after the user explicitly approves:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
```

## Basic operation commands

Handle any user instruction through ANO Host:

```bash
python ano/scripts/ano_host.py "列出应用"
python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
```

Validate this workspace:

```bash
python ano/scripts/validate_workspace.py
```

View user log:

```bash
cat USER_LOG.md
```

Check installed apps registry:

```bash
cat ano/registry/installed_apps.json
```

{script_text}
""")

    package_log = ""
    if staged_packages:
        package_log = "\n" + "\n".join(f"- {now}: Detected pending official Skill App package `{name}`. User approval required before install." for name in staged_packages)

    write(target / "USER_LOG.md", f"""
# User Log

- {now}: Initialized Agent-Native OS workspace v{VERSION} in the current directory.
- {now}: App package inbox enabled at `apps/_inbox/`.
- {now}: OS installation completed and stopped. No app was auto-installed.
{package_log}
""")

    moved = cleanup_root(target, now)
    if moved:
        moved_note = "\nRoot cleanup moved these entries to `user/imports/_unsorted/`: " + ", ".join(f"`{x}`" for x in moved) + "\n"
        append(target / "README.md", moved_note)
        append(target / "USER_LOG.md", f"- {now}: Root cleanup moved entries into `user/imports/_unsorted/`: " + ", ".join(f"`{x}`" for x in moved) + ".")

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
    print("\nPending official app packages staged:")
    staged = result.get("staged_packages", [])
    if staged:
        for name in staged:
            print(f"  - apps/_inbox/official/{name}")
    else:
        print("  - none")
    print("\nSTOP: OS installation is complete.")
    print("Do not auto-install Skill Apps. Return control to the user and wait for the next instruction.")
    print("After installation, every user instruction must be handled by ANO Host/Admin Agent first.")
    print("Do not cd into apps/<app>/runtime and run app internals directly.")
    print("\nOS Host command gate:")
    print("  python ano/scripts/ano_host.py \"列出应用\"")
    print("  python ano/scripts/ano_host.py \"打开 ANO Tiandao Furnace Skill AppAgent\"")
    print("\nApp installation guide:")
    print("  python ano/scripts/list_app_packages.py")
    print("  python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip")
    print("  python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes")
    print("\nBasic operation commands:")
    print("  python ano/scripts/ano_host.py \"列出应用\"")
    print("  python ano/scripts/validate_workspace.py")
    print("  cat USER_LOG.md")
    print("  cat ano/registry/installed_apps.json")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workspace_path", nargs="?", default=None, help="Must be omitted or '.'; ANO installs into the current directory only.")
    parser.add_argument("--no-bundled-apps", action="store_true", help="Do not stage bundled official app packages into apps/_inbox/official/.")
    args = parser.parse_args(argv)
    target = assert_current_root(args.workspace_path)
    result = init_workspace(target, no_bundled_apps=args.no_bundled_apps)
    print_final_notice(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
