"""English reflection scaffolds based on the reviewed DVS Lesson 1.3."""
CONTENT_REVISION = '2026-10-14-dvs13'
TASK_URL = 'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81528'
LESSON_URL = 'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81517'
UD_SOURCE = 'https://design.ncsu.edu/research/center-for-universal-design/'
CHART_SOURCE = 'https://www.w3.org/WAI/tutorials/images/complex/'
SOURCES = [('NC State Centre for Universal Design', UD_SOURCE), ('W3C WAI complex images tutorial', CHART_SOURCE)]
PRINCIPLES = [
    ('Equitable Use', 'Avoid excluding people from the information or its controls.', 'Consider a chart with an equivalent text explanation and accessible data table. Explain how a reader using assistive technology can obtain the same key information, including relevant privacy controls.', 'An alternative must preserve meaning; merely adding an image label is not equivalent access.'),
    ('Flexibility in Use', 'Offer appropriate choices for different preferences and abilities.', 'Consider readable text that can resize on a web page, both visual and tabular views, and controls that do not depend on one interaction method. Explain which choice helps your intended audience.', 'Do not assume that age alone establishes a particular impairment or preference.'),
    ('Simple and Intuitive Use', 'Make content and actions understandable without unnecessary complexity.', 'Consider a clear chart title, plain-language units, consistent filter labels and a visible next action. Order information by the question the audience needs to answer.', 'Removing detail should not remove context, uncertainty or important limitations.'),
    ('Perceptible Information', 'Communicate the message through cues people can perceive.', 'Consider direct labels, shapes or patterns alongside colour. Add a short chart identification and a fuller text equivalent for a complex chart, including important relationships and values where needed. Check contrast and legibility.', 'A short alt text alone may not convey a complex chart. Do not claim accessibility from colour changes alone.'),
    ('Low Physical Effort', 'Reduce fatigue and unnecessary repeated actions.', 'Consider keeping related controls close, avoiding repeated data entry and offering a clear Reset filters action. Explain how a mobile or dashboard flow reduces repeated movement or effort.', 'Focus on effort and repetition here; control size and reach are explored in the final principle.'),
    ('Tolerance of Errors', 'Prevent avoidable mistakes and make recovery understandable.', 'Consider explaining an empty filter result, preserving input after an error, allowing a filter reset and offering undo for reversible changes. Give a clear path back to a useful view.', 'Do not invent destructive behaviour in a static chart; choose a relevant interaction on its host platform.'),
    ('Size and Space for Approach and Use', 'Provide room for people to see, reach and operate the design.', 'Consider adequately spaced touch controls on mobile, readable chart labels at the actual print size, and a display positioned for different postures in a physical setting.', 'A larger font does not by itself solve reach, spacing, interaction or every access barrier.'),
]
TASK_STEPS = [(f'{i}. {name}', f'Write one short paragraph in your own words. Start with the user need: {meaning} Then apply it to your future visualisation and its platform. {example} Use the pattern: principle → user need → change → reason → check. Add a source for a researched claim.', caution) for i,(name,meaning,example,caution) in enumerate(PRINCIPLES,1)]
ILLUSTRATIONS = [
    {'file':'lesson-1-3-universal-design.png','title':'Seven universal design principles','caption':'In Noroff order: Equitable Use; Flexibility in Use; Simple and Intuitive Use; Perceptible Information; Low Physical Effort; Tolerance of Errors; Size and Space for Approach and Use. NC State places Tolerance for Error fifth and Low Physical Effort sixth. All scenes and chart values are illustrative.'},
    {'file':'task-1-3-platform-adaptations.png','title':'Adapt the visual and its platform','caption':'Illustrative web, mobile and print adaptations combine readable labels, shapes and patterns, text/data alternatives, usable controls and checks at the real display size. Reflect through principle, user need, change, reason and evaluation; a proposal is not proof of accessibility.'},
]
REFLECTION_TEMPLATE = '''# Task 1.3 Universal design reflections

## Purpose
Research universal design and write one brief paragraph for each of the seven principles in your own Word document. Discuss your future visualisations and the web page, mobile phone or printed document that hosts them.

## My visualisation context
Audience and information need: [...]
Visualisation and platform: [...]
Relevant user needs to investigate: [...]

## Writing pattern
Principle → user need → proposed change → reason → evaluation check.
Sentence scaffold: For [audience/context], I would [change] because [reason]. I would check this by [method]. Source for a researched claim: [...].

'''
for i,(name,_,_,_) in enumerate(PRINCIPLES,1):
    REFLECTION_TEMPLATE += f'## {i}. {name}\nMy brief paragraph: [write in your own words]\nSource and check: [...]\n\n'
