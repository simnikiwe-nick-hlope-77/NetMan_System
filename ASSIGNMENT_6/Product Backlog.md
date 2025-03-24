# Product Backlog for NetMan_Sys

| **Story ID** | **User Story** | **Priority (MoSCoW)** | **Effort Estimate (Story Points)** | **Dependencies** |
|-------------|-----------------------------------------------------------------|------------------|----------------------------|----------------|
| **US-001** | As a network admin, I want to monitor real-time device health status so that I can detect network failures early. | **Must-have** | 5 | None |
| **US-002** | As a system admin, I want 2-factor authentication for network device access, as well as for SNMP polling for checking device health status | **Must-have** | 3 | None |
| **US-003** | As a network technician/standby techincian, I want to receive alerts when a device goes down so that I can take immediate action. | **Must-have** | 4 | US-001 |
| **US-004** | As a network admin, I want to receive auto-generated network performance reports so that I can analyze trends. | **Should-have** | 5 | US-001 |
| **US-005** | As a network technician, I want to remotely restart malfunctioning devices so that I can fix issues faster. | **Should-have** | 3 | US-001 |
| **US-006** | As a system admin, I want a dashboard with system-wide analytics so that I can monitor performance easily. | **Could-have** | 5 | US-001, US-004 |
| **US-007** | As a cybersecurity analyst, I want all logs encrypted using AES-256 so that data integrity is maintained. I also want specialized privilege access that only the cybersecurity team has to those logs. | **Must-have** | 2 | None |
| **US-008** | As a network admin, I want a role-based access control system so that only authorized users can manage devices. | **Must-have** | 4 | US-002 |

---
# Justification for Prioritization in NetMan_Sys  

| **Story ID** | **User Story** | **Justification** |
|-------------|-----------------------------------------------------------------|------------------------------------------------|
| **US-001** | Monitor real-time device status | *Essential for network visibility; without this, admins cannot detect failures.* |
| **US-002** | Multi-user authentication | *Security-critical; ensures only authorized users can access NetMan_Sys.* |
| **US-003** | Alert notifications for offline devices | *Prevents downtime; admins must be notified of failures in real time.* |
| **US-007** | Encrypt system logs using AES-256 | *Ensures data integrity and compliance with security standards.* |
| **US-008** | Role-based access control | *Prevents unauthorized changes by restricting permissions to specific roles.* |

---

## **Should-Have User Stories (Important but Not Urgent for MVP)**  

| **Story ID** | **User Story** | **Justification** |
|-------------|-----------------------------------------------------------------|------------------------------------------------|
| **US-004** | Generate network performance reports | *Valuable for long-term analysis but not required for real-time monitoring.* |
| **US-005** | Remotely restart malfunctioning devices | *Improves efficiency but can be handled manually in early versions.* |

---

## **Could-Have User Stories (Enhancements for Future Sprints)** 

| **Story ID** | **User Story** | **Justification** |
|-------------|-----------------------------------------------------------------|------------------------------------------------|
| **US-006** | Dashboard with system-wide analytics | *Helpful for advanced monitoring but not required for core operations.* |

---
