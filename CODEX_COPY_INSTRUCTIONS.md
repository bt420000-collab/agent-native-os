# Codex Copy Instructions

This package is a direct overlay for the `agent-native-os` repository.

Codex should act as a file mover and validator, not as a theorist.

## Target repository

Expected project directory:

```txt
./agent-native-os/
```

If the repository is somewhere else, locate the directory containing:

```txt
README.md
SPEC.md
CORE_THEORY_AND_GLOSSARY.md
```

## Copy command

From the parent directory that contains both this extracted overlay and the repository:

```bash
cp -R agent-native-os-v0.2-demo-hotfix-overlay/. agent-native-os/
```

If using PowerShell on Windows:

```powershell
Copy-Item -Recurse -Force .\agent-native-os-v0.2-demo-hotfix-overlay\* .\agent-native-os\
```

## After copying

Run:

```bash
cd agent-native-os
python scripts/run_docs_brief_demo.py
python scripts/validate_workspace.py examples/docs-brief-demo
```

## Expected result

Both scripts should exit successfully.

Expected output should include:

```txt
PASS
Docs Brief Demo is ready.
```

## Do not do these things

Do not rename the project.

Do not add private domain editions.

Do not rewrite the core theory.

Do not turn Agent-Native OS into a prompt workflow system.

Do not compress Markdown, YAML, or Python files into single lines.

## Completion report

After copying and validation, create or update:

```txt
CODEX_COMPLETION_REPORT.md
```

Use the template included in this overlay.
