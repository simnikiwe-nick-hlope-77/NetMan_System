# C4 Architectural Diagram
The C4 diagram was created [Mermaid](https://mermaid-js.github.io/mermaid-live-editor//edit#pako:eNpVjsFqw0AMRH9F6NRC_AM-FBq7zSWQQnOqnYOwZe-S7GqR14Rg-9-7TlpodZJm3gyasJGWMcfuItfGkEY4lrWHNK9VYdQO0dFwgix7mXccwYnn2wzbp53AYCQE6_vnB79dISim_YoxRGP9eXlYxT1_8DxDWe0pRAmnv87xKjO8VfbDpPr_jlFOqfeqo7yjrCGFgvSO4AYdqyPbpvenVakxGnZcY57WlvRcY-2XxNEY5fPmG8yjjrxBlbE3mAovQ7rG0FLk0lKv5H6RQP5LxP1AyzeJDl_b) and its online editor

```mermaid
graph TD;
  A["🖥️ Network Admin"] -->|Monitors & Configures| B(("📊 NMS Dashboard"));
  B -->|Sends Alerts| C["📩 Email Notifications"];
  B -->|Sends Performance Data| D["☁️ Cloud Monitoring"];
  B -->|Pushes Configs| E["🛠️ Auto-Configuration System"];
  E -->|Deploys Configurations| F["📡 Routers & Switches"];
  E -->|Backs Up| G["💾 Configuration Backup"];
