"""Original DVS revision material checked against the signed-in Noroff book."""

from copy import deepcopy
from pathlib import Path

CONTENT_REVISION = "2026-10-14-dvs24-guide"
COURSE_CODE = "FI1BBDV75"
COURSE_NAME = "Data Visualisation"
ASSET_ROOT = Path(__file__).resolve().parent / "assets" / "dvs"
TEMPLATE_ROOT = ASSET_ROOT / "templates"
TASK_URL = "https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81509"
LESSON_URL = "https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81501"

ILLUSTRATIONS = [
    {"file": "lesson-1-1-empathise-define.png", "title": "Empathise and Define", "caption": "Understand the audience, organise Says/Thinks/Does/Feels, and define a user need before choosing a solution. Empathise → Define → Ideate → Prototype → Test is iterative."},
    {"file": "task-1-1-ceo-persona.png", "title": "Hypothetical CEO persona", "caption": "Supplied facts: CEO of an extreme-sports start-up, early twenties, enjoys BASE jumping. Goals, information needs, pain points and presentation preferences are hypotheses to label and validate."},
]

TASK_STEPS = [
    ("1. Read the brief and record facts", "The audience is the CEO receiving a presentation of the market analysis for snow-free bobsleds. Record only the supplied facts: he is the CEO, is in his early twenties and enjoys BASE jumping. The deliverable is a hypothetical persona, not a market-analysis report.", "The brief supplies no market findings, research quotations or personality measurements."),
    ("2. Draft the hypothetical persona", "Use the persona template to describe a fictional name, goals, information needs, potential pain points and technical familiarity. Mark each added characteristic as a hypothetical assumption. Write a question that could validate an important assumption.", "Enjoying BASE jumping does not prove that the CEO is reckless, prefers flashy charts or has a particular level of technical knowledge."),
    ("3. Connect the persona to presentation choices", "Explain how each proposed audience need would influence the presentation. For example, a hypothetical need to compare adoption opportunities may support a clearly labelled comparison chart. State the decision, required evidence and appropriate level of detail.", "Chart examples are design proposals. Do not invent market statistics, sales, profitability or stakeholder feedback."),
    ("4. Review the persona and define the need", "Check consistency with the three supplied facts. Write a user story and problem statement using the templates below. Ensure proposed visuals support the audience's decision, explain uncertainty and preserve readable labels and context.", "The task asks for a persona. User stories and problem statements support your reasoning; they do not replace that deliverable or prescribe a final design."),
]

PERSONA_TEMPLATE = """# Task 1.1 Hypothetical CEO persona

## Purpose
Describe the audience for a presentation of market analysis about snow-free bobsleds. Separate the supplied facts from additional hypothetical assumptions.

## Supplied facts
- CEO of an extreme-sports start-up
- In his early twenties
- Enjoys BASE jumping

## Fictional identity
Name: [optional fictional name]
Role: CEO

## Hypothetical goals and decisions
[What might he need to decide after seeing the analysis? Label assumptions.]

## Hypothetical information needs
[Which comparisons, context and uncertainty might support that decision?]

## Potential pain points
[What might make the presentation difficult to understand?]

## Presentation needs
[Proposed clarity, detail, labels and visual choices, with reasons.]

## Assumptions and questions to validate
Assumption: [...]
Reason for proposing it: [...]
Question to validate it: [...]

## User story
As a [user], I want to [goal], so that [benefit].

## Problem statement
[User] needs a way to [need] because [insight].

## Final check
- Supplied facts are accurate.
- Additional characteristics are labelled hypothetical.
- No fabricated interview evidence or market results.
- Presentation choices follow from audience needs.
- The persona addresses the CEO brief, not the separate Funky Monkey activity.
"""

