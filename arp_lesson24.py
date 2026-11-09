"""Original English guidance for communication, team handoffs and a stakeholder speech."""

from pathlib import Path

ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "arp"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
COURSE_CODE = "FI1BBAR05"
CHECKED_ON = "2026-11-09"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81736"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22937&chapterid=81743"
KAGGLE_URL = "https://www.kaggle.com/datasets"
METHOD = "Team leadership and evidence-based presentation"
ROLE_NOTE = (
    "Default route: hypothetical team leader, focusing on leadership responsibilities. "
    "Alternatively, work with classmates in the named roles, or work alone as Anna, Ben or Chris. "
    "State your chosen route and role in the draft. The team deliverable map describes the whole project; "
    "it does not mean a solo learner must pretend to have performed every role. Record proposed assignments "
    "as plans and actual contributions as evidence. For a solo role, focus feedback on that person's contribution "
    "and explain dependencies; do not silently demand the team leader's speech from Ben, Anna or Chris."
)
SHORTLIST_NOTE = (
    "Q1 assigns the dataset shortlist to Anna and Chris. The final deliverables say 'each team member' "
    "should present 1–2 potential datasets. The counting scope is ambiguous: record the interpretation and "
    "confirm with the tutor whether it includes every team member. The blank shortlist starts with Anna and Chris; "
    "add member rows if required. Do not silently turn this into a fixed total."
)
BOUNDARY = (
    "Task 2.4 concerns communication as a data analyst: choose a relevant Kaggle dataset, coordinate EDA, "
    "a comprehensive report and an evidence-based persuasive stakeholder speech. "
    + ROLE_NOTE
    + " "
    "Q1: introduce the team leader, Anna, Ben and Chris; delegate dataset selection to Anna and Chris. "
    "Q2: Ben leads EDA, inspecting structure, descriptive statistics, trends, visualisations and supported insights. "
    "Q3: Anna handles report structure, coherence and logical flow; Chris handles visuals and concise explanations, "
    "using Ben's findings. Q4: the team leader writes the stakeholder speech on dataset relevance, findings and impact. "
    "The speech must be at least two pages long, approximately 800–1000 words, well organised and submitted along "
    "with the report. Approximately is guidance, not a hard 1000-word maximum; check actual page layout separately. "
    + SHORTLIST_NOTE
    + " "
    "The team outputs are dataset selection with relevance descriptions, Ben's EDA summary, Anna/Chris's "
    "comprehensive report with relevant visuals, and the leader's speech. No dataset or completed EDA is supplied. "
    "Do not invent data, numerical results, actual collaboration, sources read or completed checks. Hypothetical "
    "plans must remain labelled as plans; an evidence gap must remain visible in a speech draft. No mandatory "
    "PowerPoint, GIMP project, image export, recording upload, report word count, chart count or citation style is "
    "specified here. Trace data/visual sources and reuse terms. Important insights are not automatically statistically "
    "significant; correlation does not establish causation. Imagegen illustrations are conceptual study aids, not "
    "learner analysis or project evidence. Exam Resolver reviews English notes and the selected step/role; it cannot "
    "certify unseen calculations, real teamwork, manuscript page count or speech delivery. Inspect actual files and "
    "submit them yourself."
)
RESOLVER_REQUEST = (
    "Review my Task 2.4 communication and team plan in English, following the current selected step and the route/role "
    "stated in my draft. If the role is unspecified, use hypothetical team leader and state that assumption. "
    "Check the four questions, role-specific contribution, dataset shortlist ambiguity, EDA-to-report handoff, "
    "audience, language/voice/tenses and evidence-based speech structure. Distinguish planned work from verified "
    "findings. Keep missing data and dependencies visible; ask for actual evidence instead of inventing findings "
    "or completed teamwork. For the leader's manuscript check at least two pages and approximately 800–1000 words "
    "without pretending that notes prove pagination. Explain corrections step by step. I will inspect and submit my files myself."
)
STEPS = [
    (
        "1. Choose your route and introduce the team",
        "State hypothetical team leader (default), actual group, or solo Anna/Ben/Chris in the working plan. For the leader route, introduce yourself and Anna, Ben and Chris, then explain the project purpose and proposed responsibilities. For an alternative route, identify your actual contribution and the inputs you need from other roles. Agree an audience, decision question and checkpoints; distinguish proposed assignments from work actually done.",
        "The default brief asks you to focus on leadership. The team output map is not proof that every learner must personally complete every role.",
    ),
    (
        "2. Coordinate the Kaggle dataset shortlist",
        "Assign Anna and Chris to propose relevant Kaggle datasets. Record each candidate's creator, URL, version, original source if linked, variables, scope, reuse terms and a brief relevance reason. Compare suitability for the team's question and record the choice and reason. The final deliverables mention 1–2 candidates per team member; record how you interpret this and seek clarification on who is included. Add rows to the shortlist if needed.",
        "No dataset is preselected. Public availability is not a quality or reuse guarantee. Do not silently fix the ambiguous shortlist total.",
    ),
    (
        "3. Assign Ben's EDA and define the handoff",
        "Ask Ben to profile the chosen dataset: row meaning, variables, units, missingness, potential duplicates and preparation decisions. Request appropriate descriptive statistics and visualisations of relevant patterns. For each actual finding, record the source file/range, method, denominator, filters, chart and limits. As leader, define this handoff and review its completeness; as solo Ben, perform and document your own EDA. Leave absent results pending.",
        "A planned chart is not a result. Do not invent data or p-values, treat missing values as zeros, or call an interesting observation statistically significant without the necessary analysis.",
    ),
    (
        "4. Coordinate Anna and Chris's comprehensive report",
        "Give Anna responsibility for the report's structure, coherent argument and logical flow. Give Chris responsibility for appropriate visualisations, readable labels and concise explanations. Use the report outline to connect purpose, data/preparation, actual EDA findings, interpretation, limitations, recommendations and references. Agree a version and review point. For a solo role, complete that contribution and identify any unavailable handoff honestly.",
        "Every reported result must trace to Ben's actual evidence or your own documented EDA. This task gives no fixed report word count or mandatory number of charts.",
    ),
    (
        "5. Plan the audience, language and speech story",
        "Profile the stakeholders: what decision matters, what they already know and what technical detail needs explanation. Select supported findings and translate each into a plain-language meaning and a proportionate implication. Use formal, precise wording and active voice where clear. Use past tense for completed work, future for plans, present for general/current claims and conditional language for hypothetical outcomes. Plan an engaging, truthful opener and a focused narrative.",
        "Adapting detail must preserve facts, units and uncertainty. Third person is common in formal reports, not an absolute ban on first person in a speech.",
    ),
    (
        "6. Draft the leader's stakeholder speech",
        "For the team leader route, write a well-organised manuscript: opener/purpose, dataset relevance and preparation, concise methods, supported findings, meaning/impact, limits, recommendations and a clear closing/call to action. Use the speech template as a scaffold, not a completed answer. Aim for approximately 800–1000 words and check that the formatted speech is at least two pages. If findings are unavailable, retain explicit evidence-needed markers and do not present the draft as final. Solo Anna/Ben/Chris can supply role-specific talking points and identify the leader dependency.",
        "Two pages is a minimum; the word range is approximate guidance. Word count does not prove page count. The speech manuscript accompanies the report; no recording upload or compulsory slide deck is stated.",
    ),
    (
        "7. Rehearse, review and inspect the submission files",
        "Read the speech aloud, check transitions, pacing and clarity, and prepare answers about data sources, methods, assumptions and limits. Record feedback and revisions only when they occur. Reconcile claims across the EDA summary, report, visuals and speech. Check sources, actual word/page counts, placeholder removal and role-specific deliverables. Prepare Task 2.4 in Exam Resolver for English feedback, update the actual files, reopen them and check the submission instructions before submitting yourself.",
        "Written notes cannot certify actual teamwork, calculations, page layout or delivery. Keep unperformed checks marked Not checked and unresolved scope questions visible.",
    ),
]
CHECKS = [
    (
        "Route and contribution",
        "Chosen route/role is explicit; hypothetical assignments and real contributions are distinguished.",
    ),
    (
        "Dataset shortlist",
        "Candidate relevance, Kaggle provenance and reuse checks are recorded; the each-member counting ambiguity is resolved or flagged.",
    ),
    (
        "EDA handoff",
        "Ben's actual findings trace to data, methods, units, filters and charts; unavailable evidence remains pending.",
    ),
    (
        "Report roles",
        "Anna's structure and Chris's visuals/explanations connect to verified EDA; references and limits are included.",
    ),
    (
        "Audience and language",
        "The narrative supports the stakeholder decision, with precise language, suitable tenses and cautious interpretation.",
    ),
    (
        "Leader's speech",
        "At least two actual pages, approximately 800–1000 words, well organised and accompanying the report; alternative roles identify dependencies.",
    ),
    (
        "Files and rehearsal",
        "Actual files reopened, claims reconciled, placeholders removed; feedback/rehearsal claimed only if performed. Learner submits.",
    ),
]
QUESTION_TEMPLATE = """# ARP Task 2.4 Communication and team plan

Working scaffold, not a completed submission. Replace prompts with your own work.

## Route and role
Route: [Hypothetical team leader by default / actual group / solo Anna, Ben or Chris]
My name, selected role and personal contribution: [...]
Actual collaborators, if any (otherwise hypothetical): [...]
Leader introduction and proposed responsibilities for Anna, Ben and Chris: [...]
Stakeholder audience, decision question and milestones: [...]

## Dataset shortlist and selection
Anna/Chris candidates with Kaggle URLs, creator, version and relevance: [...]
Original source, scope, variables and reuse terms checked: [Not checked]
Shortlist counting scope: [Q1 assigns Anna/Chris; final wording says each team member proposes 1–2. Interpretation and tutor clarification pending.]
Selected dataset and selection reason (or Pending): [...]

## Ben's EDA handoff
Proposed analysis instructions, input/output and review point: [...]
Actual data structure, descriptive statistics, visualisations and evidence locations: [Pending]
Verified finding, method, units, denominator, filters, chart and limitations: [Pending]
What I performed versus what I am requesting from another role: [...]

## Anna and Chris's report
Anna: outline, coherence and logical flow: [...]
Chris: visuals, labels and concise explanations: [...]
Actual evidence received, version and unresolved dependencies: [Pending]
Data/visual references and limitations: [...]

## Audience and speech
Stakeholder purpose and technical-detail level: [...]
Supported key message, finding and traceable evidence: [Pending]
Opener -> relevance/method -> findings -> meaning/limits -> action -> closing: [...]
Leader's manuscript or my role-specific contribution: [...]
Tense/voice review, cautious language and likely questions: [...]
Actual speech word count: [Not checked; approximately 800–1000 words]
Actual formatted speech page count: [Not checked; at least two pages]
Report and speech accompanying each other for leader route: [Not checked]

## Final checks
Claims reconciled with actual EDA and references: [Not checked]
Rehearsal/feedback actually completed and changes made: [Not performed]
Actual files reopened; all placeholders removed: [Not checked]
Unresolved scope question, missing evidence and next action: [...]
I will inspect the actual files and submit them myself.
"""
REPORT_TEMPLATE = """# Task 2.4 Comprehensive report outline

Original blank scaffold. Anna: structure/coherence. Chris: visuals and concise explanations.
Use Ben's actual EDA evidence; no dataset or results are supplied. A solo role should identify missing dependencies.

1. Purpose and audience: [Decision, question and scope]
2. Dataset and preparation: [Kaggle URL, creator, version, original source, row meaning, units, quality checks and changes]
3. EDA methods: [Actual descriptive statistics, groupings, filters and chart choices, with evidence locations]
4. Findings: [Verified observation, measure, units, denominator, chart, source and relevant limit for each claim]
5. Interpretation: [What the evidence supports and what it cannot establish]
6. Recommendations: [Proportionate action, responsible owner, uncertainty and next check]
7. Limitations: [Coverage, missingness, bias, assumptions and unavailable evidence]
8. References and visual credits: [Traceable source entries and required reuse attribution]

Anna's coherence check: [Not checked]
Chris's visual labels, scales and explanation check: [Not checked]
Reconciliation with Ben's EDA and leader's speech: [Not checked]
Actual saved file/version opened and checked: [Not checked]

The task prescribes no report word count, chart count or citation style. Follow any additional tutor instructions.
"""
SPEECH_TEMPLATE = """# Task 2.4 Stakeholder speech manuscript

Leader's working scaffold, not a ready-to-submit speech. Write your own connected prose from actual evidence.
For solo Anna/Ben/Chris, supply role-specific input and flag the leader dependency instead of claiming all roles.
Required length: at least two pages; approximately 800–1000 words. Verify actual formatting and page count separately.
The speech is submitted along with the report. A recording or slide deck is not stated as compulsory.

## Audience and purpose (planning notes; remove from final manuscript)
Stakeholder group and decision: [...]
One main message supported by actual analysis: [Evidence needed]
Data/visual sources and supporting evidence locations: [...]

## Opener and purpose
[Write a truthful hook, introduce your role/team where appropriate, explain the question and why the audience should care.]

## Dataset relevance and approach
[Identify the actual Kaggle dataset, creator/version and scope. Briefly explain preparation and EDA methods actually used.]

## Key findings and meaning
[Present supported observations with units, comparison, denominator and appropriate visual cues. Explain meaning in plain English. No findings are supplied by this template.]
[Evidence needed: retain this marker while results are unavailable; do not fabricate numbers or team accomplishments.]

## Impact, limits and recommended action
[Explain proportionate implications, uncertainty, sample limitations and what cannot be inferred. State a practical recommendation tied to evidence and a next check.]

## Closing and questions
[Restate the useful message, a proportionate call to action and a clear closing. Prepare answers on sources, methods and limits.]

## Review log (remove from final manuscript)
Actual manuscript words: [Not checked; approximately 800–1000]
Actual formatted pages: [Not checked; minimum two]
Formal/precise language, active voice where suitable, tenses matching actual work: [Not checked]
Read aloud, timing, feedback and revision actually performed: [Not performed]
Claims agree with EDA/report; sources included; no prompts remain: [Not checked]
Actual speech file reopened and accompanies the report: [Not checked]
"""
ILLUSTRATIONS = [
    dict(
        file="lesson-2-4-evidence-to-audience.png",
        title="From evidence to understanding",
        caption="Translate evidence into meaning and a proportionate action. Adapt detail to the audience while preserving facts, sources and limits. Choose tenses according to whether work is completed, planned, general or hypothetical.",
    ),
    dict(
        file="task-2-4-team-handoffs.png",
        title="Team roles and evidence handoffs",
        caption="Anna and Chris shortlist data; Ben leads EDA; Anna structures the report and Chris explains its visuals; the leader prepares the stakeholder speech. Default: hypothetical leader. Alternatives: real group or solo Anna/Ben/Chris. The speech is at least two pages, approximately 800–1000 words. This is a process map, not proof of completed teamwork.",
    ),
]
DOWNLOADS = [
    (
        "ARP Task 2.4 Communication Plan.md",
        "Download communication and team plan (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.4 Dataset Shortlist.csv",
        "Download dataset shortlist (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.4 Roles and Handoffs.csv",
        "Download roles and handoffs (CSV)",
        "text/csv",
    ),
    ("ARP Task 2.4 EDA Handoff.csv", "Download EDA evidence handoff (CSV)", "text/csv"),
    (
        "ARP Task 2.4 Report Outline.md",
        "Download comprehensive report outline (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.4 Speech Manuscript.md",
        "Download stakeholder speech template (Markdown)",
        "text/markdown",
    ),
    (
        "ARP Task 2.4 Review Checklist.csv",
        "Download communication and file checklist (CSV)",
        "text/csv",
    ),
    (
        "ARP Task 2.4 Seven Step Guide.md",
        "Download seven-step communication guide (Markdown)",
        "text/markdown",
    ),
]
GUIDE = dict(
    course_code=COURSE_CODE,
    id="2.4-task",
    uid="arp-2.4-task-81743",
    lesson_number="2.4",
    title="Communicate EDA findings as a team",
    source_url=TASK_URL,
    method=METHOD,
    deliverable="Role-specific contribution to a Kaggle dataset shortlist, EDA summary, comprehensive report and stakeholder speech. Default hypothetical leader: introduce/delegate/review and write the speech (at least two pages, approximately 800–1000 words), submitted with the report. Group and solo Anna/Ben/Chris alternatives are explained below.",
    steps=[instruction for _, instruction, _ in STEPS],
    caution=BOUNDARY,
    task_dataset="Learner-selected Kaggle dataset; none supplied.",
    template_file=DOWNLOADS[0][0],
)
REVIEW_CONTEXT = (
    "Role-sensitive communication review: "
    + ROLE_NOTE
    + " "
    + SHORTLIST_NOTE
    + f" Original lesson: {LESSON_URL} Original task: {TASK_URL} Checked {CHECKED_ON}. "
    "Use the route/role in the student draft. Reconcile claims across EDA, report and speech. "
    "Review manuscript pagination only from actual page evidence, not inferred from words or notes."
)
LESSON_CONTENT = """## Communication as a Data Analyst

The analytical result is useful only when someone can understand it, assess its limits and decide what to do. This lesson connects clear writing, public speaking and teamwork. The explanations and templates below are original Study Buddy learning aids based on the linked Noroff lesson, not an official solution.

### 1 Make the evidence useful to the audience

Start with a decision question: who needs this information and what could they decide? A technical colleague may need preparation steps, formulas and reproducible methods. A stakeholder may first need the message, business meaning and a proportionate action. Both need the same honest facts, units, sources and relevant uncertainty. Simplifying the explanation must not change the result.

Use a chain you can defend: **evidence → observation → interpretation → recommendation**. Keep each link distinct. An observation describes what the data show; an interpretation explains a possible meaning; a recommendation proposes action. If evidence is unavailable, state what is needed rather than presenting a plan as a finding. Clear source and method notes build trust, allow review and reduce misinterpretation.

### 2 Choose precise language, voice and tenses

Use formal, plain language and explain specialist terms when the audience needs them. Active voice often makes responsibilities clearer. Third person is common in formal reports, but is not a universal rule for every report or speech. Follow the brief and use a consistent perspective that makes sense for the audience.

| Situation | Tense/voice choice | Original language example |
|---|---|---|
| General explanation | Present | A histogram shows a numerical distribution. |
| Completed action | Past | The analyst checked the recorded date range. |
| Planned action | Future | Ben will inspect missing values before summarising the data. |
| Hypothetical outcome | Conditional | If coverage were incomplete, the comparison could be misleading. |

These sentences illustrate grammar, not work performed by your team. Consistency does not mean forcing every sentence into one tense: the tense should match the status of the claim. Prefer precise nouns, defined measures and short transitions. Use cautious wording when evidence is limited. An interesting or important pattern is not automatically statistically significant, and a correlation alone does not establish cause.

### 3 Prepare before speaking

Know the dataset's origin, variables, units, coverage, preparation decisions and limitations. Profile the audience's knowledge and interests. Choose a central message, an honest opener and the evidence needed to support it. A question can be a hook without inventing a striking statistic. Choose visuals that explain the message, with readable labels and sources; decorative graphics cannot establish a result.

Prepare for questions about sources, methods, missingness, bias, denominators and recommendations. It is acceptable to say that a point needs checking, then identify the next step. Confidence comes from knowing what the evidence supports and where it stops. Rehearse, listen for jargon, check pacing and revise from real feedback.

### 4 Build a coherent speech

A useful narrative is **purpose → dataset/context → approach → findings → meaning/limits → action → closing**. Explain why the question matters, how the evidence was obtained, what it shows and what should happen next. Weave examples and visual cues into this structure where they clarify actual findings. The lesson's suggested sections can be combined; they are not a compulsory set of separate headings.

For Task 2.4, the leader's speech must be at least two pages long, with approximately 800–1000 words as guidance. This is not an exact two-page limit or a hard 1000-word maximum. Check the actual formatted manuscript: a word count cannot establish pagination. Submit the speech along with the report. The brief does not state a compulsory recording or PowerPoint deck.

### 5 Make teamwork visible through useful handoffs

Divide work according to strengths, define inputs and outputs, and agree review points. Document versions, assumptions, decisions and unresolved issues so another person can continue the work. A handoff should contain enough detail to check the result, rather than just an attractive chart. Peer review can expose errors and challenge assumptions; it does not automatically eliminate bias. Resolve disagreements by returning to the question, evidence and agreed quality criteria.

| Role | Assigned responsibility | Useful handoff |
|---|---|---|
| Anna + Chris | Propose relevant Kaggle datasets | Candidate links, provenance, scope and relevance comparison |
| Ben | Lead EDA | Structure, descriptive summaries, appropriate charts, supported observations and limits |
| Anna | Report structure and coherence | Logical outline and consistent argument based on Ben's evidence |
| Chris | Visuals and concise explanations | Readable charts with labels, sources and evidence-based captions |
| Team leader | Introduce, delegate, coordinate and communicate | Clear plan, review decisions and persuasive stakeholder speech |

Keep assignment, execution and review separate. In a hypothetical scenario, write that a person *will* do something; do not claim that person already did it. In real group work, record actual contributions. The default task route is hypothetical team leader and focuses on leadership aspects. Alternatives allow classmates to take the named roles or an individual to work as Anna, Ben or Chris. Your personal contribution should follow the chosen route rather than pretending to be a completed four-person team.

### 6 Apply the four questions without inventing missing work

Q1 asks for introductions and a dataset selection assignment to Anna and Chris. Q2 delegates the EDA to Ben. Q3 divides the report between Anna's structure and Chris's visual explanations. Q4 asks the leader for the stakeholder speech. Use the seven learning steps below to plan and check these four questions; seven steps are a learning scaffold, not seven additional official questions.

The final deliverables describe dataset selection, an EDA summary, a comprehensive report and the leader's speech. They say each team member should propose 1–2 datasets, while Q1 names Anna and Chris. Record that ambiguity and confirm the counting scope with the tutor if needed. The shortlist template begins with Anna and Chris and can be extended; it does not resolve the ambiguity on Noroff's behalf.

No dataset or numerical findings are supplied. Keep evidence-dependent sections pending until you have actual data and analysis. The blank Markdown and CSV templates support your own work; they are not completed reports, speeches or Excel calculations. The two imagegen illustrations explain communication and role handoffs, not your analytical results.

### 7 Review the evidence and actual files

Check that the EDA summary, report, chart labels and speech agree. Preserve sources, units, denominators, limits and appropriate attribution for external visuals. Keep recommendations proportionate. Remove planning prompts before finalising, reopen the actual files, check the speech's word count and at-least-two-page layout, and follow the submission instructions for your chosen role.

Use **Prepare Task 2.4 in Exam Resolver** to transfer your draft and selected learning step for English review. Put your route/role at the top of the draft. Resolver can identify gaps, explain the next action and review the written argument; written notes alone cannot certify calculations, teamwork, page layout or speech delivery. Make the changes in the actual files, inspect them and submit them yourself.
"""


def guide_markdown():
    parts = [
        "# ARP Task 2.4 — seven-step communication guide",
        f"Original task: {TASK_URL}\n\nChecked {CHECKED_ON}. Original Study Buddy guidance, not an official solution.",
        "## Route and role\n\n" + ROLE_NOTE,
        "## Task boundary\n\n" + BOUNDARY,
    ]
    parts.extend(f"## {t}\n\n{i}\n\nCheck: {c}" for t, i, c in STEPS)
    parts.append("## Final checks\n\n" + "\n".join(f"- {t}: {d}" for t, d in CHECKS))
    return "\n\n".join(parts) + "\n"
