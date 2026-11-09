"""Original Analysis Reporting study material based on the signed-in Noroff book."""

from copy import deepcopy
from pathlib import Path
import sys
import arp_lesson12
import arp_lesson13
import arp_lesson14
import arp_lesson21
import arp_lesson22
import arp_lesson23

CONTENT_REVISION = "2026-11-09-arp23"
COURSE_CODE = "FI1BBAR05"
COURSE_NAME = "Analysis Reporting"
ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81667"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22936&chapterid=81674"
CHECKED_ON = "2026-11-09"

BOUNDARY = (
    "Task 1.1 asks for report questions, ordered from general to specific, not a completed engagement analysis. "
    "The supplied scenario is a small handmade-candle business using Facebook, Instagram and TikTok without paid advertising, over the last six months. "
    "Include posting schedule and content type. No dataset, numerical results, exact reporting dates, word count, page count, font or required file format is supplied. "
    "Choose and state an exact six-month window; do not silently substitute six months before today's date. "
    "Do not invent engagement results, a best platform, a best posting time, sales attribution or completed testing."
)

STEPS = [
    (
        "1. Decode the task",
        "Record the supplied business, Facebook, Instagram and TikTok, organic activity only, and the last six months. The output is a logically ordered set of questions that a later report should answer.",
        "You are planning a report, not calculating findings from a supplied dataset.",
    ),
    (
        "2. Define purpose, audience and period",
        "Propose the owner or marketing lead as the intended reader and label this as a working assumption. State the decision the report would support. Enter an agreed six-month start/end date and the timezone for posting times.",
        "The task does not name a recipient or give exact dates. Confirm these rather than inventing them.",
    ),
    (
        "3. Start with broad engagement questions",
        "Ask how overall organic engagement developed during the six-month window, what volume of content was published, and whether engagement was evenly distributed across the period. Ask questions neutrally, without suggesting a winner.",
        "Define engagement actions and distinguish total actions from unique engaged people.",
    ),
    (
        "4. Compare platforms and months",
        "Break the broad questions down by Facebook, Instagram and TikTok, then by month. Ask about comparable engagement measures, posting volume and engagement per post, and note whether a platform has missing or differently defined metrics.",
        "Reach, impressions, views and followers are different denominators. Do not rank mixed engagement-rate formulas as if they were the same metric.",
    ),
    (
        "5. Examine the posting schedule",
        "Ask about posting frequency, consistency, weekday and time of day, within each platform. Ask whether engagement differs across these groups after considering content type, exposure and the number of observed posts.",
        "A relationship between posting time and engagement does not prove that time caused the outcome. Small groups and seasonal campaigns can distort comparisons.",
    ),
    (
        "6. Narrow down to content and individual posts",
        "Ask how formats and themes differ in engagement on each platform, then identify specific posts to investigate: their format, topic, publication time, exposure and action mix. Consider comments for qualitative context without claiming they were already analysed.",
        "Formats and available fields must be checked in actual exports. Organic reach does not mean content production had no cost, and engagement is not automatically a sale.",
    ),
    (
        "7. Check the question sequence and export",
        "Order your final questions from overall performance to platforms, months, posting schedule, content groups and individual posts. For each question, identify the evidence needed and why it helps the report's reader. Use Exam Resolver to review your draft, then download your work for your own use.",
        "Keep every final item phrased as a question. Remove invented findings and preserve the organic-only scope. The examples are a Study Buddy scaffold, not Noroff's official solution.",
    ),
]

