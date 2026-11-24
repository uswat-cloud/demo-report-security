# Demo Report Security

A training application for reviewing GitHub security findings
and validating a YAML report importer.

## Input

POST /report accepts YAML containing exactly:

service: Demo Portal
status: healthy

Allowed statuses are healthy, degraded and unavailable.

## Input protections

- Safe YAML loading.
- Required service and status fields.
- Nonblank string service name.
- Restricted status values.
- Invalid input returns HTTP 400.
- Requests larger than 16 KiB return HTTP 413.

## Tests

Install dependencies:

python -m pip install -r requirements.txt

Run tests:

python -m unittest discover -v

Tests use Flask's test client.
No public server deployment is needed.

## Repository controls

- CodeQL code scanning.
- Dependabot vulnerability alerts.
- Weekly dependency and GitHub Actions update checks.
- Available secret scanning and push protection.

## Scope

All data is fictional.
The original baseline was deliberately vulnerable.

The changes address identified YAML-loading and dependency problems.
Passing tests and scans are not a complete security audit.
