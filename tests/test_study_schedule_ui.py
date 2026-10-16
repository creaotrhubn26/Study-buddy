from datetime import date
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
HARNESS = f"""
import sys
sys.path.insert(0, {str(ROOT)!r})
import streamlit as st
from study_schedule_ui import render_schedule, render_course_reminder, render_timeline
catalog=[{{"name":"Data Visualisation","code":"FI1BBDV75"}},{{"name":"Analysis Reporting","code":"FI1BBAR05"}}]
selected=st.selectbox('Test filter', ['All', 'Analysis Reporting', 'No match'])
names=None if selected=='All' else {{selected}}
render_schedule(catalog,names,key='test')
render_course_reminder('Data Visualisation',catalog)
render_timeline(catalog)
"""


class ScheduleUITests(unittest.TestCase):
    def setUp(self):
        for name in ["study_schedule.oslo_today", "study_schedule_ui.oslo_today"]:
            freeze = patch(name, return_value=date(2026, 10, 16))
            freeze.start()
            self.addCleanup(freeze.stop)

    def run_app(self, app):
        app.run(timeout=30)
        self.assertFalse(app.exception, [e.message for e in app.exception])
        return app

    def select(self, app, label):
        return next(s for s in app.selectbox if s.label == label)

    def button(self, app, label):
        return next(b for b in app.button if b.label == label)

    def test_submit_rerender_reminder_and_course_navigation(self):
        app = self.run_app(AppTest.from_string(HARNESS))
        self.select(app, "Assessment").select("DVS")
        self.run_app(app)
        self.select(app, "Submission status").select("submitted")
        self.run_app(app)
        with patch("study_schedule_ui.save_persisted_state", return_value=True):
            self.button(app, "Save submission status").click()
            self.run_app(app)
        self.assertEqual(
            app.session_state["assessment_submissions"]["DVS"]["status"], "submitted"
        )
        texts = "\n".join(m.value for m in app.markdown)
        self.assertIn("Submitted · Awaiting grade", texts)
        self.assertTrue(
            any(
                "Analysis Reporting" in m.value and "STARTING NEXT" in m.value
                for m in app.markdown
            )
        )
        self.button(app, "Open course").click()
        self.run_app(app)
        self.assertEqual(app.session_state["nav_page"], "Learn & Practice")
        self.assertEqual(
            app.session_state["lp_selected_course"], "FI1BBAR05 - Analysis Reporting"
        )

    def test_failed_save_and_filter_empty_state(self):
        app = self.run_app(AppTest.from_string(HARNESS))
        self.select(app, "Assessment").select("DVS")
        self.run_app(app)
        self.select(app, "Submission status").select("submitted")
        self.run_app(app)
        with patch("study_schedule_ui.save_persisted_state", return_value=False):
            self.button(app, "Save submission status").click()
            self.run_app(app)
        self.assertTrue(app.error)
        self.assertEqual(app.session_state["assessment_submissions"], {})
        self.select(app, "Test filter").select("No match")
        self.run_app(app)
        self.assertTrue(any("No upcoming deadlines" in i.value for i in app.info))
        self.assertFalse(any(b.label == "Open course" for b in app.button))
        self.select(app, "Test filter").select("Analysis Reporting")
        self.run_app(app)
        cards = [m.value for m in app.markdown if "Deadline <strong>" in m.value]
        self.assertEqual(
            sum("Data Visualisation" in m for m in cards), 1
        )  # Only the independent lesson reminder.
        self.assertTrue(any("Analysis Reporting" in m for m in cards))


if __name__ == "__main__":
    unittest.main()
