"""Shared English DVS task flow for Lessons and Universal Exam Resolver."""

import streamlit as st
import dvs_curriculum
from dvs_curriculum import (ASSET_ROOT, TEMPLATE_ROOT, COURSE_CODE, ILLUSTRATIONS,
    TASK_STEPS, get_dvs_persona_template)

CONTENT_REVISION = "2026-10-14-dvs24-guide"


def get_dvs_draft(uid):
    if uid.startswith("dvs-2.4"):
        from dvs_lesson24 import TASK_TEMPLATE, ACTIVITY_TEMPLATES
        default = TASK_TEMPLATE if uid == "dvs-2.4-task-81584" else ACTIVITY_TEMPLATES[uid]
    elif uid == "dvs-2.3-task-81573":
        from dvs_lesson23 import STUDY_TEMPLATE, COMPARISON_TEMPLATE
        default = STUDY_TEMPLATE + "\n\n" + COMPARISON_TEMPLATE
    elif uid == "dvs-2.2-task-81562":
        from dvs_lesson22 import ANALYSIS_TEMPLATE, RULES_TEMPLATE, REVIEW_TEMPLATE
        default = ANALYSIS_TEMPLATE + "\n\n" + RULES_TEMPLATE + "\n\n" + REVIEW_TEMPLATE
    elif uid == "dvs-2.1-task-81556":
        from dvs_lesson21 import REPORT_TEMPLATE, APPLICATION_TEMPLATE, EVIDENCE_TEMPLATE
        default = REPORT_TEMPLATE + "\n\n" + APPLICATION_TEMPLATE + "\n\n" + EVIDENCE_TEMPLATE
    elif uid == "dvs-1.2-task-81516":
        from dvs_lesson12 import WIREFRAME_TEMPLATE, TEST_TEMPLATE
        default = WIREFRAME_TEMPLATE + "\n\n" + TEST_TEMPLATE
    elif uid == "dvs-1.4-task-81544":
        from dvs_lesson14 import REFLECTION_TEMPLATE, RESEARCH_TEMPLATE
        default = REFLECTION_TEMPLATE + "\n\n" + RESEARCH_TEMPLATE
    elif uid == "dvs-1.3-task-81528":
        from dvs_lesson13 import REFLECTION_TEMPLATE, RESEARCH_TEMPLATE
        default = REFLECTION_TEMPLATE + "\n\n" + RESEARCH_TEMPLATE
    else:
        default = get_dvs_persona_template()
    return st.session_state.get("dvs_persona_drafts", {}).get(uid, default)


def remember_draft(uid, widget_key):
    drafts = dict(st.session_state.get("dvs_persona_drafts", {}))
    drafts[uid] = st.session_state[widget_key]
    st.session_state["dvs_persona_drafts"] = drafts


