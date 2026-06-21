# Official Skill App Packages

Agent Native OS Core is free and open-source. Skill Apps may be free, open-source, paid, freemium, or commercial, depending on the app developer.

This repository bundles first-party demo apps as **optional install packages** under:

```txt
app_packages/official/
```

They are not installed with the OS. During workspace initialization, the OS stages these ZIP packages into:

```txt
apps/_inbox/official/
```

The user then decides which packages to install after reviewing the install card.

## Full developer flow

```bash
python scripts/init_workspace.py
python ano/scripts/list_app_packages.py
python ano/scripts/install_app_package.py apps/_inbox/official/ano-calculator-skill-app_v0.1.2.zip
python ano/scripts/install_app_package.py apps/_inbox/official/ano-calculator-skill-app_v0.1.2.zip --yes
python ano/scripts/install_app_package.py apps/_inbox/official/ano-tiandao-furnace-skill-app_v0.4.0.zip
python ano/scripts/install_app_package.py apps/_inbox/official/ano-tiandao-furnace-skill-app_v0.4.0.zip --yes
python ano/scripts/validate_workspace.py
```

## Official free package #1: ANO Calculator Skill App

- File: `app_packages/official/ano-calculator-skill-app_v0.1.2.zip`
- App ID: `ano.skill.calculator`
- Package: `ano-calculator-skill-app`
- Pricing: free
- License: Apache-2.0
- Type: utility / zero-subagent reference app

Demonstrates the minimum ANO Skill App standard: manifest, install card, context request, tiny permissions, runtime health check, and clean workspace installation.

## Official free package #2: ANO Tiandao Furnace Skill App

- File: `app_packages/official/ano-tiandao-furnace-skill-app_v0.4.0.zip`
- App ID: `ano.skill.tiandao`
- Package: `ano-tiandao-furnace-skill-app`
- Pricing: free
- Type: multi-agent reference app
- Safety: entertainment-only symbolic random lab; no prediction claims, no betting advice, no probability-improvement claims.

Demonstrates a multi-agent ritual flow: visible agent roster, dynamic question batches, furnace heat gate, oracle-style entertainment interpretation, safety auditing, collision review, and experiment archiving.


## v0.2.8 rule

Official app packages are staged only. OS installation stops after staging. The app installer previews install cards by default and requires `--yes` after explicit user approval to install.

## Tiandao Furnace v0.4.0

The official multi-agent demo now enforces OS-hosted opening, previous-draw intake first, overflow-safe user choices, Host-mediated web/weather lookup requests, and feng-shui top-up. Direct `ritual` execution remains blocked. Use ANO Host command gate first.
