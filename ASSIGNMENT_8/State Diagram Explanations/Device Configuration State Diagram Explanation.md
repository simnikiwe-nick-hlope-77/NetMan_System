### Diagram: Network Device Configuration Lifecycle

**Stakeholder:** Network Administrator

**Key States:**
- `Unconfigured`: Device has no settings.
- `BaselineConfigured`: Basic config applied.
- `Optimized`: Performance tuning complete.
- `Secured`: Security configurations applied (firewall, ACLs).
- `UnderAudit`: Configuration being reviewed.
- `Rollback`: Audit failed; settings reverted.
- `Retired`: Device removed.

**Stakeholder Concern Addressed:**
Network admins are tasked with ensuring **performance and security**. This workflow:
- Structures the **step-by-step config process**.
- Allows for **audits and automatic rollbacks** to avoid misconfigurations.
- Emphasizes the **balance between speed and security**.
- Logs progress from baseline to hardened state, enabling **continuous improvement**.

**Linked User Story:**
> *"As a network admin, I want to configure network devices for optimized performance and security."*
