# SafeHands Insurance Brokers
# Weekly SOC Report

Project: SOC Analyst Starter Project  
Prepared By: Mubashir Ahmad  
Reporting Period: Project Tasks 1–3  

---

## 1. Executive Summary

During this project, 20 sample SOC alerts were collected and normalized into a consistent JSON format for easier security analysis.

The normalized alerts were then mapped to relevant MITRE ATT&CK techniques. Based on the findings, a Sigma detection rule was created and tested to demonstrate how suspicious activity could be detected using a standardized detection format.

---

## 2. Key Findings

- 20 sample security alerts were processed.
- Raw alert data was converted into a consistent JSON structure.
- Alerts were mapped to MITRE ATT&CK techniques.
- The mappings were documented in `mitre_mapping.csv`.
- A Sigma detection rule was created for the selected technique.
- The Sigma rule was tested and conversion evidence was collected.
- Standardized alert data made the investigation and detection process easier to manage.

---

## 3. Detection and Analysis

The SOC workflow used during the project was:

Raw Logs → Normalized Alerts → MITRE ATT&CK Mapping → Sigma Detection Rule → Triage

The normalized alert data is stored in:

`alerts.json`

The MITRE ATT&CK mappings are stored in:

`mitre_mapping.csv`

The detection rule and supporting files are stored in:

`sigma/`

---

## 4. Actions Taken

During the project, the following actions were completed:

- Collected 20 sample SOC log files.
- Created a Python script to process the logs.
- Normalized the alerts into JSON format.
- Reviewed the normalized security events.
- Mapped alerts to MITRE ATT&CK techniques.
- Created a MITRE ATT&CK mapping CSV.
- Identified a technique for detection.
- Created a Sigma detection rule.
- Tested the Sigma rule.
- Saved evidence of the detection-rule conversion.

---

## 5. SOC Metrics

| Metric | Result |
|--------|--------|
| Sample Alerts Processed | 20 |
| Normalized Alert File | alerts.json |
| MITRE Mapping | Completed |
| Sigma Detection Rule | Created |
| Sigma Rule Testing | Completed |
| Triage Playbook | Completed |

---

## 6. Recommendations

- Continue collecting additional security logs from different systems.
- Create additional Sigma rules for other MITRE ATT&CK techniques.
- Review detection rules regularly to reduce false positives.
- Investigate high-severity alerts using the SOC triage playbook.
- Maintain documentation so future SOC analysts can understand the detection process.

---

## 7. Conclusion

The project established a basic SOC workflow for SafeHands Insurance Brokers. Alerts can now be normalized, mapped to MITRE ATT&CK, analyzed using a Sigma detection rule, and investigated using a documented triage process.

This provides a simple foundation that a future SOC team can expand as the organization's security monitoring capabilities grow.