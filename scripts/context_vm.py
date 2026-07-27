#!/usr/bin/env python3
"""Host-owned Context Virtual Memory reference helper for ANO v0.3.0.

This helper manages metadata and access contracts. It does not copy source
contents into an agent prompt and it never grants itself permission.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import sys
from pathlib import Path, PurePosixPath
from typing import Any

VERSION = "0.3.0"
HOST_ID = "ano.host"


def now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def workspace_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if all((candidate / name).exists() for name in ("ano", "user", "apps")):
            return candidate
    raise SystemExit("Not an ANO workspace: expected ano/, user/, and apps/.")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def append_event(root: Path, event: str, **payload: Any) -> None:
    path = root / "ano/runtime/context_vm/events.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {"event": event, "time": now(), **payload}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def paths(root: Path) -> dict[str, Path]:
    base = root / "ano/runtime/context_vm"
    return {
        "base": base,
        "catalog": base / "catalog.json",
        "leases": base / "leases.json",
        "page_table": base / "page_table.json",
        "faults": base / "page_faults.jsonl",
        "snapshots": base / "snapshots",
        "working_sets": base / "working_sets",
        "cold_refs": base / "cold_refs",
    }


def ensure_layout(root: Path) -> dict[str, Path]:
    state = paths(root)
    state["snapshots"].mkdir(parents=True, exist_ok=True)
    state["working_sets"].mkdir(parents=True, exist_ok=True)
    state["cold_refs"].mkdir(parents=True, exist_ok=True)
    if not state["catalog"].exists():
        write_json(state["catalog"], {"schema_version": VERSION, "objects": []})
    if not state["leases"].exists():
        write_json(state["leases"], {"schema_version": VERSION, "leases": []})
    if not state["page_table"].exists():
        write_json(state["page_table"], {"schema_version": VERSION, "mounts": []})
    state["faults"].touch(exist_ok=True)
    return state


def require_host(args: argparse.Namespace) -> None:
    if getattr(args, "host_id", None) != HOST_ID:
        raise SystemExit("Mutation denied: only ano.host may change Context VM state.")


def relative_source(value: str) -> str:
    normalized = value.replace("\\", "/").strip()
    path = PurePosixPath(normalized)
    if not normalized or path.is_absolute() or ".." in path.parts:
        raise SystemExit(f"Source must be a safe workspace-relative path: {value}")
    return str(path)


def scope_matches(source: str, pattern: str) -> bool:
    clean = pattern.replace("\\", "/").rstrip("/")
    return source == clean or source.startswith(clean + "/") or fnmatch.fnmatch(source, clean)


def source_allowed(source: str, lease: dict[str, Any]) -> bool:
    if any(scope_matches(source, item) for item in lease.get("denied", [])):
        return False
    return any(scope_matches(source, item) for item in lease.get("read_scope", []))


def find(items: list[dict[str, Any]], key: str, value: str) -> dict[str, Any] | None:
    return next((item for item in items if item.get(key) == value), None)


def command_register(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    catalog = read_json(state["catalog"], {"schema_version": VERSION, "objects": []})
    objects = catalog["objects"]
    if find(objects, "context_id", args.context_id):
        raise SystemExit(f"Context object already exists: {args.context_id}")
    source = relative_source(args.source)
    record = {
        "context_id": args.context_id,
        "source": source,
        "source_version": args.source_version,
        "authority": args.authority,
        "classification": args.classification,
        "token_estimate": args.token_estimate,
        "registered_by": HOST_ID,
        "registered_at": now(),
    }
    objects.append(record)
    write_json(state["catalog"], catalog)
    append_event(root, "context.registered", context_id=args.context_id, source=source)
    print(f"Registered {args.context_id} -> {source}")
    return 0


def command_grant_lease(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    leases_doc = read_json(state["leases"], {"schema_version": VERSION, "leases": []})
    leases = leases_doc["leases"]
    if find(leases, "lease_id", args.lease_id):
        raise SystemExit(f"Lease already exists: {args.lease_id}")
    lease = {
        "lease_id": args.lease_id,
        "task_id": args.task_id,
        "agent_id": args.agent_id,
        "status": "active",
        "budget_tokens": args.budget_tokens,
        "read_scope": [relative_source(item) for item in args.read_scope],
        "denied": [relative_source(item) for item in args.denied],
        "granted_by": HOST_ID,
        "granted_at": now(),
        "revocable": True,
    }
    leases.append(lease)
    write_json(state["leases"], leases_doc)
    append_event(root, "lease.granted", lease_id=args.lease_id, task_id=args.task_id)
    print(f"Granted lease {args.lease_id} to {args.agent_id}")
    return 0


def command_revoke_lease(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    leases_doc = read_json(state["leases"], {"schema_version": VERSION, "leases": []})
    lease = find(leases_doc["leases"], "lease_id", args.lease_id)
    if not lease:
        raise SystemExit(f"Unknown lease: {args.lease_id}")
    lease["status"] = "revoked"
    lease["revoked_at"] = now()
    page_table = read_json(state["page_table"], {"schema_version": VERSION, "mounts": []})
    evicted = [m for m in page_table["mounts"] if m.get("lease_id") == args.lease_id]
    page_table["mounts"] = [m for m in page_table["mounts"] if m.get("lease_id") != args.lease_id]
    write_json(state["leases"], leases_doc)
    write_json(state["page_table"], page_table)
    append_event(root, "lease.revoked", lease_id=args.lease_id, evicted_mounts=len(evicted))
    print(f"Revoked {args.lease_id}; evicted {len(evicted)} mount(s)")
    return 0


def command_mount(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    catalog = read_json(state["catalog"], {"objects": []})
    leases_doc = read_json(state["leases"], {"leases": []})
    page_table = read_json(state["page_table"], {"schema_version": VERSION, "mounts": []})
    context = find(catalog["objects"], "context_id", args.context_id)
    lease = find(leases_doc["leases"], "lease_id", args.lease_id)
    if not context:
        raise SystemExit(f"Unknown context object: {args.context_id}")
    if not lease or lease.get("status") != "active":
        raise SystemExit(f"Lease is missing or inactive: {args.lease_id}")
    if not source_allowed(context["source"], lease):
        raise SystemExit(f"Lease does not allow source: {context['source']}")
    existing = next(
        (
            item
            for item in page_table["mounts"]
            if item.get("lease_id") == args.lease_id and item.get("context_id") == args.context_id
        ),
        None,
    )
    if existing:
        existing.update({"tier": args.tier, "pinned": args.pin, "last_accessed_at": now()})
    else:
        used = sum(
            int(item.get("token_estimate", 0))
            for item in page_table["mounts"]
            if item.get("lease_id") == args.lease_id
        )
        requested = int(context.get("token_estimate", 0))
        if used + requested > int(lease.get("budget_tokens", 0)):
            raise SystemExit(
                f"Context budget exceeded: {used} + {requested} > {lease['budget_tokens']}"
            )
        page_table["mounts"].append(
            {
                "lease_id": args.lease_id,
                "task_id": lease["task_id"],
                "agent_id": lease["agent_id"],
                "context_id": args.context_id,
                "source": context["source"],
                "source_version": context["source_version"],
                "token_estimate": requested,
                "tier": args.tier,
                "pinned": args.pin,
                "reason": args.reason,
                "mounted_at": now(),
                "last_accessed_at": now(),
            }
        )
    write_json(state["page_table"], page_table)
    append_event(root, "context.mounted", lease_id=args.lease_id, context_id=args.context_id)
    print(f"Mounted {args.context_id} as {args.tier} under {args.lease_id}")
    return 0


def command_unmount(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    page_table = read_json(state["page_table"], {"schema_version": VERSION, "mounts": []})
    mount = next(
        (
            item
            for item in page_table["mounts"]
            if item.get("lease_id") == args.lease_id and item.get("context_id") == args.context_id
        ),
        None,
    )
    if not mount:
        raise SystemExit("Mount not found.")
    if mount.get("pinned") and not args.force:
        raise SystemExit("Pinned context cannot be evicted without an explicit Host force.")
    page_table["mounts"].remove(mount)
    cold_file = state["cold_refs"] / f"{args.lease_id}.json"
    cold = read_json(cold_file, {"lease_id": args.lease_id, "refs": []})
    cold["refs"].append({**mount, "evicted_at": now()})
    write_json(cold_file, cold)
    write_json(state["page_table"], page_table)
    append_event(root, "context.evicted", lease_id=args.lease_id, context_id=args.context_id)
    print(f"Evicted {args.context_id} to cold references")
    return 0


def command_fault(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    leases_doc = read_json(state["leases"], {"leases": []})
    lease = find(leases_doc["leases"], "lease_id", args.lease_id)
    if not lease or lease.get("status") != "active":
        raise SystemExit(f"Lease is missing or inactive: {args.lease_id}")
    if lease.get("agent_id") != args.agent_id:
        raise SystemExit("Page fault agent does not match the lease holder.")
    request = {
        "request_id": args.request_id,
        "lease_id": args.lease_id,
        "task_id": lease["task_id"],
        "agent_id": args.agent_id,
        "missing_need": args.missing_need,
        "reason": args.reason,
        "max_tokens": args.max_tokens,
        "status": "pending_host_resolution",
        "requested_at": now(),
    }
    with state["faults"].open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(request, ensure_ascii=False) + "\n")
    append_event(root, "page_fault.requested", request_id=args.request_id, lease_id=args.lease_id)
    print(f"Recorded page fault {args.request_id}; Host resolution required")
    return 0


def command_snapshot(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    require_host(args)
    leases = read_json(state["leases"], {"leases": []})["leases"]
    mounts = read_json(state["page_table"], {"mounts": []})["mounts"]
    snapshot = {
        "schema_version": VERSION,
        "snapshot_id": args.snapshot_id,
        "task_id": args.task_id,
        "created_by": HOST_ID,
        "created_at": now(),
        "leases": [item for item in leases if item.get("task_id") == args.task_id],
        "mounts": [item for item in mounts if item.get("task_id") == args.task_id],
    }
    write_json(state["snapshots"] / f"{args.snapshot_id}.json", snapshot)
    append_event(root, "context.snapshot_created", snapshot_id=args.snapshot_id, task_id=args.task_id)
    print(f"Created snapshot {args.snapshot_id}")
    return 0


def validate_state(state: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    catalog = read_json(state["catalog"], {"objects": []})
    leases = read_json(state["leases"], {"leases": []})
    page_table = read_json(state["page_table"], {"mounts": []})
    context_ids = [item.get("context_id") for item in catalog.get("objects", [])]
    lease_ids = [item.get("lease_id") for item in leases.get("leases", [])]
    if len(context_ids) != len(set(context_ids)):
        errors.append("Duplicate context_id in catalog.")
    if len(lease_ids) != len(set(lease_ids)):
        errors.append("Duplicate lease_id in lease table.")
    lease_map = {item.get("lease_id"): item for item in leases.get("leases", [])}
    context_map = {item.get("context_id"): item for item in catalog.get("objects", [])}
    usage: dict[str, int] = {}
    for mount in page_table.get("mounts", []):
        lease = lease_map.get(mount.get("lease_id"))
        context = context_map.get(mount.get("context_id"))
        if not lease or lease.get("status") != "active":
            errors.append(f"Mount uses inactive or missing lease: {mount.get('lease_id')}")
        if not context:
            errors.append(f"Mount uses missing context object: {mount.get('context_id')}")
        if lease and context and not source_allowed(context["source"], lease):
            errors.append(f"Mount source is outside lease scope: {context['source']}")
        lease_id = str(mount.get("lease_id"))
        usage[lease_id] = usage.get(lease_id, 0) + int(mount.get("token_estimate", 0))
    for lease_id, used in usage.items():
        budget = int(lease_map.get(lease_id, {}).get("budget_tokens", 0))
        if used > budget:
            errors.append(f"Lease {lease_id} exceeds budget: {used} > {budget}")
    return errors


def command_status(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    catalog = read_json(state["catalog"], {"objects": []})
    leases = read_json(state["leases"], {"leases": []})
    page_table = read_json(state["page_table"], {"mounts": []})
    active = [item for item in leases["leases"] if item.get("status") == "active"]
    faults = [line for line in state["faults"].read_text(encoding="utf-8").splitlines() if line]
    print(f"ANO Context VM v{VERSION}")
    print(f"Context objects: {len(catalog['objects'])}")
    print(f"Active leases: {len(active)}")
    print(f"Mounted pages: {len(page_table['mounts'])}")
    print(f"Page faults recorded: {len(faults)}")
    return 0


def command_validate(args: argparse.Namespace, root: Path, state: dict[str, Path]) -> int:
    errors = validate_state(state)
    if errors:
        print("Context VM validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("Context VM state is valid.")
    return 0


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description="ANO Host-owned Context Virtual Memory")
    sub = root.add_subparsers(dest="command", required=True)

    register = sub.add_parser("register")
    register.add_argument("--host-id", required=True)
    register.add_argument("--context-id", required=True)
    register.add_argument("--source", required=True)
    register.add_argument("--source-version", required=True)
    register.add_argument("--authority", default="project")
    register.add_argument("--classification", default="normal")
    register.add_argument("--token-estimate", type=int, required=True)
    register.set_defaults(func=command_register)

    lease = sub.add_parser("grant-lease")
    lease.add_argument("--host-id", required=True)
    lease.add_argument("--lease-id", required=True)
    lease.add_argument("--task-id", required=True)
    lease.add_argument("--agent-id", required=True)
    lease.add_argument("--budget-tokens", type=int, required=True)
    lease.add_argument("--read-scope", action="append", required=True)
    lease.add_argument("--denied", action="append", default=[])
    lease.set_defaults(func=command_grant_lease)

    revoke = sub.add_parser("revoke-lease")
    revoke.add_argument("--host-id", required=True)
    revoke.add_argument("--lease-id", required=True)
    revoke.set_defaults(func=command_revoke_lease)

    mount = sub.add_parser("mount")
    mount.add_argument("--host-id", required=True)
    mount.add_argument("--lease-id", required=True)
    mount.add_argument("--context-id", required=True)
    mount.add_argument("--tier", choices=("hot", "warm"), default="warm")
    mount.add_argument("--pin", action="store_true")
    mount.add_argument("--reason", required=True)
    mount.set_defaults(func=command_mount)

    unmount = sub.add_parser("unmount")
    unmount.add_argument("--host-id", required=True)
    unmount.add_argument("--lease-id", required=True)
    unmount.add_argument("--context-id", required=True)
    unmount.add_argument("--force", action="store_true")
    unmount.set_defaults(func=command_unmount)

    fault = sub.add_parser("page-fault")
    fault.add_argument("--request-id", required=True)
    fault.add_argument("--lease-id", required=True)
    fault.add_argument("--agent-id", required=True)
    fault.add_argument("--missing-need", required=True)
    fault.add_argument("--reason", required=True)
    fault.add_argument("--max-tokens", type=int, required=True)
    fault.set_defaults(func=command_fault)

    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("--host-id", required=True)
    snapshot.add_argument("--snapshot-id", required=True)
    snapshot.add_argument("--task-id", required=True)
    snapshot.set_defaults(func=command_snapshot)

    status = sub.add_parser("status")
    status.set_defaults(func=command_status)

    validate = sub.add_parser("validate")
    validate.set_defaults(func=command_validate)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    root = workspace_root()
    state = ensure_layout(root)
    return int(args.func(args, root, state))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
