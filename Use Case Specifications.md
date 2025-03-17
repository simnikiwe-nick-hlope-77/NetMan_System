Here are the **8 critical use cases** from the **NetMan_System**, along with their detailed specifications.  

---

### **1. User Authentication**  
**Description:** Ensures only authorized users can access the system.  
**Preconditions:** User must have valid credentials stored in the database.  
**Postconditions:** User is granted or denied access.  
**Basic Flow:**  
1. User enters a username and password.  
2. System validates credentials.  
3. If valid, access is granted.  
4. If invalid, access is denied.  
**Alternative Flow:**  
- If multiple failed attempts occur, the account is locked.  

---

### **2. Monitor Network Traffic**  
**Description:** Allows administrators to track network activity and detect anomalies.  
**Preconditions:** Admin must be logged in.  
**Postconditions:** Network traffic data is displayed.  
**Basic Flow:**  
1. Admin opens the monitoring dashboard.  
2. System retrieves and displays live network data.  
3. Admin analyzes traffic patterns.  
**Alternative Flow:**  
- If data retrieval fails, an error message is displayed.  

---

### **3. Manage User Permissions**  
**Description:** Allows the administrator to modify user access rights.  
**Preconditions:** Admin must be logged in.  
**Postconditions:** User permissions are updated.  
**Basic Flow:**  
1. Admin selects a user from the list.  
2. Admin modifies access permissions.  
3. System updates and saves the new permissions.  
**Alternative Flow:**  
- If the user does not exist, an error is displayed.  

---

### **4. Configure Network Devices**  
**Description:** Enables administrators to set up and modify network devices.  
**Preconditions:** Admin must be logged in.  
**Postconditions:** Device configurations are saved and applied.  
**Basic Flow:**  
1. Admin selects a device to configure.  
2. Admin modifies settings (e.g., IP, firewall rules).  
3. System updates and applies changes.  
**Alternative Flow:**  
- If the device is offline, an error message appears.  

---

### **5. Generate Security Reports**  
**Description:** Creates reports based on network activity and security logs.  
**Preconditions:** Admin or Security Officer must be logged in.  
**Postconditions:** A report is generated and available for review.  
**Basic Flow:**  
1. Admin selects a report type (e.g., login history, firewall events).  
2. System compiles data from logs.  
3. System generates and displays the report.  
**Alternative Flow:**  
- If logs are unavailable, an error message appears.  

---

### **6. Detect Intrusions**  
**Description:** Identifies and reports unauthorized access attempts.  
**Preconditions:** The system must be actively monitoring network traffic.  
**Postconditions:** An intrusion is logged, and an alert is triggered.  
**Basic Flow:**  
1. System scans network activity for anomalies.  
2. If unusual behavior is detected, it flags the activity.  
3. System logs the event and notifies the administrator.  
**Alternative Flow:**  
- If no threats are detected, the system remains in monitoring mode.  

---

### **7. Backup & Restore Configurations**  
**Description:** Saves and restores network settings in case of failure.  
**Preconditions:** The system must be operational.  
**Postconditions:** Configurations are successfully saved or restored.  
**Basic Flow:**  
1. Admin selects **Backup** or **Restore** option.  
2. System processes the request.  
3. System confirms successful backup or restoration.  
**Alternative Flow:**  
- If backup data is corrupted, an error message appears.  

---

### **8. System Alerts & Notifications**  
**Description:** Sends real-time alerts about security threats and system failures.  
**Preconditions:** Monitoring system must be active.  
**Postconditions:** Alerts are sent to the administrator.  
**Basic Flow:**  
1. System detects a critical event (e.g., intrusion, device failure).  
2. System generates a notification.  
3. Admin receives and acknowledges the alert.  
**Alternative Flow:**  
- If notification service is down, alerts are logged but not sent.  

---
