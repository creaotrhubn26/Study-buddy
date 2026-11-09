"""Original practice content, independent progress and real app/Resolver integration."""

from collections import Counter
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import json
import os
import sys
import tempfile
import unittest
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from streamlit.testing.v1 import AppTest
import arp_quiz_bank as bank
import arp_curriculum
import study_buddy_state


class ARPQuizBankTests(unittest.TestCase):
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
        for k, v in dict(
            nav_section="Assessment" if page == "Exam Simulator" else "Learning",
            nav_page=page,
            last_selected_course="Analysis Reporting",
            lp_selected_course="FI1BBAR05 - Analysis Reporting",
        ).items():
            app.session_state[k] = v
        return self.run_app(app)

    def test_original_content_sources_images_and_download(self):
        qs = bank.get_questions()
        self.assertEqual(len(qs), 16)
        self.assertEqual(len({q["id"] for q in qs}), 16)
        self.assertEqual(
            Counter(q["lesson_number"] for q in qs), {n: 4 for n in bank.LESSONS}
        )
        self.assertEqual(Counter(q["correct"] for q in qs), {i: 4 for i in range(4)})
        lessons = {l["lesson_number"]: l for l in arp_curriculum.get_course_lessons()}
        for q in qs:
            self.assertEqual(q["source_url"], lessons[q["lesson_number"]]["source_url"])
            self.assertEqual(len(q["options"]), 4)
            self.assertEqual(len(set(q["options"])), 4)
            self.assertEqual(len(q["option_feedback"]), 4)
            self.assertTrue(
                q["explanation"] and q["example"] and all(q["option_feedback"])
            )
            self.assertIn("not collected Noroff quiz content", q["source_kind"])
            self.assertNotIn("attempt=", json.dumps(q))
            self.assertNotIn("mod/quiz", q["source_url"])
        self.assertEqual(len({q["illustration"] for q in qs}), 4)
        for filename in {q["illustration"] for q in qs}:
            with Image.open(bank.ASSETS / filename) as im:
                self.assertEqual(im.format, "PNG")
                self.assertGreaterEqual(im.width, 1000)
                im.verify()
        notes = bank.revision_markdown("2.3")
        self.assertIn(bank.NOTICE, notes)
        self.assertEqual(notes.count("Practice answer:"), 4)
        self.assertIn("Option reasoning:", notes)
        self.assertIn("Example:", notes)
        self.assertEqual(len(bank.get_curated_questions()), 16)
        self.assertIn(bank.STATE_KEY, study_buddy_state.PERSIST_KEYS)

    def test_answers_feedback_switching_and_persistence(self):
        app = self.app()
        self.assertIn("Module Quiz Bank", [t.label for t in app.tabs])
        self.assertTrue(any(bank.NOTICE in x.value for x in app.info))
        uid = bank.get_questions()[0]["id"]
        q = bank.get_questions()[0]
        app.session_state["assessment_submissions"] = {}
        before = {}
        app.button(key=f"arp_bank_{uid}_check").click()
        self.run_app(app)
        self.assertIn(
            "Choose an answer before checking.", [x.value for x in app.warning]
        )
        app.radio(key=f"arp_bank_{uid}_answer").set_value(q["options"][1])
        app.text_area(key=f"arp_bank_{uid}_reason").set_value(
            "I need to explain evidence for this reader."
        )
        self.run_app(app)
        app.button(key=f"arp_bank_{uid}_check").click()
        self.run_app(app)
        self.assertTrue(any("Review the distinction" in x.value for x in app.warning))
        self.assertIn("Reasoning for every option", [e.label for e in app.expander])
        self.assertTrue(any(q["explanation"] in m.value for m in app.markdown))
        app.radio(key=f"arp_bank_{uid}_answer").set_value(q["options"][0])
        self.run_app(app)
        self.assertTrue(any("Your selection changed" in x.value for x in app.warning))
        app.button(key=f"arp_bank_{uid}_check").click()
        self.run_app(app)
        self.assertTrue(
            any("Correct for this practice" in x.value for x in app.success)
        )
        self.assertTrue(any("1/16 checked · 1 correct" in x.value for x in app.caption))
        app.selectbox(key="arp_bank_lesson").set_value("2.3")
        self.run_app(app)
        self.assertEqual(len(app.selectbox(key="arp_bank_question_2.3").options), 4)
        app.selectbox(key="arp_bank_question_2.3").set_value("arp-m2-practice-11")
        self.run_app(app)
        self.assertIsNone(app.radio(key="arp_bank_arp-m2-practice-11_answer").value)
        app.selectbox(key="arp_bank_lesson").set_value(None)
        self.run_app(app)
        self.assertEqual(app.radio(key=f"arp_bank_{uid}_answer").value, q["options"][0])
        self.assertEqual(app.session_state["assessment_submissions"], before)
        saved = json.loads(Path(".study_buddy_state.json").read_text())
        self.assertEqual(saved[bank.STATE_KEY][uid]["checked"], q["options"][0])
        self.assertIn("explain evidence", saved[bank.STATE_KEY][uid]["reason"])
        reloaded = self.app()
        self.assertEqual(
            reloaded.radio(key=f"arp_bank_{uid}_answer").value, q["options"][0]
        )
        self.assertTrue(
            any("1/16 checked · 1 correct" in x.value for x in reloaded.caption)
        )
        self.assertIn(
            "Download original practice notes with answers (English)",
            [d.label for d in app.get("download_button")],
        )

    def test_resolver_english_normal_strict_and_stale_reference(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Plain Markdown formats text. Execution requires an appropriate environment."
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
            q = bank.get_questions()[1]
            uid = q["id"]
            app.selectbox(key="arp_bank_question_all").set_value(uid)
            self.run_app(app)
            app.radio(key=f"arp_bank_{uid}_answer").set_value(q["options"][0])
            app.text_area(key=f"arp_bank_{uid}_reason").set_value(
                "I thought a code block automatically runs its code."
            )
            self.run_app(app)
            app.button(key=f"arp_bank_{uid}_check").click()
            self.run_app(app)
            app.button(key=f"arp_bank_{uid}_resolver").click()
            self.run_app(app)
            self.assertEqual(requests, [])
            self.assertEqual(
                app.session_state[f"{bank.RESOLVER_BASE}_source_pool"], "Lessons only"
            )
            self.assertEqual(
                app.session_state[f"{bank.RESOLVER_BASE}_scope"],
                "Specific lesson or outcome",
            )
            self.assertTrue(
                app.session_state[f"{bank.RESOLVER_BASE}_specific_source"].startswith(
                    "Lesson 2.1:"
                )
            )
            self.assertIn(
                "Original practice reference: reasoning and illustration",
                [e.label for e in app.expander],
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            )
            self.assertIn("I thought a code block", prompt.value)
            self.assertIn(q["options"][0], prompt.value)
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
            for r in requests:
                system, user = [m["content"] for m in r["messages"][:2]]
                self.assertIn("ANSWER LANGUAGE: Write in English", system)
                self.assertIn("Original ARP practice reference", user)
                self.assertIn(q["explanation"], user)
                self.assertIn("Option reasoning:", user)
                self.assertIn("I thought a code block", user)
                self.assertNotIn("current selected step:", user)
            self.assertIn(
                "not collected Noroff assessment content",
                requests[1]["messages"][0]["content"],
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            )
            prompt.set_value(
                prompt.value.replace(q["question"], "Explain an unrelated concept.")
            )
            self.run_app(app)
            self.assertNotIn(
                "Original practice reference: reasoning and illustration",
                [e.label for e in app.expander],
            )
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)

    def test_curated_simulator_uses_unique_original_questions(self):
        app = self.app("Exam Simulator")
        next(s for s in app.selectbox if s.label == "Select Course:").set_value(
            bank.COURSE_CODE
        )
        self.run_app(app)
        next(s for s in app.selectbox if s.label == "Curated Bank").set_value(
            "ARP Module 2 original practice"
        )
        next(s for s in app.multiselect if s.label == "Question Types:").set_value(
            ["General", "Knowledge-based", "Skills-based"]
        )
        next(
            s for s in app.number_input if s.label == "Number of Questions:"
        ).set_value(20)
        self.run_app(app)
        next(b for b in app.button if b.label == "🚀 Start Exam").click()
        self.run_app(app)
        qs = app.session_state["exam_questions"]
        self.assertEqual(len(qs), 16)
        self.assertEqual(len({q["question"] for q in qs}), 16)
        self.assertTrue(all("[ARP original practice /" in q["question"] for q in qs))
        self.assertTrue(all("ANSWER:" in q["question"] for q in qs))


if __name__ == "__main__":
    unittest.main()
