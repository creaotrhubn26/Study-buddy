"""English teaching and reflection scaffolds for reviewed DVS Lesson 1.4."""
CONTENT_REVISION='2026-10-14-dvs14-layout'
LESSON_URL='https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81529'
TASK_URL='https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81544'
WAI_SOURCE='https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/'
WCAG_SOURCE='https://www.w3.org/TR/WCAG22/'
CONTRAST_SOURCE='https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html'
SPACING_SOURCE='https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html'
LANGUAGE_SOURCE='https://www.w3.org/International/quicktips/'
SOURCES=[('W3C WAI accessibility usability and inclusion',WAI_SOURCE),('WCAG 2.2 reference',WCAG_SOURCE)]
CONCEPTS=[
    ('Inclusive Design','Investigate people and circumstances that a design could overlook.','Consider language, digital familiarity, connectivity or individual needs. Propose one concrete adaptation to your visualisation or its host platform, explain who it could help, and plan how to investigate that need.','Do not invent an audience preference or stereotype a demographic. Accessibility remains a distinct focus on disability-related barriers.'),
    ('Usability','Help the intended audience achieve its goal effectively, efficiently and with satisfaction.','Choose a representative task, such as finding a value or filtering a chart. Explain how clear labels, predictable controls or useful feedback could make the task easier. Describe what you would observe in a usability session.','A proposed test and expected benefit are not completed observations or measured success rates.'),
    ('Accessibility','Remove barriers that prevent people with disabilities from perceiving, operating or understanding the information.','Apply a relevant POUR principle. For example, supplement a chart with equivalent text/data, support keyboard controls with visible focus, and expose control names and states to assistive technology. Identify a check and its source.','One contrast result or three reflection paragraphs do not establish WCAG conformance. Evaluate the specific barrier and platform.'),
]
TASK_STEPS=[(f'{i}. {name}',f'Write one brief paragraph under the heading {name}. {meaning} {example} Use context → proposed change → reason → evaluation → source.',caution) for i,(name,meaning,example,caution) in enumerate(CONCEPTS,1)]
POUR=[('Perceivable','Make information available in forms people can perceive.','Readable labels, text/data alternatives, contrast and adaptable layouts.'),('Operable','Make the interface usable through appropriate input methods.','Keyboard controls, visible focus, sufficient time and clear navigation.'),('Understandable','Make the content and interface behaviour clear.','Plain wording, consistent actions, explicit formats and helpful errors.'),('Robust','Make meaning and states interpretable by user agents and assistive technology.','Semantic controls, accessible names, selected/expanded states and status announcements.')]
ILLUSTRATIONS=[
    {'file':'lesson-1-4-pour.png','title':'POUR accessibility principles','caption':'Perceivable: readable information and equivalent alternatives. Operable: usable controls and keyboard focus. Understandable: clear wording, formats and behaviour. Robust: meaningful names, roles and states for browsers and assistive technology. Scenes are illustrative, not a conformance assessment.'},
    {'file':'task-1-4-three-reflections.png','title':'Three applied reflections','caption':'Task 1.4 requires Inclusive Design, Usability and Accessibility headings, with one brief applied paragraph for each. Consider context, proposed change, reason, evaluation and source, for both the visualisation and its web/mobile/printed platform. POUR supports the accessibility reflection; it does not replace the three required headings.'},
]
REFLECTION_TEMPLATE='''# Task 1.4 Three applied reflections

## Purpose
Research inclusive design, usability and accessibility. In your own Word document, use the three concept headings and write one brief paragraph under each about your future visualisations and their web, mobile or printed platforms.

## My context
Audience and goal: [...]
Visualisation and host platform: [...]
User need or barrier to investigate: [...]

## Writing pattern
Context → proposed change → reason → evaluation → source.
For [audience and task], I would [adaptation] because [reason]. I would investigate/check [method]. Source for a researched claim: [...].

'''
for name,_,_,_ in CONCEPTS:REFLECTION_TEMPLATE+=f'## {name}\nMy brief applied paragraph: [write in your own words]\nSource and proposed evaluation: [...]\n\n'
REFLECTION_TEMPLATE+='''## Final review
- All three headings have a brief applied paragraph.
- Consider the visualisation and its host platform.
- Explain concrete adaptations, reasons and relevant checks.
- Distinguish proposed benefits from observed findings.
- Cite researched claims and avoid untested conformance claims.
- POUR is supporting material, not four extra required task paragraphs.

## Research starting points
'''+ '\n'.join(f'- [{name}]({url})' for name,url in SOURCES)+'\n'
RESEARCH_TEMPLATE='''# Task 1.4 Research and evaluation notes

## Source note
Organisation and title: [...]
URL and access date: [...]
Relevant claim in my own words: [...]
Concept or barrier supported: [...]
Scope and limitations: [...]

## Proposed check
Visualisation and platform: [...]
User task and need: [...]
Proposed change: [...]
Related POUR principle if relevant: [...]
Method and expected behaviour before testing: [...]
Actual observation after a real check: [leave blank until checked]
Follow-up change or question: [...]

## Source boundaries
The course refers to WCAG 2.1; WCAG 2.2 is a supplementary current reference.
Spacing values in SC 1.4.12 describe supported user overrides, not mandatory default CSS.
SC 3.1.5 Reading Level is Level AAA; plain language is useful more generally.
A single automated result or user session does not certify WCAG conformance.
'''
CONTRAST_TEMPLATE='''# Activity 1.4.1 Contrast check log

## Pair and context
Foreground colour: [...]
Background colour: [...]
Text/component and actual size: [...]
Tool and check date: [...]
Reported ratio without rounding up: [...]
Applicable criterion and source: [...]
Result for that criterion only: [...]
Proposed adjustment and recheck: [...]

## Text contrast reference
SC 1.4.3 Level AA normally uses at least 4.5:1; qualifying large text uses at least 3:1. Consult the criterion's definitions and exceptions. Non-text graphical objects have separate requirements.
Do not use colour alone to distinguish chart series. A contrast check does not replace other accessibility checks.

## Resources
https://coolors.co/contrast-checker/112a46-acc8e5
https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
'''
LANGUAGE_TEMPLATE='''# Activity 1.4.2 Language selector plan

## Required languages
English; Norwegian; German; French.
Visible option names may use the target-language names: English; Norsk; Deutsch; Français.

## Proposed design
Visible and accessible label: [Language]
Control and placement: [...]
Current selected language: [...]
How selection is confirmed and applied: [...]
Keyboard and focus behaviour: [...]
How the chosen language/state is conveyed to assistive technology: [...]
Behaviour if a translated page is unavailable: [...]

## Proposed check
Find the selector, choose each language using a keyboard, and verify the current language and page context are clear.
Expected behaviour: [...]
Actual observations after a real check: [leave blank until checked]
Source: https://www.w3.org/International/quicktips/
Use language names; country flags are not a sufficient language label.
'''
LESSON_CONTENT='''
### Lesson 1.4: make the visual and its interface usable and accessible

Inclusive design, usability and accessibility overlap, but each provides a different question to investigate. Inclusion considers people and contexts that might be overlooked. Usability considers whether the intended audience can achieve a goal effectively and comfortably. Accessibility focuses on disability-related barriers, including how the underlying interface works with assistive technology. [W3C WAI distinctions](https://www.w3.org/WAI/fundamentals/accessibility-usability-inclusion/).

A chart is part of a wider experience. Readable values are not enough if a person cannot operate its filters, understand a form error or obtain the same information through an alternative view.

### Step 1 — connect inclusive design to actual needs

Ask who might be excluded by the language, device, connectivity, prior experience or interaction pattern. Investigate rather than assume. Include relevant people in research and evaluation. A proposed improvement can help more than one group, but do not claim a measured benefit without evidence.

### Step 2 — define a usability task

Choose a meaningful goal: find a comparison, change a filter, read a value or correct an input. Plan what to observe, such as completion, confusion or recovery. Keep predicted behaviour separate from actual observations. A satisfaction statement alone cannot establish that a person could complete the task.

### Step 3 — use the four POUR principles

'''
LESSON_CONTENT+='\n'.join(f'{i}. **{name}:** {meaning}' for i,(name,meaning,_example) in enumerate(POUR,1))
LESSON_CONTENT+='''

**Perceivable:** pair colour with labels, shapes or patterns. Provide equivalent text/data for complex charts. Check legibility and the layout when text is resized or spacing changes.

**Operable:** test chart controls with a keyboard, check focus visibility/order and ensure the user can recover or continue at an appropriate pace. Avoid interactions that depend only on hovering. Do not use rapidly flashing teaching examples.

**Understandable:** use meaningful headings and control names, consistent navigation and explicit input formats. A label such as Date (DD/MM/YYYY) helps a user know what is expected. Explain errors beside the relevant input and preserve suitable non-sensitive input for correction.

**Robust:** use meaningful interface semantics and accessible names. A selector should expose its chosen value; an accordion should expose expanded/collapsed state. A status message should communicate what changed without needlessly disrupting the task. Compatibility must be checked with relevant browsers and assistive technology.

### Step 4 — distinguish focus and state

Keyboard focus indicates where the next keyboard action will act; it does not itself mean an option is selected. Selected/checked state identifies a choice. Expanded state identifies an open group. Hover styling, a pressed active state and the current page are different concepts. Visual styling alone does not communicate every state to assistive technology.

### Step 5 — read WCAG claims carefully

Noroff's lesson refers to **WCAG 2.1**. **WCAG 2.2** provides a newer supplementary reference; both use POUR. This lesson is a learning guide, not a conformance assessment. [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

**Text spacing:** SC 1.4.12 checks that content/functionality survive user overrides: line height at least 1.5 times font size; paragraph spacing 2 times; letter spacing 0.12 times; word spacing 0.16 times. It does not require these as the author's default settings. Check the criterion's scope and language exceptions. [W3C text spacing explanation](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

**Reading level:** SC 3.1.5 is Level AAA. Writing clearly is useful, but the lower-secondary reading-level provision is not a blanket Level AA requirement. [W3C reading level](https://www.w3.org/WAI/WCAG22/Understanding/reading-level.html).

**Contrast:** SC 1.4.3 Level AA normally requires text contrast of at least 4.5:1, or 3:1 for qualifying large text. Check definitions and exceptions; text and non-text graphics have different criteria. Do not round a failing ratio up or treat a contrast pass as full accessibility. [W3C contrast reference](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

### Step 6 — complete the separate activities

**Activity 1.4.1:** explore Coolors and record a foreground/background contrast check. Note colours, ratio, context and the applicable criterion. Distinguish measured results from a plan and also consider colour-independent cues.

**Activity 1.4.2:** design an accessible selector for English, Norwegian, German and French. Provide a clear label, visible current choice, keyboard/focus behaviour and meaningful option names. Target-language names such as English, Norsk, Deutsch and Français help readers recognise their language. Country flags are not adequate language labels. [W3C internationalisation tips](https://www.w3.org/International/quicktips/).

### Step 7 — write Task 1.4

Research the three concepts. In your own Word document, use **Inclusive Design**, **Usability** and **Accessibility** headings, with one brief applied paragraph under each. Explain a concrete adaptation for your future visualisation and its web/mobile/printed platform, a reason and a proposed evaluation, supported by a source.

Use **context → proposed change → reason → evaluation → source**. Three task paragraphs are required; the four POUR principles support your accessibility reasoning rather than replacing those headings. The activity guides and templates are separate from the main reflection assignment.

[Lesson introduction](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81529). [Concepts](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81530). [POUR](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81533). [Perceivable applications](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81536). [Operable applications](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81538). [Understandable applications](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81540). [Robust applications](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81542). [Task](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81544).
'''
GUIDE={'course_code':'FI1BBDV75','id':'1.4-task','uid':'dvs-1.4-task-81544','lesson_number':'1.4','title':'Inclusive design usability and accessibility reflections','source_url':TASK_URL,'method':'inclusive design usability accessibility POUR reflection','deliverable':'Own Word document with three brief applied paragraphs under the specified concept headings','steps':[s[1] for s in TASK_STEPS],'caution':'Use exactly the three required concepts; consider the visual and its platform. Cite researched claims and distinguish proposals from completed tests. Do not certify conformance from a reflection.','task_dataset':'','template_file':'DVS Task 1.4 Three Applied Reflections.docx'}
GUIDES=[GUIDE,
    {'course_code':'FI1BBDV75','id':'1.4.1','uid':'dvs-1.4.1-81534','lesson_number':'1.4','title':'Check colour contrast with Coolors','source_url':'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81534','method':'contrast accessibility','deliverable':'Own contrast-tool exploration and foreground/background check notes','steps':['Open Coolors contrast checker and choose the actual foreground/background colours','Record the reported ratio, text size/context and relevant criterion','Propose a change if needed and recheck; consider cues beyond colour'],'caution':'Record actual tool results without rounding up. A text contrast pass is not a full accessibility assessment.','task_dataset':'','template_file':''},
    {'course_code':'FI1BBDV75','id':'1.4.2','uid':'dvs-1.4.2-81540','lesson_number':'1.4','title':'Design an accessible language selector','source_url':'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81540','method':'language selector accessible design','deliverable':'Design proposal for English Norwegian German and French language selection','steps':['Include all four required languages with meaningful names','Describe the label, current choice, selection/confirmation and keyboard focus','Explain how state and language are conveyed and propose a check'],'caution':'Do not rely on flags alone or claim a proposed selector has been tested. This activity is separate from the main three-reflection task.','task_dataset':'','template_file':''},
]

