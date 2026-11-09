"""Original Lesson 1.2 study guide, checked against the signed-in Noroff book."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81675"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81687"
SOURCE_URL = "https://learning.noroff.no/pluginfile.php/33187/mod_book/chapter/81687/LessonTasks.docx"
SOURCE_SHA256 = "d2ab8afa829bbc563e1c22f8128668d8f156a1314f66acbb2f7b2939af69a1b8"
CHECKED_ON = "2026-11-09"
BOUNDARY = (
    "Task 1.2 requires editing the supplied LessonTasks.docx in Word: change the design to Newsprint; "
    "add pagination at the top right; insert a page break after the second paragraph; insert a table of contents; "
    "change all pages to Landscape. The deliverable is an edited Word document, not a report-question plan. "
    "The source does not prescribe page count, a 1:3:25 report, font, exact file name or screenshots. "
    "Newsprint must be the exact named design/style set, not an invented substitute or an assumed theme. "
    "If unavailable in Word for the web, check desktop Word availability or ask the tutor. "
    "The second paragraph is ambiguous because headings and blank lines are also Word paragraphs. "
    "Count with paragraph marks and record the chosen text anchor; using the second substantive body paragraph "
    "starting 'Facilisis mauris sit amet massa vitae tortor' is a working interpretation, not a confirmed official answer. "
    "Exam Resolver can review written plans and check notes, but cannot certify native DOCX formatting or claim to "
    "apply Newsprint, insert Word fields, verify the saved file visually, or submit work from those notes."
)
STEPS = [
    (
        "1. Open and inspect the original file",
        "Download the original LessonTasks.docx below. Open it in Word, save a working copy and record whether you use Word for the web, Windows or Mac. Turn on paragraph marks (¶). Keep the supplied dummy text; the task asks for document formatting, not a new analysis report.",
        "The original contains a Title, four Heading2 paragraphs labelled Heading, three blank paragraphs and four substantive body paragraphs. Keep an untouched original.",
    ),
    (
        "2. Apply the Newsprint design",
        "In desktop Word, inspect Design > Document Formatting and expand the style-set gallery; look for the exact name Newsprint. The interface varies by edition. Select it if available and inspect the resulting document. Do not confuse a style set with a theme or manually imitate it with arbitrary fonts. If Word for the web does not offer the named design, use Open in Desktop App if available or ask the tutor which supported equivalent is acceptable.",
        "Record the exact gallery name and your Word edition. Do not mark this complete merely because the document looks newspaper-like.",
    ),
    (
        "3. Add dynamic page numbers at the top right",
        "Use Insert > Page Numbers (wording varies by edition), choose the header/top position and right alignment. Use a page-number field, not a manually typed 1. Inspect the first and later pages in Print Layout or Page View; check headers in every section if sections exist.",
        "Numbers appear at the top right and increment automatically. The task does not ask for a different first page or a special numbering scheme.",
    ),
    (
        "4. Insert the break after the confirmed paragraph",
        "With ¶ visible, distinguish headings, empty paragraphs and body text. A practical working interpretation is the second substantive body paragraph beginning 'Facilisis mauris sit amet massa vitae tortor'; record this assumption and confirm with the tutor if necessary. Place the cursor after that whole paragraph and before the following content, then use Insert > Page Break. Do not insert repeated blank lines or a section break.",
        "Record the beginning of the chosen paragraph and inspect the Page Break marker. Check that the following content starts on a new page; headings and empty paragraphs also count as paragraph markers.",
    ),
    (
        "5. Insert an automatic table of contents",
        "Inspect the existing Heading2 styles. Word builds an automatic table of contents from semantic headings; use Heading1 for actual top-level sections and Heading2 for subsections only if appropriate, rather than making text merely bold. Put the cursor where readers need the contents list, normally near the start after the title, and use References > Table of Contents to insert an automatic table. The brief does not specify a TOC position, depth or visual style.",
        "The entries come from real headings and include page numbers. A typed list or screenshot is not an automatic TOC. Do not invent new report content merely to fill it.",
    ),
    (
        "6. Set every page to Landscape",
        "Use Layout > Orientation > Landscape (the label can vary). Apply the change to the whole document, checking every section if needed. Inspect the page shape, headers, text wrapping and contents list again. Keep other page settings unless a change is needed to satisfy the task; no specific margin or paper size is prescribed.",
        "Every page is landscape, not just the page under the cursor. Page count may change; a fixed page count is not a task requirement.",
    ),
    (
        "7. Update, reopen and check all five requirements",
        "Update the entire table of contents after the page break and orientation changes. Save the edited DOCX, close and reopen the saved copy, and inspect all five requirements using the checklist. Record observed results, unresolved issues and the actual file name. Transfer your notes to Exam Resolver for an English review, then download and submit the actual Word document yourself when satisfied.",
        "A plan, a generated illustration or an AI response is not proof of native formatting. Mark an item checked only after inspecting it in the saved Word file. Screenshots are optional study evidence, not a stated task deliverable.",
    ),
]
CHECKS = [
    (
        "Newsprint design",
        "Exact named Newsprint design/style set is selected; record Word edition and gallery name.",
    ),
    (
        "Top-right pagination",
        "Dynamic page-number fields appear in the top-right header and increment on later pages.",
    ),
    (
        "Page break after second paragraph",
        "Record the paragraph text anchor and interpretation; inspect the explicit Page Break marker.",
    ),
    (
        "Table of contents",
        "An automatic TOC uses real headings and its entries/page numbers have been updated.",
    ),
    (
        "Landscape orientation",
        "All pages/sections are landscape in the reopened saved DOCX.",
    ),
]
QUESTION_TEMPLATE = """# ARP Task 1.2 Word editing plan and check notes

