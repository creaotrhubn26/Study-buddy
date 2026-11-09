"""Original English guide and learning templates for the Nice Ride reporting task."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
CHECKED_ON = "2026-11-09"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81722"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81727"
DATA_ROWS = [
    ("Mercedes", 220),
    ("Audi", 180),
    ("Volkswagen", 150),
    ("Skoda", 130),
    ("Volvo", 100),
    ("Tesla", 85),
]
TOTAL = sum(count for _, count in DATA_ROWS)
BOUNDARY = (
    "Task 2.2 concerns fictional car dealership Nice Ride. Create an MS Word report showing the most popular brand "
    "from the six supplied cars-sold counts: Mercedes 220, Audi 180, Volkswagen 150, Skoda 130, Volvo 100, Tesla 85. "
    "Use text formatting including different heading styles, a Column plot (vertical columns), and a short comment "
    "following the plot. Mercedes has the highest count, 220; total 865, and its lead over Audi is 40 cars. "
    "Most popular means highest recorded sales count within this supplied dataset. These are fictional aggregate "
    "counts, not national market share or proof of preference, causation, profitability or future demand. No reporting "
    "period, shop-level breakdown, prices, costs or customer-level data are supplied. Do not invent them. The brief "
    "specifies no word count, fixed page count, mandatory title page, table of contents, citation style, linked/embedded "
    "chart experiment, PowerPoint or imagegen-image submission. Keep the Word report proportionate to the quick-report "
    "request. The lesson's chocolate-bar workbook is a separate demonstration, not the car-sales task dataset. "
    "The workbook download is a Study Buddy learning aid with a native editable column chart; the Word template "
    "contains editable headings and placeholder prose plus a static chart picture, not a linked Excel object. If the "
    "source counts change, replace the Word picture and recheck the comment. Study images and written notes are not "
    "proof of completed Word work. Review the selected step and draft in English, flag missing evidence or placeholders, "
    "and have the learner inspect the actual saved report and submit it themselves."
)
RESOLVER_REQUEST = (
    "Review my Nice Ride report draft and check notes in English, following the selected Task 2.2 step. Verify all six "
    "supplied brand counts, the highest-sales conclusion, vertical column chart and short comment after the chart. "
    "Check that headings are planned as real Word styles and separate confirmed file checks from intended actions. "
    "Keep the interpretation within this fictional aggregate dataset; flag invented dates, shop comparisons, causes, "
    "profit or forecasts. Do not certify an unseen Word file or treat the template as my completed work. I will inspect "
    "the saved report and submit it myself."
)
STEPS = [
    (
        "1. Read the Nice Ride brief",
        "Open the original task. The manager wants a quick MS Word report about how many cars of each brand were sold and which brand is most popular in the supplied data. Record the four practical requirements: Word report, heading styles, a Column plot and a short comment after that plot. Use the six task counts, not the separate chocolate-bar lesson example.",
        "The task does not set a word or page count. A long report, PowerPoint, new survey or one-page article review is not required.",
    ),
    (
        "2. Enter and validate the six brand counts",
        "Use the downloadable CSV or workbook, or type a two-column Brand / Cars sold table in Excel. Check the exact pairs: Mercedes 220, Audi 180, Volkswagen 150, Skoda 130, Volvo 100, Tesla 85. In the supplied workbook these data are B10:C15, with headers in B9:C9. Preserve the original values and keep numerical cells as numbers.",
        "There are six brands and 865 cars in total. Do not include the total or summary cells as another brand in the chart. No individual shops or time periods are specified.",
    ),
    (
        "3. Identify the leading brand and keep the scope clear",
        "Compare the six counts. Mercedes is highest at 220, followed by Audi at 180, a difference of 40 cars. Tesla is lowest at 85. An optional calculation is Mercedes' share of these six-brand sales: 220 / 865 × 100, approximately 25.4%. Use this only if useful and name the denominator. Counts alone are enough to answer the task.",
        "Highest count is not a majority: 220 is less than half of 865. The data do not explain why a brand sold more, nor whether it earned more profit or was more available in stock.",
    ),
    (
        "4. Create a vertical column chart",
        "Select the Brand and Cars sold table including headers and all six data rows. Choose a two-dimensional clustered column chart in Excel. In the downloadable workbook the native chart is already linked to B9:C15; inspect its categories and values. Use brands on the horizontal axis and Cars sold on the vertical axis with a zero baseline. Keep all six labels readable and avoid 3D effects or a pie/line/horizontal-bar substitute.",
        "The six columns must match 220, 180, 150, 130, 100 and 85 in the displayed brand order. Check the chart source range; a total of 865 must not become a seventh column.",
    ),
    (
        "5. Structure the Word report and insert the chart",
        "Open the Word template or create a new Word report. Use a Title style for the document name and Heading 1 for sections such as Introduction, Sales by brand and Conclusion; use Heading 2 only where a real subsection helps. Explain the purpose and fictional dataset, then insert the verified column chart at a readable size. The supplied Word template already contains a static chart picture, with the numerical data available separately in Excel.",
        "Bold text alone is not a semantic heading style. A static chart picture can satisfy the plot requirement; linking or embedding an Excel workbook is not required. If using Word in a browser, insert a verified chart image if native chart tools are unavailable, then inspect the saved DOCX.",
    ),
    (
        "6. Write the short comment immediately after the plot",
        "State the main pattern using the actual counts, then give one useful comparison and a scoped interpretation. For example, Mercedes leads at 220, Audi follows at 180 and Tesla has 85. Explain that Mercedes is most popular by the supplied recorded sales, while the data do not establish why. Write your own concise paragraph after the chart; do not leave the template prompt or move the only explanation before the plot.",
        "Every numerical statement must match the source and chart. Do not add dates, trends, shop rankings, customer motives, profit or stocking recommendations that these aggregate counts do not support.",
    ),
    (
        "7. Reopen, check and review in Exam Resolver",
        "Save and reopen the actual Word file. Confirm heading styles, six chart categories and counts, vertical columns and zero baseline, readable placement and the short comment after the plot. Replace all bracketed template prose. If you changed workbook inputs, refresh or replace the static Word picture. Prepare Task 2.2 in Exam Resolver to review your current text and selected step in English; apply the feedback to the actual report and submit it yourself.",
        "Record actual checks as Done only after inspection. Resolver text feedback cannot certify unseen native formatting, final layout or source-chart consistency. Download your draft and keep the final DOCX yourself.",
    ),
]
SAMPLE_COMMENT = (
    "Mercedes recorded the highest sales in the supplied Nice Ride data, with 220 cars, compared with Audi's 180. "
    "Tesla had the lowest count at 85. Mercedes is therefore the most popular brand by recorded sales within this "
    "dataset. The figures do not establish the reasons for these differences."
)
CHECKS = [
    (
        "Source data",
        "All six brand/count pairs match the task; no invented dates or shop-level records.",
    ),
    (
        "MS Word file",
        "Saved DOCX reopened and all bracketed template prompts replaced.",
    ),
    (
        "Heading styles",
        "A readable heading hierarchy uses real Word styles, not only direct bold formatting.",
    ),
    (
        "Column plot",
        "Six vertical columns with correct labels/counts, zero baseline and no total column.",
    ),
    (
        "Comment placement",
        "A short explanation follows the plot and identifies Mercedes 220 with a supported comparison.",
    ),
    (
        "Scope",
        "No unsupported causes, profit claims, customer motives, forecasts or population-wide popularity claims.",
    ),
    (
        "Static chart picture",
        "If data changed, the Word picture and its explanation were updated and rechecked.",
    ),
]
QUESTION_TEMPLATE = """# ARP Task 2.2 Nice Ride report draft and checks

