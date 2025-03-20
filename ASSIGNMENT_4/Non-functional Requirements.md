# Non-Functional Requirements for NetMan_System  

## **1. Usability**  
- **Requirement:** The interface shall comply with **WCAG 2.1 Level AA** accessibility standards to ensure usability for all users, including those with disabilities.  
- **Requirement:** The system shall provide an **intuitive dashboard** with a clean UI, ensuring users can perform key tasks in **three clicks or less**.  
- **Requirement:** All user actions shall have **real-time feedback** (e.g., success/failure messages) to improve usability and reduce errors.  

## **2. Deployability**  
- **Requirement:** The system shall be deployable on **Windows Server 2019+, Linux (Ubuntu 20.04+ and CentOS 8+)** environments.  
- **Requirement:** The system shall support **containerized deployment using Docker** for ease of scalability and portability.  

## **3. Maintainability**  
- **Requirement:** The system documentation shall include **detailed API references** and **developer guides** for future integrations.  
- **Requirement:** The system shall support **modular architecture**, allowing independent updates to components without affecting overall functionality.  

## **4. Scalability**  
- **Requirement:** The system shall support **1,000 concurrent users** during peak hours without performance degradation.  
- **Requirement:** The system shall be able to handle **network traffic monitoring for up to 10,000 devices** simultaneously.  
- **Requirement:** The database shall be designed to **scale horizontally**, ensuring efficient handling of increasing data loads.  

## **5. Security**  
- **Requirement:** All user data shall be **encrypted using AES-256** both at rest and in transit.  
- **Requirement:** The system shall enforce **multi-factor authentication (MFA)** for all administrative users.  
- **Requirement:** All access logs shall be stored securely and retained for **at least 12 months** for audit purposes.  
- **Requirement:** User sessions shall automatically **expire after 15 minutes of inactivity** to prevent unauthorized access.  

## **6. Performance**  
- **Requirement:** The system shall **load the dashboard within 3 seconds** under normal network conditions.  
- **Requirement:** Search queries for network devices shall return results **within 2 seconds** for datasets of up to 100,000 records.  
- **Requirement:** The system shall process and **display real-time network monitoring data with a refresh rate of at least once every 5 seconds**.  
