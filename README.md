# Care Triage

A system for suggesting on-demand specialists for tickets.

## Usage

1. Create a `Ticket` object with a score and metadata.
2. Create a `CareTriage` object with a `MarketplaceAPI` instance.
3. Call the `suggest_agent` method to get a suggested agent.
4. If an agent is suggested, call the `assign_agent` method to assign the agent to the ticket.
5. If no agent is suggested, call the `notify_ops_manager` method to notify the ops manager.