Working notes only. The task output is an MS Word report; complete and inspect the actual DOCX.

## Introduction
[State the manager's question and the scope of the six supplied fictional car-sales counts. No period or shop breakdown is provided.]

## Sales by brand
Source values: Mercedes 220; Audi 180; Volkswagen 150; Skoda 130; Volvo 100; Tesla 85.
[Insert the verified column plot in Word here.]

## Short comment after the plot
[Write your own concise interpretation: highest brand and count, one supported comparison, and scope/limitation.]

## Conclusion
[Answer which brand has the highest recorded sales in the supplied data. Avoid unsupported causal or business claims.]

## Data source
Noroff Analysis Reporting Task 2.2, fictional Nice Ride data:
https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81727

## Working file checks — remove these notes from the final report
Word file name and edition: [...]
All six original counts verified: [Not checked]
Title and heading styles inspected: [Not checked]
Vertical Column plot, six categories and zero baseline inspected: [Not checked]
Short comment follows plot and matches source: [Not checked]
Static Word picture replaced if workbook inputs changed: [Not checked]
Template prompts replaced and saved DOCX reopened: [Not checked]
Any unresolved issue and next action: [...]
I will inspect the actual report and submit it myself.
"""
REVIEW_CONTEXT = (
    "Checked Task 2.2 source facts: Nice Ride is fictional; aggregate Brand / Cars sold pairs are "
    + "; ".join(f"{b} {n}" for b, n in DATA_ROWS)
    + ". Total = 865; Mercedes is highest at 220, Audi second at 180, gap 40. Optional Mercedes share = 220/865, about 25.4%, not a majority. "
    "No period, shop-level data, causes, profit or forecasts are supplied. The required plot uses vertical columns; a short comment must follow it in Word. "
    "The Word template's chart is a static picture, whereas the Excel template's chart is native/editable. Recheck Word if inputs change. "
    f"Original task: {TASK_URL}. Study Buddy checked {CHECKED_ON}; this is not proof of learner file inspection."
)
ILLUSTRATIONS = [
    dict(
        file="lesson-2-2-data-to-report.png",
        title="From data to a clear report",
        caption="Start with purpose and reader, explain data and method, present findings, interpret them, answer the question and discuss justified action and limits. A story explains the data; it does not replace evidence. This is a conceptual lesson illustration.",
    ),
    dict(
        file="task-2-2-nice-ride-workflow.png",
        title="Nice Ride report workflow",
        caption="Seven learning steps lead from the brief and six brand counts to a Word report with heading styles, a vertical column plot and a short comment after it. Most popular means highest sales count in the supplied data. Icons and ticks describe requirements, not completed work; the chart icon is not a measured plot.",
    ),
]
DOWNLOADS = [
    (
        "ARP Task 2.2 Nice Ride Report Template.docx",
        "Download Nice Ride Word template (DOCX)",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ),
    (
        "ARP Task 2.2 Nice Ride Workbook.xlsx",
        "Download Nice Ride data and column chart (XLSX)",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ),
    ("ARP Task 2.2 Nice Ride Data.csv", "Download six brand counts (CSV)", "text/csv"),
    (
        "ARP Task 2.2 Report Draft and Checks.md",
        "Download report draft and checks (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.2 Verification Checklist.csv",
        "Download report verification checklist (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.2 Seven Step Guide.md",
        "Download seven-step Nice Ride guide (Markdown)",
        "text/markdown",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="2.2-task",
    uid="arp-2.2-task-81727",
    lesson_number="2.2",
    title="Nice Ride — Word report and column plot",
    source_url=TASK_URL,
    method="Data report with a column chart",
    deliverable="MS Word report identifying the most popular car brand, using heading styles, a Column plot and a short comment after the plot",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="ARP Task 2.2 Nice Ride Data.csv",
    template_file="ARP Task 2.2 Report Draft and Checks.md",
)
LESSON_CONTENT = """### Lesson 2.2 Creating Full-length Reports

A useful analysis report helps a reader answer a question with evidence. Its story connects the problem, data, findings and conclusion. It should make the reasoning easier to follow while keeping the evidence, uncertainty and scope visible. Full-length describes the lesson's wider reporting process; the Nice Ride task itself asks for a quick Word report.

### 1 Give the report a purpose and a reader

Define the question, audience and decision before choosing a layout. A manager usually needs a concise answer and the main evidence; a technical colleague may also need detailed methods and reproducible calculations. Begin with the problem's context, explain why the chosen data are relevant and state what the report covers. Do not invent a time period when none is supplied.

For Nice Ride, the manager asks which brand sold the most cars in the supplied fictional data. The evidence is six aggregate counts. There is no need to collect a new dataset or build a forecast to answer that question.

### 2 Build an evidence-led narrative

| Part | What it contributes | Main check |
|---|---|---|
| Title and introduction | Subject, purpose, context and scope | Reader can identify the question |
| Data and method | Source, units, preparation and approach | Another reader can trace the work |
| Findings | Relevant numerical results and visuals | Counts and chart match the source |
| Interpretation | What the findings mean in context | Inference stays within the evidence |
| Conclusion | A direct answer to the question | No unsupported new claim |
| Recommendations and limits | Proportionate action and remaining gaps | Advice is justified; uncertainty remains visible |

A report's setting is its decision context; variables and groups are the elements being compared. An anomaly or unanswered question can give the narrative direction. Use relatable examples only when they illuminate the analysis, and label hypothetical examples. Do not create drama by hiding inconvenient results or presenting a preferred explanation as a fact.

### 3 Move from a result to an insight carefully

A finding describes an observed value or comparison. An interpretation explains its meaning for the question. A recommendation proposes an action and needs further justification. For Nice Ride, Mercedes' 220 sales exceed Audi's 180 by 40. That supports a highest-sales conclusion for these data, but does not reveal stock availability, price, customer motives, profit or the best future purchasing strategy.

An increase after a website redesign, for example, does not by itself prove that the redesign caused the change. Consider timing, comparability and alternative explanations. Report uncertainty instead of using confident language to fill an evidence gap.

### 4 Choose visuals that support the question

A column chart compares category counts using vertical columns. Put brands on the horizontal axis and Cars sold on the vertical axis. A zero baseline preserves magnitude comparisons. Show all six task brands, use readable labels and a plain two-dimensional design, and exclude the total from the category list. A table can supplement the plot but does not replace the required Column plot. [Microsoft: column charts](https://support.microsoft.com/en-us/excel/present-your-data-in-a-column-chart).

Give the chart a descriptive title and explain its main pattern in a short paragraph after it. Readers should understand the unit and the conclusion without guessing. Avoid decorative graphics that compete with the evidence. The imagegen illustrations below explain the process; the actual Nice Ride chart is generated from the supplied numerical data.

### 5 Use Word styles and proportionate formatting

Use Word's Title and heading styles to create a hierarchy. Choose consistent fonts, spacing and alignment, and keep chart text readable in the saved document. [Microsoft's heading guidance](https://support.microsoft.com/en-us/word/add-a-heading-in-a-word-document) explains how styles support navigation, restructuring and contents lists. A table of contents or separate cover can help a longer document, but neither is prescribed for this short task.

Insert the chart from the verified workbook or use the supplied Word template's static chart picture. A picture is not a live Excel link: if inputs change, replace it and revise the comment. The task does not demand a linked/embedded-object experiment. In a browser edition, check the tools available and inspect the resulting DOCX after inserting a chart image.

### 6 Review clarity, ethics and sources

Use precise language and explain technical terms for the intended reader. Cite external ideas, data and images that you actually use. Record the original source of the supplied fictional counts; there is no prescribed referencing style or minimum citation count in this task. Do not imply that a learning illustration is a screenshot or evidence of completed analysis.

Acknowledge missing fields and limits. Aggregated data do not support a ranking of individual shops or customers. In real reports, protect personal information and explain relevant cleaning decisions. Ask a colleague to check calculations and reasoning where practical; collaboration is useful, but a group exercise is not required here.

### 7 Understand the demonstration and complete the task

The lesson demonstrates a chocolate-wrapper report using a separate fictional Excel workbook, followed by hypotheses, a chart, conclusions and a contents list. That is a demonstration of the reporting process. Task 2.2 instead supplies Nice Ride brand counts directly in the task page. Its required output is an MS Word report with heading styles, a Column plot, and a short comment following the plot.

Use the seven-step walkthrough and downloads below. The Word template includes a real data chart and editable structure, with bracketed prompts for your own prose. The Excel workbook contains the six counts and a native editable column chart. Keep the learning materials distinct from your final report, replace prompts and inspect the saved file yourself.
"""


def data_markdown():
    return "| Brand | Cars sold |\n|---|---:|\n" + "\n".join(
        f"| {b} | {n} |" for b, n in DATA_ROWS
    )


def guide_markdown():
    parts = [
        "# ARP Task 2.2 — seven-step Nice Ride guide",
        f"Original task: {TASK_URL}\n\nChecked {CHECKED_ON}. Original Study Buddy material, not the official solution.",
        "## Task boundary\n\n" + BOUNDARY,
        "## Supplied task data\n\n" + data_markdown(),
    ]
    parts.extend(f"## {t}\n\n{i}\n\nCheck: {c}" for t, i, c in STEPS)
    parts.extend(
        [
            "## Worked comment to study and adapt\n\n" + SAMPLE_COMMENT,
            "## Final file checks\n\n" + "\n".join(f"- {t}: {d}" for t, d in CHECKS),
        ]
    )
    return "\n\n".join(parts) + "\n"
