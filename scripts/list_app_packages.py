#!/usr/bin/env python3
"""List pending Skill App packages in the current ANO workspace.

Usage:
  python ano/scripts/list_app_packages.py
  python scripts/list_app_packages.py
"""
from __future__ import annotations
from pathlib import Path
import argparse, json, re, zipfile

APP_INBOXES = ["apps/_inbox/official", "apps/_inbox/community"]


def read_zip_text(zf: zipfile.ZipFile, suffix: str) -> str | None:
    for name in zf.namelist():
        if name.endswith(suffix):
            try:
                return zf.read(name).decode('utf-8', errors='replace')
            except Exception:
                return None
    return None


def field(text: str | None, key: str, default: str = "") -> str:
    if not text:
        return default
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*['\"]?([^'\"\n#]+)", text, re.M)
    return m.group(1).strip() if m else default


def inspect_package(path: Path) -> dict:
    try:
        with zipfile.ZipFile(path) as zf:
            manifest = read_zip_text(zf, '/manifest.yaml') or read_zip_text(zf, 'manifest.yaml')
            install_card = read_zip_text(zf, '/INSTALL_CARD.md') or read_zip_text(zf, 'INSTALL_CARD.md')
            names = [n for n in zf.namelist() if n and not n.endswith('/')]
            top = names[0].split('/')[0] if names else path.stem
            return {
                'file': str(path),
                'package_name': field(manifest, 'package_name', top),
                'app_id': field(manifest, 'app_id', 'unknown'),
                'display_name': field(manifest, 'display_name', top),
                'version': field(manifest, 'version', 'unknown'),
                'pricing_model': field(manifest, 'pricing_model', field(manifest, 'pricing', 'unknown')),
                'has_install_card': bool(install_card),
            }
    except Exception as exc:
        return {'file': str(path), 'error': str(exc)}


def find_packages(workspace: Path) -> list[Path]:
    packages: list[Path] = []
    for inbox in APP_INBOXES:
        root = workspace / inbox
        if root.exists():
            packages.extend(sorted(root.glob('*.zip')))
    return packages


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--workspace', default='.', help="Must point to the current ANO workspace. Default: current directory.")
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    workspace = Path(args.workspace).resolve()
    if not (workspace / 'ano').exists():
        raise SystemExit(f'Not an ANO workspace: {workspace}')
    items = [inspect_package(x) for x in find_packages(workspace)]
    if args.json:
        print(json.dumps({'workspace': str(workspace), 'pending_packages': items}, ensure_ascii=False, indent=2))
        return 0
    print('ANO Pending Skill App Packages')
    print('=' * 36)
    print(f'Workspace: {workspace}')
    if not items:
        print('\nNo pending app packages found.')
        return 0
    for i, item in enumerate(items, 1):
        print(f"\n[{i}] {item.get('display_name', 'Unknown App')}")
        print(f"    file: {item.get('file')}")
        print(f"    app_id: {item.get('app_id')}")
        print(f"    package: {item.get('package_name')}")
        print(f"    version: {item.get('version')}")
        print(f"    pricing: {item.get('pricing_model')}")
        print(f"    install_card: {'yes' if item.get('has_install_card') else 'no'}")
    print('\nPreview install card without installing:')
    print('  python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip')
    print('\nInstall only after explicit user approval:')
    print('  python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