QUESTION_GROUPS = [
    (
        "Overall organic engagement",
        [
            "How has organic engagement across the business's Facebook, Instagram and TikTok accounts changed over the agreed six-month period?",
            "How much content was published during the period, and how does engagement relate to the volume of posts?",
            "Which engagement actions are relevant to the report's purpose, and are the available definitions consistent enough to compare?",
        ],
    ),
    (
        "Platform and monthly detail",
        [
            "How does organic engagement differ between Facebook, Instagram and TikTok when comparable measures are used?",
            "How do total engagement actions and engagement per post change month by month within each platform?",
            "Are differences in engagement associated with changes in posting volume or exposure, rather than a change in audience response alone?",
        ],
    ),
    (
        "Posting schedule",
        [
            "How frequently and consistently does the business publish on each platform?",
            "Within each platform, how does engagement per post vary by weekday and posting time in the stated timezone?",
            "Do those schedule patterns remain similar when posts are compared within the same content type and when the number of posts in each group is considered?",
        ],
    ),
    (
        "Content type and theme",
        [
            "Which content formats are used on each platform, and how do they differ in engagement under the chosen metric?",
            "How do content themes such as product information, candle-making processes and customer stories compare within a platform?",
            "For a given format and platform, how does the mix of comments, shares and other available engagement actions differ across themes?",
        ],
    ),
    (
        "Specific posts",
        [
            "Which individual posts have unusually high or low engagement relative to comparable posts on the same platform?",
            "For each selected post, what were its publication date and time, format, theme, exposure and engagement-action breakdown?",
            "What do comments on those selected posts suggest about the audience's response, and what additional evidence would be needed to explain the pattern?",
        ],
    ),
]

QUESTION_TEMPLATE = """# ARP Task 1.1 Report question plan

Prepare your own ordered questions for the handmade-candle business. This is a planning template, not a completed analysis or an official solution.

## Supplied scope
Business: small handmade-candle seller
Platforms: Facebook, Instagram and TikTok
Advertising: no paid advertising on any of these platforms
Reporting window: last six months
Required emphasis: posting schedule and type of content
Output: questions ordered from general to specific

## Decisions to confirm
Intended reader [proposed assumption]: [...]
Decision the report should support: [...]
Agreed period start: [...]  Period end: [...]
Calendar window and inclusion rule: [...]
Timezone for publishing times: [...]
Engagement actions included: [...]
Rate denominator and formula, if a rate is used: [...]
How missing or differently defined platform fields will be handled: [...]

## 1 Overall engagement questions
1. [...]
2. [...]

## 2 Platform and monthly questions
3. [...]
4. [...]
5. [...]

## 3 Posting schedule questions
6. [Frequency and consistency question]
7. [Weekday and time of day question]
8. [Question considering content type, exposure and group size]

## 4 Content type and theme questions
9. [Format question]
10. [Theme question]
11. [Question about the mix of engagement actions]

## 5 Individual post questions
12. [Question identifying unusual posts within a platform]
13. [Specific post details to examine]
14. [Question about comments and further evidence]

## Evidence mapping
For each question record:
Question number: [...]
Data or evidence required: [...]
Metric and unit: [...]
Comparison and breakdown: [...]
Why the reader needs this answer: [...]
Limitations or missing evidence: [...]

## Final review
- All three platforms and the agreed six-month period are covered.
- Questions move from general to specific.
- Posting schedule and content type are explicit.
- Questions are neutral and answerable with identifiable evidence.
- No fabricated results, assumed best platform or causal claim.
- No paid-advertising analysis introduced.
- Any rate uses a stated, consistent denominator.
- This is a question plan, not a completed report.
"""

REPORT_TEMPLATE = """# ARP Lesson 1.1 Optional report outline

Learning scaffold only. Task 1.1 requires report questions, not this completed report.

## Title page
Subject [...], author [...], role [...], report date [...].

## Executive summary
Write last. Summarise the purpose, key supported findings and conclusions for a reader who may not read the full report. Keep it concise; the lesson suggests approximately one page for a full report, not a page requirement for Task 1.1.

## Introduction
Reader and decision [...]. Questions [...]. Scope and period [...]. Why the topic matters [...].

## Body
### Data and methods
Source, coverage, metric definitions, cleaning, methods and limitations [...].
### Findings by question
Question [...]. Evidence [...]. Interpretation [...]. Limitation [...].
Use meaningful headings and explain any figure in the text. Do not insert results without evidence.

## Conclusion
Answer the original questions using the findings already presented [...]. No new evidence or unsupported opinions.

## Recommendations if appropriate
Proposed action [...]. Supporting finding [...]. Uncertainty [...]. How to evaluate it [...].

## References and supporting material if needed
Use the brief's required referencing style. Add navigation, page numbers and appendices when helpful for the actual report; Task 1.1 does not prescribe these.
"""

