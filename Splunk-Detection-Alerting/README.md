# Splunk - Brute Force Detection & Alerting

## Project Overview

Simulated a brute-force attack by intentionally failing SSH logins on a Linux VM. Captured authentication failures in Splunk, queried them with SPL, and built a scheduled alert notification for repeated failed login attempts.

This project gave me direct practice in:

- Log ingestion and parsing
- Writing SPL queries for detection
- Building dashboards for visibility
- Configuring scheduled alerts for suspicious activity

The workflow models what SOC analysts do in a professional environment when monitoring for brute force attacks.

---

## Steps Performed

1. Generated SSH login failures on a Linux VM
2. Forwarded authentication logs into Splunk
3. Wrote SPL queries to identify repeated failed logins
4. Created a dashboard panel to visualize the attempts
5. Configured an alert to trigger after threshold conditions

---

## Artifacts

- **Queries:** [`queries/`](./queries)
- **Dashboards:** [`dashboards/`](./dashboards)
- **Alert Example:** [`alerts/`](./alerts)

---

## Key Takeaways

- Reinforced how SIEMs like Splunk are used in detection engineering
- Practiced building queries that reduce false positives
- Demonstrated end-to-end workflow: log → query → dashboard → alert
