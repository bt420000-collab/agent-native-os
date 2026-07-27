# Context Virtual Memory Contract

Status: Experimental  
Introduced: ANO v0.3.0

## State model

```txt
REGISTERED
  → LEASED
  → MOUNTED_HOT | MOUNTED_WARM
  → COLD_REFERENCE
  → ARCHIVED
```

Registration, authorization, and visibility are separate transitions. No transition may be inferred from another.

## Context Object

```yaml
context_id: project.laws.current
source: user/projects/example/current/laws/
source_version: sha256-or-semantic-version
authority: project_law
classification: normal
token_estimate: 2400
```

## Lease validation

A conforming Host must reject a lease or mount when:

- the source is absolute or contains `..`;
- a denied scope matches the source;
- no readable scope matches the source;
- the lease is inactive or revoked;
- the Agent identity differs from the lease holder;
- visible token estimates would exceed the lease budget;
- a cross-App source did not arrive through an approved Bridge.

## Bootstrap working set

Every executable App run must begin with three pinned logical frames:

1. current task instruction;
2. authoritative laws and prohibitions;
3. output contract and acceptance gate.

The frames may point to multiple Context Objects, but their logical roles must be unambiguous.

## Page fault resolution

```txt
Agent detects missing evidence
  → emits Context Page Fault Request
  → Host checks active lease and catalog
  → Host mounts smallest sufficient authorized object
  → page table and audit event are updated
  → Agent resumes
```

A Page Fault Request is not approval. Apps may not resolve their own fault by widening scope.

## Eviction

Eviction candidates exclude pinned frames. Before a dirty page is evicted, the Host requires a checkpoint or Handoff Report. Eviction preserves a cold reference with context id, source version, last access, and reason.

## Recovery

A snapshot must contain:

- snapshot id and task id;
- active or paused leases;
- mounted context ids and tiers;
- backing source versions;
- checkpoint and Handoff Report references.

Resume must stop on source-version mismatch until the Host selects the current source, the snapshot source, or an explicit merge.
