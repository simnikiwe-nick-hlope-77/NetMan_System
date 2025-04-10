### USER LOGIN AUTHENTICATION STATE DIAGRAM
```mermaid
AuthenticationStateDiagram-v2
[*] --> Idle
Idle --> UsernameEntered : Enter Username
UsernameEntered --> EnterPassword : PasswordVerified
PasswordVerified --> LoginSuccess : CorrectPassword
LoginSuccess --> AwaitMFA : Trigger MFA
AwaitMFA --> MFAConfirmed : OTP Verified