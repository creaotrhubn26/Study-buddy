"""English practice bank covering the four reviewed DVS module quizzes."""
import json
from pathlib import Path
import streamlit as st

CONTENT_REVISION = "2026-10-14-dvs-quizzes"
COURSE_CODE = "FI1BBDV75"
ASSETS = Path(__file__).resolve().parent / "assets" / "dvs"
MODULES = {1: "Design thinking", 2: "UX, graphics and honest reporting",
           3: "Data visualisation and Excel charts", 4: "Presentations and storytelling"}


def get_questions(module=None):
    bank = json.loads((ASSETS / "module-quiz-bank.json").read_text(encoding="utf-8"))
    return [q for q in bank if module is None or q["module"] == module]


def answer_text(q):
    return f"Correct answer: {q['options'][q['correct']]}. {q['explanation']}\n\nExample: {q['example']}"


def get_curated_questions():
    return [{**q, "question": q["question"] + "\n\n" + "\n".join(
        f"{chr(65+i)}. {option}" for i, option in enumerate(q["options"])),
        "answer": answer_text(q)} for q in get_questions()]


def revision_markdown(module=None):
    text = "# DVS Module Quiz Bank\n\nEnglish practice adaptations of the reviewed questions; not a full Noroff question pool.\n\n"
    for q in get_questions(module):
        text += f"## Module {q['module']} / {q['id']}\n\n{q['question']}\n\n"
        text += "\n".join(f"- {option}" for option in q["options"])
        text += f"\n\n{answer_text(q)}\n\n[Source quiz]({q['source_url']})\n\n"
    return text


def resolver_prompt(q):
    return (f"[DVS Module {q['module']} / {q['id']}] {q['question']}\n\n"
            + "\n".join(f"{chr(65+i)}. {v}" for i, v in enumerate(q["options"]))
            + "\n\nMy answer: [choose an option and explain why]\n"
              "Help me reason through this practice question in English. Explain the concept, the distractors and an applied example.")


def prepare_in_resolver(q, base_key):
    st.session_state[f"{base_key}_prompt"] = resolver_prompt(q)
    st.session_state[f"{base_key}_quiz_reference"] = q["id"]


def render_explanation(q):
    st.info(f"Correct answer: {q['options'][q['correct']]}")
    st.markdown("**Why:** " + q["explanation"])
    st.markdown("**Apply it:** " + q["example"])
    path = ASSETS / q["illustration"]
    if path.is_file():
        st.image(str(path), caption=f"Module {q['module']}: {MODULES[q['module']]} — illustrated revision")
    st.caption(q["verified"] + ". Wording is adapted for practice; software labels can vary by version.")
    st.markdown(f"[Open the original Noroff module quiz]({q['source_url']})")


def render_resolver_reference(base_key, prompt):
    uid = st.session_state.get(f"{base_key}_quiz_reference")
    q = next((q for q in get_questions() if q["id"] == uid), None)
    if q and prompt.startswith(f"[DVS Module {q['module']} / {q['id']}]"):
        with st.expander("Quiz reference: answer, reasoning and illustration", expanded=False):
            render_explanation(q)
        return q
    return None


def render_quiz_bank(base_key="dvs_bank", resolver_base="course_exam_connector_fi1bbdv75_learn_practice"):
    st.subheader("DVS Module Quiz Bank")
    st.caption("40 reviewed question occurrences · 39 distinct practice questions · Modules 1–4")
    st.markdown("Choose a module and question, try an answer, then check the explanation and illustration. These English practice adaptations cover the four attempts reviewed, not every possible question in Noroff’s pool.")
    module = st.selectbox("Quiz module", [None, 1, 2, 3, 4],
        format_func=lambda m: "All four modules" if m is None else f"Module {m}: {MODULES[m]}", key=f"{base_key}_module")
    pool = get_questions(module)
    if module in (None, 2):
        st.caption("Module 2 repeated the bias question twice. It is stored once, with both source positions retained.")
    qid = st.selectbox("Choose a quiz question", [q["id"] for q in pool],
        format_func=lambda uid: next(f"Module {q['module']} · {q['question']}" for q in pool if q["id"] == uid),
        key=f"{base_key}_question_{module}")
    q = next(q for q in pool if q["id"] == qid)
    answer_key = f"{base_key}_{qid}_answer"
    checked_key = f"{base_key}_{qid}_checked"
    st.markdown("#### 1. Try the question")
    st.markdown(q["question"])
    previous = st.session_state.get(checked_key)
    answer = st.radio("Your quiz answer", q["options"],
        index=q["options"].index(previous) if previous in q["options"] else None, key=answer_key)
    if st.button("Check quiz answer", key=f"{base_key}_{qid}_check", type="primary"):
        if answer is None:
            st.warning("Choose an answer before checking.")
        else:
            st.session_state[checked_key] = answer
    checked = st.session_state.get(checked_key)
    if checked is not None:
        if checked == q["options"][q["correct"]]:
            st.success("Correct — now explain the reason in your own words.")
        else:
            st.warning(f"Your checked answer was {checked}. Review the distinction below, then try again.")
        if answer != checked:
            st.caption("Your selection has changed. Check it again to update the feedback.")
        st.markdown("#### 2. Understand and apply")
        render_explanation(q)
    with st.expander("Review the answer without attempting", expanded=False):
        if st.checkbox("Reveal this answer", key=f"{base_key}_{qid}_reveal"):
            render_explanation(q)
    st.markdown("#### 3. Practise explaining it")
    st.button("Use quiz question in Exam Resolver", key=f"{base_key}_{qid}_resolver",
              on_click=prepare_in_resolver, args=(q, resolver_base))
    if st.session_state.get(f"{resolver_base}_quiz_reference") == qid:
        st.success("Question prepared. Open Course Content → Universal Exam Resolver to add your reasoning. Nothing is submitted to Noroff.")
    st.download_button("Download quiz revision notes with answers (English)", revision_markdown(module),
        file_name=f"DVS-module-{module or 'all'}-quiz-revision.md", mime="text/markdown", key=f"{base_key}_download")
