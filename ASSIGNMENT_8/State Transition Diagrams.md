### Network State Transition Diagram
```mermaid
stateDiagram-v2
[*] --> DeviceRegistered
DeviceRegistered --> DeviceActive : Recorded and Approved
DeviceActive --> Maintenance : Scheduled Maintenance
Maintenance --> DeviceActive : Operation Resumed
DeviceActive --> DeActivated : NetworkAdmin Deactivates Device
DeActivated --> DeviceReplaced : IT Operations Team Replaces Device
DeviceReplaced --> DeviceActive : ReActivated
DeviceUpgrade --> RetireDevice : Retired
