import json
from pathlib import Path

STATE_FILE = Path(".study_buddy_state.json")

PERSIST_KEYS = [
    "completed_courses",
    "knowledge_progress",
    "skills_progress",
    "competence_progress",
    "training_progress",
    "quiz_scores",
    "quiz_answers",
    "show_exercise_answer",
    "study_notes",
    "flashcards",
    "flashcard_stats",
    "exam_mode",
    "exam_questions",
    "exam_answers",
    "code_snippets",
    "code_snippet_favorites",
    "study_sessions",
    "study_time_by_course",
    "important_dates",
    "last_page",
    "last_selected_course",
    "last_selected_topic",
    "nav_section",
    "nav_page",
    "tc_semester_filter",
    "tc_course_filter",
    "tc_topic",
    "lp_selected_course"
]

PROGRAM_DEADLINES = [
    ("DAF", "Data Analysis Fundamentals", "2025-11-09"),
    ("SPF", "Spreadsheet Fundamentals", "2025-11-30"),
    ("DDM", "Data Driven Decision-Making", "2026-01-11"),
    ("STT", "Statistical Tools", "2026-02-01"),
    ("SP1", "Semester Project", "2026-03-01"),
    ("EVO", "Evaluation of Outcomes", "2026-05-03"),
    ("DVS", "Data Visualisation", "2026-06-07"),
    ("ARP", "Analysis Reporting", "2026-08-30"),
    ("EP1", "Exam Project 1", "2026-10-11"),
]

COURSE_PROGRESSION_MAP = {
    "Data Analysis Fundamentals": ("DAF", "2025-11-03", "2025-11-09"),
    "Spreadsheet Fundamentals": ("SPF", "2025-11-24", "2025-11-30"),
    "Data Driven Decision-Making": ("DDM", "2026-01-05", "2026-01-11"),
    "Statistical Tools": ("STT", "2026-01-26", "2026-02-01"),
    "Semester Project 1": ("SP1", "2026-02-23", "2026-03-01"),
    "Evaluation of Outcomes": ("EVO", "2026-04-27", "2026-05-03"),
    "Data Visualisation": ("DVS", "2026-06-01", "2026-06-07"),
    "Analysis Reporting": ("ARP", "2026-08-24", "2026-08-30"),
}


def load_persisted_state(session_state):
    if not STATE_FILE.exists():
        return
    try:
        payload = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return

    if not isinstance(payload, dict):
        return

    for key in PERSIST_KEYS:
        if key in payload and key not in session_state:
            session_state[key] = payload[key]


def save_persisted_state(session_state):
    payload = {key: session_state.get(key) for key in PERSIST_KEYS if key in session_state}
    try:
        STATE_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass
