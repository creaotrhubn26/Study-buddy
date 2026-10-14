"""Compact task resources shared by the Universal Exam Resolver."""

import streamlit as st

from evo_curriculum import ASSET_ROOT, get_evo_course_lessons
from evo_tasks import TEMPLATE_ROOT

CONTENT_REVISION = "2026-10-14-lessons-73-74"


TASK_72_OBJECTIVES = {
    "Product spending": (
        "Product spending", "Income, Marital_Status, Education and the six Mnt fields",
        "Create PivotTables with customer segments in Rows and product spending summarised as Average in Values. Show group sizes and compare the same units and period.",
        "Create a bar chart. Fill in n, result, unit, filter/method and interpretation in the worksheet.",
        "Historical spending is not profit or a calculated Customer Lifetime Value (CLV).",
    ),
    "Retention": (
        "Retention and purchase activity", "Recency, Dt_Customer and purchase counts by channel",
        "Describe the distribution of Recency. Sum web, catalogue and store purchases as a historical purchase activity proxy. Check missing values before adding the counts.",
        "Compare purchase activity between clearly defined Recency groups. Document group boundaries and valid n.",
        "Dt_Customer is the registration date. Without a full purchase history or an observed churn outcome, actual retention cannot be measured directly.",
    ),
    "Upsell channels": (
        "Channels and upselling", "NumWebPurchases, NumCatalogPurchases, NumStorePurchases and product spending",
        "Create a PivotTable with customer segments in Rows and average purchase counts by channel in Values.",
        "Compare channel use with product preferences. Suggest one relevant product and one channel for a segment.",
        "The recommendation is a hypothesis to test; the pattern does not prove an upselling effect.",
    ),
    "Deals pricing": (
        "Deals and pricing", "NumDealsPurchases and Income",
        "Create a scatter plot with Income on the X-axis and NumDealsPurchases on the Y-axis. Use complete numeric pairs.",
        "Compare deal purchases between documented income groups. State the number of observations and the association you actually see.",
        "Deal purchases alone do not show the effect of a particular price change; discount amounts and a comparison baseline are missing.",
    ),
    "Profitability limits": (
        "Profitability and data limits", "MntGoldProds and Z_Revenue",
        "Check variation in Z_Revenue using =STDEV.P(EVO7Prepared[Z_Revenue]).",
        "Document that correlation is undefined when the standard deviation is zero. Excel CORREL returns #DIV/0!, not r=0.",
        "Product profitability requires relevant revenue, cost and margin data. Use currency units when a currency is not documented.",
    ),
}


TASK_73_OBJECTIVES = {
    "Complaints": (
        "Customer satisfaction and complaints", "Complain, Education, Marital_Status, Income and purchase behaviour",
        "Validate Complain as a numeric 0/1 flag. Create a PivotTable with a customer group in Rows and Complain in Values as Average (complaint rate) and Count (valid n).",
        "Compare complaint rates and purchasing patterns between groups. Create a bar chart and record the valid denominator, filters and interpretation.",
        "Complain records a complaint flag, not the complaint's cause or an overall satisfaction score. Missing or invalid flags must not be treated as zero.",
    ),
    "Personas": (
        "Customer personas and customisation", "Year_Birth, Education, Marital_Status, Kidhome and Teenhome",
        "Define documented household groups using Kidhome and Teenhome. Use a documented historical reference year for age, or analyse Year_Birth directly when that year is unknown.",
        "Profile each group using its size, recorded demographics, product preferences and channel use. Write an evidence-based persona and one marketing hypothesis to test.",
        "Do not use today's year to age a historical snapshot or invent personality traits and motivations that the data does not record.",
    ),
    "Response spending": (
        "Campaign response and spending", "Response, the six Mnt spending fields and NumWebVisitsMonth",
        "Validate Response as a numeric 0/1 flag. Create a PivotTable with Response in Rows and average product spending and web visits in Values, together with valid counts.",
        "Create a grouped bar chart comparing responders and non-responders. Report spending differences, group sizes and response rates within clearly defined groups.",
        "A spending difference does not prove campaign lift. Timing, prior behaviour and customer selection can explain an association.",
    ),
    "Detailed segments": (
        "In-depth customer segmentation", "Year_Birth, Education, Marital_Status, Income and the six Mnt spending fields",
        "Define reproducible demographic and income segment rules with explicit boundaries. Start with a few broad groups and document the age reference if age is used.",
        "Compare average product spending and campaign response rates by segment. Show valid n, inspect unusual values and propose a targeted product or campaign test.",
        "Tiny groups and extreme values can produce unstable comparisons. State uncertainty and keep units, periods and missing-value rules consistent.",
    ),
    "Household channels": (
        "Household and channel behaviour", "Kidhome, Teenhome, NumStorePurchases, NumWebPurchases and NumCatalogPurchases",
        "Reuse the household groups from Personas. Create a PivotTable with HouseholdGroup in Rows and average purchase counts by channel in Values, together with group sizes.",
        "Create a grouped bar chart and compare channel patterns. Suggest a channel to test for a specific household group using the observed evidence.",
        "Use compatible observation periods. Household composition does not automatically cause channel preferences; income, age and other factors may differ.",
    ),
    "Web engagement": (
        "Digital channel engagement", "NumWebVisitsMonth and NumWebPurchases",
        "Select aligned customer rows with complete numeric pairs. Create an XY scatter plot with web visits on the X-axis and web purchases on the Y-axis.",
        "Inspect unusual values, calculate correlation only when both variables vary, and report the number of pairs. Explain the association and propose a website investigation or test.",
        "Do not label purchases divided by monthly visits as conversion rate unless the measures cover compatible periods and units. Correlation does not establish cause.",
    ),
    "Response prediction": (
        "Promotional response prediction", "AcceptedCmp1–5 as potential predictors; Response as the target",
        "Confirm that campaign acceptance flags were known before the target response. First compare response rates by previous campaign acceptance and record group sizes.",
        "For predictive evaluation, reserve held-out customers before fitting preprocessing or tuning a classifier. Compare against the training-set majority-class baseline and report a confusion matrix, accuracy, precision and recall.",
        "Features recorded after the outcome cause data leakage. Do not tune on the final test set or treat retrospective performance as a guarantee of future campaign success.",
    ),
}