LESSON_CONTENT = """
### Lesson 1.1: understand the audience before choosing a visual

A visualisation should help its audience understand evidence and make a decision. Start by investigating the reader's goals, context and difficulties. This lesson introduces **design thinking** and focuses on **Empathise** and **Define**.

**Empathise → Define → Ideate → Prototype → Test** is an iterative process. Feedback may send you back to an earlier stage. The course also discusses implementation when a tested solution is put into use; keep that distinct from the five-stage teaching model.

### Step 1 — Empathise through interviews and observation

Ask open questions about the user's actual experiences. Listen attentively and observe how the person uses information. Record what was said or observed and distinguish it from your interpretation.

For a stakeholder presentation, useful questions are: What decision do you need to make? What evidence would help? What is hard to understand in the current presentation? How much time and technical familiarity do you have?

### Step 2 — build an empathy map

| Quadrant | Evidence to organise |
|---|---|
| Says | Actual statements, with their source |
| Thinks | Reported thoughts; clearly label interpretations |
| Does | Observed actions and behaviour |
| Feels | Reported feelings or cautious interpretations to validate |

Empty quadrants identify research gaps. Do not invent interview evidence to complete a map. In a hypothetical exercise, label fictional examples explicitly.

### Step 3 — Define through analysis and synthesis

Analysis breaks information into smaller parts; synthesis connects the parts into an understanding of user needs. Use affinity mapping to group related observations and identify recurring themes. Keep the original evidence traceable so a theme does not become an unsupported claim.

A useful problem statement is user-centred, focused enough to guide work and open enough to allow alternative solutions. Define the need before prescribing a chart, dashboard or technical feature.

**Problem statement:** [User] needs a way to [need] because [insight].

### Step 4 — describe a persona

A persona represents a relevant audience's goals, needs, behaviour and difficulties. Research-based personas summarise evidence; the CEO persona in Task 1.1 is explicitly **hypothetical**. Label invented characteristics as design assumptions rather than presenting them as researched facts.

Task 1.1's only supplied personal facts are that the CEO is male, in his early twenties and enjoys BASE jumping. The business context is an extreme-sports start-up receiving a market-analysis presentation about snow-free bobsleds. Age and hobbies do not establish technical expertise, business risk appetite or preferred chart style.

### Step 5 — connect persona, story and scenario

**User story:** As a [user], I want to [goal], so that [benefit].

A scenario adds the context and sequence of actions. A storyboard illustrates that scenario in panels. A **How Might We** question opens the problem for ideation: How might we help [user] achieve [goal] while addressing [difficulty]?

These tools support a clear understanding of the need; they are not automatically solutions.

### Step 6 — apply the lesson to the two separate briefs

**Task 1.1:** create the hypothetical CEO persona. Use the task guide below to record facts, draft assumptions, connect needs to presentation choices and review the result.

**Activity 1.1.1:** create a rough persona for Funky Monkey, a statement-sock brand aiming to become well known among athletes. Its target audience is men and women aged 25–35 participating in mountain biking, triathlons or marathons. Keep this audience separate from the CEO brief.

### Step 7 — check an exam explanation

Explain the concept, apply it to the specified audience, identify evidence or assumptions, and justify the design implication. A safe answer pattern is: **audience → need → evidence or labelled assumption → design implication → validation question**.

Example of reasoning, explicitly hypothetical: If the CEO needs a quick comparison of adoption opportunities, a readable comparison visual may help. This is a proposed information need to validate, not a finding from market data or a known personal preference.

[Original lesson](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81501). [Empathise](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81503). [Define](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81504). [Personas and affinity mapping](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81505). [User stories, problem statements and Activity 1.1.1](https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81506).
"""


def get_dvs_persona_template():
    return PERSONA_TEMPLATE


