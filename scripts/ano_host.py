#!/usr/bin/env python3
"""ANO Host/Admin Agent command gate v0.2.8.

All user instructions after OS installation must be mediated by the OS Host.
Users do not directly run app agents. This script is a lightweight CLI stand-in
for the persistent ANO Host/Admin Agent.

Usage:
  python ano/scripts/ano_host.py "打开 ANO Tiandao Furnace Skill AppAgent"
  python ano/scripts/ano_host.py "列出应用"
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional

HOST_NAME = "ANO Host / 管理员 Agent"

APP_KEYWORDS = {
    "ano.skill.tiandao": ["tiandao", "天道", "炉", "炉子", "hash", "furnace", "算命", "开炉"],
    "ano.skill.calculator": ["calculator", "计算器", "calc", "算数", "换算"],
}


def workspace_root(start: Optional[Path] = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    if (cur / "ano").is_dir() and (cur / "apps").is_dir() and (cur / "user").is_dir():
        return cur
    for p in cur.parents:
        if (p / "ano").is_dir() and (p / "apps").is_dir() and (p / "user").is_dir():
            return p
    raise SystemExit(
        "Not an ANO workspace. Run this from the authorized ANO workspace root.\n"
        "Expected root layout: README.md USER_LOG.md ano/ user/ apps/ res/ out/"
    )


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def read_zip_text(zf: zipfile.ZipFile, suffix: str) -> Optional[str]:
    for name in zf.namelist():
        if name.endswith(suffix):
            try:
                return zf.read(name).decode("utf-8", errors="replace")
            except Exception:
                return None
    return None


def yaml_field(text: Optional[str], key: str, default: str = "") -> str:
    if not text:
        return default
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*['\"]?([^'\"\n#]+)", text, re.M)
    return m.group(1).strip() if m else default


def inspect_package(path: Path) -> Dict[str, Any]:
    try:
        with zipfile.ZipFile(path) as zf:
            manifest = read_zip_text(zf, "/manifest.yaml") or read_zip_text(zf, "manifest.yaml")
            install_card = read_zip_text(zf, "/INSTALL_CARD.md") or read_zip_text(zf, "INSTALL_CARD.md")
            names = [n for n in zf.namelist() if n and not n.endswith("/")]
            top = names[0].split("/")[0] if names else path.stem
            return {
                "file": str(path),
                "package_name": yaml_field(manifest, "package_name", top),
                "app_id": yaml_field(manifest, "app_id", "unknown"),
                "display_name": yaml_field(manifest, "display_name", top),
                "version": yaml_field(manifest, "version", "unknown"),
                "pricing_model": yaml_field(manifest, "pricing_model", yaml_field(manifest, "pricing", "unknown")),
                "has_install_card": bool(install_card),
            }
    except Exception as exc:
        return {"file": str(path), "error": str(exc)}


def installed_apps(root: Path) -> List[Dict[str, Any]]:
    data = read_json(root / "ano/registry/installed_apps.json", {"installed_apps": []})
    return data.get("installed_apps", []) if isinstance(data, dict) else []


def pending_packages(root: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for inbox in ["apps/_inbox/official", "apps/_inbox/community"]:
        d = root / inbox
        if d.exists():
            for path in sorted(d.glob("*.zip")):
                item = inspect_package(path)
                item["relative_file"] = str(path.relative_to(root))
                items.append(item)
    return items


def match_app(instruction: str, apps: List[Dict[str, Any]], packages: List[Dict[str, Any]]) -> Optional[str]:
    text = instruction.lower()
    # First match curated domain keywords. Avoid generic words such as app/skill.
    for app_id, words in APP_KEYWORDS.items():
        if any(w.lower() in text for w in words):
            return app_id
    # Then match exact app_id or full display/package names.
    for item in apps + packages:
        app_id = str(item.get("app_id", "")).lower()
        display = str(item.get("display_name", "")).lower()
        package = str(item.get("package_name", "")).lower()
        for phrase in [app_id, display, package]:
            if phrase and phrase != "unknown" and phrase in text:
                return item.get("app_id")
    return None


def host_header(instruction: str) -> None:
    print("ANO Host Command Gate")
    print("=" * 40)
    print(f"身份：{HOST_NAME}")
    print("说明：OS 安装完成后，用户指令必须先由 ANO Host 接管。App 不能直接越级运行。")
    print(f"收到用户指令：{instruction}")
    print()


def show_apps(root: Path) -> None:
    apps = installed_apps(root)
    packages = pending_packages(root)
    print("已安装 Skill App：")
    if not apps:
        print("  - 暂无")
    for a in apps:
        print(f"  - {a.get('display_name')} ({a.get('app_id')}) @ {a.get('install_path')}")
    print("\n待安装 App 包：")
    if not packages:
        print("  - 暂无")
    for p in packages:
        print(f"  - {p.get('display_name')} ({p.get('app_id')}) v{p.get('version')} -> {p.get('relative_file')}")
    print("\n安装预览：python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip")
    print("用户明确批准安装后：python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes")


def find_installed(app_id: str, apps: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for a in apps:
        if a.get("app_id") == app_id:
            return a
    return None


def find_package(app_id: str, packages: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    for p in packages:
        if p.get("app_id") == app_id:
            return p
    return None


def open_installed_app(root: Path, app: Dict[str, Any]) -> int:
    app_id = app.get("app_id")
    display = app.get("display_name") or app_id
    install_path = root / str(app.get("install_path", ""))
    print(f"OS 处理结果：检测到已安装 App：{display}（{app_id}）。")
    print("OS 将先展示该 App 的上下文权限申请和 Agent 阵容，然后停止，等待用户下一步指令。")
    print()
    if app_id == "ano.skill.tiandao":
        runtime = install_path / "runtime" / "tiandao_furnace.py"
        if not runtime.exists():
            print(f"ERROR: Tiandao runtime not found: {runtime}")
            return 2
        proc = subprocess.run([sys.executable, str(runtime), "open"], cwd=str(install_path), text=True, capture_output=True)
        if proc.stdout:
            print(proc.stdout.rstrip())
        if proc.stderr:
            print(proc.stderr.rstrip(), file=sys.stderr)
        print("\nOS STOP：已完成 App 打开预检。不得继续 start 或 answer，除非用户下一条指令明确批准。")
        return proc.returncode
    if app_id == "ano.skill.calculator":
        print("计算器 App 是最小单体工具，无 Subagent。运行前仍由 OS 提示权限：tiny context, no network, no bridge。")
        print("常用命令示例：")
        print(f"  cd {app.get('install_path')}")
        print("  python runtime/calculator.py calc \"2 + 3 * 4\"")
        print("OS STOP：请等待用户指定具体计算表达式。")
        return 0
    print("该 App 尚未声明 OS 托管 open 入口。请阅读 INSTALL_CARD.md 或 README.md。")
    print("OS STOP：不要直接运行未知 App 的内部脚本。")
    return 0


def handle_instruction(root: Path, instruction: str) -> int:
    host_header(instruction)
    apps = installed_apps(root)
    packages = pending_packages(root)
    low = instruction.lower()

    if any(k in low for k in ["列表", "列出", "有哪些", "list", "app packages", "应用"]):
        show_apps(root)
        return 0

    app_id = match_app(instruction, apps, packages)
    if not app_id:
        print("OS 判断：未能明确匹配目标 App。")
        show_apps(root)
        print("\nOS STOP：请用户明确要打开或安装哪个 App。")
        return 0

    app = find_installed(app_id, apps)
    pkg = find_package(app_id, packages)

    if any(k in instruction for k in ["安装", "装上", "install"]):
        if app:
            print(f"OS 判断：{app.get('display_name')} 已安装，无需重复安装。")
            return 0
        if pkg:
            rel = pkg.get("relative_file")
            print(f"OS 判断：检测到待安装包：{pkg.get('display_name')} v{pkg.get('version')}")
            print("安装前必须先展示安装卡；只有用户明确批准时才可加 --yes。")
            print("预览安装卡：")
            print(f"  python ano/scripts/install_app_package.py {rel}")
            print("用户批准安装后：")
            print(f"  python ano/scripts/install_app_package.py {rel} --yes")
            print("OS STOP：不要自动补 --yes，除非用户指令已经明确要求立即安装。")
            return 0
        print("OS 判断：未找到该 App 的待安装包。")
        return 1

    if any(k in instruction for k in ["打开", "运行", "启动", "open", "run", "start"]):
        if app:
            return open_installed_app(root, app)
        if pkg:
            rel = pkg.get("relative_file")
            print(f"OS 判断：用户要打开的是 {pkg.get('display_name')}，但它还没有安装。")
            print("下一步应先走 App 安装流程，不得直接解压运行 App 内部脚本。")
            print("预览安装卡：")
            print(f"  python ano/scripts/install_app_package.py {rel}")
            print("用户明确批准安装后：")
            print(f"  python ano/scripts/install_app_package.py {rel} --yes")
            print("OS STOP：等待用户决定是否安装。")
            return 0

    print(f"OS 已识别目标 App：{app_id}，但指令类型不是打开/安装/列出。")
    print("OS STOP：请用户补充要执行的动作。")
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="ANO Host/Admin Agent command gate")
    p.add_argument("instruction", nargs="*", help="User instruction to be handled by ANO Host")
    args = p.parse_args(argv)
    root = workspace_root()
    instruction = " ".join(args.instruction).strip()
    if not instruction:
        instruction = "列出应用"
    return handle_instruction(root, instruction)


if __name__ == "__main__":
    raise SystemExit(main())
