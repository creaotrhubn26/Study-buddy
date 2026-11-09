"""Verify the supplied Nice Ride data, native learning files and Resolver workflow."""

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import csv
import json
import os
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import arp_curriculum as curriculum
import arp_lesson21
import arp_lesson22 as lesson
import arp_ui
import test_arp_lesson11 as helpers


class ARPLesson22Tests(unittest.TestCase):
    setUp = helpers.ARPLesson11Tests.setUp
    tearDown = helpers.ARPLesson11Tests.tearDown
    run_app = helpers.ARPLesson11Tests.run_app
    app = helpers.ARPLesson11Tests.app

    def test_source_scope_templates_native_chart_and_word_structure(self):
        self.assertEqual(
            [g["lesson_number"] for g in curriculum.all_task_guides()],
            ["1.1", "1.2", "1.3", "1.4", "2.1", "2.2"],
        )
        self.assertEqual(
            lesson.DATA_ROWS,
            [
                ("Mercedes", 220),
                ("Audi", 180),
                ("Volkswagen", 150),
                ("Skoda", 130),
                ("Volvo", 100),
                ("Tesla", 85),
            ],
        )
        self.assertEqual(lesson.TOTAL, 865)
        self.assertEqual(len(lesson.STEPS), 7)
        self.assertTrue(lesson.LESSON_URL.endswith("id=22937&chapterid=81722"))
        self.assertTrue(lesson.TASK_URL.endswith("id=22937&chapterid=81727"))
        for text in [
            "MS Word report",
            "heading styles",
            "following the plot",
            "vertical columns",
            "No reporting period",
            "no word count",
            "not a linked Excel object",
            "chocolate-bar workbook",
        ]:
            self.assertIn(text, lesson.BOUNDARY)
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / lesson.GUIDE["template_file"]).read_text(),
            lesson.QUESTION_TEMPLATE,
        )
        self.assertEqual(
            (lesson.TEMPLATE_ROOT / "ARP Task 2.2 Seven Step Guide.md").read_text(),
            lesson.guide_markdown(),
        )
        with (lesson.TEMPLATE_ROOT / "ARP Task 2.2 Nice Ride Data.csv").open() as f:
            rows = list(csv.reader(f))
        self.assertEqual(
            rows, [["Brand", "Cars sold"]] + [[b, str(n)] for b, n in lesson.DATA_ROWS]
        )
        with (
            lesson.TEMPLATE_ROOT / "ARP Task 2.2 Verification Checklist.csv"
        ).open() as f:
            checks = list(csv.DictReader(f))
        self.assertEqual(len(checks), 7)
        self.assertTrue(
            all(
                r["Status"] == "Not checked" and not r["My observed evidence"]
                for r in checks
            )
        )
        ns = {
            "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
            "s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
        }
        with ZipFile(
            lesson.TEMPLATE_ROOT / "ARP Task 2.2 Nice Ride Workbook.xlsx"
        ) as z:
            charts = [
                n for n in z.namelist() if "/charts/chart" in n and n.endswith(".xml")
            ]
            self.assertEqual(len(charts), 1)
            chart = ET.fromstring(z.read(charts[0]))
            self.assertEqual(chart.find(".//c:barDir", ns).get("val"), "col")
            self.assertEqual(chart.find(".//c:grouping", ns).get("val"), "clustered")
            formulas = [x.text for x in chart.findall(".//c:f", ns)]
            self.assertIn("'Nice Ride'!$C$10:$C$15", formulas)
            self.assertIn("'Nice Ride'!$B$10:$B$15", formulas)
            self.assertTrue(all("C4" not in f for f in formulas))
            sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
            values = {
                c.get("r"): c.find("s:v", ns).text
                for c in sheet.findall(".//s:c", ns)
                if c.find("s:v", ns) is not None
            }
            self.assertEqual(
                [int(values[f"C{i}"]) for i in range(10, 16)],
                [n for _, n in lesson.DATA_ROWS],
            )
            self.assertEqual(float(values["C4"]), 865)
            self.assertEqual(float(values["C6"]), 220)
        wn = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        with ZipFile(
            lesson.TEMPLATE_ROOT / "ARP Task 2.2 Nice Ride Report Template.docx"
        ) as z:
            root = ET.fromstring(z.read("word/document.xml"))
            styles = ET.fromstring(z.read("word/styles.xml"))
            self.assertFalse(styles.findall(".//w:pBdr", wn))
            paragraphs = root.findall(".//w:body/w:p", wn)
            text = ["".join(p.itertext()) for p in paragraphs]
            names = [
                p.find("w:pPr/w:pStyle", wn).get("{" + wn["w"] + "}val")
                for p in paragraphs
                if p.find("w:pPr/w:pStyle", wn) is not None
            ]
            self.assertIn("Title", names)
            self.assertGreaterEqual(names.count("Heading1"), 3)
            picture = next(
                i
                for i, p in enumerate(paragraphs)
                if p.find(".//w:drawing", wn) is not None
            )
            comment = next(
                i for i, t in enumerate(text) if "Write a short comment here" in t
            )
            self.assertGreater(comment, picture)
            self.assertTrue(any(n.startswith("word/media/") for n in z.namelist()))
        for v in lesson.ILLUSTRATIONS:
            self.assertTrue(
                (lesson.ASSET_ROOT / v["file"]).read_bytes().startswith(b"\x89PNG")
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
            ["2.1", "2.2"],
        )
        self.assertEqual(
            modules["ARP Module 2: Report-Generating Tools"]["exercises"][0]["title"],
            "Task 2.1 Source reliability",
        )

    def test_handoff_regular_strict_ai_draft_step_and_staleness(self):
        requests = []

        def complete(**kw):
            requests.append(kw)
            return iter(
                [
                    SimpleNamespace(
                        choices=[
                            SimpleNamespace(
                                delta=SimpleNamespace(
                                    content="Mercedes has the highest supplied count. Check the six vertical columns and put your comment after the plot."
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
                "📚 Lesson 2.2: Creating Full-length Reports",
                [e.label for e in app.expander],
            )
            note = "Mercedes leads with 220 cars and Audi has 180. I have not yet checked the saved Word headings or whether my short comment follows the chart."
            next(
                t
                for t in app.text_area
                if t.label == "Your Nice Ride report draft and file checks"
            ).set_value(note)
            next(
                s for s in app.selectbox if s.label == "Choose a Task 2.2 step"
            ).set_value(5)
            self.run_app(app)
            self.assertEqual(
                arp_ui.draft(app.session_state, arp_lesson21.GUIDE),
                arp_lesson21.QUESTION_TEMPLATE,
            )
            next(
                b for b in app.button if b.label == "Prepare Task 2.2 in Exam Resolver"
            ).click()
            self.run_app(app)
            self.assertEqual(requests, [])
            self.assertTrue(
                any(
                    "Auto-detected question style:** Data report with a column chart"
                    in m.value
                    for m in app.markdown
                )
            )
            prompt = next(
                t
                for t in app.text_area
                if t.label == "Paste the exam question, case, or task prompt"
            ).value
            self.assertIn("ARP Task 2.2:", prompt)
            self.assertIn(note, prompt)
            controls = [
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label.startswith("Choose a Task")
            ]
            self.assertEqual(
                [(s.label, s.value) for s in controls], [("Choose a Task 2.2 step", 5)]
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
                for text in [
                    "Nice Ride",
                    "Mercedes 220",
                    "Audi 180",
                    "Volkswagen 150",
                    "Skoda 130",
                    "Volvo 100",
                    "Tesla 85",
                    "865",
                    "following the plot",
                    "no word count",
                    "not a linked Excel object",
                ]:
                    self.assertIn(text, system)
                    self.assertIn(text, user)
                self.assertIn(
                    "current selected step: 6. Write the short comment immediately after the plot",
                    user,
                )
                self.assertIn(note, user)
                self.assertNotIn("NaturalNews", user)
                self.assertNotIn("45892", user)
                self.assertNotIn("handmade-candle business", user)
            signature = arp_ui.workflow_signature(app.session_state)
            next(
                s
                for s in app.selectbox
                if (s.key or "").startswith(arp_ui.RESOLVER_BASE)
                and s.label == "Choose a Task 2.2 step"
            ).set_value(6)
            self.run_app(app)
            self.assertNotEqual(signature, arp_ui.workflow_signature(app.session_state))
            self.assertIn("Previous AI answer", [e.label for e in app.expander])
            self.assertEqual(len(requests), 2)
            saved = json.loads(Path(".study_buddy_state.json").read_text())
            self.assertEqual(saved["arp_task_drafts"][lesson.GUIDE["uid"]], note)
            self.assertEqual(saved["arp_task_steps"][lesson.GUIDE["uid"]], 6)
            self.assertTrue(
                all(
                    s.value == 0
                    for s in app.selectbox
                    if s.label in ["Choose a Task 2.1 step", "Choose a Task 1.4 step"]
                )
            )

    def test_training_downloads_and_previous_lesson(self):
        app = self.app("Training Center")
        next(s for s in app.selectbox if s.label == "🎯 Select Topic:").set_value(
            "ARP Module 2: Report-Generating Tools"
        )
        self.run_app(app)
        for num in ["2.1", "2.2"]:
            self.assertIn(
                f"Prepare Task {num} in Exam Resolver", [b.label for b in app.button]
            )
        for _, label, _ in lesson.DOWNLOADS:
            self.assertIn(label, [d.label for d in app.get("download_button")])
        self.assertNotIn(
            "Prepare Task 1.4 in Exam Resolver", [b.label for b in app.button]
        )


if __name__ == "__main__":
    unittest.main()
