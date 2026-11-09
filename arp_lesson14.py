"""Original guide to Task 1.4: Word visuals, chart experiments and native-file checks."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81699"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81707"
CHECKED_ON = "2026-11-09"
SOURCE_BASE = "https://learning.noroff.no/pluginfile.php/33187/mod_book/chapter/81707/"
RESOURCE_LINKS = [
    ("Q1 original Excel workbook", SOURCE_BASE + "LessonTasksChart%20%281%29.xlsx"),
    ("Q1 original Word document", SOURCE_BASE + "LessonTasks%20%281%29.docx"),
    ("Q2 original Excel workbook", SOURCE_BASE + "LessonTasksChart%20%282%29.xlsx"),
    ("Q2 original Word document", SOURCE_BASE + "LessonTasks%20%282%29.docx"),
    ("Q3 original Word document", SOURCE_BASE + "LessonTasks%20%283%29.docx"),
    (
        "Q3 original equation image",
        SOURCE_BASE + "Lessontaskincorporatingvisualisations-1.jpg?time=1769678840084",
    ),
    ("Q4 original Word document", SOURCE_BASE + "LessonTasks%20%284%29.docx"),
]
TARGET_EDITS = [("Male users", "March", 45892), ("Female users", "December", 91364)]
TABLE_ROWS = [
    ("John", 30, "New York"),
    ("Alice", 25, "Los Angeles"),
    ("Bob", 28, "Chicago"),
]
EQUATION_NOTE = (
    "The supplied Q3 image contains two equation displays. The first shows a stacked fraction with denominator 3 "
    "and 2a following outside the fraction. The second uses inline/slash division by 2a, with unclear grouping. "
    "These are not unambiguously the same expression. Reproduce the supplied displays in Equation Editor and "
    "confirm unclear grouping with the tutor. Do not silently change the denominator 3 or substitute the conventional "
    "quadratic formula with denominator 2a. No values of a, b or c are supplied and no numerical roots are requested."
)
BOUNDARY = (
    "Task 1.4 has four questions. Q1 inserts the supplied chart at the end of the supplied Word document, changes "
    "male users in March to 45892 and female users in December to 91364 in Excel, and observes whether changes appear. "
    "A linked chart is the lesson-based Q1 workflow interpretation; the brief itself says insert, not explicitly link. "
    "Q2 explicitly embeds the chart at the end, makes the same external Excel edits and records observations. "
    "Use independent baseline copies: linked content may refresh from an accessible source, whereas an embedded "
    "workbook is a separate editable copy and external workbook edits should not update it. A picture is static, "
    "not an embedded chart. Do not claim either experiment has been performed from expected behaviour alone. "
    "Q3 requires a separate table with Name, Age, Location and John/30/New York, Alice/25/Los Angeles, Bob/28/Chicago, "
    "plus the equations in the original image. " + EQUATION_NOTE + " "
    "Q4 uses the document created in the preceding activities to generate separate lists of figures, tables and equations. "
    "Use matching caption labels and update all three lists. Different numbered source links are provided; do not assume "
    "those files are identical or replace them with the lesson's separate Report.docx demonstration. "
    "The brief does not specify a report word count, fixed page number, font, screenshot submission or a new PowerPoint. "
    "Desktop Office features are needed for the documented native chart embedding/linking workflow; Word for the web "
    "does not provide the same embedded-object tools. Confirm desktop access or a tutor-approved alternative. "
    "Exam Resolver reviews written plans and check notes in English; it cannot certify native chart relationships, "
    "refresh results, equation objects or caption fields from notes or generated images. The learner verifies the saved files and submits them."
)
RESOLVER_REQUEST = (
    "Review my Task 1.4 plan and actual check notes in English, following the selected step. Keep Q1 and Q2 experiments "
    "and baseline files separate. Check the two exact Excel target edits, Q3 table rows and equation-image ambiguity, "
    "and Q4's three caption-based lists. Distinguish expected behaviour from my recorded observations and identify "
    "Office edition limits. Do not claim to create or verify native links, embedded objects, equations or lists from "
    "these notes, and do not silently correct the supplied equations. I will inspect and submit the actual Office files myself."
)
STEPS = [
    (
        "1. Inspect the brief, files and Office edition",
        "Open the original task and its numbered file links below while signed in to Noroff. Preserve originals and create separate Q1 and Q2 working copies before changing data. Record the actual file names, locations, chart/worksheet used and starting values; the guide does not invent cell addresses. Check desktop Word/Excel access. Word for the web supports basic tables and equations, but not the same native Excel embedded-object workflow.",
        "The lesson's Report.docx is a demonstration, not the Task 1.4 working file. No original Noroff file is hosted in this public app; download it from Noroff. If desktop features are unavailable, record the issue and ask the tutor about an acceptable alternative.",
    ),
    (
        "2. Q1 — insert, link and test the source edits",
        "At the end of the Q1 Word working copy, paste the required chart using an explicit Link Data option in a supported desktop Office edition. This is the lesson-based interpretation of Q1's insertion experiment. Record the baseline, then change male users in March to 45892 and female users in December to 91364 in the external Excel working file. Save it, refresh/update the Word chart if needed, and inspect the actual plotted data or chart data. Record what happened for both values.",
        "Expected: a valid linked chart can reflect source changes after a successful refresh. That is not a recorded result. If nothing changes, check the actual paste type, chart source range, saved workbook path and refresh status. A visual change alone does not prove the intended source relationship.",
    ),
    (
        "3. Q2 — embed an independent copy and test again",
        "Start with a separate baseline workbook and Word copy so Q1's edits do not pre-populate this experiment. Paste the chart at the end using Embed Workbook, not Link Data or Picture. Record its baseline, then make the same two edits in the external Q2 Excel workbook and save. Inspect the embedded chart and its internal data, using Edit Data where available. Compare the embedded copy with the changed external workbook and record both observations.",
        "Expected: external Excel changes do not update the embedded copy. Its internal data can be edited separately. If the baseline already contained target values, no visible change is an inconclusive test; restore a clean baseline before repeating. A screenshot alone cannot distinguish an embedded chart from a static picture.",
    ),
    (
        "4. Q3 — create the separate data table",
        "In the Q3 document, insert a native Word table with three columns and four rows including the header. Enter Name | Age | Location, then John | 30 | New York, Alice | 25 | Los Angeles, and Bob | 28 | Chicago. The downloadable CSV is a typing/checking aid; importing or pasting it does not itself prove a native table was created. Keep the table readable and align its columns consistently.",
        "Check every name, age and location against the brief. Use the Table caption label when preparing Q4; a caption is separate from the header row. The task does not prescribe a table style or a fixed page position.",
    ),
    (
        "5. Q3 — enter and inspect the supplied equations",
        "Open the original equation image below. Use Insert > Equation, building fraction, radical, superscript and plus/minus structures to reproduce both displays as editable equations. The image's first denominator is 3 with 2a outside the fraction; the second uses slash division by 2a with unclear grouping. Record any interpretation and confirm it with the tutor rather than silently replacing the image with the usual quadratic formula. This is an equation-entry exercise, not a request to solve numerical roots.",
        "Compare numerator, denominator, square-root scope, exponent 2, ± sign and placement of 2a to the source. No a, b or c values are supplied. Current Word web offers an equation tool, but availability and controls should be checked in your edition. Use desktop Word if the needed structure or caption tools are missing.",
    ),
    (
        "6. Q4 — add captions and generate three lists",
        "Use the document assembled in the preceding activities; also inspect Q4's separately linked document before deciding how to carry work forward. Give charts/illustrations Figure captions, the native data table a Table caption and each equation an Equation caption using References > Insert Caption in desktop Word. Insert three separate lists through References > Insert Table of Figures, selecting Figure, Table and Equation respectively. Update each entire list after final layout changes.",
        "The labels in the objects and list settings must match. Include every relevant caption in the final document, not an invented fixed total. Typing three headings or copying a screenshot is not generating caption-based lists. Confirm entries and page numbers in the saved copy.",
    ),
    (
        "7. Reopen, document observations and review",
        "Save and reopen your working Office files. Check chart placement, actual linked/embedded object type, the two external Excel edits, recorded before/after observations, the native table, both equation objects and all three updated lists. Record unresolved features or equation ambiguity. Prepare Task 1.4 in Exam Resolver to review your notes in English. Make final changes in the actual files and submit them yourself according to the course instructions.",
        "The task does not require a new essay, PowerPoint, fixed page count or screenshot submission. Learning images and a plan are not proof that an Office experiment was completed. Preserve the linked source workbook and its usable path if sharing a linked document.",
    ),
]
QUESTION_BRIEFS = [
    (
        "Q1 · Insert and observe",
        "Place the chart at the end, edit male/March to 45892 and female/December to 91364 in Excel, and observe whether changes appear. Explicit linking is the lesson-based method, not an extra quoted instruction.",
    ),
    (
        "Q2 · Embed and observe",
        "Embed the chart at the end, make the same external Excel edits, and record what happens. Use an independent baseline to make the test meaningful.",
    ),
    (
        "Q3 · Table and equations",
        "Create the specified Name/Age/Location table and enter both equations from the source image. Confirm unclear mathematical grouping instead of silently correcting it.",
    ),
    (
        "Q4 · Three separate lists",
        "Generate lists of figures, tables and equations from matching captions in the document built during the preceding activities.",
    ),
]
CHECKS = [
    (
        "Q1 chart and source",
        "Chart is at the end; actual linked object/paste type and workbook path are checked.",
    ),
    ("Q1 target edits", "External Excel male/March = 45892; female/December = 91364."),
    (
        "Q1 observations",
        "Before/after values and refresh result are observed, not merely predicted.",
    ),
    (
        "Q2 independent baseline",
        "A clean copy was embedded before changing its external workbook.",
    ),
    (
        "Q2 embedded copy",
        "Editable embedded data is separate from external edits; object is not just a picture.",
    ),
    (
        "Q3 data table",
        "Header and John/30/New York, Alice/25/Los Angeles, Bob/28/Chicago are exact.",
    ),
    (
        "Q3 equations",
        "Both editable displays match the source; denominator/grouping ambiguity is recorded or clarified.",
    ),
    (
        "Q4 captions",
        "Relevant objects have matching Figure, Table or Equation caption fields.",
    ),
    (
        "Q4 three lists",
        "Separate figures, tables and equations lists contain correct entries and updated pages.",
    ),
    (
        "Saved files",
        "Office files reopened; path/edition issues and any unverified result remain explicit.",
    ),
]
QUESTION_TEMPLATE = """# ARP Task 1.4 Office workflow and check notes