def get_task_guide_markdown(guide):
    if guide['id'] != '1.4-task':
        text=f"### DVS Activity {guide['id']}: {guide['title']}\n\n**Deliverable:** {guide['deliverable']}\n\n"+'\n'.join(f'{i}. {step}.' for i,step in enumerate(guide['steps'],1))+f"\n\n**Check:** {guide['caution']}\n\n"
        if guide['id']=='1.4.1':text+=f'[Coolors contrast checker](https://coolors.co/contrast-checker/112a46-acc8e5). [W3C text contrast]({CONTRAST_SOURCE}).\n\n'
        else:text+=f'**Required languages:** English, Norwegian, German and French. **Example labels:** English, Norsk, Deutsch, Français. [W3C language navigation]({LANGUAGE_SOURCE}).\n\n'
        return text+f"[Original activity]({guide['source_url']})."
    text='### DVS Task 1.4: Three applied reflections\n\n**Deliverable:** Research Inclusive Design, Usability and Accessibility. Write one brief paragraph under each heading in your own Word document, applying it to future visualisations and the web/mobile/printed platform hosting them.\n\n'
    for title,instruction,caution in TASK_STEPS:text+=f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    text+='**Supporting accessibility framework:** Perceivable, Operable, Understandable and Robust. These four principles support the accessibility paragraph; they do not replace the three required concept headings.\n\n**Writing pattern:** context → proposed change → reason → evaluation → source. Keep proposals separate from observations. The course refers to WCAG 2.1; WCAG 2.2 is a supplementary reference.\n\n'
    text+='\n'.join(f'[{name}]({url})' for name,url in SOURCES)
    return text+f'\n\n[Original task]({TASK_URL}).\n\nThis is a study scaffold, not the official completed solution.'

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'1.4','title':'Design Principles — Part 2','module_number':1,'module_title':'Design Thinking','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Distinguish inclusive design usability and accessibility','Apply Perceivable Operable Understandable and Robust','Consider chart information and host-platform interaction','Separate course WCAG 2.1 references from newer guidance','Write three applied task reflections and keep activity briefs separate'],'visual_elements':{'diagrams':False,'tables':False,'highlighted_sections':True}}
