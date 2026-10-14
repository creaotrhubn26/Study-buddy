"""English study scaffolds for the reviewed DVS Lesson 1.2 brief."""
CONTENT_REVISION = "2026-10-14-dvs12"
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81516'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81510'
ILLUSTRATIONS = [
    {'file': 'lesson-1-2-ideate-prototype-test.png', 'title': 'Ideate Prototype and Test', 'caption': 'Generate alternatives, build a small experimental model, observe users attempting tasks, and revise. Feedback can return the team to an earlier design-thinking stage.'},
    {'file': 'task-1-2-bmi-wireframe.png', 'title': 'BMI mobile wireframe flow', 'caption': 'Illustrative input and results screens show labelled height, weight and age fields, submission, chart choice, an age filter and an identifiable user marker. Points are illustrative, not real user data.'},
]
TASK_STEPS = [
    ('1. Turn the brief into a checklist', 'List the required mobile input fields: height, weight and age; a submission control; a results visualisation based on other site users; the current user highlighted; chart selection; and a filter such as age range. The deliverable is a low-fidelity sketch.', 'A working BMI app, polished mockup and collected health dataset are not required.'),
    ('2. Explore alternative layouts', 'Use braindumping or sketch storming to draft two quick layouts, such as a single scrolling screen and a two-screen flow. Compare readability, control placement and the number of steps. Choose one and explain why it supports the mobile audience.', 'Alternative sketches support ideation; keep the final required input and results areas clear.'),
    ('3. Sketch inputs and submission', 'Draw labelled Height (cm), Weight (kg) and Age (years) fields with a Calculate BMI button. Annotate missing, non-numeric or non-positive height/weight errors. Explain the transition to the result. Convert centimetres to metres before applying BMI = weight (kg) / height (m)².', 'Age supports comparison filtering; it is not a term in this BMI formula. Additional fields need a justified purpose.'),
    ('4. Sketch the customisable result', 'Show Your BMI: [value], a chart area based on other users, and an explicit You marker. Add Chart type and Age range controls, axis labels, units and a legend. A dot plot of age versus BMI can show an individual point; a histogram instead needs a reference marker and clearly labelled counts.', 'Use placeholders or labelled illustrative points. Do not invent real site data or claim medical meaning.'),
    ('5. Annotate states and test the flow', 'Show how the user edits details, changes chart type and applies an age filter. Explain the state when no records match or when the selected range excludes the current user. Plan a scripted formative usability test: enter sample details, submit, find the You marker and filter the chart. Record observations separately from expected outcomes.', 'A proposed test is not a completed test. Do not fabricate participants, quotations or success rates.'),
    ('6. Review and explain the design', 'Check every brief requirement against your sketch. Keep boxes and labels simple. Explain the chosen layout, user marker and controls; identify an assumption and a question to test. Submit the sketch with short annotations in the format requested by your course.', 'The image is an illustrative concept. Produce and justify your own low-fidelity wireframe.'),
]
WIREFRAME_TEMPLATE = '''# Task 1.2 Mobile BMI wireframe plan

## Purpose and deliverable
Sketch a low-fidelity mobile web flow with an input area and a customisable results area. Use pen and paper or a simple drawing tool.

## Brief checklist
- Height, weight and age inputs with visible units
- Submission control
- Other site users represented in a chart
- Current user's calculated BMI highlighted and labelled
- Chart-type selector
- Filter such as age range

## Ideation
Layout A: [quick sketch or description]
Layout B: [quick sketch or description]
Chosen layout and reason: [...]

## Input screen sketch
[Draw labelled Height (cm), Weight (kg), Age (years) fields and Calculate BMI.]
Validation message and placement: [...]
Submission transition: [...]

## Results screen sketch
[Draw result placeholder, chart, You marker, chart choice and age filter.]
Axes and units: [...]
How the individual marker works for each proposed chart: [...]
Filter behaviour if the current user is excluded: [...]
No matching data state: [...]
Edit details control: [...]

## Calculation annotation
BMI = weight (kg) / height (m)². Convert cm to m first.
Age supports filtering; it is not part of the arithmetic.
Use placeholders or clearly labelled illustrative values.

## Design explanation
Audience need → layout/control → reason → question to test.
[...]

## Final review
Check all six brief requirements. Keep the sketch low fidelity.
Do not present illustrative points as real user data or diagnose health.
'''
TEST_TEMPLATE = '''# Task 1.2 Formative usability test plan

## Purpose
Plan how to check the mobile wireframe. This is an optional learning scaffold supporting the sketch task.

## Participant and setting
Intended audience: [...]
Recruitment plan: [...]
Setting and facilitation: [remote/in person; moderated/unmoderated]

## Neutral scripted tasks
1. Enter illustrative height, weight and age and submit.
2. Locate your calculated BMI and explain how you identify yourself.
3. Change the chart type and describe what changed.
4. Apply an age range and explain which users are shown.
5. Edit your details and try an invalid height or weight.

## Observation record
Task: [...]
Expected behaviour before testing: [...]
Observed action after testing: [leave blank until a real session]
Participant's actual words and source: [leave blank until a real session]
Difficulty: [...]
Proposed change: [...]
Question for a retest: [...]

## Interpretation
Separate what people say from what they do. Qualitative observations can guide early improvements. A success measure must be defined before a quantitative comparison.
No invented participants, findings or success percentages.
'''
LESSON_CONTENT = '''
### Lesson 1.2: move from a user need to something testable

Lesson 1.1 covered Empathise and Define. Here the focus is **Ideate, Prototype and Test**. The five stages are iterative: a test may reveal that the prototype, idea or original problem needs revision.

### Step 1 — frame ideation around the need

Start with the user-centred problem or point of view. A **How Might We** question should invite several possible solutions: How might we help a mobile visitor enter measurements and understand their position in a comparison chart? This is a study example for Task 1.2, not a researched finding.

### Step 2 — generate ideas before selecting one

| Method | How it works |
|---|---|
| Brainstorming | A team shares and builds on ideas |
| Brainwriting | People write ideas first and circulate them |
| Braindumping | An individual writes down ideas |
| Brainwalking | People move between idea stations and contribute |
| Sketch storming | Quick sketches make alternatives visible |

A facilitator can keep a team focused. Capture alternatives before judging them. Then compare options against the audience need and constraints, rather than choosing the prettiest sketch.

### Step 3 — choose the fidelity needed to learn

A prototype is an experimental model for checking ideas and assumptions. A **wireframe** primarily communicates structure, information hierarchy and controls. A **mockup** communicates visual appearance. An **interactive prototype** simulates behaviour. These dimensions overlap: fidelity describes detail, while interactivity describes behaviour.

Low fidelity uses simple boxes, labels and sketches; medium fidelity adds layout/content detail; high fidelity approaches final visual detail. Interactivity does not automatically require high fidelity. A paper sketch can simulate a flow by switching sheets. For Task 1.2, low-fidelity input and results areas are enough.

### Step 4 — make the BMI flow explicit

Sketch height, weight and age inputs and a submission control. On the results screen, mark the current user's BMI among other users and include chart choice and filtering. Annotate units, validation, edits, empty results and the case where an age filter excludes the current user.

The numeric formula is **BMI = weight (kg) / height (m)²**; age supports filtering and is not an arithmetic term. The task is an interface design exercise. Use placeholders or labelled illustrative values and avoid diagnoses or clinical categories. Children and teenagers require age/sex-specific interpretation if interpretation is ever added; that is beyond this wireframe brief. [CDC calculation reference](https://www.cdc.gov/growth-chart-training/hcp/using-bmi/calculating-bmi.html).

### Step 5 — plan a usability test

Observe people attempting representative tasks using the design. Avoid leading them to the answer. A useful formative task is: Enter sample details, locate your marker, and select an age range. Record actions, difficulties and actual comments separately from your expectations.

| Distinction | Meaning |
|---|---|
| Formative / summative | Improve a developing design / assess outcomes later against criteria |
| Qualitative / quantitative | Explore behaviour and reasons / measure defined outcomes |
| Attitudinal / behavioural | What people say / what people do |
| Explorative / comparative | Investigate needs and experiences / compare designs or alternatives |
| Scripted / unscripted | Predetermined tasks / more open exploration |
| Moderated / unmoderated | Facilitator present / participant works without a facilitator |
| Remote / in person | Participant joins from elsewhere / shares a physical setting |

These are separate dimensions. Formative work often uses qualitative observations and summative work often uses quantitative measures, but the terms are not interchangeable. Remote testing can be moderated, and scripted testing can be unmoderated.

### Step 6 — distinguish A/B testing from usability observation

An A/B test compares variants using a predefined outcome. Keep the objective clear and isolate a change if you want to attribute an effect to that change. Changing button shape and colour simultaneously only compares the combined variants; it cannot tell you which feature caused the difference. Define denominators and compare rates, not just counts. A/B testing is not the same method as observing someone attempt a usability task.

### Step 7 — explain and iterate

A defensible exam explanation links **need → alternatives → prototype choice → test task → evidence → revision**. Before a real test, write a plan and expected behaviour. After testing, add genuine observations and explain what you changed. Task 1.2's required deliverable remains your low-fidelity wireframe; a test plan supports learning rather than replacing it.

[Lesson introduction](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81510). [Ideation](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81511). [Prototype](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81512). [Fidelity and interaction](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81545). [Testing](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81513). [Testing approaches](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81514).
'''
GUIDE = {'course_code':'FI1BBDV75','id':'1.2-task','uid':'dvs-1.2-task-81516','lesson_number':'1.2','title':'Mobile BMI low-fidelity wireframe','source_url':TASK_URL,'method':'wireframe prototype usability test','deliverable':'Low-fidelity mobile input and customisable BMI visualisation sketch','steps':[s[1] for s in TASK_STEPS],'caution':'Sketch only; use placeholders or labelled illustrative data. Include all brief controls and an explicit current-user marker. Do not fabricate research or diagnose health.','task_dataset':'','template_file':'DVS Task 1.2 Wireframe and Test Plan.docx'}

def get_task_guide_markdown():
    text = '### DVS Task 1.2: Mobile BMI low-fidelity wireframe\n\n**Deliverable:** Your own low-fidelity mobile sketch. Required: height, weight and age; submission; other users in a chart; your highlighted BMI; chart selection; and a filter such as age range.\n\n'
    for title, instruction, caution in TASK_STEPS:
        text += f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    return text + f'[Original task]({TASK_URL}).\n\nUse the wireframe plan and optional formative test plan. This is a study scaffold, not a completed official solution.'

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'1.2','title':'Design Thinking — Part 2','module_number':1,'module_title':'Design Thinking','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Generate alternatives with ideation methods','Choose wireframe fidelity for the question you need to test','Observe user tasks and distinguish testing dimensions','Sketch all mobile BMI controls and a labelled current-user marker'],'visual_elements':{'diagrams':False,'tables':True,'highlighted_sections':True}}
