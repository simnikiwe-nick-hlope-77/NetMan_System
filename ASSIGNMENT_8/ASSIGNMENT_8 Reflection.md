# Assignment 8 Reflection

## Challenges in Choosing Granularity for States and Actions

One of the most persistent challenges I faced during this assignment was determining the right level of granularity when modeling states and actions. At first, it was tempting to include every possible state change, condition, and edge case within each diagram to ensure completeness. However, I quickly realized that adding too much detail made the diagrams cluttered, harder to interpret, and less effective as communication tools.

I had to shift my focus toward what would be most meaningful for stakeholders and align with the system’s core behavior. I learned that choosing the right granularity requires context. If the diagram is meant for developers, a more detailed view might be appropriate. But for system-level design and stakeholder communication, clarity must take priority.

## Aligning Diagrams with Agile User Stories

Another challenge was ensuring that each diagram tied back to one or more Agile user stories. While some stories—like those related to login authentication or device configuration—aligned naturally with system states or workflows, others were less obvious and required deeper interpretation. For instance, the encryption diagram wasn't tied to an original user story, so I created one from the system administrator's perspective: "As a system admin, I want to encrypt user data with AES-256 so that security compliance policies are upheld."

This step made each diagram feel more purposeful and user-driven, which aligns with Agile principles. It also ensured that my models stayed grounded in stakeholder needs rather than abstract technical possibilities.

## Comparing State Diagrams and Activity Diagrams

Through this assignment, I gained a much clearer understanding of when and why to use state diagrams versus activity diagrams. State diagrams are excellent for modeling the behavior of a system object over time—for example, how a `NetworkDevice` transitions between states like `Registered`, `Active`, `UnderMaintenance`, and `Retired`. They show **what can happen to an object**, and help define its lifecycle and stability.

In contrast, activity diagrams model **how things are done**—the sequence of tasks, decisions, and responsibilities involved in a specific process. These diagrams were especially useful when modeling workflows like editing user privileges or handling login sessions with MFA.

Ultimately, both types are valuable. State diagrams helped me capture system logic, while activity diagrams showed user interactions and process flow. Using them together offered a more complete understanding of both the internal and external behavior of the NetMan_System.
