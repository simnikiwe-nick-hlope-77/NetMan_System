
### Diagram: User Login with Multifactor Authentication (MFA)

**Stakeholder:** Network Administrator, Cybersecurity Officer

**Key States:**
- `Idle`: No login session has been initiated.
- `UsernameEntered`: The user has entered their login ID/username.
- `PasswordVerified`: The system has validated the password.
- `AwaitingMFA`: MFA token or push notification has been sent.
- `MFAConfirmed`: The second factor has been successfully validated.
- `Authenticated`: The user has successfully logged in and gained access.
- `LoginFailed`: Incorrect credentials or MFA failure.
- `LockedOut`: User has exceeded allowed login attempts and is locked out.

**Transitions:**
- The login process starts from `Idle`, requiring username and password entry.
- Once the password is verified, the system sends an MFA request.
- If the user passes MFA, they transition to `Authenticated`.
- Any failure in the process leads to `LoginFailed`.
- Repeated failures result in `LockedOut`, where admin intervention may be required.

**Stakeholder Concern Addressed:**
This diagram addresses **access control** and **secure login enforcement**, particularly for privileged users (e.g., admins, engineers). It ensures:
- **Layered security** through password + MFA.
- **Lockout mechanisms** to prevent brute force attacks.
- Clear state transitions that support **security monitoring** and **audit logging**.

**Compliance Alignment:**
- Helps meet industry standards like **NIST 800-63**, **ISO 27001**, or **GDPR**, which require **strong authentication** and **account protection**.

**Linked User Story:**
> *"As a network admin, I want to securely log in with multifactor authentication so that I can prevent unauthorized access to sensitive network controls."*

**Functional Requirement Example:**
- **FR-004:** The system shall require multifactor authentication for all privileged users and enforce account lockout after consecutive failed login attempts.
