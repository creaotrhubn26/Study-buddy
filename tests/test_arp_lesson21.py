"""Verify the three-article workflow, evidence limits and full-app Resolver handoff."""

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
import arp_lesson21 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson21Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_scope_evidence_templates_and_module_separation(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1"],
        )
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertTrue(lesson.TASK_URL.endswith("id=22937&chapterid=81721"))
        self.assertTrue(lesson.LESSON_URL.endswith("id=22937&chapterid=81710"))
        self.assertEqual(
            [a["publisher"] for a in lesson.ARTICLES],
            ["NaturalNews", "BeforeItsNews", "WND"],
        )
        for term in [
            "one-page report",
            "all three",
            "no word count",
            "minimum citation count",
            "not independent corroboration",
            "not proof",
            "submits it",
        ]:
            self.assertIn(term, lesson.BOUNDARY)
        notes = lesson.source_notes_markdown()
        for term in [
            "Atlas Shrugs",
            "GellerReport",
            "Jennie Taer",
            "846%",
            "367",
            "1 October 2022",
            "same FY22",
            "retrospective",
            "not independently resolved",
            "403",
            "not student",
        ]:
            self.assertIn(
                term, notes if term != "not student" else lesson.REVIEW_CONTEXT
            )
        self.assertIn("9.46", lesson.LESSON_CONTENT)
        self.assertIn(".ipynb", lesson.LESSON_CONTENT)
        self.assertIn("does not itself execute", lesson.LESSON_CONTENT)
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        self.assertEqual(
            (
                lesson.TEMPLATE_ROOT / "ARP Task 2.1 Reviewed Source Notes.md"
            ).read_text(),
            notes,
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 2.1 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        with (
            lesson.TEMPLATE_ROOT / "ARP Task 2.1 Claim Verification Matrix.csv"
        ).open() as f:
            rows = list(csv.DictReader(f))
        self.assertEqual([r["Article"] for r in rows], ["A", "A", "B", "B", "C", "C"])
        self.assertTrue(
            all(
                r["Status"] == "Not checked"
                and not r["Exact claim in my words"]
                and not r["My access date"]
                and not r["Qualified judgement"]
                for r in rows
            )
        )
        for visual in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / visual["file"]).read_bytes().startswith(b"\x89PNG")
            )
        modules = curriculum.get_training_modules()
        self.assertEqual(
            [
                l["lesson_number"]
                for l in modules["ARP Module 1: Report Writing"]["lessons"]
            ],
            ["1.1", "1.2", "1.3", "1.4"],
        )
        self.assertEqual(
            [
                l["lesson_number"]
                for l in modules["ARP Module 2: Report-Generating Tools"]["lessons"]
            ],
            ["2.1"],
        )
        self.assertEqual(
            modules["ARP Module 1: Report Writing"]["exercises"][0]["title"],
            "Task 1.1 Report questions",
        )
        guide = curriculum.get_task_guides("2.1")[0]
        guide["steps"].clear()
        self.assertEqual(len(curriculum.get_task_guides("2.1")[0]["steps"]), 7)

    def test_handoff_regular_strict_ai_and_per_task_state(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Check all three articles against dated evidence and qualify your conclusions."
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
                "📚 Lesson 2.1: Report-generating Tools",
                [e.label for e in app.expander],
            )
            self.assertIn(
                "The three articles and dated evidence checks",
                [e.label for e in app.expander],
            )
            note = "My working conclusion: the narrow CBP number is supported; broader causation is not established. I still need to read A and B and check my saved one-page layout."
            next(
                t
                for t in app.text_area
                if t.label == "Your one-page reliability report and verification notes"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 2.1 step"
            ).set_value(3)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state), curriculum.QUESTION_TEMPLATE
            )
            next(
                b for b in app.button if b.label == "Prepare Task 2.1 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            self.assertTrue(
                any(
                    "Auto-detected question style:** Critical reading and source reliability"
                    in m.value
                    for m in app.markdown
                )
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 2.1:", prompt)
            self.assertIn(note, prompt)
            resolver_steps = [
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label.startswith("Choose a Task")
            ]
            self.assertEqual(
                [(s.label, s.value) for s in resolver_steps],
                [("Choose a Task 2.1 step", 3)],
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
            for request in requests:
                system, user = [m["content"] for m in request["messages"][:2]]
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                for text in [
                    "one-page report",
                    "NaturalNews",
                    "BeforeItsNews",
                    "WND",
                    "no word count",
                    "not proof",
                ]:
                    self.assertIn(text, system)
                    self.assertIn(text, user)
                for text in [
                    "current selected step: 4. Trace and check primary evidence",
                    "846%",
                    "367",
                    "same FY22",
                    "retrospective",
                    "Atlas Shrugs",
                    "Jennie Taer",
                    "not independently resolved",
                    "www.cbp.gov",
                    note,
                ]:
                    self.assertIn(text, user)
                self.assertNotIn("handmade-candle business", user)
                self.assertNotIn("45892", user)
                self.assertNotIn("10.62273/SPYC4248", user)

            self.assertIn(
                "STRICT CURRICULUM MODE", requests[1]["messages"][1]["content"]
            )
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if s.label == "Choose a Task 2.1 step"
                and (s.key or "").startswith(arp_ui.RESOLVER_BASE)
            ).set_value(4)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 4)
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label
                    in [
                        "Choose a Task 1.1 step",
                        "Choose a Task 1.2 step",
                        "Choose a Task 1.3 step",
                        "Choose a Task 1.4 step",
                    ]
                )
            )

    def test_training_module_downloads_and_source_isolation(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 2: Report-Generating Tools"
        )
        self.run_app(app)
        self.assertIn(
            "Prepare Task 2.1 in Exam Resolver", [b.label for b in app.button]
        )
        self.assertFalse(
            any(b.label == "Prepare Task 1.4 in Exam Resolver" for b in app.button)
        )
        labels = [d.label for d in app.get("download_button")]
        for _, label, _ in lesson.DOWNLOADS:
            self.assertIn(label, labels)
        self.assertFalse(
            any(
                "Word editing plan" in label or "chart experiment log" in label
                for label in labels
            )
        )


if __name__ == "__main__":
    unittest.main()