Learning/check template only. Edit and inspect the original task files in Office; these notes are not completed Word or Excel files.

## Files and edition
Word edition/version: [...]
Excel edition/version: [...]
Desktop features available or tutor-approved alternative: [...]
Originals preserved: [Not checked]
Q1 workbook, Word file, worksheet/chart and source path: [...]
Q2 independent baseline workbook and Word file: [...]
Q3 working document: [...]
Q4 supplied document inspected and preceding work carried forward: [...]

## Q1 insertion/link experiment
Actual paste option/object type: [...]
Baseline male/March value: [...]  Baseline female/December value: [...]
External Excel targets: male/March 45892; female/December 91364
Actual values entered/saved: [...]
Refresh/update action and source path checked: [...]
Observed Word chart/data values afterwards: [...]
Conclusion supported by those observations: [...]
Expected behaviour alone is not an observation. Explicit linking is a lesson-based Q1 interpretation.

## Q2 embedding experiment
Independent baseline recorded before external edits: [...]
Actual Embed Workbook option/object check: [...]
Embedded male/March baseline: [...]  Embedded female/December baseline: [...]
External Excel targets: male/March 45892; female/December 91364
Actual changed external values: [...]
Observed embedded values after external changes: [...]
Internal Edit Data checked, distinct from Picture or Link Data: [...]
Conclusion and any inconclusive same-value baseline: [...]

