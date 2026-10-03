# SOC Analyst Starter Project - SafeHands Insurance Brokers

[![Live Demo](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen)](https://mubashirkz.github.io/SOC-Starter/)

## Project Overview

This project is a SOC Analyst Starter Project created for SafeHands Insurance Brokers.

The goal is to build a simple and documented SOC workflow that can collect and normalize security alerts, map them to MITRE ATT&CK techniques, detect suspicious activity using Sigma rules, and provide a clear triage and hand-over process for a future SOC team.

---

## SOC Workflow

**Sample Logs → Alert Normalization → MITRE ATT&CK Mapping → Sigma Detection → Alert Triage → SOC Reporting**

---

## Task 1 - Alert Collection and Normalization

Collected 20 sample SOC log files and processed them using a Python script.

The alerts were converted into a consistent JSON format to make security analysis easier.

### Files

- [logs/](./logs/) - Contains the sample SOC log files.
- [parse_alerts.py](./parse_alerts.py) - Python script used to normalize the logs.
- [alerts.json](./alerts.json) - Normalized security alerts.
- [requirements.txt](./requirements.txt) - Project dependency information.

---

## Task 2 - MITRE ATT&CK Mapping

The normalized alerts were reviewed and mapped to relevant MITRE ATT&CK techniques.

This helps SOC analysts understand the attacker behavior represented by each security alert.

### File

- [mitre_mapping.csv](./mitre_mapping.csv) - Contains the MITRE ATT&CK mappings for the normalized alerts.

---

## Task 3 - Sigma Detection Rule

A Sigma detection rule was created for the selected technique identified during the analysis.

The rule was tested and conversion evidence was collected to demonstrate that the detection logic could be converted for use with a security monitoring platform.

### Files

- [sigma/](./sigma/) - Contains the Sigma detection rule and supporting files.

---

## Task 4 - SOC Hand-Over Package

The final task packages the SOC work into documentation that can be handed over to a future security team.

The hand-over includes a triage playbook, SOC report, project documentation, and a live GitHub Pages site.

### Files

- [PLAYBOOK.md](./PLAYBOOK.md) - Step-by-step SOC alert triage process.
- [SOC_Report_Template.md](./SOC_Report_Template.md) - SOC findings, actions, metrics, and recommendations.
- [HANDOVER.md](./HANDOVER.md) - Final hand-over documentation and links to project artifacts.

---

## Project Deliverables

| Deliverable | Status |
|---|---|
| Alert Normalization Script | Completed |
| Normalized Alerts | Completed |
| MITRE ATT&CK Mapping | Completed |
| Sigma Detection Rule | Completed |
| Sigma Rule Testing | Completed |
| SOC Triage Playbook | Completed |
| SOC Report | Completed |
| Hand-Over Documentation | Completed |
| GitHub Pages Site | Live |

---

## Live Project Site

The project documentation is published using GitHub Pages.

Live Site:  
https://mubashirkz.github.io/SOC-Starter/

---

## Tools and Technologies

- Python
- JSON
- CSV
- MITRE ATT&CK
- Sigma
- Markdown
- Git
- GitHub
- GitHub Pages
- Visual Studio Code

---

## Key Skills Demonstrated

- SOC alert analysis
- Log normalization
- MITRE ATT&CK mapping
- Detection engineering basics
- Sigma rule creation
- Alert triage
- Security documentation
- Git and GitHub
- SOC reporting

---

## Hand-Over

For the complete project hand-over and access to all deliverables, see:

[HANDOVER.md](./HANDOVER.md)

---

## Author

Mubashir Ahmad  
Cyber Security Intern