"""Verified schedule and explicit, user-recorded submission status."""

from datetime import date, datetime
from zoneinfo import ZoneInfo

from study_buddy_state import (
    COURSE_PROGRESSION_MAP,
    PROGRAM_DEADLINES,
    STUDY_PATH_JAN2026,
)

SCHEDULE_EVENTS = [
    # Enrollment / IC
    {
        "date": "2026-01-05",
        "name": "Enrollment / Course Start",
        "type": "enrollment",
        "course": "IC",
        "course_name": "Introduction Course",
    },
    {
        "date": "2026-01-06",
        "name": "Introduction Course Begins",
        "type": "module_start",
        "course": "IC",
        "course_name": "Introduction Course",
    },
    {
        "date": "2026-01-11",
        "name": "Introduction Course Deadline",
        "type": "deadline",
        "course": "IC",
        "course_name": "Introduction Course",
    },
    # DAF
    {
        "date": "2026-01-12",
        "name": "DAF – Module 1 starts",
        "type": "module_start",
        "course": "DAF",
        "course_name": "Data Analysis Fundamentals",
    },
    {
        "date": "2026-01-19",
        "name": "DAF – Module 2 starts",
        "type": "module_start",
        "course": "DAF",
        "course_name": "Data Analysis Fundamentals",
    },
    {
        "date": "2026-01-26",
        "name": "DAF Assessment Week begins",
        "type": "assessment_start",
        "course": "DAF",
        "course_name": "Data Analysis Fundamentals",
    },
    {
        "date": "2026-02-01",
        "name": "DAF Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "DAF",
        "course_name": "Data Analysis Fundamentals",
    },
    # SPF
    {
        "date": "2026-02-02",
        "name": "SPF – Module 1 starts",
        "type": "module_start",
        "course": "SPF",
        "course_name": "Spreadsheet Fundamentals",
    },
    {
        "date": "2026-02-09",
        "name": "SPF – Module 2 starts",
        "type": "module_start",
        "course": "SPF",
        "course_name": "Spreadsheet Fundamentals",
    },
    {
        "date": "2026-02-16",
        "name": "SPF Assessment Week begins",
        "type": "assessment_start",
        "course": "SPF",
        "course_name": "Spreadsheet Fundamentals",
    },
    {
        "date": "2026-02-22",
        "name": "SPF Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "SPF",
        "course_name": "Spreadsheet Fundamentals",
    },
    # DDM
    {
        "date": "2026-02-23",
        "name": "DDM – Module 1 starts",
        "type": "module_start",
        "course": "DDM",
        "course_name": "Data Driven Decision-Making",
    },
    {
        "date": "2026-03-02",
        "name": "DDM – Module 2 starts",
        "type": "module_start",
        "course": "DDM",
        "course_name": "Data Driven Decision-Making",
    },
    {
        "date": "2026-03-09",
        "name": "DDM – Module 3 starts",
        "type": "module_start",
        "course": "DDM",
        "course_name": "Data Driven Decision-Making",
    },
    {
        "date": "2026-03-16",
        "name": "DDM Assessment Week begins",
        "type": "assessment_start",
        "course": "DDM",
        "course_name": "Data Driven Decision-Making",
    },
    {
        "date": "2026-03-22",
        "name": "DDM Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "DDM",
        "course_name": "Data Driven Decision-Making",
    },
    # STT
    {
        "date": "2026-03-23",
        "name": "STT – Module 1 starts",
        "type": "module_start",
        "course": "STT",
        "course_name": "Statistical Tools",
    },
    {
        "date": "2026-04-06",
        "name": "STT – Module 2 starts",
        "type": "module_start",
        "course": "STT",
        "course_name": "Statistical Tools",
    },
    {
        "date": "2026-04-13",
        "name": "STT Assessment Week begins",
        "type": "assessment_start",
        "course": "STT",
        "course_name": "Statistical Tools",
    },
    {
        "date": "2026-04-19",
        "name": "STT Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "STT",
        "course_name": "Statistical Tools",
    },
    # SP1 – Semester Project
    {
        "date": "2026-04-20",
        "name": "SP1 Semester Project – Week 1",
        "type": "module_start",
        "course": "SP1",
        "course_name": "Semester Project 1",
    },
    {
        "date": "2026-04-27",
        "name": "SP1 Semester Project – Week 2",
        "type": "module_start",
        "course": "SP1",
        "course_name": "Semester Project 1",
    },
    {
        "date": "2026-05-04",
        "name": "SP1 Semester Project – Week 3",
        "type": "module_start",
        "course": "SP1",
        "course_name": "Semester Project 1",
    },
    {
        "date": "2026-05-11",
        "name": "SP1 Semester Project – Final Week begins",
        "type": "assessment_start",
        "course": "SP1",
        "course_name": "Semester Project 1",
    },
    {
        "date": "2026-05-17",
        "name": "SP1 Semester Project Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "SP1",
        "course_name": "Semester Project 1",
    },
    # EVO
    {
        "date": "2026-05-18",
        "name": "EVO – Module 1 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-05-25",
        "name": "EVO – Module 2 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-06-01",
        "name": "EVO – Module 3 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-08-10",
        "name": "EVO – Module 4 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-08-17",
        "name": "EVO – Module 5 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-08-24",
        "name": "EVO – Module 6 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-08-31",
        "name": "EVO – Module 7 starts",
        "type": "module_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-09-07",
        "name": "EVO Assessment Week begins",
        "type": "assessment_start",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    {
        "date": "2026-09-13",
        "name": "EVO Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "EVO",
        "course_name": "Evaluation of Outcomes",
    },
    # DVS
    {
        "date": "2026-09-14",
        "name": "DVS – Module 1 starts",
        "type": "module_start",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    {
        "date": "2026-09-21",
        "name": "DVS – Module 2 starts",
        "type": "module_start",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    {
        "date": "2026-09-28",
        "name": "DVS – Module 3 starts",
        "type": "module_start",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    {
        "date": "2026-10-05",
        "name": "DVS – Module 4 starts",
        "type": "module_start",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    {
        "date": "2026-10-12",
        "name": "DVS Assessment Week begins",
        "type": "assessment_start",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    {
        "date": "2026-10-18",
        "name": "DVS Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "DVS",
        "course_name": "Data Visualisation",
    },
    # ARP
    {
        "date": "2026-10-19",
        "name": "ARP – Module 1 starts",
        "type": "module_start",
        "course": "ARP",
        "course_name": "Analysis Reporting",
    },
    {
        "date": "2026-10-26",
        "name": "ARP – Module 2 starts",
        "type": "module_start",
        "course": "ARP",
        "course_name": "Analysis Reporting",
    },
    {
        "date": "2026-11-02",
        "name": "ARP Assessment Week begins",
        "type": "assessment_start",
        "course": "ARP",
        "course_name": "Analysis Reporting",
    },
    {
        "date": "2026-11-08",
        "name": "ARP Assessment Deadline (Sun 23:59)",
        "type": "deadline",
        "course": "ARP",
        "course_name": "Analysis Reporting",
    },
    # EP1 – Exam Project
    {
        "date": "2026-11-09",
        "name": "EP1 Exam Project – Week 1",
        "type": "module_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-11-16",
        "name": "EP1 Exam Project – Week 2",
        "type": "module_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-11-23",
        "name": "EP1 Exam Project – Week 3",
        "type": "module_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-11-30",
        "name": "EP1 Exam Project – Week 4",
        "type": "module_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-12-07",
        "name": "EP1 Exam Project – Week 5",
        "type": "module_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-12-14",
        "name": "EP1 Exam Project – Final Week begins",
        "type": "assessment_start",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
    {
        "date": "2026-12-20",
        "name": "EP1 Exam Project 1 – FINAL DELIVERY (Sun 23:59)",
        "type": "deadline",
        "course": "EP1",
        "course_name": "Exam Project 1",
    },
]

STATUS_LABELS = {
    "not_recorded": "No submission recorded",
    "submitted": "Submitted · Awaiting grade",
    "passed": "Passed (recorded by you)",
    "resubmission": "Resubmission required",
    "completed": "Marked complete (recorded by you)",
}
CLOSED_STATUSES = {"submitted", "passed", "completed"}


def oslo_today():
    return datetime.now(ZoneInfo("Europe/Oslo")).date()


def schedule_rows(submissions=None, completed=(), today=None, names=None, catalog=()):
    """Calendar passage never supplies submission or grade evidence."""
    today = today or oslo_today()
    submissions = submissions if isinstance(submissions, dict) else {}
    completed = set(completed or ())
    full_codes = {c["name"]: c["code"] for c in catalog}
    deadlines = {code: date.fromisoformat(d) for code, _, d in PROGRAM_DEADLINES}
    rows = []
    for code, name, start, end in STUDY_PATH_JAN2026:
        if names is not None and name not in names:
            continue
        full_code = full_codes.get(name, code)
        record = submissions.get(code, {})
        record = record if isinstance(record, dict) else {}
        status = record.get("status", "not_recorded")
        if status not in STATUS_LABELS or status == "completed":
            status = "not_recorded"
        # An explicit record overrides the older completion checkbox.
        if not record and (code in completed or full_code in completed):
            status = "completed"
        submitted_date = record.get("submitted_date")
        try:
            submitted_date = (
                date.fromisoformat(submitted_date) if submitted_date else None
            )
        except (ValueError, TypeError):
            submitted_date = None
        deadline = deadlines[code]
        days = (deadline - today).days
        closed = status in CLOSED_STATUSES
        if status == "resubmission":
            timing = "Check your resit instructions on Noroff for the new deadline"
        elif closed:
            timing = "Submission date not recorded"
            if submitted_date:
                timing = "Submitted " + submitted_date.strftime("%d %b %Y")
            if status == "completed":
                timing = "Completion recorded; grade not verified"
        elif days < 0:
            timing = "Deadline passed · " + (
                "Check your resit instructions"
                if status == "resubmission"
                else "No submission recorded"
            )
        elif days == 0:
            timing = "Due today at 23:59"
        else:
            timing = f"{days} day{'s' if days != 1 else ''} left"
        assessment = COURSE_PROGRESSION_MAP.get(name)
        rows.append(
            dict(
                code=code,
                full_code=full_code,
                name=name,
                start=date.fromisoformat(start),
                end=date.fromisoformat(end),
                assessment_start=(
                    date.fromisoformat(assessment[1]) if assessment else None
                ),
                deadline=deadline,
                days=days,
                status=status,
                status_label=STATUS_LABELS[status],
                closed=closed,
                submitted_date=submitted_date,
                timing=timing,
            )
        )
    return sorted(rows, key=lambda r: r["deadline"])


def partition_rows(rows):
    return {
        "upcoming": [
            r
            for r in rows
            if not r["closed"] and r["days"] >= 0 and r["status"] != "resubmission"
        ],
        "attention": [r for r in rows if r["status"] == "resubmission"],
        "recorded": [r for r in rows if r["closed"]],
        "past": [
            r
            for r in rows
            if not r["closed"] and r["days"] < 0 and r["status"] != "resubmission"
        ],
    }


def next_course(rows, today=None):
    today = today or oslo_today()
    eligible = [
        r
        for r in rows
        if not r["closed"] and r["end"] >= today and r["status"] != "resubmission"
    ]
    return min(eligible, key=lambda r: r["start"], default=None)


def save_submission(state, code, status, submitted_date=None, today=None):
    """Validate before changing state; no automatic Noroff synchronization."""
    today = today or oslo_today()
    if code not in {c for c, _, _ in PROGRAM_DEADLINES}:
        raise ValueError("Choose a scheduled course.")
    if status not in STATUS_LABELS or status == "completed":
        raise ValueError("Choose a valid submission status.")
    if submitted_date and submitted_date > today:
        raise ValueError("The submission date cannot be in the future.")
    if status in {"submitted", "passed"} and submitted_date is None:
        raise ValueError("Enter the date you submitted the assessment.")
    records = dict(state.get("assessment_submissions") or {})
    records[code] = {
        "status": status,
        "submitted_date": (
            submitted_date.isoformat()
            if submitted_date and status in {"submitted", "passed"}
            else None
        ),
    }
    state["assessment_submissions"] = records
