### ACTIVE DIRECTORY STATE DIAGRAM
```mermaid
stateDiagram-v2
[*] --> UserCreated
UserCreated --> AdminPrivileges : Network Admin Role Assigned
UserCreated --> Cybersecurity : Cybersecurity Privilege Role Assigned
UserCreated --> ITOps : IT Operations Role Assigned
UserCreated --> SystemArchitect : System Architect Role Assigned
UserCreated --> Developer : Software Developer Role Assigned
UserCreated --> ViewOnly : Project Manager Role Assigned

AdminPrivileges --> Suspended : Manual Suspension
Cybersecurity --> Quarantined : Suspicious Activity Detected
ITOps --> PendingReview : Privileged Access Request
OpsPrivilege --> TempPrivilege : Temporary Access Granted
SystemArchitect --> DesignSubmission : Submit Architecture Plan
DesignSubmission --> UnderReview : Awaiting Design Approval
Developers --> CodeSubmitted : Submit Code for Approval
CodeSubmitted --> UnderReview : Awaiting Approval