This is a planning/check log. The task deliverable is the edited LessonTasks.docx, not this Markdown file.

## Working file
Original: LessonTasks.docx (downloaded from Noroff, unchanged)
Working copy file name: [...]
Word edition and version: [...]
Original preserved: [Not checked]

## Paragraph interpretation
Show paragraph marks (¶). Headings and empty paragraphs are paragraph markers too.
Chosen meaning of second paragraph: [...]
Beginning of the paragraph after which I insert the break: [...]
Working interpretation to confirm if needed: the second substantive body paragraph begins 'Facilisis mauris sit amet massa vitae tortor'.
Tutor clarification, if needed: [...]

## Five required checks
1. Newsprint design: [Not checked]
   Exact gallery name, edition and observed result: [...]
2. Dynamic page numbers at top right: [Not checked]
   First and later page observations: [...]
3. Page break after the second paragraph: [Not checked]
   Text anchor and explicit Page Break marker observed: [...]
4. Automatic table of contents: [Not checked]
   Heading styles, TOC entries and update result: [...]
5. All pages Landscape: [Not checked]
   Sections/pages inspected: [...]

## Final native-file review
Entire TOC updated after layout changes: [Not checked]
Saved DOCX closed and reopened: [Not checked]
Five checks repeated in saved copy: [Not checked]
Outstanding issue or unavailable command: [...]
Next action: [...]

## Exam Resolver request
Review my plan and actual observations in English. Explain my selected step and flag missing checks. Do not claim to inspect or modify my DOCX from these notes. I will verify the actual Word file and submit it myself.
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-1-2-report-types-styles.png",
        title="Report type and writing style",
        caption="A report type describes purpose and audience; a writing style describes how the explanation is presented. The seven report types and five styles can overlap. Choose for the reader and support claims with evidence.",
    ),
    dict(
        file="task-1-2-word-checks.png",
        title="Five checks in Word",
        caption="The five required edits are Newsprint design, dynamic top-right page numbers, a page break after the confirmed second paragraph, an automatic table of contents and Landscape orientation. This conceptual image is not a Word screenshot or proof of completed formatting. Its decorative columns and pictures are not extra task requirements. Verify the saved DOCX.",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="1.2-task",
    uid="arp-1.2-task-81687",
    lesson_number="1.2",
    title="Writing Styles — format LessonTasks.docx",
    source_url=TASK_URL,
    method="Word document formatting and verification",
    deliverable="Edited LessonTasks.docx with the five required formatting changes",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file="ARP Task 1.2 Word Editing Plan.md",
)
LESSON_CONTENT = """### Lesson 1.2 Writing Styles

A useful report matches its purpose and reader. This lesson connects report types and writing styles to practical Word tools: styles, page numbers, contents lists, breaks, views and page layout. Task 1.2 applies the Word tools to an existing dummy-text document.

### 1 Choose a report type for its purpose

| Report type | Typical purpose | Reader check |
|---|---|---|
| Formal | Give a structured, detailed account of a significant issue | Clear scope, evidence, methods and conclusions |
| Informal or short | Communicate a focused update or small investigation | Concise and professional; claims still need evidence |
| Technical | Explain specialist methods, systems or results | Define terminology and provide reproducible detail |
| White paper | Examine an issue and explain a proposed approach | Evaluate the argument and its evidence; consider who produced it |
| Performance | Compare actual performance with stated objectives or measures | Define targets, periods, units and comparability |
| Evaluation | Judge an intervention or outcome against explicit criteria | Explain criteria, evidence, limitations and attribution |
| Annual | Review an organisation's activity over a year | Identify the period, audience and relevant financial/non-financial scope |

These categories overlap. An annual report may contain performance, technical and evaluation sections. Informal does not mean unsupported opinion is evidence. The source mentions GRI in the context of sustainability reporting; choosing a framework does not itself demonstrate compliance with any current rule.

### 2 Choose how to explain

| Writing style | What it does | Example study sentence |
|---|---|---|
| Analytical / informational | Presents information clearly; analytical writing also examines relationships and meaning | “Compare monthly totals using the same definitions before interpreting the pattern.” |
| Investigative | Examines a question through traceable evidence and competing explanations | “Check source records and alternative explanations before attributing the difference.” |
| Narrative | Gives a coherent sequence with relevant context | “Describe what happened, in what order, and why each event matters to the question.” |
| Persuasive | Argues for a justified position or action | “Recommend an action, explain the evidence and address its limitations.” |
| Technical | Explains specialist procedures accurately | “State inputs, software, steps, units and assumptions so another analyst can repeat the work.” |

Combine styles when helpful. Keep facts, interpretation and recommendations distinct. A confident tone or attractive layout cannot substitute for reliable evidence.

### 3 Layer detail for the audience

The 1:3:25 guideline means **one page of main messages, a three-page executive summary and up to 25 pages of findings and methodology**. The Noroff lesson describes the first two layers differently; use the original method's definitions. This is an optional way to serve readers who need different levels of detail, not a required length for Task 1.2. [BetterEvaluation: 1:3:25](https://www.betterevaluation.org/methods-approaches/methods/one-three-twenty-five-1325-principle).

### 4 Understand Word's formatting layers

A paragraph style, such as Heading1, Heading2 or Normal, assigns a semantic role and consistent formatting. A design/style set changes coordinated document formatting. A theme coordinates elements such as colours and fonts. A template is a starting document with predefined structure and settings. These are related but different tools. See [Microsoft's explanation of templates, themes and styles](https://support.microsoft.com/en-us/word/differences-between-templates-themes-and-word-styles).

Use real heading styles for navigation and automatic contents entries. Bold or enlarged Normal text is not automatically a heading. The supplied task file already has a Title and four Heading2 paragraphs named Heading. Inspect these rather than assuming they are absent. The lesson's separate Report.docx demonstration is not the Task 1.2 working file.

### 5 Build navigation that updates

Insert page numbers as fields in the header, rather than typing a number on each page. An automatic table of contents uses heading styles and must be updated after changes to headings, breaks or layout. In Word, use References > Table of Contents; labels differ by edition. A typed contents list will not automatically follow layout changes. [Microsoft: insert a table of contents](https://support.microsoft.com/en-us/word/training/insert-a-table-of-contents?ad=US&redirectSourcePath=%252fen-us%252farticle%252fCreate-a-table-of-contents-in-Word-2016-for-Mac-054a1411-bb5f-4583-9ba5-03d7e1778956&rs=en-US&ui=en-US).

### 6 Choose the right break and view

A **page break** starts following content on a new page. A **section break** creates a section that can have its own layout or header settings; continuous, next-page and odd/even-page variants serve different needs. A **column break** moves to the next column; a **line break** starts another line within the same paragraph. Repeated Enter presses create extra paragraphs, not a reliable page break.

Text-wrapping settings such as Square and Tight control how text flows around an object; they are not the same thing as inserting a page break or a text-wrapping break. Turn on ¶ to inspect paragraph and break markers. Use Print Layout or Page View to check page boundaries and header positions. Draft, outline and reading views vary by Word edition and are not all available in the browser.

### 7 Use page layout deliberately

Orientation changes page shape: Portrait is taller than wide, Landscape is wider than tall. Margins, paper size, columns and section settings also affect layout. A whole-document instruction requires checking all sections. After changing orientation, inspect headers and update the TOC because page numbers may change.

Word for the web supports page numbers, page breaks, orientation and contents features, but its controls differ from desktop Word. It supports applying built-in styles; it does not offer all desktop customisation. The exact **Newsprint** gallery item must be checked in your edition. Do not claim a particular theme or style set has been applied merely from its appearance. [Microsoft: Word for the web features](https://learn.microsoft.com/en-us/office365/servicedescriptions/office-online-service-description/word-online) · [Styles in Word for the web](https://support.microsoft.com/en-au/word/use-styles-in-word-for-the-web).

### 8 Apply only the five task requirements

Task 1.2 asks you to edit **LessonTasks.docx**: Newsprint design, top-right pagination, a page break after the second paragraph, a table of contents and Landscape pages. The supplied file contains Lorem ipsum dummy text. You do not need to write a new report or apply the 1:3:25 guideline. No page count, font, file naming rule or screenshot requirement is specified.

“Second paragraph” needs care: Word counts headings and blank paragraphs too. The guide proposes the second substantive body paragraph starting **“Facilisis mauris sit amet massa vitae tortor”** as a working interpretation, explicitly to confirm if needed. Record the chosen anchor and inspect the actual break. Use the seven steps below, then reopen the saved DOCX and verify all five requirements. Exam Resolver reviews your written plan and observations; it does not certify native Word formatting from notes.

**Exam explanation pattern:** purpose and reader → report type and writing style → semantic structure → navigation and layout → inspect the saved file. The illustrations are conceptual study aids, not completed-document evidence.
"""


def guide_markdown():
    text = "## ARP Task 1.2 Word formatting\n\n" + BOUNDARY + "\n\n"
    for title, instruction, check in STEPS:
        text += f"### {title}\n{instruction}\n\nCheck: {check}\n\n"
    text += "### Five required checks\n" + "\n".join(
        f"- **{title}:** {detail}" for title, detail in CHECKS
    )
    return (
        text
        + f"\n\n[Original task]({TASK_URL}) · [Original working file]({SOURCE_URL}). Checked {CHECKED_ON}. This is an original Study Buddy guide; the official solution was not used.\n"
    )