ILLUSTRATIONS = [
    {
        "file": "lesson-1-1-report-structure.png",
        "title": "An evidence-based report",
        "caption": "The lesson's four core parts are executive summary, introduction, body and conclusion. Explain data and methods in the body as appropriate, and keep justified recommendations distinct from supported conclusions. Write the summary last. This is an educational illustration, not a required Task 1.1 report layout.",
    },
    {
        "file": "task-1-1-question-funnel.png",
        "title": "From broad questions to specific evidence",
        "caption": "For the handmade-candle business, narrow questions from overall organic engagement to platforms, months, posting schedule, content and individual posts. Cover Facebook, Instagram and TikTok over an agreed six-month window. The illustration contains no measured performance results.",
    },
]

LESSON_CONTENT = """### Lesson 1.1 Report Writing

A report turns evidence into an organised explanation for a defined reader and purpose. An analysis report should make the data, methods, findings and their meaning understandable enough to support a decision. Good writing makes the analysis traceable; it does not repair weak evidence.

### 1 Start with the question and the reader

Ask what the report must answer and who will use the answer. The same analysis may need a concise explanation for a business owner and fuller methodological detail for an analyst. Define specialist terms, keep language professional and remove irrelevant detail. Do not assume that a non-technical reader can infer the meaning of a chart or metric.

Reports help people make decisions, explain resource choices, review evidence, collaborate and revisit earlier work. Their credibility depends on transparent sources, methods, assumptions and limitations. Whether regulatory rules apply depends on the actual setting; report writing alone does not establish compliance.

### 2 Plan before drafting

Confirm the purpose, intended reader, scope and time period. Map each report question to evidence that could answer it. Obtain suitable data, check coverage and quality, record cleaning decisions and document the method and software used. Keep the work focused on the original questions.

The lesson uses sales and staff-turnover examples to show that questions depend on the business problem. Those examples are not the candle-business task. One sales example loosely labels sales minus cost of sales as gross sales; use clear financial definitions rather than copying that label. Task 1.1 does not require financial calculations.

### 3 Separate evidence from interpretation and action

A finding describes what the analysis supports. Interpretation explains its meaning with appropriate uncertainty. A conclusion answers the report's questions from the findings already presented. A recommendation proposes a justified next action and should be distinguished from a proven result.

The source first mentions opinions in conclusions but later says conclusions should be free of opinions. The consistent study rule is to support conclusions with evidence and label recommendations separately. A relationship between two variables is not, by itself, proof of causation.

### 4 Organise the report around four core parts

| Part | Its job | Check |
|---|---|---|
| Executive summary | Give a concise standalone account of purpose, important findings and conclusions | Write it after the analysis; do not merely list what is coming |
| Introduction | Explain context, purpose, questions, audience and scope | Make the decision and boundaries clear |
| Body | Present data, methods, findings and their explanation in meaningful sections | Connect every claim to evidence and define metrics |
| Conclusion | Answer the original questions and explain their supported significance | Introduce no unsupported claim or new analysis |

A title page identifies the subject, author, role and date. A longer report can benefit from a table of contents, page numbers, references and supporting material. Methodology can be a body subsection or a separate section when the brief calls for it. Recommendations should be clearly identified if appropriate. These are report-writing principles, not additional prescribed deliverables for Task 1.1.

### 5 Draft first and then edit

Start with a rough structure, use headings and keep paragraphs focused. Build a paragraph from its question or topic through evidence and explanation to a useful implication. Match technical detail to the reader. Review the logic and factual claims before polishing sentences, spelling and layout. If possible, ask a fresh reader to review the draft or return after a break. Proofreading tools can suggest edits; they do not verify data or make every suggestion correct.

### 6 Apply the lesson to Task 1.1

The scenario concerns a small handmade-candle business and organic engagement on Facebook, Instagram and TikTok. Prepare the questions that a report about the last six months should answer, moving from general to specific. Explicitly examine posting schedule and content type. No dataset or measured results are supplied. The task does not prescribe a word count, page count, font or file format.

Use the question plan below to define an agreed six-month window and propose a reader without treating that assumption as a supplied fact. Move from total engagement to platforms and months, then to posting frequency, weekday and time, formats, themes and individual posts. The examples are original Study Buddy prompts to adapt, not the downloaded Noroff solution, which was not used.

### 7 Define comparisons before asking which performs best

Engagement actions are not necessarily unique engaged people. State which actions you would count and which platform fields actually exist. If you propose an engagement rate, define its numerator, denominator and period. For example, actions divided by reach and actions divided by impressions are different rates; comparing them directly can mislead. Followers, impressions, views and reach are not interchangeable measures. Do not sum cross-platform audiences and call the result unique people.

Ask about engagement per post as well as totals: posting more often can change total actions without improving the typical post. Consider small groups, unequal exposure, content mix, seasonal events and missing data. Organic-only describes the absence of paid advertising in the brief, not the absence of production costs. Likes and comments alone do not establish sales impact or return on investment.

**Exam explanation pattern:** purpose → reader → question → evidence and method → supported conclusion → justified action and limitation. For this task, stop at an ordered plan of questions and the evidence needed; actual findings require actual data.
"""

