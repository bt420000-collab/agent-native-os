# Codex Identity Fix Instructions

This overlay fixes a repository identity misunderstanding.

External AI summarizers may currently describe Agent-Native OS as "a Python project" because the repository contains Python validation scripts.

That is wrong.

Agent-Native OS is a spec-first, natural-language-first architecture project.

## Copy action

Copy this overlay into the `agent-native-os` repository root:

```txt
.gitattributes
REPO_IDENTITY.md
AI_SUMMARY_HINT.md
README_IDENTITY_PATCH.md
CODEX_IDENTITY_FIX_INSTRUCTIONS.md
```

## README update

Read `README_IDENTITY_PATCH.md`.

Insert the English patch section into `README.md`.

Insert the Chinese patch section into `README.zh-CN.md`.

Do not rewrite the whole README.

## Do not change

- project name
- homepage images
- core theory
- demo files
- public/private boundary
- Python helper scripts

## Validation

After copying, check:

```bash
git status --short
python scripts/run_docs_brief_demo.py
python scripts/validate_workspace.py examples/docs-brief-demo
```

## Completion report

Update or create `CODEX_COMPLETION_REPORT.md` with:

```txt
identity fix applied
files changed
commands run
validation result
whether README identity section was inserted
```