TASK_WORKFLOWS = {
    "7.2-task": {
        "title": "Product spending, retention and pricing",
        "deliverable": "Separate product spending, retention, channel, deals and profitability worksheets",
        "objectives": TASK_72_OBJECTIVES,
    },
    "7.3-task": {
        "title": "Customer insight, segmentation and campaign response",
        "deliverable": "Seven analysis worksheets: complaints, personas, response/spending, segments, household/channels, web engagement and response prediction",
        "objectives": TASK_73_OBJECTIVES,
    },
    "7.4-task": {
        "title": "Four evidence-based conclusions for the shareholders",
        "deliverable": "Choose four objectives from Tasks 7.2 and 7.3; write about half a page per objective with references to your analysis",
        "mode": "conclusions",
    },
}

CONCLUSION_OBJECTIVES = {**TASK_72_OBJECTIVES, **TASK_73_OBJECTIVES}
DEFAULT_CONCLUSION_OBJECTIVES = ["Response spending", "Detailed segments", "Household channels", "Web engagement"]
CONCLUSION_STEPS = (
    "Record the chosen objective, cleaned data version, filters and method. Refer to the analysis worksheet or chart that answers the objective.",
    "Copy one or two verified numerical findings with valid n, units and period. Explain their business meaning and an important limitation or alternative explanation.",
    "Write about half a page for the shareholders. Recommend a specific action or pilot, name an owner and define a follow-up KPI and comparison. State what further evidence is needed.",
)
CONCLUSION_SCAFFOLD = "We analysed […] using […], covering […] valid observations. The result was […] compared with […], documented in […]. This suggests […], although […]. We recommend […] for […]. […] should evaluate it over […] using […] against […]. Our conclusion is […], subject to […]."
ACTIVITY_WORKFLOWS = {
    "7.3.1": (
        "Airbnb: extend the exploratory analysis",
        "Continue your activity dataset and analyses from Activity 7.2.1, covering neighbourhood, price, room type and availability.",
        "Use defined groups, valid counts and consistent units. Compare distributions and unusual values, then record the evidence supporting each interpretation.",
        "Availability is a snapshot measure, not observed occupancy or a seasonal booking history. Price is not host profit.",
    ),
    "7.4.1": (
        "Activity: conclusions from the earlier EDA",
        "Use your own activity results from lessons 7.2 and 7.3. State the questions, data, scope and methods used.",
        "List supported conclusions and suggestions. Link each to a numerical finding, a table or chart, and a limitation. Propose how an action could be evaluated.",
        "Keep the activity dataset separate from the marketing task. Price is not host profit, and calendar availability is not observed occupancy.",
    ),
}


def get_task_display_title(guide):
    workflow = TASK_WORKFLOWS.get(guide["id"])
    if workflow:
        return workflow["title"]
    activity = ACTIVITY_WORKFLOWS.get(guide["id"])
    return activity[0] if activity else guide["title"]


def get_selected_conclusion_objectives(base_key):
    """Read the same four choices for the UI, download and AI context."""
    values = st.session_state.get(f"{base_key}_evo_conclusion_objectives", DEFAULT_CONCLUSION_OBJECTIVES)
    return [name for name in values if name in CONCLUSION_OBJECTIVES][:4]