GUIDE = dict(
    course_code=COURSE_CODE,
    id="1.1-task",
    uid="arp-1.1-task-81674",
    lesson_number="1.1",
    title="Organic social media engagement report questions",
    source_url=TASK_URL,
    method="report question planning",
    deliverable="Questions ordered from general to specific for the last six months, explicitly covering posting schedule and content type",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file="ARP Task 1.1 Report Question Plan.md",
)


def guide_markdown(guide=None):
    if guide and guide.get("lesson_number") in TASK_MATERIALS:
        return task_material(guide).guide_markdown()
    text = "## ARP Task 1.1 Report question planning\n\n" + BOUNDARY + "\n\n"
    for title, instruction, check in STEPS:
        text += f"### {title}\n{instruction}\n\nCheck: {check}\n\n"
    text += "### Example questions to adapt\nOriginal Study Buddy examples, not the official solution. Themes are proposals, not known facts about existing posts.\n\n"
    for group, questions in QUESTION_GROUPS:
        text += f"#### {group}\n" + "\n".join(f"- {q}" for q in questions) + "\n\n"
    return text + f"[Original task]({TASK_URL}). Source checked {CHECKED_ON}.\n"


def get_task_guides(number):
    if str(number) != "1.1" and str(number) not in TASK_MATERIALS:
        return []
    guide = deepcopy(task_material({"lesson_number": str(number)}).GUIDE)
    guide["markdown"] = guide_markdown(guide)
    return [guide]


# Additional lessons supply the same task material interface as Lesson 1.1.
TASK_MATERIALS = {
    "1.2": arp_lesson12,
    "1.3": arp_lesson13,
    "1.4": arp_lesson14,
    "2.1": arp_lesson21,
    "2.2": arp_lesson22,
    "2.3": arp_lesson23,
}


def task_material(guide=None):
    """Keep every task's steps, draft and assets together without sharing state."""
    return TASK_MATERIALS.get((guide or {}).get("lesson_number"), sys.modules[__name__])


def all_task_guides():
    return [
        guide
        for number in ("1.1", *TASK_MATERIALS)
        for guide in get_task_guides(number)
    ]


