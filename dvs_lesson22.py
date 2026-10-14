"""English ethical visualisation teaching and reviewed Task 2.2 scaffolds."""
CONTENT_REVISION = '2026-10-14-dvs22'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81557'
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81562'
AXES_URL = 'https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines'
LINE_URL = 'https://digitalblog.ons.gov.uk/2016/06/27/does-the-axis-have-to-start-at-zero-part-1-line-charts/'
RULES = [
 ('Do not be picky with the numbers','Avoid cherry-picking values, periods or categories to support a preferred conclusion.','Define the relevant dataset, period and inclusion criteria before drawing the chart. Record exclusions and missing data and compare a selected view with the broader context.','A justified subset can be useful when its scope is clear; a subset is not automatically manipulation.'),
 ('Be aware of biases','Question assumptions and interpretations that favour your expected answer.','Write down your initial expectation, check conflicting evidence, and separate data observations from the story you infer.','Bias cannot be eliminated by claiming to be objective; document checks and limitations.'),
 ('Keep the graphs clear and non-confusing','Use faithful geometry, explicit labels, suitable scales, units and context.','Check positions against values, use a zero baseline for bars, explain time gaps and data status, and avoid perspective and colour cues that obscure interpretation.','A non-zero line-chart axis is not automatically misleading; justify the range and avoid treating truncated area or bar lengths as full magnitudes.'),
 ('Encourage third-party review','Ask someone else to check the chart and explain their first interpretation.','Compare their interpretation with the underlying data and intended message; record feedback and revise any mismatch.','A planned peer review is not completed feedback, and one reviewer does not certify accuracy or accessibility.'),
]
FIGURE_NOTES = '''### Screenshot evidence, not verified underlying statistics

**Figure 7 — unemployment (caption: 12 December 2011).** The visible November label is **8.6%**, but its plotted point appears close to the **9.0%** October/January levels and above March’s **8.8%** point. This is a label–position inconsistency to explain using the visible screenshot. Replot the values on a consistent scale after checking the original series. The vertical scale is approximately 8–10%; the zoom can amplify perceived change. A line may use a justified non-zero range, but the filled area and decorative perspective can encourage misleading magnitude comparisons. Distinguish that issue from the more direct misplaced-point evidence. Do not claim the Bureau of Labor Statistics source label independently verifies the displayed data.

**Figure 8 — public health expenditure (caption: 8 June 2021).** The bars start around **4.0%**, rather than zero, so their visible lengths exaggerate relative differences. The displayed **4.8%** and **7.0%** values have a magnitude ratio of about **1.46**, while idealised lengths above a 4.0% baseline would have ratio **3.75**. This arithmetic illustrates truncation using printed labels; it is not a pixel measurement or verification of actual expenditure. The displayed years include **2016, 2020, 2021, 2023 and 2027**, with visually similar category spacing despite unequal time gaps. Explain the risk if readers treat that spacing as an annual timeline; keep category labels explicit or use a proportional time axis. **2023 and 2027 are future years relative to the 2021 broadcast caption**, so clarify whether they are plans, targets or forecasts, rather than assuming they are observed outcomes. The percentage denominator and source/method are not established by this cropped screenshot. Colour changes may imply a favourable story but do not prove a broadcaster’s intent.

Use the original Noroff images for your own analysis. These notes identify visible checks and limitations, not a completed independent audit of the broadcasts. No official task solution was opened.
'''
TASK_STEPS = [
 ('1. Separate the two questions','Question 1: analyse the supplied unemployment and public health expenditure TV graphs and identify what might mislead. Question 2: state each of the four lesson rules and explain your own view of its application in your data visualisation process.','The brief specifies no page count or font requirement. The Word template is an optional scaffold; do not import the previous task’s length requirements.'),
 ('2. Compare unemployment labels and positions','Inspect Figure 7. Record a specific label and plotted position, compare it with neighbouring months and explain any mismatch. The November label is 8.6%, while its position appears near the 9.0% level and above March’s 8.8% point.','Describe visible screenshot evidence, not independently verified labour statistics. Check the original series before reconstructing the chart.'),
 ('3. Explain the unemployment scale and presentation','Inspect the approximate 8–10% range, filled area and perspective. Explain how the visual may magnify a small change or obscure precise reading, and propose a clean, correctly plotted presentation.','A justified zoomed line chart can be valid. Do not use “every chart must start at zero” as a universal rule; bars and filled magnitude areas need a zero baseline.'),
 ('4. Analyse health expenditure bar lengths','Inspect Figure 8’s approximately 4% baseline, labels and perspective. Explain why truncated bar lengths distort ratios, and propose a zero-baseline flat bar chart with meaningful units and a defined percentage denominator.','The 4.8% and 7.0% labels imply a value ratio near 1.46; idealised lengths above 4% imply 3.75. This is label-based arithmetic, not a measured screenshot lie factor.'),
 ('5. Check health expenditure time and status','Record unequal gaps between labelled years, including 2016→2020 and 2023→2027. Explain how equally spaced categories may be mistaken for annual change. Identify future years relative to the June 2021 caption and request explicit plan/forecast/target labels and sources.','Do not classify future figures as realised outcomes. Equal category spacing alone is not proof of falsified values or deliberate deception; explain the reading risk.'),
 ('6. Apply all four lesson rules','Use the four exact course headings. For each, state the rule, explain your own view, describe a concrete action during collection/processing/presentation, and identify evidence or a check. Connect the reasoning to your own visualisation workflow.','The four rules are Do not be picky with the numbers; Be aware of biases; Keep the graphs clear and non-confusing; Encourage third-party review. They are not the four POUR principles.'),
 ('7. Review evidence and corrections','Check that Question 1 discusses both graphs with observation, misleading effect, proposed correction and limitations. Check all four rule-and-view entries for Question 2. Remove placeholders, cite sources and distinguish proposed review from real feedback.','Exam Resolver reviews your written observations and reasoning using the supplied guide. It does not inspect uploaded chart pixels, verify the original datasets or prove deliberate intent.'),
]
ANALYSIS_TEMPLATE = '''# Task 2.2 Question 1 — Analyse the two TV graphs

Repeat observation → misleading effect → correction → limitation for each issue.

## Figure 7: Unemployment
Visible label, month and plotted position: [...]
Comparison with neighbouring months: [...]
Scale, filled area or perspective concern: [...]
How a reader might be misled: [...]
Proposed correction and source verification needed: [...]
What I can and cannot conclude from the screenshot: [...]

## Figure 8: Public health expenditure
Visible labels and bar baseline: [...]
Effect on magnitude comparison: [...]
Unequal time gaps and category/timeline interpretation: [...]
Future years relative to broadcast caption, and status to clarify: [...]
Percentage denominator, source and context to verify: [...]
Proposed corrections and limitations: [...]

## Final check
Cover both supplied graphs. Support each judgement with a specific visible feature. A zoomed line-chart scale is not automatically misleading; truncated bars distort length ratios. Do not claim verified datasets, measured pixel geometry or deliberate intent without evidence.
'''
RULES_TEMPLATE = '''# Task 2.2 Question 2 — Four rules and my view

For each rule: meaning → my view → concrete workflow action → evidence/check.

'''
for name,meaning,action,caution in RULES:
    RULES_TEMPLATE += f'## {name}\nMeaning in my own words: [...]\nMy view and reason: [...]\nMy concrete workflow action: [...]\nEvidence or check: [...]\n\n'
