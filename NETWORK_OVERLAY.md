# Network Overlay

## Purpose

The overlay provides a private logical connectivity layer across distributed nodes while avoiding dependence on shared physical network location.

## NetBird in this project

The evidence-backed project story includes:

- multiple NetBird peers;
- peer status/configuration views;
- policy configuration;
- overlay addressing;
- connectivity tests between participating nodes;
- use of WireGuard through NetBird's networking model.

Historical peer names and addresses are intentionally abstracted here.

## Connectivity model

```text
Public / cloud network
        |
        +-- Linux peer A --+
        +-- Linux peer B --+--> NetBird-managed WireGuard overlay
        +-- Linux peer C --+
                              \
                               +--> protected Nextcloud service
```

The public network is treated as transport, while the overlay establishes the logical private path used by project participants.

## Why an overlay helps

A managed encrypted overlay can reduce operational friction compared with directly exposing every internal service or manually maintaining point-to-point VPN configuration. It also creates a convenient policy layer around peer groups and resource reachability.

## Security considerations

A secure overlay is not automatically secure merely because it is encrypted. Relevant controls include:

- safe peer enrollment;
- least-privilege policy;
- removal of stale peers;
- host firewalling and patching;
- protection of setup keys/tokens;
- application authentication;
- logging and monitoring.

## Portfolio sanitization

The original project documentation included environment-specific values. This repository does not publish historical IP addresses, passwords, private keys, setup keys, session material, or cloud credentials.
