# Results

## Evidence-backed outcomes

The surviving project material supports the following outcomes:

1. Multiple nodes were represented as peers in a NetBird-managed environment.
2. The project established an encrypted overlay using NetBird/WireGuard.
3. A Nextcloud collaboration service was deployed with Docker in the cloud/Linux environment.
4. Network access policies/groups were configured for the collaboration scenario.
5. Connectivity between participating nodes was tested.
6. Nextcloud accounts, folders, and sharing/access scenarios were exercised.

## What the results demonstrate

The project demonstrates a working relationship between three layers:

```text
secure transport / overlay
          ↓
network reachability policy
          ↓
application & data authorization
```

This layered view is the main security lesson of the project. Encryption alone does not define authorization, and network policy alone does not replace application permissions.

## What is not treated as a verified result

The final report contains inconsistent references to **Ryu, SDN, and VNF**. Because the strongest surviving implementation evidence centers on NetBird, Nextcloud, cloud hosts, policy configuration, and connectivity testing, this portfolio does not claim Ryu/SDN/VNF as verified project results.

Likewise, the report describes a JWT/authentication component, but the surviving source-level evidence available for this portfolio is weaker than for the network and Nextcloud portions. It is therefore labeled as **report-described** rather than independently verified here.

## Engineering takeaway

A portfolio should not maximize the number of technologies claimed. It should maximize the amount of **defensible engineering evidence** behind each claim. This repository follows that rule intentionally.