RULES_TEMPLATE += '## Final check\nInclude all four course rules with your own view and application. Planned peer review is not completed feedback. Cite researched claims and explain limitations.\n'
REVIEW_TEMPLATE = '''# Task 2.2 Optional chart and peer review log

## Chart integrity check
Source, definition, population, period and units: [...]
Data inclusion/exclusion and missingness: [...]
Labels agree with plotted values: [...]
Baseline, scale, geometry and relevant comparisons: [...]
Time gaps and observed/plan/forecast status: [...]
Percentage denominator and percentage-point/relative-change distinction: [...]
Colour cues and equivalent readable information: [...]
Corrections proposed: [...]

## Third-party review
Reviewer and date: [leave blank until completed]
Chart version and question asked: [...]
Reviewer’s actual first interpretation: [leave blank until observed]
Comparison with the data and intended message: [...]
Actual feedback, revision and recheck: [leave blank until completed]
Unresolved limitation: [...]

An optional lie-factor exercise is not required by this task. Define graphic and data effects consistently; a zero data effect makes their ratio undefined. Do not estimate a precise factor from a perspective screenshot without a justified measurement method.
'''
ILLUSTRATIONS = [
 {'file':'lesson-2-2-chart-integrity.png','title':'Make the visual agree with the evidence','caption':'Check scale, plotted geometry, context, and time/status. Bar lengths need a zero baseline; a line-chart zoom needs a defensible range. Match positions to labels, explain relevant data and definitions, show time gaps and distinguish observed from future values. Illustrative scenes, not verified TV graphs or numerical data.'},
 {'file':'task-2-2-four-rules.png','title':'Analyse two graphs and apply four rules','caption':'Question 1 analyses both supplied TV graphs using observation, misleading effect, correction and limitation. Question 2 states and applies the four course rules: do not be picky with the numbers; be aware of biases; keep the graphs clear and non-confusing; encourage third-party review. Add your own view and workflow action. Planned review is not observed feedback.'},
]
LESSON_CONTENT = '''
### Lesson 2.2: ethical data visualisation

A chart influences how readers interpret evidence and make decisions. Accurate numbers can still produce a misleading impression through selective inclusion, inconsistent geometry or missing context. Misleading design can be accidental; a screenshot does not establish deliberate intent.

The course’s historical advertising example illustrates how a survey claim can imply more than its questions support. Examine question wording, who was sampled, the denominator and what comparison is actually justified. Do not treat a catchy percentage as a complete explanation.

### Step 1 — check the data before styling

Record source, definition, relevant population, period, units and limitations. Avoid leading questions when collecting data. During processing, document exclusions, transformations and missingness. A trustworthy source can still have limits or bias. Statistical significance is relevant to suitable inferential claims, not a universal prerequisite for displaying descriptive information.

### Step 2 — preserve scale and geometry

For bar charts, length represents magnitude, so use a zero baseline. A truncated baseline can make modest differences look much larger. A line chart encodes positions and may use a justified non-zero range to reveal change, but communicate the range and context. Filled areas invite magnitude comparisons, so take particular care with truncation. Avoid decorative perspective that makes positions, areas or lengths harder to compare. [ONS axes guidance](https://service-manual.ons.gov.uk/data-visualisation/guidance/axes-and-gridlines). [ONS line-chart discussion](https://digitalblog.ons.gov.uk/2016/06/27/does-the-axis-have-to-start-at-zero-part-1-line-charts/).

Check that every point or bar agrees with its value label. Explain irregular time intervals, and identify forecasts, plans or targets separately from realised observations. Two differently scaled axes can suggest a relationship through arbitrary scaling; an apparent visual match does not establish correlation or causation.

### Step 3 — understand the optional lie-factor concept

The course introduces Tufte’s **lie factor** as **size of effect shown in the graphic / size of effect in the data**. In a percentage-change calculation, use comparable relative effects and make the chosen baseline explicit.

Illustrative example: values rise from 100 to 110, a 10% data increase. Idealised bar lengths above a 90 baseline rise from 10 to 20, a 100% graphic increase. The ratio of those relative changes is 100% / 10% = **10**. A zero-baseline pair instead rises from 100 to 110, giving **1**. These are defined mathematical examples, not measurements of either task screenshot.

Noroff gives 0.95–1.05 as its suggested near-one range. Treat it as course guidance, not a universal certification of truthfulness: exclusions, context and uncertainty can still mislead. If the data effect is zero, the ratio is undefined. The task does not ask you to calculate a lie factor.

### Step 4 — retain relevant context

A selected period or category can be useful when its scope and exclusions are clear. Check whether omitted information changes the apparent conclusion. Explain the denominator of percentages. A change from 4.8% to 7.0% is **2.2 percentage points**, or about **45.8% relative to 4.8%**; those are different descriptions. These are arithmetic interpretations of labels, not verified expenditure statistics.

Use comparable populations, periods and measures when making comparisons. Counts may need population or exposure context, but rates also require comparable definitions and collection methods. Colour associations and visual emphasis should support accurate reading, with labels or other cues that do not depend only on colour.

### Step 5 — apply the four course rules

'''
for i,(name,meaning,action,caution) in enumerate(RULES,1):
    LESSON_CONTENT += f'**{i}. {name}.** {meaning} {action} {caution}\n\n'
