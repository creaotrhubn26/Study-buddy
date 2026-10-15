"""Original preparation material based on the DVS assessment brief and landing page.

No assessment attempt was started and no live assessment questions were read.
5.1 is a Study Buddy navigation identifier, not an official Noroff task number.
"""
from copy import deepcopy

CONTENT_REVISION = "2026-10-15-dvs5-preparation"
COURSE_CODE = "FI1BBDV75"
BRIEF = "https://learning.noroff.no/mod/book/view.php?id=22902&chapterid=81498"
MODULE_BRIEF = "https://learning.noroff.no/mod/book/view.php?id=22902&chapterid=81497"
ASSESSMENT = "https://learning.noroff.no/mod/quiz/view.php?id=22933"
SECTION = "https://learning.noroff.no/course/section.php?id=1772"
RULES = """| Item | Published requirement, checked 15 October 2026 |
|---|---|
| Prerequisites | Complete all four module assessments before attempting the CA |
| Format | One quiz attempt, including practical work |
| Total / pass mark | 80 marks / 32 marks (40%) |
| Duration | 48 hours from starting; closing the browser does not pause the timer |
| Availability | Opened 12 October 2026 at 08:00; closes 18 October 2026 at 23:59, as displayed on Noroff |
| Section A | Create visualisations in Excel |
| Section B | Select/edit images and construct a PowerPoint presentation |
"""
BOUNDARY = ("This is preparation, not a completed assessment or an official Task 5.1. "
    "The actual questions, datasets, detailed file requirements and marking allocation were not opened. "
    "Use the current assessment instructions when you begin. Keep live assessment questions and answers out of the shared quiz bank.")
ILLUSTRATIONS = [{"file":"module-5-assessment-workflow.png", "title":"Prepare the complete workflow",
    "caption":"Practise Excel summaries and charts, image layers/editing/export, then PowerPoint presentation and rehearsal. The illustration uses schematic practice visuals, not assessment data or questions. Verify the final files in the actual applications."}]

STEPS = [
    ("1. Confirm the rules and your time window",
     "Read the brief and quiz landing page. Confirm the four module assessments are complete. Record the displayed closing time and account timezone, choose a start time and plan a finish with a buffer before both the 48-hour duration and course closing time.",
     "One attempt only. The timer runs while the browser is closed. Do not assume starting late extends the course deadline; recheck the current Noroff instructions."),
    ("2. Rehearse Excel with lesson practice data",
     "Use a Module 3 or 4 practice dataset in a working copy. Inspect fields and units, distinguish count from average, create a justified chart, label axes and verify chart values against the summary. Practise group-average filters before rounding.",
     "Practice datasets are not confirmed CA datasets. Match each actual question to its specified source when the assessment begins. Never present a chart choice as a known exam requirement."),
    ("3. Rehearse image selection and editing",
     "Practise importing an image, keeping editable layers, cropping/scaling without distortion, masking or removing a background where appropriate, and exporting a copy. Reopen the editable file and exported image to check dimensions, edges, transparency and legibility.",
     "The landing page confirms image selection/editing, but does not specify an image, editing operation, format or software version for the actual questions. Record only checks you performed."),
    ("4. Rehearse a coherent PowerPoint presentation",
     "Plan a consistent colour palette that also works in Excel charts. Place a practice chart and edited image on readable slides, retain source and unit context, and rehearse the presentation. Revisit themes, transitions, object animations and custom shows from Module 4.",
     "Facet, Wisp, Morph, Float In and three custom shows are previous lesson-task requirements, not confirmed CA requirements. Native effects must be checked in PowerPoint; static images cannot prove them."),
    ("5. Check the complete file workflow",
     "Move a practice chart and edited image into a practice presentation. Choose editable/embedded, linked or static content deliberately. Save working files separately from exports, reopen them and run the slide show. Check that no link depends on an unavailable local path.",
     "This is a suggested rehearsal. The actual assessment controls required file names, formats, upload locations and deliverables; none are prescribed by this preparation template."),
    ("6. Diagnose gaps and revise with evidence",
     "Use the existing module quiz bank and lesson tasks. Explain mistakes in English using concept → application → evidence → limitation. Record a weak skill, the relevant lesson, one practice action and a real result. Ask Exam Resolver to review these preparation notes.",
     "The bank contains reviewed module practice questions, not the unseen CA. A good practice score is not a guarantee of the assessment result. Check course rules before using assistance during the assessment."),
    ("7. Complete your readiness check",
     "Confirm time, prerequisites, software access, backup copies, working space and the three practical skills. Save your study plan outside the session. When ready, open the Noroff landing page, read any final instructions and make the decision to start the attempt yourself.",
     "Study Buddy does not start, pause, extend, submit or grade the Noroff assessment. Once started, follow its actual questions and final submission instructions; a local saved file alone is not proof of submission."),
]

