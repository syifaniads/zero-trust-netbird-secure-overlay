# Limitations

## Academic prototype scope

The project was a university implementation/prototype rather than a production enterprise Zero Trust deployment.

## Evidence limitations

The public portfolio is reconstructed from the surviving final project material. Not every command, source file, configuration export, or original Git history is available in this repository.

## Report inconsistency

The final report contains conflicting statements around Ryu, SDN, and VNF. Other sections scope the project around NetBird/JWT/Nextcloud and exclude Ryu/SDN. For that reason, this repository does **not** claim Ryu/SDN/VNF as verified implementation.

## Authentication evidence

A JWT/authentication component is described in the report, but it does not have the same surviving evidence level as the NetBird/Nextcloud/network implementation. It is therefore documented conservatively.

## Zero Trust maturity

The project demonstrates useful Zero Trust principles, but a production deployment would require additional controls such as:

- enterprise identity lifecycle;
- device posture and attestation;
- centralized audit logging;
- SIEM/alerting;
- secret management;
- high availability;
- backup and disaster recovery;
- automated policy validation;
- endpoint hardening;
- infrastructure-as-code and reproducible deployment;
- formal policy governance.

## Performance testing

This portfolio does not claim large-scale throughput, latency, HA, or capacity benchmarks because such evidence is not part of the verified project story.