def prepare_task_in_resolver(guide, lesson_base):
    resolver_base = "course_exam_connector_fi1bbdv75_learn_practice"
    step = st.session_state.get(f"{lesson_base}_dvs_step_{guide['uid']}", 0)
    st.session_state[f"{resolver_base}_dvs_step_{guide['uid']}"] = step
    if guide["lesson_number"] == "2.4":
        kind = "Task 2.4" if guide["id"] == "2.4-task" else f"Activity {guide['id']}"
        prompt = (f"DVS {kind}: Review my written GIMP editing plan and actual check notes in English. Required output: {guide['deliverable']} {guide['caution']} "
            "Flag placeholders, distinguish planned and completed actions, and give specific next actions. The selected step is available in the task guide. Do not claim to inspect image pixels, open XCF files, operate GIMP, verify actual layer settings or submit work.\n\nMy editing plan and check notes:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "2.3-task":
        prompt = ("DVS Task 2.3: Review my seven-question study notes in English. Questions 1–6 cover graphics types, five raster formats, three vector formats, pixel storage, three raster-oriented tools and two vector-oriented tools. Question 7 compares CorelDRAW, Procreate and Photopea for a hypothetical ordinary paper company with year-end funds left: include platforms, price, raster/vector support and complex functions. Specify product editions, dated official sources, currencies, tax and licence periods. Flag placeholders and company assumptions. Do not invent current prices, device fleets, benchmarks or completed tests. A recommendation is optional; no page count or font is specified. Review written notes without submitting or grading the H5P activity, installing software or inspecting project pixels.\n\nMy study answers and comparison:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "2.2-task":
        prompt = ("DVS Task 2.2: Review both parts of my draft in English. Question 1: analyse what might mislead in the supplied unemployment and public health expenditure TV graphs. Question 2: state and apply all four course rules, each with my own view and a concrete visualisation workflow action. Check evidence, misleading effects, corrections and limitations. Flag placeholders. Distinguish label-position inconsistency, truncated bars, justified zoomed lines, time gaps and future status. Do not invent verified datasets, measured pixel geometry, broadcaster intent or completed peer feedback. There is no specified page count or font requirement. Review written evidence; you are not inspecting chart pixels.\n\nMy graph analysis, rules and review notes:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "2.1-task":
        prompt = ("DVS Task 2.1: Review both parts of my draft in English. Question 1: one-page report identifying good and bad design elements of OECD Data and the OECD Forum Network, with justified evidence. Question 2: at least half a page defining UX design in my own words and applying it to data analysis visualisations, in Word using Arial 11 pt. Flag placeholders and missing reasons. Record redirects and scope limitations; do not invent old Forum observations, completed tests or conformance. Review only the evidence supplied; final formatting and page lengths need checking in Word.\n\nMy report, UX application and evidence:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "1.1-task":
        prompt = ("DVS Task 1.1: Review my hypothetical CEO persona for the snow-free bobsled market-analysis presentation. "
            "Write in English. Supplied facts: CEO of an extreme-sports start-up, early twenties, enjoys BASE jumping. "
            "Treat additional characteristics as hypothetical assumptions. Flag unfilled placeholders. "
            "Do not invent real interviews, market findings or known personal preferences.\n\nMy persona draft:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "1.2-task":
        prompt = ("DVS Task 1.2: Review my low-fidelity mobile BMI wireframe plan. Write in English. "
            "Required: height, weight and age inputs, submission, other users' BMI visualisation, "
            "a highlighted current-user marker, chart selection and an age filter. "
            "Check units, transitions, invalid inputs and empty/filter states. Flag unfilled placeholders. "
            "Do not invent actual user data, completed tests or health diagnoses. The deliverable is a sketch, not a production app.\n\nMy wireframe and test plan:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "1.3-task":
        prompt = ("DVS Task 1.3: Review my seven universal design reflection paragraphs. Write in English. "
            "Required: your own Word document with one brief applied paragraph per principle, considering future visualisations and their web/mobile/print platforms. "
            "Check concrete changes, reasons, evaluation plans and source links. Flag placeholders and missing principles. "
            "Keep Noroff order and distinguish the NC State numbering. Do not invent source claims, completed tests or compliance certification.\n\nMy reflections and research notes:\n" + get_dvs_draft(guide["uid"]))
    elif guide["id"] == "1.4-task":
        prompt = ("DVS Task 1.4: Review my three applied reflections. Write in English. "
            "Required: your own Word document with Inclusive Design, Usability and Accessibility headings and one brief paragraph under each, considering future visualisations and their web/mobile/printed platforms. "
            "Check concrete adaptations, reasons, evaluation plans and source links. Flag placeholders and missing concepts. "
            "POUR supports accessibility reasoning; it does not replace the three task headings. Do not invent source claims, completed tests or WCAG conformance.\n\nMy reflections and research notes:\n" + get_dvs_draft(guide["uid"]))
    elif guide["lesson_number"] in {"1.3", "1.4"}:
        prompt = f"DVS Activity {guide['id']}: {guide['title']}. Write in English. Required output: {guide['deliverable']}. Steps: {'; '.join(guide['steps'])}. {guide['caution']} Follow this activity's stated requirements."
    else:
        prompt = "DVS Activity 1.1.1: Help me draft a clearly labelled hypothetical athlete persona for Funky Monkey, a statement-sock brand seeking recognition among men and women aged 25–35 who participate in mountain biking, triathlons or marathons. Write in English. Keep this brief separate from the CEO task."
    st.session_state[f"{resolver_base}_prompt"] = prompt
    st.session_state[f"{resolver_base}_source_pool"] = "Lessons + learning outcomes"
    st.session_state[f"{resolver_base}_scope"] = "Whole course (auto-select best matches)"
    st.session_state["nav_section"] = "Learning"
    st.session_state["nav_page"] = "Learn & Practice"
    st.session_state["last_selected_course"] = "Data Visualisation"
    st.session_state["lp_selected_course"] = f"{COURSE_CODE} - Data Visualisation"


def render_dvs_images(base_key, illustrations=None):
    for index, visual in enumerate(ILLUSTRATIONS if illustrations is None else illustrations):
        path = ASSET_ROOT / visual["file"]
        if path.is_file():
            with st.expander(f"Visual study guide — {visual['title']}", expanded=index == 0):
                st.image(str(path), caption=visual["caption"], width="stretch")
                st.markdown(f"**Read the illustration:** {visual['caption']}")
                st.download_button("Download DVS illustration (PNG)", path.read_bytes(), file_name=path.name,
                    mime="image/png", key=f"{base_key}_image_{index}")


def render_dvs_task_resources(guides, base_key, heading=None, draft_editor=False, show_images=True):
    if heading is None:
        heading = "### 2. Task guide and templates" if any(g["lesson_number"] != "1.1" for g in guides) else "### 2. Task guide and persona template"
    st.markdown(heading)
    for guide in guides:
        with st.container(border=True):
            st.markdown(f"**{guide['id']} · {guide['title']}**")
            st.markdown(f"**Deliverable:** {guide['deliverable']}")
            st.markdown(f"[Open the original {'task' if guide['id'].endswith('-task') else 'activity'} on Noroff]({guide['source_url']})")
            if guide["id"] == "1.1-task":
                st.info("Supplied facts: CEO of an extreme-sports start-up; early twenties; enjoys BASE jumping. Additional characteristics must be labelled hypothetical.")
                step = st.selectbox("Choose a Task 1.1 step", list(range(len(TASK_STEPS))),
                    format_func=lambda i: TASK_STEPS[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
                st.markdown(f"**{TASK_STEPS[step][0]}**")
                st.markdown(TASK_STEPS[step][1])
                st.caption(f"Check: {TASK_STEPS[step][2]}")
                with st.expander("Persona fields and writing patterns", expanded=False):
                    st.markdown("**Fields:** fictional identity; supplied facts; hypothetical goals; information needs; potential pain points; presentation needs; assumptions and questions to validate.")
                    st.markdown("**User story:** As a [user], I want to [goal], so that [benefit].\n\n**Problem statement:** [User] needs a way to [need] because [insight].")
                st.download_button("Download persona template (Markdown)", get_dvs_persona_template().encode(),
                    file_name="DVS Task 1.1 Persona Template.md", mime="text/markdown", key=f"{base_key}_persona_md_{guide['uid']}")
                template = TEMPLATE_ROOT / guide["template_file"]
                if template.is_file():
                    st.download_button("Download persona template (Word)", template.read_bytes(), file_name=template.name,
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_persona_docx_{guide['uid']}")
                if draft_editor:
                    with st.expander("Write your Task 1.1 persona", expanded=False):
                        widget_key = f"{base_key}_persona_editor_{guide['uid']}"
                        st.text_area("Your Task 1.1 persona draft", value=get_dvs_draft(guide["uid"]), height=380,
                            key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
                        st.caption("Your draft is kept during this session. Prepare the task below to copy it into Exam Resolver for review.")
                else:
                    st.caption("Paste your completed persona into the question above to request a review, or prepare it from Lesson 1.1.")
            elif guide["lesson_number"] == "2.4":
                render_image_editing_resources(guide, base_key, draft_editor)
            elif guide["id"] == "2.3-task":
                render_graphics_resources(guide, base_key, draft_editor)
            elif guide["id"] == "2.2-task":
                render_ethics_resources(guide, base_key, draft_editor)
            elif guide["id"] == "2.1-task":
                render_ux_review_resources(guide, base_key, draft_editor)
            elif guide["id"] == "1.2-task":
                render_wireframe_resources(guide, base_key, draft_editor)
            elif guide["id"] in {"1.3-task", "1.4-task"}:
                render_reflection_resources(guide, base_key, draft_editor)
            else:
                st.markdown("\n".join(f"{i}. {step}." for i, step in enumerate(guide["steps"], 1)))
                st.info(guide["caution"])
                if guide["lesson_number"] == "1.4":
                    render_activity14_template(guide, base_key)
            label = "Full task guide" if draft_editor else "Resolver task"
            with st.expander(f"{label} {guide['id']}: {guide['title']}", expanded=False):
                markdown = dvs_curriculum.get_dvs_task_guide_markdown(guide)
                st.markdown(markdown)
                st.download_button("Download DVS task guide (Markdown)", markdown.encode(),
                    file_name=f"DVS-{guide['id']}-guide.md", mime="text/markdown", key=f"{base_key}_guide_{guide['uid']}")
    if show_images:
        with st.expander("Illustrations for this task", expanded=False):
            visuals = []
            if any(g["lesson_number"] == "1.1" for g in guides):
                visuals.extend(ILLUSTRATIONS)
            if any(g["lesson_number"] == "1.2" for g in guides):
                from dvs_lesson12 import ILLUSTRATIONS as images12
                visuals.extend(images12)
            if any(g["lesson_number"] == "1.3" for g in guides):
                from dvs_lesson13 import ILLUSTRATIONS as images13
                visuals.extend(images13)
            if any(g["lesson_number"] == "1.4" for g in guides):
                from dvs_lesson14 import ILLUSTRATIONS as images14
                visuals.extend(images14)
            if any(g["lesson_number"] == "2.1" for g in guides):
                from dvs_lesson21 import ILLUSTRATIONS as images21
                visuals.extend(images21)
            if any(g["lesson_number"] == "2.2" for g in guides):
                from dvs_lesson22 import ILLUSTRATIONS as images22
                visuals.extend(images22)
            if any(g["lesson_number"] == "2.3" for g in guides):
                from dvs_lesson23 import ILLUSTRATIONS as images23
                visuals.extend(images23)
            if any(g["lesson_number"] == "2.4" for g in guides):
                from dvs_lesson24 import ILLUSTRATIONS as images24
                visuals.extend(images24)
            render_dvs_images(f"{base_key}_resolver", visuals)


def render_wireframe_resources(guide, base_key, draft_editor):
    from dvs_lesson12 import TASK_STEPS as steps, WIREFRAME_TEMPLATE, TEST_TEMPLATE
    st.info("Required sketch: height, weight, age, submission, other users' chart, your highlighted BMI, chart selection and an age filter.")
    step = st.selectbox("Choose a Task 1.2 step", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Wireframe requirements and writing patterns", expanded=False):
        st.markdown("**Input area:** labelled units, height, weight, age, submission and validation.\n\n**Results area:** your BMI, labelled marker, other users, chart choice, age filtering and an edit route.\n\n**Explanation:** audience need → layout/control → reason → question to test.")
        st.caption("The sketch communicates layout and behaviour. It does not need working calculations or real health data.")
    for label, content, filename in [
        ("Download wireframe plan (Markdown)", WIREFRAME_TEMPLATE, "DVS Task 1.2 Wireframe Plan.md"),
        ("Download usability test plan (Markdown)", TEST_TEMPLATE, "DVS Task 1.2 Usability Test Plan.md")]:
        st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")
    template = TEMPLATE_ROOT / guide["template_file"]
    if template.is_file():
        st.download_button("Download wireframe and test plan (Word)", template.read_bytes(), file_name=template.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_wireframe_docx")
    if draft_editor:
        with st.expander("Write your Task 1.2 wireframe plan", expanded=False):
            widget_key = f"{base_key}_wireframe_editor_{guide['uid']}"
            st.text_area("Your Task 1.2 wireframe and test plan", value=get_dvs_draft(guide["uid"]), height=380,
                key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
            st.caption("Your plan is kept during this session. Describe the layout and controls in words, then prepare the task to copy the plan into Exam Resolver.")
    else:
        st.caption("Paste your plan above or prepare it from Lesson 1.2. The resolver reviews your written plan; describe the sketch layout and controls in words.")


def render_activity14_template(guide, base_key):
    from dvs_lesson14 import CONTRAST_TEMPLATE, LANGUAGE_TEMPLATE
    if guide["id"] == "1.4.1":
        label, content, filename = "Download contrast check log (Markdown)", CONTRAST_TEMPLATE, "DVS Activity 1.4.1 Contrast Check Log.md"
    else:
        label, content, filename = "Download language selector plan (Markdown)", LANGUAGE_TEMPLATE, "DVS Activity 1.4.2 Language Selector Plan.md"
    st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")


def render_reflection_resources(guide, base_key, draft_editor):
    number = guide["lesson_number"]
    if number == "1.4":
        from dvs_lesson14 import TASK_STEPS as steps, REFLECTION_TEMPLATE, RESEARCH_TEMPLATE, SOURCES
        focus = "concept"
        brief = "Required: research Inclusive Design, Usability and Accessibility and write one brief applied paragraph under each heading in your own Word document. Include the visual and its host platform."
        pattern = "context → proposed change → reason → evaluation → source"
        word_label = "Download three-concept template (Word)"
        source_note = "The course refers to WCAG 2.1; WCAG 2.2 is a supplementary reference. POUR supports the accessibility reflection rather than replacing the three required concepts."
    else:
        from dvs_lesson13 import TASK_STEPS as steps, REFLECTION_TEMPLATE, RESEARCH_TEMPLATE, SOURCES
        focus = "principle"
        brief = "Required: research universal design and write one brief applied paragraph for each of the seven principles in your own Word document. Include the visual and its host platform."
        pattern = "principle → user need → change → reason → check"
        word_label = "Download seven-principle template (Word)"
        source_note = "Steps follow Noroff order. NC State places Tolerance for Error fifth and Low Physical Effort sixth. Complete all seven paragraphs, regardless of order."
    st.info(brief)
    step = st.selectbox(f"Choose a Task {number} {focus}", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Reflection pattern and research sources", expanded=False):
        st.markdown(f"**Pattern:** {pattern}.\n\n**Sentence scaffold:** For [audience/context], I would [change] because [reason]. I would check this by [method]. Source for a researched claim: [...].")
        st.markdown("\n\n".join(f"[{name}]({url})" for name, url in SOURCES))
        st.caption(source_note)
    for label, content, filename in [
        ("Download reflection template (Markdown)", REFLECTION_TEMPLATE, f"DVS Task {number} Reflection Template.md"),
        ("Download research notes (Markdown)", RESEARCH_TEMPLATE, f"DVS Task {number} Research Notes.md")]:
        st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")
    template = TEMPLATE_ROOT / guide["template_file"]
    if template.is_file():
        st.download_button(word_label, template.read_bytes(), file_name=template.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_reflection_docx_{guide['uid']}")
    if draft_editor:
        with st.expander(f"Write your Task {number} reflections", expanded=False):
            widget_key = f"{base_key}_reflection_editor_{guide['uid']}"
            st.text_area(f"Your Task {number} reflections and research notes", value=get_dvs_draft(guide['uid']), height=380,
                key=widget_key, on_change=remember_draft, args=(guide['uid'], widget_key))
            st.caption(f"Your draft is kept during this session. Prepare the task to copy the reflections and selected {focus} into Exam Resolver. Save your final paragraphs in your own Word document.")
    else:
        st.caption(f"Paste your reflections above or prepare them from Lesson {number}. The resolver reviews the written paragraphs and source notes; proposed checks are not completed tests.")


def render_dvs_lesson_resources(lesson, context):
    if lesson.get("course_code") != COURSE_CODE:
        return
    from dvs_curriculum import get_dvs_task_guides
    base_key = f"dvs_lesson_{context}_{lesson['lesson_number']}"
    render_dvs_images(base_key, lesson.get("dvs_illustrations"))
    guides = get_dvs_task_guides(lesson["lesson_number"])
    selected = st.selectbox(f"Choose a DVS Lesson {lesson['lesson_number']} activity or task", [g["uid"] for g in guides],
        format_func=lambda uid: next(f"{g['id']} — {g['title']}" for g in guides if g["uid"] == uid),
        key=f"{base_key}_task")
    guide = next(g for g in guides if g["uid"] == selected)
    render_dvs_task_resources([guide], base_key, heading=f"#### Task walkthrough — DVS Lesson {lesson['lesson_number']}", draft_editor=True, show_images=False)
    label = f"Prepare Task {guide['lesson_number']} in Exam Resolver" if guide["id"].endswith('-task') else f"Prepare Activity {guide['id']} in Exam Resolver"
    st.button(label, key=f"{base_key}_prepare", on_click=prepare_task_in_resolver, args=(guide, base_key))
    st.markdown("[Go to Exam Resolver](#semester-exam-connector)")


def render_ux_review_resources(guide, base_key, draft_editor):
    from dvs_lesson21 import TASK_STEPS as steps, REPORT_TEMPLATE, APPLICATION_TEMPLATE, EVIDENCE_TEMPLATE, REDIRECT_NOTE
    st.info(guide["deliverable"])
    step = st.selectbox("Choose a Task 2.1 step", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Website evidence and current redirects", expanded=False):
        st.markdown(REDIRECT_NOTE)
        st.markdown("**Report pattern:** observation → UX reason → user impact → improvement or check.\n\n**Application pattern:** concept → design choice → user benefit → evaluation.")
        st.caption("The resolver reviews your supplied evidence and written reasoning. Inspect the sites yourself and verify final formatting and page lengths in Word.")
    for label, content, filename in [
        ("Download website review template (Markdown)", REPORT_TEMPLATE, "DVS Task 2.1 Website Review.md"),
        ("Download UX application template (Markdown)", APPLICATION_TEMPLATE, "DVS Task 2.1 UX Application.md"),
        ("Download website evidence log (Markdown)", EVIDENCE_TEMPLATE, "DVS Task 2.1 Evidence Log.md")]:
        st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")
    path = TEMPLATE_ROOT / guide["template_file"]
    if path.is_file():
        st.download_button("Download website review and UX template (Word)", path.read_bytes(), file_name=path.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_ux_docx_{guide['uid']}")
    if draft_editor:
        with st.expander("Write your Task 2.1 answers and evidence", expanded=False):
            widget_key = f"{base_key}_ux_editor_{guide['uid']}"
            st.text_area("Your Task 2.1 report UX application and evidence", value=get_dvs_draft(guide["uid"]), height=420,
                key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
            st.caption("Your draft is kept during this session. Prepare the task to copy it and the selected step into Exam Resolver. Save the final answers in your own Word document.")
    else:
        st.caption("Paste both answers and evidence above, or prepare them from Lesson 2.1. The resolver cannot establish unobserved website behaviour or final Word pagination.")


def render_ethics_resources(guide, base_key, draft_editor):
    from dvs_lesson22 import TASK_STEPS as steps, ANALYSIS_TEMPLATE, RULES_TEMPLATE, REVIEW_TEMPLATE, FIGURE_NOTES, RULES
    step = st.selectbox("Choose a Task 2.2 step", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Screenshot evidence and limits", expanded=False):
        st.markdown(FIGURE_NOTES)
        st.caption("Inspect the original graphs on Noroff. The resolver reviews your written evidence; it does not inspect uploaded pixels or independently verify the original data.")
    with st.expander("Four course rules and writing pattern", expanded=False):
        for name, meaning, action, caution in RULES:
            st.markdown(f"**{name}:** {meaning} {action}")
            st.caption(caution)
        st.markdown("**Graph analysis:** observation → misleading effect → correction → limitation.\n\n**Rule application:** meaning → my view → workflow action → evidence/check.")
    for label, content, filename in [
        ("Download graph analysis template (Markdown)", ANALYSIS_TEMPLATE, "DVS Task 2.2 Graph Analysis.md"),
        ("Download four rules template (Markdown)", RULES_TEMPLATE, "DVS Task 2.2 Four Rules.md"),
        ("Download chart and peer review log (Markdown)", REVIEW_TEMPLATE, "DVS Task 2.2 Chart and Peer Review Log.md")]:
        st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")
    path = TEMPLATE_ROOT / guide["template_file"]
    if path.is_file():
        st.download_button("Download graph analysis and four rules template (Word)", path.read_bytes(), file_name=path.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_ethics_docx_{guide['uid']}")
    st.caption("Word is an optional study scaffold. The task brief specifies no page count or font requirement.")
    if draft_editor:
        with st.expander("Write your Task 2.2 analysis and rule applications", expanded=False):
            widget_key = f"{base_key}_ethics_editor_{guide['uid']}"
            st.text_area("Your Task 2.2 graph analysis rules and review notes", value=get_dvs_draft(guide["uid"]), height=420,
                key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
            st.caption("Your draft is kept during this session. Prepare the task to copy it and the selected step into Exam Resolver.")
    else:
        st.caption("Paste both answers and evidence above, or prepare them from Lesson 2.2. State all four rules with your own view and application.")


def render_graphics_resources(guide, base_key, draft_editor):
    from dvs_lesson23 import TASK_STEPS as steps, STUDY_TEMPLATE, COMPARISON_TEMPLATE, SETUP_TEMPLATE, RESEARCH_NOTES, COMPARISON_EXAMPLE
    step = st.selectbox("Choose a Task 2.3 question", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Question 7 software research and dated prices", expanded=False):
        st.markdown(RESEARCH_NOTES)
        st.markdown(COMPARISON_EXAMPLE)
    with st.expander("GIMP orientation and format checks", expanded=False):
        st.markdown("Find the image window/menu, toolbox, tool options, brushes/patterns/gradients and layers. Save an editable XCF project and export a sharing image. Layout varies by version.\n\nRaster/vector describe representation; a vector document can embed a bitmap, and rasterising it creates pixels.")
        st.caption("The setup log is optional lesson practice. The seven-question task does not require a GIMP project submission or a particular font/page count.")
    for label, content, filename in [
        ("Download graphics study worksheet (Markdown)", STUDY_TEMPLATE, "DVS Task 2.3 Graphics Study Worksheet.md"),
        ("Download software comparison template (Markdown)", COMPARISON_TEMPLATE, "DVS Task 2.3 Software Comparison.md"),
        ("Download GIMP orientation log (Markdown)", SETUP_TEMPLATE, "DVS Lesson 2.3 GIMP Orientation Log.md")]:
        st.download_button(label, content.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_{filename}")
    path = TEMPLATE_ROOT / guide["template_file"]
    if path.is_file():
        st.download_button("Download graphics and software comparison template (Word)", path.read_bytes(), file_name=path.name,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_graphics_docx_{guide['uid']}")
    st.caption("Templates help you study and draft Question 7; they do not submit or grade the Noroff H5P activity.")
    if draft_editor:
        with st.expander("Write your Task 2.3 study answers and comparison", expanded=False):
            widget_key = f"{base_key}_graphics_editor_{guide['uid']}"
            st.text_area("Your Task 2.3 study answers and software comparison", value=get_dvs_draft(guide["uid"]), height=420,
                key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
            st.caption("Your notes are kept during this session. Prepare the task to copy them and the selected question step into Exam Resolver.")
    else:
        st.caption("Paste your notes above or prepare them from Lesson 2.3. The resolver reviews your text and supplied evidence; recheck live prices and actual software behaviour yourself.")



def render_image_editing_resources(guide, base_key, draft_editor):
    from dvs_lesson24 import (TASK_STEPS as steps24, ACTIVITY_STEPS, TASK_TEMPLATE,
        ACTIVITY_TEMPLATES, EVIDENCE_TEMPLATE, ASSETS, FILE_NOTE, CHART_NOTE, VERSION_NOTES)
    is_task = guide["id"] == "2.4-task"
    kind = "Task 2.4" if is_task else f"Activity {guide['id']}"
    steps = steps24 if is_task else ACTIVITY_STEPS[guide["id"]]
    step = st.selectbox(f"Choose a {kind} step" if is_task else f"Choose an {kind} step", list(range(len(steps))),
        format_func=lambda i: steps[i][0], key=f"{base_key}_dvs_step_{guide['uid']}")
    st.markdown(f"**{steps[step][0]}**")
    st.markdown(steps[step][1])
    st.caption(f"Check: {steps[step][2]}")
    with st.expander("Original images and file names", expanded=False):
        if is_task:
            st.markdown(FILE_NOTE)
        else:
            st.caption("Open the activity’s original image link while signed in to Noroff; keep a fresh source copy for each operation.")
        if is_task:
            source_files = ASSETS[:4]
        elif guide["id"] == "2.4.2":
            source_files = [ASSETS[5]]
        elif guide["id"] == "2.4.4":
            source_files = []
            st.markdown("Create a new project and the text Data Analyst. No supplied photograph is required for this activity.")
        else:
            source_files = [ASSETS[4]]
        for name,url in source_files:
            st.markdown(f"[{name}]({url})")
    if is_task:
        with st.expander("Strawberry chart meaning and design options", expanded=False):
            st.markdown(CHART_NOTE)
            st.markdown("One optional composition uses a strawberry photograph beside readable quarter labels and a short ordering summary. Your own design is allowed. Keep image decoration separate from quantitative encodings.")
    with st.expander("GIMP commands and version notes", expanded=False):
        st.markdown(VERSION_NOTES)
    template = TASK_TEMPLATE if is_task else ACTIVITY_TEMPLATES[guide["uid"]]
    label = "Download three image design worksheet (Markdown)" if is_task else f"Download Activity {guide['id']} worksheet (Markdown)"
    filename = "DVS Task 2.4 Three Image Designs.md" if is_task else f"DVS Activity {guide['id']} Worksheet.md"
    st.download_button(label, template.encode(), file_name=filename, mime="text/markdown", key=f"{base_key}_editing_md_{guide['uid']}")
    st.download_button("Download editing and export log (Markdown)", EVIDENCE_TEMPLATE.encode(),
        file_name="DVS Lesson 2.4 Editing and Export Log.md", mime="text/markdown", key=f"{base_key}_editing_log_{guide['uid']}")
    if is_task:
        path = TEMPLATE_ROOT / guide["template_file"]
        if path.is_file():
            st.download_button("Download GIMP image design worksheet (Word)", path.read_bytes(), file_name=path.name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"{base_key}_editing_docx_{guide['uid']}")
    st.caption("The images are the task output. Templates and file/log suggestions are optional study scaffolds; the brief specifies no font/page count or export format.")
    if draft_editor:
        with st.expander(f"Write your {kind} editing plan and checks", expanded=False):
            widget_key = f"{base_key}_editing_editor_{guide['uid']}"
            st.text_area(f"Your {kind} editing plan and check notes", value=get_dvs_draft(guide["uid"]), height=420,
                key=widget_key, on_change=remember_draft, args=(guide["uid"], widget_key))
            st.caption("Prepare copies your notes and selected step into Exam Resolver. Record only checks you actually performed.")
    else:
        st.caption("The resolver reviews written notes and descriptions. Check actual pixels, masks, layer settings and reopened exports in GIMP yourself.")



def get_image_editing_step_context(guide, base_key):
    """Use the current resolver selection, including changes after handoff."""
    from dvs_lesson24 import TASK_STEPS as steps24, ACTIVITY_STEPS
    steps = steps24 if guide["id"] == "2.4-task" else ACTIVITY_STEPS[guide["id"]]
    index = st.session_state.get(f"{base_key}_dvs_step_{guide['uid']}", 0)
    if not isinstance(index, int) or not 0 <= index < len(steps):
        index = 0
    title, instruction, caution = steps[index]
    return f"Current selected step: {title}\nFocus: {instruction}\nCheck: {caution}\nThis current selector state takes precedence over an earlier step mentioned in the written notes.\n\n"
