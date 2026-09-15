# Sanitized Deployment Notes

These notes explain the deployment sequence at an architectural level. They intentionally omit original secrets, addresses, and account-specific values.

## 1. Prepare cloud/Linux nodes

- provision the required Linux instances;
- apply OS updates;
- configure cloud firewall/security-group rules conservatively;
- avoid exposing the collaboration service broadly unless required for setup.

## 2. Deploy the collaboration service

- install Docker/Compose;
- deploy Nextcloud and its backing database/storage configuration;
- create application users/groups/shares appropriate to the collaboration scenario.

A generic example is provided in [../examples/docker-compose.nextcloud.example.yml](../examples/docker-compose.nextcloud.example.yml).

## 3. Enroll peers into NetBird

- install the NetBird client/agent as appropriate;
- enroll each intended peer using securely handled setup material;
- verify peer status;
- remove or rotate setup material after use where applicable.

## 4. Define network policy

- organize peers into meaningful groups;
- define required source/destination paths;
- avoid unnecessary all-to-all reachability;
- document why each allow rule exists.

## 5. Validate

- test expected allowed paths;
- test expected denied paths;
- test Nextcloud login/share permissions separately;
- capture sanitized results.

## Production hardening

For production, add infrastructure-as-code, secret management, centralized logging, monitoring, backups, TLS lifecycle, automated policy tests, host hardening, container scanning, and formal incident-response procedures.
