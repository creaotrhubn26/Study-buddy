"""Check ARP provenance and the real Lessons to Exam Resolver path."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import csv
import json
import os
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arp_curriculum as c
import arp_ui
from streamlit.testing.v1 import AppTest


class ARPLesson11Tests(unittest.TestCase):
    def setUp(self):
        self.old = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)

    def tearDown(self):
        os.chdir(self.old)
        self.temp.cleanup()

    def run_app(self, app):
        app.run(timeout=90)
        self.assertFalse(app.exception, [e.message for e in app.exception])
        return app

    def app(self, page="Learn & Practice"):
        app = AppTest.from_file(str(ROOT / "app.py"))
        for key, value in dict(
            nav_section="Learning",
            nav_page=page,
            last_selected_course=c.COURSE_NAME,
            lp_selected_course=f"{c.COURSE_CODE} - {c.COURSE_NAME}",
            tc_course_filter=f"{c.COURSE_CODE} - {c.COURSE_NAME}",
        ).items():
            app.session_state[key] = value
        return self.run_app(app)

    def test_source_scope_templates_and_real_images(self):
        lesson = c.get_course_lessons()[0]
        self.assertEqual(lesson["source_checked_on"], "2026-11-09")
        self.assertEqual(lesson["source_url"], c.LESSON_URL)
        self.assertEqual(len(c.STEPS), 7)
        self.assertNotEqual(c.get_task_guides("1.2")[0]["uid"], c.GUIDE["uid"])
        for fact in [
            "handmade",
            "Facebook",
            "Instagram",
            "TikTok",
            "six months",
            "posting schedule",
            "content type",
            "No dataset",
        ]:
            self.assertIn(fact, c.BOUNDARY)
        self.assertEqual(
            (c.TEMPLATE_ROOT / c.GUIDE["template_file"]).read_text(),
            c.QUESTION_TEMPLATE,
        )
        matrix = list(
            csv.reader((c.TEMPLATE_ROOT / "ARP Task 1.1 Evidence Matrix.csv").open())
        )
        self.assertEqual(len(matrix), 16)
        self.assertTrue(all(len(row) == 11 for row in matrix))
        self.assertTrue(all(not row[2] for row in matrix[1:]))
        for image in c.ILLUSTRATIONS:
            self.assertTrue(
                (c.ASSET_ROOT / image["file"]).read_bytes().startswith(b"\x89PNG")
            )
        self.assertIn("not the official solution", c.guide_markdown())
        guide = c.get_task_guides("1.1")[0]
        guide["steps"].append("changed")
        self.assertEqual(len(c.get_task_guides("1.1")[0]["steps"]), 7)

    def test_lesson_handoff_selected_step_and_regular_strict_ai_context(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Review the question order and metric definitions."
                                )
                            )
                        ]
                    )
                ]
            )

        fake = SimpleNamespace(
            chat=SimpleNamespace(completions=SimpleNamespace(create=complete))
        )
        env = {"OPENAI_API_KEY": "offline-test", "AI_PROVIDER": "openai"}
        env["_STUDY_BUDDY_INITIAL_ENV_KEYS"] = json.dumps(list(os.environ) + list(env))
        with patch.dict(os.environ, env), patch("openai.OpenAI", return_value=fake):
            app = self.app()
            self.assertIn(
                "📚 Lesson 1.1: Report Writing", [e.label for e in app.expander]
            )
            self.assertIn(
                "Download question evidence matrix (CSV)",
                [d.label for d in app.get("download_button")],
            )
            question = "How does organic engagement per post differ by weekday within Instagram?"
            next(
                t
                for t in app.text_area
                if t.label == "Your report questions and evidence plan"
            ).set_value(question)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 1.1 step"
            ).set_value(4)
            self.run_app(app)
            next(
                b for b in app.button if b.label == "Prepare Task 1.1 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(len(requests), 0)
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 1.1:", prompt)
            self.assertIn(question, prompt)
            self.assertEqual(
                app.session_state["lp_selected_course"],
                "FI1BBAR05 - Analysis Reporting",
            )
            resolver_step = next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.1 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            )
            self.assertEqual(resolver_step.value, 4)
            next(
                b for b in app.button if b.label == "💡 Generate answer with reasoning"
            ).click()
            self.run_app(app)
            next(
                x
                for x in app.checkbox
                if x.label == "📚 Strict curriculum mode (use ONLY the syllabus)"
            ).set_value(True)
            self.run_app(app)
            next(b for b in app.button if b.label == "🔁 Re-generate answer").click()
            self.run_app(app)
            self.assertEqual(len(requests), 2)
            for request in requests:
                user = request["messages"][1]["content"]
                system = request["messages"][0]["content"]
                self.assertIn(
                    "current selected step: 5. Examine the posting schedule", user
                )
                self.assertIn(question, user)
                self.assertIn("No dataset", user)
                self.assertIn("without paid advertising", user)
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                self.assertIn("Task 1.1 asks for report questions", system)
                self.assertNotIn("snow-free bobsled", user)
            self.assertIn(
                "STRICT CURRICULUM MODE", requests[1]["messages"][1]["content"]
            )
            # Changing a step refreshes both visible copies and invalidates earlier answers.
            resolver_step = next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.1 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            )
            resolver_step.set_value(5)
            self.run_app(app)
            self.assertTrue(
                all(
                    s.value == 5
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.1 step"
                )
            )
            self.assertEqual(len(requests), 2)
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][c.GUIDE["uid"]], question)
            self.assertEqual(saved["arp_task_steps"][c.GUIDE["uid"]], 5)

    def test_training_resources_available(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 1: Report Writing"
        )
        self.run_app(app)
        self.assertIn(
            "Prepare Task 1.1 in Exam Resolver", [b.label for b in app.button]
        )
        self.assertIn(
            "Download question plan (Markdown)",
            [d.label for d in app.get("download_button")],
        )


if __name__ == "__main__":
    unittest.main()
