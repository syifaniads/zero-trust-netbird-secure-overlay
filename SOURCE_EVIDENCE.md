# Source Evidence

## Purpose

This file documents how claims in this public portfolio are classified. The goal is to keep the repository recruiter-friendly **without converting report text into unsupported claims**.

## Evidence hierarchy

### Strong implementation evidence

The original final project material includes screenshots or concrete configuration/testing evidence for:

- NetBird peer configuration/status;
- multiple participating nodes;
- NetBird policies/access-control setup;
- Dockerized Nextcloud deployment;
- Nextcloud accounts/folders/sharing scenarios;
- cloud/Linux environment;
- peer connectivity tests.

These are treated as the core verified portfolio story.

### Report-described evidence

The report describes an authentication/JWT component. Because the surviving source-level evidence used for this portfolio is weaker than the evidence for the overlay and Nextcloud implementation, this repository does not elevate that component to the same verification level.

### Conflicting / insufficient evidence

The report also contains references to Ryu Controller, SDN, and VNF while other report sections define a scope centered on NetBird/JWT/Nextcloud and exclude SDN/Ryu. Those claims are therefore not presented as verified implementation in this portfolio.

See [docs/REPORT_CONSISTENCY_NOTES.md](docs/REPORT_CONSISTENCY_NOTES.md).

## Why the original report is not committed here

The original material contains environment-specific information that should not be republished casually, including historical credentials and other sensitive deployment details. Rather than upload the raw report, this repository contains sanitized technical summaries.

See [docs/REPORT_REDACTION_NOTICE.md](docs/REPORT_REDACTION_NOTICE.md).

## Leadership evidence

The portfolio owner has identified their role in this project as **Group Lead (Ketua Kelompok)** and technical contributor. This repository states that role explicitly while keeping implementation-level claims collaborative unless individual authorship can be independently established.

## Verification philosophy

A reviewer should be able to distinguish among:

- **implemented and evidenced**;
- **described in project documentation**;
- **not claimed because evidence is conflicting or incomplete**.

That distinction is intentional and is part of the security-engineering quality of this portfolio reconstruction.
