### Diagram: User Profile Management

**Stakeholder:** Network Administrator

**Key States:**
- `Created`: A new user profile has been initialized in the system.
- `PendingActivation`: The user must confirm their email or complete onboarding.
- `Active`: The user has full access based on their assigned role.
- `Suspended`: Temporarily disabled due to inactivity, policy violation, or security concern.
- `Deactivated`: Manually deactivated.
- `Archived`: User is offboarded or has left the organization — account locked but audit trail retained.
- `Deleted`: All data and logs associated with the user are permanently removed.

**Transitions:**
- User transitions from `Created` to `PendingActivation` upon admin setup.
- Upon verification, the user becomes `Active`.
- Users may be temporarily `Suspended` or `Deactivated`, and reactivated later.
- Eventually, user accounts move to `Archived`, then optionally to `Deleted`.

**Stakeholder Concern Addressed:**
Network administrators need to **track and control user account status** over time to:
- Ensure **proper onboarding and offboarding**.
- Respond quickly to **policy violations or role changes**.
- Retain user records for **audit/compliance** even after users leave.
- Fully delete accounts in line with **data retention laws**.

**Security Implications:**
- Supports **least privilege** and **access lifecycle management**.
- Prevents orphaned accounts or active users bypassing security processes.
- Allows for a **traceable suspension/reactivation path** in sensitive environments.

**Linked User Story:**
> *"As a network admin, I want to create and manage user profiles so that I can control access and maintain account integrity like Active Directory."*

**Functional Requirement Example:**
- **FR-006:** The system shall allow authorized admins to create, activate, suspend, deactivate, archive, and delete user accounts with full traceability.