def conclusion_guide_markdown(guide, selected_objectives):
    text = "### Task 7.4: Four evidence-based conclusions for the shareholders\n\n"
    text += "**Requirement:** Choose four different objectives from your analyses in Tasks 7.2 and 7.3. Write about half a page per objective and refer to the specific analysis supporting your recommendation.\n\n"
    text += f"**Dataset:** {guide['task_dataset']} — continue your cleaned data.\n\n**Workbook:** {guide['template_file']} — Conclusion 1, Conclusion 2, Conclusion 3, Conclusion 4.\n\n"
    text += "**Chosen objectives:** " + "; ".join(f"Conclusion {i}: {CONCLUSION_OBJECTIVES[name][0]} (evidence: {name})" for i, name in enumerate(selected_objectives, 1)) + ".\n\n"
    text += "**Evidence rule:** Use your actual results. Do not invent CLV, profit, complaint causes, causal effects or model performance. A recommendation is a proposal to evaluate, not proof of an effect.\n\n"
    if len(selected_objectives) != 4:
        text += "**Selection incomplete:** Choose four objectives before preparing the final response.\n\n"
    text += "**Procedure for each conclusion:**\n\n" + "\n".join(f"{n}. {step}" for n, step in enumerate(CONCLUSION_STEPS, 1)) + "\n\n"
    for i, name in enumerate(selected_objectives, 1):
        title, fields, _first, _second, caution = CONCLUSION_OBJECTIVES[name]
        text += f"#### Conclusion {i}: {title}\n\n**Evidence worksheet:** {name}\n\n**Relevant fields:** {fields}\n\n"
        text += f"**Check:** {caution}\n\n"
    text += f"**Writing template:** {CONCLUSION_SCAFFOLD}\n\n"
    text += f"[Original task and dataset on Noroff]({guide['source_url']}).\n\nThis is a study guide, not a solved dataset or an official solution."
    return text


def get_resolver_task_guide_markdown(guide, selected_objectives=None):
    """Keep the English download and the AI's task explanation consistent."""
    workflow = TASK_WORKFLOWS.get(guide["id"])
    if not workflow:
        activity = ACTIVITY_WORKFLOWS.get(guide["id"])
        if activity:
            title, first, second, caution = activity
            return f"### {guide['id']}: {title}\n\n1. {first}\n2. {second}\n3. Write a numerical finding, its interpretation, limitation and a justified next step.\n\n**Check:** {caution}\n\n[Original activity on Noroff]({guide['source_url']}).\n\nThis is an original working guide; use your own analysis."
        return guide["markdown"]
    if workflow.get("mode") == "conclusions":
        choices = DEFAULT_CONCLUSION_OBJECTIVES if selected_objectives is None else selected_objectives
        return conclusion_guide_markdown(guide, choices)
    objectives = workflow["objectives"]
    text = f"### Task {guide['lesson_number']}: {workflow['title']}\n\n"
    text += f"**Dataset:** {guide['task_dataset']}. Continue the cleaned task data; import the CSV separately. The workbook is a scaffold, not solved data.\n\n"
    text += f"**Workbook:** {guide['template_file']}\n\n"
    text += "**Worksheets:** " + ", ".join(objectives) + ".\n\n"
    for sheet, (objective, fields, first, second, caution) in objectives.items():
        text += f"#### {objective} — {sheet}\n\n**Fields:** {fields}\n\n1. {first}\n2. {second}\n3. Write one numerical finding, its interpretation and a limitation in your own words.\n\n**Check:** {caution}\n\n"
    text += "**Answer scaffold:** I examined […] using […]. The result was […] across […] valid observations. This suggests […]. The limitation is […]. I recommend […], evaluated using […].\n\n"
    text += f"[Original task and dataset on Noroff]({guide['source_url']}).\n\nThis is a study guide, not a solved dataset or an official solution."
    return text


