```markdown
# STORIES.md - Care Triage

## Epic: Core Triage Functionality

### User Story 1: Initial Ticket Triage
As a support agent, I want to submit a new ticket with its score and metadata, so that the system can begin the triage process.

**Acceptance Criteria:**
*   The system accepts a `Ticket` object with at least a `score` (integer) and `metadata` (dictionary).
*   The `Ticket` object is stored and accessible for subsequent processing.

### User Story 2: Agent Suggestion
As an ops manager, I want the system to suggest the most appropriate on-demand specialist for a given ticket, so that tickets are routed efficiently.

**Acceptance Criteria:**
*   The `CareTriage` system can be initialized with a `MarketplaceAPI` instance.
*   The `suggest_agent` method returns a suggested agent ID or `None` if no suitable agent is found.
*   The suggestion logic considers ticket score and metadata.

### User Story 3: Agent Assignment
As an ops manager, I want to be able to assign a suggested agent to a ticket, so that the ticket is officially routed for resolution.

**Acceptance Criteria:**
*   The `assign_agent` method successfully associates a suggested agent with a ticket.
*   The assignment is recorded and visible in the system.

### User Story 4: Escalation to Ops Manager
As an ops manager, I want to be notified when no suitable agent can be suggested for a ticket, so that I can manually intervene and assign resources.

**Acceptance Criteria:**
*   If `suggest_agent` returns `None`, the `notify_ops_manager` method is called.
*   The notification mechanism for the ops manager is clearly defined (e.g., email, internal alert).

## Epic: Marketplace Integration

### User Story 5: Basic Marketplace API Integration
As a developer, I want to integrate the `CareTriage` system with a `MarketplaceAPI` to fetch available agents, so that the system has a source of specialists.

**Acceptance Criteria:**
*   A `MarketplaceAPI` interface is defined.
*   The `CareTriage` system can instantiate with a concrete implementation of `MarketplaceAPI`.
*   The `MarketplaceAPI` can be queried for available agents based on ticket requirements (e.g., skills, availability).

### User Story 6: Agent Skill Matching
As an ops manager, I want the system to match ticket metadata to agent skills available through the `MarketplaceAPI`, so that the most qualified agents are suggested.

**Acceptance Criteria:**
*   Ticket metadata can be parsed to identify required skills or expertise.
*   The `MarketplaceAPI` can filter agents based on these identified skills.

## Epic: System Observability and Improvement

### User Story 7: Logging of Triage Decisions
As a system administrator, I want all triage decisions (suggestions, assignments, escalations) to be logged, so that we can audit and analyze system performance.

**Acceptance Criteria:**
*   Key events in the triage process are logged with relevant details (ticket ID, suggested agent, timestamp).
*   Logs are stored in a retrievable format.

### User Story 8: Feedback Loop for Agent Suggestions
As an AI engineer, I want to capture the outcomes of agent assignments (e.g., ticket resolution success), so that we can retrain and improve the agent suggestion model.

**Acceptance Criteria:**
*   A mechanism exists to record whether an assigned agent successfully resolved a ticket.
*   This outcome data is stored and can be used for future model training.
```