def get_dvs_task_guide_markdown(guide):
    if guide["lesson_number"] == "2.4":
        from dvs_lesson24 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["lesson_number"] == "2.3":
        from dvs_lesson23 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["lesson_number"] == "2.2":
        from dvs_lesson22 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["lesson_number"] == "2.1":
        from dvs_lesson21 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["lesson_number"] == "1.4":
        from dvs_lesson14 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["lesson_number"] == "1.3":
        from dvs_lesson13 import get_task_guide_markdown
        return get_task_guide_markdown(guide)
    if guide["id"] == "1.2-task":
        from dvs_lesson12 import get_task_guide_markdown
        return get_task_guide_markdown()
    if guide["id"] == "1.1.1":
        return "### Activity 1.1.1: Funky Monkey athlete persona\n\nCreate a rough hypothetical persona for a statement-sock brand seeking recognition among athletes. Supplied audience: men and women aged 25–35 who participate in mountain biking, triathlons or marathons.\n\n1. Record the supplied brand goal and audience.\n2. Propose labelled hypothetical goals, needs and pain points.\n3. Explain a design implication and a question to validate it.\n\nKeep this activity separate from the CEO in Task 1.1.\n\n[Original activity](" + guide["source_url"] + ")."
    text = "### DVS Task 1.1: Hypothetical CEO persona\n\n"
    text += "**Deliverable:** A hypothetical persona for the CEO receiving the snow-free bobsled market-analysis presentation.\n\n**Supplied facts:** CEO of an extreme-sports start-up; early twenties; enjoys BASE jumping.\n\n"
    text += "**Evidence boundary:** Additional characteristics are hypothetical assumptions. Do not invent real interviews, market results or measured personality traits. Enjoying BASE jumping does not establish business risk appetite, technical knowledge or visual preferences.\n\n"
    for title, instruction, caution in TASK_STEPS:
        text += f"#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n"
    text += "**Persona fields:** fictional identity; supplied facts; hypothetical goals; information needs; pain points; presentation needs; assumptions and validation questions.\n\n"
    text += "**User story:** As a [user], I want to [goal], so that [benefit].\n\n**Problem statement:** [User] needs a way to [need] because [insight].\n\n"
    text += f"[Original task on Noroff]({TASK_URL}).\n\nThis is an original study scaffold, not Noroff's completed solution."
    return text


from dvs_lesson12 import GUIDE as TASK12_GUIDE

DVS_TASK_GUIDES = [
    {"course_code": COURSE_CODE, "id": "1.1-task", "uid": "dvs-1.1-task-81509", "lesson_number": "1.1", "title": "Hypothetical CEO persona", "source_url": TASK_URL, "method": "persona", "deliverable": "Hypothetical persona supporting a presentation to the CEO", "steps": [s[1] for s in TASK_STEPS[:3]], "caution": "Only the CEO role, early twenties and BASE-jumping hobby are supplied facts; mark added characteristics as hypothetical. Do not invent interview evidence or market results.", "task_dataset": "", "template_file": "DVS Task 1.1 Persona Template.docx"},
    {"course_code": COURSE_CODE, "id": "1.1.1", "uid": "dvs-1.1.1-81506", "lesson_number": "1.1", "title": "Funky Monkey athlete persona", "source_url": "https://learning.noroff.no/mod/book/view.php?id=22904&chapterid=81506", "method": "persona", "deliverable": "Rough hypothetical athlete persona for a statement-sock brand", "steps": ["Record the brand goal and target audience", "Propose labelled hypothetical goals, needs and pain points", "Explain a design implication and a question to validate it"], "caution": "Funky Monkey targets athletes aged 25–35; this is a separate brief from the CEO task.", "task_dataset": "", "template_file": ""},
]
DVS_TASK_GUIDES.append(TASK12_GUIDE)
from dvs_lesson13 import GUIDES as GUIDES13
DVS_TASK_GUIDES.extend(GUIDES13)
from dvs_lesson14 import GUIDES as GUIDES14
DVS_TASK_GUIDES.extend(GUIDES14)
from dvs_lesson21 import GUIDE as GUIDE21
DVS_TASK_GUIDES.append(GUIDE21)
from dvs_lesson22 import GUIDE as GUIDE22
DVS_TASK_GUIDES.append(GUIDE22)
from dvs_lesson23 import GUIDE as GUIDE23
DVS_TASK_GUIDES.append(GUIDE23)
from dvs_lesson24 import GUIDES as GUIDES24
DVS_TASK_GUIDES.extend(GUIDES24)
for _guide in DVS_TASK_GUIDES:
    _guide["markdown"] = get_dvs_task_guide_markdown(_guide)


def get_dvs_task_guides(number):
    return deepcopy([g for g in DVS_TASK_GUIDES if g["lesson_number"] == str(number)])


def _get_lesson11():
    return [{"course_code": COURSE_CODE, "lesson_number": "1.1", "title": "Design Thinking — Part 1", "module_number": 1, "module_title": "Design Thinking", "source_url": LESSON_URL, "source_checked_on": "2026-10-14", "content": LESSON_CONTENT.strip(), "illustration": None, "dvs_illustrations": deepcopy(ILLUSTRATIONS), "key_points": ["Empathise through interviews and observation", "Organise Says, Thinks, Does and Feels with traceable evidence", "Synthesise research into a user-centred problem statement", "Label hypothetical persona characteristics and link them to presentation needs"], "visual_elements": {"diagrams": False, "tables": True, "highlighted_sections": True}}]