LESSON_TEXT = """### Course Assessment preparation

This is an original Study Buddy preparation lesson for **Module 5 — Course Assessment**. The navigation label **5.1** is internal to this app; Noroff's brief does not list a new Lesson 5.1 or Task 5.1. We reviewed both brief chapters and the quiz landing page without starting an attempt.

#### Understand the assessment before practising

""" + RULES + """

The opening page describes **practical work inside a quiz**. Section A concerns Excel visualisations; Section B concerns image selection/editing and a PowerPoint presentation. It asks you to read each question completely, use the correct dataset and plan a visually appealing, coordinated colour scheme for the charts and slides.

This is not evidence that the exam repeats the fruit or chocolate tasks. The landing page does not reveal the question count, question-level marks, actual datasets, slide count, themes, export formats or filenames. Treat those details as unknown until the real instructions are available. The course brief says passed/not passed; do not infer a guaranteed result from a practice score.

#### Plan the uninterrupted clock

Closing your browser does **not** stop the 48-hour timer. Plan to finish before both your personal 48-hour window and the published closing time, with time for reopening files and final submission checks. For example, a practice planning scenario starting Thursday 15 October at 12:00 reaches 48 hours on Saturday 17 October at 12:00. This is an illustrative schedule, not a booked start or a live countdown. Confirm the timezone displayed in your Noroff account. The dates above were checked on 15 October 2026 and may change; revisit the source.

#### Rehearse three connected skills

| Skill | Relevant reviewed material | Evidence of readiness |
|---|---|---|
| Understand the audience and design ethically | Modules 1–2: personas, design, usability, accessibility and truthful graphics | Explain a visual choice, its audience benefit and a limitation |
| Excel visualisation | Module 3 and Task 4.4 | A summary reconciles to the source and a chart shows the intended measure |
| Image editing | Lessons 2.3–2.4 | An editable project and a reopened export retain the intended content |
| PowerPoint delivery | Lessons 4.1–4.4 | Readable slides, appropriate chart transfer and a tested slide show |

Use the downloaded lesson files for rehearsal. Practise the difference between a category bar/column chart and an XY scatter; between average and count; and between filtering individual rows and filtering calculated group means. For images, distinguish the editable layered project from an exported picture. For presentations, distinguish a slide transition from an object animation, and check native effects in the application.

#### Use a working record, not a guessed answer

Record **requirement → action → evidence → limitation → next check**. A plan to test a file is not a completed test. An imagegen illustration explains a process; it is not evidence that an Excel calculation or PowerPoint effect works. If a fact is unknown, identify the source you must inspect rather than inventing it.

The seven-step preparation guide below includes a downloadable English working template and an Exam Resolver handoff. The resolver reviews your written preparation, preserves the selected step and flags gaps. It cannot inspect local application files merely because you mention them, verify actual slide animation or confirm a Noroff submission.

#### Keep preparation and the live assessment distinct

The Noroff landing page says assessment questions and answers must not be discussed or shared with other students on any platform. Keep live CA material out of the shared quiz bank. The existing bank is module revision material. Check the assessment's assistance rules before using tools during your attempt. No attempt was started and no live question was collected to create this lesson.
"""