REFLECTION_TEMPLATE += '''## Final check
- All seven principles have a brief paragraph, not just a list or definitions.
- Each paragraph gives a concrete change, a reason and a relevant check.
- Consider both the visual and its platform; choose relevant web/mobile/print examples.
- Distinguish researched information, proposed changes and actual observations.
- Add source links and do not claim untested compliance or universal success.

## Research starting points
'''
REFLECTION_TEMPLATE += '\n'.join(f'- [{name}]({url})' for name,url in SOURCES)
REFLECTION_TEMPLATE += '\n\nOrder note: Noroff places Low Physical Effort before Tolerance of Errors. NC State numbers Tolerance for Error fifth and Low Physical Effort sixth; the same seven concepts are covered.\n'
RESEARCH_TEMPLATE = '''# Task 1.3 Research and evaluation notes

## Research question
[Which principle, user need or platform issue am I investigating?]

## Source record
Title and organisation: [...]
URL: [...]
Date accessed: [...]
Relevant claim in my own words: [...]
How it supports a reflection: [...]
Limitations or context: [...]

## Proposed evaluation
Visualisation/platform: [...]
User need or barrier: [...]
Proposed change: [...]
How I would check it: [...]
Expected outcome before testing: [...]
Actual observation after a real check: [leave blank until checked]
Follow-up question: [...]

## Research starting points
- NC State: https://design.ncsu.edu/research/center-for-universal-design/
- W3C WAI complex images: https://www.w3.org/WAI/tutorials/images/complex/

A proposed design is not evidence of successful testing or a compliance assessment.
'''
LESSON_CONTENT = '''
### Lesson 1.3: design for people and contexts beyond your own

Universal design aims to make products, information and environments useful to as many people as practicable. Consider sensory, cognitive and physical needs, language, experience and the context of use. A pleasing chart can still exclude a reader if its labels, controls or supporting content are inaccessible.

The lesson introduces seven broad principles. They guide design choices; they are not a substitute for user research, accessibility checks or specific requirements. The explanations below apply the principles to a visualisation and its host platform.

### The seven principles with visualisation examples

'''
for i,(name,meaning,example,caution) in enumerate(PRINCIPLES,1):
    LESSON_CONTENT += f'#### {i}. {name}\n\n{meaning} {example}\n\n**Check:** {caution}\n\n'
