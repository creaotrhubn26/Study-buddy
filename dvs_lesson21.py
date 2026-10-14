"""Reviewed Lesson 2.1: English UX teaching and two-question task scaffolds."""
CONTENT_REVISION = '2026-10-14-dvs21'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81548'
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22905&chapterid=81556'
MORVILLE_URL = 'https://semanticstudios.com/user_experience_design/'
IMAGE_SOURCE = 'https://www.w3.org/WAI/tutorials/images/complex/'
REDIRECT_NOTE = 'Checked 14 October 2026: https://data.oecd.org/ redirected to https://www.oecd.org/en/data.html; https://www.oecd-forum.org/ redirected to https://www.oecd.org/en/about.html. These destinations are not the original historical interfaces. Record your own inspection date and final URLs. If the original Forum interface is required, ask your tutor for an approved archive or replacement; do not silently substitute the About page or invent Forum findings.'
FACTORS = [('Useful','Does the information meet a real audience need?'),('Usable','Can the audience complete its task?'),('Findable','Can people locate relevant information and controls?'),('Credible','Can readers understand and trust the source and context?'),('Desirable','Does the presentation invite engagement without obscuring meaning?'),('Accessible','Can people with disabilities obtain and operate the information?'),('Valuable','Does it benefit users and support organisational goals?')]
TASK_STEPS = [
 ('1. Separate the two questions','Plan Question 1 as one page reviewing good and bad design elements of both OECD Data and the OECD Forum Network, with justification. Plan Question 2 as at least half a page defining UX design in your own words and applying it to data analysis visualisations, in a Word document using Arial 11 pt.','The lengths are separate requirements. Placeholder text and research notes do not count as your completed answer.'),
 ('2. Inspect OECD Data','Open the supplied link, record the final URL, inspection date, device and a representative goal such as finding an indicator and its definition. Note what you actually see or do, with page/feature evidence.','A visible link is evidence of its presence; successful task completion, performance and keyboard behaviour require actual checks.'),
 ('3. Inspect the Forum link','Open the supplied OECD Forum Network link and record its destination. If it redirects, document the limitation and seek an approved historical page or replacement from your tutor. Prepare your evaluation questions while that is resolved.','A current About page cannot establish strengths or weaknesses of the old Forum interface. Do not fabricate historical observations.'),
 ('4. Justify strengths and weaknesses','For each available site, connect an observed feature to a relevant UX facet and a specific user goal. Explain the likely effect, a concrete improvement for a weakness, and what further check would support the judgement.','Use observation → UX reason → user impact → improvement or follow-up check. Label inferred effects; do not present them as measured findings.'),
 ('5. Write the one-page report','Write a short scope introduction, concise justified strengths and weaknesses for each named site, then a comparative conclusion. Cite inspected pages and record any access limitation explicitly.','One-page report is the stated requirement, not one page per site. Check the final layout in Word and remove scaffold instructions.'),
 ('6. Define and apply UX design','Write at least half a page in your own words: define UX design, distinguish UX from UI, and connect research, information organisation, interaction and evaluation to readable, trustworthy and accessible data visualisations. Apply these ideas to an audience and data question.','Explain why each choice helps that audience: chart type, labels/units, source/date, equivalent text/data, responsive layout and usable controls. Proposed tests are not completed findings.'),
 ('7. Review both outputs','Check both site evaluations, evidence and justifications, the UX definition and applied reasoning, source notes and explicit redirect limitations. Save your Word document using Arial 11 pt and verify the one-page and at-least-half-page requirements after replacing placeholders.','Exam Resolver reviews your written draft and supplied evidence; it does not browse the OECD sites or verify Word pagination or font. Confirm those yourself.'),
]
REPORT_TEMPLATE = '''# Task 2.1 Question 1 — One-page website review

## Scope and evidence
Audience and task: [...]
Inspection date, browser/device and viewport: [...]
OECD Data supplied URL and final URL: [...]
OECD Forum Network supplied URL and final URL: [...]
Access/redirect limitation and tutor-approved scope, if needed: [...]

## OECD Data
Observed strength and page/feature evidence: [...]
UX reason and likely effect on the audience task: [...]
Observed weakness and evidence: [...]
Reason, proposed improvement and check: [...]

## OECD Forum Network
Observed strength and page/feature evidence: [...]
UX reason and likely effect on the audience task: [...]
Observed weakness and evidence: [...]
Reason, proposed improvement and check: [...]
If unavailable, record the limitation; do not invent observations or silently assess a different site.

## Comparative conclusion
Most important findings and design lessons: [...]
Sources for observations and researched claims: [...]

## Final layout check
Turn these notes into a justified one-page report covering both named sites. Remove prompts and verify pagination in Word.
'''
APPLICATION_TEMPLATE = '''# Task 2.1 Question 2 — UX design and data visualisations

Required: at least half a page in your own words, in a Word document using Arial 11 pt.

## Define UX design
My explanation of UX design and how UX differs from UI: [...]
How research and evaluation inform design: [...]

## Apply it to a data visualisation
Audience, goal and data question: [...]
Chart type and information organisation, with reasons: [...]
Labels, units, source/date and credibility: [...]
Equivalent text/data and relevant accessibility checks: [...]
Layout, interaction and device considerations: [...]
Proposed user task and evaluation method: [...]

## Write connected paragraphs
Concept → concrete design choice → user benefit → evaluation.
Write your own explanation, cite researched claims and distinguish proposals from actual findings. Replace all placeholders; inspect the final length and Arial 11 pt formatting in Word.
'''
EVIDENCE_TEMPLATE = '''# Task 2.1 Evidence log (optional preparation)

Repeat this record for each finding.
Named site: [...]
Supplied URL, final URL and inspection date: [...]
Device/viewport and user goal: [...]
Page/feature and exact action attempted: [...]
Observed behaviour or visible evidence: [...]
Strength or weakness and relevant UX facet: [...]
Reason and inferred effect on the user task: [...]
Proposed improvement and further check: [...]
Evidence reference or screenshot filename: [...]
Limitations and untested claims: [...]

Record redirects and approved alternatives explicitly. Do not infer performance, keyboard access or WCAG conformance from appearance alone. Research notes are separate from the required report and definition.
'''
ILLUSTRATIONS = [
 {'file':'lesson-2-1-ux-facets.png','title':'UX: the whole experience','caption':'UX covers a person’s experience of reaching a goal; UI controls support it. Morville’s seven facets are useful, usable, findable, credible, desirable, accessible and valuable. The chart, source and date shown are illustrative, not real OECD data or findings. The facets are a reasoning framework, not an accessibility certification.'},
 {'file':'task-2-1-observe-justify-apply.png','title':'Observe justify and apply','caption':'Question 1 is a justified one-page report about both named websites. Question 2 is at least half a page defining UX design and applying it to data visualisations, in your own words, in Word using Arial 11 pt. Record current redirects, observations and scope limitations. Proposed improvements and tests are not findings.'},
]
LESSON_CONTENT = '''
### Lesson 2.1: design the experience around a user’s goal

**User experience (UX)** covers how someone experiences a product or service in context: finding information, understanding it, acting on it and reaching a goal. **UX design** is the work of investigating needs and shaping and evaluating that experience. **User interface (UI)** design concerns the interface people operate, including layout, labels, controls and states. UI contributes to UX; an attractive interface can still leave a person unable to complete a task.

The course introduces Don Norman’s role in popularising the term and its connection to human–computer interaction. For an exam explanation, concentrate on the user’s whole experience and the design decisions that support it.

### Step 1 — use seven UX facets as questions

Peter Morville’s framework helps you reason about different qualities rather than reduce UX to appearance. It is not a numerical score or a compliance checklist.
'''
LESSON_CONTENT += '\n'.join(f'- **{name}:** {question}' for name, question in FACTORS)
LESSON_CONTENT += '''

[Morville’s original framework](https://semanticstudios.com/user_experience_design/). Choose relevant facets to justify a specific decision; a good-looking chart does not by itself prove usability, credibility or accessibility.

### Step 2 — connect four design disciplines

**User research:** investigate people’s tasks, needs and constraints using suitable research and observation. Personas should reflect evidence; label hypothetical assumptions.

**Experience strategy:** connect user needs to organisational goals and constraints. Define what a successful experience should enable.

**Interaction design:** shape actions and feedback, such as applying filters, resetting a view and recovering from empty results or input errors.

**Information architecture:** organise and label information so people can find and understand it. Card sorting can investigate how participants group concepts; it does not automatically prove the final navigation works.

### Step 3 — follow an iterative process

Define audience, goal and scope → research → synthesise needs → organise information → sketch wireframes and flows → evaluate representative tasks → revise. A low-fidelity wireframe explains structure and behaviour with simple shapes and labels. A storyboard can show the connected steps of a journey. A finished-looking mock-up is not evidence of successful use.

Ask what people expect (their mental model) and check how they actually interpret the design. Keep planned sessions separate from recorded observations.

### Step 4 — evaluate a website with evidence

Choose a representative task. Record the inspection date, page, device and exact feature or action. Distinguish **observed behaviour**, **your interpretation** and **a proposed improvement**. Use a pattern: observation → relevant UX facet → effect on the task → improvement or further check.

For example, if you observe a clear indicator definition beside a data link, you can explain why it may help a reader interpret the measure. Do not claim that users completed the task faster unless you measured that. Check keyboard operation, loading performance and assistive-technology behaviour directly before making claims about them.

Noroff uses Eurostat screenshots as a teaching example of headings, categories, breadcrumbs and navigation. Those screenshots are historical examples, not a current audit. Cookie placement or a short sign-in form does not establish good UX for every audience or task.

### Step 5 — apply UX to data visualisations

Start with the audience’s question. Use bars for category comparisons, lines for change over time, a histogram for the distribution of a numerical variable in intervals, a scatter plot to investigate the relationship between two numerical variables, and a suitable parts-of-whole chart when the whole and categories are clear. A Pareto chart combines descending categories with cumulative percentage. Explain why the choice fits the data and task.

Use readable labels, explicit units and a meaningful title. State source, date and important limitations. Avoid colour-only meaning and unintended good/bad implications. For a complex chart, provide a concise text identification with an equivalent longer description or data alternative as appropriate. [W3C complex image guidance](https://www.w3.org/WAI/tutorials/images/complex/).

On smaller screens, prioritise the important comparison, keep labels legible and preserve access to the same information. Mobile interaction is not automatically unsuitable: check that touch controls, keyboard access, feedback and layout support the task. Avoid hiding the central result behind optional interaction. Evaluate rather than assume one layout suits all contexts.

### Step 6 — complete the two-question task

**Question 1:** write a **one-page report** identifying good and bad design elements of **OECD Data** and **the OECD Forum Network**, justifying your judgements.

**Question 2:** define **UX design in your own words** and explain its application to presenting data analysis visualisations. Write **at least half a page**, in a **Word document using Arial 11 pt**.

The steps and downloadable templates below separate both outputs and include an optional evidence log. They are original study scaffolds. Check the final page lengths after writing your own answer.

### Current link note

'''
LESSON_CONTENT += REDIRECT_NOTE + '\n\n[Original lesson](' + LESSON_URL + '). [Original Task 2.1](' + TASK_URL + ').'
GUIDE = {'course_code':'FI1BBDV75','id':'2.1-task','uid':'dvs-2.1-task-81556','lesson_number':'2.1','title':'Website UX review and visualisation application','source_url':TASK_URL,'method':'ux_review','deliverable':'Question 1: justified one-page report on both OECD sites. Question 2: at least half a page defining UX design and applying it to data visualisations, in own words, Word, Arial 11 pt.','steps':[s[1] for s in TASK_STEPS],'caution':'Record redirects and evidence. Do not invent historical Forum findings, completed tests or conformance. Verify formatting and final page lengths in Word.','task_dataset':'','template_file':'DVS Task 2.1 Website Review and UX Application.docx'}

