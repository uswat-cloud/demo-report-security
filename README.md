# Demo Report Security

A deliberately vulnerable training sample for practising
GitHub security scanning and remediation.

## Starting behaviour

The application accepts YAML at POST /report and returns JSON.

## Sample input

service: Demo Portal
status: healthy

## Exercise scope

- Configure dependency alerts.
- Configure code scanning.
- Enable available secret protection.
- Investigate actual findings.
- Fix confirmed problems.
- Add regression tests and verify the changes.

All information is fictional.
Do not deploy the vulnerable baseline as a public service.
Do not add real credentials or customer information.
