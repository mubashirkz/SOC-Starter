# SafeHands SOC Triage Playbook

## Purpose

This playbook provides a simple process for SOC analysts to investigate and respond to alerts detected by the Sigma rule created for the SafeHands Insurance Brokers SOC project.

## Triage Steps

### 1. Review the Alert
- Check the alert timestamp.
- Identify the affected host and user.
- Review the event that triggered the detection.
- Confirm which Sigma rule generated the alert.

### 2. Validate the Activity
- Review related logs around the alert time.
- Check whether the activity is expected or authorized.
- Look for repeated or similar alerts.
- Identify any suspicious source IP, process, account, or command.

### 3. Determine Severity

Low: Activity appears legitimate with little security risk.

Medium: Suspicious activity that requires further investigation.

High: Strong evidence of malicious activity or possible compromise.

### 4. Investigate
- Search for additional events involving the same user or host.
- Check for related suspicious activity.
- Review the MITRE ATT&CK technique mapped to the alert.
- Record relevant evidence and findings.

### 5. Containment
If malicious activity is confirmed:
- Isolate the affected system if necessary.
- Disable or secure compromised accounts.
- Block malicious indicators when appropriate.
- Preserve relevant logs and evidence.

### 6. Escalation

Escalate confirmed or high-severity incidents to:

- SOC Analyst / Security Team
- IT Administrator
- SOC Manager or Incident Response Lead

Critical incidents should be escalated immediately.

### 7. Documentation and Closure
- Record the alert and investigation results.
- Document actions taken.
- Record whether the alert was a true positive or false positive.
- Add lessons learned if necessary.
- Close the alert only after investigation is complete.

## Evidence to Record

For every investigated alert, record:

- Alert ID
- Date and time
- Affected user/host
- Source IP (if available)
- MITRE ATT&CK technique
- Severity
- Investigation findings
- Actions taken
- Final status