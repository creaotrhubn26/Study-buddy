"""Check real ARP 1.3 source selection, handoff and citation context."""

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
import arp_lesson12
import arp_lesson13 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson13Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_brief_templates_sources_and_illustrations(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2"],
        )
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertEqual(sum(p[1] for p in lesson.PARAGRAPHS), 500)
        for phrase in [
            "500-word overview",
            "at least four citations",
            "not explicitly four distinct sources",
            "Harvard",
            "Google Scholar",
            "No Harvard institutional variant",
            "John Doe",
            "Never fabricate",
        ]:
            self.assertIn(phrase, lesson.BOUNDARY)
        self.assertEqual(
            curriculum.get_course_lessons()[2]["source_url"], lesson.LESSON_URL
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 1.3 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        self.assertEqual(
            (
                lesson.TEMPLATE_ROOT / "ARP Task 1.3 Harvard Source Starter.md"
            ).read_text(),
            lesson.source_cards_markdown(),
        )
        with (
            lesson.TEMPLATE_ROOT / "ARP Task 1.3 Citation Evidence Matrix.csv"
        ).open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 4)
        self.assertTrue(
            all(
                r["Actual access or reading status"] == "Not read"
                and not r["Supporting passage or real locator"]
                for r in rows
            )
        )
        self.assertEqual(len(lesson.SOURCES), 3)
        self.assertIn("10.1109/TVCG.2012.219", lesson.SOURCES[0]["reference"])
        self.assertIn("10.62273/SPYC4248", lesson.SOURCES[1]["reference"])
        self.assertIn("10.1080/08874417.2022.2070799", lesson.SOURCES[2]["reference"])
        for source in lesson.SOURCES:
            self.assertTrue(source["url"].startswith("https://"))
            self.assertIn("abstract", source["checked"])
        for visual in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / visual["file"]).read_bytes().startswith(b"\x89PNG")
            )
        # Preserve earlier exercise and quiz positions used by existing progress state.
        module = curriculum.get_training_modules()["ARP Module 1: Report Writing"]
        self.assertEqual(module["exercises"][0]["title"], "Task 1.1 Report questions")
        self.assertIn("Task 1.1 deliverable", module["quiz"][0]["question"])
        other = curriculum.get_task_guides("1.3")[0]
        other["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("1.3")[0]["steps"]), 7)

    def test_handoff_and_regular_strict_source_context(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Check four citation placements and their supporting passages. Your overview is not yet complete."
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
                "📚 Lesson 1.3: Referencing Styles and Tools",
                [e.label for e in app.expander],
            )
            self.assertTrue(
                any(
                    link.proto.url == lesson.SCHOLAR_URL
                    for link in app.get("link_button")
                )
            )
            note = "My workplace overview is not finished. I read only the Kandel abstract; S2 and S3 are not read. Please help plan four citation placements without claiming full-text access."
            next(
                t
                for t in app.text_area
                if t.label == "Your workplace overview and source notes"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 1.3 step"
            ).set_value(4)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state), curriculum.QUESTION_TEMPLATE
            )
            self.assertEqual(
                arp_ui.draft(app.session_state, arp_lesson12.GUIDE),
                arp_lesson12.QUESTION_TEMPLATE,
            )
            next(
                b for b in app.button if b.label == "Prepare Task 1.3 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 1.3:", prompt)
            self.assertIn(note, prompt)
            resolver = next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.3 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            )
            self.assertEqual(resolver.value, 4)
            self.assertFalse(
                any(
                    s.label in {"Choose a Task 1.1 step", "Choose a Task 1.2 step"}
                    and s.key.startswith(arp_ui.RESOLVER_BASE)
                    for s in app.selectbox
                )
            )
            self.assertIn(
                "Download citation evidence matrix (CSV)",
                [d.label for d in app.get("download_button")],
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
                self.assertIn("500-word overview", system)
                self.assertIn("not explicitly four distinct sources", system)
                self.assertIn("Never fabricate", system)
                self.assertIn(
                    "current selected step: 5. Draft and insert Harvard citations", user
                )
                self.assertIn(note, user)
                self.assertIn("10.1109/TVCG.2012.219", user)
                self.assertIn("10.62273/SPYC4248", user)
                self.assertIn("10.1080/08874417.2022.2070799", user)
                self.assertIn("not proof of student reading", user)
                self.assertNotIn("handmade-candle business", user)
                self.assertNotIn("Facilisis mauris", user)
            self.assertIn(
                "STRICT CURRICULUM MODE", requests[1]["messages"][1]["content"]
            )
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 1.3 step"
                and s.key.startswith(arp_ui.RESOLVER_BASE)
            ).set_value(6)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            self.assertTrue(
                all(
                    s.value == 6
                    for s in app.selectbox
                    if s.label == "Choose a Task 1.3 step"
                )
            )
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label in {"Choose a Task 1.1 step", "Choose a Task 1.2 step"}
                )
            )
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 6)

    def test_training_resources_available(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 1: Report Writing"
        )
        self.run_app(app)
        self.assertIn(
            "Prepare Task 1.3 in Exam Resolver", [b.label for b in app.button]
        )
        for label in [
            "Download workplace overview template (Markdown)",
            "Download citation evidence matrix (CSV)",
            "Download seven-step referencing guide (Markdown)",
            "Download Harvard source starter (Markdown)",
        ]:
            self.assertIn(label, [d.label for d in app.get("download_button")])


if __name__ == "__main__":
    unittest.main()
