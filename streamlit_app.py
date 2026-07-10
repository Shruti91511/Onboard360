from datetime import date, timedelta

import streamlit as st


st.set_page_config(
    page_title="Onboard 360",
    page_icon="360",
    layout="wide",
)


PRIMARY = "#0d766e"
DARK = "#102427"
INK = "#172026"
MUTED = "#5f6c72"
TODAY = date.today()


st.markdown(
    f"""
    <style>
    .block-container {{
        padding-top: 1.4rem;
        padding-bottom: 2rem;
    }}
    .app-header {{
        background: {DARK};
        color: white;
        padding: 24px 28px;
        border-radius: 8px;
        border-bottom: 4px solid {PRIMARY};
        margin-bottom: 20px;
    }}
    .app-header h1 {{
        margin: 0;
        font-size: 34px;
        letter-spacing: 0;
    }}
    .app-header p {{
        margin: 6px 0 0;
        color: #d5e5e7;
        font-size: 16px;
    }}
    .metric-card {{
        border: 1px solid #dce3e7;
        background: #ffffff;
        border-radius: 8px;
        padding: 15px 16px;
        min-height: 112px;
    }}
    .metric-label {{
        color: {MUTED};
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
    }}
    .metric-value {{
        color: {INK};
        font-size: 29px;
        font-weight: 800;
        margin-top: 7px;
    }}
    .metric-caption {{
        color: {MUTED};
        font-size: 13px;
        margin-top: 3px;
    }}
    .agent-note {{
        border: 1px solid #b7d8d4;
        background: #eef8f7;
        border-radius: 8px;
        padding: 14px 16px;
        color: #244346;
        margin: 8px 0 16px;
    }}
    .risk-high {{
        color: #9b2424;
        font-weight: 800;
    }}
    .risk-medium {{
        color: #9a5b00;
        font-weight: 800;
    }}
    .risk-low {{
        color: #1f7a3f;
        font-weight: 800;
    }}
    .small-muted {{
        color: {MUTED};
        font-size: 14px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


SCENARIOS = {
    "Sales Manager onboarding": {
        "request": "Onboard Priya Sharma as a Sales Manager joining on July 15 in Bangalore. Her manager is Rahul Mehta and she needs a premium laptop.",
        "name": "Priya Sharma",
        "role": "Sales Manager",
        "department": "Sales",
        "location": "Bangalore",
        "joining_date": date(2026, 7, 15),
        "manager": "Rahul Mehta",
        "laptop": "Premium",
        "employment_type": "Full-time",
        "seniority": "Manager",
    },
    "Remote Engineer onboarding": {
        "request": "Onboard Arjun Rao as a Software Engineer joining on July 20 as a remote employee. His manager is Neha Iyer.",
        "name": "Arjun Rao",
        "role": "Software Engineer",
        "department": "Engineering",
        "location": "Remote",
        "joining_date": date(2026, 7, 20),
        "manager": "Neha Iyer",
        "laptop": "Standard",
        "employment_type": "Full-time",
        "seniority": "Individual Contributor",
    },
    "Finance Analyst onboarding": {
        "request": "Onboard Meera Nair as a Finance Analyst joining on July 18 in Mumbai. Her manager is Sandeep Kulkarni.",
        "name": "Meera Nair",
        "role": "Finance Analyst",
        "department": "Finance",
        "location": "Mumbai",
        "joining_date": date(2026, 7, 18),
        "manager": "Sandeep Kulkarni",
        "laptop": "Standard",
        "employment_type": "Full-time",
        "seniority": "Analyst",
    },
    "Senior Leadership onboarding": {
        "request": "Onboard Vikram Menon as Vice President, Enterprise Sales joining on July 22 in Delhi. His manager is Ananya Sen and he requires a premium laptop.",
        "name": "Vikram Menon",
        "role": "Vice President, Enterprise Sales",
        "department": "Sales",
        "location": "Delhi",
        "joining_date": date(2026, 7, 22),
        "manager": "Ananya Sen",
        "laptop": "Premium",
        "employment_type": "Full-time",
        "seniority": "Executive",
    },
}


BASE_TASKS = [
    ("Collect identity and employment documents", "HR", "HR Operations", "High", -7, "HR Agent"),
    ("Create HRMS employee profile", "HR", "HR Operations", "Critical", -6, "HR Agent"),
    ("Create company email and directory account", "IT", "IT Service Desk", "Critical", -5, "IT Access Agent"),
    ("Allocate laptop and endpoint security baseline", "Procurement", "Asset Team", "Critical", -4, "Procurement Agent"),
    ("Schedule manager welcome and first-week plan", "HR", "Hiring Manager", "Medium", 0, "Notification Agent"),
]


STATUS_OPTIONS = ["Pending", "In Progress", "Blocked", "Completed"]


def init_state():
    defaults = {
        "employee": None,
        "tasks": [],
        "policies": [],
        "reasoning": [],
        "audit": [],
        "connector_events": [],
        "generated": False,
        "connectors_synced": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def add_audit(message):
    timestamp = date.today().strftime("%d %b %Y")
    st.session_state.audit.append(f"{timestamp} - {message}")


def make_task(title, department, owner, priority, joining_date, offset, agent, approval=False):
    return {
        "title": title,
        "department": department,
        "owner": owner,
        "due_date": joining_date + timedelta(days=offset),
        "priority": priority,
        "agent": agent,
        "approval_required": approval,
        "status": "Pending",
    }


def append_policy(policies, reasoning, policy, reason):
    policies.append(policy)
    reasoning.append(reason)


def build_workflow(employee):
    tasks = []
    policies = []
    reasoning = []
    joining_date = employee["joining_date"]
    department = employee["department"]
    role = employee["role"].lower()
    seniority = employee["seniority"]

    append_policy(
        policies,
        reasoning,
        "All employees require HRMS profile, email, documents, laptop allocation, manager planning, and audit logging.",
        "Orchestrator Agent created the baseline workflow because every employee needs identity, access, asset, and manager-readiness steps.",
    )

    for title, team, owner, priority, offset, agent in BASE_TASKS:
        tasks.append(make_task(title, team, owner, priority, joining_date, offset, agent))

    if department == "Sales":
        append_policy(
            policies,
            reasoning,
            "Sales employees require CRM access and revenue-tool enablement.",
            "IT Access Agent added CRM access because the employee belongs to Sales and needs customer pipeline tools from day one.",
        )
        tasks.append(
            make_task("Grant CRM and sales enablement access", "IT", "Sales Systems", "Critical", joining_date, -4, "IT Access Agent")
        )

    if department == "Engineering":
        append_policy(
            policies,
            reasoning,
            "Engineering employees require source-control, work-tracking, and secure developer access.",
            "IT Access Agent added GitHub and Jira tasks because Engineering onboarding depends on developer tooling and traceable delivery workspaces.",
        )
        tasks.append(make_task("Grant GitHub repository access", "IT", "Engineering IT", "Critical", joining_date, -4, "IT Access Agent"))
        tasks.append(make_task("Grant Jira and Confluence access", "IT", "Engineering IT", "High", joining_date, -4, "IT Access Agent"))

    if department == "Finance":
        append_policy(
            policies,
            reasoning,
            "Finance employees require ERP access and segregation-of-duties review.",
            "Compliance/Risk Agent added ERP and access-control review because Finance roles touch sensitive financial systems.",
        )
        tasks.append(make_task("Grant ERP access", "IT", "Finance Systems", "Critical", joining_date, -5, "IT Access Agent", approval=True))
        tasks.append(make_task("Complete segregation-of-duties access review", "Compliance", "Risk Control Team", "Critical", joining_date, -4, "Compliance/Risk Agent", approval=True))

    if "manager" in role or employee["laptop"] == "Premium":
        append_policy(
            policies,
            reasoning,
            "Manager roles or premium assets require Finance approval before procurement completion.",
            "Finance Approval Agent triggered approval because either the role is managerial or the asset request has higher cost impact.",
        )
        tasks.append(make_task("Approve premium asset budget", "Finance", "Finance Ops", "High", joining_date, -7, "Finance Approval Agent", approval=True))

    if employee["location"] in ["Bangalore", "Mumbai", "Delhi"]:
        append_policy(
            policies,
            reasoning,
            "Office-based employees require facility readiness, ID card, and workspace allocation.",
            "Admin Agent added office-readiness tasks because the employee is joining from an HCLTech office location.",
        )
        tasks.append(make_task("Prepare office ID card", "Admin", "Facilities", "High", joining_date, -3, "Admin Agent"))
        tasks.append(make_task("Allocate workspace and facility access", "Admin", "Facilities", "Medium", joining_date, -3, "Admin Agent"))

    if employee["location"] == "Remote":
        append_policy(
            policies,
            reasoning,
            "Remote employees require secure laptop shipment and remote-work enablement.",
            "Procurement Agent added laptop shipment because remote employees need logistics completed before their first day.",
        )
        tasks.append(make_task("Ship laptop to employee address", "Procurement", "Asset Logistics", "Critical", joining_date, -7, "Procurement Agent"))
        tasks.append(make_task("Enable VPN and remote collaboration tools", "IT", "IT Service Desk", "Critical", joining_date, -4, "IT Access Agent"))

    if seniority == "Executive":
        append_policy(
            policies,
            reasoning,
            "Senior leadership onboarding requires executive support, priority asset handling, and leadership communications.",
            "Orchestrator Agent escalated the workflow because executive onboarding has higher visibility and stricter first-day readiness expectations.",
        )
        tasks.append(make_task("Assign executive assistant coordination", "Admin", "Executive Office", "High", joining_date, -5, "Admin Agent"))
        tasks.append(make_task("Prepare leadership announcement draft", "HR", "HR Communications", "Medium", joining_date, -2, "Notification Agent", approval=True))

    reasoning.append(
        "Notification Agent will route reminders to the department owner of the next pending critical task."
    )

    return tasks, policies, reasoning


def readiness_score(tasks):
    if not tasks:
        return 0
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    return round((completed / len(tasks)) * 100)


def pending_tasks(tasks):
    return [task for task in tasks if task["status"] != "Completed"]


def sla_risk_tasks(tasks):
    risk_items = []
    for task in pending_tasks(tasks):
        due_soon = task["due_date"] <= TODAY + timedelta(days=7)
        critical_or_blocked = task["priority"] == "Critical" or task["status"] == "Blocked"
        if due_soon and critical_or_blocked:
            risk_items.append(task)
    return risk_items


def manual_handoffs_avoided(tasks):
    departments = {task["department"] for task in tasks}
    return max(0, len(tasks) + len(departments) - 2)


def effort_saved_minutes(tasks):
    if not tasks:
        return 0
    return 25 + (len(tasks) * 6)


def risk_level(tasks, joining_date):
    score = readiness_score(tasks)
    sla_count = len(sla_risk_tasks(tasks))
    days_to_joining = (joining_date - TODAY).days if joining_date else 999
    if sla_count >= 3 or (days_to_joining <= 7 and score < 60):
        return "High"
    if sla_count > 0 or score < 75:
        return "Medium"
    return "Low"


def sla_status(tasks):
    count = len(sla_risk_tasks(tasks))
    if not tasks:
        return "Not Started"
    if count >= 3:
        return "SLA At Risk"
    if count > 0:
        return "Watchlist"
    return "On Track"


def readiness_status(tasks, employee):
    if not tasks:
        return "Draft"
    score = readiness_score(tasks)
    risk = risk_level(tasks, employee["joining_date"] if employee else None)
    if score == 100:
        return "Ready"
    if risk == "High":
        return "Executive Attention"
    if score >= 76:
        return "Almost Ready"
    if score >= 41:
        return "In Progress"
    return "At Risk"


def generate_workflow(employee):
    st.session_state.employee = employee
    st.session_state.tasks, st.session_state.policies, st.session_state.reasoning = build_workflow(employee)
    st.session_state.connector_events = []
    st.session_state.audit = [
        "Orchestrator Agent received HR onboarding request.",
        "Employee context extracted: role, department, location, seniority, joining date, and asset need.",
        "Specialized agents applied policy rules and generated department-owned work items.",
        "Compliance/Risk Agent calculated SLA risk, readiness score, and approval gates.",
        "Notification Agent identified next-action owners for follow-up.",
    ]
    st.session_state.generated = True
    st.session_state.connectors_synced = False


def connector_for_task(task):
    if task["approval_required"] and task["department"] == "Finance":
        return "SAP/Finance Approval"
    if task["approval_required"] and task["department"] == "Compliance":
        return "GRC Access Review"
    if task["department"] == "IT":
        return "ServiceNow IAM"
    if task["department"] == "Procurement":
        return "SAP Ariba"
    if task["department"] == "Admin":
        return "Facilities Portal"
    if task["department"] == "HR":
        return "Workday"
    return "Enterprise Workflow Queue"


def connector_action(task):
    if task["approval_required"]:
        return "Approval routed"
    if task["department"] == "IT":
        return "Access request created"
    if task["department"] == "Procurement":
        return "Procurement request opened"
    if task["department"] == "Admin":
        return "Facilities ticket created"
    if task["department"] == "HR":
        return "HR workflow task created"
    return "Work item created"


def simulate_enterprise_connectors():
    if not st.session_state.tasks:
        return

    events = []
    for index, task in enumerate(st.session_state.tasks, start=1):
        ticket_id = f"ONB-{TODAY.strftime('%y%m%d')}-{index:03d}"
        system = connector_for_task(task)
        action = connector_action(task)
        status = "Waiting for human approval" if task["approval_required"] else "Created"
        events.append(
            {
                "System": system,
                "Reference": ticket_id,
                "Action": action,
                "Task": task["title"],
                "Owner": task["owner"],
                "Status": status,
            }
        )

        if task["status"] == "Pending" and not task["approval_required"] and index <= 3:
            task["status"] = "In Progress"

    events.append(
        {
            "System": "Microsoft Teams",
            "Reference": f"MSG-{TODAY.strftime('%y%m%d')}-001",
            "Action": "Reminder sent",
            "Task": "Notify department owners of next pending critical actions",
            "Owner": "Notification Agent",
            "Status": "Delivered",
        }
    )
    events.append(
        {
            "System": "Outlook Calendar",
            "Reference": f"CAL-{TODAY.strftime('%y%m%d')}-001",
            "Action": "Calendar hold drafted",
            "Task": "Manager welcome and first-week planning",
            "Owner": st.session_state.employee["manager"],
            "Status": "Drafted",
        }
    )

    st.session_state.connector_events = events
    st.session_state.connectors_synced = True
    add_audit("Enterprise connectors simulated: tickets created, approvals routed, reminders sent, and status sync received.")


def scenario_data(name):
    return SCENARIOS[name].copy()


def show_header():
    st.markdown(
        """
        <div class="app-header">
            <h1>Onboard 360</h1>
            <p>Agentic Enterprise Onboarding Control Tower for HR, IT, Finance, Procurement, Admin, and Compliance</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(column, label, value, caption):
    with column:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-caption">{caption}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def show_metrics():
    tasks = st.session_state.tasks
    employee = st.session_state.employee
    score = readiness_score(tasks)
    departments = {task["department"] for task in tasks}
    sla_count = len(sla_risk_tasks(tasks))
    saved = effort_saved_minutes(tasks)

    col1, col2, col3, col4, col5 = st.columns(5)
    metric_card(col1, "Readiness", f"{score}%", "Policy-aware completion")
    metric_card(col2, "Total Tasks", str(len(tasks)), "Generated by agents")
    metric_card(col3, "SLA Risks", str(sla_count), "Critical or blocked due soon")
    metric_card(col4, "Effort Saved", f"{saved} min", "Estimated HR coordination")
    metric_card(col5, "Teams", str(len(departments)), "Departments orchestrated")
    st.progress(score / 100)

    if employee and tasks:
        risk = risk_level(tasks, employee["joining_date"])
        risk_class = "risk-high" if risk == "High" else "risk-medium" if risk == "Medium" else "risk-low"
        st.markdown(
            f"""
            <div class="agent-note">
                <strong>Control Tower Status:</strong> {readiness_status(tasks, employee)} |
                <strong>SLA:</strong> {sla_status(tasks)} |
                <strong>Risk:</strong> <span class="{risk_class}">{risk}</span> |
                <strong>Manual handoffs avoided:</strong> {manual_handoffs_avoided(tasks)}
            </div>
            """,
            unsafe_allow_html=True,
        )


def show_employee_summary():
    employee = st.session_state.employee
    if not employee:
        st.info("Generate a workflow to see the enterprise onboarding context.")
        return

    st.subheader("Employee Context")
    col1, col2, col3, col4 = st.columns(4)
    col1.write(f"**Employee:** {employee['name']}")
    col1.write(f"**Role:** {employee['role']}")
    col2.write(f"**Department:** {employee['department']}")
    col2.write(f"**Seniority:** {employee['seniority']}")
    col3.write(f"**Location:** {employee['location']}")
    col3.write(f"**Joining:** {employee['joining_date'].strftime('%d %b %Y')}")
    col4.write(f"**Manager:** {employee['manager']}")
    col4.write(f"**Laptop:** {employee['laptop']}")


def priority_badge(priority):
    if priority == "Critical":
        return "Critical"
    if priority == "High":
        return "High"
    return "Medium"


def show_tasks():
    st.subheader("Department-Wise Task Dashboard")
    if not st.session_state.tasks:
        st.info("No tasks yet. Select a scenario and generate a workflow.")
        return

    header = st.columns([3.1, 1.1, 1.4, 1.2, 1.1, 1.5, 1.5])
    header[0].markdown("**Task**")
    header[1].markdown("**Team**")
    header[2].markdown("**Agent**")
    header[3].markdown("**Due**")
    header[4].markdown("**Priority**")
    header[5].markdown("**Approval**")
    header[6].markdown("**Status**")
    st.divider()

    for index, task in enumerate(st.session_state.tasks):
        cols = st.columns([3.1, 1.1, 1.4, 1.2, 1.1, 1.5, 1.5])
        cols[0].write(f"**{task['title']}**")
        cols[0].caption(f"Owner: {task['owner']}")
        cols[1].write(task["department"])
        cols[2].write(task["agent"])
        cols[3].write(task["due_date"].strftime("%d %b %Y"))
        cols[4].write(priority_badge(task["priority"]))
        cols[5].write("Human approval" if task["approval_required"] else "Standard")
        new_status = cols[6].selectbox(
            "Status",
            STATUS_OPTIONS,
            index=STATUS_OPTIONS.index(task["status"]),
            key=f"task_status_{index}",
            label_visibility="collapsed",
        )
        if new_status != task["status"]:
            task["status"] = new_status
            add_audit(f"{task['title']} marked as {new_status}.")
            st.rerun()
        st.divider()


def show_agent_reasoning():
    st.subheader("Agent Reasoning")
    if not st.session_state.reasoning:
        st.info("Agent reasoning will appear after workflow generation.")
        return

    for item in st.session_state.reasoning:
        st.info(item)

    st.subheader("Agent Operating Model")
    st.table(
        [
            {"Agent": "Orchestrator Agent", "Responsibility": "Understands request, creates workflow plan, coordinates specialist agents."},
            {"Agent": "HR Agent", "Responsibility": "Employee profile, documents, HRMS profile, manager readiness."},
            {"Agent": "IT Access Agent", "Responsibility": "Email, CRM, ERP, GitHub, Jira, VPN, and secure access tasks."},
            {"Agent": "Procurement Agent", "Responsibility": "Laptop allocation, asset readiness, and shipment logistics."},
            {"Agent": "Finance Approval Agent", "Responsibility": "Budget approvals for premium assets and higher-cost requests."},
            {"Agent": "Compliance/Risk Agent", "Responsibility": "Policy checks, approval gates, SLA risk, and audit readiness."},
            {"Agent": "Notification Agent", "Responsibility": "Reminders, next-action routing, and leadership communications."},
        ]
    )


def show_governance():
    st.subheader("Governance and Controls")
    tasks = st.session_state.tasks
    if not tasks:
        st.info("Generate a workflow to see governance controls.")
        return

    approvals = [task for task in tasks if task["approval_required"]]
    access_tasks = [task for task in tasks if task["department"] in ["IT", "Compliance"]]
    risk_items = sla_risk_tasks(tasks)

    col1, col2, col3 = st.columns(3)
    col1.metric("Human Approval Gates", len(approvals))
    col2.metric("Access-Control Tasks", len(access_tasks))
    col3.metric("SLA Watchlist Items", len(risk_items))

    st.markdown("**Policy Checks Applied**")
    for policy in st.session_state.policies:
        st.success(policy)

    st.markdown("**Access and Risk Controls**")
    controls = [
        "Human-in-the-loop approval is required for premium assets, ERP access, segregation-of-duties checks, and leadership communications.",
        "Every generated action is stored in the audit log for traceability.",
        "Critical tasks due soon are elevated to the SLA watchlist.",
        "The readiness report identifies the next department owner instead of leaving HR to manually chase teams.",
        "Mock connectors represent Workday, ServiceNow, SAP, Jira, Outlook, and Teams without using real enterprise data.",
    ]
    for control in controls:
        st.write(f"- {control}")

    st.markdown("**Audit Log**")
    for item in st.session_state.audit:
        st.write(f"- {item}")


def show_enterprise_connectors():
    st.subheader("Enterprise Connectors")
    tasks = st.session_state.tasks
    if not tasks:
        st.info("Generate a workflow to simulate enterprise system integration.")
        return

    st.markdown(
        """
        In the hackathon prototype, this tab simulates integrations. In a production rollout,
        Onboard 360 would create tickets, route approvals, send reminders, and sync status through
        systems such as ServiceNow, Workday, SAP, Jira, Microsoft Teams, Outlook, IAM, and GRC tools.
        """
    )

    if st.button("Simulate Enterprise Connectors", type="primary", use_container_width=True):
        simulate_enterprise_connectors()
        st.success("Connector simulation completed. Tickets, approvals, reminders, and status sync are now visible.")
        st.rerun()

    if not st.session_state.connector_events:
        st.info("Click the simulation button to show how Onboard 360 moves work into enterprise systems.")
        return

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tickets / Requests", len(st.session_state.connector_events) - 2)
    col2.metric(
        "Approvals Routed",
        sum(1 for event in st.session_state.connector_events if event["Action"] == "Approval routed"),
    )
    col3.metric(
        "Notifications Sent",
        sum(1 for event in st.session_state.connector_events if event["System"] in ["Microsoft Teams", "Outlook Calendar"]),
    )
    col4.metric("Status Sync", "Active" if st.session_state.connectors_synced else "Pending")

    st.markdown("**Connector Activity Log**")
    st.dataframe(st.session_state.connector_events, use_container_width=True, hide_index=True)

    st.markdown("**How work continues after the agent creates the workflow**")
    st.write("- IT teams continue work in ServiceNow/IAM, not inside Onboard 360.")
    st.write("- Procurement continues work in SAP Ariba or the asset system.")
    st.write("- Finance and Compliance approvals remain human-approved.")
    st.write("- Teams and Outlook carry reminders and calendar actions.")
    st.write("- Onboard 360 syncs status back and keeps HR focused on readiness, SLA risk, and exceptions.")


def show_business_impact():
    st.subheader("Business Impact")
    tasks = st.session_state.tasks
    if not tasks:
        st.info("Generate a workflow to calculate impact metrics.")
        return

    saved = effort_saved_minutes(tasks)
    handoffs = manual_handoffs_avoided(tasks)
    departments = len({task["department"] for task in tasks})

    col1, col2, col3 = st.columns(3)
    col1.metric("Estimated Effort Saved", f"{saved} min")
    col2.metric("Manual Handoffs Avoided", handoffs)
    col3.metric("Functions Coordinated", departments)

    st.markdown("**Before vs After**")
    st.table(
        [
            {"Area": "Request intake", "Before": "Email or spreadsheet", "With Onboard 360": "Single HR request converted into workflow"},
            {"Area": "Coordination", "Before": "Manual follow-ups with every team", "With Onboard 360": "Agent-routed owners and next actions"},
            {"Area": "Policy adherence", "Before": "Depends on HR memory and local checklists", "With Onboard 360": "Policy-driven task generation"},
            {"Area": "Risk visibility", "Before": "Discovered late or on joining day", "With Onboard 360": "SLA watchlist and readiness score"},
            {"Area": "Auditability", "Before": "Scattered email evidence", "With Onboard 360": "Central audit log and readiness report"},
        ]
    )

    st.markdown("**Enterprise Value Proposition**")
    st.write("- Productivity: reduces repetitive HR coordination and task creation effort.")
    st.write("- SLA adherence: highlights critical pending work before the joining date.")
    st.write("- Employee experience: improves first-day readiness for access, assets, and workspace.")
    st.write("- Governance: keeps sensitive actions behind human approval gates.")
    st.write("- Scalability: the same orchestration pattern can extend to offboarding, transfers, access reviews, and procurement requests.")


def show_report():
    st.subheader("Enterprise Readiness Report")
    employee = st.session_state.employee
    tasks = st.session_state.tasks
    if not employee or not tasks:
        st.info("Generate a workflow to create the readiness report.")
        return

    score = readiness_score(tasks)
    pending = pending_tasks(tasks)
    critical = [task for task in pending if task["priority"] == "Critical"]
    approvals = [task for task in pending if task["approval_required"]]
    risk_items = sla_risk_tasks(tasks)
    next_action = pending[0] if pending else None

    report_lines = [
        "ONBOARD 360 ENTERPRISE ONBOARDING READINESS REPORT",
        "",
        f"Employee: {employee['name']}",
        f"Role: {employee['role']}",
        f"Department: {employee['department']}",
        f"Seniority: {employee['seniority']}",
        f"Location: {employee['location']}",
        f"Joining Date: {employee['joining_date'].strftime('%d %b %Y')}",
        f"Manager: {employee['manager']}",
        "",
        f"Readiness Score: {score}%",
        f"Control Tower Status: {readiness_status(tasks, employee)}",
        f"SLA Status: {sla_status(tasks)}",
        f"Risk Level: {risk_level(tasks, employee['joining_date'])}",
        "",
        f"Completed Tasks: {sum(1 for task in tasks if task['status'] == 'Completed')}",
        f"Pending Tasks: {len(pending)}",
        f"Critical Pending Tasks: {len(critical)}",
        f"Open Approval Gates: {len(approvals)}",
        f"SLA Watchlist Items: {len(risk_items)}",
        "",
        "Executive Risk Summary:",
    ]

    if risk_items:
        report_lines.extend(
            [
                f"- {task['title']} owned by {task['owner']} is {task['status']} and due on {task['due_date'].strftime('%d %b %Y')}."
                for task in risk_items
            ]
        )
    else:
        report_lines.append("- No critical SLA risks currently open.")

    report_lines.extend(["", "Recommended Next Action:"])
    if next_action:
        report_lines.append(
            f"Route reminder to {next_action['department']} owner {next_action['owner']} for '{next_action['title']}'."
        )
    else:
        report_lines.append("Confirm first-day schedule and send welcome communication.")

    report_lines.extend(
        [
            "",
            "Governance Note:",
            "Sensitive access, premium assets, ERP permissions, and leadership communications remain human-approved before execution.",
        ]
    )

    st.code("\n".join(report_lines), language="text")


def show_input_panel():
    st.subheader("Enterprise Onboarding Request")
    st.caption("Choose a scenario, adjust details, and generate the agentic workflow.")

    scenario = st.selectbox("Demo scenario", list(SCENARIOS.keys()))
    demo = scenario_data(scenario)
    scenario_key = scenario.lower().replace(" ", "_")

    request = st.text_area(
        "Natural language request",
        value=demo["request"],
        height=118,
        key=f"request_{scenario_key}",
    )
    name = st.text_input("Employee name", value=demo["name"], key=f"name_{scenario_key}")

    col1, col2 = st.columns(2)
    role = col1.text_input("Role", value=demo["role"], key=f"role_{scenario_key}")
    department = col2.selectbox(
        "Department",
        ["Sales", "Engineering", "Finance", "HR", "Legal"],
        index=["Sales", "Engineering", "Finance", "HR", "Legal"].index(demo["department"]),
        key=f"department_{scenario_key}",
    )

    col3, col4 = st.columns(2)
    location = col3.selectbox(
        "Location",
        ["Bangalore", "Mumbai", "Delhi", "Remote"],
        index=["Bangalore", "Mumbai", "Delhi", "Remote"].index(demo["location"]),
        key=f"location_{scenario_key}",
    )
    joining_date = col4.date_input(
        "Joining date",
        value=demo["joining_date"],
        key=f"joining_date_{scenario_key}",
    )

    col5, col6 = st.columns(2)
    manager = col5.text_input("Manager", value=demo["manager"], key=f"manager_{scenario_key}")
    laptop = col6.selectbox(
        "Laptop",
        ["Premium", "Standard"],
        index=["Premium", "Standard"].index(demo["laptop"]),
        key=f"laptop_{scenario_key}",
    )

    col7, col8 = st.columns(2)
    employment_type = col7.selectbox(
        "Employment type",
        ["Full-time", "Contractor", "Intern"],
        index=["Full-time", "Contractor", "Intern"].index(demo["employment_type"]),
        key=f"employment_type_{scenario_key}",
    )
    seniority = col8.selectbox(
        "Seniority",
        ["Individual Contributor", "Analyst", "Manager", "Executive"],
        index=["Individual Contributor", "Analyst", "Manager", "Executive"].index(demo["seniority"]),
        key=f"seniority_{scenario_key}",
    )

    if st.button("Generate Enterprise Workflow", type="primary", use_container_width=True):
        missing = [
            label
            for label, value in {
                "Employee name": name,
                "Role": role,
                "Department": department,
                "Location": location,
                "Joining date": joining_date,
                "Manager": manager,
            }.items()
            if not value
        ]
        if missing:
            st.error("Missing required fields: " + ", ".join(missing))
        else:
            generate_workflow(
                {
                    "request": request,
                    "name": name,
                    "role": role,
                    "department": department,
                    "location": location,
                    "joining_date": joining_date,
                    "manager": manager,
                    "laptop": laptop,
                    "employment_type": employment_type,
                    "seniority": seniority,
                }
            )
            st.success("Enterprise workflow generated.")


def main():
    init_state()
    show_header()

    st.markdown(
        """
        <div class="agent-note">
        <strong>Enterprise story:</strong> Onboarding is not only an HR checklist.
        It is a cross-functional operations workflow across HR, IT, Finance, Procurement,
        Admin, Compliance, and managers. Onboard 360 turns that workflow into a governed control tower.
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([0.9, 1.75], gap="large")

    with left:
        show_input_panel()

    with right:
        st.subheader("Executive Control Tower")
        show_metrics()
        show_employee_summary()

        tabs = st.tabs(
            [
                "Tasks",
                "Agent Reasoning",
                "Enterprise Connectors",
                "Governance",
                "Business Impact",
                "Readiness Report",
            ]
        )
        with tabs[0]:
            show_tasks()
        with tabs[1]:
            show_agent_reasoning()
        with tabs[2]:
            show_enterprise_connectors()
        with tabs[3]:
            show_governance()
        with tabs[4]:
            show_business_impact()
        with tabs[5]:
            show_report()


if __name__ == "__main__":
    main()
