### USE CASE DIAGRAM & ACTORS
![Use case diagram](https://github.com/user-attachments/assets/28643b43-8546-4e9c-ab7c-2a3694ce3597)

### Actors and Use cases
- Network Administrator: oversees configurations, rights, and authentication.
- System User: After being authenticated, this person gains access to the system.
- Cybersecurity team: keep an eye on network activity and any dangers.
- Monitoring System: Notifies users of problems automatically.
- Database: Holds configurations, logs, and authentication credentials.

In the **NetMan_System**, the **Network Administrator** plays a crucial role by managing **user authentication**, **permissions**, **network configurations**, and **security reports**. The administrator must first log in (**User Authentication**) before accessing features like **Manage User Permissions**, which allows them to assign or revoke user access, and **Configure Network Devices**, which enables them to set up routers and firewalls. The **Security Officer** is responsible for monitoring network activity through **Monitor Network Traffic** and identifying unauthorized access attempts via **Detect Intrusions**. Additionally, they can generate **Security Reports** to track system vulnerabilities and security events.  

The **System User**, on the other hand, only interacts with **User Authentication**, as they need to log in before using network services. The **Monitoring System** operates automatically, assisting the **Security Officer** by continuously scanning for security threats (**Detect Intrusions**) and triggering **System Alerts & Notifications** when issues are detected. The **Database** supports multiple use cases by storing user credentials for **User Authentication**, logs for **Generate Security Reports**, and system configurations for **Backup & Restore Configurations**.  

Finally, the **External Attacker** attempts to exploit vulnerabilities in the system, which triggers **Detect Intrusions** and **System Alerts & Notifications** to inform administrators of potential threats. The relationships between these use cases follow UML standards, with **inclusion relationships** (e.g., **User Authentication** includes **Validate Credentials**) ensuring critical processes are always executed, and **extension relationships** (e.g., **System Alerts & Notifications** extends **Detect Intrusions**) enabling additional actions when specific conditions are met. These relationships define how different actors interact with the system to maintain network security and ensure efficient management.

The **use case diagram** for **NetMan_System** addresses stakeholder concerns by ensuring **secure access control** through **User Authentication** and **Manage User Permissions**, while **Monitor Network Traffic** and **Detect Intrusions** enhance security by providing real-time threat detection. **Backup & Restore Configurations** ensures data integrity, and **Generate Security Reports** supports compliance needs. These use cases align with stakeholder expectations by visually mapping out how security and network management are effectively handled.
