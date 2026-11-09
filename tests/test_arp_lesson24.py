"""Verify role-sensitive communication guidance and the real Lessons/Resolver workflow."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import csv
import json
import os
import sys
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arp_curriculum as curriculum
import arp_lesson23
import arp_lesson24 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson24Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_sources_scope_blank_templates_and_module_order(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4"],
        )
        self.assertTrue(lesson.LESSON_URL.endswith("id=22937&chapterid=81736"))
        self.assertTrue(lesson.TASK_URL.endswith("id=22937&chapterid=81743"))
        self.assertEqual(len(lesson.STEPS), 7)
        for text in [
            "hypothetical team leader",
            "work alone as Anna, Ben or Chris",
            "Anna handles report structure",
            "Chris handles visuals",
            "Ben leads EDA",
            "at least two pages",
            "approximately 800–1000",
            "along with the report",
            "not a hard 1000-word maximum",
            "counting scope is ambiguous",
            "No dataset",
            "No mandatory PowerPoint",
            "report word count",
            "not automatically statistically significant",
        ]:
            self.assertIn(text, lesson.BOUNDARY)
        for filename, content in [
            (lesson.GUIDE["template_file"], lesson.QUESTION_TEMPLATE),
            ("ARP Task 2.4 Report Outline.md", lesson.REPORT_TEMPLATE),
            ("ARP Task 2.4 Speech Manuscript.md", lesson.SPEECH_TEMPLATE),
            ("ARP Task 2.4 Seven Step Guide.md", lesson.guide_markdown()),
        ]:
            self.assertEqual((lesson.TEMPLATE_ROOT / filename).read_text(), content)
        self.assertIn("Evidence needed", lesson.SPEECH_TEMPLATE)
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.4 Dataset Shortlist.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(
            [(r["Proposer"], r["Candidate"]) for r in rows],
            [("Anna", "1"), ("Anna", "2"), ("Chris", "1"), ("Chris", "2")],
        )
        self.assertTrue(
            all(
                not r["Kaggle URL"]
                and not r["Dataset title"]
                and "Confirm who is included" in r["Counting scope note"]
                and r["Status"] == "Not checked"
                for r in rows
            )
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.4 EDA Handoff.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertTrue(
            all(
                not r["Actual finding"]
                and not r["Source file and range"]
                and r["Status"] == "Not checked"
                for r in rows
            )
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.4 Roles and Handoffs.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(
            [r["Role"] for r in rows],
            ["Anna + Chris", "Ben", "Anna", "Chris", "Team leader"],
        )
        self.assertTrue(
            all(
                not r["Actual contribution and evidence"]
                and r["Status"] == "Planned only"
                for r in rows
            )
        )
        for filename, _, _ in lesson.DOWNLOADS:
            self.assertTrue((lesson.TEMPLATE_ROOT / filename).is_file())
        for visual in lesson.ILLUSTRATIONS:
            with Image.open(lesson.ASSET_ROOT / visual["file"]) as im:
                self.assertEqual(im.format, "PNG")
                self.assertGreaterEqual(im.width, 1000)
                im.verify()
        modules = curriculum.get_training_modules()
        self.assertEqual(
            [
                l["lesson_number"]
                for l in modules["ARP Module 1: Report Writing"]["lessons"]
            ],
            ["1.1", "1.2", "1.3", "1.4"],
        )
        m = modules["ARP Module 2: Report-Generating Tools"]
        self.assertEqual(
            [l["lesson_number"] for l in m["lessons"]], ["2.1", "2.2", "2.3", "2.4"]
        )
        self.assertEqual(
            [e["title"] for e in m["exercises"]],
            [
                "Task 2.1 Source reliability",
                "Task 2.2 Nice Ride report",
                "Task 2.3 EDA infographic",
                "Task 2.4 Team communication",
            ],
        )
        self.assertIn("Task 2.1", m["quiz"][0]["question"])
        self.assertIn("Task 2.3", m["quiz"][5]["question"])
        self.assertEqual(m["quiz"][-2]["correct"], 2)
        g = curriculum.get_task_guides("2.4")[0]
        g["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("2.4")[0]["steps"]), 7)

    def test_handoff_regular_strict_ai_and_independent_draft_step(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="As solo Ben, document the EDA evidence and hand it to Anna and Chris; keep unavailable results pending."
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
                "📚 Lesson 2.4: Communication as a Data Analyst",
                [e.label for e in app.expander],
            )
            note = "Route: solo Ben. I have not performed EDA yet. I will inspect the Kaggle source, variables and missing values, then hand actual evidence to Anna and Chris. I am not claiming completed teamwork."
            next(
                t
                for t in app.text_area
                if t.label == "Your route, team plan and speech evidence"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 2.4 step"
            ).set_value(2)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state, arp_lesson23.GUIDE),
                arp_lesson23.QUESTION_TEMPLATE,
            )
            next(
                b for b in app.button if b.label == "Prepare Task 2.4 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            self.assertTrue(
                any(
                    "Auto-detected question style:** Team leadership and evidence-based presentation"
                    in m.value
                    for m in app.markdown
                )
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 2.4:", prompt)
            self.assertIn(note, prompt)
            controls = [
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label.startswith("Choose a Task")
            ]
            self.assertEqual(
                [(s.label, s.value) for s in controls], [("Choose a Task 2.4 step", 2)]
            )
            next(
                b for b in app.button if b.label == "💡 Generate answer with reasoning"
            ).click()
            self.run_app(app)
            next(
                c
                for c in app.checkbox
                if c.label == "📚 Strict curriculum mode (use ONLY the syllabus)"
            ).set_value(True)
            self.run_app(app)
            next(b for b in app.button if b.label == "🔁 Re-generate answer").click()
            self.run_app(app)
            self.assertEqual(len(requests), 2)
            for req in requests:
                system, user = [m["content"] for m in req["messages"][:2]]
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                for t in [
                    "Kaggle",
                    "Anna",
                    "Ben",
                    "Chris",
                    "at least two pages",
                    "approximately 800–1000",
                    "hypothetical team leader",
                    "each team member",
                    "No dataset",
                    "not a hard 1000-word maximum",
                ]:
                    self.assertIn(t, system)
                    self.assertIn(t, user)
                self.assertIn(
                    "current selected step: 3. Assign Ben's EDA and define the handoff",
                    user,
                )
                self.assertIn("Route: solo Ben", user)
                self.assertIn(note, user)
                self.assertNotIn("Mercedes", user)
                self.assertNotIn("NaturalNews", user)
                self.assertNotIn("45892", user)
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label == "Choose a Task 2.4 step"
            ).set_value(6)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            next(
                t
                for t in app.text_area
                if t.label == "Your route, team plan and speech evidence"
            ).set_value(
                "Route: hypothetical team leader. EDA findings pending. I will coordinate handoffs and draft the speech from actual evidence."
            )
            self.run_app(app)
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            next(
                b for b in app.button if b.label == "Prepare Task 2.4 in Exam Resolver"
            ).click()
            self.run_app(app)
            next(b for b in app.button if b.label == "🔁 Re-generate answer").click()
            self.run_app(app)
            self.assertEqual(len(requests), 3)
            self.assertIn(
                "Route: hypothetical team leader",
                requests[-1]["messages"][1]["content"],
            )
            self.assertNotIn("Route: solo Ben", requests[-1]["messages"][1]["content"])
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertIn(
                "Route: hypothetical team leader",
                saved["arp_task_drafts"][lesson.GUIDE["uid"]],
            )
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 6)
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label in ["Choose a Task 2.3 step", "Choose a Task 2.2 step"]
                )
            )

    def test_training_downloads_and_previous_tasks(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 2: Report-Generating Tools"
        )
        self.run_app(app)
        for n in ["2.1", "2.2", "2.3", "2.4"]:
            self.assertIn(
                f"Prepare Task {n} in Exam Resolver", [b.label for b in app.button]
            )
        for _, label, _ in lesson.DOWNLOADS:
            self.assertIn(label, [d.label for d in app.get("download_button")])
        self.assertIn(
            "Choose your role and understand the team deliverables",
            [e.label for e in app.expander],
        )
        self.assertNotIn(
            "Prepare Task 1.4 in Exam Resolver", [b.label for b in app.button]
        )


if __name__ == "__main__":
    unittest.main()
