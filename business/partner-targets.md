# partner‑targets.md – Care‑Triage Integration Roadmap  

| # | SaaS / API | Primary Use‑Case for Care‑Triage | Free‑Tier / Trial Limits* | Integration Effort | Value‑Add (User Job Solved) | Affiliate / Rev‑Share Potential |
|---|------------|----------------------------------|---------------------------|--------------------|----------------------------|---------------------------------|
| 1 | **ServiceNow ITSM** | Pull existing support tickets, push AI‑generated triage recommendations, auto‑assign to the right support group. | Developer Instance (free, 1 yr) – 1 M API calls / month, 10 k records storage. | **M** – OAuth 2.0, table API, webhook subscription, data‑model mapping (Incident ↔ Care‑Triage Ticket). | *“Prioritize & route tickets”* – reduces mean‑time‑to‑triage (MTTT) by surfacing severity, affected service, and suggested remediation. | ServiceNow Partner Program (tiered revenue‑share on marketplace listings). |
| 2 | **Jira Service Management (Atlassian)** | Sync tickets from Jira, enrich with AI‑driven symptom classification, suggest resolution steps, auto‑close solved tickets. | Free tier – 3 agents, 2 GB attachment storage, 2 000 API calls / month. | **S** – REST API + webhooks, simple field mapping (Issue → Care‑Triage Ticket). | *“Accelerate ticket resolution”* – cuts resolution time by auto‑populating knowledge‑base links and diagnostic scripts. | Atlassian Marketplace affiliate (15 % revenue share on paid add‑ons). |
| 3 | **Zendesk Support** | Ingest tickets, run AI triage, auto‑escalate high‑severity cases, surface root‑cause hypotheses. | 14‑day free trial (full feature), then “Team” plan $49/agent/mo – 100 k API calls / month. | **M** – OAuth, ticket API, trigger/webhook integration, custom fields for AI tags. | *“Reduce manual triage effort”* – lowers average tickets per agent per day. | Zendesk Partner Program – co‑sell & revenue‑share on integrated apps. |
| 4 | **Datadog Monitoring** | Pull alerts & metrics (e.g., latency spikes, error rates) to auto‑create tickets with contextual logs & graphs. | Free tier – 5 hosts, 1 day retention, 1 M custom metrics. | **S** – API key auth, metric/alert ingestion, webhook to create Care‑Triage tickets. | *“Proactive incident creation”* – creates tickets before users report issues, improving MTTR. | Datadog Technology Partner – referral fees for paid plans. |
| 5 | **Slack (or Microsoft Teams)** | Real‑time ticket notifications, AI‑driven suggestions via slash‑commands, collaborative triage chat. | Slack Free – 10 k searchable messages, 1‑on‑1 & 2‑person channels; Teams Free – 300 MB file storage. | **S** – Bot user, slash‑command endpoint, event subscription, OAuth scopes. | *“Enable on‑the‑fly triage”* – agents can ask AI for next steps without leaving chat. | Slack App Directory (revenue share on paid app installs). |
| 6 | **Okta Identity Cloud** | Verify requester identity, enforce role‑based access to ticket data, auto‑populate user profile info. | Developer Edition – 1 000 MAU, unlimited API calls. | **M** – OpenID Connect, SCIM provisioning, token validation. | *“Secure ticket handling”* – ensures only authorized staff see PHI‑related tickets. | Okta Integration Network – partner incentives for SSO add‑ons. |
| 7 | **Google Cloud Healthcare API (FHIR)** | Pull patient‑context (e.g., device IDs, encounter data) to enrich tickets with clinical relevance. | Free tier – 1 GB storage, 50 k API calls / month. | **L** – FHIR resource mapping, HIPAA‑compliant data handling, consent management. | *“Clinical‑aware triage”* – AI can suggest device‑specific fixes, reducing false positives. | Google Cloud Partner Advantage – joint go‑to‑market and revenue‑share on API usage. |
| 8 | **Confluence (Atlassian) Knowledge Base** | Auto‑link AI‑suggested solutions to existing KB articles, surface most‑relevant docs in ticket view. | Free tier – 10 users, 2 GB storage, 100 0 API calls / month. | **S** – REST API, page search, embed links. | *“Knowledge‑driven resolution”* – cuts time spent searching docs by 30 %. | Atlassian Marketplace (same as #2). |

\*Free‑tier limits are current as of 2024‑06; they are sufficient for pilot integrations and can be upgraded as usage scales.

---

## Prioritization & Roll‑out Timeline  

| Phase | Target(s) | Rationale | Expected Business Impact (KPIs) |
|-------|-----------|-----------|---------------------------------|
| **Phase 1 – Core Ticketing** (Weeks 1‑4) | ServiceNow, Jira Service Management, Zendesk | These are the three most common ITSM platforms in healthcare tech ops; integration unlocks immediate ticket ingestion & AI triage. | • Reduce Mean‑Time‑to‑Triage (MTTT) by 40 % <br>• Capture 15 % of existing tickets for AI‑driven routing (pilot). |
| **Phase 2 – Observability & Proactive Alerts** (Weeks 5‑8) | Datadog, Google Cloud Healthcare API | Correlate system alerts & clinical context to auto‑create tickets before user impact. | • Decrease Mean‑Time‑to‑Detect (MTTD) by 25 % <br>• Increase proactive ticket volume to 20 % of total. |
| **Phase 3 – Collaboration & Security** (Weeks 9‑12) | Slack (or Teams), Okta | Embed AI suggestions directly into agents’ workflow and secure access to PHI‑linked tickets. | • Cut average handling time per ticket by 15 % <br>• Achieve 100 % compliance with role‑based access policies. |
| **Phase 4 – Knowledge‑Base Enrichment** (Weeks 13‑16) | Confluence | Close the loop by surfacing relevant KB articles automatically. | • Reduce repeat tickets by 10 % <br>• Increase KB article usage metrics by 30 %. |

---

## Affiliate / Revenue‑Share Playbook  

1. **Marketplace Listings** – Publish Care‑Triage as a paid add‑on in ServiceNow Store, Atlassian Marketplace (Jira & Confluence), and Zendesk Marketplace.  
2. **Referral Fees** – Negotiate a 10‑15 % referral fee with Datadog and Okta for every new paid tenant that enables the integration.  
3. **Co‑Sell Agreements** – Partner with Google Cloud to bundle Care‑Triage with the Healthcare API; Google shares 5 % of API usage revenue.  
4. **App Directory Monetization** – For Slack/Teams, use the “Paid App” model (per‑install fee) and share 20 % with the platform.  

These arrangements turn integration work into a recurring revenue stream beyond the core SaaS subscription.

---  

*Prepared by Business‑Synthesis – Care‑Triage product line*  