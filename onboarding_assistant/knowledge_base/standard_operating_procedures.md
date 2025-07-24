# Standard Operating Procedures (SOP)

This document outlines repeatable processes for common tasks within our organization.  SOPs ensure consistency and reduce cognitive load.

## Onboarding a New Hire

1. **Account provisioning:** Create accounts for email, project management, code repositories, and any SaaS tools.
2. **Introduce to documentation:** Share links to the handbook, engineering principles, and personal philosophy documents.
3. **First week roadmap:** Assign a small starter project, schedule 1:1s with key team members, and set up mentorship.
4. **Feedback checkpoint:** At the end of week 1, solicit feedback from the new hire on the onboarding process and adjust accordingly.

## Running a Deployment

1. Ensure all tests pass locally.
2. Draft a change log describing the update.
3. Deploy to the staging environment and perform smoke tests.
4. Once verified, deploy to production using the chosen CI/CD pipeline.
5. Monitor logs and metrics for anomalies post‑deployment.

## Incident Response

1. **Detect:** Use monitoring tools to identify incidents quickly.
2. **Communicate:** Notify affected stakeholders and declare an incident.
3. **Mitigate:** Roll back or hotfix to minimize impact.
4. **Post‑mortem:** Document the root cause, resolution steps, and prevention measures.

Replace these procedures with ones specific to your organization.  Keep SOPs concise and update them as your processes evolve.