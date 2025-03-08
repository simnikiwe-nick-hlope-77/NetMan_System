Creating a network management software system involves defining several key functional requirements to ensure it meets the needs of users and administrators. Here are some essential functional requirements:

Fault Management: The system should detect, isolate, notify, and correct faults encountered in the network. This includes real-time monitoring and alerting for network issues.

Configuration Management: The system should manage the configuration of network devices, including configuration file management, inventory management, and software management.

Performance Management: The system should monitor and measure various aspects of network performance to maintain overall performance at an acceptable level. This includes performance monitoring, measurement, and reporting.

Security Management: The system should provide access control to network devices and corporate resources, ensuring that only authorized individuals can access them.

Accounting Management: The system should track the usage information of network resources, helping in resource allocation and billing.

User Interface: The system should have an intuitive and user-friendly interface for administrators to easily manage and monitor the network.

Scalability: The system should be scalable to accommodate the growth of the network and the addition of new devices and users.

Reliability and Availability: The system should ensure high availability and reliability, with minimal downtime and robust backup and recovery mechanisms.

These requirements will help in designing a comprehensive network management software system that meets the needs of users and administrators effectively.




# FUNCTIONAL REQUIREMENTS
### 1. Fault Management: 
The system should perform real-time detection, notification, and if possible correction of anomalies within the network infrastructure.
### 2. Configuration Management:
The system should be able to manage conifguration, including mass configuration of network devices, inventory management, and software management. The system should also be able to captutre logs and store backups of configuration files.
### 3. Performance Management:
The system should monitor, measure, and report certain aspects of network operations to maintain a high level of network performance.
### 4. Security Management:
Through the  RADIUS and TACACS security protocols, network engineers and administrators can enforce user validation and authentication before granting individuals access to the network devices. The network engineers should segment the network into different parts through the use of VLANs, manage access control via ACLs and traffic rules set by a firewall to prevent unauthorised access to the network. This will prevent the potential spread of malicious traffic throughout the network. The security team should conduct continuous monitoring and logging of network activities to help identify unusual patterns and prevent data breaches. In addition, intrusion detection and prevention systems should also be implemented, along with honeypots to direct threat actors away from sensitive data.
### 5. Accounting Management:
Through the aaa network security framework, authorized users and their actions should be tracked through logs, and their actions accounted for should there be any irregularities in system processes. Accounting management will also help in tracking resource usage information, determining resource allocation and billing for services.
### 6. User Interface:
The software's user interface should have a well-presented and easy-to-use interactive interface through which network administrators can control and monitor the network management system and its various components.
### 7. Scalability:
The network management software should be able to accommodate a continuously growing capacity of users and network devices without depreciating in system performance. Device on-boarding and auto-configuration should also be seamless through software-defined networking capabilities.
### 8. Reliability:
The system should prove to be reliable, with constant availability throughout its operation. There should be robust backup and recovery mechanisms in case of failure caused by either the software itself or even external factors.
