# Access Control

## Two different authorization problems

One of the most important engineering distinctions in this project is that **network access control and file/application authorization are not the same control**.

### NetBird policy

NetBird controls whether a source peer/group can reach a destination peer/resource over specified network paths or services.

Conceptually:

```text
Source peer/group
      |
      v
NetBird policy decision
      |
      +---- deny ---> no network path
      |
      +---- allow --> destination service
```

### Nextcloud permissions

After the network path exists, Nextcloud still decides whether the authenticated user may access, upload, download, or share application data.

```text
Reachable Nextcloud
      |
      v
Application login
      |
      v
User/group/share permission
      |
      +---- deny ---> no data access
      +---- allow --> authorized data
```

## Why the distinction matters

A statement such as "NetBird allows access to `/files/design/`" would overstate what a network policy does. NetBird can restrict reachability to the service/peer/port. Nextcloud owns authorization for folders and shared objects.

This repository preserves that separation so the portfolio reflects the actual control boundaries.

## Policy-design approach

A sensible project policy model is:

1. Define peers and groups based on collaboration needs.
2. Permit only required source-to-destination paths.
3. Avoid broad all-to-all policies unless justified by the lab scenario.
4. Use Nextcloud roles/groups/shares for content authorization.
5. Test both expected success and expected denial.

See [examples/netbird-policy.example.md](examples/netbird-policy.example.md) for a sanitized conceptual example. It is illustrative rather than an export of the original environment.
