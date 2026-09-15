# Zero Trust Model

## Scope

This project applies **Zero Trust principles** to a secure overlay collaboration scenario. It is not presented as a complete enterprise Zero Trust Architecture implementation.

## Principles applied

### 1. Explicit peer enrollment

A device does not receive the protected network path merely because it can reach the public Internet. It must first become an enrolled peer in the overlay environment.

### 2. Encrypted connectivity

Peer communication uses the NetBird/WireGuard overlay rather than assuming the underlying network is trusted.

### 3. Least-privilege reachability

Policies and groups are used to restrict which peers/services are reachable rather than relying on blanket east-west access.

### 4. Multiple authorization layers

Network policy answers **"can this peer reach that network resource?"**. Nextcloud authorization answers **"can this application user access that data?"**. These are different decisions and should not be conflated.

### 5. Verification

Controls are useful only when tested. The project therefore includes peer connectivity and access-control validation scenarios.

## Trust assumptions

The project still relies on trusted components:

- integrity of enrolled endpoints;
- correct NetBird account/policy configuration;
- secure handling of setup/enrollment material;
- correct Linux and Docker host configuration;
- correct Nextcloud authentication and sharing configuration.

A production Zero Trust environment would require stronger device posture, identity lifecycle, centralized logging, policy governance, secret management, monitoring, and incident-response controls.

## Zero Trust mapping

| Principle | Project implementation |
| --- | --- |
| Verify before granting network path | Overlay peer enrollment |
| Encrypt traffic | WireGuard-based tunnel |
| Restrict lateral access | NetBird policies/groups |
| Keep authorization contextual | Application permissions remain separate |
| Validate enforcement | Connectivity and access tests |

## Terminology note

This repository uses the phrase **"Zero Trust-inspired"** deliberately. It is a more precise representation than claiming full compliance with a specific enterprise Zero Trust standard or reference architecture.
