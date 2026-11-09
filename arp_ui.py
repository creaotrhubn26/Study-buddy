"""Lesson resources and the real ARP lesson to Exam Resolver handoff."""

import json
import streamlit as st
import arp_curriculum as curriculum

RESOLVER_BASE = "course_exam_connector_fi1bbar05_learn_practice"
UID = curriculum.GUIDE["uid"]


def draft(state, guide=None):
    guide = guide or curriculum.GUIDE
    return state.get("arp_task_drafts", {}).get(
        guide["uid"], curriculum.task_material(guide).QUESTION_TEMPLATE
    )


def remember_draft(widget_key, uid=UID):
    saved = dict(st.session_state.get("arp_task_drafts", {}))
    saved[uid] = st.session_state[widget_key]
    st.session_state["arp_task_drafts"] = saved


def remember_step(widget_key, uid=UID):
    saved = dict(st.session_state.get("arp_task_steps", {}))
    saved[uid] = st.session_state[widget_key]
    st.session_state["arp_task_steps"] = saved


def workflow_signature(state, base_key=RESOLVER_BASE):
    return json.dumps(
        {
            "steps": state.get("arp_task_steps", {}),
            "specific": state.get(f"{base_key}_specific_source", ""),
            "manual": state.get(f"{base_key}_selected_sources", []),
            "drafts": {g["uid"]: draft(state, g) for g in curriculum.all_task_guides()},
            "pool": state.get(f"{base_key}_source_pool", "Lessons + learning outcomes"),
            "scope": state.get(
                f"{base_key}_scope", "Whole course (auto-select best matches)"
            ),
        },
        sort_keys=True,
    )


def step_context(guide, base_key, state):
    material = curriculum.task_material(guide)
    index = state.get("arp_task_steps", {}).get(guide["uid"], 0)
    if not isinstance(index, int) or not 0 <= index < len(material.STEPS):
        index = 0
    title, instruction, check = material.STEPS[index]
    research = ""
    if hasattr(material, "SOURCES"):
        research = "\nOptional research leads (not proof of student reading):\n" + "\n".join(
            f"{source['id']}: {source['reference']} Original: {source['url']} Status: {source['checked']}"
            for source in material.SOURCES
        )
    if hasattr(material, "RESOURCE_LINKS"):
        research += (
            "\nOriginal task resources on Noroff (not native-file verification):\n"
            + "\n".join(f"{label}: {url}" for label, url in material.RESOURCE_LINKS)
        )
    return (
        f"ARP Task {guide['lesson_number']} current selected step: {title}\n{instruction}\nCheck: {check}\n"
        + material.BOUNDARY
        + research
        + "\nStudent draft and check notes:\n"
        + draft(state, guide)[:7000]
        + "\n\n"
    )


def prepare_task_in_resolver(guide=None):
    guide = guide or curriculum.GUIDE
    material = curriculum.task_material(guide)
    request = (
        "Review my Word editing plan and check notes in English. Explain the selected step, "
        "check all five requirements and flag unverified formatting, paragraph ambiguity and Word edition limits. "
        "Do not claim to inspect or modify the DOCX from notes. I will verify the saved Word file and submit it myself."
        if guide["lesson_number"] == "1.2"
        else "Review my report-question plan in English. Check the general-to-specific order, all three platforms, "
        "six-month scope, posting schedule and content type. Flag placeholders and missing definitions. "
        "Explain the currently selected step and suggest neutral questions. Do not invent findings."
    )
    if hasattr(material, "RESOLVER_REQUEST"):
        request = material.RESOLVER_REQUEST
    st.session_state[f"{RESOLVER_BASE}_prompt"] = (
        f"ARP Task {guide['lesson_number']}: "
        + request
        + "\n"
        + material.BOUNDARY
        + "\n\nMy draft:\n"
        + draft(st.session_state, guide)
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


def render_images(base_key, guide=None):
    material = curriculum.task_material(guide)
    for index, visual in enumerate(material.ILLUSTRATIONS):
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
                "AI-generated educational illustration made with OpenAI imagegen. Conceptual study aid, not a software screenshot or evidence of completed work."
            )


def render_task_resources(
    guides, base_key, heading="### 2. Task guide and templates", show_images=True
):
    st.markdown(heading)
    for guide in guides:
        _render_task(guide, base_key + "_" + guide["uid"], show_images)


