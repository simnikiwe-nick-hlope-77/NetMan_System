### Diagram: Network Traffic Monitoring Workflow

**Stakeholder:** Cybersecurity Officer

**Key States:**
- `Idle`: Not monitoring.
- `Monitoring`: Active inspection.
- `AnomalyDetected`: Suspicious activity flagged.
- `UnderInvestigation`: Human-in-the-loop review.
- `Escalated`: Confirmed threat.
- `Cleared`: False positive.
- `Offline`: System maintenance.

**Stakeholder Concern Addressed:**
Security officers need to **detect threats in real time** and **respond appropriately**. This workflow:
- Introduces a **clear path from detection to escalation**.
- Allows for **manual review**, reducing false positives.
- Supports **logging and resolution**, aligned with **incident response policies**.
- Reflects real-world tools like IDS/IPS or SIEM integration.

**Linked User Story:**
> *"As a Cybersecurity officer, I want to monitor network traffic so that I can detect unusual activity."*
