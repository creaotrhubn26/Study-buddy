"""Lesson resources and the real ARP lesson to Exam Resolver handoff."""

import json
import streamlit as st
import arp_curriculum as curriculum

RESOLVER_BASE = "course_exam_connector_fi1bbar05_learn_practice"
UID = curriculum.GUIDE["uid"]


def draft(state):
    return state.get("arp_task_drafts", {}).get(UID, curriculum.QUESTION_TEMPLATE)


def remember_draft(widget_key):
    saved = dict(st.session_state.get("arp_task_drafts", {}))
    saved[UID] = st.session_state[widget_key]
    st.session_state["arp_task_drafts"] = saved


def remember_step(widget_key):
    saved = dict(st.session_state.get("arp_task_steps", {}))
    saved[UID] = st.session_state[widget_key]
    st.session_state["arp_task_steps"] = saved


def workflow_signature(state, base_key=RESOLVER_BASE):
    return json.dumps(
        {
            "step": state.get("arp_task_steps", {}).get(UID, 0),
            "specific": state.get(f"{base_key}_specific_source", ""),
            "manual": state.get(f"{base_key}_selected_sources", []),
            "draft": draft(state),
            "pool": state.get(f"{base_key}_source_pool", "Lessons + learning outcomes"),
            "scope": state.get(
                f"{base_key}_scope", "Whole course (auto-select best matches)"
            ),
        },
        sort_keys=True,
    )


def step_context(guide, base_key, state):
    index = state.get("arp_task_steps", {}).get(guide["uid"], 0)
    if not isinstance(index, int) or not 0 <= index < len(curriculum.STEPS):
        index = 0
    title, instruction, check = curriculum.STEPS[index]
    return (
        f"ARP Task 1.1 current selected step: {title}\n{instruction}\nCheck: {check}\n"
        + curriculum.BOUNDARY
        + "\nStudent question-plan draft:\n"
        + draft(state)[:7000]
        + "\n\n"
    )


def prepare_task_in_resolver():
    st.session_state[f"{RESOLVER_BASE}_prompt"] = (
        "ARP Task 1.1: Review my report-question plan in English. "
        + curriculum.BOUNDARY
        + " Check the general-to-specific order, all three platforms, six-month scope, posting schedule and content type. "
        "Flag placeholders and missing definitions. Explain the currently selected step and suggest neutral questions. "
        "Do not write an invented findings report, require paid-ad ROI, or claim to inspect platform analytics or submit work.\n\nMy draft:\n"
        + draft(st.session_state)
    )
    st.session_state[f"{RESOLVER_BASE}_source_pool"] = "Lessons + task guides"
    st.session_state[f"{RESOLVER_BASE}_scope"] = (
        "Whole course (auto-select best matches)"
    )
    st.session_state["nav_section"] = "Learning"
    st.session_state["nav_page"] = "Learn & Practice"
    st.session_state["lp_selected_course"] = (
        f"{curriculum.COURSE_CODE} - {curriculum.COURSE_NAME}"
    )
    st.session_state["last_selected_course"] = curriculum.COURSE_NAME


def render_images(base_key):
    for index, visual in enumerate(curriculum.ILLUSTRATIONS):
        with st.expander("Visual study guide — " + visual["title"], expanded=False):
            path = curriculum.ASSET_ROOT / visual["file"]
            if not path.is_file():
                st.warning(
                    "This illustration is unavailable. Use the explanation below."
                )
            else:
                st.image(str(path), caption=visual["caption"], width="stretch")
                st.download_button(
                    "Download ARP illustration (PNG)",
                    path.read_bytes(),
                    file_name=path.name,
                    mime="image/png",
                    key=f"{base_key}_arp_image_{index}",
                )
            st.write(visual["caption"])
            st.caption(
                "AI-generated educational illustration made with OpenAI imagegen. No measured engagement results are depicted."
            )