## Q3 table
Name | Age | Location
John | 30 | New York
Alice | 25 | Los Angeles
Bob | 28 | Chicago
Native three-column/four-row table checked: [Not checked]

## Q3 equations
Original image inspected: [Not checked]
First display: stacked fraction denominator 3, followed by 2a outside the fraction.
Second display: inline/slash division by 2a, with unclear grouping.
Both editable Equation Editor objects entered and compared: [Not checked]
Radical scope, ±, exponent, numerator/denominator and placement of 2a: [...]
Any working interpretation and tutor clarification: [...]
Do not silently replace the source with the conventional quadratic formula. No numerical roots are requested.

## Q4 captions and lists
Figure captions checked: [Not checked]
Table captions checked: [Not checked]
Equation captions checked: [Not checked]
Separate List of Figures generated and updated: [Not checked]
Separate List of Tables generated and updated: [Not checked]
Separate List of Equations generated and updated: [Not checked]
Entries, page numbers and matching labels in saved copy: [...]

## Final native-file review
Files saved, closed and reopened: [Not checked]
Actual Office observations checked against the four questions: [Not checked]
Linked source path remains usable: [Not checked]
Unresolved issue, unavailable feature or ambiguity: [...]
Next action: [...]
I will review the actual files and submit them myself.
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-1-4-linked-embedded-picture.png",
        title="Linked, embedded or picture?",
        caption="A linked chart can refresh from an accessible source workbook. An embedded chart has its own editable copy of the data and does not follow external edits. A picture is a static snapshot. Actual results depend on the pasted object, source path, refresh and Office edition; this image is conceptual, not test evidence.",
    ),
    dict(
        file="task-1-4-four-question-workflow.png",
        title="Four questions, one clear workflow",
        caption="Use separate Q1/Q2 baselines for chart experiments; enter the supplied table and equation displays in Q3; add captions and generate separate figures, tables and equations lists for Q4. The Excel target edits are male/March 45892 and female/December 91364. Explicit linking is the lesson-based Q1 method. These are required edits and expected behaviours, not recorded results.",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="1.4-task",
    uid="arp-1.4-task-81707",
    lesson_number="1.4",
    title="Incorporating Visualisations — four Office questions",
    source_url=TASK_URL,
    method="Office chart integration and native-file verification",
    deliverable="The task's Office document work: two chart experiments, a table and equations, and three caption-based lists",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file="ARP Task 1.4 Office Workflow and Checks.md",
)
LESSON_CONTENT = """### Lesson 1.4 Incorporating Visualisations

A report needs visuals that answer its questions and remain readable in the final document. This lesson connects chart selection, Excel-to-Word paste behaviour, object layout, captions, object lists and editable equations. Task 1.4 is practical Office work with four questions, not a new written analysis report.

### 1 Match the visual to the question

| Visual | Useful for | Main check |
|---|---|---|
| Bar chart | Comparing categories | Meaningful order, readable labels and a suitable baseline |
| Line chart | Change over ordered time | Correct time order, units and intervals |
| Pie chart | A simple part-to-whole composition | Parts share one meaningful total; avoid too many slices |
| Scatter plot | Relationship between two numerical variables | A pattern does not establish causation |
| Histogram | Distribution of a numerical variable | Explain bins; unlike a bar chart, bars represent numerical intervals |
| Bubble chart | Two coordinates plus a third numerical measure | Bubble area and legend must be understandable |
| Area chart | Magnitude or composition over ordered time | Overlap/stacking can make comparison difficult |

Name the measure and unit, explain the important pattern and retain relevant limitations. Do not invent a result because the chart looks convincing. The two numbers in Task 1.4 are prescribed input edits; no original cell addresses, initial values or observed chart results are supplied in this guide.

### 2 Distinguish linking, embedding and pictures

| Object in Word | Where the chart data comes from | What an external Excel change means |
|---|---|---|
| Linked chart | The source workbook | Can update when the source is accessible and the link is refreshed successfully |
| Embedded chart | A copy stored inside the Word document | Does not change the embedded copy; its internal workbook can be edited separately |
| Picture | Saved pixels/vector appearance | No editable chart data or live source connection |

Choose an explicit paste option. In supported desktop Office, **Link Data** and **Embed Workbook** have different meanings; source/destination formatting choices mainly control appearance. A hyperlink to an XLSX file is not a linked chart object. A picture pasted into Word is not proof of chart embedding. Ordinary paste can choose a default that depends on the item and edition, so inspect the object rather than relying only on Ctrl+V. [Microsoft: chart paste choices](https://support.microsoft.com/en-us/excel/insert-a-chart-from-an-excel-spreadsheet-into-word).

A normal Word table copied from cells can be editable without containing an embedded Excel workbook. Do not call every non-linked pasted table an Excel object. [Microsoft: linked and embedded objects](https://support.microsoft.com/en-au/word/linked-objects-and-embedded-objects) explains the underlying storage distinction.

### 3 Make the comparison a real experiment

For Q1, the lesson-based workflow uses a linked chart at the end of the document. Record baseline values before changing male users in March to **45892** and female users in December to **91364** in the external workbook. Save, refresh if necessary and inspect what actually changed. A broken path, wrong source range or picture paste can explain an apparent failure to update.

For Q2, start with an independent baseline and embed a separate copy **before** changing the external workbook. Its internal data should retain its baseline when only the external file changes. If you embed after applying the targets, an unchanged display proves little because both already contain those values. Record before/after data for both experiments. Expected behaviour belongs in a prediction; only observed behaviour belongs in the results column.

Keep linked source files accessible. Renaming, moving or sharing only the Word file can break a link. A stable local working folder can make a desktop experiment easier to inspect; do not generalise the lesson's OneDrive warning into a claim that all cloud-linked workflows always fail.

### 4 Use tables and layout to support reading

Insert the Q3 data as a native table, including a header row. Choose clear alignment and adequate column widths; keep text and figures readable at the saved page size. Inline objects behave like characters in a paragraph. Floating objects use wrapping and positioning settings; Square, Tight, Through, Top and Bottom, Behind Text and In Front of Text serve different needs. Inspect the actual result rather than assuming one wrapping style suits every object.

Move with Text lets an object follow its anchor as content changes; Fix Position affects its page position. Preserve aspect ratio when resizing charts and images. A small chart may fit beside text, while a dense chart needs more space. Avoid covering text or separating a caption from the object it explains. Placement choices in the lesson demonstrations are not extra mandatory page numbers for the task; Q1 and Q2 specifically say the chart goes at the end.

### 5 Build captions before object lists

A caption identifies an object and provides a stable numbered label. In desktop Word, select the object and use **References > Insert Caption**, choosing **Figure**, **Table** or **Equation** to match its kind. Charts normally use Figure. Follow any specified institutional caption position; placement is not universal. A typed header row is not a table caption.

To create the lists, use **References > Insert Table of Figures** three times with the corresponding caption label: one list for figures, one for tables, one for equations. The command's name does not mean every resulting list must contain figures. Update each entire list after captions or layout change, then check entries and page numbers. A manually typed list or screenshot is not the same generated field. The number of entries depends on the actual final document. [Microsoft: captions](https://support.microsoft.com/en-us/word/add-format-or-delete-captions-in-word) · [Microsoft: table of figures](https://support.microsoft.com/en-us/word/insert-a-table-of-figures).

### 6 Reproduce equations without silently changing them

Use Equation Editor to make editable mathematical structures: fractions, superscripts, radicals, operators and ±. Check grouping as carefully as character appearance. A stacked fraction fixes which terms lie above and below the bar; inline slash notation needs clear parentheses to communicate the intended division.

The Q3 source image has two displays. The first visibly has **3 as the stacked denominator and 2a outside the fraction**. The second uses slash division by **2a**, with unclear grouping. They should not be silently rewritten as the familiar quadratic formula. Open the original image, reproduce its structures, record any interpretation and ask the tutor to clarify ambiguity. There are no numerical a, b or c values to solve for. [Microsoft: equation structures](https://support.microsoft.com/en-us/word/training/write-an-equation-or-formula).

### 7 Check Office edition limits

Your Microsoft 365 browser workflow supports ordinary tables and an equation builder, but Microsoft's comparison lists native **Embedded Objects** as a desktop feature. Use supported desktop Word/Excel for the documented chart link/embed experiments, and check caption/list tools in your edition. If desktop access is unavailable, record that limitation and confirm an acceptable alternative with the tutor; a screenshot should not be presented as a completed native embed experiment. [Microsoft: web versus desktop features](https://support.microsoft.com/en-au/word/word-features-comparison-word-for-the-web-vs-desktop).

Current Microsoft guidance describes [creating equations in Word for the web](https://support.microsoft.com/en-us/education/onenote/create-equations-in-word-for-the-web). Some older help pages say otherwise; check the current Insert > Equation controls in your account. Do not assume a Windows shortcut or ribbon location works identically on Mac or web.

### 8 Connect the four questions to Exam Resolver

The seven steps below keep Q1 and Q2 experiments distinct, cover Q3's exact table and equation image, and create Q4's three separate caption-based lists. Original numbered files stay on authenticated Noroff links. The editable check log, experiment CSV, caption register and table-data CSV are original learning aids, not replacements for the supplied Office files.

Prepare Task 1.4 in Exam Resolver to transfer your selected step and written observations. The English review can identify missing checks and explain expected behaviour; it cannot inspect native links, embedded data, equation objects or generated lists from notes alone. Reopen the actual saved files and verify them before submitting yourself. Conceptual imagegen illustrations are not proof of completed task work.
"""


def guide_markdown():
    text = "## ARP Task 1.4 Incorporating Visualisations\n\n" + BOUNDARY + "\n\n"
    for title, instruction, check in STEPS:
        text += f"### {title}\n{instruction}\n\nCheck: {check}\n\n"
    text += "### Final native-file checks\n" + "\n".join(
        f"- **{title}:** {detail}" for title, detail in CHECKS
    )
    return (
        text
        + f"\n\n[Original task]({TASK_URL}). Sources checked {CHECKED_ON}. This is an original Study Buddy scaffold, not the official solution.\n"
    )
