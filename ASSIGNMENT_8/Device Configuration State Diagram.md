### DEVICE CONFIGURATION STATE DIAGRAM
stateDiagram-v2
    [*] --> Unconfigured
    Unconfigured --> BaselineConfigured : Apply Default Config
    BaselineConfigured --> Optimized : Optimize for Performance
    Optimized --> Secured : Apply Security Policies
    BackupConfig --> Backups : Configurations Backed Up For Future Use
    MassConfig --> Ansible : Use Ansible For Mass Configuraion For All Devices
    Secured --> UnderAudit : Initiate Security Audit
    UnderAudit --> Secured : Audit Passed
    UnderAudit --> Rollback : Audit Failed
    Rollback --> Secured : Reapply Secured Config
    Secured --> Retired : Device Decommissioned