def get_task_guide_markdown(guide=None):
    text = '### DVS Task 2.1: Website UX review and visualisation application\n\n**Deliverable:** ' + GUIDE['deliverable'] + '\n\n'
    for title, instruction, caution in TASK_STEPS:
        text += f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    text += '**Current link note:** ' + REDIRECT_NOTE + '\n\n'
    text += '**UX facets:** ' + '; '.join(n for n,_ in FACTORS) + '.\n\n**Writing pattern:** observation → UX reason → user impact → improvement or check.\n\n'
    text += f'[Original task]({TASK_URL}). [OECD Data supplied link](https://data.oecd.org/). [Forum supplied link](https://www.oecd-forum.org/). [Morville framework]({MORVILLE_URL}). [Complex image alternatives]({IMAGE_SOURCE}).\n\nExam Resolver reviews supplied text and evidence. It does not browse the sites or verify Word font and pagination. This is a scaffold, not an official completed solution.'
    return text

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'2.1','title':'User Experience and User Experience Design','module_number':2,'module_title':'User Experience and User Experience Design','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['UX is the whole experience; UI supports it','Use seven UX facets and four disciplines to justify decisions','Separate observed evidence, interpretation and proposed evaluation','Task 2.1 requires a one-page review and at least half a page of applied UX definition'],'visual_elements':{'diagrams':False,'tables':False,'highlighted_sections':True}}
