#!/usr/bin/env python3
"""Preview or install a pending Skill App package into the current ANO workspace.

Usage:
  python ano/scripts/install_app_package.py apps/_inbox/official/app.zip
  python ano/scripts/install_app_package.py apps/_inbox/official/app.zip --yes

Default behavior is preview-only and non-interactive.
Use --yes only after the user explicitly approves the installation.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

VERSION = "0.2.13"


def iso_now() -> str:
    return (
        datetime.datetime.now(datetime.UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def read_zip_text(zf: zipfile.ZipFile, suffix: str) -> str | None:
    for name in zf.namelist():
        if name.endswith(suffix):
            try:
                return zf.read(name).decode("utf-8", errors="replace")
            except Exception:
                return None
    return None


def field(text: str | None, key: str, default: str = "") -> str:
    if not text:
        return default
    match = re.search(rf"^\s*{re.escape(key)}\s*:\s*['\"]?([^'\"\n#]+)", text, re.M)
    return match.group(1).strip() if match else default


def package_top(zf: zipfile.ZipFile) -> str:
    for name in zf.namelist():
        if name and not name.endswith("/"):
            return name.split("/")[0]
    raise ValueError("Package is empty")


def inspect_package(package_zip: Path) -> dict:
    with zipfile.ZipFile(package_zip) as zf:
        top = package_top(zf)
        manifest = read_zip_text(zf, "/manifest.yaml") or read_zip_text(zf, "manifest.yaml")
        install_card = read_zip_text(zf, "/INSTALL_CARD.md") or read_zip_text(zf, "INSTALL_CARD.md")
        app_id = field(manifest, "app_id", top)
        package_name = field(manifest, "package_name", top)
        return {
            "top": top,
            "app_id": app_id,
            "package_name": package_name,
            "display_name": field(manifest, "display_name", package_name),
            "version": field(manifest, "version", "unknown"),
            "pricing_model": field(
                manifest,
                "pricing_model",
                field(manifest, "pricing", "unknown"),
            ),
            "install_card": install_card or "",
        }


def assert_workspace(workspace: Path) -> Path:
    workspace = workspace.resolve()
    if workspace != Path.cwd().resolve():
        raise SystemExit(
            "ANO App installation must run from the current workspace root.\n"
            f"Current directory: {Path.cwd().resolve()}\n"
            f"Rejected workspace: {workspace}"
        )
    if not (workspace / "ano").exists():
        raise SystemExit(f"Not an ANO workspace: {workspace}")

    version_file = workspace / "ano/VERSION"
    if version_file.exists():
        actual = version_file.read_text(encoding="utf-8").strip()
        if actual != VERSION:
            raise SystemExit(
                f"Workspace version mismatch: installer expects {VERSION}, found {actual}"
            )
    return workspace


def append_event(workspace: Path, event: dict) -> None:
    path = workspace / "ano/runtime/events.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def update_installed_apps(workspace: Path, record: dict) -> None:
    path = workspace / "ano/registry/installed_apps.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {"installed_apps": []}
    if path.exists():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            pass
    apps = [
        item
        for item in data.get("installed_apps", [])
        if item.get("app_id") != record["app_id"]
    ]
    apps.append(record)
    data["installed_apps"] = apps
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def print_install_card(info: dict) -> None:
    print(f"ANO v{VERSION} Skill App Install Request")
    print("=" * 42)
    print(f"App: {info['display_name']}")
    print(f"App ID: {info['app_id']}")
    print(f"Package: {info['package_name']}")
    print(f"Version: {info['version']}")
    print(f"Pricing: {info['pricing_model']}")
    if info["install_card"]:
        print("\n--- INSTALL_CARD.md ---")
        print(info["install_card"].strip())
        print("--- END INSTALL_CARD.md ---")


def install(
    workspace: Path,
    package_zip: Path,
    yes: bool = False,
    force: bool = False,
    keep_package: bool = False,
) -> dict:
    workspace = assert_workspace(workspace)
    package_zip = package_zip.resolve()
    if not package_zip.exists():
        raise SystemExit(f"Package not found: {package_zip}")

    info = inspect_package(package_zip)
    print_install_card(info)

    if not yes:
        print("\nPreview only: no App was installed.")
        relative = (
            package_zip.relative_to(workspace)
            if package_zip.is_relative_to(workspace)
            else package_zip
        )
        print("To install after explicit user approval, run:")
        print(f"  python ano/scripts/install_app_package.py {relative} --yes")
        return {"installed": False, "preview_only": True, **info}

    target = workspace / "apps" / info["package_name"]
    if target.exists():
        if not force:
            raise SystemExit(f"App already installed: {target} (use --force to replace)")
        shutil.rmtree(target)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(package_zip) as zf:
            zf.extractall(tmp_path)
        src = tmp_path / info["top"]
        if not src.exists():
            raise SystemExit("Extracted package root not found")
        shutil.move(str(src), str(target))

    app_id = info["app_id"]
    domain = app_id.split(".")[-1] if "." in app_id else info["package_name"]
    for relative in [
        f"ano/runtime/apps/{app_id}/state",
        f"ano/runtime/apps/{app_id}/logs",
        f"ano/runtime/apps/{app_id}/inbox",
        f"ano/runtime/apps/{app_id}/outbox",
        f"user/apps/{app_id}",
        f"out/{domain}",
    ]:
        (workspace / relative).mkdir(parents=True, exist_ok=True)

    now = iso_now()
    record = {
        "app_id": app_id,
        "package_name": info["package_name"],
        "display_name": info["display_name"],
        "version": info["version"],
        "pricing_model": info["pricing_model"],
        "installed_at": now,
        "install_path": f'apps/{info["package_name"]}',
        "runtime_path": f"ano/runtime/apps/{app_id}",
        "user_context_path": f"user/apps/{app_id}",
        "source_package": str(package_zip),
    }

    registry_file = workspace / "ano/registry/apps" / f"{app_id}.json"
    registry_file.parent.mkdir(parents=True, exist_ok=True)
    registry_file.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    update_installed_apps(workspace, record)
    append_event(workspace, {"event": "app.installed", "time": now, **record})

    archived_to: str | None = None
    inbox_root = (workspace / "apps/_inbox").resolve()
    try:
        package_zip.relative_to(inbox_root)
        in_inbox = True
    except ValueError:
        in_inbox = False

    if in_inbox and not keep_package:
        archive_dir = workspace / "apps/_inbox/installed"
        archive_dir.mkdir(parents=True, exist_ok=True)
        archive_path = archive_dir / package_zip.name
        if archive_path.exists():
            stamp = now.replace(":", "").replace("-", "")
            archive_path = archive_dir / f"{package_zip.stem}.{stamp}{package_zip.suffix}"
        shutil.move(str(package_zip), str(archive_path))
        archived_to = str(archive_path)
        record["archived_package"] = archived_to
        registry_file.write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        update_installed_apps(workspace, record)

    with (workspace / "USER_LOG.md").open("a", encoding="utf-8") as handle:
        handle.write(
            f"\n- {now}: Installed Skill App `{app_id}` from `{package_zip.name}`.\n"
        )
        if archived_to:
            relative_archive = Path(archived_to).relative_to(workspace)
            handle.write(
                f"- {now}: Archived installed package to `{relative_archive}`.\n"
            )

    print(f"\nInstalled: {info['display_name']} -> {target}")
    if archived_to:
        print(f"Archived package: {archived_to}")
    return {"installed": True, **record}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "package_zip",
        help="Path to a pending App package ZIP, usually apps/_inbox/official/<package>.zip",
    )
    parser.add_argument(
        "--workspace",
        default=".",
        help="Must be '.' or the current workspace root.",
    )
    parser.add_argument(
        "--yes",
        "--approve",
        action="store_true",
        help="Install after explicit user approval. Otherwise preview only.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed App folder.",
    )
    parser.add_argument(
        "--keep-package",
        action="store_true",
        help="Keep an inbox package in place after installation.",
    )
    args = parser.parse_args()
    install(
        Path(args.workspace),
        Path(args.package_zip),
        args.yes,
        args.force,
        args.keep_package,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
