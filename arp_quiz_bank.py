"""Original lesson-based practice; no live Noroff quiz questions are collected."""

import json
from pathlib import Path
import streamlit as st

CONTENT_REVISION = "2026-11-09-arp-module2-practice"
COURSE_CODE = "FI1BBAR05"
ASSETS = Path(__file__).resolve().parent / "assets" / "arp"
RESOLVER_BASE = "course_exam_connector_fi1bbar05_learn_practice"
STATE_KEY = "arp_quiz_responses"
LESSONS = {
    "2.1": "Reporting tools and source reliability",
    "2.2": "Evidence-based data reports",
    "2.3": "EDA and infographics",
    "2.4": "Communication and teamwork",
}
NOTICE = (
    "Original Study Buddy practice based on Lessons 2.1–2.4. These are not collected, reviewed or predicted "
    "Noroff quiz questions. No official attempt was started and no Noroff grade or completion is recorded here."
)
ILLUSTRATION_CAPTIONS = {
    "2.1": "Choose a reporting tool for the reader's need. Plain Markdown formats text; code execution needs an appropriate environment. Trace original evidence and assess specific claims rather than counting reposts or judging tone alone.",
    "2.2": "Connect purpose, evidence, interpretation and conclusion. Use real heading styles, readable category labels, units and a zero baseline for column magnitudes. A static chart picture needs updating when its data change.",
    "2.3": "Inspect data before selecting evidence and designing a message. Keep sources and limits visible. Save the editable GIMP working project as XCF and separately export the flattened JPEG; dimensions depend on the intended use.",
    "2.4": "Ben leads EDA; Anna structures the report and Chris explains its visuals; the leader prepares the stakeholder speech. Match tense to actual work status, preserve facts for each audience and check actual pagination separately from approximate words.",
}


def get_questions(lesson=None):
    bank = json.loads(
        (ASSETS / "module-2-practice-bank.json").read_text(encoding="utf-8")
    )
    return [q for q in bank if lesson is None or q["lesson_number"] == lesson]


def answer_text(q):
    reasons = "\n".join(
        f"{chr(65+i)}: {reason}" for i, reason in enumerate(q["option_feedback"])
    )
    return (
        f"Practice answer: {q['options'][q['correct']]}. {q['explanation']}\n\n"
        f"Option reasoning:\n{reasons}\n\nExample: {q['example']}"
    )


def question_block(q):
    return (
        f"[ARP original practice / {q['id']}] Lesson {q['lesson_number']}\n"
        + q["question"]
        + "\n\n"
        + "\n".join(f"{chr(65+i)}. {value}" for i, value in enumerate(q["options"]))
    )


def get_curated_questions():
    return [
        {**q, "question": question_block(q), "answer": answer_text(q)}
        for q in get_questions()
    ]


def revision_markdown(lesson=None):
    parts = ["# ARP Module 2 — original practice quiz", NOTICE]
    for q in get_questions(lesson):
        parts += [
            "## " + question_block(q),
            answer_text(q),
            f"[Lesson source]({q['source_url']}) · Original practice authored {q['authored_on']}.",
        ]
    return "\n\n".join(parts) + "\n"


def response(uid):
    return st.session_state.get(STATE_KEY, {}).get(uid, {})


def remember_response(widget_key, uid, field):
    saved = dict(st.session_state.get(STATE_KEY, {}))
    saved[uid] = {**saved.get(uid, {}), field: st.session_state[widget_key]}
    st.session_state[STATE_KEY] = saved


def check_answer(q, answer):
    if answer is None:
        st.warning("Choose an answer before checking.")
        return
    saved = dict(st.session_state.get(STATE_KEY, {}))
    saved[q["id"]] = {**saved.get(q["id"], {}), "checked": answer}
    st.session_state[STATE_KEY] = saved


def resolver_prompt(q):
    saved = response(q["id"])
    return (
        question_block(q)
        + f"\n\nMy practice answer: {saved.get('selected') or '[not selected]'}"
        + f"\nMy reasoning: {saved.get('reason') or '[add my explanation]'}"
        + "\n\nHelp me learn this original practice concept in English. Explain the evidence, "
        "why each option fits or fails and an applied example. This is not an official Noroff question "
        "or a request to complete a live graded quiz."
    )


def prepare_in_resolver(q, base_key=RESOLVER_BASE):
    from arp_curriculum import get_course_lessons

    lesson = next(
        l for l in get_course_lessons() if l["lesson_number"] == q["lesson_number"]
    )
    st.session_state[f"{base_key}_prompt"] = resolver_prompt(q)
    st.session_state[f"{base_key}_quiz_reference"] = q["id"]
    st.session_state[f"{base_key}_source_pool"] = "Lessons only"
    st.session_state[f"{base_key}_scope"] = "Specific lesson or outcome"
    st.session_state[f"{base_key}_specific_source"] = (
        f"Lesson {lesson['lesson_number']}: {lesson['title']}"
    )


