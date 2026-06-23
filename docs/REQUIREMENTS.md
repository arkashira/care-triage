# REQUIREMENTS.md

## Functional Requirements

### Ticket Management

1. **FR-1:** The system must allow the creation of a `Ticket` object with a score and metadata.
2. **FR-2:** The `Ticket` object must include fields for `score`, `metadata`, and `status`.
3. **FR-3:** The system must provide methods to update the `score` and `metadata` of a `Ticket`.

### Care Triage Logic

4. **FR-4:** The system must create a `CareTriage` object with a `MarketplaceAPI` instance as a dependency.
5. **FR-5:** The `CareTriage` object must have a `suggest_agent` method that takes a `Ticket` object as input and returns a suggested agent based on the ticket's score and metadata.
6. **FR-6:** The `suggest_agent` method must utilize the `MarketplaceAPI` to fetch available agents and their capabilities.
7. **FR-7:** The `suggest_agent` method must match the ticket's requirements with the agents' capabilities using a predefined algorithm or heuristic.
8. **FR-8:** The `CareTriage` object must have an `assign_agent` method that assigns the suggested agent to the ticket and updates the ticket's status accordingly.
9. **FR-9:** The `CareTriage` object must have a `notify_ops_manager` method that notifies the operations manager if no suitable agent is found for a ticket.

### Notification and Assignment

10. **FR-10:** The `assign_agent` method must send a notification to the assigned agent about the new ticket.
11. **FR-11:** The `notify_ops_manager` method must log the details of the ticket and send a notification to the operations manager for manual intervention.

## Non-Functional Requirements

### Performance

1. **NFR-1:** The `suggest_agent` method must respond within 2 seconds for 95% of requests under normal load conditions.
2. **NFR-2:** The system must handle up to 100 concurrent ticket submissions without degradation in performance.

### Security

3. **NFR-3:** All data exchanged between the `CareTriage` system and external APIs must be encrypted using TLS 1.2 or higher.
4. **NFR-4:** The system must implement role-based access control (RBAC) to ensure that only authorized personnel can access and modify ticket data.
5. **NFR-5:** Sensitive data such as agent and ticket metadata must be stored securely, adhering to industry-standard encryption practices.

### Reliability

6. **NFR-6:** The system must achieve an uptime of at least 99.9%.
7. **NFR-7:** The system must have a robust error handling mechanism to gracefully manage failures in agent assignment and notifications.

## Constraints

1. **CON-1:** The `CareTriage` system must integrate with the existing `MarketplaceAPI` without requiring significant changes to its interface.
2. **CON-2:** The system must be designed to scale horizontally to accommodate future increases in ticket volume.
3. **CON-3:** The implementation must adhere to the company's coding standards and best practices for maintainability and readability.

## Assumptions

1. **ASS-1:** The `MarketplaceAPI` provides reliable and accurate data about available agents and their capabilities.
2. **ASS-2:** The operations manager will be available to handle cases where no suitable agent is found within a reasonable timeframe.
3. **ASS-3:** The predefined algorithm or heuristic used by the `suggest_agent` method is effective in matching tickets with appropriate agents.
