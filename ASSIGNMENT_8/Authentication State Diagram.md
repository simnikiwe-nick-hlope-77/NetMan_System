### USER LOGIN AUTHENTICATION STATE DIAGRAM
```mermaid
stateDiagram-v2
[*] --> Idle
Idle --> UsernameEntered : Enter Username
UsernameEntered --> EnterPassword : PasswordVerified
PasswordVerified --> AwaitingMFA : Trigger MFA
AwaitingMFA --> MFAConfirmed : OTP Verified
MFAConfirmed --> Authenticated : Grant Access
AwaitingMFA --> LoginFailed : MFA Failed
LoginFailed --> LockedOut : Too Many Failures
LoginFailed --> Idle : Retry Login