def get_dvs_course_lessons():
    from dvs_lesson12 import get_lesson
    from dvs_lesson13 import get_lesson as get_lesson13
    from dvs_lesson14 import get_lesson as get_lesson14
    from dvs_lesson21 import get_lesson as get_lesson21
    from dvs_lesson22 import get_lesson as get_lesson22
    from dvs_lesson23 import get_lesson as get_lesson23
    from dvs_lesson24 import get_lesson as get_lesson24
    return _get_lesson11() + [deepcopy(get_lesson()), deepcopy(get_lesson13()), deepcopy(get_lesson14()), deepcopy(get_lesson21()), deepcopy(get_lesson22()), deepcopy(get_lesson23()), deepcopy(get_lesson24())]


def _get_dvs_training_modules():
    return {"DVS Module 1: Design Thinking": {"course": COURSE_NAME, "course_code": COURSE_CODE, "description": "Noroff Lesson 1.1: Empathise, Define and a hypothetical CEO persona. Later lessons are added as they are reviewed.", "lessons": [lesson for lesson in get_dvs_course_lessons() if lesson["module_number"] == 1], "exercises": [{"title": "Task 1.1: Hypothetical CEO persona", "type": "case_study", "question": "Create a hypothetical persona for the CEO in the brief. Distinguish supplied facts from assumptions and explain one presentation implication.", "hint": "Start with CEO, early twenties and enjoys BASE jumping. Label additional characteristics.", "answer": "A defensible persona retains the supplied facts, labels its proposed goals and needs as hypothetical, links them to a clear presentation decision and identifies questions to validate the assumptions."}], "quiz": [{"question": "Which claim is supported by the Task 1.1 brief?", "options": ["The CEO prefers complicated charts", "The CEO enjoys BASE jumping", "The CEO has advanced statistical expertise", "The CEO wants reckless business decisions"], "correct": 1, "explanation": "Only the BASE-jumping hobby is supplied among these choices. The other claims would be assumptions to label and validate."}]}}


