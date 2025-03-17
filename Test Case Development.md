Here's the **Test Case Table** for the **NetMan_System**, including **8 functional test cases** and **2 non-functional test cases** (performance and security).  

---

### **Test Case Table**  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |  
|---------------|----------------|----------------|-----------|------------------|----------------|-----------------|  
| TC-001 | FR-001 | User Authentication | 1. Enter valid credentials <br> 2. Click Login | User is logged in successfully | | |  
| TC-002 | FR-002 | Failed Authentication | 1. Enter incorrect password <br> 2. Click Login | Login attempt is denied and an error message appears | | |  
| TC-003 | FR-003 | Monitor Network Traffic | 1. Open admin dashboard <br> 2. Click on "View Traffic" | Live network traffic data is displayed | | |  
| TC-004 | FR-004 | Detect Intrusions | 1. Simulate unauthorized access <br> 2. Check system logs | System detects and logs intrusion attempt | | |  
| TC-005 | FR-005 | Manage User Permissions | 1. Select a user <br> 2. Modify permissions <br> 3. Save changes | User permissions update successfully | | |  
| TC-006 | FR-006 | Configure Network Devices | 1. Select a network device <br> 2. Modify settings <br> 3. Save changes | Device configuration updates successfully | | |  
| TC-007 | FR-007 | Generate Security Reports | 1. Click on "Generate Report" <br> 2. Select report type <br> 3. View/download report | Security report is generated successfully | | |  
| TC-008 | FR-008 | System Alerts & Notifications | 1. Simulate a security event <br> 2. Check notification system | Alert is triggered and sent to the administrator | | |  

---

### **Non-Functional Test Cases**  

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |  
|---------------|----------------|----------------|-----------|------------------|----------------|-----------------|  
| TC-009 | NFR-001 | **Performance Test: User Login Speed** | 1. Simulate 500 users logging in simultaneously <br> 2. Measure response time | Login requests are processed within **2 seconds** | | |  
| TC-010 | NFR-002 | **Security Test: SQL Injection Prevention** | 1. Attempt SQL injection in login field <br> 2. Monitor system response | System blocks malicious input and logs the attempt | | |  

---
