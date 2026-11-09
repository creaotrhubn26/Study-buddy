"""Original English study material for ARP 2.1, checked against Noroff and dated evidence."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
CHECKED_ON = "2026-11-09"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81710"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81721"
BOUNDARY = (
    "Task 2.1 asks for a one-page report evaluating all three supplied articles (A NaturalNews, B BeforeItsNews, C WND) "
    "and explaining whether each can be considered a reliable information source. Judge specific claims with evidence, "
    "not the author's politics or loaded tone alone. A repost is not independent corroboration. A verified event does not "
    "validate every interpretation or causal claim. The brief specifies no word count, minimum citation count, Harvard style, "
    "font, particular software, dataset, Excel chart, PowerPoint or required images. Do not import another task's requirements. "
    "Use traceable references and keep the actual saved report to one readable page; confirm any separate reference-page "
    "arrangement with the tutor. Historical articles are dated February 2023: distinguish contemporaneous evidence from "
    "later updates. The source notes below are Study Buddy checks, not proof that the student read or verified sources. "
    "Do not invent source-reading results, authors, statistics, citations or access dates. Review the selected step and "
    "student draft in English; flag unverified claims and placeholders. The learner checks the actual file and submits it."
)
RESOLVER_REQUEST = (
    "Review my one-page source-reliability report and verification notes in English. Follow my selected Task 2.1 step. "
    "Cover NaturalNews, BeforeItsNews and WND separately, explaining claim, evidence, limitation and qualified judgement. "
    "Check provenance, republication, dates, independent corroboration and statistical scope. Separate what the article says "
    "from the dated primary-source checks and from my own verified reading. Do not infer a completed source check from a "
    "template or give a blanket verdict based only on tone. Flag missing citations and unsupported inferences. I will check "
    "the saved one-page report and submit it myself."
)
STEPS = [
    (
        "1. Decode the one-page brief",
        "Open the original task. Create a working document for a one-page report covering all three articles. Use the same criteria for each: authorship/provenance, evidence, independent verification, date/context and the fit between evidence and conclusion. A word processor is sufficient; learning about notebooks does not make a notebook a task requirement.",
        "All three articles need a reasoned judgement. No 500-word target, minimum citation count or compulsory Harvard style is stated for this task.",
    ),
    (
        "2. Record the three article identities",
        "Open A, B and C from the article cards. Record the actual displayed author, publisher, publication date, URL and your access date. Trace the original publisher of syndicated material. The task labels B Citizen Free Press, but the accessible page credits Atlas Shrugs and links GellerReport; WND also credits Jennie Taer / Daily Caller News Foundation within the story. Record these attribution chains instead of silently treating reposts as separate witnesses.",
        "Record what you actually opened. Article-body review does not mean every embedded video, social post or outgoing link has been checked.",
    ),
    (
        "3. Separate claims from interpretation",
        "For each article select its central checkable assertion and the broader conclusion built on it. In A distinguish reported airborne-object incidents from a coordinated psyop allegation. In B distinguish the derailment/chemical-release event from media-blackout and nuclear analogies. In C distinguish the sector-specific count and percentage from broader explanations about immigration. Put claim, evidence, uncertainty and provisional verdict in separate matrix columns.",
        "Emotive language warrants scrutiny but does not itself refute a fact. A genuine event does not prove the article's explanation of intent or cause.",
    ),
    (
        "4. Trace and check primary evidence",
        "Compare the selected claims with the dated primary links in the source notes. Check what each source actually establishes and what it leaves open. For C, CBP's 13 February 2023 release reports 367 January apprehensions/encounters in Swanton and approximately 846% growth for 1 October 2022–31 January 2023 versus the same FY22 period. That is not all northern-border activity or a count guaranteed to represent unique people. Distinguish a contemporaneous release from a later updated background page.",
        "Record the exact scope and dates, not just a matching number. An 846% increase means approximately 9.46 times the baseline. Do not invent baseline counts to reproduce a rounded percentage.",
    ),
    (
        "5. Make a qualified judgement for each article",
        "Use the pattern: claim → supporting/contradicting evidence → limit → judgement. A can report real incidents while its coordinated-psyop conclusion lacks demonstrated evidence. B can describe a serious chemical incident while its blackout/nuclear framing needs separate support. C's specific 846% statistic is corroborated by CBP, while the near-900% headline, sector scope and causal claims still need qualification. These are worked reasoning notes to test against your reading, not a required official answer.",
        "Answer reliable for which purpose and claim. Do not dismiss every statement in all three articles, or treat an official source as automatically complete and infallible.",
    ),
    (
        "6. Draft a concise one-page report",
        "Use the report scaffold: short purpose/method, one compact evidence-based paragraph per article and a comparative conclusion. For each article explain both a concrete strength or supported fact and a limitation affecting reliability. Cite the original article and the primary evidence where used. Condense repeated background rather than shrinking text until it is unreadable. The scaffold and notes are working aids, not the final formatted page.",
        "All three judgements need reasons tied to sources. Use a consistent reference format. Do not add Task 1.3's word-count or Harvard requirements to this brief.",
    ),
    (
        "7. Verify the saved page and review in Exam Resolver",
        "Replace placeholders with your own reading and verified references. Reopen the saved report, inspect readability and actual page count, and check dates, attributions, paraphrases, URLs and numerical scope. Prepare Task 2.1 in Exam Resolver for English feedback on the selected step and your current draft. Resolve flagged gaps in your actual document and submit the report yourself.",
        "Study Buddy can review text and notes; it cannot certify an unseen document's page count or that you opened a source. Images are study aids, not required evidence or a completed report.",
    ),
]
ARTICLES = [
    dict(
        id="A",
        label="NaturalNews · airborne-object / psyop claim",
        publisher="NaturalNews",
        attribution="Mike Adams; published 13 February 2023",
        url="https://www.naturalnews.com/2023-02-13-fake-alien-invasion-psyop-tested-americans.html",
        note="Body reviewed. Separate documented shoot-down events from the unsupported inference of an organised deception. The article does not establish the claimed intent merely by linking reports of objects.",
    ),
    dict(
        id="B",
        label="BeforeItsNews · East Palestine chemical incident",
        publisher="BeforeItsNews",
        attribution="Task label: Citizen Free Press. Live page: Atlas Shrugs, linking GellerReport; published 13 February 2023",
        url="https://beforeitsnews.com/opinion-conservative/2023/02/we-nuked-a-town-media-blackout-on-catastrophic-environmental-disaster-in-ohio-caused-by-large-controlled-explosion-journalists-covering-it-arrested-3654809.html",
        note="Body reviewed in the browser; automated text retrieval failed. Embedded videos/social posts were not exhaustively verified. The body itself cites mainstream reporting, which weakens an absolute no-coverage claim. Chemical danger is real; nuclear analogies and claims about suppression need separate evidence. Reporter-arrest claims are not independently resolved in these notes.",
    ),
    dict(
        id="C",
        label="WND · Swanton Sector encounter growth",
        publisher="WND",
        attribution="Task label: WND News Services. Live page: Around the Web; story credits Jennie Taer / Daily Caller News Foundation; published 13 February 2023",
        url="https://www.wnd.com/2023/02/not-just-mexico-now-northern-border-sector-sees-900-increase-illegals/",
        note="Body reviewed. Its roughly 846% figure is supported by the linked CBP release; the near-900% headline is less precise. Keep Swanton Sector, fiscal-year comparison and encounter/apprehension scope. Syndication is not independent corroboration; wider causal assertions need separate checks.",
    ),
]
PRIMARY_NOTES = [
    dict(
        id="P1",
        label="Canada National Defence · 11 February 2023",
        url="https://www.canada.ca/en/department-national-defence/news/2023/02/minister-anandprovides-an-important-national-security-update.html",
        note="Read contemporaneous statement: NORAD downed an object over Yukon; capabilities, purpose and origin were not established in that statement. It supports the incident, not A's coordinated-psyop inference.",
    ),
    dict(
        id="P2",
        label="Ohio EMA · 6 February 2023",
        url="https://ema.ohio.gov/media-publications/news/dewine-020623",
        note="Read contemporaneous announcement in browser: planned controlled release/burning of vinyl chloride to address an explosion risk, with evacuation and serious fume warnings. Supports the announced chemical-response plan, not nuclear terminology, a media blackout or a universal health/safety conclusion.",
    ),
    dict(
        id="P3",
        label="US EPA · later updated incident background",
        url="https://www.epa.gov/east-palestine-oh-train-derailment",
        note="Read current background page: derailment on 3 February 2023 and hazardous cargo. It includes later monitoring updates, so label it retrospective and do not imply all content was available on 13 February 2023. No blanket health conclusion follows.",
    ),
    dict(
        id="P4",
        label="US CBP · 13 February 2023 · archived release",
        url="https://www.cbp.gov/newsroom/local-media-release/border-patrol-s-swanton-sector-apprehensions-encounters-reach-historic",
        note="Read in browser after automated retrieval returned 403. Reports 367 January FY23 Swanton apprehensions/encounters and approximately 846% increase for 1 October 2022–31 January 2023 against the same FY22 period. Confirms that narrow statistic, not a nationwide total, guaranteed unique-person count or the article's causal narrative. Page now marked archived and last modified 27 January 2025.",
    ),
]


def source_notes_markdown():
    parts = [
        "## Reviewed source notes",
        f"Study Buddy review: {CHECKED_ON}. Original analysis notes, not an official solution or proof of learner reading. These checks cover selected claims, not every linked item.",
    ]
    for source in ARTICLES:
        parts.append(
            f"### Article {source['id']} · {source['label']}\n\n[{source['publisher']} article]({source['url']})\n\nAttribution: {source['attribution']}.\n\n{source['note']}"
        )
    parts.append("## Primary evidence and limits")
    for source in PRIMARY_NOTES:
        parts.append(
            f"**{source['id']} · [{source['label']}]({source['url']})**\n\n{source['note']}"
        )
    parts.append(
        "Use these as research starting points. Record your own access dates, reading notes and any unavailable source. Do not present later findings as evidence available to the original author."
    )
    return "\n\n".join(parts) + "\n"


REVIEW_CONTEXT = "Dated Study Buddy source checks (not student verification):\n" + "\n".join(
    f"{s['id']}: {s.get('attribution', s.get('label', ''))}. {s['note']} Source: {s['url']}"
    for s in ARTICLES + PRIMARY_NOTES
)
QUESTION_TEMPLATE = """# Task 2.1 — one-page source-reliability report

