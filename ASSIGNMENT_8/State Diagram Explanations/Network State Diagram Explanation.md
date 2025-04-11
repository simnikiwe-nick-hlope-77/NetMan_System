### Diagram: Network Device State Lifecycle

**Stakeholder:** Network Administrator

**Key States:**
- `Registered`: The device has been entered into the system (e.g., MAC, IP, type).
- `Approved`: An admin or system has verified the device for use.
- `Active`: Device is live on the network and functioning.
- `UnderMaintenance`: Temporarily taken offline for updates or fixes.
- `Deactivated`: Access to the network is revoked by admin (temporarily).
- `Retired`: Permanently removed from service (end-of-life or replacement).

**Transitions:**
- Devices are registered, then approved before activation.
- Admins can manually deactivate/reactivate devices.
- Scheduled or emergency maintenance leads to `UnderMaintenance`.
- Any device can eventually be `Retired`, regardless of current state.

**Stakeholder Concern Addressed:**
Network admins need to **track and manage device states** for performance, availability, and security. This workflow ensures:
- Devices must go through **approval and activation** steps before use.
- There are clearly defined states for **maintenance** and **decommissioning**.
- Admins can **deactivate** or **retire** devices based on status or policy.
- The system supports a **lifecycle-aware approach**, helping prevent unauthorized or outdated device usage.

**Enhancements Included:**
- A transition from `Approved → Retired` is allowed, representing devices approved but **decommissioned before use**.
- Re-entry into `Active` is possible after both maintenance and deactivation, enabling **flexibility** in managing live infrastructure.

**Linked User Story:**
> *"As a network admin, I want to register, approve, and manage devices across their lifecycle so that I can ensure operational stability and compliance."*

**Functional Requirement Example:**
- **FR-002:** The system shall allow admins to register, activate, deactivate, and retire network devices, maintaining a complete lifecycle history.