def render_resolver_task_resources(guides, base_key, heading="### 2. Task guide and workbook", show_illustrations=True, guide_label="Resolver task"):
    """Put downloads and one readable procedure before the generated answer."""
    st.markdown(heading)
    for guide in guides:
        workflow = TASK_WORKFLOWS.get(guide["id"])
        with st.container(border=True):
            title = get_task_display_title(guide)
            st.markdown(f"**{guide['id']} · {title}**")
            if guide.get("task_dataset"):
                st.caption(f"Dataset: {guide['task_dataset']}")
            deliverable = workflow["deliverable"] if workflow else ("Evidence, interpretation, limitations and next steps" if guide["id"] in ACTIVITY_WORKFLOWS else guide["deliverable"])
            st.markdown(f"**Deliverable:** {deliverable}")
            st.markdown(f"[Open the original task and dataset on Noroff]({guide['source_url']})")
            template = TEMPLATE_ROOT / guide["template_file"]
            if template.is_file():
                st.download_button(
                    f"Download matched workbook: {template.name}", template.read_bytes(),
                    file_name=template.name,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key=f"{base_key}_evo_workbook_{guide['uid']}",
                )
                st.caption("The workbook is a scaffold. Import the task CSV into Raw and the cleaned copy into Prepared." if guide.get("task_dataset") else "Use the activity dataset and your own earlier analysis with this calculation scaffold.")
            choices = None
            if workflow and workflow.get("mode") == "conclusions":
                choices = st.multiselect(
                    "Choose four objectives from Tasks 7.2 and 7.3", list(CONCLUSION_OBJECTIVES),
                    default=DEFAULT_CONCLUSION_OBJECTIVES, max_selections=4,
                    format_func=lambda name: CONCLUSION_OBJECTIVES[name][0],
                    key=f"{base_key}_evo_conclusion_objectives",
                )
                st.caption(f"{len(choices)} of 4 objectives selected. Selection order assigns Conclusion 1–4.")
                if len(choices) != 4:
                    st.warning("Choose four objectives before preparing the final response. The guide below covers only your current selection.")
                if choices:
                    slot = st.selectbox("Choose a Task 7.4 conclusion", list(range(len(choices))),
                        format_func=lambda i, names=tuple(choices): f"Conclusion {i + 1}: {CONCLUSION_OBJECTIVES[names[i]][0]}",
                        key=f"{base_key}_evo_conclusion_slot")
                    name = choices[slot]
                    st.markdown(f"**Objective:** {CONCLUSION_OBJECTIVES[name][0]}")
                    st.markdown(f"**Write in the Excel worksheet `Conclusion {slot + 1}`**")
                    st.markdown(f"**Use evidence from `{name}`**")
                    st.caption(f"Relevant fields: {CONCLUSION_OBJECTIVES[name][1]}")
                    st.markdown("\n".join(f"{i}. {step}" for i, step in enumerate(CONCLUSION_STEPS, 1)))
                    st.info(CONCLUSION_OBJECTIVES[name][4])
                    with st.expander("Half-page writing template", expanded=False):
                        st.markdown(CONCLUSION_SCAFFOLD)
                st.caption("Start with verified results. The resolver can review your reasoning; missing evidence must remain explicit.")
            elif workflow:
                objectives = workflow["objectives"]
                sheet = st.selectbox(
                    f"Choose a Task {guide['lesson_number']} objective", list(objectives),
                    format_func=lambda name, items=objectives: items[name][0],
                    key=f"{base_key}_evo_objective_{guide['uid']}",
                )
                _objective_title, fields, first, second, caution = objectives[sheet]
                st.markdown(f"**Work in the Excel worksheet `{sheet}`**")
                st.caption(f"Fields: {fields}")
                st.markdown(f"1. {first}\n2. {second}\n3. Write one numerical finding, its interpretation and a limitation in your own words.")
                st.info(caution)
            else:
                activity = ACTIVITY_WORKFLOWS.get(guide["id"])
                if activity:
                    st.markdown(f"1. {activity[1]}\n2. {activity[2]}\n3. Write a numerical finding, its interpretation, limitation and next step.")
                    st.info(activity[3])
                else:
                    st.markdown("\n".join(f"{i}. {step}." for i, step in enumerate(guide["steps"], 1)))
            guide_text = get_resolver_task_guide_markdown(guide, choices)
            with st.expander(f"{guide_label} {guide['id']}: {title}", expanded=False):
                st.markdown(guide_text)
                st.download_button(
                    "Download matched task guide (Markdown)", guide_text.encode("utf-8"),
                    file_name=f"EVO-{guide['uid']}.md", mime="text/markdown",
                    key=f"{base_key}_evo_task_md_{guide['uid']}",
                )
    if not show_illustrations:
        return
    modules = {int(guide["lesson_number"].split(".")[0]) for guide in guides}
    numbers = {guide["lesson_number"] for guide in guides}
    with st.expander("Module illustrations for the matched tasks", expanded=False):
        st.caption("These images show lesson examples. Use the task's own dataset for calculations.")
        for lesson in get_evo_course_lessons():
            if lesson.get("illustration") and (lesson["lesson_number"] in numbers or (lesson["lesson_number"].endswith(".1") and lesson["module_number"] in modules)):
                path = ASSET_ROOT / lesson["illustration"]
                if path.is_file():
                    st.image(str(path), caption=lesson["illustration_caption"], width="stretch")
                    st.download_button(
                        "Download matched module illustration", path.read_bytes(),
                        file_name=path.name, mime="image/png",
                        key=f"{base_key}_evo_illustration_{lesson['lesson_number']}",
                    )
