#!/usr/bin/env python3
"""Static checks for the sanitized NetBird/Nextcloud portfolio examples.

These checks validate repository invariants only. They do not prove a live
NetBird control plane, WireGuard tunnel, cloud node, or Nextcloud deployment.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        raise AssertionError(f"missing artifact: {path}")
    return p.read_text(encoding="utf-8")


def require(text: str, value: str, label: str) -> None:
    if value not in text:
        raise AssertionError(f"{label}: expected {value!r}")


def main() -> int:
    compose = read("examples/docker-compose.nextcloud.example.yml")
    policy = read("examples/netbird-policy.example.md")

    require(compose, "image: mariadb:11", "database image")
    require(compose, "image: nextcloud:stable", "Nextcloud image")
    require(compose, "${NEXTCLOUD_DB_PASSWORD}", "database password indirection")
    require(compose, "${MARIADB_ROOT_PASSWORD}", "root password indirection")
    require(compose, "db_data:/var/lib/mysql", "database persistence")
    require(compose, "nextcloud_data:/var/www/html", "Nextcloud persistence")

    for group in ("collaboration-client", "collaboration-service", "admin-operator"):
        require(policy, group, f"policy group {group}")
    require(policy, "Reduce lateral movement", "least-reachability rationale")
    require(policy, "application-level responsibility", "authorization boundary")

    # Common secret assignment patterns should not appear with literal values.
    suspicious = re.compile(
        r"(?im)^\s*(?:password|secret|private[_-]?key|setup[_-]?key|token)\s*(?:=|:)\s*(?!\$\{|<REDACTED>|<CHANGE_ME>|PLACEHOLDER).+"
    )
    for path in (ROOT / "examples").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if suspicious.search(text):
            raise AssertionError(f"possible literal secret in {path.relative_to(ROOT)}")

    print("portfolio validation passed")
    print("- Nextcloud + MariaDB example topology present")
    print("- credentials remain environment-driven")
    print("- persistent volumes remain declared")
    print("- NetBird policy model retains client/service/admin separation")
    print("- no obvious literal secret assignments detected")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
