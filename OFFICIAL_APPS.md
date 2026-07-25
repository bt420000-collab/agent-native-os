# Official Skill App Packages

Agent Native OS Core is free and open-source. Skill Apps may be free, open-source, paid, freemium, or commercial, depending on the app developer.

Official packages are stored under `app_packages/official/`. Workspace initialization stages them into `apps/_inbox/official/` and then stops. No App is auto-installed.

## Installation flow

```bash
python scripts/init_workspace.py
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip
python ano/scripts/install_app_package.py apps/_inbox/official/<package>.zip --yes
python ano/scripts/validate_workspace.py
```

The first install command previews the App installation card. Use `--yes` only after explicit user approval.

## Official free package #1: ANO Calculator Skill App

- File: `ano-calculator-skill-app_v0.1.2.zip`
- App ID: `ano.skill.calculator`
- Type: utility / zero-subagent reference App
- License: Apache-2.0

Demonstrates the minimum ANO App contract: manifest, installation card, tiny permission request, clean workspace installation, and health check.

## Official free package #2: ANO Tiandao Furnace Skill App

- File: `ano-tiandao-furnace-skill-app_v0.4.0.zip`
- App ID: `ano.skill.tiandao`
- Type: interactive multi-agent reference App
- Safety: entertainment-only symbolic random lab

Demonstrates visible Agent rosters, staged user interaction, dynamic question batches, furnace heat gating, Host-mediated web/weather requests, feng-shui entertainment interpretation, safety auditing, and experiment archiving.

## Official free package #3: ANO Novel Skill App

- File: `ano-novel-skill-app_v0.3.1.zip`
- App ID: `ano.skill.novel`
- Chinese display name: `ANO 小说工坊`
- Type: long-form novel production multi-agent App

Major capabilities:

- opening and context approval mediated by the single ANO Host
- source-law archive and project initialization
- built-in base prose/craft reference patch
- project-specific Literary Filter layer
- isolated Material Collection Lab
- Material Collector and Material Curator workflow
- material usage reports, handoff reports, material debt, and chapter preflight gates

The Novel App is optional. Installing the mother OS never installs or starts it automatically.

To preview and install it after OS initialization:

```bash
python ano/scripts/install_app_package.py apps/_inbox/official/ano-novel-skill-app_v0.3.1.zip
python ano/scripts/install_app_package.py apps/_inbox/official/ano-novel-skill-app_v0.3.1.zip --yes
python ano/scripts/ano_host.py "打开 ANO 小说工坊"
```
