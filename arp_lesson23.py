"""Original study guidance for creating an evidence-based infographic in GIMP."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
CHECKED_ON = "2026-11-09"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81728"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81735"
KAGGLE_URL = "https://www.kaggle.com/datasets"
SAVE_URL = "https://docs.gimp.org/3.0/en/gimp-save-dialog.html"
JPEG_URL = "https://docs.gimp.org/3.0/en/file-jpeg-export.html"
BOUNDARY = (
    "Task 2.3 requires a dataset of the learner's choice from Kaggle, loaded into MS Excel for basic Exploratory Data "
    "Analysis (EDA), followed by an original infographic built in GIMP. Inspect the data structure, variables and "
    "patterns; use appropriate visualisations and identify supported observations. The brief offers histograms, "
    "scatter plots and bar charts as examples, not a requirement to include all three. Choose suitable canvas dimensions: "
    "800 × 1200 px is an example, not a fixed requirement; A4 belongs to the lesson demonstration. Save the editable "
    "GIMP project as .xcf and export the final infographic as JPEG .jpg. Cite external resources and keep the design "
    "original. No dataset, numerical findings, statistical significance or completed EDA is supplied by Study Buddy. "
    "Do not invent them or substitute another task's data. The brief specifies no word count, fixed number of charts, "
    "mandatory Word report, PowerPoint, 500-word essay or citation style. Data and image sources need traceable attribution "
    "and reuse checks; a public Kaggle listing does not by itself grant every reuse right. Correlation does not establish "
    "causation, and missing values are not automatically zeros. The optional .ora download is a six-layer OpenRaster "
    "layout guide with raster placeholder text, not native editable GIMP text, a completed .xcf or a final .jpg. Hide or "
    "replace guide layers, add actual charts and GIMP text layers, save .xcf and export .jpg. Its archive, layer images "
    "and preview were checked; opening in GIMP was not tested on this machine. The imagegen pictures are study aids, "
    "not evidence of learner EDA or a substitute for building the assigned GIMP project. Exam Resolver reviews the "
    "selected step and written evidence in English; it cannot certify unseen Excel calculations, GIMP layers or exports "
    "from notes. The learner inspects the actual files and submits them themselves."
)
RESOLVER_REQUEST = (
    "Review my Task 2.3 dataset plan, EDA evidence and infographic storyboard in English, following my selected step. "
    "Check the Kaggle provenance, Excel import/profile, actual calculations and appropriate chart choices. Trace each "
    "headline or number to recorded evidence and flag placeholders, missing data and unsupported causal claims. "
    "Explain the GIMP layer workflow, source credits and the difference between saving .xcf and exporting .jpg. "
    "Treat 800 × 1200 px as an example. Do not invent a dataset or findings, treat an imagegen illustration or the "
    "OpenRaster guide as completed student work, or certify unseen native files. I will inspect and submit my files myself."
)
STEPS = [
    (
        "1. Choose and document a Kaggle dataset",
        "Browse Kaggle and choose a dataset that interests you and can answer a focused question. Record creator, title, dataset URL, version/update date, original source if linked, licence or reuse terms, and the files selected. Define the audience and one provisional question. Check that the data are available and suitable before designing a headline.",
        "No dataset is preselected. Public availability is not proof of unlimited reuse rights, and a proposed question is not a finding.",
    ),
    (
        "2. Import and profile the data in Excel",
        "Download the chosen data and load it into MS Excel. Keep an original copy. Record rows, columns, what one row represents, variable types, units and any time/geographic scope. Check delimiters, decimal separators, date interpretation, missing values and potential duplicates. Log cleaning or filters and their reasons before analysing the data.",
        "Keep missing values separate from genuine zeros. Do not delete unusual observations or duplicate-looking rows without checking the data definition.",
    ),
    (
        "3. Explore, calculate and verify the evidence",
        "Use appropriate summaries and charts for your question: category counts or totals with a bar chart, a numerical distribution with a histogram, or two numerical variables with a scatter plot. Record the actual worksheet/range, formula or summary method, denominator, filters, sample size, chart file and observed result. Reconcile selected numbers against the source and note uncertainty or data-quality limits.",
        "The brief does not require every example chart or a statistical test. A correlation is not evidence that one variable caused another. Leave unperformed checks marked Not checked.",
    ),
    (
        "4. Plan the infographic message and layout",
        "Use the storyboard to organise an evidence-based headline, brief context, the relevant chart or charts, a short explanation, limits and sources. Decide a reading order and suitable canvas dimensions for the intended viewer. The optional 800 × 1200 px layout guide is a starting point; adapt or create your own design. Only write a final headline after the evidence supports it.",
        "A chart can be part of an infographic; there is no mandatory number of panels or charts. Keep the message understandable without spoken commentary and avoid overcrowding.",
    ),
    (
        "5. Build the infographic with GIMP layers",
        "Create a canvas in GIMP or open the optional OpenRaster .ora layout guide. Check its named layers. The guide contains raster text: hide or replace placeholder layers and create your own editable GIMP text layers. Import verified Excel chart images with Open as Layers, then scale proportionally. Add relevant, credited images/icons where useful and use consistent alignment, spacing, fonts and colours. Keep a visible background suitable for JPEG.",
        "The .ora helper is not a native .xcf or a completed infographic. Its text is not an editable GIMP text object. Check the imported layers in your GIMP edition before relying on the helper.",
    ),
    (
        "6. Check evidence, citations and readability",
        "Compare every displayed number, unit, denominator and label with the Excel evidence log. Check chart scales, category order, legible text, contrast and reading flow at the intended viewing size. Add traceable data and visual credits and retain licence/permission notes. Identify any AI-generated decorative visuals honestly; the learning images do not establish your results. Remove or hide all template prompts before export.",
        "Citing an image is not permission to reuse it. Use more than colour alone to convey an important distinction. A polished layout does not compensate for an unsupported claim.",
    ),
    (
        "7. Save XCF, export JPEG and inspect both files",
        "Use File > Save or Save As to save the GIMP working project as .xcf, then File > Export As to export a separate .jpg. Inspect the JPEG preview and choose settings that keep text and charts readable; the task gives no fixed quality number. Reopen the .xcf and check layers, then open the .jpg separately and inspect dimensions, clipping, legibility, credits and placeholder removal. Prepare Task 2.3 in Exam Resolver for English feedback on your evidence notes and selected step, make changes in the actual project and submit your files yourself.",
        "JPEG does not preserve layers or transparency. A file renamed from .png to .jpg is not a JPEG export, and a flattened image renamed .xcf is not an editable GIMP project. Written notes cannot prove these file checks were performed.",
    ),
]
CHECKS = [
    (
        "Dataset provenance",
        "Kaggle dataset URL, creator, version, original source and reuse terms are recorded.",
    ),
    (
        "Excel profile",
        "Actual row/column counts, row meaning, types, units, missingness and cleaning are documented.",
    ),
    (
        "EDA evidence",
        "Selected findings trace to actual ranges, methods, denominators, filters and checked calculations.",
    ),
    (
        "Visual integrity",
        "Chart type, labels, units, scale and sample are suitable; no invented or unsupported claims.",
    ),
    (
        "Original GIMP design",
        "Own charts and content replace the guide; named layers and editable text are inspected.",
    ),
    (
        "Credits and reading",
        "Data/visual credits, reuse conditions, contrast and readability are checked; prompts removed.",
    ),
    (
        "Two actual files",
        "The .xcf reopens with layers; the separately exported .jpg is readable and matches the project.",
    ),
]
LAYOUT_NOTE = (
    "Optional six-layer OpenRaster layout guide, 800 × 1200 px. Open it in GIMP, inspect the layers, hide/replace "
    "raster placeholder text and create your own GIMP text layers. Add your actual Excel charts and evidence, "
    "save the project as .xcf and export a separate .jpg. This download is neither final deliverable. "
    "The archive and preview were checked; a GIMP open/save round trip was not tested on this machine."
)
QUESTION_TEMPLATE = """# ARP Task 2.3 Infographic plan and evidence notes

