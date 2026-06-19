# Governance

Agent-Native OS starts as a maintainer-led specification project.

## Maintainer Responsibilities

- Keep the public core vendor-neutral and broadly useful.
- Protect the boundary between open architecture and private editions.
- Review changes for source authority, permission, audit, and recovery implications.
- Prefer small, clear specification changes over broad rewrites.
- Keep examples generic enough for public reuse.

## Decision Process

Project decisions are made through public issues and pull requests when possible.

Maintainers may accept straightforward documentation, template, and example improvements directly. Larger changes to the architecture should include:

- The problem or failure mode being addressed.
- The proposed contract, schema, or runtime behavior.
- Compatibility impact on existing examples.
- Security and governance tradeoffs.

## Private Editions

Private editions may extend the open core with domain-specific workflows, scoring systems, business logic, or proprietary operational patterns. Those private layers should not be required to understand, implement, or contribute to the public architecture.
