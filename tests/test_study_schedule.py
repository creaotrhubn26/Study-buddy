from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import study_buddy_state as storage
from study_schedule import next_course, partition_rows, save_submission, schedule_rows

TODAY = date(2026, 10, 16)
CATALOG = [
    {"name": "Data Visualisation", "code": "FI1BBDV75"},
    {"name": "Analysis Reporting", "code": "FI1BBAR05"},
]


class ScheduleTests(unittest.TestCase):
    def test_calendar_passage_never_means_submitted_or_passed(self):
        rows = schedule_rows(today=TODAY)
        self.assertTrue(all(r["status"] == "not_recorded" for r in rows))
        past = partition_rows(rows)["past"]
        self.assertTrue(past)
        self.assertTrue(all("No submission recorded" in r["timing"] for r in past))
        self.assertEqual(
            [r["code"] for r in partition_rows(rows)["upcoming"]], ["DVS", "ARP", "EP1"]
        )

    def test_submitted_assessment_does_not_remain_urgent_and_next_course_advances(self):
        state = {}
        save_submission(state, "DVS", "submitted", TODAY, today=TODAY)
        rows = schedule_rows(
            state["assessment_submissions"], today=TODAY, catalog=CATALOG
        )
        groups = partition_rows(rows)
        self.assertEqual([r["code"] for r in groups["upcoming"]], ["ARP", "EP1"])
        self.assertEqual(
            groups["recorded"][0]["status_label"], "Submitted · Awaiting grade"
        )
        self.assertNotIn("left", groups["recorded"][0]["timing"])
        self.assertEqual(next_course(rows, TODAY)["full_code"], "FI1BBAR05")

    def test_record_persists_across_reload_and_can_be_corrected(self):
        with (
            TemporaryDirectory() as tmp,
            patch.object(storage, "STATE_FILE", Path(tmp) / "state.json"),
        ):
            state = {}
            save_submission(state, "DVS", "submitted", TODAY, today=TODAY)
            self.assertTrue(storage.save_persisted_state(state))
            loaded = {}
            storage.load_persisted_state(loaded)
            self.assertEqual(loaded, state)
            save_submission(loaded, "DVS", "not_recorded", today=TODAY)
            rows = schedule_rows(loaded["assessment_submissions"], today=TODAY)
            self.assertEqual(next_course(rows, TODAY)["code"], "DVS")

    def test_completion_flags_and_explicit_status_are_distinct(self):
        for completion in ["DVS", "FI1BBDV75"]:
            rows = schedule_rows(completed=[completion], today=TODAY, catalog=CATALOG)
            self.assertEqual(
                next(r for r in rows if r["code"] == "DVS")["status"], "completed"
            )
            explicit = schedule_rows(
                {"DVS": {"status": "not_recorded"}},
                [completion],
                today=TODAY,
                catalog=CATALOG,
            )
            self.assertEqual(
                next(r for r in explicit if r["code"] == "DVS")["status"],
                "not_recorded",
            )

    def test_invalid_save_does_not_mutate_state(self):
        state = {}
        for code, status, day in [
            ("bad", "submitted", TODAY),
            ("DVS", "completed", TODAY),
            ("DVS", "submitted", None),
            ("DVS", "submitted", date(2026, 10, 17)),
        ]:
            with self.assertRaises(ValueError):
                save_submission(state, code, status, day, today=TODAY)
            self.assertEqual(state, {})

    def test_filters_empty_states_due_today_and_resubmission(self):
        self.assertEqual(schedule_rows(names=set(), today=TODAY), [])
        self.assertIsNone(next_course([], TODAY))
        selected = schedule_rows(names={"Analysis Reporting"}, today=TODAY)
        self.assertEqual([r["code"] for r in selected], ["ARP"])
        row = next(
            r for r in schedule_rows(today=date(2026, 10, 18)) if r["code"] == "DVS"
        )
        self.assertEqual(row["timing"], "Due today at 23:59")
        row = next(
            r
            for r in schedule_rows(
                {"DVS": {"status": "resubmission"}}, today=date(2026, 10, 19)
            )
            if r["code"] == "DVS"
        )
        self.assertFalse(row["closed"])
        self.assertIn("Check your resit instructions", row["timing"])
        groups = partition_rows([row])
        self.assertEqual(groups["upcoming"], [])
        self.assertEqual(groups["past"], [])
        self.assertEqual(groups["attention"], [row])

    def test_failed_write_is_reported(self):
        with patch.object(
            storage, "STATE_FILE", Path("/nonexistent-study-buddy-dir/state.json")
        ):
            self.assertFalse(storage.save_persisted_state({}))

    def test_failed_save_keeps_previous_file(self):
        with (
            TemporaryDirectory() as tmp,
            patch.object(storage, "STATE_FILE", Path(tmp) / "state.json"),
        ):
            self.assertTrue(
                storage.save_persisted_state({"study_notes": {"note": "Keep me"}})
            )
            previous = storage.STATE_FILE.read_bytes()
            with patch.object(Path, "replace", side_effect=OSError("read-only disk")):
                self.assertFalse(
                    storage.save_persisted_state({"study_notes": {"note": "Changed"}})
                )
            self.assertEqual(storage.STATE_FILE.read_bytes(), previous)
            self.assertEqual(list(Path(tmp).iterdir()), [storage.STATE_FILE])


if __name__ == "__main__":
    unittest.main()
