### Diagram: Encryption State Diagram (AES-256)

**Key States:**
- `Unencrypted`: Raw data stored without protection.
- `EncryptionPending`: Scheduled for AES-256 encryption.
- `Encrypted`: AES-256 applied.
- `Validated`: Encryption verified.
- `DecryptionRequested`: Temporary read access granted.
- `ReEncrypted`: Re-applied with new key (e.g., after key rotation).
- `AuditLogged`: Compliance log entry.
- `NonCompliant`: Data failed encryption or integrity checks.

**Stakeholder Concern Addressed:**
System administrators are responsible for **ensuring compliance with security policies** (e.g., GDPR, HIPAA). This workflow:
- Ensures **encryption is enforced by default**.
- **Logs every encryption event** for audit.
- Detects and flags **noncompliance** for fast mitigation.
- Supports **key rotation** and **temporary, auditable access**, covering both **performance** and **policy requirements**.

**Linked User Story:**
> *"As a system admin, I want to encrypt user data with AES-256 so that security compliance policies are upheld."*

