### ACTIVE DIRECTORY STATE DIAGRAM
```mermaid
[*] --> UserCreated
UserCreated --> AdminPrivileges : Network Admin Role Assigned
UserCreated --> Cybersecurity : Cybersecurity Privilege Role Assigned
UserCreated --> ITOps : IT Operations Role Assigned
UserCreated --> SystemArchitect : System Architect Role Assigned
UserCreated --> Developer : Software Developer Role Assigned
UserCreated --> ViewOnly : Project Manager Role Assigned