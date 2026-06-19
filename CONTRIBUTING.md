# Contributing

Agent-Native OS is currently a specification-first project.

## Good contributions

- Clarify the spec
- Add neutral examples
- Improve templates
- Add validation scripts
- Add diagrams
- Add generic Skill App examples
- Improve security and permission models

## Avoid

- Domain-specific private workflows
- Prompt packs disguised as OS components
- Unvalidated claims
- Vendor-locked assumptions
- Hard dependency on a single model provider
- Hidden mutation of source files

## Design principles

1. Context is a first-class resource.
2. Skill Apps must declare permissions.
3. Outputs must be contract-bound.
4. Handoffs must be machine-readable enough to continue work.
5. Sources must have authority levels.
6. Long-running work must support audit and recovery.