Working template only. Choose your own Kaggle dataset, perform EDA in Excel and build the infographic in GIMP.

## Dataset and question
Creator, dataset title and Kaggle URL: [...]
Version/update date and files used: [...]
Original source and licence or reuse terms: [...]
Audience and question: [...]
Population, period, units and what one row represents: [...]

## Excel import and preparation
Actual rows and columns: [...]
Relevant variables and types: [...]
Missing values, duplicates and unusual values: [...]
Cleaning, filters and reasons, preserving the original: [...]

## Verified EDA evidence
Question and measure: [...]
Worksheet/range and actual formula or summary method: [...]
Denominator, sample size and filters: [...]
Chart type/file and observed finding: [...]
Independent check and limitations: [Not checked]
Do not turn a planned calculation or chart into a claimed result.

## Infographic storyboard
Evidence-based headline: [...]
Context and intended reading order: [...]
Chart(s), explanation and source credits: [...]
Canvas dimensions and reason: [...]
GIMP layer names and editable text plan: [...]
Optional .ora guide layers replaced or hidden: [Not checked]

## Export and final checks
Data and visual credits and reuse terms checked: [Not checked]
Numbers, scales, units, contrast and readability checked: [Not checked]
All placeholders removed: [Not checked]
Actual .xcf file saved and reopened with layers: [Not checked]
Actual .jpg exported, reopened and compared with project: [Not checked]
Unresolved issue and next action: [...]
I will inspect the actual files and submit them myself.
"""
STORYBOARD_TEMPLATE = """# Task 2.3 Infographic storyboard