def get_course_lessons():
    return [
        dict(
            course_code=COURSE_CODE,
            lesson_number="1.1",
            title="Report Writing",
            module_number=1,
            module_title="Report Writing",
            source_url=LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=LESSON_CONTENT
            + f"\n\n[Original lesson]({LESSON_URL}) · [Original task]({TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(ILLUSTRATIONS),
            key_points=[
                "Define purpose, reader and scope before drafting",
                "Use the four core report parts and keep claims supported",
                "Order Task 1.1 questions from general to specific",
                "Distinguish organic engagement, metrics, evidence and assumptions",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="1.2",
            title="Writing Styles",
            module_number=1,
            module_title="Report Writing",
            source_url=arp_lesson12.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson12.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson12.LESSON_URL}) · [Original task]({arp_lesson12.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson12.ILLUSTRATIONS),
            key_points=[
                "Choose report types and writing styles for the reader",
                "Distinguish semantic styles, design sets, themes and templates",
                "Apply the five Word edits to LessonTasks.docx",
                "Inspect the saved file; notes alone cannot prove formatting",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="1.3",
            title="Referencing Styles and Tools",
            module_number=1,
            module_title="Report Writing",
            source_url=arp_lesson13.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson13.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson13.LESSON_URL}) · [Original task]({arp_lesson13.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson13.ILLUSTRATIONS),
            key_points=[
                "Link claims, in-text citations and full references",
                "Use Harvard consistently; confirm the required institutional variant",
                "Find sources with Scholar, read and verify the original evidence",
                "Plan 500 words and at least four citations for Task 1.3",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="1.4",
            title="Incorporating Visualisations",
            module_number=1,
            module_title="Report Writing",
            source_url=arp_lesson14.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson14.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson14.LESSON_URL}) · [Original task]({arp_lesson14.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson14.ILLUSTRATIONS),
            key_points=[
                "Distinguish linked charts, embedded copies and pictures",
                "Record independent before/after observations for both chart experiments",
                "Enter the exact table and inspect the source equation ambiguity",
                "Generate three separate caption-based lists and verify saved files",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="2.1",
            title="Report-generating Tools",
            module_number=2,
            module_title="Report-Generating Tools",
            source_url=arp_lesson21.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson21.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson21.LESSON_URL}) · [Original task]({arp_lesson21.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson21.ILLUSTRATIONS),
            key_points=[
                "Choose narrative, paginated or executable reporting for the reader",
                "Distinguish Jupyter .ipynb, plain Markdown and R Markdown .Rmd",
                "Trace claims to dated evidence and independent sources",
                "Evaluate all three Task 2.1 articles in one page with qualified judgements",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="2.2",
            title="Creating Full-length Reports",
            module_number=2,
            module_title="Report-Generating Tools",
            source_url=arp_lesson22.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson22.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson22.LESSON_URL}) · [Original task]({arp_lesson22.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson22.ILLUSTRATIONS),
            key_points=[
                "Connect purpose, data, findings, interpretation and conclusion",
                "Use the six supplied fictional Nice Ride brand counts",
                "Create a Word report with heading styles and a vertical Column plot",
                "Place a short supported comment after the plot and inspect the saved file",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
        dict(
            course_code=COURSE_CODE,
            lesson_number="2.3",
            title="Generating Infographics",
            module_number=2,
            module_title="Report-Generating Tools",
            source_url=arp_lesson23.LESSON_URL,
            source_checked_on=CHECKED_ON,
            content=arp_lesson23.LESSON_CONTENT
            + f"\n\n[Original lesson]({arp_lesson23.LESSON_URL}) · [Original task]({arp_lesson23.TASK_URL}). Checked {CHECKED_ON}.",
            illustration=None,
            arp_illustrations=deepcopy(arp_lesson23.ILLUSTRATIONS),
            key_points=[
                "Use evidence, context and design to explain one clear message",
                "Choose a Kaggle dataset and perform actual EDA in MS Excel",
                "Build original GIMP layers and cite external data and visuals",
                "Save editable .xcf and separately export .jpg; canvas size is a choice",
            ],
            visual_elements=dict(
                diagrams=False, tables=True, highlighted_sections=True
            ),
        ),
    ]


def get_training_modules():
    modules = {
        "ARP Module 1: Report Writing": dict(
            course=COURSE_NAME,
            description="Reviewed Lessons 1.1–1.4: report writing, formatting, referencing and visual integration with guided task workflows.",
            lessons=[
                lesson
                for lesson in get_course_lessons()
                if lesson["module_number"] == 1
            ],
            exercises=[
                dict(
                    title="Task 1.1 Report questions",
                    type="case_study",
                    question=GUIDE["deliverable"],
                    hint="Use the candle-business brief and start broad.",
                    answer=guide_markdown(),
                ),
                dict(
                    title="Task 1.2 Word formatting",
                    type="case_study",
                    question=arp_lesson12.GUIDE["deliverable"],
                    hint="Use the original LessonTasks.docx and verify all five requirements in Word.",
                    answer=arp_lesson12.guide_markdown(),
                ),
                dict(
                    title="Task 1.3 Workplace overview",
                    type="case_study",
                    question=arp_lesson13.GUIDE["deliverable"],
                    hint="Plan 500 words, read sources and trace at least four Harvard citations to real evidence.",
                    answer=arp_lesson13.guide_markdown(),
                ),
                dict(
                    title="Task 1.4 Office visual integration",
                    type="case_study",
                    question=arp_lesson14.GUIDE["deliverable"],
                    hint="Use independent chart baselines and check the actual saved Office files.",
                    answer=arp_lesson14.guide_markdown(),
                ),
            ],
            quiz=[
                dict(
                    question="Original Study Buddy revision: What is the Task 1.1 deliverable?",
                    options=[
                        "Invent six months of platform results",
                        "Plan report questions from general to specific",
                        "Calculate paid-advertising ROI",
                    ],
                    correct=1,
                    explanation="The task supplies a scenario, not a dataset. It asks for ordered questions about organic engagement, including schedule and content.",
                ),
                dict(
                    question="Original Study Buddy revision: What belongs in a conclusion?",
                    options=[
                        "A supported answer to the original questions",
                        "Unrelated new evidence",
                        "An assumed best posting time",
                    ],
                    correct=0,
                    explanation="Conclusions follow the evidence already presented. Identify recommendations and uncertainty separately.",
                ),
                dict(
                    question="Original Study Buddy revision: What proves Task 1.2 formatting?",
                    options=[
                        "The conceptual image",
                        "A written plan only",
                        "Inspection of all five requirements in the saved DOCX",
                    ],
                    correct=2,
                    explanation="Plans and illustrations guide the work; reopen the actual Word file and inspect the required formatting.",
                ),
                dict(
                    question="Original Study Buddy revision: What feeds an automatic table of contents?",
                    options=[
                        "Semantic heading styles",
                        "Bold text alone",
                        "A screenshot of the headings",
                    ],
                    correct=0,
                    explanation="Use real heading styles and update the TOC after layout changes.",
                ),
                dict(
                    question="Original Study Buddy revision: What does Task 1.3 explicitly require?",
                    options=[
                        "Four distinct sources and Chicago footnotes",
                        "500 words, at least four citations and a Harvard end list",
                        "Only a bibliography with no in-text citations",
                    ],
                    correct=1,
                    explanation="The brief asks for at least four citations, not explicitly four distinct sources. Confirm the Harvard variant and counting rule.",
                ),
                dict(
                    question="Original Study Buddy revision: Does an accurate paraphrase need a citation?",
                    options=[
                        "Yes, borrowed ideas still need attribution",
                        "No, only direct quotations need citations",
                        "Only when using Zotero",
                    ],
                    correct=0,
                    explanation="Write the meaning in your own words and cite the original source. Tools do not remove the need to read and verify evidence.",
                ),
                dict(
                    question="Original Study Buddy revision: What should an external Excel edit do to an embedded chart copy?",
                    options=[
                        "Always update it immediately",
                        "Leave its internal data unchanged",
                        "Turn it into a picture",
                    ],
                    correct=1,
                    explanation="An embedded chart has a separate data copy. Actual observations still need to be checked; a pre-edited baseline makes a no-change test inconclusive.",
                ),
                dict(
                    question="Original Study Buddy revision: How are the three Q4 lists generated?",
                    options=[
                        "Type the headings only",
                        "Paste three screenshots",
                        "Use matching Figure, Table and Equation captions, then insert and update each list",
                    ],
                    correct=2,
                    explanation="Each caption label feeds its corresponding list. Check entries and page numbers in the saved document.",
                ),
            ],
        )
    }

    modules["ARP Module 2: Report-Generating Tools"] = dict(
        course=COURSE_NAME,
        description="Reviewed Lessons 2.1–2.3: reporting tools, critical reading, a Word report and an EDA-based GIMP infographic.",
        lessons=[
            lesson for lesson in get_course_lessons() if lesson["module_number"] == 2
        ],
        exercises=[
            dict(
                title="Task 2.1 Source reliability",
                type="case_study",
                question=arp_lesson21.GUIDE["deliverable"],
                hint="Use the same evidence criteria for all three articles and distinguish verified facts from broader interpretations.",
                answer=arp_lesson21.guide_markdown(),
            )
        ],
        quiz=[
            dict(
                question="Original Study Buddy revision: What does Task 2.1 require?",
                options=[
                    "A one-page report evaluating all three supplied articles",
                    "A 500-word Harvard overview",
                    "A new Excel chart and PowerPoint",
                ],
                correct=0,
                explanation="Task 2.1 asks for explained reliability findings on all three articles in a one-page report; the other requirements belong elsewhere.",
            ),
            dict(
                question="Original Study Buddy revision: Two sites republish the same original story. What does this establish?",
                options=[
                    "Two independent confirmations",
                    "A republication chain, not independent corroboration",
                    "That every claim is false",
                ],
                correct=1,
                explanation="Trace the original evidence. Neither repetition nor biased wording alone settles factual accuracy.",
            ),
            dict(
                question="Original Study Buddy revision: An 846% increase means the new amount is approximately…",
                options=[
                    "8.46 times the baseline",
                    "846 times the baseline",
                    "9.46 times the baseline",
                ],
                correct=2,
                explanation="The original 100% remains: 1 + 8.46 = 9.46. Check dates, geography, denominator and rounding before using the result.",
            ),
        ],
    )
    modules["ARP Module 2: Report-Generating Tools"]["exercises"].append(
        dict(
            title="Task 2.2 Nice Ride report",
            type="case_study",
            question=arp_lesson22.GUIDE["deliverable"],
            hint="Check all six counts, identify Mercedes 220, use a vertical column chart and put the comment after it.",
            answer=arp_lesson22.guide_markdown(),
        )
    )
    modules["ARP Module 2: Report-Generating Tools"]["quiz"].extend(
        [
            dict(
                question="Original Study Buddy revision: Which brand has the highest Nice Ride count?",
                options=["Audi 180", "Mercedes 220", "Tesla 85"],
                correct=1,
                explanation="Mercedes has 220 of the supplied 865 cars. This describes the fictional data, not national demand or profit.",
            ),
            dict(
                question="Original Study Buddy revision: What plot and comment does Task 2.2 require?",
                options=[
                    "A pie chart with no explanation",
                    "A line chart and a future forecast",
                    "A Column plot and a short comment following it",
                ],
                correct=2,
                explanation="Use six vertical columns and real Word heading styles. No reporting period or shop-level breakdown is supplied.",
            ),
        ]
    )
    modules["ARP Module 2: Report-Generating Tools"]["exercises"].append(
        dict(
            title="Task 2.3 EDA infographic",
            type="case_study",
            question=arp_lesson23.GUIDE["deliverable"],
            hint="Choose data from Kaggle, verify Excel findings and build your own GIMP infographic with source credits.",
            answer=arp_lesson23.guide_markdown(),
        )
    )
    modules["ARP Module 2: Report-Generating Tools"]["quiz"].extend(
        [
            dict(
                question="Original Study Buddy revision: Which files does Task 2.3 ask you to retain/export?",
                options=[
                    "Only a PNG renamed as XCF",
                    "An editable .xcf and an exported .jpg",
                    "A Word report and a PowerPoint",
                ],
                correct=1,
                explanation="Save the working GIMP project as XCF, then export JPEG separately and inspect both files. JPEG does not retain layers.",
            ),
            dict(
                question="Original Study Buddy revision: Is 800 × 1200 px compulsory?",
                options=[
                    "Yes, every task uses that size",
                    "Only if a dataset contains dates",
                    "No, it is an example; choose suitable dimensions",
                ],
                correct=2,
                explanation="The brief gives an example. Choose for the intended output, and verify readable text, chart labels and source credits.",
            ),
        ]
    )
    return modules
