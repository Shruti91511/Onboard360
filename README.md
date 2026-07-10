# Onboard 360

**Agentic Enterprise Onboarding Control Tower**

Onboard 360 is a hackathon prototype for the **Agents/Agentic Workflows for Enterprise Operations** track. It converts one HR onboarding request into a governed, policy-aware workflow across HR, IT, Finance, Procurement, Admin, Compliance, and the hiring manager.

## Executive Summary

In large enterprises, onboarding is not only an HR checklist. It is a cross-functional operations workflow. HR must coordinate identity documents, HRMS profile creation, email setup, application access, laptop allocation, finance approvals, office readiness, manager planning, and audit evidence.

Onboard 360 acts as an agentic control tower. It uses an Orchestrator Agent and specialist function agents to generate the right tasks, apply policy rules, identify approval gates, calculate SLA risk, track readiness, and produce an enterprise readiness report.

## Problem

Enterprise onboarding is often managed through emails, spreadsheets, manual reminders, and separate ticketing tools. This creates:

- Missed or delayed access
- Laptop and workspace delays
- Manual HR follow-ups across multiple teams
- Low visibility into joining readiness
- Weak audit trail for sensitive access and approvals
- Poor first-day employee experience

## Solution

Onboard 360 turns a single request into a complete onboarding workflow:

- Captures employee context from HR
- Applies policy rules based on department, role, location, seniority, and asset needs
- Creates department-wise tasks
- Identifies human approval gates
- Simulates enterprise connectors for tickets, approvals, reminders, and status sync
- Tracks readiness score and SLA risk
- Shows agent reasoning
- Produces an audit-ready enterprise readiness report

## Agentic Architecture

```text
HR Request
  -> Orchestrator Agent
  -> HR Agent
  -> IT Access Agent
  -> Procurement Agent
  -> Finance Approval Agent
  -> Compliance/Risk Agent
  -> Notification Agent
  -> Control Tower Dashboard + Governance + Readiness Report
```

## Demo Scenarios

The prototype includes four enterprise scenarios:

- Sales Manager onboarding: CRM access, premium asset approval, ID card, desk allocation
- Remote Engineer onboarding: GitHub, Jira, VPN, collaboration tools, laptop shipment
- Finance Analyst onboarding: ERP access and segregation-of-duties review
- Senior Leadership onboarding: executive coordination, premium asset handling, leadership communication

## Business Impact

Onboard 360 demonstrates measurable enterprise value:

- Reduces manual onboarding coordination effort
- Avoids repeated handoffs between HR, IT, Finance, Procurement, Admin, and Compliance
- Improves SLA visibility before the employee joins
- Improves first-day readiness and employee experience
- Keeps sensitive actions behind human approval gates
- Creates audit-ready workflow history

## Run Locally

Install Python and Streamlit, then run:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Demo Instructions

1. Open the Streamlit app.
2. Select **Sales Manager onboarding**.
3. Click **Generate Enterprise Workflow**.
4. Show the Executive Control Tower metrics.
5. Open **Tasks** and point out department owners.
6. Open **Agent Reasoning** to show why tasks were added.
7. Open **Enterprise Connectors** and click **Simulate Enterprise Connectors** to show tickets, approvals, reminders, and status sync.
8. Open **Governance** to show approvals, policy checks, access controls, and audit log.
9. Open **Business Impact** to show before vs after value.
10. Open **Readiness Report** for the executive summary.

## Future Roadmap

- Integrate with Workday, ServiceNow, SAP, Jira, Outlook, Teams, and enterprise identity platforms
- Add real approval routing and notification delivery
- Add document upload and ID verification
- Extend to offboarding, internal transfers, access reviews, procurement requests, and vendor onboarding
- Add analytics for SLA bottlenecks, department performance, and employee experience trends

## Hackathon Track

Agents/Agentic Workflows for Enterprise Operations
# Onboard360
Onboard360 turns one HR request into a complete employee onboarding workflow.