LESSON_CONTENT += '''
**Order and naming:** the steps follow Noroff's lesson order. The original NC State principles place Tolerance for Error fifth and Low Physical Effort sixth. Noroff calls the former Tolerance of Errors. Recognise the concept by its name rather than treating the course order as the original numbering. [Original principles](https://design.ncsu.edu/research/center-for-universal-design/).

### Universal and inclusive design

Universal design provides broad guidance across varied users and settings. Inclusive design investigates particular people, barriers and circumstances and involves those people in design and evaluation. Both seek wider participation. A persona or test should represent a relevant need without stereotyping a person or inventing their experience.

For example, a reader with low vision, someone using a small screen in bright light and a person reading a monochrome printout may encounter overlapping information barriers. Clear labels can help across these contexts, but you should still investigate their different needs.

### Communicate the same message in another form

For a complex chart, identify what it shows with a short text alternative and provide a fuller description of the essential information. A suitably structured data table can carry values; explanatory text should also convey important patterns and context. Use real text alongside teaching images so the ideas remain available when images are not visible. [W3C WAI complex images guidance](https://www.w3.org/WAI/tutorials/images/complex/).

### Apply the principle to its platform

| Platform | Examples to investigate |
|---|---|
| Web page | Logical headings, meaningful control names, keyboard operation, text alternatives and data access |
| Mobile phone | Readable labels, reflow, spaced reachable controls and fewer repeated actions |
| Printed document | Readable type at actual size, patterned/labelled series, visible units and explanatory captions |
| Physical display | Sightlines, reach, posture and room for assistive devices |

These are starting points for your own reflection, not evidence that a particular design has passed an accessibility assessment.

### Complete Task 1.3

Research universal design and related topics. Create your own Word document with all seven principle headings and one short paragraph under each. Explain how each would affect a future visualisation and its host platform. No chart dataset or finished application is required.

Use **principle → user need → proposed change → reason → check**, and cite researched claims. Avoid seven repeated generic definitions: show a concrete design decision under each principle. The editable templates below keep proposed checks separate from real observations.

### Lesson activities

**Activity 1.3.1:** try a screen reader and record your own experience of navigating a chosen page. Do not claim a test happened before it did.

**Activity 1.3.2:** reflect on font size, legibility and text representation for a graphic that older people may review. Identify relevant needs without assuming everyone of one age has the same abilities.

**Activity 1.3.3:** inspect the Yale School of Art website for simplicity, purpose, hierarchy and navigation. Base your reflection on the page you actually view; this guide does not claim a current site assessment.

**Activity 1.3.4:** identify three physical/environmental designs around your home that could be more accessible. Explain a barrier, a proposed change and how you would check it.

### Exam explanation pattern

Name the principle, describe the barrier in the case, propose a concrete adaptation, explain the benefit and state how you would evaluate it. Distinguish your proposal from observed results. One change may support more than one principle, but explain the different reasons.

[Lesson introduction](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81517). [Universal design](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81518). [Inclusive design](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81526). [Task 1.3](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81528).
'''
GUIDE = {'course_code':'FI1BBDV75','id':'1.3-task','uid':'dvs-1.3-task-81528','lesson_number':'1.3','title':'Seven universal design reflections','source_url':TASK_URL,'method':'universal inclusive design reflection accessibility','deliverable':'Own Word document with one brief applied paragraph per universal design principle','steps':[s[1] for s in TASK_STEPS],'caution':'Research and write all seven reflections in your own words. Cover visualisations and their host platforms. Proposed adaptations and checks are not observed outcomes or compliance certification.','task_dataset':'','template_file':'DVS Task 1.3 Universal Design Reflections.docx'}
ACTIVITIES = [
    ('1.3.1',81519,'Try a screen reader','Own notes about a real screen-reader experience',['Choose a screen reader and a page to explore','Try navigating headings, controls and information','Record actual actions, barriers and a possible improvement'],'Record your actual experience. Do not invent test results or enable system settings on someone else\'s behalf.'),
    ('1.3.2',81520,'Reflect on readable text','Reflection on legibility for an audience including older readers',['Identify the message and audience needs','Consider readable text size, contrast and representation','Explain an improvement and how to check it'],'Age alone does not establish a specific impairment. Evaluate readability in the actual medium.'),
    ('1.3.3',81521,'Review simplicity on a website','Own reflection on the Yale School of Art website',['Visit the website linked in the Noroff activity','Identify its purpose and inspect hierarchy and navigation','Describe your actual experience and a change supporting simplicity'],'The website may change. Do not treat this guide as a current website audit.'),
    ('1.3.4',81523,'Find three physical design improvements','Three examples around your home with barriers and proposed changes',['Select three physical or environmental designs','Describe who might encounter a barrier and why','Propose a practical improvement and a check for each'],'Use your own observations; do not fabricate home conditions or user experiences.'),
]
GUIDES = [GUIDE]
for ident,chapter,title,deliverable,steps,caution in ACTIVITIES:
    GUIDES.append({'course_code':'FI1BBDV75','id':ident,'uid':f'dvs-{ident}-{chapter}','lesson_number':'1.3','title':title,'source_url':f'https://learning.noroff.no/mod/book/view.php?id=22904&chapterid={chapter}','method':'universal design activity','deliverable':deliverable,'steps':steps,'caution':caution,'task_dataset':'','template_file':''})

def get_task_guide_markdown(guide):
    if guide['id'] != '1.3-task':
        return f"### DVS Activity {guide['id']}: {guide['title']}\n\n**Deliverable:** {guide['deliverable']}\n\n" + '\n'.join(f'{i}. {s}.' for i,s in enumerate(guide['steps'],1)) + f"\n\n**Check:** {guide['caution']}\n\n[Original activity]({guide['source_url']}).\n\nThis activity is separate from Task 1.3's seven-paragraph Word document."
    text = '### DVS Task 1.3: Seven universal design reflections\n\n**Deliverable:** Research the topic and write your own Word document with all seven principles and one brief applied paragraph per principle. Discuss both the visual and the web/mobile/print platform hosting it.\n\n'
    for title,instruction,caution in TASK_STEPS:
        text += f'#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n'
    text += '**Writing pattern:** principle → user need → change → reason → check. Cite researched claims; separate proposed adaptations from actual findings.\n\n**Order note:** Noroff places Low Physical Effort before Tolerance of Errors. NC State numbers Tolerance for Error fifth and Low Physical Effort sixth.\n\n'
    text += '\n'.join(f'[{name}]({url})' for name,url in SOURCES)
    return text+f'\n\n[Original task]({TASK_URL}).\n\nThis is a study scaffold, not the official completed solution.'

def get_lesson():
    return {'course_code':'FI1BBDV75','lesson_number':'1.3','title':'Design Principles — Part 1','module_number':1,'module_title':'Design Thinking','source_url':LESSON_URL,'source_checked_on':'2026-10-14','content':LESSON_CONTENT.strip(),'illustration':None,'dvs_illustrations':ILLUSTRATIONS,'key_points':['Apply all seven universal design principles','Consider both a visualisation and its host platform','Investigate individual needs through inclusive design','Support complex charts with equivalent text and data','Separate proposed adaptations from observed outcomes'],'visual_elements':{'diagrams':False,'tables':True,'highlighted_sections':True}}
