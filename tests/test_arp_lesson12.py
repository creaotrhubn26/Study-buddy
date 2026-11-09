"""Exercise the real ARP 1.2 workflow and isolation from Task 1.1."""

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
import arp_lesson12 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson12Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_original_file_requirements_and_resources(self):
        guides = curriculum.all_task_guides()
        self.assertEqual(
            [g["lesson_number"] for g in guides], ["1.1", "1.2", "1.3", "1.4"]
        )
        self.assertNotEqual(guides[0]["uid"], guides[1]["uid"])
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertEqual(len(lesson.CHECKS), 5)
        self.assertFalse((lesson.ASSET_ROOT / "source" / "LessonTasks.docx").exists())
        manifest = (lesson.ASSET_ROOT / "source" / "README.md").read_text()
        self.assertIn(lesson.SOURCE_URL, manifest)
        self.assertIn(lesson.SOURCE_SHA256, manifest)
        self.assertIn("Facilisis mauris sit amet massa vitae tortor", lesson.BOUNDARY)
        self.assertIn("working interpretation", lesson.BOUNDARY)
        self.assertIn("cannot certify native DOCX", lesson.BOUNDARY)
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 1.2 Formatting Checks.csv").open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 5)
        self.assertTrue(
            all(
                r["Status"] == "Not checked" and not r["Observed evidence"]
                for r in rows
            )
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 1.2 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        for visual in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / visual["file"]).read_bytes().startswith(b"\x89PNG")
            )
        self.assertEqual(
            curriculum.get_course_lessons()[1]["source_url"], lesson.LESSON_URL
        )
        self.assertEqual(curriculum.guide_markdown(guides[1]), lesson.guide_markdown())
        changed = curriculum.get_task_guides("1.2")[0]
        changed["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("1.2")[0]["steps"]), 7)

    def test_task12_handoff_ai_context_and_independent_state(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Check the saved Word file; Newsprint is not yet verified."
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
                "📚 Lesson 1.2: Writing Styles", [e.label for e in app.expander]
            )
            self.assertTrue(
                any(
                    link.proto.url == lesson.SOURCE_URL
                    for link in app.get("link_button")
                )
            )
            note = "Word web: Newsprint not available yet. My paragraph anchor is Facilisis mauris. I have not checked the saved file."
            next(
                t
                for t in app.text_area
                if t.label == "Your Word editing plan and check notes"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 1.2 step"
            ).set_value(3)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state), curriculum.QUESTION_TEMPLATE
            )
            next(
                b for b in app.button if b.label == "Prepare Task 1.2 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 1.2:", prompt)
            self.assertIn(note, prompt)
            resolver_step = next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.2 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            )
            self.assertEqual(resolver_step.value, 3)
            self.assertFalse(
                any(
                    s.label == "Choose a Task 1.1 step"
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
                self.assertIn(
                    "Task 1.2 requires editing the supplied LessonTasks.docx", system
                )
                self.assertIn("cannot certify native DOCX", system)
                self.assertIn(
                    "current selected step: 4. Insert the break after the confirmed paragraph",
                    user,
                )
                self.assertIn(note, user)
                self.assertIn("Newsprint", user)
                self.assertIn("Landscape", user)
                self.assertNotIn("Student question-plan draft", user)
                self.assertNotIn("handmade-candle business", user)
                self.assertNotIn("snow-free bobsled", user)
            self.assertIn(
                "STRICT CURRICULUM MODE", requests[1]["messages"][1]["content"]
            )
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.2 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            ).set_value(6)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertEqual(len(requests), 2)
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertTrue(
                any("earlier question or dataset" in i.value for i in app.info)
            )
            self.assertTrue(
                all(
                    s.value == 6
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.2 step"
                )
            )
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.1 step"
                )
            )
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 6)

    def test_training_has_task12_and_separate_task11(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 1: Report Writing"
        )
        self.run_app(app)
        for number in ("1.1", "1.2"):
            self.assertIn(
                f"Prepare Task {number} in Exam Resolver", [b.label for b in app.button]
            )
        self.assertTrue(
            any(link.proto.url == lesson.SOURCE_URL for link in app.get("link_button"))
        )
        for label in (
            "Download five formatting checks (CSV)",
            "Download Word editing plan (Markdown)",
        ):
            self.assertIn(label, [d.label for d in app.get("download_button")])


if __name__ == "__main__":
    unittest.main()
