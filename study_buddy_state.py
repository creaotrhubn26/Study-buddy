import json
import os
import tempfile
from pathlib import Path


def _resolve_state_file():
    """Where progress is persisted.

    Set STUDY_BUDDY_STATE_FILE to a path on durable storage when deploying;
    otherwise the file lives next to this module. Anchoring to the module
    directory rather than the process working directory matters because
    Streamlit can be launched from anywhere, and a relative path would
    silently start every session from an empty state file.
    """
    configured = str(os.getenv("STUDY_BUDDY_STATE_FILE", "") or "").strip()
    if configured:
        return Path(configured).expanduser()
    return Path(__file__).resolve().parent / ".study_buddy_state.json"


STATE_FILE = _resolve_state_file()

# Set by save_persisted_state so the UI can surface a write failure instead of
# losing the user's progress silently.
LAST_SAVE_ERROR = None

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
    "lp_selected_course",
    "custom_lesson_glossary",
    "custom_glossary",
    "resolver_answer_history",
]

PROGRAM_DEADLINES = [
    ("IC", "Introduction Course", "2026-01-11"),
    ("DAF", "Data Analysis Fundamentals", "2026-02-01"),
    ("SPF", "Spreadsheet Fundamentals", "2026-02-22"),
    ("DDM", "Data Driven Decision-Making", "2026-03-22"),
    ("STT", "Statistical Tools", "2026-04-19"),
    ("SP1", "Semester Project 1", "2026-05-17"),
    ("EVO", "Evaluation of Outcomes", "2026-09-13"),
    ("DVS", "Data Visualisation", "2026-10-18"),
    ("ARP", "Analysis Reporting", "2026-11-08"),
    ("EP1", "Exam Project 1", "2026-12-20"),
]

COURSE_PROGRESSION_MAP = {
    "Data Analysis Fundamentals": ("DAF", "2026-01-26", "2026-02-01"),
    "Spreadsheet Fundamentals": ("SPF", "2026-02-16", "2026-02-22"),
    "Data Driven Decision-Making": ("DDM", "2026-03-16", "2026-03-22"),
    "Statistical Tools": ("STT", "2026-04-13", "2026-04-19"),
    "Semester Project 1": ("SP1", "2026-05-11", "2026-05-17"),
    "Evaluation of Outcomes": ("EVO", "2026-09-07", "2026-09-13"),
    "Data Visualisation": ("DVS", "2026-10-12", "2026-10-18"),
    "Analysis Reporting": ("ARP", "2026-11-02", "2026-11-08"),
    "Exam Project 1": ("EP1", "2026-12-14", "2026-12-20"),
}

STUDY_PATH_JAN2026 = [
    ("IC", "Introduction Course", "2026-01-05", "2026-01-11"),
    ("DAF", "Data Analysis Fundamentals", "2026-01-12", "2026-02-01"),
    ("SPF", "Spreadsheet Fundamentals", "2026-02-02", "2026-02-22"),
    ("DDM", "Data Driven Decision-Making", "2026-02-23", "2026-03-22"),
    ("STT", "Statistical Tools", "2026-03-23", "2026-04-19"),
    ("SP1", "Semester Project 1", "2026-04-20", "2026-05-17"),
    ("EVO", "Evaluation of Outcomes", "2026-05-18", "2026-09-13"),
    ("DVS", "Data Visualisation", "2026-09-14", "2026-10-18"),
    ("ARP", "Analysis Reporting", "2026-10-19", "2026-11-08"),
    ("EP1", "Exam Project 1", "2026-11-09", "2026-12-20"),
]


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
    """Persist the tracked session keys. Returns True on success.

    The write goes to a temporary file in the same directory and is then
    moved into place, so an interrupted save cannot leave a half-written
    file that the next load would discard as corrupt.
    """
    global LAST_SAVE_ERROR

    payload = {key: session_state.get(key) for key in PERSIST_KEYS if key in session_state}
    serialized = json.dumps(payload, ensure_ascii=False, indent=2)

    temp_path = None
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        handle = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=str(STATE_FILE.parent),
            prefix=STATE_FILE.name + ".",
            suffix=".tmp",
            delete=False,
        )
        with handle:
            temp_path = Path(handle.name)
            handle.write(serialized)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, STATE_FILE)
        temp_path = None
        LAST_SAVE_ERROR = None
        return True
    except Exception as error:
        LAST_SAVE_ERROR = f"{type(error).__name__}: {error}"
        return False
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except OSError:
                pass