Working scaffold: replace brackets with your own verified evidence, then format and inspect one readable page. Remove these instructions from the final report. The brief sets no word count or compulsory citation style.

## Purpose and method
[State the purpose and common reliability criteria: provenance, evidence, independent checks, date/context and whether conclusions follow.]

## Article A — NaturalNews
[Identify the article/date/author. Separate a checkable event from the broader psyop interpretation. Explain what evidence supports, what remains unproven, and your qualified judgement. Cite sources actually read.]

## Article B — BeforeItsNews
[Record the actual attribution/repost chain. Distinguish the chemical incident from claims about coverage, suppression and nuclear analogies. Cite evidence and state verification limits. Explain your qualified judgement.]

## Article C — WND
[Trace the original author and CBP source. Check the approximately 846% figure, Swanton Sector, October–January FY23 comparison and 367 January count. Explain which claim is supported and why it does not validate every broader conclusion.]

## Comparative conclusion
[Answer which source is usable for which claim and purpose; explain any preference for primary records and remaining uncertainty.]

## References
[Consistent references to articles and evidence actually used. No fixed minimum or mandatory Harvard style is specified. Keep the report to one page; confirm any separate reference-page arrangement if needed.]

Working verification notes — remove from final page:
My actual sources opened, access dates and claim/evidence/limit notes: [...]
Sources unavailable or not checked, including embedded media: [...]
Contemporaneous evidence distinguished from later updates: [Not checked]
Saved report reopened, readable and one page: [Not checked]
References and placeholders checked: [Not checked]
I will inspect the actual file and submit it myself.
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-2-1-reporting-workflows.png",
        title="Choose a reporting workflow",
        caption="A word processor supports narrative layout; Report Builder designs paginated output; Jupyter .ipynb notebooks combine code and explanation; R Markdown .Rmd renders prose and code. Plain Markdown does not execute analysis by itself. Choose for the audience, data and reproducibility; check generated claims.",
    ),
    dict(
        file="task-2-1-claim-verification.png",
        title="From article claim to reliability judgement",
        caption="Apply the same process to A, B and C: record a claim, trace its source, check dates/context/numbers, separate evidence from interpretation, and write a qualified judgement. A repost is not independent corroboration; biased wording alone does not prove falsehood. The output is one page covering all three articles.",
    ),
]
DOWNLOADS = [
    (
        "ARP Task 2.1 One Page Reliability Report.md",
        "Download one-page report scaffold (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.1 Claim Verification Matrix.csv",
        "Download claim verification matrix (CSV)",
        "text/csv",
    ),
    (
        "ARP Lesson 2.1 Tool Choice Matrix.csv",
        "Download reporting tool choice matrix (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.1 Reviewed Source Notes.md",
        "Download reviewed source notes (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.1 Seven Step Guide.md",
        "Download seven-step critical reading guide (Markdown)",
        "text/markdown",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="2.1-task",
    uid="arp-2.1-task-81721",
    lesson_number="2.1",
    title="Critical reading — three-article reliability report",
    source_url=TASK_URL,
    method="Critical reading and source reliability",
    deliverable="One-page report evaluating the reliability of all three supplied articles with explained findings",
    steps=[s[1] for s in STEPS],
    caution=BOUNDARY,
    task_dataset="",
    template_file=DOWNLOADS[0][0],
)
LESSON_CONTENT = """### Lesson 2.1 Report-generating Tools

Reporting connects a question, evidence, analysis and a readable output. A tool can organise this process, but it cannot make unsupported conclusions reliable. This lesson covers writing tools, repeatable analytical documents, AI assistance and critical reading. Task 2.1 applies the critical-reading part to three news articles in a one-page report.

### 1 Choose the workflow for the reader

Start with the audience, purpose and delivery format. Ask whether the report is a one-off narrative or a recurring output from changing data; whether readers need print layout or exploration; and whether another analyst must rerun the analysis. Record data access, privacy, dependencies and the cost of maintaining the workflow.

| Workflow | Suitable use | Verification need |
|---|---|---|
| Word, Pages, Google Docs or Writer | A narrative report edited visually | Heading structure, citations, compatibility and exported pages |
| LaTeX | Structured typesetting, especially complex mathematics | Compile with the required packages/fonts; check output and environment |
| Power BI Report Builder | Paginated reports with controlled page layout | Data queries, parameters, totals and page breaks |
| Jupyter notebook | Explain and execute analysis alongside results | Code execution order, data version and environment |
| R Markdown | Render prose and analytical code into a report | R/code dependencies, source data and rendered output |

LaTeX is a markup-and-compile workflow, rather than direct visual editing. Document appearance still depends on the environment; markup does not guarantee identical output everywhere. A simple word processor is sufficient for Task 2.1. No installation or tool purchase is required by this guide.

### 2 Understand paginated reporting

Power BI Report Builder creates page-based reports such as long tables and print-ready documents. This differs from interactive Power BI report pages and from the Power BI service's single-page dashboards. A repeating table header and predictable page breaks solve a different problem from interactive exploration. Check the final rendered pages, not only the designer preview. [Microsoft: paginated reports](https://learn.microsoft.com/en-us/power-bi/paginated-reports/paginated-reports-report-builder-power-bi).

### 3 Combine explanation and executable analysis

Jupyter documents use the **.ipynb** extension and combine code cells, Markdown explanations, equations and stored outputs. Kernels support different languages; Jupyter is not limited to Python. Stored output can be stale: restart the kernel and run the notebook in order with the intended data and environment before sharing. A static export does not provide a live data connection, and not every output is interactive. [Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html).

Plain Markdown describes text formatting; it does not itself execute analysis. **R Markdown (.Rmd)** adds executable code chunks to prose and renders their results through its reporting workflow. Rendering should use recorded inputs and dependencies so the next run is explainable. Inspect the output and keep the source file. [Posit: R Markdown documentation](https://rmarkdown.rstudio.com/docs/).

### 4 Use AI assistance with evidence checks

AI can help propose an outline, simplify wording or flag an unclear argument. A plausible sentence is not evidence, and a generated citation must be checked against the real source. Keep observed results separate from suggested explanations. The course's named AI services are historical examples; product availability and capabilities may have changed. Focus on the function and verify any current service before relying on it. Do not paste confidential data into an unapproved service.

### 5 Read critically before you report

Use a repeatable chain: **claim → original source → evidence → context → qualified judgement**. Identify the author and publisher, their expertise and incentives, the publication date, corrections and the links behind factual assertions. Separate an observable event from opinion, a causal inference or an allegation about intent. Check whether apparently separate stories merely repeat the same original report.

Bias can affect selection and framing without making every number false. Conversely, one accurate fact does not establish the rest of a narrative. Primary sources are useful because their scope is easier to inspect, but they also have methods, institutional perspectives and limitations. Judge reliability for a particular claim and intended use, rather than assigning an automatic credibility score to a publisher.

### 6 Read and present data ethically

Check measure, unit, denominator, geography, time window and source. A large percentage increase can begin from a small baseline; percentage changes differ from percentage-point changes. An 846% increase corresponds to about 9.46 times the baseline, not 8.46 times. Do not manufacture absolute counts from a rounded percentage.

Bar length normally needs a zero baseline to preserve magnitude comparisons. A clearly labelled zoomed line-chart axis can be useful, so a non-zero axis alone is not proof of deception. Unequal time intervals, selected start/end dates, omitted comparison groups and emotive colours can change the impression. Distinguish observations from forecasts and label model assumptions. Ask what is missing before drawing a conclusion.

### 7 Apply the lesson to Task 2.1

The task supplies NaturalNews, BeforeItsNews and WND articles from February 2023. Evaluate all three and explain the findings in one page. Use the walkthrough, blank verification matrix and reviewed source notes below. The source notes model checking selected claims; they are not an official solution or a record of your own reading. There is no required dataset, new chart, PowerPoint, image submission or prescribed word count. The two illustrations are conceptual study aids.
"""


def guide_markdown():
    parts = [
        "# ARP Task 2.1 — seven-step critical reading guide",
        f"Original task: {TASK_URL}\n\nReviewed {CHECKED_ON}. Original Study Buddy guidance, not an official solution.",
        "## Task boundary\n\n" + BOUNDARY,
    ]
    parts.extend(
        f"## {title}\n\n{instruction}\n\nCheck: {check}"
        for title, instruction, check in STEPS
    )
    parts.append(source_notes_markdown())
    return "\n\n".join(parts) + "\n"
