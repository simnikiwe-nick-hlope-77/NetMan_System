# C4 Architectural Diagram
The C4 diagram was created [Mermaid](https://mermaid-js.github.io/mermaid-live-editor//edit#pako:eNpVjsFqw0AMRH9F6NRC_AM-FBq7zSWQQnOqnYOwZe-S7GqR14Rg-9-7TlpodZJm3gyasJGWMcfuItfGkEY4lrWHNK9VYdQO0dFwgix7mXccwYnn2wzbp53AYCQE6_vnB79dISim_YoxRGP9eXlYxT1_8DxDWe0pRAmnv87xKjO8VfbDpPr_jlFOqfeqo7yjrCGFgvSO4AYdqyPbpvenVakxGnZcY57WlvRcY-2XxNEY5fPmG8yjjrxBlbE3mAovQ7rG0FLk0lKv5H6RQP5LxP1AyzeJDl_b) and its online editor

```mermaid
graph TD;
  subgraph Admin["👨‍💻 Network Operations"]
    A["🖥️ Network Admin"]
  end

  subgraph NMS["📊 NetMan_System"]
    B(("Dashboard"))
    C["📩 Email Notifications"]
    D["☁️ Cloud Monitoring"]
  end

  subgraph Config["🛠️ Auto-Configuration"]
    E["Ansible/SolarWinds NCM"]
    F["📡 Routers & Switches"]
    G["💾 Configuration Backup"]
  end

  A -->|Monitors & Configures| B
  B -->|Sends Alerts| C
  B -->|Sends Performance Data| D
  B -->|Pushes Configs| E
  E -->|Deploys| F
  E -->|Backs Up| G

   %% Apply Styles for Better Readability
  style A fill:#FF8C00,stroke:#5A3D00,stroke-width:2px,color:#000;
  style B fill:#008080,stroke:#005F5F,stroke-width:3px,color:#FFF;
  style C fill:#FFD700,stroke:#B8860B,stroke-width:2px,color:#000;
  style D fill:#1E90FF,stroke:#0057A0,stroke-width:2px,color:#FFF;
  style E fill:#DC143C,stroke:#A00026,stroke-width:3px,color:#FFF;
  style F fill:#32CD32,stroke:#228B22,stroke-width:2px,color:#000;
  style G fill:#4682B4,stroke:#2C4F76,stroke-width:2px,color:#FFF;
