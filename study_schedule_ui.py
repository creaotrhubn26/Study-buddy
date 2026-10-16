"""Shared English schedule views for Study Buddy."""

from datetime import date
from html import escape

import streamlit as st

from study_buddy_state import save_persisted_state
from study_schedule import (
    SCHEDULE_EVENTS,
    STATUS_LABELS,
    next_course,
    oslo_today,
    partition_rows,
    save_submission,
    schedule_rows,
)


def _rows(catalog=(), names=None):
    return schedule_rows(
        st.session_state.get("assessment_submissions"),
        st.session_state.get("completed_courses", []),
        names=names,
        catalog=catalog,
    )


def _open_course(row):
    st.session_state["nav_section"] = "Learning"
    st.session_state["nav_page"] = "Learn & Practice"
    st.session_state["last_page"] = "Learn & Practice"
    st.session_state["lp_selected_course"] = f"{row['full_code']} - {row['name']}"
    st.session_state["last_selected_course"] = row["name"]


def _card(row):
    color = (
        "#2563eb" if row["closed"] else ("#b45309" if row["days"] <= 7 else "#64748b")
    )
    # Use inherited foreground/background for both Streamlit themes.
    st.markdown(
        f"""<div style="border:1px solid #94a3b866;border-left:4px solid {color};
      border-radius:10px;padding:14px 16px;margin:8px 0;">
      <div style="font-size:.8rem;opacity:.75">{escape(row['code'])} · {escape(row['status_label'])}</div>
      <div style="font-size:1.05rem;font-weight:650;margin:4px 0">{escape(row['name'])}</div>
      <div>{"Original deadline" if row["status"] == "resubmission" else "Deadline"} <strong>{row['deadline'].strftime('%d %b %Y')} · 23:59</strong></div>
      <div style="margin-top:4px">{escape(row['timing'])}</div></div>""",
        unsafe_allow_html=True,
    )


def render_next_up(catalog, names=None, key="schedule"):
    rows = _rows(catalog, names)
    row = next_course(rows)
    st.subheader("Next up")
    if row is None:
        st.info(
            "No scheduled course remaining in this selection. Review recorded submissions or change the filter. Year 2 dates are not yet verified."
        )
        return
    delta = (row["start"] - oslo_today()).days
    with st.container(border=True):
        start_text = (
            f"Starts {row['start'].strftime('%a %d %b %Y')}"
            if delta > 0
            else f"Started {row['start'].strftime('%d %b %Y')}"
        )
        assessment_text = (
            f"Assessment week: {row['assessment_start'].strftime('%d %b')}–{row['deadline'].strftime('%d %b %Y')}"
            if row["assessment_start"]
            else ""
        )
        st.markdown(
            f"""<div style="line-height:1.6">
          <div style="font-size:.8rem;opacity:.75">{'STARTING NEXT' if delta > 0 else 'CURRENT COURSE'}</div>
          <div style="font-size:1.3rem;font-weight:650;margin:3px 0">{escape(row['name'])}</div>
          <div>{escape(row['code'])} · {escape(start_text)}</div>
          <div style="font-size:.9rem;opacity:.8">{escape(assessment_text)}</div>
          <div><strong>Deadline: {row['deadline'].strftime('%d %b %Y')} at 23:59</strong> · {escape(row['timing'])}</div>
        </div>""",
            unsafe_allow_html=True,
        )
        if any(c["code"] == row["full_code"] for c in catalog):
            st.button(
                "Open course",
                key=f"{key}_open",
                type="primary",
                on_click=_open_course,
                args=(row,),
                help="Opens Learn & Practice. Noroff usually releases new course material on Mondays at 08:00; availability there is separate from this study plan.",
            )
        else:
            st.link_button(
                "Open Noroff programme home",
                "https://learning.noroff.no/course/view.php?id=438",
            )


