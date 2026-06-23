# ROADMAP.md

## Roadmap for Care Triage

### MVP Milestone

The MVP milestone focuses on delivering a functional core system capable of triaging tickets and suggesting appropriate specialists. This will ensure a solid foundation for future enhancements.

#### Must-Have Features:

- **Ticket Creation**: Implement the creation of `Ticket` objects with necessary attributes such as score and metadata. (MVP-Critical)
- **CareTriage Initialization**: Develop the `CareTriage` class that initializes with a `MarketplaceAPI` instance. (MVP-Critical)
- **Agent Suggestion Logic**: Implement the `suggest_agent` method within the `CareTriage` class to suggest an appropriate agent based on ticket details. (MVP-Critical)
- **Agent Assignment**: Develop the `assign_agent` method to assign the suggested agent to the ticket. (MVP-Critical)
- **Ops Manager Notification**: Implement the `notify_ops_manager` method to alert the operations manager if no suitable agent is found. (MVP-Critical)
- **Basic Marketplace Integration**: Ensure the `MarketplaceAPI` provides a list of available agents and their specialties. (MVP-Critical)

### Phase v1: Enhanced Functionality

Phase v1 aims to enhance the basic functionality by adding more sophisticated features and improving user experience.

#### Themes:

- **Advanced Matching Algorithms**: Improve the agent suggestion logic by incorporating advanced matching algorithms that consider additional factors like agent availability, past performance, and ticket urgency.
- **User Interface**: Develop a simple web interface for creating tickets, viewing suggestions, and managing assignments.
- **Analytics Dashboard**: Introduce an analytics dashboard for tracking ticket trends, agent performance, and system efficiency.

#### Features:

- **Enhanced Suggestion Logic**: Refine the `suggest_agent` method to include more complex decision-making criteria. 
- **Web Interface Development**: Create a user-friendly web interface for interacting with the Care Triage system.
- **Analytics Module**: Implement a module that collects and analyzes data to provide insights into system performance.

### Phase v2: Scalability and Automation

Phase v2 focuses on scaling the system and automating routine tasks to handle larger volumes of tickets efficiently.

#### Themes:

- **Scalability Enhancements**: Optimize the system architecture to support increased ticket volume and concurrent users.
- **Automation**: Automate repetitive tasks such as ticket categorization, initial triage, and routine notifications.
- **Integration with External Systems**: Integrate Care Triage with other systems like CRM, helpdesk tools, and communication platforms.

#### Features:

- **System Optimization**: Refactor the codebase and optimize database queries to improve performance under load.
- **Automated Ticket Handling**: Implement machine learning models to automate initial ticket categorization and triage.
- **External System Integrations**: Develop APIs and connectors for seamless integration with external systems.

By following this roadmap, Care Triage will evolve from a basic ticket triage system into a comprehensive, scalable solution that enhances operational efficiency and customer satisfaction.
