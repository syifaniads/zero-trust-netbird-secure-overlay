# Example NetBird Policy Model

> Sanitized conceptual example. This is not an export of the original NetBird account.

## Groups

- `collaboration-client`
- `collaboration-service`
- `admin-operator`

## Intended rules

| Source | Destination | Service | Action | Rationale |
| --- | --- | --- | --- | --- |
| collaboration-client | collaboration-service | HTTPS / approved app port | Allow | Reach protected collaboration service |
| admin-operator | collaboration-service | SSH | Allow | Controlled administration |
| collaboration-client | unrelated peers | Any | Deny / no allow rule | Reduce lateral movement |

## Design rule

Prefer explicit business-required paths over broad all-to-all connectivity.

This network policy only addresses **reachability**. Folder/file authorization remains an application-level responsibility in Nextcloud.
