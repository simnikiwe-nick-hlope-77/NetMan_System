### CYBERSECURITY STATE DIAGRAM
```mermaid
stateDiagram-v2
[*] --> Idle
    Idle --> Monitoring : Enable Monitoring
    Monitoring --> AnomalyDetected : Unusual Pattern Detected
    AnomalyDetected --> UnderInvestigation : Security Officer Reviews
    UnderInvestigation --> Escalated : Threat Confirmed
    UnderInvestigation --> Cleared : False Positive
    Escalated --> Monitoring : Response Complete
    Cleared --> Monitoring : Resume Monitoring
    Monitoring --> Offline : System Maintenance
    Offline --> Idle : Restart Monitoring Engine