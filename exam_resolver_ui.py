"""Compact task resources shared by the Universal Exam Resolver."""

import streamlit as st

from evo_curriculum import ASSET_ROOT, get_evo_course_lessons
from evo_tasks import TEMPLATE_ROOT


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


def render_resolver_task_resources(guides, base_key):
    """Put downloads and one readable procedure before the generated answer."""
    st.markdown("### 2. Task guide and workbook")
    for guide in guides:
        with st.container(border=True):
            title = "Product spending, retention and pricing" if guide["id"] == "7.2-task" else guide["title"]
            guide_text = guide["markdown"]
            if guide["id"] == "7.2-task":
                guide_text = "### Task 7.2: Product spending, retention and pricing\n\n"
                guide_text += "**Dataset:** marketing_campaign_fixed.csv. Import the task CSV separately; the workbook is a scaffold.\n\n"
                for sheet, (objective, fields, first, second, caution) in TASK_72_OBJECTIVES.items():
                    guide_text += f"#### {objective} — {sheet}\n\n**Fields:** {fields}\n\n1. {first}\n2. {second}\n\n**Check:** {caution}\n\n"
                guide_text += "**Answer scaffold:** I examined […] using […]. The result was […] across […] valid observations. This suggests […]. The limitation is […]. I recommend […], evaluated using […].\n\n"
                guide_text += f"[Original task and dataset on Noroff]({guide['source_url']}).\n\nThis is a study guide, not a solved dataset or an official solution."
            st.markdown(f"**{guide['id']} · {title}**")
            if guide.get("task_dataset"):
                st.caption(f"Dataset: {guide['task_dataset']}")
            deliverable = "Separate product spending, retention, channel, deals and profitability worksheets" if guide["id"] == "7.2-task" else guide["deliverable"]
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
                st.caption("The workbook is a scaffold. Import the task CSV into Raw and the cleaned copy into Prepared.")
            if guide["id"] == "7.2-task":
                sheet = st.selectbox(
                    "Choose a Task 7.2 objective", list(TASK_72_OBJECTIVES),
                    format_func=lambda name: TASK_72_OBJECTIVES[name][0],
                    key=f"{base_key}_evo_objective_{guide['uid']}",
                )
                _objective_title, fields, first, second, caution = TASK_72_OBJECTIVES[sheet]
                st.markdown(f"**Work in the Excel worksheet `{sheet}`**")
                st.caption(f"Fields: {fields}")
                st.markdown(f"1. {first}\n2. {second}\n3. Write one numerical finding, its interpretation and a limitation in your own words.")
                st.info(caution)
            else:
                st.markdown("\n".join(f"{i}. {step}." for i, step in enumerate(guide["steps"], 1)))
            with st.expander(f"Resolver task {guide['id']}: {title}", expanded=False):
                st.markdown(guide_text)
                st.download_button(
                    "Download matched task guide (Markdown)", guide_text.encode("utf-8"),
                    file_name=f"EVO-{guide['uid']}.md", mime="text/markdown",
                    key=f"{base_key}_evo_task_md_{guide['uid']}",
                )
    modules = {int(guide["lesson_number"].split(".")[0]) for guide in guides}
    with st.expander("Module illustrations for the matched tasks", expanded=False):
        st.caption("These images show lesson examples. Use the task's own dataset for calculations.")
        for lesson in get_evo_course_lessons():
            if lesson.get("illustration") and lesson["module_number"] in modules:
                path = ASSET_ROOT / lesson["illustration"]
                if path.is_file():
                    st.image(str(path), caption=lesson["illustration_caption"], width="stretch")
                    st.download_button(
                        "Download matched module illustration", path.read_bytes(),
                        file_name=path.name, mime="image/png",
                        key=f"{base_key}_evo_illustration_{lesson['module_number']}",
                    )