def render_explanation(q, base_key):
    st.info("Practice answer: " + q["options"][q["correct"]])
    st.markdown("**Why:** " + q["explanation"])
    with st.expander("Reasoning for every option", expanded=False):
        for i, reason in enumerate(q["option_feedback"]):
            st.markdown(f"- **{chr(65+i)} · {q['options'][i]}:** {reason}")
    st.markdown("**Apply it:** " + q["example"])
    with st.expander(
        "Visual study guide — " + LESSONS[q["lesson_number"]], expanded=False
    ):
        path = ASSETS / q["illustration"]
        if path.is_file():
            st.image(str(path), width="stretch")
            st.download_button(
                "Download practice illustration (PNG)",
                path.read_bytes(),
                file_name=path.name,
                mime="image/png",
                key=f"{base_key}_visual_{q['id']}",
            )
        else:
            st.warning("Illustration unavailable. Use the explanation below.")
        st.write(ILLUSTRATION_CAPTIONS[q["lesson_number"]])
        st.caption(
            "AI-generated educational illustration made with built-in OpenAI imagegen. Conceptual study aid, not a software screenshot, measured result or official quiz question."
        )
    st.markdown(f"[Read Lesson {q['lesson_number']} on Noroff]({q['source_url']})")


def render_resolver_reference(base_key, prompt):
    uid = st.session_state.get(f"{base_key}_quiz_reference")
    q = next((q for q in get_questions() if q["id"] == uid), None)
    if q and prompt.startswith(question_block(q)):
        with st.expander(
            "Original practice reference: reasoning and illustration", expanded=False
        ):
            st.caption(NOTICE)
            render_explanation(q, base_key + "_reference")
        return q
    return None


def render_quiz_bank(base_key="arp_bank", resolver_base=RESOLVER_BASE):
    st.subheader("ARP Module 2 Practice Quiz Bank")
    st.info(NOTICE)
    st.caption(
        "16 original questions · four per lesson · English explanations and four imagegen study guides"
    )
    st.markdown(
        "Choose a lesson and question, try an answer, then check the reasoning. Your practice record is separate from Noroff results."
    )
    checked = [(q, response(q["id"]).get("checked")) for q in get_questions()]
    valid = [(q, a) for q, a in checked if a in q["options"]]
    correct = sum(a == q["options"][q["correct"]] for q, a in valid)
    st.caption(
        f"Practice record: {len(valid)}/16 checked · {correct} correct on last check. This is not a Noroff grade."
    )
    lesson = st.selectbox(
        "Filter practice by lesson",
        [None, *LESSONS],
        format_func=lambda n: (
            "All Module 2 lessons" if n is None else f"Lesson {n}: {LESSONS[n]}"
        ),
        key=f"{base_key}_lesson",
    )
    pool = get_questions(lesson)
    uid = st.selectbox(
        "Choose an original practice question",
        [q["id"] for q in pool],
        format_func=lambda uid: next(
            f"Lesson {q['lesson_number']} · {q['question']}"
            for q in pool
            if q["id"] == uid
        ),
        key=f"{base_key}_question_{lesson or 'all'}",
    )
    q = next(q for q in pool if q["id"] == uid)
    saved = response(uid)
    st.markdown("#### 1. Try and explain")
    st.markdown(q["question"])
    answer_key = f"{base_key}_{uid}_answer"
    selected = saved.get("selected")
    answer = st.radio(
        "Your practice answer",
        q["options"],
        index=q["options"].index(selected) if selected in q["options"] else None,
        key=answer_key,
        on_change=remember_response,
        args=(answer_key, uid, "selected"),
    )
    reason_key = f"{base_key}_{uid}_reason"
    st.text_area(
        "Explain your choice (optional)",
        value=saved.get("reason", ""),
        key=reason_key,
        on_change=remember_response,
        args=(reason_key, uid, "reason"),
        height=100,
    )
    if st.button(
        "Check practice answer", key=f"{base_key}_{uid}_check", type="primary"
    ):
        check_answer(q, answer)
        if answer is not None:
            st.rerun()
    checked_answer = response(uid).get("checked")
    if checked_answer in q["options"]:
        if answer != checked_answer:
            st.warning(
                "Your selection changed. Check again to update the feedback and practice record."
            )
        elif checked_answer == q["options"][q["correct"]]:
            st.success(
                "Correct for this practice question. Explain the concept in your own words."
            )
        else:
            st.warning("Review the distinction below, then try again.")
        st.markdown("#### 2. Understand and apply")
        render_explanation(q, base_key)
    else:
        st.caption("Check your answer to reveal the explanation and illustration.")
    st.markdown("#### 3. Practise in Exam Resolver")
    st.button(
        "Use original practice question in Exam Resolver",
        key=f"{base_key}_{uid}_resolver",
        on_click=prepare_in_resolver,
        args=(q, resolver_base),
    )
    if st.session_state.get(f"{resolver_base}_quiz_reference") == uid:
        st.success(
            "Prepared with your answer, reasoning and linked lesson. Open Course Content → Universal Exam Resolver. AI review remains manual."
        )
    st.download_button(
        "Download original practice notes with answers (English)",
        revision_markdown(lesson),
        file_name=f"ARP-module-2-{lesson or 'all'}-original-practice.md",
        mime="text/markdown",
        key=f"{base_key}_download",
    )
