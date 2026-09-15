# Implementation Evidence Map

This document maps portfolio claims to the type of evidence present in the original project material. It deliberately avoids reproducing sensitive screenshots.

| Capability | Evidence type in original project material | Portfolio treatment |
| --- | --- | --- |
| Cloud/Linux nodes | Deployment screenshots/configuration context | Verified project component |
| NetBird peers | Peer list/status screenshots | Verified project component |
| WireGuard-based overlay | NetBird architecture/use + peer connectivity | Verified project component |
| NetBird policy | Policy/group configuration screenshots | Verified project component |
| Nextcloud | Docker/service screenshots | Verified project component |
| File collaboration | User/folder/share screenshots | Verified project scenario |
| Connectivity | Peer ping/reachability tests | Verified project validation |
| JWT/auth layer | Narrative/report description | Report-described |
| Ryu/SDN/VNF | Conflicting report statements | Not claimed as verified |

## Why screenshots are not copied directly

The original report contains sensitive environment-specific material. A public portfolio should preserve the **engineering claim** while removing secrets and unnecessary infrastructure exposure.

## Reviewer guidance

The strongest technical story in this repository is the combination of:

1. distributed Linux/cloud peers;
2. NetBird-managed WireGuard overlay;
3. explicit peer/network policy;
4. Dockerized Nextcloud;
5. application-level sharing permissions;
6. multi-node connectivity/access validation.

That is the architecture reviewers should use when evaluating the project.