def _render_task(guide, base_key, show_images):
    material = curriculum.task_material(guide)
    uid, number = guide["uid"], guide["lesson_number"]
    st.markdown(f"**Task {number} · {guide['title']}**")
    st.info("Deliverable: " + guide["deliverable"])
    st.markdown(f"[Open the original task on Noroff]({guide['source_url']})")
    if number == "1.2":
        st.caption(
            "Five required edits, explained in seven learning steps. The Word file must be edited and checked in Word."
        )
    if number == "1.3":
        st.caption(
            "Seven learning steps: research → evidence plan → 500-word overview → Harvard citation checks."
        )
        st.link_button("Find research in Google Scholar", material.SCHOLAR_URL)
    if number == "1.4":
        st.caption(
            "Four questions, explained in seven learning steps. Record actual Office observations separately from expected behaviour."
        )
        with st.expander("Original Task 1.4 files on Noroff", expanded=False):
            st.caption(
                "Sign in to Noroff to download the numbered originals. This app does not host the original course documents or a completed task."
            )
            for label, url in material.RESOURCE_LINKS:
                st.markdown(f"- [{label}]({url})")
    current = st.session_state.get("arp_task_steps", {}).get(uid, 0)
    current = (
        current
        if isinstance(current, int) and 0 <= current < len(material.STEPS)
        else 0
    )
    step_key = f"{base_key}_arp_step_{uid}"
    if step_key in st.session_state and st.session_state[step_key] != current:
        st.session_state[step_key] = current
    step = st.selectbox(
        f"Choose a Task {number} step",
        list(range(len(material.STEPS))),
        index=current,
        format_func=lambda i: material.STEPS[i][0],
        key=step_key,
        on_change=remember_step,
        args=(step_key, uid),
    )
    title, instruction, check = material.STEPS[step]
    st.markdown("**" + title + "**")
    st.write(instruction)
    st.caption("Check: " + check)
    if number == "1.2":
        with st.expander(
            "Five required checks and paragraph interpretation", expanded=False
        ):
            for title, detail in material.CHECKS:
                st.markdown(f"- **{title}:** {detail}")
            st.warning(
                "Second paragraph is ambiguous: headings and blank paragraphs count too. The second substantive body paragraph (Facilisis…) is a working interpretation to confirm if needed."
            )
    elif number == "1.3":
        with st.expander(
            "Suggested 500-word structure and final checks", expanded=False
        ):
            for title, words, purpose in material.PARAGRAPHS:
                st.markdown(f"- **{title} · {words} words:** {purpose}")
            st.caption(
                "Suggested budget only. Confirm what counts toward 500 words; the task states no tolerance."
            )
            for title, detail in material.CHECKS:
                st.markdown(f"- **{title}:** {detail}")
        with st.expander(
            "Harvard examples and optional research leads", expanded=False
        ):
            st.markdown(material.source_cards_markdown())
    elif number == "1.4":
        with st.expander("The four task questions and final checks", expanded=False):
            for title, detail in material.QUESTION_BRIEFS:
                st.markdown(f"**{title}**")
                st.write(detail)
            for title, detail in material.CHECKS:
                st.markdown(f"- **{title}:** {detail}")
        with st.expander("Equation image: what needs clarification", expanded=False):
            st.warning(material.EQUATION_NOTE)
            st.markdown(
                f"[Open the original Q3 equation image on Noroff]({material.RESOURCE_LINKS[5][1]})"
            )
    else:
        with st.expander("Example questions from general to specific", expanded=False):
            st.caption(
                "Original Study Buddy examples to adapt, not the downloaded official solution. The number of questions is a suggestion, not a task requirement."
            )
            for title, questions in curriculum.QUESTION_GROUPS:
                st.markdown("#### " + title)
                for question in questions:
                    st.markdown("- " + question)
    downloads = [
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
    ]
    if number == "1.2":
        downloads = [
            (
                guide["template_file"],
                "Download Word editing plan (Markdown)",
                "text/markdown",
            ),
            (
                "ARP Task 1.2 Formatting Checks.csv",
                "Download five formatting checks (CSV)",
                "text/csv",
            ),
            (
                "ARP Task 1.2 Seven Step Guide.md",
                "Download seven-step Word guide (Markdown)",
                "text/markdown",
            ),
        ]
        st.link_button(
            "Download original LessonTasks.docx from Noroff", material.SOURCE_URL
        )
        st.caption(
            "Original working file hosted by Noroff; sign in there to download it. Edit a copy in Word. This app does not host the original file or a completed task."
        )
    elif number == "1.3":
        downloads = [
            (
                guide["template_file"],
                "Download workplace overview template (Markdown)",
                "text/markdown",
            ),
            (
                "ARP Task 1.3 Citation Evidence Matrix.csv",
                "Download citation evidence matrix (CSV)",
                "text/csv",
            ),
            (
                "ARP Task 1.3 Seven Step Guide.md",
                "Download seven-step referencing guide (Markdown)",
                "text/markdown",
            ),
            (
                "ARP Task 1.3 Harvard Source Starter.md",
                "Download Harvard source starter (Markdown)",
                "text/markdown",
            ),
        ]
    elif number == "1.4":
        downloads = [
            (
                guide["template_file"],
                "Download Office workflow and check log (Markdown)",
                "text/markdown",
            ),
            (
                "ARP Task 1.4 Chart Experiments.csv",
                "Download chart experiment log (CSV)",
                "text/csv",
            ),
            (
                "ARP Task 1.4 Caption Register.csv",
                "Download caption and list register (CSV)",
                "text/csv",
            ),
            ("ARP Task 1.4 Table Data.csv", "Download Q3 table data (CSV)", "text/csv"),
            (
                "ARP Task 1.4 Seven Step Guide.md",
                "Download seven-step visuals guide (Markdown)",
                "text/markdown",
            ),
        ]
    for name, label, mime in downloads:
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
    if number == "1.1":
        st.caption(
            "The report outline is optional lesson practice. Task 1.1 asks for questions; it does not prescribe a completed report, page count or file format."
        )
    draft_title = {
        "1.1": "question plan",
        "1.2": "Word plan and check notes",
        "1.3": "overview and source notes",
        "1.4": "Office plan and observations",
    }[number]
    draft_label = {
        "1.1": "Your report questions and evidence plan",
        "1.2": "Your Word editing plan and check notes",
        "1.3": "Your workplace overview and source notes",
        "1.4": "Your Office workflow and observed results",
    }[number]
    with st.expander(
        f"Write your Task {number} " + draft_title,
        expanded=False,
    ):
        editor_key = f"{base_key}_arp_draft_{uid}"
        if editor_key in st.session_state and st.session_state[editor_key] != draft(
            st.session_state, guide
        ):
            st.session_state[editor_key] = draft(st.session_state, guide)
        st.text_area(
            draft_label,
            value=draft(st.session_state, guide),
            height=260,
            key=editor_key,
            on_change=remember_draft,
            args=(editor_key, uid),
        )
        st.caption(
            "Apply edits with Ctrl+Enter or by leaving the field. Your draft is saved with Study Buddy state on this app instance; download a copy to keep your work."
        )
        st.download_button(
            f"Download my Task {number} draft",
            draft(st.session_state, guide).encode(),
            file_name=f"My ARP Task {number} draft.md",
            mime="text/markdown",
            key=f"{base_key}_arp_my_draft",
        )
    with st.expander(f"Full Task {number} guide and checklist", expanded=False):
        st.markdown(curriculum.guide_markdown(guide))
    if show_images:
        render_images(base_key, guide)


def render_lesson_resources(lesson, context):
    if lesson.get("course_code") != curriculum.COURSE_CODE:
        return
    number = lesson["lesson_number"]
    guides = curriculum.get_task_guides(number)
    if not guides:
        return
    guide = guides[0]
    base_key = f"arp_{context}_{number}"
    render_images(base_key, guide)
    with st.expander(f"Task {number} walkthrough and templates", expanded=False):
        render_task_resources(
            guides,
            base_key,
            heading=f"### Task {number} — seven steps",
            show_images=False,
        )
        st.button(
            f"Prepare Task {number} in Exam Resolver",
            key=f"{base_key}_prepare",
            on_click=prepare_task_in_resolver,
            args=(guide,),
        )
        st.caption(
            "Transfers your applied draft and selected step. Generate a review in Exam Resolver when you are ready; no Noroff task is submitted."
        )
