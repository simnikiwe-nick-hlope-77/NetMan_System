### DEVICE CONFIGURATION STATE DIAGRAM
```mermaid
stateDiagram-v2
    [*] --> Unconfigured
    Unconfigured --> BaselineConfigured : Apply Default Config
    BaselineConfigured --> Optimized : Optimize for Performance
    BaselineConfigured--> BackupConfig : Configurations Backed Up For Future Use
    BaselineConfigured --> MassConfig : Use Ansible For Mass Configuraion For All Devices
    Optimized --> Secured : Apply Security Policies
    Secured --> UnderAudit : Initiate Security Audit
    UnderAudit --> Secured : Audit Passed
    UnderAudit --> Rollback : Audit Failed
    Rollback --> Secured : Reapply Secured Config
    Secured --> Retired : Device Decommissioned