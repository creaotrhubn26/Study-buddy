"""Shared English DVS task flow for Lessons and Universal Exam Resolver."""

import streamlit as st
from dvs_curriculum import (ASSET_ROOT, TEMPLATE_ROOT, COURSE_CODE, ILLUSTRATIONS,
    TASK_STEPS, get_dvs_persona_template, get_dvs_task_guide_markdown)

CONTENT_REVISION = "2026-10-14-dvs11"


def get_dvs_draft(uid):
    return st.session_state.get("dvs_persona_drafts", {}).get(uid, get_dvs_persona_template())


def remember_draft(uid, widget_key):
    drafts = dict(st.session_state.get("dvs_persona_drafts", {}))
    drafts[uid] = st.session_state[widget_key]
    st.session_state["dvs_persona_drafts"] = drafts


def prepare_task_in_resolver(guide, lesson_base):
    resolver_base = "course_exam_connector_fi1bbdv75_learn_practice"
    step = st.session_state.get(f"{lesson_base}_dvs_step_{guide['uid']}", 0)
    st.session_state[f"{resolver_base}_dvs_step_{guide['uid']}"] = step
    if guide["id"] == "1.1-task":
        prompt = ("DVS Task 1.1: Review my hypothetical CEO persona for the snow-free bobsled market-analysis presentation. "
            "Write in English. Supplied facts: CEO of an extreme-sports start-up, early twenties, enjoys BASE jumping. "
            "Treat additional characteristics as hypothetical assumptions. Flag unfilled placeholders. "
            "Do not invent real interviews, market findings or known personal preferences.\n\nMy persona draft:\n" + get_dvs_draft(guide["uid"]))
    else:
        prompt = "DVS Activity 1.1.1: Help me draft a clearly labelled hypothetical athlete persona for Funky Monkey, a statement-sock brand seeking recognition among men and women aged 25–35 who participate in mountain biking, triathlons or marathons. Write in English. Keep this brief separate from the CEO task."
    st.session_state[f"{resolver_base}_prompt"] = prompt
    st.session_state[f"{resolver_base}_source_pool"] = "Lessons + learning outcomes"
    st.session_state[f"{resolver_base}_scope"] = "Whole course (auto-select best matches)"
    st.session_state["nav_section"] = "Learning"
    st.session_state["nav_page"] = "Learn & Practice"
    st.session_state["last_selected_course"] = "Data Visualisation"
    st.session_state["lp_selected_course"] = f"{COURSE_CODE} - Data Visualisation"


def render_dvs_images(base_key):
    for index, visual in enumerate(ILLUSTRATIONS):
        path = ASSET_ROOT / visual["file"]
        if path.is_file():
            with st.expander(f"Visual study guide — {visual['title']}", expanded=index == 0):
                st.image(str(path), caption=visual["caption"], width="stretch")
                st.markdown(f"**Read the illustration:** {visual['caption']}")
                st.download_button("Download DVS illustration (PNG)", path.read_bytes(), file_name=path.name,
                    mime="image/png", key=f"{base_key}_image_{index}")


def render_dvs_task_resources(guides, base_key, heading="### 2. Task guide and persona template", draft_editor=False, show_images=True):
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
            else:
                st.markdown("\n".join(f"{i}. {step}." for i, step in enumerate(guide["steps"], 1)))
                st.info(guide["caution"])
            label = "Full task guide" if draft_editor else "Resolver task"
            with st.expander(f"{label} {guide['id']}: {guide['title']}", expanded=False):
                markdown = get_dvs_task_guide_markdown(guide)
                st.markdown(markdown)
                st.download_button("Download DVS task guide (Markdown)", markdown.encode(),
                    file_name=f"DVS-{guide['id']}-guide.md", mime="text/markdown", key=f"{base_key}_guide_{guide['uid']}")
    if show_images:
        with st.expander("Illustrations for this task", expanded=False):
            render_dvs_images(f"{base_key}_resolver")


def render_dvs_lesson_resources(lesson, context):
    if lesson.get("course_code") != COURSE_CODE:
        return
    from dvs_curriculum import get_dvs_task_guides
    base_key = f"dvs_lesson_{context}_{lesson['lesson_number']}"
    render_dvs_images(base_key)
    guides = get_dvs_task_guides(lesson["lesson_number"])
    selected = st.selectbox("Choose a DVS Lesson 1.1 activity or task", [g["uid"] for g in guides],
        format_func=lambda uid: next(f"{g['id']} — {g['title']}" for g in guides if g["uid"] == uid),
        key=f"{base_key}_task")
    guide = next(g for g in guides if g["uid"] == selected)
    render_dvs_task_resources([guide], base_key, heading="#### Task walkthrough — DVS Lesson 1.1", draft_editor=True, show_images=False)
    label = "Prepare Task 1.1 in Exam Resolver" if guide["id"] == "1.1-task" else "Prepare Activity 1.1.1 in Exam Resolver"
    st.button(label, key=f"{base_key}_prepare", on_click=prepare_task_in_resolver, args=(guide, base_key))
    st.markdown("[Go to Exam Resolver](#semester-exam-connector)")
