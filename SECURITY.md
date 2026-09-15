# Security Policy

## Public portfolio rules

This repository is a sanitized portfolio reconstruction. It must not contain real or historical secrets from the original lab/project environment.

Do not commit:

- passwords;
- private keys;
- SSH keys;
- NetBird setup/enrollment keys;
- API tokens;
- cloud credentials;
- session cookies/tokens;
- `.env` files with real values;
- historical credentials copied from screenshots or reports;
- infrastructure data that unnecessarily exposes a still-active environment.

## Examples

Files under `examples/` are intentionally generic and use placeholder values. They are not verbatim exports from the original deployment.

## Historical material

The original report contained environment-specific information. If any historical credential is still valid, it should be rotated/revoked rather than relying on the fact that the report is not committed here.

## Responsible disclosure

This repository is an academic/portfolio project. If a sensitive value is accidentally committed, remove it from the current tree, rotate the credential, and consider history rewriting if the value appeared in Git history.