GUIDE = {"course_code":COURSE_CODE,"id":"5.1","uid":"dvs-5.1-preparation-81498", "lesson_number":"5.1",
    "title":"Course Assessment preparation — Study Buddy", "source_url":BRIEF,"method":"assessment preparation",
    "deliverable":"Your own readiness plan and practice evidence; optional study notes, not a Noroff submission",
    "steps":[s[1] for s in STEPS],"step_details":STEPS,"caution":BOUNDARY,"task_dataset":"","template_file":""}
GUIDES = [GUIDE]

def get_template(guide=None):
    text = "# DVS Course Assessment preparation record\n\nOptional Study Buddy worksheet. Not an official Task 5.1 or an assessment answer.\n\n"
    text += f"Brief: {BRIEF}\nLanding page: {ASSESSMENT}\n\n"
    text += "## Current rules and schedule — verify on Noroff\nDate checked: [...]\nAccount timezone: [...]\nCurrent closing time: [...]\nAll four module assessments complete: [verify]\nPlanned start: [...]\nPlanned finish, before both limits and with buffer: [...]\n\n"
    for title, instruction, caution in STEPS:
        text += f"## {title}\nPractice action: {instruction}\nCheck: {caution}\nMy plan: [...]\nActual evidence and file/source: [...]\nRemaining gap: [...]\n\n"
    return text + "## Evidence log\n| Skill | Practice source | Action actually completed | Check and result | Remaining work |\n|---|---|---|---|---|\n| Excel | [...] | [...] | [...] | [...] |\n| Image editing | [...] | [...] | [...] | [...] |\n| PowerPoint | [...] | [...] | [...] | [...] |\n\n## Readiness decision\n[What is ready? What still needs practice?]\n\nDo not place live CA questions or answers in the shared quiz bank.\n"

def get_task_guide_markdown(guide):
    text = "### DVS Activity 5.1: Course Assessment preparation — Study Buddy\n\n" + BOUNDARY + "\n\n" + RULES + "\n\n"
    for title, instruction, caution in STEPS:
        text += f"#### {title}\n\n{instruction}\n\n**Check:** {caution}\n\n"
    return text + f"[CA brief]({BRIEF}) · [Module prerequisites]({MODULE_BRIEF}) · [Quiz landing page]({ASSESSMENT}).\n\nChecked 15 October 2026. Recheck current dates and rules on Noroff."

def get_lessons():
    return [{"course_code":COURSE_CODE,"lesson_number":"5.1","title":"Course Assessment — Preparation",
        "module_number":5,"module_title":"Course Assessment","source_url":BRIEF,"source_checked_on":"2026-10-15",
        "content":LESSON_TEXT.strip()+f"\n\n[CA brief]({BRIEF}) · [Quiz landing page]({ASSESSMENT}) · [Module prerequisites]({MODULE_BRIEF}).",
        "illustration":None,"dvs_illustrations":deepcopy(ILLUSTRATIONS),
        "key_points":["One attempt; 48-hour timer continues when the browser is closed","Practise Excel, image editing and PowerPoint as a connected workflow","Use the specified dataset and verify the actual deliverables","Keep a readiness record; recheck current Noroff rules before starting"],
        "visual_elements":{"diagrams":False,"tables":True,"highlighted_sections":True}}]

def step_context(guide,base_key,state):
    index = state.get(f"{base_key}_dvs_step_{guide['uid']}",0)
    if not isinstance(index,int) or not 0 <= index < len(STEPS):
        index = 0
    title,instruction,caution = STEPS[index]
    return f"Current selected step: {title}\n{instruction}\nCheck: {caution}\nPreparation only; no live assessment questions are supplied.\n\n"