def render_submission_editor(catalog, key="schedule"):
    with st.expander("Update submission status", expanded=False):
        st.caption(
            "Your personal record, saved with Study Buddy state on this app instance. This is not an automatic Noroff sync. Check Noroff before recording a submission or grade. Saving here never submits an assessment."
        )
        rows = _rows(catalog)
        chosen = st.selectbox(
            "Assessment",
            [r["code"] for r in rows],
            format_func=lambda c: next(
                f"{r['name']} ({c})" for r in rows if r["code"] == c
            ),
            key=f"{key}_status_course",
        )
        row = next(r for r in rows if r["code"] == chosen)
        options = ["not_recorded", "submitted", "passed", "resubmission"]
        current = row["status"] if row["status"] in options else "not_recorded"
        revision = f"{row['status']}_{row['submitted_date']}"
        # Course-specific widget keys prevent carrying one course's edit to another.
        status = st.selectbox(
            "Submission status",
            options,
            index=options.index(current),
            format_func=STATUS_LABELS.get,
            key=f"{key}_{chosen}_{revision}_status",
        )
        submitted_date = None
        if status in {"submitted", "passed"}:
            submitted_date = st.date_input(
                "Submitted on",
                value=row["submitted_date"] or oslo_today(),
                max_value=oslo_today(),
                key=f"{key}_{chosen}_{revision}_date",
            )
        if row["status"] == "completed":
            st.info(
                "An older course-completion flag exists. Saving a submission status overrides it for reminders; it does not change your learning progress."
            )
        if st.button("Save submission status", key=f"{key}_save"):
            previous = st.session_state.get("assessment_submissions", {})
            try:
                save_submission(st.session_state, chosen, status, submitted_date)
                if not save_persisted_state(st.session_state):
                    st.session_state["assessment_submissions"] = previous
                    st.error(
                        "Could not save the status. Please try again; your previous record was kept."
                    )
                else:
                    st.session_state[f"{key}_saved"] = (
                        f"Saved: {row['name']} — {STATUS_LABELS[status]}"
                    )
                    st.rerun()
            except ValueError as error:
                st.error(str(error))
    message = st.session_state.pop(f"{key}_saved", None)
    if message:
        st.success(message)


def render_deadlines(catalog=(), names=None, key="schedule"):
    groups = partition_rows(_rows(catalog, names))
    st.subheader("Upcoming deadlines")
    st.caption(
        "Chronological order · 23:59 Europe/Oslo · Submitted work is listed separately."
    )
    if not groups["upcoming"]:
        st.info(
            "No upcoming deadlines in this selection. This does not confirm that past assessments were submitted."
        )
    for row in groups["upcoming"]:
        _card(row)
    if groups["attention"]:
        st.markdown("#### Needs attention")
        for row in groups["attention"]:
            _card(row)
    if groups["recorded"]:
        st.markdown("#### Recorded submissions")
        for row in sorted(
            groups["recorded"], key=lambda r: r["deadline"], reverse=True
        ):
            _card(row)
        st.caption(
            "Submission and grade labels reflect your saved records; they are not verified automatically with Noroff."
        )
    if groups["past"]:
        with st.expander(
            f"Past deadlines · {len(groups['past'])} without a recorded submission",
            expanded=False,
        ):
            st.caption(
                "A passed deadline is not evidence of completion. Check Noroff and update your record if you have already submitted."
            )
            for row in reversed(groups["past"]):
                _card(row)


def render_schedule(catalog, names=None, key="schedule"):
    render_next_up(catalog, names, key)
    render_submission_editor(catalog, key)
    render_deadlines(catalog, names, key)


def render_course_reminder(name, catalog=()):
    rows = _rows(catalog, {name})
    if rows:
        _card(rows[0])
        st.caption(
            "Manage your personal submission record in Course Plan or Progression Plan."
        )


def render_timeline(catalog):
    st.subheader("Module timeline")
    choices = {"All courses": None, **{r["name"]: r["code"] for r in _rows(catalog)}}
    selected = st.selectbox(
        "Timeline course", list(choices), key="schedule_timeline_course"
    )
    kind = st.selectbox(
        "Event type",
        ["All events", "Module starts", "Assessment weeks", "Deadlines"],
        key="schedule_event_type",
    )
    kinds = {
        "Module starts": {"module_start", "enrollment"},
        "Assessment weeks": {"assessment_start"},
        "Deadlines": {"deadline"},
    }
    rows = {r["code"]: r for r in _rows(catalog)}
    events = [
        e
        for e in SCHEDULE_EVENTS
        if (choices[selected] is None or e["course"] == choices[selected])
        and (kind == "All events" or e["type"] in kinds[kind])
    ]
    future, past = [], []
    for event in sorted(events, key=lambda e: e["date"]):

        event_date = date.fromisoformat(event["date"])
        line = f"**{event_date.strftime('%d %b %Y')}** · {event['name']}"
        if event["type"] == "deadline":
            line += " · " + rows[event["course"]]["status_label"]
        (past if event_date < oslo_today() else future).append(line)
    if not future:
        st.info("No upcoming events match these filters.")
    for line in future:
        st.markdown(line)
    if past:
        with st.expander(f"Past events ({len(past)})"):
            st.caption(
                "These events are in the past; this does not indicate lesson completion or submission."
            )
            for line in reversed(past):
                st.markdown(line)
