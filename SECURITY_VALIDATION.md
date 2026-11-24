# Security validation

## Scope

Configured GitHub security checks and remediated identified
problems in the fictional YAML report importer.

## Changes

- Replaced unsafe YAML loading with yaml.safe_load.
- Updated PyYAML from 5.3.1 to 6.0.3.
- Added report schema and status validation.
- Added a 16 KiB request limit.
- Added nine regression tests.
- Configured weekly dependency and Actions updates.

## Functional and input checks

| Check | Expected | Result |
| --- | --- | --- |
| Valid healthy report | HTTP 200 and correct JSON | Passed |
| Valid degraded report | HTTP 200 | Passed |
| Unknown status | HTTP 400 | Passed |
| Blank service | HTTP 400 | Passed |
| List instead of mapping | HTTP 400 | Passed |
| Malformed YAML | HTTP 400 | Passed |
| Python object tag | HTTP 400 | Passed |
| Missing field | HTTP 400 | Passed |
| Oversized request | HTTP 413 | Passed |

## GitHub checks

- All nine regression tests passed on the merged main branch.
- CodeQL completed successfully on the merged main branch.
- The original unsafe-deserialization alert was marked fixed.
- The original PyYAML dependency advisory was marked fixed.
- Dependency alerts and security updates are enabled.
- Secret scanning and available push protection are enabled.

## Limitations

The repository is a training sample with fictional information.
No public application was deployed.
No real credentials were added to test secret scanning.

These checks address specific findings and input behaviour.
They do not establish that the application is free of all vulnerabilities.
