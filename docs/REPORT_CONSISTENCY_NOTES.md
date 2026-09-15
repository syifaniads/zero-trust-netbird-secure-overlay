# Report Consistency Notes

## Why this file exists

The final academic report is useful evidence, but it is not internally consistent in every technical statement. This portfolio therefore documents the inconsistency rather than silently choosing whichever wording sounds more impressive.

## Main inconsistency

One part of the report scopes the implementation around **NetBird, JWT, and Nextcloud** and states that SDN/Ryu is outside the implementation scope. Later implementation/conclusion wording references **Ryu Controller, SDN flow rules, and VNF**.

The strongest surviving screenshots/configuration evidence supports the NetBird/Nextcloud/cloud-peer implementation.

## Portfolio decision

This repository therefore:

- **claims** NetBird/WireGuard overlay networking;
- **claims** cloud-hosted Linux peers;
- **claims** Dockerized Nextcloud;
- **claims** NetBird peer/policy configuration and connectivity testing;
- **labels** JWT/authentication as report-described when source evidence is weaker;
- **does not claim** Ryu/SDN/VNF as verified implementation.

## Why this is stronger than copying the report

Security and infrastructure engineering depend on evidence quality. Explicitly documenting uncertainty is preferable to overstating a technology simply because its name appears in a report.

If stronger original Ryu/SDN/VNF artifacts are recovered later, this file and the architecture can be updated with direct evidence.