def render_task_resources(
    guides, base_key, heading="### 2. Task guide and templates", show_images=True
):
    st.markdown(heading)
    st.markdown("**Task 1.1 · " + curriculum.GUIDE["title"] + "**")
    st.info(
        "Deliverable: an ordered set of report questions. No dataset or measured engagement findings are supplied."
    )
    st.markdown(f"[Open the original task on Noroff]({curriculum.TASK_URL})")
    current = st.session_state.get("arp_task_steps", {}).get(UID, 0)
    current = (
        current
        if isinstance(current, int) and 0 <= current < len(curriculum.STEPS)
        else 0
    )
    step_key = f"{base_key}_arp_step_{UID}"
    if step_key in st.session_state and st.session_state[step_key] != current:
        st.session_state[step_key] = current
    step = st.selectbox(
        "Choose a Task 1.1 step",
        list(range(len(curriculum.STEPS))),
        index=current,
        format_func=lambda i: curriculum.STEPS[i][0],
        key=step_key,
        on_change=remember_step,
        args=(step_key,),
    )
    title, instruction, check = curriculum.STEPS[step]
    st.markdown("**" + title + "**")
    st.write(instruction)
    st.caption("Check: " + check)
    with st.expander("Example questions from general to specific", expanded=False):
        st.caption(
            "Original Study Buddy examples to adapt, not the downloaded official solution. The number of questions is a suggestion, not a task requirement."
        )
        for title, questions in curriculum.QUESTION_GROUPS:
            st.markdown("#### " + title)
            for question in questions:
                st.markdown("- " + question)
    for name, label, mime in [
        (
            "ARP Task 1.1 Report Question Plan.md",
            "Download question plan (Markdown)",
            "text/markdown",
        ),
        (
            "ARP Task 1.1 Evidence Matrix.csv",
            "Download question evidence matrix (CSV)",
            "text/csv",
        ),
        (
            "ARP Lesson 1.1 Optional Report Outline.md",
            "Download optional report outline (Markdown)",
            "text/markdown",
        ),
    ]:
        path = curriculum.TEMPLATE_ROOT / name
        if path.is_file():
            st.download_button(
                label,
                path.read_bytes(),
                file_name=name,
                mime=mime,
                key=f"{base_key}_arp_{name}",
            )
        else:
            st.warning("Template unavailable: " + name)
    st.caption(
        "The report outline is optional lesson practice. Task 1.1 asks for questions; it does not prescribe a completed report, page count or file format."
    )
    with st.expander("Write your Task 1.1 question plan", expanded=False):
        editor_key = f"{base_key}_arp_draft_{UID}"
        if editor_key in st.session_state and st.session_state[editor_key] != draft(
            st.session_state
        ):
            st.session_state[editor_key] = draft(st.session_state)
        st.text_area(
            "Your report questions and evidence plan",
            value=draft(st.session_state),
            height=260,
            key=editor_key,
            on_change=remember_draft,
            args=(editor_key,),
        )
        st.caption(
            "Apply edits with Ctrl+Enter or by leaving the field. Your draft is saved with Study Buddy state on this app instance; download a copy to keep your work."
        )
        st.download_button(
            "Download my Task 1.1 draft",
            draft(st.session_state).encode(),
            file_name="My ARP Task 1.1 question plan.md",
            mime="text/markdown",
            key=f"{base_key}_arp_my_draft",
        )
    with st.expander("Full Task 1.1 guide and checklist", expanded=False):
        st.markdown(curriculum.guide_markdown())
    if show_images:
        render_images(base_key)


def render_lesson_resources(lesson, context):
    if lesson.get("course_code") != curriculum.COURSE_CODE:
        return
    base_key = f"arp_{context}_{lesson['lesson_number']}"
    render_images(base_key)
    with st.expander("Task 1.1 walkthrough and templates", expanded=False):
        render_task_resources(
            curriculum.get_task_guides("1.1"),
            base_key,
            heading="### Task 1.1 — seven steps",
            show_images=False,
        )
        st.button(
            "Prepare Task 1.1 in Exam Resolver",
            key=f"{base_key}_prepare",
            on_click=prepare_task_in_resolver,
        )
        st.caption(
            "Transfers your applied draft and selected step. Generate a review in Exam Resolver when you are ready; no Noroff task is submitted."
        )
