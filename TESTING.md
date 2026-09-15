# Testing Strategy

## Objective

The project validation asks a simple question: **does the implemented policy produce the expected network and collaboration behavior?**

A strong validation plan therefore checks positive and negative cases.

## Test categories

### 1. Peer enrollment and status

Verify that expected nodes appear in the NetBird environment and are connected/available as intended.

### 2. Overlay connectivity

Use basic network tests to verify expected peer reachability through the secure overlay.

### 3. Policy enforcement

Test traffic from different peer roles/groups against the configured policy. The important result is not just "ping works" but whether **allowed paths work and restricted paths do not**.

### 4. Nextcloud service reachability

Confirm that authorized peers can reach the protected collaboration service over the intended network path.

### 5. Application/data authorization

Test Nextcloud users/shares separately from network reachability. A reachable service should still enforce application permissions.

## Test matrix

| Test | Expected result | Control being tested |
| --- | --- | --- |
| Enrolled peer reaches permitted peer/service | Allow | Overlay + policy |
| Restricted peer attempts disallowed path | Deny | NetBird policy |
| Authorized user opens shared Nextcloud content | Allow | Nextcloud authorization |
| Unprivileged user requests unauthorized content | Deny | Nextcloud authorization |
| Peer is not enrolled / not connected | No protected overlay path | Enrollment / overlay state |

## Evidence standard

This portfolio uses screenshots/configuration evidence from the original project report as proof of deployment and testing, but does not republish screenshots containing historical secrets or sensitive infrastructure details.

## Production testing that would be added

- automated policy tests;
- TCP/service-level checks rather than relying only on ICMP;
- centralized logs for allow/deny decisions;
- endpoint posture validation;
- failure and peer-revocation tests;
- backup/restore validation for Nextcloud;
- container and host vulnerability scanning.