LESSON_CONTENT += '''### Step 6 — work through Task 2.2

**Question 1:** identify what might mislead readers in the supplied unemployment and public health expenditure screenshots. Use **observation → misleading effect → proposed correction → limitation**. The following notes help you locate evidence; write your own justified analysis.

'''+FIGURE_NOTES+'''
**Question 2:** state each of the four lesson rules and explain your own view of its application to your data visualisation process. Use **rule → meaning → my view → workflow action → check**. Four rule entries are required; they are not the POUR principles from the accessibility lesson.

The task brief specifies no page count or font. The downloadable Word and Markdown documents are optional study scaffolds, not additional submission requirements. Exam Resolver reviews the text you provide and the task guide. It does not inspect uploaded screenshot pixels or independently verify the underlying datasets.

[Original lesson](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81557). [Manipulation examples](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81559). [Four rules](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81560). [Original Task 2.2 and both graphs](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81562).
'''
GUIDE = {'course_code':'FI1BBDV75','id':'2.2-task','uid':'dvs-2.2-task-81562','lesson_number':'2.2','title':'Misleading graph analysis and four ethical rules','source_url':TASK_URL,'method':'chart_integrity','deliverable':'Question 1: analyse both supplied TV graphs. Question 2: state each of the four course rules and explain your own view of its application to your visualisation process.','steps':[s[1] for s in TASK_STEPS],'caution':'Separate screenshot evidence from verified data, inference and intent. Apply all four course rules. The brief specifies no page count or font; Word is an optional template.','task_dataset':'','template_file':'DVS Task 2.2 Graph Analysis and Four Rules.docx'}