No dataset, chart or finding is supplied. Adapt the structure to your actual evidence and audience.

1. Headline: [One supported message, written after EDA]
2. Context: [What is being measured, for whom, where and when the data support it]
3. Evidence panel: [Actual chart file, units, scale, denominator and relevant source]
4. Explanation: [What the result means for the question, with a relevant comparison]
5. Limit: [Missingness, sample, filters, uncertainty and what cannot be inferred]
6. Credits: [Traceable data and external visual references plus required attribution]

Canvas dimensions and reason: [...]
Reading order, font sizes, contrast and alignment: [...]
GIMP layer plan: Background / Charts / Headline / Explanation / Sources
Additional panels only when they help: [...]

## Using the optional .ora guide

The guide is 800 × 1200 px with six raster layers. It has no example data. In GIMP, inspect its layer stack, hide or replace guides, and add real text layers and verified chart images. Raster placeholder text is not editable with the Text tool. The panel backgrounds can be retained, changed or removed. Save your own .xcf and export a separate .jpg. The guide itself is neither final output, and its open/save behaviour was not tested in GIMP here.
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-2-3-chart-and-infographic.png",
        title="Chart and infographic",
        caption="A chart focuses on an analytical question; an infographic combines evidence, context, explanation and design into a visual message. A chart can be part of that message. Both formats can stand alone with clear context, labels and sources; multiple charts are not a fixed requirement.",
    ),
    dict(
        file="task-2-3-kaggle-to-gimp.png",
        title="From Kaggle data to a GIMP infographic",
        caption="Choose and document data, inspect it in Excel, verify EDA findings, plan the message, build GIMP layers, check sources/readability, then save .xcf and export .jpg. The 800 × 1200 px size is an example. The illustrated checks are process cues, not proof of completed learner work.",
    ),
]
DOWNLOADS = [
    (
        "ARP Task 2.3 Infographic Plan.md",
        "Download infographic plan and evidence notes (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.3 EDA Evidence Log.csv",
        "Download Excel EDA evidence log (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.3 Infographic Storyboard.md",
        "Download infographic storyboard (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.3 Source Register.csv",
        "Download data and visual source register (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.3 Infographic Layout.ora",
        "Download optional layered layout guide (ORA)",
        "image/openraster",
    ),
    (
        "ARP Task 2.3 Verification Checklist.csv",
        "Download GIMP and export checklist (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.3 Seven Step Guide.md",
        "Download seven-step infographic guide (Markdown)",
        "text/markdown",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="2.3-task",
    uid="arp-2.3-task-81735",
    lesson_number="2.3",
    title="Kaggle EDA and original GIMP infographic",
    source_url=TASK_URL,
    method="EDA infographic design and GIMP export",
    deliverable="Original infographic based on Excel EDA of a chosen Kaggle dataset, retained as an editable GIMP .xcf and exported as .jpg, with external resources cited",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file=DOWNLOADS[0][0],
)
REVIEW_CONTEXT = (
    "Checked Task 2.3 workflow: Kaggle dataset chosen by learner → MS Excel basic EDA and appropriate visualisations → "
    "original infographic made in GIMP → editable .xcf plus separately exported JPEG .jpg. No dataset or findings are "
    "preselected. Histograms, scatter and bar charts are examples, not all mandatory. Canvas 800 × 1200 px is an example, "
    "not a fixed requirement. Cite external data and visuals, check reuse terms, preserve limits and avoid causal claims "
    "from correlation. The optional six-layer .ora guide has raster placeholder text and is neither final output; create "
    "GIMP text layers, replace guides and save/export actual files. Archive/preview checked, no GIMP round-trip test. "
    f"Original task: {TASK_URL}. Save documentation: {SAVE_URL}. JPEG documentation: {JPEG_URL}. "
    "No file inspection or learner EDA is established by these source notes."
)
LESSON_CONTENT = """### Lesson 2.3 Generating Infographics

An infographic communicates a message through a deliberate combination of evidence, explanation and visual design. It should help a reader understand a topic quickly while preserving the meaning and limits of the information. Task 2.3 puts this into practice: choose data from Kaggle, explore them in Excel and create an original infographic in GIMP.

### 1 Understand what the format contributes

A chart can answer a focused question through position, length, colour or another visual encoding. An infographic places evidence into a broader reading structure with a headline, context, explanation and sources. A chart can be part of an infographic, but there is no universal rule requiring several charts. A well-labelled chart can stand alone, and an infographic can contain one main visual. Static versus interactive is also not a strict boundary between the formats.

Examples include a weather overview combining location, symbols and temperatures, or a transport guide joining routes with relevant landmarks. The design should prioritise the information rather than decoration. Help the reader compare values, move from overview to detail and understand the purpose without relying on spoken commentary.

### 2 Start with the question and trustworthy data

Choose an audience and a manageable question. Inspect the dataset creator, description, version, scope, units and reuse terms. Kaggle hosts datasets with different origins and licences; a listing is a starting point for checking provenance, not an automatic guarantee of quality or permission.

For this task, download your chosen dataset and load it into MS Excel. Keep the original and record what each row represents. Check variable types, missing values, duplicates, filters and the interpretation of dates or decimal separators. A visually plausible import can still have numerical columns stored as text. Record cleaning decisions rather than silently changing the population being described.

### 3 Use EDA to find a supported message

| Question | Possible evidence | Main check |
|---|---|---|
| How are categories represented? | Counts or a suitable aggregate and bar chart | Comparable groups and correct denominator |
| How is a numerical variable distributed? | Summary statistics and histogram | Units, bins, missing values and unusual observations |
| Are two numerical variables related? | Scatter plot and an appropriate numerical summary | Sample, filters, outliers and correlation limits |
| How does a measure vary over time? | Time-ordered summary and line chart, if dates exist | Actual date coverage and comparable intervals |

These are choices, not a mandatory list of charts. Select evidence that answers your question. Do not invent a trend, correlation, p-value or recommendation because the planned layout has a space for one. Keep an evidence log linking each proposed claim to the actual calculation, chart, sample, denominator and limitation. A correlation does not establish causation.

### 4 Plan a visual story that can be read alone

Use a storyboard before detailed editing. Give the reader a supported headline, brief context, the useful evidence, an explanation and a relevant limit. Put sources where they remain readable. Choose a sensible reading order, alignment and spacing. Use colour consistently and avoid relying only on red versus green or colour alone to identify an important distinction.

Choose canvas size for the intended use. The task gives 800 × 1200 px as an example, while the lesson demonstration uses A4. Neither is a universal requirement. Pixel dimensions determine the available detail; changing a resolution label alone does not add pixels. Check the infographic at its intended viewing size and avoid cramming in small text.

### 5 Choose tools for their role

Word processors and presentation tools can arrange text and visuals, BI tools help analyse and present data, and graphics editors provide composition and image controls. Capabilities and export options vary by version. A chart need not always be drawn elsewhere, and commercial software does not automatically make a better infographic.

The assigned workflow here is Excel for EDA and GIMP for the infographic. In GIMP, use named layers for the background, chart images, headline, explanation and source credits. Import verified chart images using Open as Layers, preserve their proportions and check label readability after resizing. Add images or icons only when they clarify the message, and check their source and permitted use.

The optional OpenRaster layout guide provides six raster layers at 800 × 1200 px. Its placeholder text is not native editable GIMP text. Hide or replace those guide layers and create actual text layers with GIMP's Text tool. Check the imported layers in your installed edition. The guide is a composition aid, not a finished infographic or saved GIMP project.

### 6 Keep attribution and visual integrity visible

Record the data creator, dataset title, version, original source and URL. For external images and icons, retain creator, source, licence or permission and the attribution actually required. A reference does not itself grant reuse permission. Use the source register to distinguish data, charts you made from those data, and externally sourced visuals.

Reconcile displayed numbers to Excel, including units, filters and denominators. Check category labels, scale and any rounding. A simplified explanation must still preserve the result. Label uncertainty rather than presenting an incomplete sample as an entire population. The two imagegen illustrations in Study Buddy explain the workflow; they do not contain your EDA results or replace the assigned GIMP work.

### 7 Save an editable project and a separate final image

Use GIMP's Save/Save As workflow for the .xcf project, which retains the working layer structure. Export the final image separately as .jpg and inspect the export. JPEG does not retain layers or transparency; check the visible background and whether compression makes text or chart lines hard to read. There is no fixed quality setting in the task. See the [GIMP Save documentation](https://docs.gimp.org/3.0/en/gimp-save-dialog.html) and [JPEG export guidance](https://docs.gimp.org/3.0/en/file-jpeg-export.html).

Reopen both actual files: check the .xcf layer stack and the final .jpg's readability, dimensions, credits and agreement with the project. Renaming an extension does not convert a file. The brief asks for original work and cited external resources; it does not prescribe a separate Word report or PowerPoint. Use Exam Resolver to review your selected step, evidence notes and storyboard in English, then make and inspect changes in the real files yourself.
"""


def guide_markdown():
    parts = [
        "# ARP Task 2.3 — seven-step infographic guide",
        f"Original task: {TASK_URL}\n\nChecked {CHECKED_ON}. Original Study Buddy guidance, not an official solution.",
        "## Task boundary\n\n" + BOUNDARY,
    ]
    parts.extend(f"## {t}\n\n{i}\n\nCheck: {c}" for t, i, c in STEPS)
    parts.extend(
        [
            "## Optional layout guide\n\n" + LAYOUT_NOTE,
            "## Final checks\n\n" + "\n".join(f"- {t}: {d}" for t, d in CHECKS),
        ]
    )
    return "\n\n".join(parts) + "\n"