def get_dvs_training_modules():
    modules = _get_dvs_training_modules()
    module = modules["DVS Module 1: Design Thinking"]
    module["description"] = "Reviewed Noroff Module 1 Lessons 1.1–1.4: design thinking, persona and wireframe tasks, universal design, inclusion, usability and accessibility."
    module["exercises"].append({"title": "Task 1.2: Mobile BMI wireframe", "type": "case_study", "question": "Sketch mobile input and results areas, chart choice, age filtering and a labelled current-user BMI marker.", "hint": "Use simple boxes and labels. Include height, weight, age and a submission button.", "answer": "The sketch includes all required controls and a visible labelled user marker, explains units and transitions, and uses placeholders or labelled illustrative points."})
    module["quiz"].append({"question": "What is the required deliverable for Task 1.2?", "options": ["A production BMI application", "A low-fidelity mobile wireframe", "A medical diagnosis", "A real user health dataset"], "correct": 1, "explanation": "The task asks for a simple sketch, with input and customisable results areas."})
    module["exercises"].append({"title": "Task 1.3: Universal design reflections", "type": "case_study", "question": "Write seven applied paragraphs for your future visualisations and their platforms.", "hint": "Use principle, user need, proposed change, reason and check.", "answer": "Each paragraph applies a named principle to a concrete visual or platform decision and distinguishes a proposed check from real findings."})
    module["quiz"].append({"question": "Which is a defensible universal design reflection?", "options": ["Changing colours proves full accessibility", "A proposed design is a completed user test", "Explain a barrier, propose an adaptation and identify a check", "Only the chart matters; its platform is irrelevant"], "correct": 2, "explanation": "The task needs applied reasoning about the visual and its host platform, supported by sources and relevant evaluation."})
    module["exercises"].append({"title": "Task 1.4: Three applied reflections", "type": "case_study", "question": "Write one applied paragraph under Inclusive Design, Usability and Accessibility headings.", "hint": "Consider the visual and platform, with a change, reason, proposed check and source.", "answer": "The three paragraphs apply distinct concepts and explain relevant adaptations and checks without presenting planned tests as findings."})
    module["quiz"].append({"question": "What are Task 1.4's required headings?", "options": ["All seven universal design principles", "Only the four POUR principles", "Inclusive Design Usability and Accessibility", "A market analysis and medical diagnosis"], "correct": 2, "explanation": "Three brief concept reflections are required. POUR supports the accessibility reasoning."})
    modules["DVS Module 2: User Experience and User Experience Design"] = {
        "course": COURSE_NAME, "course_code": COURSE_CODE,
        "description": "Reviewed Lessons 2.1–2.4: UX design, chart ethics, raster/vector graphics, software comparison and practical GIMP image manipulation.",
        "lessons": [lesson for lesson in get_dvs_course_lessons() if lesson["module_number"] == 2],
        "exercises": [{"title": "Task 2.1: Website review and UX application", "type": "case_study", "question": "Plan both task answers and distinguish observed website behaviour from interpretation and proposals.", "hint": "Record final URLs and access limitations; justify each design judgement with evidence and a relevant UX facet.", "answer": "Question 1 is one page covering both named sites with justified strengths and weaknesses. Question 2 is at least half a page defining UX design in own words and applying it to visualisations, in Word Arial 11 pt. Redirected pages must be identified and historical findings must not be invented."}],
        "quiz": [{"question": "What can a redirect to OECD About establish?", "options": ["The old Forum had poor keyboard access", "The original Forum interface was evaluated", "The supplied link currently reaches a different page", "All OECD pages conform to WCAG"], "correct": 2, "explanation": "Record the current destination and limitation. An approved archive or replacement is needed to evaluate the historical Forum interface."}]
    }
    module2 = modules["DVS Module 2: User Experience and User Experience Design"]
    module2["exercises"].append({"title": "Task 2.2: Graph analysis and four rules", "type": "case_study", "question": "Explain a specific misleading feature in each supplied TV graph, then apply all four course rules to your workflow.", "hint": "Compare labels and geometry, baseline, time gaps and future data status. Distinguish observations from inferred effects.", "answer": "A defensible answer uses visible evidence, explains the misleading effect, proposes a correction and identifies limits. It states each course rule with a personal view and concrete action, without claiming verified data or deliberate intent."})
    module2["quiz"].append({"question": "Which scale judgement is defensible?", "options": ["Every line chart must start at zero", "Bars need a zero baseline; a line-chart zoom requires context and accurate positions", "A correct value label excuses an incorrectly plotted point", "A planned future value is an observed historical result"], "correct": 1, "explanation": "Bars encode magnitude as length. Line charts can use a justified non-zero range, but the scale and geometry must support honest interpretation."})
    module2["exercises"].append({"title": "Task 2.3: Graphics and software comparison", "type": "case_study", "question": "Explain the graphics concepts and compare all three software candidates using dated primary evidence.", "hint": "Include platforms, price, raster/vector support and complex functions; specify editions and company assumptions.", "answer": "A useful comparison includes CorelDRAW, Procreate and Photopea with all four required dimensions, sources and dates. It distinguishes annual, app-purchase and prepaid price models and avoids invented company needs."})
    module2["quiz"].append({"question": "What does Save do in GIMP?", "options": ["Always exports a JPEG", "Saves an editable XCF project", "Converts every raster image to vector", "Preserves all undo history forever"], "correct": 1, "explanation": "Save stores XCF project structure. Export creates a sharing format; XCF does not retain undo history."})
    module2["exercises"].append({"title": "Task 2.4: Three image designs with GIMP", "type": "case_study", "question": "Plan the leaves/tree blend, pineapple on Stone and strawberry-sales illustration, then perform and record actual checks.", "hint": "Set leaves opacity to 80%, keep Stone below pineapple and do not invent chart units or values.", "answer": "The task requires three original image outputs. Notes support the images; layer settings and export checks must be performed in GIMP rather than inferred by Exam Resolver."})
    module2["quiz"].append({"question": "Which layer has 80% opacity in Task 2.4 Question 1?", "options": ["The tree", "The leaves", "Every layer", "The pineapple"], "correct": 1, "explanation": "The instruction sets leaves opacity to 80%. The butterfly example used a different setting."})
    return modules
