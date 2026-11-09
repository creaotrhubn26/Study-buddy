"""Exercise the exact four-question ARP workflow in the full Streamlit app."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import csv
import json
import os
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arp_curriculum as curriculum
import arp_lesson13
import arp_lesson14 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson14Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_four_questions_templates_and_source_boundaries(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4"],
        )
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertEqual(len(lesson.QUESTION_BRIEFS), 4)
        self.assertEqual(
            lesson.TARGET_EDITS,
            [("Male users", "March", 45892), ("Female users", "December", 91364)],
        )
        for term in [
            "denominator 3",
            "2a following outside",
            "No values of a, b or c",
            "not explicitly link",
            "independent baseline",
            "separate editable copy",
            "John/30/New York",
            "Alice/25/Los Angeles",
            "Bob/28/Chicago",
            "separate lists of figures, tables and equations",
            "Desktop Office",
            "cannot certify native",
        ]:
            self.assertIn(term, lesson.BOUNDARY)
        self.assertEqual(len(lesson.RESOURCE_LINKS), 7)
        self.assertTrue(
            all(
                url.startswith(
                    "https://learning.noroff.no/pluginfile.php/33187/mod_book/chapter/81707/"
                )
                for _, url in lesson.RESOURCE_LINKS
            )
        )
        self.assertTrue(
            all("solution" not in url.lower() for _, url in lesson.RESOURCE_LINKS)
        )
        self.assertEqual(
            curriculum.get_course_lessons()[3]["source_url"], lesson.LESSON_URL
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 1.4 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 1.4 Chart Experiments.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(
            [
                (
                    r["Question"],
                    r["Series"],
                    r["Month"],
                    int(r["Target external value"]),
                )
                for r in rows
            ],
            [(q, s, m, n) for q in ["Q1", "Q2"] for s, m, n in lesson.TARGET_EDITS],
        )
        self.assertTrue(
            all(
                r["Status"] == "Not checked"
                and not r["Observed Word chart data after edit"]
                and not r["External baseline"]
                for r in rows
            )
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 1.4 Table Data.csv").open() as f:
            table = list(csv.reader(f))
        self.assertEqual(
            table,
            [
                ["Name", "Age", "Location"],
                ["John", "30", "New York"],
                ["Alice", "25", "Los Angeles"],
                ["Bob", "28", "Chicago"],
            ],
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 1.4 Caption Register.csv").open() as f:
            register = list(csv.DictReader(f))
        self.assertEqual(
            [r["Caption label"] for r in register], ["Figure", "Table", "Equation"]
        )
        self.assertTrue(
            all(
                not r["Actual caption text or number"]
                and r["Entry and page checked"] == "Not checked"
                for r in register
            )
        )
        for visual in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / visual["file"]).read_bytes().startswith(b"\x89PNG")
            )
        module = curriculum.get_training_modules()["ARP Module 1: Report Writing"]
        self.assertEqual(module["exercises"][0]["title"], "Task 1.1 Report questions")
        self.assertIn("Task 1.1 deliverable", module["quiz"][0]["question"])
        guide = curriculum.get_task_guides("1.4")[0]
        guide["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("1.4")[0]["steps"]), 7)

    def test_handoff_regular_strict_ai_and_independent_observations(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Record native-file observations and confirm the equation grouping with your tutor."
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
                "📚 Lesson 1.4: Incorporating Visualisations",
                [e.label for e in app.expander],
            )
            self.assertIn(
                "Original Task 1.4 files on Noroff", [e.label for e in app.expander]
            )
            self.assertIn(
                "Equation image: what needs clarification",
                [e.label for e in app.expander],
            )
            note = "Q1 and Q2 are not yet tested. I have Word web. The first equation has denominator 3; I need to confirm the slash grouping. Do not mark expected results as observed."
            next(
                t
                for t in app.text_area
                if t.label == "Your Office workflow and observed results"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 1.4 step"
            ).set_value(4)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state), curriculum.QUESTION_TEMPLATE
            )
            self.assertEqual(
                arp_ui.draft(app.session_state, arp_lesson13.GUIDE),
                arp_lesson13.QUESTION_TEMPLATE,
            )
            next(
                b for b in app.button if b.label == "Prepare Task 1.4 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 1.4:", prompt)
            self.assertIn(note, prompt)
            self.assertEqual(
                next(
                    s
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.4 step"
                    and s.key.startswith(arp_ui.RESOLVER_BASE)
                ).value,
                4,
            )
            self.assertFalse(
                any(
                    s.label
                    in {
                        "Choose a Task 1.1 step",
                        "Choose a Task 1.2 step",
                        "Choose a Task 1.3 step",
                    }
                    and s.key.startswith(arp_ui.RESOLVER_BASE)
                    for s in app.selectbox
                )
            )
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
                system, user = [m["content"] for m in request["messages"][:2]]
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                for text in [
                    "45892",
                    "91364",
                    "denominator 3",
                    "No values of a, b or c",
                    "not explicitly link",
                    "cannot certify native",
                ]:
                    self.assertIn(text, system)
                    self.assertIn(text, user)
                self.assertIn(
                    "current selected step: 5. Q3 — enter and inspect the supplied equations",
                    user,
                )
                self.assertIn(note, user)
                self.assertIn("Original task resources on Noroff", user)
                self.assertIn("LessonTasksChart%20%281%29.xlsx", user)
                self.assertIn("LessonTasksChart%20%282%29.xlsx", user)
                self.assertIn("Lessontaskincorporatingvisualisations-1.jpg", user)
                self.assertNotIn("handmade-candle business", user)
                self.assertNotIn("10.62273/SPYC4248", user)
            self.assertIn(
                "STRICT CURRICULUM MODE", requests[1]["messages"][1]["content"]
            )
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.4 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            ).set_value(5)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            self.assertTrue(
                all(
                    s.value == 5
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.4 step"
                )
            )
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label
                    in {
                        "Choose a Task 1.1 step",
                        "Choose a Task 1.2 step",
                        "Choose a Task 1.3 step",
                    }
                )
            )
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 5)

    def test_training_downloads_and_previous_tasks(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 1: Report Writing"
        )
        self.run_app(app)
        for number in ["1.1", "1.2", "1.3", "1.4"]:
            self.assertIn(
                f"Prepare Task {number} in Exam Resolver", [b.label for b in app.button]
            )
        for label in [
            "Download Office workflow and check log (Markdown)",
            "Download chart experiment log (CSV)",
            "Download caption and list register (CSV)",
            "Download Q3 table data (CSV)",
            "Download seven-step visuals guide (Markdown)",
        ]:
            self.assertIn(label, [d.label for d in app.get("download_button")])


if __name__ == "__main__":
    unittest.main()