def get_task_guide_markdown(guide=None):
    text = '### DVS Task 2.2: Misleading graph analysis and four ethical rules\n\n**Deliverable:** '+GUIDE['deliverable']+'\n\n'
    for title,instruction,caution in TASK_STEPS:
        text += f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    text += FIGURE_NOTES+'\n### Four rules and application\n\n'
    for name,meaning,action,caution in RULES:
        text += f'**{name}:** {meaning} {action} Check: {caution}\n\n'
    text += f'[Original task and screenshots]({TASK_URL}). [Four course rules](https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81560). [ONS axes guidance]({AXES_URL}). [ONS line-chart discussion]({LINE_URL}).\n\nThe brief specifies no page count or font. Word is an optional scaffold. Exam Resolver reviews supplied text, not chart pixels or independently verified datasets. This guide is not Noroff’s completed solution.'
    return text

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'2.2','title':'The Ethics of Data Visualisation','module_number':2,'module_title':'User Experience and User Experience Design','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Faithful data can still be distorted by selection geometry and context','Distinguish zero-baseline bars from justified zoomed line charts','Task 2.2 analyses both screenshots and applies four ethical rules','Separate visible evidence proposed corrections verified data and intent'],'visual_elements':{'diagrams':False,'tables':False,'highlighted_sections':True}}
