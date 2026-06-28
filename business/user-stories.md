# user-stories.md  

## Epic 1 – Ticket Ingestion & Classification  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 1 | **As a support analyst, I want the system to automatically ingest tickets from our existing ITSM tools (ServiceNow, JIRA Service Management, etc.), so that I don’t have to manually copy data.** | - Connectors for ServiceNow, JIRA Service Management, and email inboxes are configurable via UI.<br>- New tickets appear in Care‑Triage within 30 seconds of creation in the source system.<br>- All original ticket fields (title, description, priority, requester, attachments) are preserved.<br>- Ingestion logs show success/failure status for each ticket.<br>- Errors trigger an alert to the ops team. | M |
| 2 | **As a support manager, I want each incoming ticket to be automatically classified by clinical domain (e.g., EMR, PACS, Telehealth) and severity, so that we can prioritize resources correctly.** | - AI model assigns a domain label with ≥ 90 % precision on a validation set.<br>- Severity (Critical, High, Medium, Low) is inferred from keywords, SLA fields, and historical resolution time.<br>- Classification appears on the ticket card with a confidence score.<br>- Users can override the classification; overrides are logged for model retraining.<br>- Classification runs within 5 seconds of ingestion. | L |
| 3 | **As a compliance officer, I want all ingested tickets to be automatically tagged with HIPAA‑relevant metadata (PHI presence, data source), so that downstream workflows respect privacy rules.** | - Text analysis flags PHI indicators (MRN, DOB, etc.) with ≥ 85 % recall.<br>- Tagged tickets are stored in an encrypted, access‑controlled datastore.<br>- Metadata is visible in the ticket header and searchable.<br>- Non‑PHI tickets are not unnecessarily encrypted (performance optimization).<br>- Audit log records every tagging decision. | M |

---

## Epic 2 – Automated Triage & Routing  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 4 | **As a support analyst, I want the system to suggest the most appropriate internal resolver group for each ticket, so that tickets are routed to the right experts instantly.** | - Resolver group recommendation is based on domain, severity, and historical resolver performance.<br>- Recommendation appears as a dropdown with top 3 groups and confidence scores.<br>- Auto‑routing can be enabled/disabled per group.<br>- If auto‑routing is enabled, the ticket is assigned within 2 seconds of classification.<br>- Mis‑routed tickets can be re‑assigned; the action feeds back to the recommendation engine. | L |
| 5 | **As a shift lead, I want a “triage queue” view that surfaces tickets with AI‑generated priority scores, so that my team can focus on the highest‑impact issues first.** | - Priority score combines severity, SLA remaining time, and impact estimate.<br>- UI allows sorting/filtering by score, domain, and age.<br>- Score updates in real‑time as ticket data changes.<br>- Each ticket row shows a concise “action badge” (e.g., “Escalate”, “Assign”, “Awaiting Info”).<br>- Export to CSV/Excel is available for reporting. | M |
| 6 | **As a senior engineer, I want the system to automatically flag tickets that likely require escalation to a vendor or third‑party, so that we avoid delays.** | - Escalation flag is triggered when ticket mentions known vendor‑specific components or error codes.<br>- Flag includes suggested vendor contact template.<br>- Flagged tickets are highlighted in the UI and added to an “Escalation” dashboard.<br>- False‑positive rate ≤ 10 % on a rolling 30‑day window.<br>- Engineers can dismiss the flag; dismissal is logged. | S |

---

## Epic 3 – AI‑Driven Troubleshooting & Resolution Suggestions  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 7 | **As a support analyst, I want the AI to surface the top three most likely root‑cause hypotheses for a ticket, so that I can investigate faster.** | - Hypotheses are generated from a knowledge base of past tickets, error logs, and system topology.<br>- Each hypothesis includes a confidence score and a link to supporting documentation.<br>- Hypotheses appear within 8 seconds of ticket opening.<br>- Analysts can mark a hypothesis as “validated” or “rejected”; actions are stored for model improvement.<br>- At least 70 % of tickets have the correct root cause in the top‑3 list (based on historical data). | L |
| 8 | **As a support analyst, I want one‑click “apply known fix” actions that execute pre‑approved scripts or API calls, so that routine issues are resolved automatically.** | - Fix actions are defined in a secure playbook library with role‑based access control.<br>- Clicking a fix prompts a confirmation dialog showing expected impact.<br>- Execution logs (timestamp, outcome, operator) are attached to the ticket.<br>- Success rate of automated fixes ≥ 85 % on pilot tickets.<br>- Failure triggers an automatic rollback or escalation. | L |
| 9 | **As a knowledge‑base manager, I want the system to suggest updates to existing KB articles based on new resolution patterns, so that our documentation stays current.** | - When a hypothesis is marked “validated” and a fix is applied, the system proposes a KB edit draft.<br>- Draft includes a diff view, source ticket link, and suggested tags.<br>- Manager can approve/reject within the UI; approved edits are versioned.<br>- Suggested edits are generated for ≥ 60 % of tickets with novel resolutions.<br>- Edit acceptance rate is tracked for model tuning. | M |

---

## Epic 4 – Reporting, Analytics & Compliance  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 10 | **As a director of operations, I want a dashboard that shows SLA compliance trends by domain and severity, so that I can identify bottlenecks.** | - Dashboard visualizes % tickets meeting SLA per domain, severity, and week.<br>- Drill‑down to individual tickets and responsible teams.<br>- Alerts are generated when SLA breach risk exceeds 80 % for any cohort.<br>- Data refreshes every 5 minutes.<br>- Exportable PDF/PNG reports are available. | M |
| 11 | **As a security auditor, I want an immutable audit trail of all AI decisions (classification, routing, fix execution), so that we can demonstrate compliance with regulatory standards.** | - Every AI decision is logged with timestamp, model version, input snapshot, and output.<br>- Logs are stored in tamper‑evident append‑only storage (e.g., WORM S3 bucket).<br>- Auditors can query logs via a read‑only UI with filters (ticket ID, date range, decision type).<br>- Export to CSV for external audit tools.<br>- Retention period configurable (default 7 years). | S |
| 12 | **As a product owner, I want quarterly “impact reports” that quantify time saved per ticket and overall cost reduction, so that we can justify ROI to stakeholders.** | - Report calculates average handling time before vs. after AI assistance per ticket.<br>- Cost savings are estimated using internal labor rates.<br>- Includes charts for ticket volume, AI adoption rate, and satisfaction scores.<br>- Delivered automatically via email to stakeholders on the 1st of each quarter.<br>- Report template is customizable. | S |

---  

*Complexity Scale:*  
- **S** – Small (≤ 2 person‑days, low integration risk)  
- **M** – Medium (3‑5 person‑days, moderate integration)  
- **L** – Large (≥ 6 person‑days, significant AI model work or cross‑system integration)  