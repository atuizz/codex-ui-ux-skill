# Security Policy

## Supported versions

This project currently supports the latest version on the main branch.

## Reporting a vulnerability

If you find a security issue, please open a private security advisory if the
hosting platform supports it. If not, contact the maintainers through the
project's published maintainer channel.

Please include:

- affected files or instructions;
- a short reproduction or example;
- impact and likely severity;
- any safe remediation suggestion.

## Security expectations for this skill

Do not contribute:

- secrets, tokens, credentials, private URLs, or sensitive identifiers;
- prompts or scripts that encourage data exfiltration or unauthorized access;
- organization-specific examples that expose internal systems or customers;
- hidden network calls or unexpected filesystem writes.

Helper scripts should be deterministic, local, and unsurprising. If a script
needs to write files, it should write only to an explicitly requested project
path or a temporary directory.
