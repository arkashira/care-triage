```markdown
# tech-spec.md

## Stack
- **Language**: Python (3.11+)
- **Framework**: FastAPI (for API), Django (for admin and complex queries)
- **Runtime**: Docker containers orchestrated by Kubernetes
- **Database**: PostgreSQL (for relational data), MongoDB (for unstructured data)
- **Message Queue**: RabbitMQ (for asynchronous task processing)
- **AI/ML**: PyTorch (for model training and inference)

## Hosting
- **Free-tier-first**: AWS Free Tier (for initial development and testing)
- **Specific Platforms**:
  - **Development**: AWS EC2 (t2.micro instances)
  - **Staging**: AWS EKS (Elastic Kubernetes Service) with 2 nodes
  - **Production**: AWS EKS with auto-scaling (3-10 nodes based on load)

## Data Model
### Tables/Collections
1. **Tickets**
   - `ticket_id` (UUID, primary key)
   - `title` (String)
   - `description` (Text)
   - `status` (Enum: 'open', 'in_progress', 'resolved', 'closed')
   - `priority` (Enum: 'low', 'medium', 'high', 'critical')
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)
   - `assignee_id` (UUID, foreign key to Users)
   - `category` (String)

2. **Users**
   - `user_id` (UUID, primary key)
   - `username` (String)
   - `email` (String)
   - `role` (Enum: 'admin', 'agent', 'viewer')
   - `created_at` (Timestamp)

3. **Logs**
   - `log_id` (UUID, primary key)
   - `ticket_id` (UUID, foreign key to Tickets)
   - `action` (String)
   - `user_id` (UUID, foreign key to Users)
   - `timestamp` (Timestamp)
   - `details` (Text)

## API Surface
1. **POST /api/tickets** - Create a new support ticket
2. **GET /api/tickets** - List all support tickets with optional filters
3. **GET /api/tickets/{ticket_id}** - Retrieve a specific support ticket
4. **PUT /api/tickets/{ticket_id}** - Update a support ticket
5. **DELETE /api/tickets/{ticket_id}** - Delete a support ticket
6. **POST /api/tickets/{ticket_id}/assign** - Assign a ticket to an agent
7. **POST /api/tickets/{ticket_id}/resolve** - Mark a ticket as resolved
8. **POST /api/tickets/{ticket_id}/close** - Close a ticket
9. **GET /api/users** - List all users
10. **GET /api/users/{user_id}** - Retrieve a specific user

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for API authentication
- **Secrets**: AWS Secrets Manager for storing sensitive information like database credentials and API keys
- **IAM**: AWS IAM roles and policies for fine-grained access control
- **Data Encryption**: TLS for data in transit, AES-256 for data at rest

## Observability
- **Logs**: AWS CloudWatch for centralized logging
- **Metrics**: Prometheus for metrics collection and Grafana for visualization
- **Traces**: Jaeger for distributed tracing

## Build/CI
- **Version Control**: GitHub
- **CI/CD Pipeline**: GitHub Actions
  - **Build**: Docker images built and pushed to AWS ECR
  - **Test**: Unit tests, integration tests, and security scans
  - **Deploy**: Automated deployment to AWS EKS
- **Testing**:
  - **Unit Tests**: Pytest
  - **Integration Tests**: Postman/Newman
  - **Security Scans**: Trivy for container vulnerability scanning
```